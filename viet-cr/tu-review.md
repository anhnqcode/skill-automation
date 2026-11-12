# Tự review CR

Đi hết danh sách trên bản CR vừa viết. Sửa thẳng vào CR, phần chưa sửa được ghi vào note.

## A. Dev có code được không

- [ ] Mỗi quy tắc trả lời được: ai, ở màn nào, khi nào, hệ thống làm gì, kết quả hiển thị ra sao.
- [ ] Dữ liệu mới: lưu ở đâu, giá trị mặc định, dữ liệu cũ đã có trước CR thì xử lý thế nào.
- [ ] Field mới: đủ Loại (kèm min–max ký tự), mặc định, bắt buộc, quy tắc nhập, chữ báo lỗi.
- [ ] Nút mới: điều kiện hiện, điều kiện bật/tắt, kết quả khi bấm, xác nhận trước khi xử lý.
- [ ] CR chưa có bảng Trạng thái màn hình, Hết hạn phiên đăng nhập (xem văn phong mục 6). Hành vi lỗi riêng của thay đổi thì đã viết thành quy tắc.
- [ ] Bản ghi đổi trạng thái: hiện ở đâu, mất khỏi đâu, module khác bị ảnh hưởng gì, điều hướng sau thao tác.
- [ ] Phân quyền: vai trò nào thấy, vai trò nào thao tác được.
- [ ] API dùng chung với màn khác thì ghi cách giữ nguyên hành vi màn khác.
- [ ] Web và Mobile, các portal liên quan đã xét hết, portal nào áp dụng thì có mục riêng.

## B. Tester test được không

- [ ] Mỗi quy tắc ở mục 3 có ít nhất một AC.
- [ ] AC có dữ liệu đầu vào cụ thể (số lượng, giá trị, trạng thái) và kết quả đo được. Không dùng chữ chung chung như "hiển thị đúng", "hoạt động bình thường".
- [ ] Có AC biên: min, max, 0, rỗng, đúng mốc thời gian, làm tròn.
- [ ] Có AC cho thứ tự thao tác khác thường: đổi trạng thái giữa chừng, hai người cùng thao tác, tải lại trang.
- [ ] Có AC cấu hình (đổi giá trị cấu hình, bật/tắt) và AC dữ liệu cũ.
- [ ] Không có dòng "Không đổi", hàng "Không áp dụng", AC "như trước khi có CR" hay quy tắc chỉ nói điều giữ nguyên.

## C. Logic còn hở

- [ ] Đã tự hỏi: dữ liệu rỗng, thiếu, quá nhiều; xóa hoặc gỡ bản ghi nguồn; đổi cấu hình khi đang có dữ liệu; người dùng chưa đăng nhập; bản app cũ.
- [ ] Mâu thuẫn giữa các mục (To-Be, bảng tác động, quy tắc, AC, note) sau các lần sửa.
- [ ] Mâu thuẫn với SRS và CR cũ đã đọc ở Bước 2. Mâu thuẫn nào CR này thay thế thì ghi rõ ở bảng Tài liệu bị ảnh hưởng.
- [ ] Rủi ro triển khai: dữ liệu cũ, phát hành không cùng lúc, hiệu năng khi dữ liệu lớn.
- [ ] Điểm yếu nghiệp vụ (đo hiệu quả, trải nghiệm người dùng, trường hợp lạm dụng) ghi vào note mục "Tự đánh giá điểm yếu".

## D. Thừa và văn phong

- [ ] Quy tắc, AC chỉ lặp lại hành vi cũ: xóa hoặc gộp thành một câu tham chiếu.
- [ ] Hệ quả tất yếu của quy tắc cũ: chuyển sang Rủi ro hoặc note.
- [ ] Rà văn phong mục 8 (grep "không", từ hoa mỹ, backtick trong phần nghiệp vụ).
- [ ] Ô bảng nhiều ý (Quy tắc nhập, Mô tả nút, Ghi chú tài liệu bị ảnh hưởng, Ảnh hưởng kỹ thuật, Phạm vi, bảng sự kiện): mỗi ý một gạch đầu dòng nối bằng <br>, không viết liền thành đoạn.
- [ ] Tên màn, tên nút, tên trường viết giống hệt giao diện và SRS.
