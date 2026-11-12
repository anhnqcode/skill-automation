---
name: cap-nhat-srs
description: Gộp CR đã duyệt vào các SRS bị ảnh hưởng, viết lại thành mô tả hệ thống hiện hành, thêm lịch sử thay đổi. Dùng khi gọi /cap-nhat-srs <mã CR> hoặc nhờ cập nhật SRS theo CR.
argument-hint: "<mã CR, ví dụ CR-2610-008> [| ghi chú thêm]"
---

# Cập nhật SRS theo CR: $ARGUMENTS

Trả lời người dùng bằng tiếng Việt, gọi người dùng theo cách đã lưu trong memory.

## Bước 0. Nạp cấu hình

1. Thư mục Skill BA: `cat ~/.claude/skills/.skill-ba-root`. Gọi là `<SKILL_BA>`.
2. Đọc `<SKILL_BA>/_chung/van-phong.md`. Bắt buộc.
3. Chọn file cấu hình dự án trong `<SKILL_BA>/_du-an/` có **Thư mục dự án** chứa thư mục đang làm việc.
4. `$ARGUMENTS` trống thì hỏi mã CR.

## Bước 0b. Tư duy và phân tích

Làm **đầu tiên**, trước khi đọc template hay viết: theo `<SKILL_BA>/_chung/tu-duy-phan-tich.md`, **mức đầy đủ**. In khối "Phân tích" ngắn cho người dùng xem. Có câu hỏi chặn thì hỏi và chờ, không có thì làm tiếp. Lưu khối này vào đầu file note.

## Bước 1. Đọc CR

1. Tìm file CR và `.note.md` theo mã trong Thư mục CR. Đọc trọn cả hai.
2. Người dùng gọi skill này nghĩa là CR đã được duyệt. Các điểm trong note còn ở bảng "tự chốt — cần BA xác nhận" thì coi là đã được chấp nhận, trừ khi người dùng nói khác.
3. Lập danh sách thay đổi từ mục 3 và mục 4 của CR: mỗi dòng gồm quy tắc mới/đổi, mục 3.x nguồn, AC liên quan.

## Bước 2. Xác định SRS cần sửa

1. Bắt đầu từ bảng "Tài liệu bị ảnh hưởng" của CR.
2. Rà thêm: grep tên màn, tên nút, tên trường, tên trạng thái mà CR đổi trên toàn bộ Thư mục SRS (cả thư mục lồng sâu) và Thư mục quy tắc nghiệp vụ. SRS nào mô tả cùng hành vi mà CR chưa ghi thì đưa vào danh sách, báo người dùng ở Bước 6.
3. Mở từng SRS, đọc trọn file cùng `.note.md` đi kèm nếu có.
4. Thay đổi lớn ngoài phạm vi CR (phải sửa cả một module khác, hay phải viết SRS mới) thì hỏi người dùng trước.

## Bước 3. Sửa SRS

Với mỗi SRS, đi lần lượt các phần sau và sửa những chỗ thay đổi chạm tới:

| Phần SRS | Việc làm |
|:---|:---|
| Thông tin chung, Lịch sử thay đổi | Thêm một dòng: phiên bản tăng một bậc nhỏ, ngày hôm nay, mô tả ngắn, Tham chiếu CR là mã CR, người thực hiện lấy từ cấu hình |
| Mô tả, tiền điều kiện, hậu điều kiện | Sửa nếu phạm vi chức năng đổi |
| Sơ đồ luồng và bảng bước | Thêm, sửa bước. Mermaid sửa theo |
| Thành phần giao diện | Thêm, sửa dòng field, nút, cột. Độ dài ghi ở cột Loại, đủ min–max |
| Ảnh màn hình | Theo mục "Cập nhật ảnh" bên dưới |
| Business Rules | Sửa BR cũ thay vì thêm BR mới nói ngược lại. BR mới lấy số kế tiếp |
| Trạng thái màn hình | Thành phần giao diện mới phải có đủ 6 trạng thái |
| Use case | Sửa luồng chính, luồng ngoại lệ |
| AC | Thêm AC từ mục 4 của CR, viết lại theo khung AC của SRS. AC cũ bị thay thì sửa hoặc xóa |

Quy tắc khi gộp:

- **SRS mô tả hệ thống hiện hành, không kể lịch sử.** Viết thẳng "Hệ thống …". Mã CR chỉ xuất hiện ở Lịch sử thay đổi và Tài liệu tham chiếu, không rải vào mô tả, BR, AC.
- **Xóa hẳn nội dung cũ đã bị CR thay.** Không giữ lại kèm chú thích "trước đây", "đã đổi theo CR".
- CR chỉ viết phần thay đổi, nhưng SRS phải đầy đủ. Khi gộp, nối quy tắc mới vào quy tắc cũ cho liền mạch, đừng dán nguyên văn mục CR vào.
- Giữ văn phong của SRS mẫu (ghi ở cấu hình): bảng có alignment marker, BR và AC dạng bảng ID | Nội dung, UC dạng câu đánh số kết thúc bằng **Kết thúc** in đậm.
- CR ghi "sửa mô tả cũ cho đúng với hệ thống đang chạy" thì sửa luôn.
- Điểm CR và SRS mâu thuẫn mà CR không nói tới: tự chốt theo hướng hợp lý, ghi vào `.note.md` của SRS mục "Các điểm đã chốt", báo ở Bước 6.

### Cập nhật ảnh

Chỉ thay ảnh ở chỗ CR thay đổi. Ảnh của phần màn không đổi giữ nguyên, không chụp lại cả màn.

1. Lấy ảnh phần Sau của CR (trong `_attachments` của CR), copy sang `_attachments` của SRS, đặt ngay ở mục mô tả chỗ thay đổi đó.
2. SRS đang có ảnh cũ đúng chỗ đó thì thay bằng ảnh mới, xóa ảnh cũ. Không giữ cả hai.
3. CR không có ảnh cho chỗ thay đổi thì chụp riêng chỗ đó từ hệ thống đã có bản sửa (Production chỉ xem, không sửa dữ liệu thật; không thì stg, repo thiết kế). Chụp không được thì báo ở Bước 6.

### Khi nào hỏi

- Hỏi ngay và chờ: thay đổi làm đổi phạm vi hoặc nghiệp vụ, CR và hệ thống đang chạy khác nhau ở chỗ quan trọng, phải sửa module ngoài CR hoặc phải viết SRS mới.
- Tự chốt, ghi vào note, cuối lượt báo lại: các điểm nhỏ như câu chữ, cách gộp BR, đánh số.

## Bước 4. Tự rà

- Grep lại toàn SRS các từ khóa của quy tắc cũ (giá trị cũ, tên cũ, số cũ) để chắc không còn chỗ nào viết theo hành vi cũ.
- Mọi AC trong mục 4 của CR đã có AC tương ứng trong SRS.
- Rà văn phong theo mục 8 của `van-phong.md`.

## Bước review độc lập

Sau khi tự review, giao các SRS vừa sửa (chỉ khi sửa từ 2 SRS trở lên), nguồn đối chiếu là CR cho một agent mới review theo `<SKILL_BA>/_chung/review-doc-lap.md`. Lỗi rõ ràng thì sửa luôn, điểm cần BA quyết đưa vào danh sách đề xuất khi báo lại. Ghi kết quả vào note mục "Review độc lập".

## Bước 4b. Gộp testcase của CR

Làm khi cạnh CR có `CR-YYMM-NNN.test.md` ở trạng thái **Chưa gộp**. Không có file này thì bỏ qua, cuối lượt gợi ý chạy `/viet-testcase` cho các SRS đã sửa.

1. Với mỗi phần của file (mỗi phần ứng một SRS đích), mở `.test.md` của SRS đó:
   - `Gộp: Mới`: cấp mã chính thức nối tiếp mã lớn nhất của file, thêm vào đúng nhóm (chưa có nhóm thì tạo theo cấu trúc nhóm của file), bỏ dấu "Gộp:" khỏi Ghi chú.
   - `Gộp: Sửa TC-xxx`: thay nội dung case TC-xxx bằng nội dung mới, **giữ mã TC-xxx**. Cột Kết quả thực tế để trống.
   - Bảng "Case cũ bỏ khi gộp": **xóa hẳn** các case đó khỏi file.
   - Cập nhật bảng tổng hợp số lượng ở đầu file.
2. Cập nhật `.auto.md` cạnh SRS: case bị sửa thì xem lại tầng và tên script; case bị xóa mà đã có script thì **báo người dùng**, không tự xóa script.
3. Ghi bảng đối chiếu **mã tạm → mã chính thức** vào `.note.md` của từng SRS và vào đầu file testcase CR. Đổi trạng thái file testcase CR thành **Đã gộp** kèm ngày và các file đã gộp vào. Giữ lại file này.
4. Rà văn phong và đối chiếu: mọi AC mới trong SRS có ít nhất một case.
5. **Đẩy Testcase List:** dự án có công cụ đồng bộ sheet (ghi ở cấu hình hoặc quy ước repo automation) thì chạy thử (`--dry-run`), báo số dòng thêm, sửa, xóa, người dùng đồng ý mới đẩy thật.
6. Gợi ý một dòng: chạy `/viet-automation` chế độ A cho các case mới, giờ đã có mã chính thức.

## Bước 5. Cập nhật CR

Thêm một dòng vào Lịch sử phê duyệt của CR: ngày hôm nay, người phân tích, "Cập nhật SRS", ghi tên các SRS đã sửa. Trạng thái CR chỉ đổi khi người dùng yêu cầu.

## Bước 6. Báo lại và dừng

- Danh sách SRS đã sửa (link markdown) kèm các mục đã đổi.
- SRS ngoài bảng tác động của CR đã phát hiện và đã sửa (nếu có).
- Các điểm đã tự chốt.
- Ảnh đã thay (tên ảnh, lấy từ CR hay chụp mới) và ảnh chưa thay được.
- Testcase: đã gộp bao nhiêu case mới, sửa bao nhiêu, xóa bao nhiêu vào từng `.test.md`, bảng đối chiếu mã, script cần xử lý do case bị xóa, kết quả đẩy Testcase List. CR chưa có file testcase thì gợi ý chạy `/viet-testcase` cho từng SRS.

Dừng, chờ người dùng duyệt.
