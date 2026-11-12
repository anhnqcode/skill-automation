# Vẽ sơ đồ làn (swimlane) từ file JSON, xuất HTML (SVG) rồi chụp PNG bằng Edge headless.
# Kiểu vẽ lấy theo sơ đồ luồng tổng thể của dự án mẫu.
# Cách dùng: python ve_so_do_lan.py <file.json> [--out <file.png>]
#   Không có --out thì PNG ra cùng thư mục, cùng tên với file JSON. HTML luôn để cạnh JSON.
#
# Cấu trúc JSON:
# {
#   "tieu_de": "Luồng tổng quan ...",          (bắt buộc)
#   "nhan": "END-TO-END",                       (chữ nhỏ phía trên tiêu đề, có thể bỏ)
#   "chu_thich": "Ô nét đứt là việc diễn ra ngoài hệ thống",   (góc dưới phải, có thể bỏ)
#   "lan": [ {"ten": "Quản trị", "mau": "xanh-la"}, ... ],    (màu: xanh-la, xanh-duong, cam, tim, do, xanh-ngoc, xam)
#   "buoc": [
#     {"id": "tao", "lan": 0, "cot": 0, "ten": "Tạo chiến dịch", "mo_ta": "tên, thời gian, trạng thái"},
#     {"id": "hoc", "lan": 2, "cot": 1, "ten": "Học trực tiếp", "mo_ta": "...", "ngoai_he_thong": true},
#     {"id": "dk",  "lan": 1, "cot": 4, "ten": "File hợp lệ?", "loai": "quyet-dinh"},
#     {"id": "bd",  "lan": 0, "cot": 0, "ten": "Bắt đầu", "loai": "bat-dau"}
#   "loai": "the" (mặc định, thẻ có số), "quyet-dinh" (hình thoi), và ba sự kiện kiểu BPMN:
#           "bat-dau" (vòng tròn mảnh), "ket-thuc" (vòng tròn đậm), "hen-gio" (vòng tròn đôi có kim, ví dụ "Hết hạn đăng ký").
#   ],
#   "noi": [ {"tu": "tao", "den": "hoc", "nhan": "Đồng ý", "net_dut": false}, ... ]
# }
# - "lan" của bước là số thứ tự làn (bắt đầu từ 0), "cot" là cột (bắt đầu từ 0).
# - Bước thường được đánh số tự động theo thứ tự khai báo. Bước ngoài hệ thống và ô quyết định không đánh số.
#   Muốn tắt số của một bước: "so": false.
# - "ten", "mo_ta" có thể là chuỗi (tự xuống dòng) hoặc mảng các dòng.
import html
import json
import os
import shutil
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

FONT = "Segoe UI, Arial, sans-serif"
INK, MUTED, LINE = "#1d2733", "#5b6773", "#8a96a3"
MAU = {
    "xanh-la": ("#e4f2ea", "#1f7a4d"),
    "xanh-duong": ("#e7eef9", "#2a5db0"),
    "cam": ("#fbede1", "#b5541a"),
    "tim": ("#efe9f8", "#6a3fb0"),
    "do": ("#fbe7e7", "#b42b2b"),
    "xanh-ngoc": ("#e2f4f4", "#167a7a"),
    "xam": ("#eef0f3", "#5b6773"),
}
THU_TU_MAU = ["xanh-la", "xanh-duong", "cam", "tim", "xanh-ngoc", "do", "xam"]

CW, CH = 185, 132          # kích thước thẻ
COL_GAP = 215              # khoảng cách tâm hai cột
LEFT = 250                 # lề trái, chừa chỗ tên làn
LANE_H = 195
LANE_GAP = 15
TOP = 150


def wrap(text, width):
    if isinstance(text, list):
        return text
    words, lines, cur = str(text).split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return lines or [""]


class Ve:
    def __init__(self):
        self.parts = []

    def add(self, s):
        self.parts.append(s)

    def text(self, x, y, lines, size=18, weight=400, color=INK, anchor="middle", gap=1.3):
        lines = lines if isinstance(lines, list) else [lines]
        y0 = y - (len(lines) - 1) * size * gap / 2
        for i, ln in enumerate(lines):
            self.add(f'<text x="{x}" y="{y0 + i * size * gap}" font-size="{size}" font-weight="{weight}" '
                     f'fill="{color}" text-anchor="{anchor}" dominant-baseline="middle">{html.escape(ln)}</text>')

    def arrow(self, pts, label=None, dashed=False):
        d = "M " + " L ".join(f"{x} {y}" for x, y in pts)
        dash = ' stroke-dasharray="9 7"' if dashed else ""
        self.add(f'<path d="{d}" fill="none" stroke="{LINE}" stroke-width="2.5"{dash} marker-end="url(#ah)"/>')
        if label:
            # đặt nhãn ở đoạn dài nhất
            best = max(range(len(pts) - 1), key=lambda i: abs(pts[i + 1][0] - pts[i][0]) + abs(pts[i + 1][1] - pts[i][1]))
            (x1, y1), (x2, y2) = pts[best], pts[best + 1]
            if y1 == y2:
                self.text((x1 + x2) / 2, y1 - 16, label, size=16, color=MUTED)
            else:
                self.text(x1 + 10, (y1 + y2) / 2, label, size=16, color=MUTED, anchor="start")


def ve(spec):
    lanes, steps, links = spec["lan"], spec["buoc"], spec.get("noi", [])
    ncol = max(s["cot"] for s in steps) + 1
    W = LEFT + ncol * COL_GAP + 40
    lane_top = lambda i: TOP + i * (LANE_H + LANE_GAP)
    H = lane_top(len(lanes)) + 90
    v = Ve()

    for i, ln in enumerate(lanes):
        band, edge = MAU[ln.get("mau") or THU_TU_MAU[i % len(THU_TU_MAU)]]
        y = lane_top(i)
        v.add(f'<rect x="20" y="{y}" width="{W - 40}" height="{LANE_H}" rx="14" fill="{band}"/>')
        v.text(45, y + LANE_H / 2, wrap(ln["ten"], 12), size=26, weight=700, color=edge, anchor="start")

    box = {}
    so = 0
    EV = 64  # đường kính sự kiện bắt đầu, kết thúc, hẹn giờ
    for s in steps:
        ln = lanes[s["lan"]]
        _, edge = MAU[ln.get("mau") or THU_TU_MAU[s["lan"] % len(THU_TU_MAU)]]
        x = LEFT + s["cot"] * COL_GAP
        y = lane_top(s["lan"]) + (LANE_H - CH) / 2
        loai = s.get("loai", "the")
        if loai in ("bat-dau", "ket-thuc", "hen-gio"):
            ex, ey = x + (CW - EV) / 2, y + (CH - EV) / 2
            box[s["id"]] = (ex, ey, EV, EV)
            cx, cy, r = x + CW / 2, y + CH / 2, EV / 2
            if loai == "bat-dau":
                v.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#ffffff" stroke="{edge}" stroke-width="2.5"/>')
            elif loai == "ket-thuc":
                v.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#ffffff" stroke="{edge}" stroke-width="6"/>')
            else:
                v.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#ffffff" stroke="{edge}" stroke-width="2.5"/>')
                v.add(f'<circle cx="{cx}" cy="{cy}" r="{r - 7}" fill="#ffffff" stroke="{edge}" stroke-width="1.5"/>')
                v.add(f'<path d="M{cx} {cy - 14} V{cy} L{cx + 10} {cy + 6}" stroke="{edge}" stroke-width="2.5" fill="none"/>')
            if s.get("ten"):
                v.text(cx, cy + r + 20, wrap(s["ten"], 18), size=15, weight=600, color=MUTED)
            continue
        box[s["id"]] = (x, y, CW, CH)
        outside = s.get("ngoai_he_thong", False)
        if loai == "quyet-dinh":
            cx, cy = x + CW / 2, y + CH / 2
            pts = f"{cx},{y} {x + CW},{cy} {cx},{y + CH} {x},{cy}"
            v.add(f'<polygon points="{pts}" fill="#fffdf5" stroke="{edge}" stroke-width="2.5"/>')
            v.text(cx, cy, wrap(s["ten"], 12), size=16, weight=600)
            continue
        dash = ' stroke-dasharray="9 7"' if outside else ""
        fill = "#fbfbfc" if outside else "#ffffff"
        v.add(f'<rect x="{x}" y="{y}" width="{CW}" height="{CH}" rx="12" fill="{fill}" stroke="{edge}" stroke-width="2.5"{dash}/>')
        title = wrap(s["ten"], 15)
        sub = wrap(s["mo_ta"], 22) if s.get("mo_ta") else []
        th, sh = 21, 16
        total = len(title) * th * 1.25 + (len(sub) * sh * 1.3 + 8 if sub else 0)
        top = y + CH / 2 - total / 2
        v.text(x + CW / 2, top + len(title) * th * 1.25 / 2, title, size=th, weight=700, gap=1.25)
        if sub:
            v.text(x + CW / 2, top + len(title) * th * 1.25 + 8 + len(sub) * sh * 1.3 / 2, sub, size=sh, color=MUTED)
        if s.get("so", not outside):
            so += 1
            v.add(f'<circle cx="{x + 8}" cy="{y + 8}" r="21" fill="{edge}" stroke="#fff" stroke-width="3"/>')
            v.text(x + 8, y + 9, str(so), size=19, weight=700, color="#fff")

    step_by_id = {s["id"]: s for s in steps}
    for l in links:
        a, b = step_by_id[l["tu"]], step_by_id[l["den"]]
        (ax, ay, aw, ah), (bx, by, bw, bh) = box[l["tu"]], box[l["den"]]
        dashed, label = l.get("net_dut", False), l.get("nhan")
        if a["lan"] == b["lan"]:
            between = [s for s in steps if s["lan"] == a["lan"] and min(a["cot"], b["cot"]) < s["cot"] < max(a["cot"], b["cot"])]
            if b["cot"] > a["cot"] and not between:
                pts = [(ax + aw, ay + ah / 2), (bx - 4, by + bh / 2)]
            else:  # đi vòng dưới các thẻ trong làn
                yb = lane_top(a["lan"]) + (LANE_H + CH) / 2 + 22
                pts = [(ax + aw / 2, ay + ah), (ax + aw / 2, yb), (bx + bw / 2, yb), (bx + bw / 2, by + bh + 4)]
        elif a["cot"] == b["cot"]:
            if b["lan"] > a["lan"]:
                pts = [(ax + aw / 2, ay + ah), (bx + bw / 2, by - 4)]
            else:
                pts = [(ax + aw / 2, ay), (bx + bw / 2, by + bh + 4)]
        else:  # khác làn, khác cột: đi theo khe giữa hai làn ngay trước làn đích
            if b["lan"] > a["lan"]:
                yg = lane_top(b["lan"]) - LANE_GAP / 2
                pts = [(ax + aw / 2, ay + ah), (ax + aw / 2, yg), (bx + bw / 2, yg), (bx + bw / 2, by - 4)]
            else:
                yg = lane_top(b["lan"] + 1) - LANE_GAP / 2
                pts = [(ax + aw / 2, ay), (ax + aw / 2, yg), (bx + bw / 2, yg), (bx + bw / 2, by + bh + 4)]
        v.arrow(pts, label, dashed)

    if spec.get("chu_thich"):
        v.text(W - 40, H - 40, spec["chu_thich"], size=17, color=MUTED, anchor="end")

    head = ""
    if spec.get("nhan"):
        head += f'<text x="40" y="52" font-size="20" font-weight="700" letter-spacing="4" fill="#1f7a4d">{html.escape(spec["nhan"])}</text>'
    head += f'<text x="40" y="105" font-size="44" font-weight="800" fill="{INK}">{html.escape(spec["tieu_de"])}</text>'
    doc = f'''<!doctype html><html><head><meta charset="utf-8">
<style>html,body{{margin:0;background:#f6f7f9}}svg{{display:block;font-family:{FONT}}}</style></head><body>
<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="ah" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto" markerUnits="userSpaceOnUse">
<path d="M0,0 L12,6 L0,12 z" fill="{LINE}"/></marker></defs>
{head}
{''.join(v.parts)}
</svg></body></html>'''
    return doc, W, H


def tim_trinh_duyet():
    for p in [r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
              r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
              r"C:\Program Files\Google\Chrome\Application\chrome.exe"]:
        if os.path.exists(p):
            return p
    return shutil.which("msedge") or shutil.which("chrome") or shutil.which("google-chrome")


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__ or "python ve_so_do_lan.py <file.json> [--out <file.png>]")
        sys.exit(1)
    src = os.path.abspath(args[0])
    out = os.path.abspath(args[args.index("--out") + 1]) if "--out" in args else os.path.splitext(src)[0] + ".png"
    with open(src, encoding="utf-8") as f:
        spec = json.load(f)
    doc, W, H = ve(spec)
    page = os.path.splitext(src)[0] + ".html"
    with open(page, "w", encoding="utf-8") as f:
        f.write(doc)
    browser = tim_trinh_duyet()
    if not browser:
        print("Không tìm thấy Edge hoặc Chrome. Đã tạo HTML: " + page)
        sys.exit(2)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    subprocess.run([browser, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--force-device-scale-factor=1", f"--window-size={W},{H}",
                    f"--screenshot={out}", "file:///" + page.replace("\\", "/")],
                   check=True, capture_output=True)
    print("Đã vẽ: " + out)


if __name__ == "__main__":
    main()
