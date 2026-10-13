# Tư duy test: tìm case ngoài SRS

SRS thường chỉ nói luồng chính. Với mỗi màn, mỗi quy tắc, đi qua các câu hỏi dưới đây. Câu nào ra case mà SRS chưa có thì viết case và ghi vào note mục "SRS thiếu".

## 1. Dữ liệu đầu vào

- **Phân vùng tương đương:** mỗi field chia nhóm hợp lệ, không hợp lệ. Một case cho mỗi nhóm.
- **Giá trị biên:** min, min − 1, max, max + 1 lấy từ cột Loại. Số: 0, âm, số thập phân, số rất lớn, dấu phân cách hàng nghìn. Ngày: hôm nay, hôm qua, ngày mai, 29/02, cuối tháng, đúng mốc giờ.
- **Chuỗi:** khoảng trắng đầu cuối, chỉ khoảng trắng, ký tự đặc biệt, emoji, tiếng Việt có dấu và không dấu, dán từ Word/Excel, HTML/script.
- **Tệp:** đúng định dạng, sai định dạng đổi đuôi, dung lượng biên, tệp rỗng, tên tệp có dấu, tải nhiều tệp.

## 2. Tổ hợp điều kiện

- **Bảng quyết định:** quy tắc có từ hai điều kiện trở lên thì lập bảng đủ tổ hợp, mỗi cột một case.
- **Phụ thuộc giữa field:** đổi field cha sau khi đã chọn field con. Bắt buộc có điều kiện.
- **Ma trận đầu vào × đầu ra:** hàng là kịch bản, cột là các nơi bị ảnh hưởng, ô là mã TC.

## 3. Trạng thái và thứ tự thao tác

- **Chuyển trạng thái:** vẽ các trạng thái của bản ghi. Mỗi chuyển hợp lệ một case, mỗi chuyển không hợp lệ (nhảy cóc, lùi lại) một case.
- **Thao tác sai thứ tự:** bản ghi đổi trạng thái khi người dùng đang mở màn cũ rồi mới bấm nút. Bấm nút khi điều kiện vừa hết. Quay lại bằng nút Back của trình duyệt. Mở hai tab.
- **Mốc thời gian:** trước, đúng, sau mốc một giây. Thời gian theo giờ máy chủ. Qua nửa đêm, qua cuối tuần, ngày lễ nếu tính ngày làm việc.

## 4. Nhiều người, nhiều lần

- **Đồng thời:** hai người sửa cùng bản ghi, hai người duyệt cùng lúc, bấm nút hai lần liên tiếp, mạng chậm rồi bấm lại.
- **Lặp lại:** làm lại thao tác đã làm (duyệt lần hai, xóa lần hai, tải lại trang sau khi gửi).

## 5. Phân quyền

- Vai trò được phép, vai trò không được phép, người chưa đăng nhập.
- Gọi thẳng URL hoặc API khi giao diện đã ẩn nút.
- Xem dữ liệu của tổ chức khác, người khác (đổi ID trên URL).
- Bị đổi quyền khi đang dùng.

## 6. Người dùng nhìn thấy gì

- Con số, trạng thái trên màn có cập nhật sau thao tác không, hay phải tải lại.
- Hệ thống đổi dữ liệu ngầm thì có chỗ nào báo cho người dùng biết.
- Thông báo thành công, thất bại có đúng chữ, đúng chỗ, đúng lúc.
- Dữ liệu dài thì cắt, xuống dòng, tooltip ra sao. Số tiền, ngày giờ đúng định dạng.
- Web và Mobile hiển thị cùng một dữ liệu có khớp nhau.

## 7. Tích hợp và dây chuyền

- Sau thao tác, bản ghi xuất hiện ở menu, tab nào, biến mất khỏi đâu.
- Module khác dùng dữ liệu này: danh sách, báo cáo, dashboard, thông báo, email, nhật ký.
- Dữ liệu đã tạo trước khi có chức năng mới.
- Dịch vụ ngoài lỗi hoặc chậm (thanh toán, email, ký số, lưu tệp).

## 8. Trạng thái màn hình và lỗi

- 6 trạng thái: Mặc định, Đang tải, Không có dữ liệu, Không có kết quả lọc, Lỗi hệ thống, Hết hạn phiên (đang xem, đang nhập dở trong popup, đang bấm nút xử lý, bị thu hồi quyền).
- Mất mạng giữa chừng, máy chủ trả lỗi, phản hồi rất chậm.

## 9. Đoán lỗi

Dựa vào kinh nghiệm, tự hỏi: chỗ nào dev dễ làm sai nhất? Thường là làm tròn số, múi giờ, so sánh hoa thường, dữ liệu rỗng, phân trang sau khi xóa, bộ lọc giữ lại sau khi quay về, cache sau khi đổi cấu hình.
