# Tự review FSD

## A. Đúng khung

- [ ] Đủ các mục của template, đúng thứ tự. Mỗi màn trong Screen flow có một mục SCR.
- [ ] Mỗi màn có Tổng quan: User story, Pre-condition, Post-condition (màn có đổi dữ liệu). Có BRD thì story ghi mã US của BRD.
- [ ] Mục "theo điều kiện" không có điều kiện thì đã xóa hẳn. Đã xóa các dòng hướng dẫn bắt đầu bằng `>`.
- [ ] Bảng Nút chức năng hai cột, không mô tả vị trí nút.
- [ ] Không còn mã MSG, không còn "theo BR-xx", "theo mục x.y".
- [ ] BR mỗi BR một ý, BR dài đã tách a, b, c.

## B. Đủ để Dev code

- [ ] Field: Loại kèm min–max, bắt buộc, mặc định, câu báo lỗi nguyên văn.
- [ ] Danh sách: thứ tự sắp xếp, số dòng mỗi trang, câu khi không có dữ liệu.
- [ ] Nút: kết quả khi bấm, popup xác nhận, câu thông báo sau xử lý, điều kiện khóa nếu có.
- [ ] Vòng đời trạng thái: mọi đối tượng có trạng thái đã có bảng, ai đổi, đổi rồi ai làm được gì.
- [ ] Ảnh hưởng chéo giữa các cổng: mọi thao tác ở cổng này làm đổi dữ liệu cổng kia đã có dòng, kể cả người đang mở màn đúng lúc đó.
- [ ] Phạm vi dữ liệu: chặn ở phía máy chủ, gọi thẳng đường dẫn thì bị từ chối.
- [ ] Xuất tệp: tên tệp, các cột, lọc ra 0 bản ghi thì sao.
- [ ] Nhập tệp: tệp mẫu, dòng lỗi xử lý ra sao, dòng trùng, giới hạn số dòng.

## C. Đủ để Tester viết case

- [ ] Mỗi BR có ít nhất một AC.
- [ ] AC có điều kiện cụ thể và kết quả đo được, có câu thông báo nguyên văn.
- [ ] Có AC cho trạng thái màn, hết hạn phiên, phân quyền, định dạng chung.
- [ ] Mỗi quy tắc có cả phần xử lý và phần người dùng nhìn thấy trên màn.

## D. Khớp nguồn

- [ ] Có BRD: bảng đối chiếu User story → Màn → AC trong note đã đủ, phạm vi FSD không vượt BRD.
- [ ] Tên field, nút, cột khớp design. Chỗ design lệch nhau đã ghi ở Screen flow hoặc câu hỏi mở.
- [ ] Câu hỏi đã được trả lời đã chuyển thành quy tắc, xóa khỏi danh sách đang chờ.

## E. Văn phong

- [ ] Rà theo mục 8 của `van-phong.md`.
- [ ] Tên đơn vị, vai trò đúng như dự án đã chốt (ví dụ: gọi Quản trị, không dùng chữ "Cục").
