"""Bo ham dung chung cho skill verify-bug: chay trinh duyet co giao dien, cham, hien dai chu bao bug dang kiem,
do dac cu the tren trang (chu, kich thuoc, vi tri, mau, gia tri) thay vi chi nhin anh.

Chep vao thu muc Automation cua du an thanh verify_chung.py, hoac import thang tu Skill BA.

Gom:
- mo(p, xem=False, kho=(1920, 1080), cham=500)  mo trinh duyet. Mac dinh chay ngam; xem=True (chi khi nguoi dung yeu cau): co giao dien, chay cham, kho 1920x1080
- dai_chu(page, bug, buoc="", trang_thai="dang")   hien dai chu tren cung trang: bug dang kiem, buoc dang lam, ket qua
- do(page, bo_chon)        do mot phan tu: co hien, chu, gia tri, khung (x, y, rong, cao), co chu, mau, nen, tran chu
- do_nhieu(page, bo_chon)  do moi phan tu khop bo chon (so luong, chu tung phan tu)
- so_sanh(ten, thuc_te, mong_muon, cach="bang")    so mot chi so, tra ve dong ket qua co Dat/Khong dat
- doi_kho(page, rong, cao)  doi kich thuoc khung nhin khi kiem man responsive
- chup(page, duong_dan)     chup bang chung o ti le 2x, an dai chu truoc khi chup
- gan_canh_gac(ctx)         theo doi link duoc bam (co thuoc tinh download khong), window.open, print; mo() tu gan
- kiem_tai(page, bam, duong_dan)  bam nut tai / xuat / in roi kiem: co tep tai ve that, khong roi trang, khong mo tab la, khong link blob thieu download
- kiem_bo_cuc(page)         do bo cuc: nut trung, tieu de cot xuong dong, cot rong noi dung ngan, khoang trang lon giua cot, chu bang nho

Chay ngam dung Chrome day du (channel="chromium"), khong dung headless-shell rut gon. Xem muc 8 cua viet-automation/kiem-thu-chua-co-testcase.md.
"""
import json
import re

MAU_DAI = {"dang": "#1f4e79", "dat": "#1e7b34", "khong-dat": "#b42318", "chua-ro": "#8a6d00"}

_DAI_JS = r"""
([chu, mau]) => {
  let d = document.getElementById('__verify_bug_dai');
  if (!d) {
    d = document.createElement('div');
    d.id = '__verify_bug_dai';
    d.style.cssText = 'position:fixed;top:0;left:0;right:0;z-index:2147483647;padding:10px 18px;'
      + 'font:600 18px/1.4 Segoe UI,Arial,sans-serif;color:#fff;box-shadow:0 2px 8px rgba(0,0,0,.3);'
      + 'pointer-events:none;white-space:pre-line';
    document.documentElement.appendChild(d);
  }
  d.style.background = mau;
  d.textContent = chu;
}
"""

_DO_JS = r"""
(el) => {
  const r = el.getBoundingClientRect();
  const s = getComputedStyle(el);
  return {
    hien: !!(r.width || r.height) && s.visibility !== 'hidden' && s.display !== 'none',
    chu: (el.innerText || '').trim(),
    gia_tri: ('value' in el) ? el.value : null,
    x: Math.round(r.x), y: Math.round(r.y), rong: Math.round(r.width), cao: Math.round(r.height),
    co_chu: s.fontSize, dam: s.fontWeight, mau: s.color, nen: s.backgroundColor,
    vien: s.borderColor, can_le: s.textAlign, an_tran: s.overflow,
    tran_ngang: el.scrollWidth > el.clientWidth + 1,
    bi_khoa: el.disabled === true || el.getAttribute('aria-disabled') === 'true',
  };
}
"""

_trang_thai_dai = {}


def mo(p, xem=False, kho=(1920, 1080), cham=500, trinh_duyet="chromium"):
    """Mo trinh duyet. xem=True: co giao dien, cham, cua so dung kho. Tra ve (browser, context, page)."""
    # Chay ngam dung Chrome day du (channel="chromium", headless moi), khong dung headless-shell rut gon:
    # ban rut gon khong co trinh xem PDF, xu ly tai tep, mo tab, in khac Chrome that nen giau loi.
    kw = dict(headless=not xem, slow_mo=cham if xem else 0, args=[f"--window-size={kho[0]},{kho[1]}"] if xem else [])
    if trinh_duyet == "chromium":
        kw["channel"] = "chromium"
    b = getattr(p, trinh_duyet).launch(**kw)
    ctx = b.new_context(viewport={"width": kho[0], "height": kho[1]}, device_scale_factor=1, accept_downloads=True)
    ctx.set_default_timeout(10000)  # buoc loi bao sau 10 giay, khong treo 30 giay mac dinh
    ctx.set_default_navigation_timeout(30000)
    gan_canh_gac(ctx)
    page = ctx.new_page()
    # giu dai chu khi trang chuyen sang trang khac
    page.on("load", lambda _: _ve_lai_dai(page))
    return b, ctx, page


def _ve_lai_dai(page):
    if page in _trang_thai_dai:
        try:
            page.evaluate(_DAI_JS, list(_trang_thai_dai[page]))
        except Exception:
            pass


def dai_chu(page, bug, buoc="", trang_thai="dang"):
    """bug: chuoi kieu 'Bug #12 - [Quan tri][Chien dich] Nut Luu bi khoa'. trang_thai: dang / dat / khong-dat / chua-ro."""
    nhan = {"dang": "ĐANG KIỂM", "dat": "ĐẠT", "khong-dat": "KHÔNG ĐẠT", "chua-ro": "CHƯA KẾT LUẬN"}[trang_thai]
    chu = f"{nhan} | {bug}" + (f"\n{buoc}" if buoc else "")
    _trang_thai_dai[page] = (chu, MAU_DAI[trang_thai])
    page.evaluate(_DAI_JS, [chu, MAU_DAI[trang_thai]])


def do(page, bo_chon):
    """Do phan tu dau tien khop bo chon. Khong co thi tra ve {'co': False}."""
    loc = page.locator(bo_chon).first
    if loc.count() == 0:
        return {"co": False, "bo_chon": bo_chon}
    kq = loc.evaluate(_DO_JS)
    kq.update({"co": True, "bo_chon": bo_chon})
    return kq


def do_nhieu(page, bo_chon):
    loc = page.locator(bo_chon)
    return {"bo_chon": bo_chon, "so_luong": loc.count(), "chu": [t.strip() for t in loc.all_inner_texts()]}


def so_sanh(ten, thuc_te, mong_muon, cach="bang"):
    """cach: bang / chua (thuc_te chua mong_muon) / khong-chua / nho-hon-bang / lon-hon-bang."""
    ok = {
        "bang": thuc_te == mong_muon,
        "chua": str(mong_muon) in str(thuc_te),
        "khong-chua": str(mong_muon) not in str(thuc_te),
        "nho-hon-bang": thuc_te is not None and thuc_te <= mong_muon,
        "lon-hon-bang": thuc_te is not None and thuc_te >= mong_muon,
    }[cach]
    return {"chi_so": ten, "thuc_te": thuc_te, "mong_muon": mong_muon, "cach": cach, "dat": bool(ok)}


def doi_kho(page, rong, cao):
    page.set_viewport_size({"width": rong, "height": cao})
    page.wait_for_timeout(300)


def chup(page, duong_dan, toan_trang=False):
    """Chup bang chung. An dai chu luc chup de anh gon, chup xong hien lai."""
    page.evaluate("() => { const d = document.getElementById('__verify_bug_dai'); if (d) d.style.display = 'none'; }")
    page.screenshot(path=duong_dan, full_page=toan_trang)
    page.evaluate("() => { const d = document.getElementById('__verify_bug_dai'); if (d) d.style.display = ''; }")
    return duong_dan


def in_ket_qua(bug_id, cac_so_sanh):
    """In mot dong JSON cho moi bug de buoc sau doc lai."""
    dat = all(x["dat"] for x in cac_so_sanh)
    print(json.dumps({"bug": bug_id, "dat": dat, "chi_tiet": cac_so_sanh}, ensure_ascii=False))
    return dat


# ------------------------------------------------------------------ canh gac khac biet chay ngam / trinh duyet that
_CANH_GAC_JS = r"""
(() => {
  if (window.__canh_gac) return;
  window.__canh_gac = [];
  const ghi = (x) => { try { window.__canh_gac.push(x); if (window.__bao_canh_gac) window.__bao_canh_gac(x); } catch (e) {} };
  const oc = HTMLAnchorElement.prototype.click;
  HTMLAnchorElement.prototype.click = function () {
    ghi({loai: 'link', href: String(this.href || '').slice(0, 60), download: this.hasAttribute('download') ? (this.download || '(rong)') : null, target: this.target || ''});
    return oc.apply(this, arguments);
  };
  document.addEventListener('click', (e) => {
    const a = e.target && e.target.closest && e.target.closest('a[href]');
    if (a) ghi({loai: 'link', href: String(a.href).slice(0, 60), download: a.hasAttribute('download') ? (a.download || '(rong)') : null, target: a.target || ''});
  }, true);
  const oo = window.open;
  window.open = function (u, t) { ghi({loai: 'window.open', href: String(u).slice(0, 60), target: t || ''}); return oo.apply(this, arguments); };
  const op = window.print;
  window.print = function () { ghi({loai: 'print'}); return op.apply(this, arguments); };
})();
"""


def gan_canh_gac(ctx):
    """Cai doan theo doi vao moi trang cua context: ghi lai link duoc bam (co thuoc tinh download khong), window.open, window.print.
    Bat duoc goc loi ngay ca khi trinh duyet chay ngam khong lo hau qua."""
    if not hasattr(ctx, "_canh_gac"):
        ctx._canh_gac = []  # gui ve Python ngay luc bam, khong mat khi trang bi chuyen di
        ctx.expose_binding("__bao_canh_gac", lambda nguon, x: ctx._canh_gac.append(x))
    ctx.add_init_script(_CANH_GAC_JS)


def kiem_tai(page, bam, duong_dan=None, cho=6000):
    """Bam mot nut tai / xuat file roi kiem 3 lop. bam: ham khong tham so thuc hien cu bam.
    Tra ve dict: tai_ve (co su kien download), ten_tep, roi_trang (khung chinh tu chuyen trang), tab_moi, link_rui_ro (link blob/data/file
    khong co thuoc tinh download), dat (True khi tai ve that, khong roi trang, khong co link rui ro)."""
    goc = page.url
    tai, dieu_huong, tab = [], [], []
    h1 = lambda d: tai.append(d)
    h2 = lambda f: dieu_huong.append(f.url) if f == page.main_frame else None
    h3 = lambda p: tab.append(p)
    page.on("download", h1); page.on("framenavigated", h2); page.context.on("page", h3)
    so_cu = len(getattr(page.context, "_canh_gac", []))
    bam()
    page.wait_for_timeout(cho)
    page.remove_listener("download", h1); page.remove_listener("framenavigated", h2); page.context.remove_listener("page", h3)
    nhat_ky = getattr(page.context, "_canh_gac", [])[so_cu:]
    roi_trang = page.url != goc
    kq = {
        "tai_ve": bool(tai),
        "ten_tep": tai[0].suggested_filename if tai else None,
        "roi_trang": page.url[:60] if roi_trang else None,
        "tab_moi": [p.url[:60] for p in tab],
        "link_rui_ro": [dict(t) for t in {tuple(sorted(x.items())) for x in nhat_ky if x.get("loai") == "link" and re.match(r"(blob|data|file):", x.get("href", "")) and x.get("download") is None}],
    }
    if tai and duong_dan:
        tai[0].save_as(duong_dan)
    kq["dat"] = kq["tai_ve"] and not roi_trang and not kq["tab_moi"] and not kq["link_rui_ro"]
    if roi_trang:  # tra trang ve cho cu de buoc sau chay tiep
        try:
            page.go_back(wait_until="load")
        except Exception:
            pass
        if page.url != goc:
            page.goto(goc, wait_until="load")
    return kq


# ------------------------------------------------------------------ do bo cuc: can chinh, khoang trong, trung nut, co chu
_BO_CUC_JS = r"""
(cfg) => {
  const ra = [];
  const hien = e => { const r = e.getBoundingClientRect(); const s = getComputedStyle(e); return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none'; };
  // khung cua cac doan chu that (khong lay khung cua the bao ngoai, the khoi rong full o)
  const khung_chu = e => { const out = []; const w = document.createTreeWalker(e, NodeFilter.SHOW_TEXT);
    while (w.nextNode()) { const n = w.currentNode; if (!n.textContent.trim()) continue; const rg = document.createRange(); rg.selectNodeContents(n);
      [...rg.getClientRects()].forEach(r => { if (r.width > 0) out.push(r); }); }
    [...e.querySelectorAll('svg, img, input, [role=checkbox], [data-slot=checkbox-control]')].filter(hien).forEach(x => out.push(x.getBoundingClientRect()));
    return out; };
  const rong_chu = e => { const rs = khung_chu(e); if (!rs.length) return 0; return Math.max(...rs.map(r => r.right)) - Math.min(...rs.map(r => r.left)); };
  // 1. nut cung nhan hien 2 lan tren man (ngoai cac dong bang)
  const nut = [...document.querySelectorAll(cfg.vung + ' button, ' + cfg.vung + ' a')].filter(hien).filter(b => !b.closest('[role=dialog]')).filter(b => { const tr = b.closest('tbody tr'); return !tr || tr.children.length <= 1; });
  const dem = {}; nut.forEach(b => { const t = b.innerText.trim(); if (t) (dem[t] = dem[t] || []).push(b); });
  Object.entries(dem).filter(([t, ds]) => ds.length > 1).forEach(([t, ds]) => ra.push({loai: 'Trùng nút', chi_tiet: `"${t}" hiện ${ds.length} lần`,
    khung: ds.map(b => { const r = b.getBoundingClientRect(); return [r.x, r.y, r.right, r.bottom].map(Math.round); })}));
  // 2-5. bang
  document.querySelectorAll(cfg.vung + ' table').forEach((tb, ib) => {
    if (!hien(tb)) return;
    const W = tb.getBoundingClientRect().width;
    const th = [...tb.querySelectorAll('thead th')];
    const dong = [...tb.querySelectorAll('tbody tr')].filter(hien).slice(0, 20);
    if (!th.length || !dong.length) return;
    const cot = th.map((h, i) => {
      const r = h.getBoundingClientRect(); const lh = parseFloat(getComputedStyle(h).lineHeight) || parseFloat(getComputedStyle(h).fontSize) * 1.3;
      const o = dong.map(tr => tr.children[i]).filter(Boolean);
      const noi = o.map(c => rong_chu(c));
      const trai = o.map(c => { const rs = khung_chu(c); return rs.length ? Math.min(...rs.map(x => x.left)) : Infinity; }).filter(isFinite);
      const phai = o.map(c => { const rs = khung_chu(c); return rs.length ? Math.max(...rs.map(x => x.right)) : -Infinity; }).filter(isFinite);
      const co = o.map(c => { const t = [...c.querySelectorAll('*')].filter(x => x.childElementCount === 0 && x.innerText && x.innerText.trim()); return t.length ? Math.max(...t.map(x => parseFloat(getComputedStyle(x).fontSize))) : parseFloat(getComputedStyle(c).fontSize); });
      return {ten: h.innerText.trim().replace(/\s+/g, ' '), x: r.x, rong: r.width, tieu_de_xuong_dong: h.querySelector('*') ? r.height > lh * 1.6 + 24 : false,
              tieu_de_cao: r.height, lh, noi_max: Math.max(0, ...noi), trai_min: Math.min(...trai), phai_max: Math.max(...phai), co_chu: Math.max(...co)};
    });
    // tieu de cot bi xuong dong: so dong chu cua tieu de
    th.forEach((h, i) => { const dongs = new Set(khung_chu(h).filter(x => x.height < 40).map(x => Math.round(x.top / 4))); cot[i].so_dong_tieu_de = dongs.size; });
    const du = cot.filter(c => c.ten && c.rong > W * 0.18 && c.noi_max < c.rong * 0.35);
    cot.forEach(c => { c.trai_min = c.trai_min === undefined || !isFinite(c.trai_min) ? c.x : c.trai_min; });
    cot.forEach((c, i) => {
      if (c.ten && c.so_dong_tieu_de > 1 && du.length) ra.push({loai: 'Tiêu đề cột xuống dòng', chi_tiet: `"${c.ten}" ${c.so_dong_tieu_de} dòng, rộng ${Math.round(c.rong)}px, trong khi cột ${du.map(d => '"' + d.ten + '"').join(', ')} dư chỗ`, khung: [[Math.round(c.x), Math.round(th[i].getBoundingClientRect().y), Math.round(c.x + c.rong), Math.round(th[i].getBoundingClientRect().bottom)]]});
    });
    du.forEach(c => ra.push({loai: 'Cột rộng nhưng nội dung ngắn', chi_tiet: `"${c.ten}" rộng ${Math.round(c.rong)}px (${Math.round(c.rong / W * 100)}% bảng), nội dung dài nhất ${Math.round(c.noi_max)}px`, khung: [[Math.round(c.x), Math.round(tb.getBoundingClientRect().y), Math.round(c.x + c.rong), Math.round(tb.getBoundingClientRect().bottom)]]}));
    for (let i = 0; i + 1 < cot.length; i++) {
      const gap = cot[i + 1].trai_min - cot[i].phai_max;
      if (isFinite(gap) && gap > W * cfg.ty_le_khoang_trong) ra.push({loai: 'Khoảng trắng lớn giữa hai cột', chi_tiet: `giữa "${cot[i].ten || 'cột ' + (i + 1)}" và "${cot[i + 1].ten || 'cột ' + (i + 2)}" trống ${Math.round(gap)}px (${Math.round(gap / W * 100)}% bảng)`,
        khung: [[Math.round(cot[i].phai_max), Math.round(tb.getBoundingClientRect().y), Math.round(cot[i + 1].trai_min), Math.round(tb.getBoundingClientRect().bottom)]]});
    }
    const nho = cot.filter(c => c.ten && c.co_chu < cfg.co_chu_toi_thieu);
    if (nho.length) ra.push({loai: 'Chữ trong bảng nhỏ', chi_tiet: nho.map(c => `"${c.ten}" ${c.co_chu}px`).join(', ') + ` (< ${cfg.co_chu_toi_thieu}px)`, khung: []});
  });
  return ra;
}
"""


def kiem_bo_cuc(page, vung="main", ty_le_khoang_trong=0.25, co_chu_toi_thieu=14):
    """Do bo cuc man dang mo, tra ve danh sach phat hien (loai, chi_tiet, khung toa do CSS de ve anh bug):
    - Trung nut: cung mot nut hanh dong hien 2 lan tren man (vi du nut Them o dau trang va o trang thai rong)
    - Tieu de cot xuong dong trong khi co cot khac du cho
    - Cot rong nhung noi dung ngan (>18% be rong bang ma noi dung < 35% be rong cot)
    - Khoang trang lon giua hai cot lien ke (> 25% be rong bang)
    - Chu trong bang nho hon co chu toi thieu (mac dinh 14px, doi theo design)
    Ket qua la goi y can xem lai, khong tu dong la Loi: doi chieu design truoc khi ket luan."""
    return page.evaluate(_BO_CUC_JS, {"vung": vung, "ty_le_khoang_trong": ty_le_khoang_trong, "co_chu_toi_thieu": co_chu_toi_thieu})
