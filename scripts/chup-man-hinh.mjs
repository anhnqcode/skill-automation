// Chụp một màn hình của bản thiết kế đang chạy dev.
// Chạy từ thư mục repo thiết kế (nơi có node_modules/playwright):
//   node "<Skill BA>/scripts/chup-man-hinh.mjs" <url> <file.png> [--selector "<css>"] [--click "<css>"]
//        [--width 1440] [--height 900] [--full] [--wait 800]
// --click có thể lặp lại, bấm lần lượt trước khi chụp (mở popup, chuyển tab...).
// --selector: chỉ chụp phần tử đó thay vì cả trang.
import { createRequire } from 'node:module';
import { mkdirSync } from 'node:fs';
import { dirname } from 'node:path';

const require = createRequire(process.cwd() + '/');
const { chromium } = require('playwright');

const [url, out, ...rest] = process.argv.slice(2);
if (!url || !out) {
  console.error('Thiếu tham số. Cách dùng: node chup-man-hinh.mjs <url> <file.png> [tùy chọn]');
  process.exit(1);
}

const opt = { width: 1440, height: 900, wait: 800, full: false, selector: null, clicks: [] };
for (let i = 0; i < rest.length; i++) {
  const k = rest[i];
  if (k === '--full') opt.full = true;
  else if (k === '--click') opt.clicks.push(rest[++i]);
  else if (k === '--selector') opt.selector = rest[++i];
  else if (k === '--width') opt.width = Number(rest[++i]);
  else if (k === '--height') opt.height = Number(rest[++i]);
  else if (k === '--wait') opt.wait = Number(rest[++i]);
}

mkdirSync(dirname(out), { recursive: true });
const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: opt.width, height: opt.height } });
await page.goto(url);
await page.waitForLoadState('networkidle');
await page.waitForTimeout(opt.wait);

for (const sel of opt.clicks) {
  await page.locator(sel).first().click();
  await page.waitForTimeout(opt.wait);
}

if (opt.selector) {
  await page.locator(opt.selector).first().screenshot({ path: out });
} else {
  await page.screenshot({ path: out, fullPage: opt.full });
}
console.log('Đã chụp: ' + out);
await browser.close();
