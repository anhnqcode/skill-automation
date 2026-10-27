# Skill SRS, Automation, Testcase, Log bug và Verify bug

Bộ skill Claude Code dùng cho công việc BA / QA. Mỗi skill là một quy trình làm việc đóng gói sẵn: gọi `/tên-skill` trong Claude Code kèm mô tả ngắn là chạy.

## Skill trong gói

| Lệnh | Việc làm |
|:---|:---|
| `/viet-srs` | Viết SRS mới cho một màn hoặc chức năng theo template dự án, tìm SRS cũ trước, đủ trạng thái màn, BR, UC, AC. Có chế độ renew UI cho màn đã có SRS làm lại giao diện, kể cả chuyển bản khi lên Production. Dùng khi gọi /viet-srs hoặc nhờ viết SRS. |
| `/viet-automation` | Automation test theo hai chế độ. Chế độ A - đã có bộ testcase duyệt - lập .auto.md và viết script còn thiếu theo quy ước repo automation. Chế độ B - dev vừa code xong, chưa có testcase - dùng Playwright kiểm thẳng bản đã deploy, phủ rộng chứ không chỉ happy path - đối chiếu UI với design và FSD, validate, CRUD, biên, dữ liệu kỳ quặc, trạng thái lỗi, hết phiên, phân quyền, ảnh hưởng chéo - chụp lại mọi lỗi, xuất file kết quả, quay video luồng E2E có chú thích khi được yêu cầu, chuyển sang /log-bug. Dùng khi gọi /viet-automation, nhờ làm automation cho bộ testcase, hoặc nhờ dùng automation kiểm hệ thống dev vừa làm xong. |
| `/viet-testcase` | Viết testcase manual cho SRS/FSD/CR theo checklist và template dự án, tự nhận mẫu bảng, phủ cả case ngoài SRS. Dùng khi gọi /viet-testcase hoặc nhờ viết testcase. |
| `/log-bug` | Ghi bug vào file bug Google Sheet theo mẫu của team, kèm ảnh ghi chú và bảng REPORT, hoặc tạo issue Bug trên Jira khi dự án ghi bug trên Jira. Dùng khi gọi /log-bug hoặc nhờ ghi, log bug cho dev. |
| `/verify-bug` | Kiểm lại các bug dev báo đã sửa (Resolved) trên file bug Google Sheet hoặc trên Jira, kèm vài mục hồi quy liên quan, đo đạc cụ thể trên trang bằng Playwright, mặc định chạy ngầm, chỉ bật cửa sổ chạy chậm có dải chữ khi người dùng yêu cầu. Đạt thì chuyển Passed (Jira: Done), còn lỗi thì Reopen kèm ghi chú và ảnh (Jira: comment). Chuyển Closed sau khi build Production thành công. Dùng khi gọi /verify-bug hoặc nhờ verify, kiểm lại bug dev đã fix. |

## Cài đặt

1. Cài [Claude Code](https://claude.com/claude-code) (VS Code extension hoặc CLI).
2. Tải gói về:

   ```bash
   git clone <link repo này> "C:/Users/<tên máy>/Desktop/BA/Skill BA"
   ```

3. Cài skill vào Claude Code (chạy lại mỗi khi tải bản mới):

   ```powershell
   powershell -ExecutionPolicy Bypass -File "C:/Users/<tên máy>/Desktop/BA/Skill BA/cai-dat.ps1"
   ```

4. Tạo cấu hình cho dự án của bạn: copy `_du-an/_mau.md` thành `_du-an/<tên dự án>.md` và điền các khóa (thư mục dự án, repo automation, file bug...). Hoặc cứ gọi skill trong thư mục dự án, skill sẽ hỏi và tự tạo file.
5. Mở phiên Claude Code mới, gõ `/` để thấy skill.

## Lưu ý

- Văn phong tài liệu theo `_chung/van-phong.md` (tiếng Việt, câu ngắn, giọng thường). Sửa file này nếu team bạn có quy ước khác.
- Skill dùng Google Sheet cần một service account riêng của bạn. Cách tạo và kết nối: `_chung/ket-noi-google-sheet.md`. Khóa đặt ngoài thư mục skill, không đưa lên git.
- Không đưa thư mục `_du-an/` có cấu hình dự án thật lên repo công khai.

## Bộ checklist sinh testcase

Thư mục `_mau-chung/checklist/` có các checklist dùng chung. Mỗi dự án bật những file phù hợp qua **file điều phối**:

1. Copy `_mau-chung/00-checklist-ap-dung_mau.md` vào thư mục testcase của dự án, đổi tên thành `00-checklist-ap-dung.md`.
2. Điền bối cảnh, bật tắt checklist theo cột "Bật khi", ghi quy tắc riêng và mẫu bảng.
3. Ghi đường dẫn file này vào khóa **File điều phối checklist** của `_du-an/<dự án>.md`. Hoặc gọi `/viet-testcase` khi chưa có file điều phối, skill sẽ hỏi rồi tạo.

Thứ tự đọc: `Testcase_Template.md` (nền, 37 mục) → các checklist được bật → `viet-testcase/tu-duy-test.md` (tìm case ngoài tài liệu).

| File | Nội dung |
|:---|:---|
| `QA-AI-Assisted-Review-Checklist.md` | Checklist Kiểm thử Luồng Máy Chấm, Người Duyệt |
| `QA-Adversarial-Integrity-Checklist.md` | Checklist Tư duy Đối kháng và Liêm chính Dữ liệu |
| `QA-Business-Risk-Core-Checklist.md` | Checklist rủi ro nghiệp vụ chung (tầng 1) |
| `QA-Data-Crawling-Checklist.md` | Checklist Kiểm thử Thu thập Dữ liệu từ Nguồn Ngoài |
| `QA-Identity-Account-Linking-Checklist.md` | Checklist Kiểm thử Danh tính và Liên kết Tài khoản |
| `QA-Metrics-Listing-Checklist.md` | Checklist Kiểm thử Số liệu Tổng hợp và Màn Danh sách Dữ liệu |
| `QA-Mobile-Native-Checklist.md` | Checklist Kiểm thử Native Mobile App (iOS & Android) |
| `QA-Public-Share-Link-Checklist.md` | Checklist Kiểm thử Link & QR Chia sẻ Công khai |
| `QA-Ranking-Leaderboard-Checklist.md` | Checklist Kiểm thử Xếp hạng và Bảng Xếp hạng |
| `QA-Scoring-RuleBase-Checklist.md` | Checklist Kiểm thử Bộ Quy tắc và Chấm điểm |
| `QA-States-Errors-Notification-Checklist.md` | Checklist Kiểm thử Trạng thái màn hình, Lỗi & Thông báo |
| `QA-TV-App-Checklist.md` | Checklist Kiểm thử TV App |
| `QA-Voice-Interaction-Checklist.md` | Checklist Kiểm thử Tương tác bằng Giọng nói |
| `Template_Testcase_Advanced.md` | Checklist Nâng Cao — 7 Dạng Case Đặc Thù |

- Gói này có nhắc tới skill chưa kèm theo: `/cap-nhat-srs`, `/lam-task-jira`, `/ve-so-do-lan`, `/viet-cr`. Bước đó làm tay hoặc xin thêm skill.
