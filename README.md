# Skill Automation và Log bug

Bộ skill Claude Code dùng cho công việc BA / QA. Mỗi skill là một quy trình làm việc đóng gói sẵn: gọi `/tên-skill` trong Claude Code kèm mô tả ngắn là chạy.

## Skill trong gói

| Lệnh | Việc làm |
|:---|:---|
| `/viet-automation` | Automation test theo hai chế độ. Chế độ A - đã có bộ testcase duyệt - lập .auto.md và viết script còn thiếu theo quy ước repo automation. Chế độ B - dev vừa code xong, chưa có testcase - dùng Playwright kiểm thẳng bản đã deploy, phủ rộng chứ không chỉ happy path - đối chiếu UI với design và FSD, validate, CRUD, biên, dữ liệu kỳ quặc, trạng thái lỗi, hết phiên, phân quyền, ảnh hưởng chéo - chụp lại mọi lỗi, xuất file kết quả, quay video luồng E2E có chú thích khi được yêu cầu, chuyển sang /log-bug. Dùng khi gọi /viet-automation, nhờ làm automation cho bộ testcase, hoặc nhờ dùng automation kiểm hệ thống dev vừa làm xong. |
| `/log-bug` | Ghi bug vào file bug Google Sheet theo mẫu của team, kèm ảnh ghi chú và bảng REPORT. Dùng khi gọi /log-bug hoặc nhờ ghi, log bug cho dev. |

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
- Skill dùng Google Sheet cần một service account riêng của bạn. Khóa đặt ngoài thư mục skill, không đưa lên git.
- Không đưa thư mục `_du-an/` có cấu hình dự án thật lên repo công khai.

- Gói này có nhắc tới skill chưa kèm theo: `/viet-testcase`. Bước đó làm tay hoặc xin thêm skill.
