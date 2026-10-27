// Gọi Google Sheets, Docs, Drive bằng service account. Không cần thư viện ngoài.
// Cách làm giống scripts/sheets/google.ts của repo e2e của dự án: tự ký JWT, đổi lấy token, gọi REST.
//
// Khóa service account: --key <đường dẫn file JSON>, hoặc biến môi trường GOOGLE_SA_KEY_FILE.
// File Google phải được chia sẻ quyền Người chỉnh sửa (Editor) cho email của service account.
// <file> nhận cả link docs.google.com lẫn ID.
//
// Lệnh:
//   whoami                                  In email service account (để chia sẻ file)
//   info <file>                             Tên, loại, link của file
//   list <thư mục>                          Liệt kê file trong thư mục Drive
//   export <file> <đường dẫn ra>            Tải file về: .docx .pdf .xlsx .md .txt
//
//   sheet-tabs <file>                       Danh sách tab
//   sheet-read <file> <vùng>                Đọc ô, ví dụ "Tab 1!A1:J50". In JSON
//   sheet-write <file> <vùng> <json>        Ghi ô. <json> là mảng 2 chiều, hoặc đường dẫn file .json
//   sheet-append <file> <vùng> <json>       Thêm dòng vào cuối bảng
//   sheet-add-tab <file> <tên tab>          Thêm tab mới
//   sheet-batch <file> <requests.json>      Gửi lô yêu cầu batchUpdate của Sheets API (công thức, danh sách chọn, màu, định dạng)
//   sheet-info <file>                       Id từng tab và các quy tắc định dạng có điều kiện, danh sách chọn đang có
//   drive-list <thư mục>                    Liệt kê tệp trong thư mục Drive (id, tên, link xem). Thư mục phải chia sẻ cho service account
//   drive-get <file> <đường dẫn ra>         Tải tệp thường trên Drive (ảnh, pdf...) về máy
//   (thêm --nhap-nhu-tay để Google tự hiểu số, ngày, công thức như khi gõ tay. Mặc định ghi nguyên văn)
//
//   doc-read <file> [--json <đường dẫn>]    In nội dung Google Doc dạng chữ, mỗi đoạn một dòng có số thứ tự
//   doc-replace <file> <chữ cũ> <chữ mới> [--tat-ca]
//                                           Thay chữ. Chữ cũ phải xuất hiện đúng 1 lần, trừ khi có --tat-ca
//   doc-insert-after <file> <chữ trong đoạn mốc> <đoạn mới>
//                                           Chèn một đoạn mới ngay sau đoạn có chứa chữ mốc (mốc phải duy nhất)
//   doc-batch <file> <requests.json>        Gửi lô yêu cầu batchUpdate của Docs API, có khóa revision
//
//   comments <file> [--ra <file.md>]        Liệt kê comment, xếp theo vị trí trong tài liệu
//   comment-reply <file> <id comment> <nội dung>
import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'node:fs';
import { createSign } from 'node:crypto';
import { dirname, extname, resolve } from 'node:path';

const SCOPES = [
  'https://www.googleapis.com/auth/spreadsheets',
  'https://www.googleapis.com/auth/documents',
  'https://www.googleapis.com/auth/drive',
].join(' ');

function fail(msg) {
  throw new Error(msg);
}

// ---------- tham số ----------
const argv = process.argv.slice(2);
const flags = {};
const pos = [];
for (let i = 0; i < argv.length; i++) {
  const a = argv[i];
  if (a === '--key' || a === '--json' || a === '--ra') flags[a.slice(2)] = argv[++i];
  else if (a.startsWith('--')) flags[a.slice(2)] = true;
  else pos.push(a);
}
const [cmd, ...args] = pos;

function fileId(s) {
  if (!s) fail('Thiếu link hoặc ID file.');
  const m = s.match(/\/(?:d|folders)\/([a-zA-Z0-9_-]+)/) || s.match(/[?&]id=([a-zA-Z0-9_-]+)/);
  return m ? m[1] : s;
}

function loadKey() {
  const p = flags.key || process.env.GOOGLE_SA_KEY_FILE;
  if (!p) fail('Chưa chỉ đường dẫn khóa service account (--key hoặc GOOGLE_SA_KEY_FILE).');
  if (!existsSync(p)) fail('Không thấy file khóa: ' + p);
  const key = JSON.parse(readFileSync(p, 'utf8'));
  if (!key.client_email || !key.private_key) fail('File khóa không đúng dạng khóa service account.');
  return key;
}

// ---------- token ----------
let token = '';
async function accessToken() {
  if (token) return token;
  const key = loadKey();
  const now = Math.floor(Date.now() / 1000);
  const b64 = (o) => Buffer.from(JSON.stringify(o)).toString('base64url');
  const unsigned = `${b64({ alg: 'RS256', typ: 'JWT' })}.${b64({
    iss: key.client_email, scope: SCOPES, aud: 'https://oauth2.googleapis.com/token', iat: now, exp: now + 3600,
  })}`;
  const sig = createSign('RSA-SHA256').update(unsigned).sign(key.private_key, 'base64url');
  const res = await fetch('https://oauth2.googleapis.com/token', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({ grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer', assertion: `${unsigned}.${sig}` }),
  });
  const json = await res.json();
  if (!json.access_token) fail('Không lấy được quyền truy cập: ' + (json.error_description || json.error || res.status));
  token = json.access_token;
  return token;
}

async function api(url, { method = 'GET', body, raw = false } = {}) {
  const res = await fetch(url, {
    method,
    headers: { Authorization: `Bearer ${await accessToken()}`, ...(body ? { 'Content-Type': 'application/json' } : {}) },
    body: body ? JSON.stringify(body) : undefined,
  });
  if (!res.ok) {
    let msg = `${res.status}`;
    try { msg += ' ' + ((await res.json()).error?.message ?? ''); } catch { /* bỏ qua */ }
    if (res.status === 403 || res.status === 404) msg += '\nKiểm tra: file đã chia sẻ quyền Người chỉnh sửa cho email service account chưa (lệnh whoami), API tương ứng đã bật trong Google Cloud chưa.';
    fail(msg);
  }
  return raw ? Buffer.from(await res.arrayBuffer()) : res.json();
}

const DRIVE = 'https://www.googleapis.com/drive/v3/files';
const SHEETS = 'https://sheets.googleapis.com/v4/spreadsheets';
const DOCS = 'https://docs.googleapis.com/v1/documents';
const out = (o) => console.log(typeof o === 'string' ? o : JSON.stringify(o, null, 2));

function jsonArg(s) {
  if (!s) fail('Thiếu dữ liệu JSON.');
  const txt = existsSync(s) ? readFileSync(s, 'utf8') : s;
  try { return JSON.parse(txt); } catch { fail('Dữ liệu không phải JSON hợp lệ.'); }
}

// ---------- Docs: đọc thành các đoạn ----------
function paragraphs(doc) {
  const list = [];
  const walk = (content) => {
    for (const el of content || []) {
      if (el.paragraph) {
        const text = (el.paragraph.elements || []).map((e) => e.textRun?.content ?? '').join('');
        list.push({ start: el.startIndex, end: el.endIndex, text: text.replace(/\n$/, ''), style: el.paragraph.paragraphStyle?.namedStyleType });
      } else if (el.table) {
        for (const row of el.table.tableRows) for (const cell of row.tableCells) walk(cell.content);
      }
    }
  };
  walk(doc.body.content);
  return list;
}

function countIn(doc, needle) {
  return paragraphs(doc).reduce((n, p) => n + p.text.split(needle).length - 1, 0);
}

async function docBatch(id, requests) {
  const doc = await api(`${DOCS}/${id}`);
  return api(`${DOCS}/${id}:batchUpdate`, {
    method: 'POST', body: { requests, writeControl: { requiredRevisionId: doc.revisionId } },
  });
}

// ---------- lệnh ----------
const EXPORT = {
  '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
  '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
  '.pdf': 'application/pdf', '.md': 'text/markdown', '.txt': 'text/plain', '.csv': 'text/csv',
};

const commands = {
  async whoami() { out(loadKey().client_email); },

  async info() {
    out(await api(`${DRIVE}/${fileId(args[0])}?fields=id,name,mimeType,webViewLink,modifiedTime&supportsAllDrives=true`));
  },

  async list() {
    const q = encodeURIComponent(`'${fileId(args[0])}' in parents and trashed=false`);
    const r = await api(`${DRIVE}?q=${q}&fields=files(id,name,mimeType,webViewLink,modifiedTime)&pageSize=200&supportsAllDrives=true&includeItemsFromAllDrives=true`);
    out(r.files);
  },

  async export() {
    const [f, dest] = args;
    const mime = EXPORT[extname(dest || '').toLowerCase()];
    if (!mime) fail('Đuôi file ra phải là ' + Object.keys(EXPORT).join(', '));
    const buf = await api(`${DRIVE}/${fileId(f)}/export?mimeType=${encodeURIComponent(mime)}`, { raw: true });
    mkdirSync(dirname(resolve(dest)), { recursive: true });
    writeFileSync(dest, buf);
    out('Đã tải: ' + resolve(dest));
  },

  async 'drive-get'() {
    const [f, dest] = args;
    if (!dest) fail('Cần đường dẫn ra');
    const buf = await api(`${DRIVE}/${fileId(f)}?alt=media&supportsAllDrives=true`, { raw: true });
    mkdirSync(dirname(resolve(dest)), { recursive: true });
    writeFileSync(dest, buf);
    out('Đã tải: ' + resolve(dest));
  },

  async 'sheet-tabs'() {
    const r = await api(`${SHEETS}/${fileId(args[0])}?fields=properties.title,sheets.properties`);
    out({ title: r.properties.title, tabs: r.sheets.map((s) => ({ id: s.properties.sheetId, title: s.properties.title, rows: s.properties.gridProperties.rowCount, cols: s.properties.gridProperties.columnCount })) });
  },

  async 'sheet-read'() {
    const r = await api(`${SHEETS}/${fileId(args[0])}/values/${encodeURIComponent(args[1])}`);
    out(r.values || []);
  },

  async 'sheet-write'() {
    const opt = flags['nhap-nhu-tay'] ? 'USER_ENTERED' : 'RAW';
    const r = await api(`${SHEETS}/${fileId(args[0])}/values/${encodeURIComponent(args[1])}?valueInputOption=${opt}`, {
      method: 'PUT', body: { values: jsonArg(args[2]) },
    });
    out(`Đã ghi ${r.updatedCells ?? 0} ô ở ${r.updatedRange}`);
  },

  async 'sheet-append'() {
    const opt = flags['nhap-nhu-tay'] ? 'USER_ENTERED' : 'RAW';
    const r = await api(`${SHEETS}/${fileId(args[0])}/values/${encodeURIComponent(args[1])}:append?valueInputOption=${opt}&insertDataOption=INSERT_ROWS`, {
      method: 'POST', body: { values: jsonArg(args[2]) },
    });
    out(`Đã thêm ${r.updates?.updatedRows ?? 0} dòng ở ${r.updates?.updatedRange}`);
  },

  async 'sheet-batch'() {
    const r = await api(`${SHEETS}/${fileId(args[0])}:batchUpdate`, { method: 'POST', body: { requests: jsonArg(args[1]) } });
    out(`Đã gửi ${r.replies.length} yêu cầu.`);
  },

  async 'sheet-info'() {
    const r = await api(`${SHEETS}/${fileId(args[0])}?fields=properties(title,locale),sheets(properties(sheetId,title),conditionalFormats(ranges,booleanRule(condition)))`);
    out({ locale: r.properties.locale, tabs: r.sheets.map((t) => ({ id: t.properties.sheetId, title: t.properties.title, soQuyTacMau: (t.conditionalFormats || []).length })) });
  },

  async 'drive-list'() {
    const id = fileId(args[0]);
    const r = await api(`${DRIVE}?q=${encodeURIComponent(`'${id}' in parents and trashed=false`)}&fields=files(id,name,mimeType,webViewLink)&pageSize=200&orderBy=name&supportsAllDrives=true&includeItemsFromAllDrives=true`);
    out(r.files);
  },

  async 'sheet-add-tab'() {
    const r = await api(`${SHEETS}/${fileId(args[0])}:batchUpdate`, {
      method: 'POST', body: { requests: [{ addSheet: { properties: { title: args[1] } } }] },
    });
    out(`Đã thêm tab "${args[1]}" (id ${r.replies[0].addSheet.properties.sheetId})`);
  },

  async 'doc-read'() {
    const doc = await api(`${DOCS}/${fileId(args[0])}`);
    if (flags.json) { writeFileSync(flags.json, JSON.stringify(doc)); }
    const lines = [`# ${doc.title}  (revision ${doc.revisionId})`];
    paragraphs(doc).forEach((p, i) => { if (p.text.trim()) lines.push(`[${i}] ${p.style?.startsWith('HEADING') ? '## ' : ''}${p.text}`); });
    out(lines.join('\n'));
  },

  async 'doc-replace'() {
    const [f, oldText, newText] = args;
    if (!oldText || newText === undefined) fail('Cần <chữ cũ> <chữ mới>.');
    const id = fileId(f);
    const doc = await api(`${DOCS}/${id}`);
    const n = countIn(doc, oldText);
    if (n === 0) fail('Không tìm thấy chữ cần thay.');
    if (n > 1 && !flags['tat-ca']) fail(`Chữ cần thay xuất hiện ${n} lần. Viết dài hơn cho duy nhất, hoặc thêm --tat-ca.`);
    const r = await docBatch(id, [{ replaceAllText: { containsText: { text: oldText, matchCase: true }, replaceText: newText } }]);
    out(`Đã thay ${r.replies[0].replaceAllText?.occurrencesChanged ?? 0} chỗ.`);
  },

  async 'doc-insert-after'() {
    const [f, anchor, text] = args;
    if (!anchor || !text) fail('Cần <chữ trong đoạn mốc> <đoạn mới>.');
    const id = fileId(f);
    const doc = await api(`${DOCS}/${id}`);
    const hits = paragraphs(doc).filter((p) => p.text.includes(anchor));
    if (hits.length !== 1) fail(`Đoạn mốc phải duy nhất, đang có ${hits.length} đoạn khớp.`);
    await docBatch(id, [{ insertText: { location: { index: hits[0].end - 1 }, text: '\n' + text } }]);
    out('Đã chèn đoạn mới sau: ' + hits[0].text.slice(0, 80));
  },

  async 'doc-batch'() {
    const r = await docBatch(fileId(args[0]), jsonArg(args[1]));
    out(`Đã gửi ${r.replies.length} yêu cầu.`);
  },

  async comments() {
    const id = fileId(args[0]);
    const all = [];
    let page = '';
    do {
      const r = await api(`${DRIVE}/${id}/comments?fields=nextPageToken,comments(id,content,author/displayName,resolved,quotedFileContent/value,createdTime,replies(content,author/displayName))&pageSize=100${page ? '&pageToken=' + page : ''}`);
      all.push(...r.comments);
      page = r.nextPageToken;
    } while (page);
    // xếp theo vị trí đoạn được comment trong tài liệu (Drive API không trả số trang)
    let text = '';
    try { text = paragraphs(await api(`${DOCS}/${id}`)).map((p) => p.text).join('\n'); } catch { /* không phải Google Doc */ }
    const posOf = (c) => { const q = c.quotedFileContent?.value; const i = q ? text.indexOf(q.split('\n')[0]) : -1; return i < 0 ? Infinity : i; };
    all.sort((a, b) => posOf(a) - posOf(b));
    const esc = (s) => (s || '').replace(/\|/g, '\\|').replace(/\n/g, '<br>');
    const rows = ['| # | ID comment | Đoạn được comment | Người comment | Nội dung và trả lời | Trạng thái |', '|---|---|---|---|---|---|'];
    all.forEach((c, i) => {
      const body = esc(c.content) + (c.replies || []).map((r) => `<br>↳ **${esc(r.author?.displayName)}:** ${esc(r.content)}`).join('');
      rows.push(`| ${i + 1} | ${c.id} | ${esc(c.quotedFileContent?.value).slice(0, 200)} | ${esc(c.author?.displayName)} | ${body} | ${c.resolved ? 'Đã xong' : 'Còn mở'} |`);
    });
    const md = `# Comment trên tài liệu\n\nTổng ${all.length} luồng, ${all.filter((c) => !c.resolved).length} luồng còn mở. Xếp theo vị trí trong tài liệu.\n\n${rows.join('\n')}\n`;
    if (flags.ra) { writeFileSync(flags.ra, md); out('Đã ghi: ' + resolve(flags.ra)); } else out(md);
  },

  async 'comment-reply'() {
    const [f, cid, text] = args;
    if (!cid || !text) fail('Cần <id comment> <nội dung>.');
    await api(`${DRIVE}/${fileId(f)}/comments/${cid}/replies?fields=id`, { method: 'POST', body: { content: text } });
    out('Đã trả lời comment ' + cid);
  },
};

if (!cmd || !commands[cmd]) {
  console.log(readFileSync(new URL(import.meta.url), 'utf8').split('\n').filter((l) => l.startsWith('//')).map((l) => l.slice(3)).join('\n'));
  process.exit(cmd ? 1 : 0);
}
try {
  await commands[cmd]();
} catch (e) {
  console.error('LỖI: ' + e.message);
  process.exitCode = 1;
}
