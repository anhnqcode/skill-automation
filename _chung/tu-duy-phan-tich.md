# Tư duy và phân tích trước khi làm

Mọi skill làm bước này **đầu tiên**, sau khi nạp cấu hình và trước khi đọc template hay viết. Mục đích là hiểu đúng bài toán trước khi viết, để không viết cả tài liệu theo một giả định sai.

## Cách trình bày

- Đọc yêu cầu và các nguồn chính (mô tả của người dùng, tài liệu được chỉ tên, SRS/CR liên quan) rồi in ra khối **"Phân tích"** ngắn, khoảng 5 đến 10 gạch đầu dòng, giọng thường theo `van-phong.md`.
- Có câu hỏi chặn: hỏi ngay bằng AskUserQuestion (tối đa 4 câu, phương án đề xuất đặt đầu) và chờ trả lời.
- Không có câu hỏi chặn: làm tiếp luôn, không chờ duyệt.
- Lưu khối Phân tích vào đầu file note của tài liệu (mục "Phân tích ban đầu") để sau tra lại.
- Trong lúc làm phát hiện phân tích ban đầu sai: sửa khối Phân tích trong note và báo người dùng một dòng.

## Mức đầy đủ

Dùng cho `/phan-ra-chuc-nang`, `/viet-brd`, `/viet-fsd`, `/viet-srs`, `/viet-cr`, `/cap-nhat-srs`, `/viet-testcase`. Tự trả lời từng câu, câu nào không liên quan thì bỏ qua, không viết "không áp dụng".

| # | Câu hỏi | Gợi ý |
|:--|:---|:---|
| 1 | **Vấn đề thật là gì?** | Yêu cầu nói "làm X", nhưng X để giải quyết việc gì. Có cách đơn giản hơn để giải quyết đúng việc đó không |
| 2 | **Cho ai, vì sao?** | Vai trò nào được lợi, vai trò nào bị ảnh hưởng. Lý do nghiệp vụ, con số nếu có |
| 3 | **Phạm vi** | Trong phạm vi, ngoài phạm vi, giai đoạn sau. Cổng, nền tảng (web, mobile) |
| 4 | **Chức năng con** | Chức năng này gồm những phần nào. Đủ lớn (từ 2 chức năng con trở lên) thì dùng sơ đồ phân rã |
| 5 | **Dữ liệu và trạng thái** | Đối tượng dữ liệu nào được tạo, sửa, xóa. Có vòng đời trạng thái không. Dữ liệu cũ trước khi thay đổi xử lý ra sao |
| 6 | **Chỗ bị ảnh hưởng** | Màn khác, module khác, cổng khác, báo cáo, thông báo, tích hợp ngoài, quyền |
| 7 | **Trường hợp biên** | Rỗng, quá nhiều, đúng mốc thời gian, thao tác sai thứ tự, hai người cùng làm, mất kết nối, hết phiên |
| 8 | **Rủi ro** | Tiền, dữ liệu cá nhân, văn bản pháp lý, hiệu năng, phát hành không cùng lúc |
| 9 | **Giả định** | Điều đang tự cho là đúng mà chưa ai xác nhận. Giả định nào sai thì phải viết lại nhiều: hỏi ngay |
| 10 | **Câu hỏi chặn** | Chỉ những câu tài liệu chưa trả lời và không tự quyết được (xem mục 7 của `van-phong.md`) |
| 11 | **Sơ đồ cần có** | Chọn theo `chon-so-do.md`, ghi một dòng lý do |

## Mức gọn

Dùng cho `/viet-automation`, `/dong-bo-drive`, `/log-bug`, `/ve-so-do-lan`, `/truy-vet`, `/review-tai-lieu`, `/bien-ban-hop`. Khối Phân tích 3 đến 5 gạch đầu dòng:

- Hiểu đúng yêu cầu chưa: làm việc gì, trên file nào, kết quả mong đợi là gì.
- Chỗ bị ảnh hưởng: file, sheet, tài liệu, người đang dùng file đó.
- Rủi ro khi làm: ghi đè dữ liệu của người khác, sửa nhầm file, thao tác không hoàn tác được.
- Câu hỏi chặn (nếu có).
