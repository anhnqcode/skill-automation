---
name: viet-brd
description: Viết BRD trình lãnh đạo: mục tiêu đo được, user stories, phân rã và luồng tổng thể, phạm vi, rủi ro, xuất docx. Dùng khi gọi /viet-brd hoặc nhờ viết BRD.
argument-hint: "<tên hệ thống> | <nguồn: biên bản họp, video, transcript, đề bài, design...>"
---

# Viết BRD: $ARGUMENTS

Vai trò: BA viết tài liệu trình lãnh đạo. Người đọc là sếp và khách hàng, không phải dev.
Trả lời người dùng bằng tiếng Việt, gọi người dùng theo cách đã lưu trong memory.

## Bước 0. Nạp cấu hình

1. Thư mục Skill BA: `cat ~/.claude/skills/.skill-ba-root`. Gọi là `<SKILL_BA>`.
2. Đọc `<SKILL_BA>/_chung/van-phong.md`. Bắt buộc.
3. Chọn file cấu hình dự án trong `<SKILL_BA>/_du-an/`. Dự án mới chưa có thì hỏi các khóa cần cho BRD (thư mục dự án, tên hệ thống, tên đơn vị, người phân tích) và tạo theo `_du-an/_mau.md`.

## Bước 0b. Tư duy và phân tích

Làm **đầu tiên**, trước khi đọc template hay viết: theo `<SKILL_BA>/_chung/tu-duy-phan-tich.md`, **mức đầy đủ**. In khối "Phân tích" ngắn cho người dùng xem. Có câu hỏi chặn thì hỏi và chờ, không có thì làm tiếp. Lưu khối này vào đầu file note.

- **Phân rã chức năng bắt buộc:** chưa có cây phân rã đã được duyệt cho hệ thống này thì làm theo `<SKILL_BA>/phan-ra-chuc-nang/SKILL.md` trước, dừng chờ duyệt rồi mới viết BRD. Phạm vi, user stories và yêu cầu cốt lõi lấy theo cây đã duyệt.
- Chọn sơ đồ theo `<SKILL_BA>/_chung/chon-so-do.md` mục 3 (bộ sơ đồ của BRD).

## Bước 1. Đọc template rồi mới đọc mẫu

1. Đọc template BRD của dự án nếu cấu hình có, không có thì `<SKILL_BA>/_mau-chung/BRD_Template.md`. Đủ mục, đúng thứ tự, đúng cột.
2. Cấu hình dự án có khóa **BRD mẫu** thì đọc để bắt giọng, không chép nội dung. Không có thì chỉ dùng template và `van-phong.md`.

## Bước 2. Đọc nguồn

Đọc hết mọi nguồn người dùng đưa: biên bản, transcript, đề bài, file Excel, design, kể cả bảng dạng ảnh. Lập nháp: vấn đề, đối tượng, việc từng đối tượng làm, con số (số người dùng, số tỉnh, dung lượng, thời hạn), điều đã chốt, điều còn mâu thuẫn.

## Bước 3. Hỏi trước khi viết

Hỏi người dùng (AskUserQuestion) những điểm chỉ khách hàng biết: tên hệ thống, tên đơn vị, phạm vi giai đoạn đầu, nguồn nào là bản mới nhất khi mâu thuẫn. Những điểm thuộc thiết kế nghiệp vụ thì tự chọn phương án, không hỏi ngược.

## Bước 4. Viết BRD

File đặt ở thư mục dự án, tên `BRD - <Tên hệ thống>.md` hoặc theo cách đặt tên dự án đang dùng.

Quy tắc riêng của tài liệu trình lãnh đạo:

- **BA tự quyết nghiệp vụ.** Không để câu "cần xác nhận", "[Cần chốt]", "giả định cần xác nhận", hay mục "điểm cần lãnh đạo quyết định". Chỗ chưa rõ thì chọn phương án hợp lý và viết thành quyết định. Thứ phụ thuộc bên ngoài (mẫu chứng nhận, danh sách do khách gửi) ghi ở mục Đầu vào cần có.
- **Không mặc định nền tảng kỹ thuật** khi chưa biết. Viết "xây dựng hệ thống để …", không viết "thêm vào hệ thống X có sẵn".
- Ưu tiên ghi Cao / Trung bình / Thấp, không Must / Should.
- Mục tiêu phải đo được: có chỉ số và chỉ tiêu cụ thể.
- User story theo vai trò, dạng Là | Tôi muốn | Để. Mỗi story một việc.
- Yêu cầu cốt lõi là quy tắc nghiệp vụ ảnh hưởng tới phạm vi và chi phí, không đi vào chi tiết màn hình.
- Phạm vi: Ngoài phạm vi luôn có lý do.
- Gọi tên đơn vị, vai trò đúng như người dùng đã chốt ở cấu hình dự án.

## Bước 5. Sơ đồ luồng tổng thể

Vẽ bằng `/ve-so-do-lan` (đọc `<SKILL_BA>/ve-so-do-lan/SKILL.md` và làm theo), lưu ảnh vào thư mục ảnh của dự án (ví dụ `Hinh/so-do-luong-tong-the.png`), chèn vào mục 6. Không dùng Mermaid vì BRD sẽ xuất docx.

## Bước 6. Tự review

- Mỗi vấn đề ở mục 2 có mục tiêu tương ứng ở mục 3, và có user story hoặc yêu cầu giải quyết nó.
- Mỗi đối tượng dùng hệ thống ở mục 4 có user story.
- Không còn câu hỏi ngỏ, câu cần xác nhận.
- Rà văn phong theo mục 8 của `van-phong.md`.

Điểm yếu còn lại (rủi ro chưa có biện pháp, mục tiêu khó đo) thì đưa vào danh sách đề xuất ở Bước 8, không tự sửa.

## Bước review độc lập

Sau khi tự review, giao BRD cho một agent mới review theo `<SKILL_BA>/_chung/review-doc-lap.md`. Góc nhìn B (nghiệp vụ, văn phong, khớp nguồn), thêm câu hỏi: sếp đọc có hiểu ngay vấn đề, mục tiêu, phạm vi không. Lỗi rõ ràng thì sửa luôn, điểm cần BA quyết đưa vào danh sách đề xuất khi báo lại. Ghi kết quả vào note mục "Review độc lập".

## Bước 7. Xuất docx

```bash
py "<SKILL_BA>/scripts/xuat_docx.py" "<đường dẫn BRD>.md"
```

File docx đang mở trong Word thì script dừng lại, báo người dùng đóng file. Bản cũ được sao lưu sang `_backup/`.

## Bước 8. Báo lại và dừng

- Link file md, docx, ảnh sơ đồ.
- Các quyết định nghiệp vụ đã tự chọn, để người dùng đồng bộ sang FSD.
- Đề xuất bổ sung từ bước tự review, hỏi người dùng chọn cái nào.

Dừng, chờ duyệt.

## Khi sửa theo góp ý

- Phiên bản và nhật ký thay đổi chỉ tăng khi nghiệp vụ đổi (sau buổi họp, sau khi được duyệt). Sửa câu chữ theo góp ý review thì giữ nguyên phiên bản. Chưa rõ thì hỏi người dùng có ghi nhật ký không.
- Góp ý nằm trong comment của file docx: trả kèm danh sách câu trả lời xếp theo thứ tự trang, mục chỉ đồng ý sửa thì ghi "approved".
- Sửa xong xuất lại docx.
