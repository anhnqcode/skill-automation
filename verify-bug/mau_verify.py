"""Bo ham dung chung cho skill verify-bug: chay trinh duyet co giao dien, cham, hien dai chu bao bug dang kiem,
do dac cu the tren trang (chu, kich thuoc, vi tri, mau, gia tri) thay vi chi nhin anh.

Chep vao thu muc Automation cua du an thanh verify_chung.py, hoac import thang tu Skill BA.

Gom:
- mo(p, xem=True, kho=(1920, 1080), cham=500)  mo trinh duyet. xem=True: co giao dien, chay cham, kho 1920x1080
- dai_chu(page, bug, buoc="", trang_thai="dang")   hien dai chu tren cung trang: bug dang kiem, buoc dang lam, ket qua
- do(page, bo_chon)        do mot phan tu: co hien, chu, gia tri, khung (x, y, rong, cao), co chu, mau, nen, tran chu
- do_nhieu(page, bo_chon)  do moi phan tu khop bo chon (so luong, chu tung phan tu)
- so_sanh(ten, thuc_te, mong_muon, cach="bang")    so mot chi so, tra ve dong ket qua co Dat/Khong dat
- doi_kho(page, rong, cao)  doi kich thuoc khung nhin khi kiem man responsive
- chup(page, duong_dan)     chup bang chung o ti le 2x, an dai chu truoc khi chup
"""
import json

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


def mo(p, xem=True, kho=(1920, 1080), cham=500, trinh_duyet="chromium"):
    """Mo trinh duyet. xem=True: co giao dien, cham, cua so dung kho. Tra ve (browser, context, page)."""
    b = getattr(p, trinh_duyet).launch(headless=not xem, slow_mo=cham if xem else 0,
                                       args=[f"--window-size={kho[0]},{kho[1]}"] if xem else [])
    ctx = b.new_context(viewport={"width": kho[0], "height": kho[1]}, device_scale_factor=1)
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
