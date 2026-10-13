# Bộ checklist áp dụng cho <Tên dự án>

File điều phối: ghi dự án dùng checklist nào. Skill `/viet-testcase` tự dựng file này bằng cách dò dấu hiệu theo `checklist/_danh-muc.md`, người dùng chỉ cần xem lại, bật mục nào, chạy theo thứ tự nào. Quy tắc chung nằm ở các file checklist dùng chung, sửa ở đó. File này chỉ ghi phần riêng của dự án. Copy file này vào thư mục testcase của dự án, đổi tên thành `00-checklist-ap-dung.md`, điền các chỗ trong ngoặc nhọn, rồi ghi đường dẫn vào khóa **File điều phối checklist** của cấu hình dự án.

Cập nhật lần cuối: <DD/MM/YYYY>

---

## 1. Bối cảnh dự án

<3 đến 6 câu: hệ thống làm gì, các nhóm người dùng, nền tảng (web, mobile, thiết bị), luồng chính, kết quả nào của hệ thống ảnh hưởng tiền thật, dữ liệu cá nhân, văn bản pháp lý. Phần này quyết định checklist nào được bật ở mục 3.>

Testcase viết theo **nghiệp vụ thật** của tài liệu đặc tả (SRS, FSD, CR) và hệ thống đang chạy.

---

## 2. Thứ tự chạy

Chạy đúng thứ tự. Đảo thứ tự thì bộ case vẫn đủ số lượng nhưng sai trọng tâm.

| Bước | Việc làm | File |
|---|---|---|
| 0 | Lập danh sách rủi ro trọng tâm của chức năng, đặt lên đầu file note | `QA-Adversarial-Integrity-Checklist.md` Mục A |
| 1 | Điền bảng tham số (con số, mốc thời gian, giới hạn) và đọc các mâu thuẫn tài liệu. Ô nào trống hoặc mâu thuẫn thì hỏi BA trước, không viết case đoán mò | Bảng thông tin đầu mỗi file tầng 3 được bật |
| 2 | Chạy checklist nền cho từng màn | `Testcase_Template.md` |
| 3 | Chạy checklist rủi ro nghiệp vụ chung (bật từng nhóm theo dấu hiệu), rồi bộ domain nếu có | `QA-Business-Risk-Core-Checklist.md`, `domain/domain-*.md` |
| 4 | Chạy các checklist năng lực theo bảng ở mục 3 | các file `QA-*` |
| 5 | Chạy file tư duy đối kháng để soát lại trọng tâm và quyết định case nào lên mức cao nhất | `QA-Adversarial-Integrity-Checklist.md` |
| 6 | Rà soát cuối: sáu trạng thái màn hình và các câu hỏi rà soát | `QA-States-Errors-Notification-Checklist.md` Mục H |
| 7 | Đối chiếu: mọi BR/AC của chức năng có ít nhất một case | — |
| 8 | Lập file automation song song (nếu dự án có automation): chọn tầng theo bảng ở `Automation_Checklist.md` | `Automation_Checklist.md` |

---

## 3. Bảng bật tắt

Đánh dấu file nào bật, bật mục nào, vì sao. File không liên quan thì đưa xuống dòng "Tắt".

| File | Bật khi | Bật gì | Ghi chú của dự án |
|---|---|---|---|
| `Testcase_Template.md` | Luôn bật | Toàn bộ | Nền tảng, không có ngoại lệ |
| `QA-Business-Risk-Core-Checklist.md` | Luôn bật | Các nhóm khớp dấu hiệu | Tầng 1, rủi ro nghiệp vụ chung |
| `QA-States-Errors-Notification-Checklist.md` | Luôn bật | Toàn bộ | Sáu trạng thái màn hình, bảng lỗi, thông báo đa kênh |
| `QA-Adversarial-Integrity-Checklist.md` | Hệ thống có tiền, điểm, xếp hạng, quyền duyệt, dữ liệu nhạy cảm | <mục> | |
| `Template_Testcase_Advanced.md` | Có realtime, hàng đợi, offline, ghép nối, chuỗi nhiều bước, tích hợp ngoài | <mục> | |
| `QA-Mobile-Native-Checklist.md` | Có app mobile | <mục> | |
| `QA-Identity-Account-Linking-Checklist.md` | Có tài khoản, đăng nhập mạng xã hội, xác minh danh tính, dữ liệu cá nhân | <mục> | |
| `QA-Metrics-Listing-Checklist.md` | Có dashboard, báo cáo, danh sách có bộ lọc, số liệu tổng hợp | <mục> | |
| `QA-Public-Share-Link-Checklist.md` | Có trang mở được bằng liên kết không cần đăng nhập, mã QR | <mục> | |
| `QA-AI-Assisted-Review-Checklist.md` | Có chức năng AI đề xuất để người duyệt | <mục> | |
| `QA-Data-Crawling-Checklist.md` | Có thu thập dữ liệu từ nguồn ngoài | <mục> | |
| `QA-Scoring-RuleBase-Checklist.md` | Có chấm điểm theo bộ quy tắc | <mục> | |
| `QA-Ranking-Leaderboard-Checklist.md` | Có xếp hạng, bảng xếp hạng | <mục> | |
| `QA-TV-App-Checklist.md` | Có app TV, điều khiển bằng D-pad | <mục> | |
| `QA-Voice-Interaction-Checklist.md` | Có điều khiển bằng giọng nói, đọc thành tiếng | <mục> | |
| `Automation_Checklist.md` | Dự án có automation | <nhóm> | |

**Tắt, không dùng:** <danh sách file>.

---

## 4. Quy tắc riêng của dự án

<Tối đa 5 quy tắc. Ví dụ: máy chủ quyết định, giao diện chỉ hiển thị nên mọi thao tác bị chặn trên giao diện phải có thêm case gửi thẳng API; thời điểm tính theo giờ máy chủ; không có con số thì không viết kết quả mong muốn.>

1. <Quy tắc>

---

## 5. Mẫu bảng và quy tắc nâng mức ưu tiên

- Mẫu bảng testcase: <các cột, theo khóa Mẫu bảng testcase ở cấu hình dự án>.
- Thang ưu tiên: <P0 / P1 / P2 hoặc High / Medium / Low>.
- Case chạm vào <tiền, dữ liệu cá nhân, văn bản pháp lý, kết quả quyết định, mất dấu vết...> luôn ở mức cao nhất.
- Các file tầng 3 có mẫu bảng riêng thì bỏ mẫu đó, dùng mẫu bảng của dự án, quy đổi thang ưu tiên cho khớp.

---

## 6. Câu hỏi chặn còn treo

Chưa có câu trả lời thì nhóm case tương ứng chưa viết được kết quả mong muốn. Viết phần khác trước, ghi câu hỏi vào file note của chức năng.

| Câu hỏi | Nguồn | Chặn nhóm nào |
|---|---|---|
| <Câu hỏi> | <tài liệu, mục> | <checklist, mục> |
