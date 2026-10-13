# Cấu hình dự án: <Tên dự án>

Mỗi dự án một file trong thư mục `_du-an/`. Skill chọn file có **Thư mục dự án** chứa thư mục đang làm việc.
Đường dẫn tương đối tính từ Thư mục dự án. Mục nào dự án không có thì ghi "—".
Template để "—" thì skill dùng bản trong `_mau-chung/` của Skill BA.

## Chung

| Khóa | Giá trị |
|:---|:---|
| Thư mục dự án | C:\đường\dẫn\tới\repo |
| Người phân tích | <Họ tên BA> |
| Người duyệt | <Họ tên PO/người duyệt> |
| Thư mục biên bản họp | — (mặc định <thư mục dự án>/Bien-ban-hop/) |
| Vai trò người dùng hệ thống | <Danh sách vai trò, portal> |

## CR

| Khóa | Giá trị |
|:---|:---|
| Thư mục CR | docs/CR |
| Quy tắc đặt tên CR | Thư mục `CR-YYMM` theo tháng viết, file `CR-YYMM-NNN - <Tên thay đổi>.md`, note `CR-YYMM-NNN.note.md`, ảnh ở `CR-YYMM/_attachments/crNNN-scrNN-<tên-ngắn>.png` |
| Template CR | — |
| CR mẫu văn phong | — (không bắt buộc, template đã đủ) |

## SRS

| Khóa | Giá trị |
|:---|:---|
| Thư mục SRS | docs/SRS |
| Template SRS | — |
| SRS mẫu văn phong | — |
| Thư mục quy tắc nghiệp vụ | — |

## Tài liệu mẫu (không bắt buộc, chỉ để bắt giọng văn)

| Khóa | Giá trị |
|:---|:---|
| BRD mẫu | — |
| FSD mẫu | — |
| Screen flow mẫu | — |
| Câu hỏi mở mẫu | — |
| File điều phối mẫu | — (file điều phối checklist testcase của dự án khác, để dựng file cho dự án này) |

## Thiết kế

| Khóa | Giá trị |
|:---|:---|
| Repo thiết kế | — |
| Lệnh chạy thiết kế | — |
| Hệ thống thật để đối chiếu | — |

## Testcase

| Khóa | Giá trị |
|:---|:---|
| File điều phối checklist | — (chưa có thì `/viet-testcase` hỏi và tạo) |
| Thư mục checklist dùng chung | — (để trống thì dùng `<SKILL_BA>/_mau-chung/checklist/` nếu có) |
| Template testcase | — |
| Mẫu bảng testcase | — (bỏ trống thì skill dò theo file testcase có sẵn của dự án, không có thì dùng `_mau-chung/Testcase_Mau-bang-mac-dinh.md`) |
| Nơi đặt file testcase | Cạnh SRS: `<tên>.test.md`, `<tên>.auto.md`, `<tên>.note.md` |

| Mã truy vết | US,YC,SCR,UC,BR,AC (mã nào testcase ghi để truy vết thì giữ) |
| File thuật ngữ | — (bảng thuật ngữ có sẵn của dự án, hoặc tạo `<SKILL_BA>/_du-an/<tên>.thuat-ngu.md` theo `_mau-chung/thuat-ngu_mau.md`) |

## Automation

Chế độ A (viết script từ testcase đã duyệt):

| Khóa | Giá trị |
|:---|:---|
| Repo automation | — (không có repo thì chỉ dùng được chế độ B) |
| Công cụ | <Playwright TS / Selenium + Pytest ...> |
| Môi trường chạy | <stg, URL> |
| Quy ước của repo | <đường dẫn CLAUDE.md của repo automation> |

Chế độ B (kiểm hệ thống khi chưa có testcase). Skill đọc các khóa này trước, chỉ hỏi khóa còn trống rồi ghi câu trả lời ngược lại vào đây:

| Khóa | Giá trị |
|:---|:---|
| Link từng cổng | <tên cổng: URL đăng nhập> |
| File thông tin đăng nhập | <chỉ ghi đường dẫn, không chép nội dung> |
| Email test gốc | <email để tạo tài khoản dạng +alias> |
| Cách đọc email | <hộp thư bắt giữ của môi trường test / IMAP, Gmail API bằng khóa người dùng cấp / người dùng tự dán liên kết vào file> |
| Được gửi email thật | <có / không / hỏi trước mỗi lần> |
| Khóa tài khoản theo | <tài khoản / IP / chưa rõ> |
| Thư mục Automation | <thư mục kịch bản và kết quả trong dự án> |
| Thư mục design | <đường dẫn bộ design hoặc mockup, phiên bản, ngày> |
| Thao tác cấm | <ví dụ: không xóa dữ liệu thật, không khóa tài khoản dùng chung> |
| Cách dọn dữ liệu thử | <xóa qua giao diện / nhờ dev xóa trong cơ sở dữ liệu, giới hạn số bản ghi được tạo> |
| Người dùng có dùng Safari, điện thoại | <có / không>. Có thì chạy thêm WebKit, khổ điện thoại |

## Sơ đồ

| Khóa | Giá trị |
|:---|:---|
| Phân rã chức năng | Bắt buộc trước BRD/FSD. Với CR/SRS: khi chức năng mới có từ 2 chức năng con |
| Dạng sơ đồ trong tài liệu | Ảnh PNG (bắt buộc khi tài liệu xuất docx) hoặc Mermaid (tài liệu chỉ đọc bằng Markdown) |
| Thư mục ảnh sơ đồ | — |

## Google Drive

| Khóa | Giá trị |
|:---|:---|
| Khóa service account | C:/Users/<tên máy>/.secrets/google-sa.json (chỉ ghi đường dẫn, không chép nội dung khóa) |
| Email service account | — (lấy bằng lệnh whoami, dùng để chia sẻ thư mục Drive) |
| Thư mục Drive | — (link thư mục chứa tài liệu gửi sếp, đã chia sẻ quyền Người chỉnh sửa cho email service account) |

**Tài liệu đã gửi**

| File ở máy | Link Google | Loại | Ngày gửi |
|:---|:---|:---|:---|

## Ghi chú riêng của dự án

- <Thuật ngữ, quy ước riêng cần nhớ khi viết>
