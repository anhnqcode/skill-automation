# Lập ma trận truy vết: mã yêu cầu (US, YC, SCR, UC, BR, AC, NFR...) -> testcase -> bug, và báo chỗ hở.
# Cách dùng:
#   py truy_vet.py --yeu-cau <file hoặc thư mục ...> --testcase <file hoặc thư mục ...>
#                  [--phan-ra <file.json>] [--bug <file.json>] [--tien-to US,YC,SCR,UC,BR,AC,NFR] [--ra <file.md>]
#   --yeu-cau  : BRD, FSD, SRS, CR (.md). Thư mục thì quét mọi .md, bỏ .test.md, .testcase.md, .auto.md, .note.md
#   --testcase : file .test.md / .testcase.md. Thư mục thì quét hai loại này
#   --phan-ra  : JSON của sơ đồ phân rã (nút có khóa "gan_yeu_cau" ghi các mã đã đặc tả)
#   --bug      : JSON mảng 2 chiều (đọc từ Google Sheet bằng google_api.mjs sheet-read), dòng đầu là tiêu đề
#   --tien-to  : các tiền tố mã yêu cầu. Mặc định US,YC,MT,SCR,UC,BR,AC,NFR
# Mã yêu cầu được coi là "định nghĩa" khi đứng ở ô đầu bảng, sau "**" in đậm, hoặc ở tiêu đề. Mã TC dạng TC-...-<số>.
import glob
import json
import os
import re
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")


def arg_list(name):
    a = sys.argv[1:]
    if name not in a:
        return []
    i = a.index(name) + 1
    out = []
    while i < len(a) and not a[i].startswith("--"):
        out.append(a[i])
        i += 1
    return out


def arg_one(name, default=None):
    v = arg_list(name)
    return v[0] if v else default


def files_of(paths, kind):
    out = []
    for p in paths:
        if os.path.isdir(p):
            for f in glob.glob(os.path.join(p, "**", "*.md"), recursive=True):
                low = f.lower()
                is_tc = low.endswith(".test.md") or low.endswith(".testcase.md")
                if kind == "tc" and is_tc:
                    out.append(f)
                if kind == "req" and not is_tc and not low.endswith((".auto.md", ".note.md")):
                    out.append(f)
        elif os.path.isfile(p):
            out.append(p)
    return sorted(set(out))


PREFIX = (arg_one("--tien-to") or "US,YC,MT,SCR,UC,BR,AC,NFR").split(",")
ID_RE = re.compile(r"(?<![\w-])((?:%s)(?:-[A-Z0-9]+)*-?\d+[a-z]?)(?![\w])" % "|".join(PREFIX))
TC_RE = re.compile(r"(?<![\w-])(TC(?:-[A-Z0-9]+)*-\d+[a-z]?)(?![\w])")
DEF_RE = re.compile(r"(?:^\|\s*\**|\*\*|^#+\s.*?)((?:%s)(?:-[A-Z0-9]+)*-?\d+[a-z]?)\b" % "|".join(PREFIX))


def kind_of(i):
    return re.match(r"[A-Z]+", i).group(0)


def main():
    req_files = files_of(arg_list("--yeu-cau"), "req")
    tc_files = files_of(arg_list("--testcase"), "tc")
    if not req_files or not tc_files:
        print(open(__file__, encoding="utf-8").read().split("import glob")[0])
        sys.exit(1)

    defined = {}                      # mã -> "file › tiêu đề"
    mentioned_in_req = set()
    for f in req_files:
        heading = ""
        for line in open(f, encoding="utf-8"):
            if line.startswith("#"):
                heading = line.strip("# \n")[:60]
            for m in DEF_RE.finditer(line):
                defined.setdefault(m.group(1), f"{os.path.basename(f)} › {heading}")
            mentioned_in_req.update(ID_RE.findall(line))

    tc_refs = {}                      # TC -> set mã yêu cầu
    tc_where = {}
    for f in tc_files:
        for line in open(f, encoding="utf-8"):
            if not line.startswith("|"):
                continue
            tcs = TC_RE.findall(line.split("|")[1]) if line.count("|") > 2 else []
            if not tcs:
                continue
            tc = tcs[0]
            tc_refs.setdefault(tc, set()).update(ID_RE.findall(line))
            tc_where[tc] = os.path.basename(f)

    cover = defaultdict(set)
    for tc, ids in tc_refs.items():
        for i in ids:
            cover[i].add(tc)

    bugs = defaultdict(list)          # TC -> [(mô tả ngắn, trạng thái)]
    bug_file = arg_one("--bug")
    if bug_file:
        rows = json.load(open(bug_file, encoding="utf-8"))
        head = [str(h).lower() for h in rows[0]] if rows else []
        st = next((i for i, h in enumerate(head) if "status" in h or "trạng thái" in h), None)
        sm = next((i for i, h in enumerate(head) if "summary" in h or "tiêu đề" in h), None)
        for r in rows[1:]:
            text = " ".join(str(c) for c in r)
            for tc in set(TC_RE.findall(text)):
                bugs[tc].append(((r[sm] if sm is not None and sm < len(r) else "")[:60], r[st] if st is not None and st < len(r) else ""))

    phan_ra = []
    if arg_one("--phan-ra"):
        spec = json.load(open(arg_one("--phan-ra"), encoding="utf-8"))
        for n in spec["nut"]:
            if n.get("giai_doan_sau"):
                continue
            ids = ID_RE.findall(str(n.get("gan_yeu_cau", "")))
            phan_ra.append((n["id"], n["ten"], ids, sorted({tc for i in ids for tc in cover.get(i, [])})))

    req_ids = sorted(defined, key=lambda x: (PREFIX.index(kind_of(x)) if kind_of(x) in PREFIX else 99, x))
    testable = [i for i in req_ids if kind_of(i) in ("BR", "AC", "UC", "SCR", "NFR", "US", "YC")]
    missing = [i for i in testable if not cover.get(i)]
    unknown = sorted({i for ids in tc_refs.values() for i in ids} - set(defined) - mentioned_in_req)
    no_ref = sorted(tc for tc, ids in tc_refs.items() if not ids)

    L = ["# Ma trận truy vết", ""]
    L.append(f"Nguồn yêu cầu: {len(req_files)} file. Testcase: {len(tc_files)} file, {len(tc_refs)} case." + (f" Bug: {sum(len(v) for v in bugs.values())} dòng có dẫn mã TC." if bug_file else ""))
    L += ["", "## 1. Độ phủ theo loại mã", "", "| Loại | Số mã | Có testcase | Chưa có | Tỷ lệ phủ |", "|:---|---:|---:|---:|---:|"]
    for k in PREFIX:
        ids = [i for i in req_ids if kind_of(i) == k]
        if not ids:
            continue
        c = sum(1 for i in ids if cover.get(i))
        L.append(f"| {k} | {len(ids)} | {c} | {len(ids) - c} | {round(100 * c / len(ids))}% |")
    L += ["", "## 2. Mã yêu cầu chưa có testcase", ""]
    if missing:
        L += ["| Mã | Định nghĩa ở |", "|:---|:---|"] + [f"| {i} | {defined[i]} |" for i in missing]
    else:
        L.append("Mọi mã yêu cầu đều có ít nhất một testcase.")
    L += ["", "## 3. Testcase dẫn tới mã không có trong tài liệu", "", "Mã gõ sai, hoặc mã đã bị xóa khỏi tài liệu."]
    L += ([""] + [f"- {i}: {', '.join(sorted(tc for tc, ids in tc_refs.items() if i in ids))}" for i in unknown]) if unknown else ["", "Không có."]
    L += ["", "## 4. Testcase không dẫn mã yêu cầu nào", "", f"{len(no_ref)} case. Đây thường là case ngoài SRS (tư duy test). Kiểm tra case nào thật ra phủ một quy tắc có mã thì ghi mã vào."]
    if no_ref:
        L += ["", ", ".join(no_ref[:200]) + (" …" if len(no_ref) > 200 else "")]
    if phan_ra:
        L += ["", "## 5. Nút phân rã chức năng", "", "| Nút | Tên | Mã đặc tả | Testcase |", "|:---|:---|:---|:---|"]
        for nid, ten, ids, tcs in phan_ra:
            L.append(f"| {nid} | {ten} | {', '.join(ids) or '**Chưa có đặc tả**'} | {len(tcs) if tcs else ('**Chưa có**' if ids else '')} |")
    L += ["", "## 6. Ma trận chi tiết", "", "| Mã | Định nghĩa ở | Testcase | Bug |", "|:---|:---|:---|:---|"]
    for i in req_ids:
        tcs = sorted(cover.get(i, []))
        b = [x for tc in tcs for x in bugs.get(tc, [])]
        bug_txt = f"{len(b)} ({', '.join(sorted({s for _, s in b if s}))})" if b else ""
        L.append(f"| {i} | {defined[i]} | {', '.join(tcs) or '—'} | {bug_txt} |")
    out = "\n".join(L) + "\n"
    dest = arg_one("--ra")
    if dest:
        open(dest, "w", encoding="utf-8").write(out)
        print(f"Đã ghi {dest}. Mã yêu cầu: {len(req_ids)}, chưa có testcase: {len(missing)}, mã lạ trong testcase: {len(unknown)}, case không dẫn mã: {len(no_ref)}.")
    else:
        print(out)


if __name__ == "__main__":
    main()
