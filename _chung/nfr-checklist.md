# Checklist yêu cầu phi chức năng (NFR)

Dùng khi viết mục Yêu cầu phi chức năng của SRS, FSD, hoặc phần Ràng buộc của BRD. Đi từng nhóm, nhóm nào liên quan thì viết thành yêu cầu **có con số đo được**. Nhóm không liên quan thì bỏ, không viết "không áp dụng".

Viết theo dạng: **[đối tượng] [làm gì] trong [ngưỡng] khi [điều kiện tải]**. Ví dụ: "Danh sách cuộc đấu hiển thị trang đầu trong 2 giây khi có 500 người cùng mở".

## 1. Hiệu năng

- [ ] Thời gian phản hồi của màn chính, thao tác chính (mở danh sách, tìm kiếm, lưu, xuất file). Ghi theo mức 95% số lần.
- [ ] Số người dùng cùng lúc, số thao tác mỗi giây ở giờ cao điểm.
- [ ] Dung lượng dữ liệu: số bản ghi tối đa của danh sách, dung lượng tệp tải lên, số dòng import.
- [ ] Tác vụ chạy nền: import, xuất báo cáo lớn, gửi email hàng loạt. Bao lâu xong, người dùng biết kết quả bằng cách nào.
- [ ] Thời gian thực (realtime): độ trễ tối đa từ lúc phát sinh tới lúc người khác thấy.

## 2. Bảo mật và phân quyền

- [ ] Xác thực: cách đăng nhập, độ mạnh mật khẩu, khóa tài khoản khi nhập sai nhiều lần, xác thực hai lớp.
- [ ] Phiên đăng nhập: thời gian hết phiên, đăng nhập nhiều thiết bị.
- [ ] Phân quyền chặn ở phía máy chủ, không chỉ ẩn nút. Gọi thẳng đường dẫn hoặc API khi không có quyền thì bị từ chối.
- [ ] Phạm vi dữ liệu: người dùng chỉ thấy dữ liệu của tổ chức mình, của chính mình.
- [ ] Tệp tải lên: kiểm tra định dạng theo nội dung tệp, quét mã độc nếu cần, đường dẫn tải kiểm tra quyền mỗi lần mở.
- [ ] Mã hóa: dữ liệu khi truyền (HTTPS), dữ liệu nhạy cảm khi lưu.

## 3. Dữ liệu cá nhân

- [ ] Dữ liệu cá nhân nào được thu thập (họ tên, số định danh, ảnh giấy tờ, số điện thoại, tài khoản ngân hàng), để làm gì.
- [ ] Sự đồng ý của chủ thể dữ liệu và nơi ghi nhận (Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân và văn bản thay thế nếu có).
- [ ] Che bớt khi hiển thị (ví dụ chỉ hiện 4 số cuối), ai được xem bản đầy đủ.
- [ ] Thời gian lưu giữ, xóa hoặc ẩn danh khi người dùng rời hệ thống.
- [ ] Xuất dữ liệu cá nhân ra file: ai được xuất, có ghi nhật ký không.

## 4. Nhật ký và truy vết

- [ ] Thao tác nào phải ghi nhật ký: ai, lúc nào, làm gì, giá trị trước và sau.
- [ ] Ai xem được nhật ký, lưu bao lâu, có sửa xóa được không.
- [ ] Mốc thời gian theo giờ máy chủ, múi giờ nào.

## 5. Khả dụng và phục hồi

- [ ] Thời gian hệ thống chạy được trong tháng (ví dụ 99,5%), khung giờ bảo trì.
- [ ] Sao lưu: tần suất, giữ bao lâu, thời gian khôi phục tối đa, mất tối đa bao nhiêu dữ liệu.
- [ ] Dịch vụ ngoài lỗi (thanh toán, email, SMS, ký số): hệ thống xử lý thế nào, có thử lại không, người dùng thấy gì.

## 6. Tương thích

- [ ] Trình duyệt và phiên bản hỗ trợ.
- [ ] Thiết bị: máy tính, máy tính bảng, điện thoại. Độ rộng màn hình nhỏ nhất.
- [ ] App mobile: phiên bản hệ điều hành tối thiểu, xử lý khi người dùng chưa cập nhật app.

## 7. Dễ dùng và trợ năng

- [ ] Ngôn ngữ giao diện, định dạng ngày, số, tiền.
- [ ] Người dùng đặc thù (người lớn tuổi, ít dùng máy tính): cỡ chữ, độ tương phản, số bước tối đa cho thao tác chính.
- [ ] Thông báo lỗi nói được cách sửa.

## 8. Vận hành và mở rộng

- [ ] Giá trị nào để ở cấu hình để đổi không cần sửa code (tỷ lệ, thời hạn, giới hạn).
- [ ] Theo dõi và cảnh báo: chỉ số nào cần theo dõi, ai nhận cảnh báo.
- [ ] Dự kiến tăng trưởng dữ liệu, người dùng trong 1 đến 2 năm.
