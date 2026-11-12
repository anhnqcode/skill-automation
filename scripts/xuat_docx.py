# -*- coding: utf-8 -*-
"""
Xuat mot file markdown sang Word (lay tu cong cu cua mot du an truoc).

Cach dung:
  python xuat_docx.py "<duong dan file>.md"

Ket qua: file .docx cung ten, cung thu muc voi file md. Anh duoc tim theo duong dan tuong doi tu thu muc do.
Dinh dang theo cach cua mot du an truoc: Times New Roman 12pt, bang ke du vien.
File docx dang mo trong Word thi dung lai. Ban cu duoc sao luu sang _backup.
"""
import io, os, re, shutil, sys, datetime
import pypandoc
import docx
import docx.text.paragraph
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import Pt, Cm
from docx.enum.style import WD_STYLE_TYPE

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

GOC = None  # thu muc chua file md, dat trong main()
FONT = "Times New Roman"
RONG_ANH = "16.5cm"


def dang_mo_trong_word(duong_dan):
    thu_muc, ten = os.path.split(duong_dan)
    if os.path.exists(os.path.join(thu_muc, "~$" + ten)):
        return True
    try:
        with open(duong_dan, "r+b"):
            return False
    except FileNotFoundError:
        return False
    except OSError:
        return True


def sao_luu(duong_dan):
    if not os.path.exists(duong_dan):
        return None
    thu_muc = os.path.join(GOC, "_backup")
    os.makedirs(thu_muc, exist_ok=True)
    dau_ten, duoi = os.path.splitext(os.path.basename(duong_dan))
    moc = datetime.datetime.now().strftime("%Y%m%d-%H%M")
    dich = os.path.join(thu_muc, "%s - %s%s" % (dau_ten, moc, duoi))
    shutil.copy2(duong_dan, dich)
    return dich


def chuan_bi_markdown(noi_dung):
    """Sua markdown cho hop voi Word: bo duong ke ngang, doi bang thong tin dau trang, dat do rong anh."""
    # bang thong tin khong co tieu de cot thi doi thanh cac dong in dam
    def doi_bang_thong_tin(m):
        dau = m.group(1)
        dong = []
        for hang in m.group(0).strip().splitlines()[2:]:
            hang = hang[len(dau):] if hang.startswith(dau) else hang
            o = [x.strip() for x in hang.strip().strip("|").split("|")]
            if len(o) == 2:
                dong.append("%s%s: %s  " % (dau, o[0], o[1]))
        return "\n".join(dong) + "\n"
    # ca bang nam trong khoi trich dan (mau email) cung doi
    noi_dung = re.sub(r"^((?:> ?)?)\| \| \|\n\1\|---\|---\|\n(?:\1\|.*\|\n)+", doi_bang_thong_tin, noi_dung, flags=re.M)
    # bo duong ke ngang
    noi_dung = re.sub(r"^---\s*$", "", noi_dung, flags=re.M)
    # trong khoi trich dan, moi dong giu nguyen la mot dong (khong bi don lai)
    dong = noi_dung.split("\n")
    for i in range(len(dong) - 1):
        a, b = dong[i], dong[i + 1]
        if (a.startswith(">") and b.startswith(">") and a[1:].strip() and b[1:].strip()
                and not a[1:].strip().startswith("|") and not a.endswith("  ")):
            dong[i] = a + "  "
    noi_dung = "\n".join(dong)
    # xuong dong trong o bang: Word khong hieu the <br> nen doi sang ngat dong cua Word
    noi_dung = re.sub(r"<br\s*/?>", "`<w:r><w:br/></w:r>`{=openxml}", noi_dung)
    # anh vua kho giay
    noi_dung = re.sub(r"(!\[[^\]]*\]\((?:<[^>]*>|[^)]+)\))", r"\1{width=%s}" % RONG_ANH, noi_dung)
    return noi_dung


def _dat_font(run_xml):
    rPr = run_xml.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.insert(0, rFonts)
    for tt in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rFonts.set(qn(tt), FONT)


RONG_TRANG_CM = 17.0


def chia_do_rong_cot(bang):
    """Cot ngan (ma, so thu tu) hep lai, cot noi dung rong ra, theo do dai chu trong cot."""
    so_cot = len(bang.columns)
    cm_moi_ky_tu = 0.21
    toi_thieu, mong_muon = [], []
    for c in range(so_cot):
        chu = [hang.cells[c].text for hang in bang.rows]
        tu_dai = max((len(t) for x in chu for t in x.split()), default=2)
        dong_dai = max((len(x) for x in chu), default=2)
        toi_thieu.append(tu_dai * cm_moi_ky_tu + 0.5)
        mong_muon.append(max(dong_dai * cm_moi_ky_tu + 0.5, toi_thieu[-1]))
    if sum(mong_muon) <= RONG_TRANG_CM:
        he_so = RONG_TRANG_CM / sum(mong_muon)
        cm = [m * he_so for m in mong_muon]
    else:
        du = RONG_TRANG_CM - sum(toi_thieu)
        them = [m - t for m, t in zip(mong_muon, toi_thieu)]
        cm = [t + du * th / sum(them) for t, th in zip(toi_thieu, them)]
    rong = [Cm(x) for x in cm]
    tblPr = bang._tbl.tblPr
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tblPr.append(layout)
    grid = bang._tbl.tblGrid
    for i, gc in enumerate(grid.findall(qn("w:gridCol"))):
        gc.set(qn("w:w"), str(int(rong[i].twips)))
    for hang in bang.rows:
        for i, o in enumerate(hang.cells):
            o.width = rong[i]


def dinh_dang(duong_dan):
    tai_lieu = docx.Document(duong_dan)
    for section in tai_lieu.sections:
        section.left_margin = section.right_margin = Cm(2)
        section.top_margin = section.bottom_margin = Cm(2)
    for style in tai_lieu.styles:
        try:
            style.font.name = FONT
        except Exception:
            pass
    # Co chu mac dinh cua ca tai lieu dat 11pt, roi dat 12pt rieng cho Normal va cho kieu bang.
    # Neu de 12pt trung voi mac dinh thi Word coi la thua va xoa khi luu, chu trong bang ve lai 10pt
    # theo kieu bang cua pandoc.
    rPr_mac_dinh = tai_lieu.styles.element.find(qn("w:docDefaults") + "/" + qn("w:rPrDefault") + "/" + qn("w:rPr"))
    if rPr_mac_dinh is not None:
        for tt in ("w:sz", "w:szCs"):
            e = rPr_mac_dinh.find(qn(tt))
            if e is not None:
                e.set(qn("w:val"), "22")
    tai_lieu.styles["Normal"].font.size = Pt(12)
    for style in tai_lieu.styles:
        if style.type == WD_STYLE_TYPE.TABLE:
            style.font.size = Pt(12)
    for r in tai_lieu.element.body.iter(qn("w:r")):
        _dat_font(r)

    for bang in tai_lieu.tables:
        # mot hang khong bi cat doi sang hai trang
        for hang in bang.rows:
            hang._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))
        # hang tieu de di cung hang dau tien, khong nam le o cuoi trang
        for o in bang.rows[0].cells:
            for doan in o.paragraphs:
                doan.paragraph_format.keep_with_next = True
        # dong nhan dung ngay truoc bang (Truong thong tin, Nut chuc nang...) di cung bang
        truoc = bang._tbl.getprevious()
        if truoc is not None and truoc.tag == qn("w:p"):
            docx.text.paragraph.Paragraph(truoc, None).paragraph_format.keep_with_next = True
        tblPr = bang._tbl.tblPr
        cu = tblPr.find(qn("w:tblBorders"))
        if cu is not None:
            tblPr.remove(cu)
        vien = OxmlElement("w:tblBorders")
        for canh in ("top", "left", "bottom", "right", "insideH", "insideV"):
            e = OxmlElement("w:" + canh)
            e.set(qn("w:val"), "single")
            e.set(qn("w:sz"), "6")
            e.set(qn("w:space"), "0")
            e.set(qn("w:color"), "808080")
            vien.append(e)
        tblPr.append(vien)
        # bang rong het kho giay
        rong = tblPr.find(qn("w:tblW"))
        if rong is None:
            rong = OxmlElement("w:tblW")
            tblPr.append(rong)
        rong.set(qn("w:type"), "pct")
        rong.set(qn("w:w"), "5000")
        chia_do_rong_cot(bang)
        # hang tieu de: in dam, nen xam nhat, lap lai khi sang trang
        hang_dau = bang.rows[0]
        trPr = hang_dau._tr.get_or_add_trPr()
        lap = OxmlElement("w:tblHeader")
        trPr.append(lap)
        for o in hang_dau.cells:
            tcPr = o._tc.get_or_add_tcPr()
            nen = OxmlElement("w:shd")
            nen.set(qn("w:val"), "clear")
            nen.set(qn("w:color"), "auto")
            nen.set(qn("w:fill"), "E7EBF0")
            tcPr.append(nen)
            for doan in o.paragraphs:
                for run in doan.runs:
                    run.bold = True
    tai_lieu.save(duong_dan)


def hoan_thien_bang_word(duong_dan):
    """Mo file bang Word de dat co chu 12 cho moi bang (kieu bang cua pandoc la 10pt) va cap nhat muc luc.
    Chi dat co chu o buoc nay. Neu python-docx dat truoc thi Word bo qua lenh dat co roi lai xoa khi luu, chu ve 10pt."""
    import subprocess
    ps = (
        "$w = New-Object -ComObject Word.Application; $w.Visible = $false; "
        "$ErrorActionPreference = 'Stop'; "
        "$p = '%s'; "
        # lan mo dau Word chi luu lai file cho dung chuan cua Word. Dat co chu ngay o lan nay thi khong giu duoc
        "$d = $w.Documents.Open($p); $d.Save(); $d.Close(); "
        "$d = $w.Documents.Open($p); "
        "foreach ($t in $d.Tables) { $t.Range.Font.Size = 12 }; "
        "foreach ($t in $d.TablesOfContents) { $t.Update() }; "
        "$d.Save(); $d.Close(); $w.Quit()" % duong_dan.replace("'", "''")
    )
    try:
        kq = subprocess.run(["powershell", "-NoProfile", "-Command", ps],
                            capture_output=True, timeout=300)
        loi = kq.stderr.decode("utf-8", "replace").strip()
        if kq.returncode or loi:
            print("Word bao loi khi hoan thien file:", loi[:500])
            return False
        return True
    except Exception as e:
        print("Khong mo duoc Word de hoan thien. Chu trong bang co the con 10pt, muc luc chua co so trang.", e)
        return False


def main():
    if len(sys.argv) < 2:
        print("Cach dung: python xuat_docx.py \"<duong dan file>.md\"")
        return 1
    global GOC
    nguon = os.path.abspath(sys.argv[1])
    GOC = os.path.dirname(nguon)
    ra = os.path.splitext(nguon)[0] + ".docx"
    if dang_mo_trong_word(ra):
        print("DUNG LAI: file docx dang mo trong Word. Dong file roi chay lai.")
        return 1
    ban_cu = sao_luu(ra)
    if ban_cu:
        print("Da sao luu ban cu:", ban_cu)

    noi_dung = chuan_bi_markdown(io.open(nguon, encoding="utf-8").read())
    tam = os.path.join(__import__("tempfile").gettempdir(), "_xuat_docx_tam.md")
    os.makedirs(os.path.dirname(tam), exist_ok=True)
    io.open(tam, "w", encoding="utf-8", newline="").write(noi_dung)

    pypandoc.convert_file(tam, "docx", outputfile=ra,
                          format="markdown+pipe_tables-yaml_metadata_block-implicit_figures",
                          extra_args=[f"--resource-path={GOC}"])
    dinh_dang(ra)
    hoan_thien_bang_word(ra)
    print("Da xuat:", ra)
    return 0


if __name__ == "__main__":
    sys.exit(main())
