"""Ve anh ghi chu bug cho dev: khung do khoanh cho loi, hop xam chu den ghi Actual/Expect, mui ten tu hop xam chi vao khung.

Cach chay:
  python ve_anh_bug.py <spec.json>

spec.json la mot object hoac danh sach object:
  {
    "anh": "duong dan anh chup man hinh",
    "ra": "duong dan anh ket qua .png",
    "dpr": 2,                      ti le anh chup so voi px CSS (Playwright device_scale_factor), mac dinh 2
    "vung": [x1, y1, x2, y2],      vung CSS can cat, bo trong thi lay ca anh
    "khung": [[x1, y1, x2, y2]],   cac khung do, toa do CSS; khung dau tien la noi mui ten cham toi
    "chu": "- Actual: ...\\n\\n- Expect: ...",
    "mui_ten": [x, y],             diem CSS mui ten cham toi, bo trong thi la giua canh phai khung dau
    "hop_y": 300                   vi tri doc cua hop xam (px anh ra), bo trong thi tu dat ngang mui ten
  }
Mui ten nen cham vao duong ke giua hai dong bang hoac canh duoi khung de khong che noi dung.
"""
import json
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT = "C:/Windows/Fonts/times.ttf"
PANEL = 620
S = 1.25  # 1 px CSS = 1.25 px anh ra


def ngat_dong(chu, font, rong, ve):
    dong = []
    for doan in chu.split("\n"):
        cur = ""
        for tu in doan.split(" "):
            thu = (cur + " " + tu).strip()
            if ve.textlength(thu, font=font) <= rong:
                cur = thu
            else:
                dong.append(cur)
                cur = tu
        dong.append(cur)
    return "\n".join(dong)


def ve(spec):
    dpr = spec.get("dpr", 2)
    im = Image.open(spec["anh"]).convert("RGB")
    vung = spec.get("vung") or [0, 0, im.size[0] / dpr, im.size[1] / dpr]
    im = im.crop(tuple(int(v * dpr) for v in vung))
    im = im.resize((int(im.size[0] / dpr * S), int(im.size[1] / dpr * S)))
    cx = lambda x: int((x - vung[0]) * S)
    cy = lambda y: int((y - vung[1]) * S)
    can = Image.new("RGB", (im.size[0] + PANEL, max(im.size[1], 500)), (245, 245, 245))
    can.paste(im, (0, 0))
    d = ImageDraw.Draw(can)
    font = ImageFont.truetype(FONT, 30)
    txt = ngat_dong(spec["chu"], font, PANEL - 80, d)
    cao = int(d.multiline_textbbox((0, 0), txt, font=font, spacing=8)[3]) + 44
    k0 = spec["khung"][0]
    mt = spec.get("mui_ten")
    ty = cy(mt[1]) if mt else cy((k0[1] + k0[3]) / 2)
    tx = cx(mt[0]) if mt else cx(k0[2]) + 6
    y0 = spec.get("hop_y")
    if y0 is None:
        y0 = max(10, min(ty - 60, can.size[1] - cao - 10))
    if y0 + cao + 20 > can.size[1]:
        moi = Image.new("RGB", (can.size[0], y0 + cao + 20), (245, 245, 245))
        moi.paste(can, (0, 0))
        can = moi
    bx = [im.size[0] + 20, y0, can.size[0] - 20, y0 + cao]
    bong = Image.new("RGBA", can.size, (0, 0, 0, 0))
    ImageDraw.Draw(bong).rectangle([bx[0] + 8, bx[1] + 8, bx[2] + 8, bx[3] + 8], fill=(0, 0, 0, 90))
    can = Image.alpha_composite(can.convert("RGBA"), bong.filter(ImageFilter.GaussianBlur(6))).convert("RGB")
    d = ImageDraw.Draw(can)
    goc = min(max(ty, bx[1] + 20), bx[3] - 20)
    d.polygon([(bx[0] + 2, goc - 14), (bx[0] + 2, goc + 14), (tx, ty)], fill=(150, 150, 150))
    d.rectangle(bx, fill=(150, 150, 150), outline=(110, 110, 110), width=2)
    d.multiline_text((bx[0] + 22, bx[1] + 20), txt, font=font, fill=(0, 0, 0), spacing=8)
    for k in spec["khung"]:
        d.rectangle([cx(k[0]), cy(k[1]), cx(k[2]), cy(k[3])], outline=(230, 30, 30), width=5)
    can.save(spec["ra"])
    return spec["ra"]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    for sp in data if isinstance(data, list) else [data]:
        print("Đã vẽ", ve(sp))
