"""Bo ham dung chung cho che do B (kiem he thong khi chua co testcase). Chep vao thu muc Automation cua du an thanh chung.py roi sua phan CAU HINH.

Gom:
- ghi(...)            ghi mot muc kiem, nhan thang gia tri Ket qua, kem loi ngam phat sinh trong luc chay muc do
- chup(...)           chup anh, che vung tai khoan theo phan tu (khong theo toa do)
- cho_api(...)        bam roi cho dung phan hoi API, thay cho wait_for_timeout
- dat_cho(ctx)        cho mac dinh 10 giay cho thao tac, 30 giay cho dieu huong: buoc loi bao som, khong treo 30 giay
- dung_lai_phien(...) dang nhap mot lan cho moi tai khoan, cac kich ban sau nap lai cookie
- chay_lai_neu_loi    chi chay lai khi het thoi gian cho, so sai gia tri thi ket luan luon
- theo_doi_tai(page)  dem request dang chay; cho_yen(page, toi_da_ms) dung thay wait_for_timeout sau thao tac:
                      cho toi thieu max(600 ms, 40% so cu), roi di tiep khi het request va DOM dung yen 600 ms
- theo_doi(page)      bat loi console, loi JS, phan hoi 4xx/5xx ngoai chu dich
- bat_trace / dong_trace   trace Playwright theo nhom, giu trace cua muc Loi
- loc_bi_mat(chu)     xoa thong tin dang nhap, email, mat khau khoi moi cho ghi ra
- luu_ket_qua(...)    ghi JSON, bang Tong quan dem tu cot Ket qua
- trang_thai(...)     luu ma, duong dan ban ghi do lan chay tao ra de dot sau va buoc chay lai dung tiep
"""
import hashlib
import json
import os
import re
import shutil
import tempfile
import time
from collections import Counter

# ======================= CAU HINH (sua theo du an) =======================
THU_MUC = os.path.dirname(os.path.abspath(__file__))
KET_QUA_DIR = os.path.join(THU_MUC, "ket-qua")
TAM = os.path.join(tempfile.gettempdir(), "automation-" + os.path.basename(os.path.dirname(THU_MUC)))  # trace, phien, tep tai ve: ngoai thu muc du an
VUNG_TAI_KHOAN = ["header [data-slot=avatar]", "header .user-menu"]  # bo chon vung ten, email tai khoan can che
BI_MAT = []  # dien luc chay: email quan tri, mat khau... doc tu file thong tin dang nhap, KHONG viet cung
CHO_MS = int(os.environ.get("CHO_MS", "10000"))  # thao tac: click, fill, wait_for_selector, expect_response
CHO_DIEU_HUONG_MS = int(os.environ.get("CHO_DIEU_HUONG_MS", "30000"))  # goto, wait_for_url
PHIEN_HAN_GIAY = int(os.environ.get("PHIEN_HAN_GIAY", "1800"))  # NHO HON han phien cua may chu tru nhom dai nhat
# =========================================================================

GIA_TRI = ("Đạt", "Lỗi", "Cần xác nhận", "Bị chặn", "Không tạo được tình huống", "Chưa kiểm")
KET_QUA = []
_LOI_NGAM = []
os.makedirs(TAM, exist_ok=True)


def loc_bi_mat(chu):
    chu = str(chu)
    for b in BI_MAT:
        if b:
            chu = chu.replace(b, "<đã che>")
    chu = re.sub(r"[\w.+-]+@[\w-]+\.[\w.]+", lambda m: m.group(0) if m.group(0).endswith("@example.com") else "<email>", chu)
    return chu


def theo_doi(page, bo_qua_url=()):
    """Bat loi ngam: console error, loi JS, phan hoi >= 500, 4xx ngoai chu dich, mixed content."""
    def _r(resp):
        if resp.status >= 500 or (resp.status >= 400 and not any(x in resp.url for x in bo_qua_url)):
            _LOI_NGAM.append("HTTP %d %s" % (resp.status, resp.url.split("?")[0][-80:]))
    page.on("console", lambda m: _LOI_NGAM.append("console: " + m.text[:150]) if m.type == "error" else None)
    page.on("pageerror", lambda e: _LOI_NGAM.append("JS: " + str(e)[:150]))
    page.on("response", _r)


def ghi(ma, phan, noi_dung, mong_muon, thuc_te, ket_qua, page=None, nguon="", lan="L1"):
    """ket_qua phai la mot trong GIA_TRI. Loi ngam phat sinh tu lan ghi truoc toi gio duoc gan vao muc nay."""
    assert ket_qua in GIA_TRI, ket_qua
    anh = chup(page, ma) if page is not None and ket_qua != "Đạt" else ""
    muc = dict(ma=ma, phan=phan, noi_dung=loc_bi_mat(noi_dung), mong_muon=loc_bi_mat(mong_muon), thuc_te=loc_bi_mat(thuc_te),
               ket_qua=ket_qua, anh=anh, nguon=nguon, lan=lan, loi_ngam=list(_LOI_NGAM),
               kho=(page.viewport_size if page is not None else None))
    _LOI_NGAM.clear()
    KET_QUA.append(muc)
    print(loc_bi_mat("[%s] %s: %s" % (ket_qua, ma, noi_dung)))
    return muc


def chup(page, ten, full=True, thu_muc=None):
    thu_muc = thu_muc or os.path.join(KET_QUA_DIR, "anh")
    os.makedirs(thu_muc, exist_ok=True)
    f = os.path.join(thu_muc, re.sub(r"[^\w-]+", "-", ten)[:60] + ".png")
    che = [page.locator(s) for s in VUNG_TAI_KHOAN if page.locator(s).count()]
    page.screenshot(path=f, full_page=full, mask=che, mask_color="#EBEEF2")
    return os.path.relpath(f, KET_QUA_DIR)


def cho_api(page, hanh_dong, duong_dan, ma=None, timeout=15000):
    """Bam roi cho phan hoi API co duong_dan (chuoi con). Tra ve response. Dung thay cho wait_for_timeout."""
    with page.expect_response(lambda r: duong_dan in r.url and (ma is None or r.status == ma), timeout=timeout) as info:
        hanh_dong()
    return info.value


_DANG_TAI = {}
_YEN_JS = """(dat_lai) => {
  if (!window.__qa_mo) {
    window.__qa_mo = new MutationObserver(() => { window.__qa_cuoi = performance.now(); });
    window.__qa_mo.observe(document, {subtree: true, childList: true, attributes: true, characterData: true});
  }
  if (dat_lai || window.__qa_cuoi === undefined) window.__qa_cuoi = performance.now();
  return performance.now() - window.__qa_cuoi;
}"""


def theo_doi_tai(page):
    """Goi mot lan cho moi page, cung cho voi theo_doi(). cho_yen() can bo dem nay."""
    loai = ("xhr", "fetch", "document")

    def _bat_dau(r):
        if r.resource_type in loai:
            _DANG_TAI[page] = _DANG_TAI.get(page, 0) + 1

    def _xong(r):
        if r.resource_type in loai:
            _DANG_TAI[page] = max(0, _DANG_TAI.get(page, 0) - 1)
    page.on("request", _bat_dau)
    page.on("requestfinished", _xong)
    page.on("requestfailed", _xong)


def cho_yen(page, toi_da_ms, yen_ms=600, san=0.4):
    """Thay wait_for_timeout(toi_da_ms) sau mot thao tac. Dem lai tu luc goi, cho toi thieu max(yen_ms, san x toi_da_ms)
    (go o tim kiem chi doi value va request bi tre do debounce; chon tep doc bat dong bo: DOM chua doi ngay), roi di tiep
    khi het request dang chay va DOM dung yen yen_ms. Khong bao gio cho lau hon toi_da_ms.
    KHONG dung cho cho co chu dich theo dong ho (giua cac lan sai mat khau, gui lai, thong bao tu tat, dem nguoc)."""
    t0 = time.time()
    han, moc_san = t0 + toi_da_ms / 1000, t0 + max(yen_ms, san * toi_da_ms) / 1000
    try:
        page.evaluate(_YEN_JS, True)
    except Exception:
        pass
    while time.time() < han:
        page.wait_for_timeout(100)
        if time.time() < moc_san:
            continue
        try:
            yen = page.evaluate(_YEN_JS, False)
        except Exception:
            yen = 0  # dang chuyen trang
        if yen >= yen_ms and not _DANG_TAI.get(page):
            return


def dat_cho(o):
    """Goi cho moi context (va page tao bang browser.new_page). Buoc goi timeout= rieng thi van theo so rieng."""
    o.set_default_timeout(CHO_MS)
    o.set_default_navigation_timeout(CHO_DIEU_HUONG_MS)


def dung_lai_phien(pg, khoa, dang_nhap_that, url_kiem, da_vao):
    """Nap phien da luu cho tai khoan 'khoa' (vi du 'qt:' + email); con hieu luc thi bo qua man dang nhap.

    dang_nhap_that(): dang nhap qua form. url_kiem: trang chi vao duoc khi da dang nhap.
    da_vao(pg) -> bool: kiem dau hieu CHAC CHAN da dang nhap (nut Dang xuat, menu tai khoan), khong chi URL: nhieu app
    chi day ve trang dang nhap sau khi API tra 401, luc do URL van dung.
    Phien cookie. He thong luu phien o localStorage thi nap them origins cua storage_state bang add_init_script.
    KHONG dung cho case kiem dang nhap, mat khau sai, khoa tai khoan, het phien: cac case do goi form truc tiep.
    Sau case dang xuat hoac doi mat khau thi goi xoa_phien().
    """
    tep = os.path.join(TAM, "phien", hashlib.sha1(khoa.encode("utf-8")).hexdigest()[:12] + ".json")  # email khong nam tren ten tep
    ctx = pg.context
    if os.environ.get("PHIEN_MOI") != "1" and os.path.exists(tep) and time.time() - os.path.getmtime(tep) < PHIEN_HAN_GIAY:
        try:
            with open(tep, encoding="utf-8") as f:
                ctx.add_cookies(json.load(f)["cookies"])
            pg.goto(url_kiem, wait_until="networkidle")
            if da_vao(pg):
                return True
        except Exception:
            pass
        ctx.clear_cookies()  # phien cu het han hoac bi thu hoi: xoa de form dang nhap chay sach
        try:
            os.remove(tep)
        except OSError:
            pass
    dang_nhap_that()
    pg.goto(url_kiem, wait_until="networkidle")
    if not da_vao(pg):  # khong luu phien hong: sai mat khau, tai khoan dang bi khoa
        raise RuntimeError("Dang nhap qua form khong vao duoc he thong")
    os.makedirs(os.path.dirname(tep), exist_ok=True)
    ctx.storage_state(path=tep)
    return False


def xoa_phien():
    shutil.rmtree(os.path.join(TAM, "phien"), ignore_errors=True)


def chay_lai_neu_loi(ham, so_lan=1):
    """ham() tra True/False. Tra ve True, False, hoac None khi khong on dinh.
    So sai gia tri (False) thi ket luan luon, khong chay lai: lap lai chi nhan thoi gian ma ket qua khong doi.
    Chi chay lai khi het thoi gian cho (TimeoutError). Lan sau qua thi tra None: noi goi ghi ket qua "Cần xác nhận",
    cot Thuc te ghi "Không ổn định" de xem tay. Chi dung cho thao tac chi doc: chay lai thao tac tao du lieu co the tao trung."""
    from playwright.sync_api import TimeoutError as HetCho
    try:
        return bool(ham())
    except HetCho:
        for _ in range(so_lan):
            try:
                return None if ham() else False
            except HetCho:
                pass
        return False


def bat_trace(context, nhom):
    context.tracing.start(name=nhom, screenshots=True, snapshots=True)


def dong_trace(context, nhom, co_loi):
    """Chi giu trace khi nhom co muc Loi. Trace chua cookie va chu da go: chi luu may, khong gui ai."""
    f = os.path.join(TAM, "trace-%s.zip" % nhom)
    context.tracing.stop(path=f)
    if not co_loi:
        os.remove(f)
    return f if co_loi else ""


def trang_thai(ten, du_lieu=None):
    """Doc (du_lieu=None) hoac ghi trang thai ban ghi do lan chay tao ra, vi du ma chien dich thu."""
    d = os.path.join(KET_QUA_DIR, "trang-thai")
    os.makedirs(d, exist_ok=True)
    f = os.path.join(d, ten + ".json")
    if du_lieu is None:
        return json.load(open(f, encoding="utf-8")) if os.path.exists(f) else None
    json.dump(du_lieu, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def thu_ghi_file(duong_dan):
    """Truoc khi chay nhom doi mat khau: file du lieu dang mo (Windows khoa) thi dung lai, khong bam luu."""
    try:
        with open(duong_dan, "a+b"):
            return True
    except PermissionError:
        return False


def luu_ket_qua(ten_dot):
    d = os.path.join(KET_QUA_DIR, time.strftime("%Y%m%d-%H%M"))
    os.makedirs(d, exist_ok=True)
    json.dump(KET_QUA, open(os.path.join(d, "ket-qua_%s.json" % ten_dot), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    dem = Counter(m["ket_qua"] for m in KET_QUA)
    print("Tổng quan:", {k: dem.get(k, 0) for k in GIA_TRI}, "Tổng", len(KET_QUA))
    return d


def don_tam():
    shutil.rmtree(TAM, ignore_errors=True)
