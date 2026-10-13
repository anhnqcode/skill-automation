---
name: log-bug
description: Ghi bug vào file bug Google Sheet theo mẫu của team, kèm ảnh ghi chú và bảng REPORT, hoặc tạo issue Bug trên Jira khi dự án ghi bug trên Jira. Dùng khi gọi /log-bug hoặc nhờ ghi, log bug cho dev.
argument-hint: "<link Google Sheet file bug | mã task test Jira> | <nguồn bug: file kết quả kiểm thử, danh sách mã bug, hoặc mô tả bug>"
---

# Ghi bug cho dev: $ARGUMENTS

Vai trò: tester ghi bug để dev đọc là sửa được, không phải hỏi lại.
Trả lời người dùng bằng tiếng Việt, gọi người dùng theo cách đã lưu trong memory.

## Bước 0. Nạp cấu hình

1. Thư mục Skill BA: `cat ~/.claude/skills/.skill-ba-root`. Gọi là `<SKILL_BA>`.
2. Đọc `<SKILL_BA>/_chung/van-phong.md` và `mau-bang-bug.md` (cùng thư mục skill này). Bắt buộc.
3. Chọn file cấu hình dự án trong `<SKILL_BA>/_du-an/`. Đọc mục Google Drive (khóa service account) và Ghi chú riêng của dự án (tên cổng, cách gọi các bên).
4. `GAPI` = `node "<SKILL_BA>/scripts/google_api.mjs" <lệnh> ... --key "<Khóa service account>"`. Không bao giờ đọc, in hay chép nội dung file khóa.
5. Thiếu link file bug thì tra bảng Tài liệu đã gửi của dự án, không có thì hỏi.
6. Xem khóa **Nơi ghi bug** trong mục Jira của cấu hình dự án. Là **Jira** thì đọc thêm `mau-bug-jira.md` và làm theo mục "Ghi bug lên Jira" ở cuối file này, bỏ mục 4 tới 6 của bước này.
7. Lấy link **thư mục ảnh bug** trong cấu hình dự án (bảng Tài liệu đã gửi). Chưa có thì hỏi người dùng tạo một thư mục trên Drive, chia sẻ cho email service account (Người xem) và cho dev, rồi ghi link vào cấu hình.

## Bước 0b. Tư duy và phân tích

Làm **đầu tiên**, trước khi đọc template hay viết: theo `<SKILL_BA>/_chung/tu-duy-phan-tich.md`, **mức gọn**. In khối "Phân tích" ngắn cho người dùng xem. Có câu hỏi chặn thì hỏi và chờ, không có thì làm tiếp. Lưu khối này vào đầu file note.

## Bước 1. Đọc file bug

1. `GAPI sheet-info <link>`: locale (quyết định dấu `;` hay `,` trong công thức), id từng tab, số quy tắc màu đang có.
2. `GAPI sheet-read <link> "<tab>!A1:I30"`: bảng REPORT, dòng tiêu đề, các bug đã có. Ghi nhận ID cuối cùng và văn phong các bug cũ để viết cho đồng bộ.
3. Lỗi 403/404: nhắc người dùng chia sẻ quyền Người chỉnh sửa cho email service account (`GAPI whoami`).

## Bước 2. Dựng khung và công thức (chỉ làm khi sheet chưa có)

Sheet đã có danh sách chọn và màu (sheet-info báo có quy tắc màu) thì bỏ qua bước này, chạy lại sẽ nhân đôi quy tắc màu.

1. Dựng lô yêu cầu:
   - Tab trống: `py "<SKILL_BA>/scripts/tao_bang_bug.py" --ra <tạm>.json --sheet-id <id> --tao-khung`
   - Tab đã có chữ và khung như mẫu, chỉ thiếu công thức và danh sách chọn: bỏ `--tao-khung`.
   - Locale en: thêm `--dau-phay`. Asignee, Reporter khác mặc định thì thêm `--asignee`, `--reporter`.
2. Gửi: `GAPI sheet-batch <link> <tạm>.json`.
3. Đọc lại F3:F9 bằng `sheet-read`. Ra `#ERROR!` thường là sai dấu ngăn tham số.
4. Người dùng thêm giá trị cho danh sách chọn (ví dụ thêm người vào Asignee) thì gửi `setDataValidation` mới cho cột đó cùng một quy tắc màu, không chạy lại cả lô.

## Bước 3. Gom và kiểm lại bug

1. Lấy danh sách bug từ nguồn người dùng đưa: file kết quả kiểm thử, file đối chiếu giao diện, mô tả trong chat. Nguồn là file kết quả của `/viet-automation` chế độ B thì lấy luôn các trường Cổng, Màn, Tab, Bước tái hiện, Thực tế, **Mong muốn cho dev** (làm Expect), Mức độ, ảnh và khổ chụp; bỏ các lỗi có trạng thái Đóng. Bỏ các mục người dùng đã chốt chấp nhận, các mục là lỗi của design (gửi designer, không gửi dev) và các câu hỏi nghiệp vụ.
2. **Kiểm lại trên hệ thống trước khi ghi.** Bug phát hiện từ phiên trước có thể dev đã sửa. Dùng Playwright (skill `viet-automation` hoặc kịch bản có sẵn của dự án) mở lại từng chỗ, chụp màn hình ở đúng khổ đã thấy lỗi, tỉ lệ 2x. Thao tác làm đổi dữ liệu để tái hiện thì phải trả dữ liệu về như cũ ngay sau khi chụp.
3. Bug đã hết thì không ghi, báo người dùng.

## Bước 4. Viết nội dung

Theo đúng mục Văn phong của `mau-bang-bug.md`:

- Summary `[Cổng][Màn][Tab] <mô tả ngắn>`, cổng luôn đứng đầu.
- Step đánh số, mỗi bước một dòng.
- Result `- Actual:` và `- Expect:`. Expect là mong muốn bằng lời thường. **Không dẫn mã BR, mã màn, tên tài liệu.**
- Status Todo, Asignee và Reporter theo mặc định của file (theo file mẫu của dự án). ID nối tiếp ID cuối.
- Note chỉ khi có thêm thông tin cho dev.

Xếp thứ tự: bug mức Cao trước, cùng màn thì để gần nhau. File bug không có cột mức độ nên ghi mức độ vào đầu cột Note khi mức là Cao hoặc Trung bình, ví dụ "Mức Cao: lộ số điện thoại giáo viên khác".

## Bước 5. Vẽ ảnh ghi chú

1. Bug cần hình (giao diện, bố cục, hiển thị sai) mới vẽ. Bug dữ liệu, file xuất, focus bàn phím thì không cần.
2. Xem ảnh chụp để lấy tọa độ CSS của chỗ lỗi.
3. Viết spec JSON rồi chạy `py "<SKILL_BA>/scripts/ve_anh_bug.py" <spec>.json`. Cách viết spec ở đầu script.
4. Đặt tên tệp `<ID>-<mã nội bộ>-<mô tả không dấu>.png`, lưu cạnh kết quả kiểm thử của dự án.
5. Mở lại từng ảnh kiểm tra theo bảng Ảnh ghi chú trong `mau-bang-bug.md`. Sai thì sửa spec, vẽ lại.

## Bước 6. Ghi vào sheet

1. Dòng mới chưa có khung: chép định dạng dòng bug đầu tiên xuống bằng `copyPaste` với `PASTE_FORMAT` qua `GAPI sheet-batch`.
2. `GAPI sheet-write <link> "<tab>!A<dòng>:I<dòng>" <bugs>.json`. Cột Image tạm để trống.
3. Đọc lại bảng REPORT, số Todo và Tổng phải tăng đúng số bug vừa ghi.
4. Nguồn là file kết quả của `/viet-automation`: điền ID dòng trên sheet và trạng thái sheet ngược lại vào từng lỗi BUG-xx trong file kết quả, để lần chạy lại đối chiếu được.

## Bước 7. Gắn liên kết ảnh

Cột Image chứa liên kết "Xem ảnh", dev bấm vào là mở ảnh cỡ lớn trong trình xem Drive. Không chèn ảnh vào ô vì ảnh trong ô quá nhỏ, dev không đọc được.

1. Service account không có dung lượng Drive nên không tự tải ảnh lên được. Báo người dùng kéo các tệp ảnh vừa vẽ vào thư mục ảnh bug, rồi chờ người dùng báo xong.
2. `GAPI drive-list <thư mục ảnh bug>`. Ghép tệp với dòng bug theo ID ở đầu tên tệp. Thiếu tệp nào thì báo người dùng.
3. Kiểm tra trước ô Image của các dòng sắp ghi. Ô đã có nội dung khác thì hỏi người dùng trước khi ghi đè.
4. Ghi vào ô Image công thức `=HYPERLINK("https://drive.google.com/file/d/<id>/view";"Xem ảnh")` (locale en dùng dấu `,`), qua `GAPI sheet-batch` với `updateCells` dùng `formulaValue`. Chữ Times New Roman 12, gạch chân, màu xanh, căn giữa.
5. Đọc lại ô bằng Sheets API (`fields=...values(formattedValue,hyperlink)`) để chắc liên kết đúng tệp.

Không đưa ảnh lên chỗ công khai và không dùng hàm IMAGE, vì IMAGE chỉ hiện được ảnh công khai, mà ảnh chụp có giao diện và dữ liệu hệ thống.

## Ghi bug lên Jira

Dự án có Nơi ghi bug là Jira thì thay Bước 1, 2, 6, 7 bằng các bước sau. Bước 3, 4, 5 giữ nguyên (gom, kiểm lại, viết nội dung, vẽ ảnh).

1. Lấy mã task test từ tham số hoặc từ `/lam-task-jira`. Không có thì hỏi người dùng bug thuộc task nào, vì sprint và version của bug lấy theo task đó.
2. Viết từng bug theo `mau-bug-jira.md`: Summary như Bước 4, mô tả theo mẫu wiki markup, Priority theo mức độ, Sprint và Fix Version theo task test, Env theo môi trường đang test.
3. Tìm bug trùng trước khi tạo, rồi tạo, tải mọi ảnh của bug lên Jira đính kèm vào bug, liên kết với task test theo mục 3 của `mau-bug-jira.md`.
4. Assignee theo **Người nhận bug** trong cấu hình, để trống thì không giao.
5. Nguồn là file kết quả của `/viet-automation`: điền mã bug Jira ngược lại vào từng lỗi BUG-xx.

## Sau khi dev sửa

Dev chuyển bug sang Resolved thì kiểm lại bằng skill `/verify-bug`: đạt thì Passed, còn lỗi thì Reopen, build Production thành công thì Closed.

## Báo lại

- Link file bug (hoặc link từng bug Jira), số bug đã ghi theo ID, kèm một dòng tóm tắt mỗi bug.
- Bug nào kiểm lại thấy đã hết nên không ghi.
- Danh sách ảnh cần kéo lên thư mục ảnh bug (ID dòng và đường dẫn tệp), hoặc xác nhận đã gắn liên kết xong.
- Nhắc người dùng kiểm tra dev đã có quyền xem thư mục ảnh bug.
- Mục bỏ ra vì là lỗi design hoặc câu hỏi nghiệp vụ, để người dùng chuyển đúng người.
