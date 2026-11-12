# Dựng sơ đồ Mermaid (flowchart, sequence, state, ERD, journey...) thành ảnh PNG bằng Edge headless.
# Dùng cho dự án xuất docx, nơi tài liệu cần ảnh thay vì khối mermaid.
# Cách dùng: py ve_mermaid.py <file.mmd> [--out <file.png>] [--rong 1600]
#   File .mmd chỉ chứa mã Mermaid (không có dòng ```mermaid). Cần mạng để tải thư viện Mermaid từ cdn.jsdelivr.net.
#   HTML trung gian để cạnh file .mmd. Ảnh được cắt sát nội dung, chừa lề 24px.
import html
import os
import shutil
import subprocess
import sys

from PIL import Image, ImageChops

sys.stdout.reconfigure(encoding="utf-8")


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
        print("Cách dùng: py ve_mermaid.py <file.mmd> [--out <file.png>] [--rong 1600]")
        sys.exit(1)
    src = os.path.abspath(args[0])
    out = os.path.abspath(args[args.index("--out") + 1]) if "--out" in args else os.path.splitext(src)[0] + ".png"
    width = int(args[args.index("--rong") + 1]) if "--rong" in args else 1600
    code = open(src, encoding="utf-8").read().strip()
    page = os.path.splitext(src)[0] + ".html"
    with open(page, "w", encoding="utf-8") as f:
        f.write(f'''<!doctype html><html><head><meta charset="utf-8">
<style>html,body{{margin:0;background:#ffffff}} #c{{padding:24px;display:inline-block}}</style>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script></head><body>
<div id="c"><pre class="mermaid">{html.escape(code)}</pre></div>
<script>mermaid.initialize({{startOnLoad:true, theme:"neutral", fontFamily:"Segoe UI, Arial, sans-serif",
  flowchart:{{useMaxWidth:false}}, sequence:{{useMaxWidth:false}}, er:{{useMaxWidth:false}}, state:{{useMaxWidth:false}}}});</script>
</body></html>''')
    browser = tim_trinh_duyet()
    if not browser:
        print("Không tìm thấy Edge hoặc Chrome. Đã tạo HTML: " + page)
        sys.exit(2)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    subprocess.run([browser, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=2",
                    "--virtual-time-budget=8000", f"--window-size={width},2400", f"--screenshot={out}",
                    "file:///" + page.replace("\\", "/")], check=True, capture_output=True)
    img = Image.open(out).convert("RGB")
    box = ImageChops.difference(img, Image.new("RGB", img.size, (255, 255, 255))).getbbox()
    if not box:
        print("Ảnh trống: mã Mermaid lỗi hoặc không tải được thư viện. Mở " + page + " bằng trình duyệt để xem lỗi.")
        sys.exit(3)
    pad = 48
    img.crop((max(box[0] - pad, 0), max(box[1] - pad, 0), min(box[2] + pad, img.width), min(box[3] + pad, img.height))).save(out)
    if box[3] >= img.height - 2 or box[2] >= img.width - 2:
        print("Cảnh báo: sơ đồ có thể bị cắt mép. Tăng --rong hoặc tách sơ đồ.")
    print("Đã vẽ: " + out)


if __name__ == "__main__":
    main()
