# Tự review SRS

## A. Đúng template

- [ ] Đủ mọi mục của template, đúng thứ tự, đúng tên mục, đúng cột của từng bảng.
- [ ] Đã xóa phần "Hướng dẫn sử dụng" và các chữ mẫu trong ngoặc vuông của template.
- [ ] Ma trận phạm vi bao phủ ở mục AC đã đi hết từng dòng.

## B. Đủ để Dev code

- [ ] Field: Loại kèm min–max, mặc định, bắt buộc, quy tắc nhập, chữ báo lỗi nguyên văn.
- [ ] Dự án có khóa "Cột data-testid" hoặc có repo automation: mọi bảng giao diện có cột `data-testid`, đủ ID của khối và ID trạng thái.
- [ ] Nút: điều kiện hiện, bật/tắt, kết quả khi bấm, popup xác nhận, câu thông báo sau xử lý.
- [ ] Danh sách: cột, sắp xếp mặc định, phân trang, bộ lọc, tìm kiếm (khớp một phần hay toàn bộ, hoa thường, dấu tiếng Việt, khoảng trắng đầu cuối).
- [ ] 6 trạng thái màn hình, hết hạn phiên đủ 4 bối cảnh.
- [ ] Use case viết đủ điều kiện và kết quả bằng lời, grep "BR[0-9]" trong mục use case bằng 0.
- [ ] Ảnh nằm đúng khu hoặc đúng trường hợp nó minh họa, mục Ảnh design/mockup chỉ có ảnh toàn trang.
- [ ] Màn có nhiều kích thước (máy tính, tablet, điện thoại): có link thiết kế của cả ba bản, bảng breakpoint, bảng hành vi thành phần. Business Rules viết một lần, không có mục màn riêng chép lại bảng thành phần cho tablet hay điện thoại. Có AC riêng cho phần hành vi khác nhau.
- [ ] Lời văn không có "theo BR…", "như nhóm…", "giống SCR…", "xem mục…". Mã tham chiếu chỉ nằm ở cột Tham chiếu.
- [ ] Luồng tích hợp: bản ghi đi đâu sau từng thao tác đổi trạng thái.
- [ ] Phân quyền theo vai trò, theo phạm vi dữ liệu, theo trạng thái bản ghi.
- [ ] Dữ liệu đã tạo trước khi có chức năng: xử lý thế nào.
- [ ] Thao tác đồng thời (hai người sửa cùng bản ghi, bấm hai lần) có quy tắc.

## C. Đủ để Tester viết case

- [ ] Mỗi BR có ít nhất một AC.
- [ ] AC có dữ liệu cụ thể, kết quả đo được. Không có chữ "hiển thị đúng", "hoạt động bình thường".
- [ ] Có AC biên, AC cấu hình, AC thao tác sai thứ tự, AC phân quyền.
- [ ] Mỗi quy tắc có cả phần hệ thống xử lý và phần người dùng nhìn thấy trên màn.
- [ ] BR nào thay đổi theo lựa chọn của người dùng (giá trị lọc, tab, trạng thái) đã tách mỗi lựa chọn một BR con, tên BR ghi rõ lựa chọn. Không còn câu gộp kiểu "lọc theo X thì giữ như trên" (mục 5b `van-phong.md`).
- [ ] Ô bảng có từ 2 ý trở lên đã viết gạch đầu dòng, ý con bắt đầu bằng `&nbsp;&nbsp;+ ` (mục 5 `van-phong.md`).

## D. Khớp nguồn

- [ ] Mọi quy tắc của SRS cũ đã đối chiếu ở note: giữ, bỏ, hay mâu thuẫn.
- [ ] Tên field, nút, cột, chữ hiển thị khớp thiết kế.
- [ ] CR đã duyệt đụng tới màn này đã được phản ánh.

## E. Văn phong

- [ ] Rà theo mục 8 của `van-phong.md`.
- [ ] Mã CR chỉ nằm ở Lịch sử thay đổi và Tài liệu tham chiếu.
