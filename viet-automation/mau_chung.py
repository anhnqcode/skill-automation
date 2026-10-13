"""Bo ham dung chung cho che do B (kiem he thong khi chua co testcase). Chep vao thu muc Automation cua du an thanh chung.py roi sua phan CAU HINH.

Gom:
- ghi(...)            ghi mot muc kiem, nhan thang gia tri Ket qua, kem loi ngam phat sinh trong luc chay muc do
- chup(...)           chup anh, che vung tai khoan theo phan tu (khong theo toa do)
- cho_api(...)        bam roi cho dung phan hoi API, thay cho wait_for_timeout
- theo_doi(page)      bat loi console, loi JS, phan hoi 4xx/5xx ngoai chu dich
- bat_trace / dong_trace   trace Playwright theo nhom, giu trace cua muc Loi
- loc_bi_mat(chu)     xoa thong tin dang nhap, email, mat khau khoi moi cho ghi ra
- luu_ket_qua(...)    ghi JSON, bang Tong quan dem tu cot Ket qua
- trang_thai(...)     luu ma, duong dan ban ghi do lan chay tao ra de dot sau va buoc chay lai dung tiep
"""
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


def chay_lai_neu_loi(ham, so_lan=2):
    """Muc ra Loi thi tu chay lai; ket qua khong on dinh thi tra 'Không ổn định' de xem tay."""
    if ham():
        return True
    lai = [bool(ham()) for _ in range(so_lan)]
    return False if not any(lai) else "Không ổn định"


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
