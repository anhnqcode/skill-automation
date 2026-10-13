"""Dung lo yeu cau Sheets API batchUpdate cho file bug theo mau: bang REPORT dem bug theo trang thai, danh sach chon Status, Asignee, Reporter va mau cho tung trang thai.

Cach chay:
  python tao_bang_bug.py --ra requests.json [--sheet-id 0] [--dong-dau 12] [--asignee "Đức"] [--reporter "Q.Anh"] [--tao-khung] [--dau-phay]
roi gui:  node google_api.mjs sheet-batch <link sheet> requests.json --key <khoa>

Bo cuc mau (giong file "Bug Tập huấn"):
  E1:F1  REPORT * (gop o)
  E2:F2  Mã trường hợp kiểm thử | B         (chu cai cot Status, cong thuc dem tren cot nay)
  E3:F8  Số bugs <...> (Todo/Inprogress/Resolved/Reopen/Pending/Passed) | cong thuc COUNTIF lay trang thai trong ngoac
  E9:F9  Tổng số bugs | COUNTA cot Status
  Dong dong-dau - 1: tieu de ID, Status, Asignee, Reporter, Summary, Step to reproduce, Result, Image, Note
--tao-khung: ghi ca chu cua bang REPORT, dong tieu de va dinh dang khung (dung cho tab trong).
Khong co --tao-khung: chi them cong thuc, danh sach chon, mau (dung khi bang da co san chu va khung).
--dau-phay: sheet dung dau phay ngan tham so (locale en). Mac dinh dung dau cham phay (locale vi).
"""
import argparse
import json

TRANG_THAI = [  # ten, nen, chu
    ("Passed", "#c9daf8", "#1c4587"), ("Todo", "#fcd5b4", "#7f3f00"), ("Inprogress", "#b6e7f0", "#0c5460"),
    ("Resolved", "#ffe5a0", "#7f6000"), ("Reopen", "#b4e5e0", "#134f4a"), ("Pending", "#ffcfc9", "#990000"),
    ("Closed", "#e6cff2", "#4a148c"), ("Testing", "#d4edbc", "#274e13"),
]
NHAN_REPORT = ["Số bugs chưa fix (Todo)", "Số bugs đang fix (Inprogress)", "Số bugs đã fix (Resolved)",
               "Số bugs không đạt (Reopen)", "Số bugs đang xem xét (Pending)", "Số bugs đạt (Passed)"]
TIEU_DE = ["ID", "Status", "Asignee", "Reporter", "Summary", "Step to reproduce", "Result", "Image", "Note"]
RONG_COT = [60, 120, 100, 100, 330, 330, 330, 190, 200]
FONT = "Times New Roman"


def hx(h):
    h = h.lstrip("#")
    return {"red": int(h[0:2], 16) / 255, "green": int(h[2:4], 16) / 255, "blue": int(h[4:6], 16) / 255}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ra", required=True)
    ap.add_argument("--sheet-id", type=int, default=0)
    ap.add_argument("--dong-dau", type=int, default=12, help="dong du lieu dau tien (danh so tu 1)")
    ap.add_argument("--asignee", default="Đức")
    ap.add_argument("--reporter", default="Q.Anh")
    ap.add_argument("--tao-khung", action="store_true")
    ap.add_argument("--dau-phay", action="store_true")
    a = ap.parse_args()
    sid, d0 = a.sheet_id, a.dong_dau - 1
    sep = "," if a.dau_phay else ";"
    rng = lambda c0, c1, r0=d0, r1=1000: {"sheetId": sid, "startRowIndex": r0, "endRowIndex": r1, "startColumnIndex": c0, "endColumnIndex": c1}
    vien = {"style": "SOLID", "width": 1, "color": hx("#1f2329")}
    req = []

    if a.tao_khung:
        o = lambda v, dam=False, nen=None, giua=False, co=13: {"userEnteredValue": {"stringValue": v}, "userEnteredFormat": {
            "textFormat": {"fontFamily": FONT, "fontSize": co, "bold": dam}, "horizontalAlignment": "CENTER" if giua else "LEFT",
            "verticalAlignment": "MIDDLE", **({"backgroundColor": hx(nen)} if nen else {}),
            "borders": {"top": vien, "bottom": vien, "left": vien, "right": vien}}}
        hang = [[o("REPORT *", True), o("", True)], [o("Mã trường hợp kiểm thử", True), o("B", giua=True)]]
        hang += [[o(n, True), o("", nen="#ccffcc", giua=True)] for n in NHAN_REPORT]
        hang += [[o("Tổng số bugs", True, "#ccffcc"), o("", nen="#ccffcc", giua=True)]]
        req.append({"updateCells": {"start": {"sheetId": sid, "rowIndex": 0, "columnIndex": 4}, "rows": [{"values": h} for h in hang],
                                    "fields": "userEnteredValue,userEnteredFormat"}})
        req.append({"mergeCells": {"range": rng(4, 6, 0, 1), "mergeType": "MERGE_ALL"}})
        req.append({"updateCells": {"start": {"sheetId": sid, "rowIndex": d0 - 1, "columnIndex": 0},
                                    "rows": [{"values": [o(t, nen="#d9ead3", giua=True, co=12) for t in TIEU_DE]}], "fields": "userEnteredValue,userEnteredFormat"}})
        for i, w in enumerate(RONG_COT):
            req.append({"updateDimensionProperties": {"range": {"sheetId": sid, "dimension": "COLUMNS", "startIndex": i, "endIndex": i + 1},
                                                      "properties": {"pixelSize": w}, "fields": "pixelSize"}})
        req.append({"repeatCell": {"range": rng(0, 9, d0, d0 + 100), "cell": {"userEnteredFormat": {"borders": {"top": vien, "bottom": vien, "left": vien, "right": vien}}},
                                   "fields": "userEnteredFormat.borders"}})
        req.append({"repeatCell": {"range": rng(0, 1), "cell": {"userEnteredFormat": {"horizontalAlignment": "CENTER", "verticalAlignment": "MIDDLE",
                                   "textFormat": {"fontFamily": FONT, "fontSize": 12}}}, "fields": "userEnteredFormat(horizontalAlignment,verticalAlignment,textFormat.fontFamily,textFormat.fontSize)"}})

    # danh sach chon
    req.append({"setDataValidation": {"range": rng(1, 2), "rule": {"condition": {"type": "ONE_OF_LIST", "values": [{"userEnteredValue": t} for t, _, _ in TRANG_THAI]},
                                                                  "strict": True, "showCustomUi": True}}})
    req.append({"setDataValidation": {"range": rng(2, 3), "rule": {"condition": {"type": "ONE_OF_LIST", "values": [{"userEnteredValue": a.asignee}]}, "strict": False, "showCustomUi": True}}})
    req.append({"setDataValidation": {"range": rng(3, 4), "rule": {"condition": {"type": "ONE_OF_LIST", "values": [{"userEnteredValue": a.reporter}]}, "strict": False, "showCustomUi": True}}})
    # mau theo gia tri
    i = 0
    for t, nen, chu in TRANG_THAI:
        req.append({"addConditionalFormatRule": {"index": i, "rule": {"ranges": [rng(1, 2)], "booleanRule": {"condition": {"type": "TEXT_EQ", "values": [{"userEnteredValue": t}]},
                    "format": {"backgroundColor": hx(nen), "textFormat": {"foregroundColor": hx(chu)}}}}}}); i += 1
    req.append({"addConditionalFormatRule": {"index": i, "rule": {"ranges": [rng(2, 3)], "booleanRule": {"condition": {"type": "TEXT_EQ", "values": [{"userEnteredValue": a.asignee}]},
                "format": {"textFormat": {"foregroundColor": hx("#126e8c")}}}}}}); i += 1
    req.append({"addConditionalFormatRule": {"index": i, "rule": {"ranges": [rng(3, 4)], "booleanRule": {"condition": {"type": "TEXT_EQ", "values": [{"userEnteredValue": a.reporter}]},
                "format": {"backgroundColor": hx("#c9daf8"), "textFormat": {"foregroundColor": hx("#1c4587")}}}}}})
    # canh le vung du lieu
    req.append({"repeatCell": {"range": rng(1, 4), "cell": {"userEnteredFormat": {"horizontalAlignment": "CENTER", "verticalAlignment": "MIDDLE", "textFormat": {"fontFamily": FONT, "fontSize": 12}}},
                               "fields": "userEnteredFormat(horizontalAlignment,verticalAlignment,textFormat.fontFamily,textFormat.fontSize)"}})
    req.append({"repeatCell": {"range": rng(4, 9), "cell": {"userEnteredFormat": {"wrapStrategy": "WRAP", "verticalAlignment": "MIDDLE", "textFormat": {"fontFamily": FONT, "fontSize": 12}}},
                               "fields": "userEnteredFormat(wrapStrategy,verticalAlignment,textFormat.fontFamily,textFormat.fontSize)"}})
    # cong thuc bang REPORT
    cot = '$F$2&"%d:"&$F$2' % a.dong_dau
    dem = lambda r: '=COUNTIF(INDIRECT(%s)%sREGEXEXTRACT(E%d%s"\\(([^)]+)\\)"))' % (cot, sep, r, sep)
    hang = [[{"userEnteredValue": {"formulaValue": dem(r)}}] for r in range(3, 9)]
    hang.append([{"userEnteredValue": {"formulaValue": "=COUNTA(INDIRECT(%s))" % cot}}])
    req.append({"updateCells": {"start": {"sheetId": sid, "rowIndex": 2, "columnIndex": 5}, "rows": [{"values": h} for h in hang], "fields": "userEnteredValue"}})

    json.dump(req, open(a.ra, "w", encoding="utf-8"), ensure_ascii=False)
    print("Đã dựng %d yêu cầu vào %s" % (len(req), a.ra))


if __name__ == "__main__":
    main()
