---
name: verify-bug
description: Kiểm lại các bug dev báo đã sửa (Resolved) trên file bug Google Sheet, kèm vài mục hồi quy liên quan, đo đạc cụ thể trên trang bằng Playwright có giao diện, chạy chậm, có dải chữ báo bug đang kiểm. Đạt thì chuyển Passed, còn lỗi thì Reopen kèm ghi chú và ảnh. Chuyển Closed sau khi build Production thành công. Dùng khi gọi /verify-bug hoặc nhờ verify, kiểm lại bug dev đã fix.
argument-hint: "<link Google Sheet file bug> [| môi trường / URL] [| ID bug] [| closed: đợt build Production]"
---

# Kiểm lại bug đã sửa: $ARGUMENTS

Vai trò: tester kiểm lại bug sau khi dev sửa. Kết luận dựa trên **số đo trên trang** (chữ, giá trị, trạng thái, kích thước, vị trí, màu, số lượng, phản hồi API), không chỉ nhìn ảnh.
Trả lời người dùng bằng tiếng Việt, gọi người dùng theo cách đã lưu trong memory.

## Bước 0. Nạp cấu hình

1. Thư mục Skill BA: `cat ~/.claude/skills/.skill-ba-root`. Gọi là `<SKILL_BA>`.
2. Đọc `<SKILL_BA>/_chung/van-phong.md` và `<SKILL_BA>/log-bug/mau-bang-bug.md` (bố cục sheet, cột, văn phong Note).
3. Chọn file cấu hình dự án trong `<SKILL_BA>/_du-an/`: khóa service account, link file bug, thư mục ảnh bug, mục Automation (thư mục kịch bản, tài khoản test, môi trường).
4. `GAPI` = `node "<SKILL_BA>/scripts/google_api.mjs" <lệnh> ... --key "<Khóa service account>"`. Không bao giờ đọc, in hay chép nội dung file khóa.

## Bước 0b. Tư duy và phân tích

Theo `<SKILL_BA>/_chung/tu-duy-phan-tich.md`, mức gọn: môi trường nào đã có bản sửa, bug nào cần kiểm, bug nào làm đổi dữ liệu (cần trả dữ liệu về như cũ), bug nào cần tài khoản hay dữ liệu đặc biệt.

## Bước 1. Lấy danh sách bug cần kiểm

1. `GAPI sheet-read <link> "<tab>!A11:I2000"`, lấy các dòng Status = **Resolved**. Người dùng đưa ID thì chỉ lấy các ID đó.
2. Bug Todo, Inprogress, Pending, Reopen giữ nguyên, không kiểm.
3. Với mỗi bug, đọc Summary, Step to reproduce, Result (Actual, Expect), Note, ảnh. Viết ra **tiêu chí đạt đo được**: Expect nói gì thì đo cái đó. Ví dụ "nút Lưu bật khi đủ dữ liệu" → đo trạng thái khóa của nút. "Tên dài không tràn" → đo tràn ngang của ô. "Hiện popup xác nhận" → đo popup có hiện và đúng chữ. Expect mơ hồ, không đo được thì hỏi người dùng trước khi kiểm.
4. Chọn **vài mục hồi quy** cho mỗi bug, theo chỗ sửa có thể ảnh hưởng:
   - Cùng màn: các nút, trường, thao tác ngay cạnh chỗ sửa.
   - Cùng thành phần dùng chung: màn khác dùng cùng component, cùng API.
   - Luồng trước và sau: bước trước và sau thao tác bị lỗi.
   - Khổ màn hình khác, nếu bug là giao diện.
   - Dữ liệu biên quanh giá trị trong Step (rỗng, dài, giá trị kế bên).
   Mỗi bug 2 đến 4 mục hồi quy, không chạy lại cả bộ testcase.

## Bước 2. Viết kịch bản kiểm

1. Dùng bộ hàm `<SKILL_BA>/verify-bug/mau_verify.py` (Python Playwright). Dự án dùng Playwright TypeScript thì làm theo cùng cách trong repo đó. Đặt kịch bản trong thư mục Automation của dự án, tên `verify_<ngày>.py`.
2. Mỗi bug một hàm: làm theo Step to reproduce, rồi **đo** và **so sánh** với tiêu chí đạt bằng `do()`, `do_nhieu()`, `so_sanh()`. Đo cả phản hồi API khi Expect liên quan dữ liệu (`page.expect_response`). Ghi kết quả bằng `in_ket_qua()`.
3. Mỗi bước gọi `dai_chu(page, "Bug #<ID> - <Summary>", "Bước x/y: <việc đang làm>")` để người xem biết đang kiểm gì. Kết luận xong mỗi bug thì đổi dải chữ sang `dat` hoặc `khong-dat` và dừng 2 giây.
4. Chụp bằng chứng bằng `chup()` (dải chữ tự ẩn khi chụp) cho mọi bug **không đạt**.
5. Thao tác làm đổi dữ liệu (tạo, sửa, xóa, đổi trạng thái) thì trả dữ liệu về như cũ ngay sau khi đo.
6. Bug cần kiểm ở nhiều khổ màn hình: đo ở từng khổ bằng `doi_kho()` (ví dụ 1280 × 720, 1366 × 768, 1440 × 900, 1920 × 1080, 390 × 844 cho điện thoại). Khổ nào lỗi thì ghi rõ khổ đó.

## Bước 3. Chạy

- **Chạy để người dùng xem:** `mo(p, xem=True, kho=(1920, 1080), cham=500)`. Trình duyệt có giao diện, chạy chậm, cửa sổ và khung nhìn 1920 × 1080, dải chữ hiện trên cùng trang. Đây là chế độ mặc định của skill.
- Bug cần kiểm khổ responsive: khung nhìn đổi theo khổ đang kiểm bằng `doi_kho()`, xong thì trả về 1920 × 1080.
- Người dùng nói chạy nền, không cần xem: `xem=False`.
- Chạy nền khi kịch bản dài, báo người dùng mở cửa sổ trình duyệt để theo dõi.

## Bước 4. Kết luận từng bug

| Kết quả đo | Status mới | Ghi chú |
|:---|:---|:---|
| Mọi tiêu chí đạt, mục hồi quy đạt | **Passed** | Không ghi Note |
| Còn lỗi ở tiêu chí của bug | **Reopen** | Note thêm một dòng: `Verify <dd/mm> trên <môi trường>: <hiện tượng còn lại, số đo thực tế so với mong muốn>`. Ảnh mới gắn vào cột Image theo Bước 7 của `/log-bug`. Asignee giữ nguyên |
| Bug đạt nhưng mục hồi quy lỗi | Bug gốc: **Passed** | Lỗi hồi quy ghi thành **bug mới** theo `/log-bug`, Note của bug mới ghi "Phát sinh sau khi sửa bug #<ID gốc>" |
| Không kiểm được (môi trường chưa có bản sửa, thiếu dữ liệu, thiếu tài khoản) | Giữ **Resolved** | Báo người dùng lý do, không ghi Note |
| Kết quả đo khó kết luận (Expect có hai cách hiểu, lỗi lúc có lúc không) | Giữ **Resolved** | Hỏi người dùng trước khi đổi |

Ghi Status bằng `GAPI sheet-write <link> "<tab>!B<dòng>" '[["Passed"]]'`. Nối thêm Note, không ghi đè nội dung Note cũ. Đọc lại bảng REPORT sau khi ghi: số Resolved giảm, Passed và Reopen tăng đúng số vừa đổi.

## Bước 5. Chuyển Closed

Chỉ làm khi người dùng báo **build Production thành công** (`/verify-bug <link> | closed: <đợt build>`).

1. Hỏi rõ đợt build gồm những bug nào nếu người dùng chưa nói (thường là mọi bug đang Passed).
2. Chuyển các bug đó từ Passed sang **Closed**. Không đổi bug ở trạng thái khác.
3. Người dùng muốn kiểm nhanh trên Production trước khi đóng thì chạy lại Bước 2, 3 với URL Production, chỉ thao tác chỉ đọc, không tạo hay sửa dữ liệu thật.

## Báo lại

- Bảng: ID | Summary | Kết quả | Status mới | Số đo chính (thực tế so với mong muốn).
- Bug mới phát sinh từ hồi quy (đã ghi bằng `/log-bug`).
- Bug chưa kiểm được và lý do.
- Ảnh cần kéo lên thư mục ảnh bug (bug Reopen), theo cách ở `/log-bug` Bước 7.
- Đường dẫn kịch bản để chạy lại lần sau.
