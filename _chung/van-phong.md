# Văn phong tài liệu BA

Áp dụng cho CR, SRS, testcase, note và cả câu trả lời trong hội thoại. Đọc file này trước khi viết.

**Đây là nguồn chính của mọi quy tắc văn phong.** Memory chỉ trỏ sang đây. Người dùng góp ý văn phong mới thì sửa file này, không ghi quy tắc chi tiết vào memory.

## 1. Giọng văn

- Viết giọng thường ngày, câu ngắn, dễ hiểu. Câu dài thì tách thành hai, ba câu.
- Không dùng từ hoa mỹ, ẩn dụ. Một số chỗ hay sai:

| Tránh | Viết |
|:---|:---|
| cửa ngõ, chặng, điểm chốt, mốc một chiều | nơi tổng hợp, giai đoạn, chuyển sang X rồi thì không lùi lại được |
| thương vụ đấu giá | một lần đấu giá tài sản |
| không hồi tố | giữ nguyên các bản ghi đã tạo trước đó |
| chỉ mang tính gợi ý | chỉ là giá trị điền sẵn |
| công tắc | gọi thẳng thứ nó điều khiển: "quy tắc được bật" |
| "điền sẵn" cho nút bật/tắt | mặc định bật / mặc định tắt |
| cửa sổ xét, cửa sổ kích hoạt | chỉ tính khi xảy ra trong …, khoảng được tính |
| ánh xạ, cờ, máy trạng thái, offset, index, parse, render | chỉnh cho khớp, giá trị, quy tắc chuyển trạng thái, vị trí thứ mấy, đọc, hiển thị |
| thương thảo | làm việc, trao đổi |
| gom tất cả văn bản vào một chỗ | xếp tất cả văn bản vào một bộ hồ sơ |
| khối lượng công việc còn tồn | còn bao nhiêu văn bản chưa xử lý |
| bố cục đã trôi, bố cục không còn xê dịch | nội dung đã dịch sang trang khác, nội dung không thay đổi nữa |
| hai mốc Chưa thực hiện và Đang thực hiện | hai trạng thái Chưa thực hiện và Đang thực hiện |
| phản ánh tiến độ xử lý | cho biết đang làm đến đâu |
| căn cứ truy vết | căn cứ để hai bên đối chiếu |
| không tồn tại độc lập ngoài X | chỉ thuộc về X, không dùng ở chỗ nào khác |
| làm sai lệch quan hệ giữa các bản ghi | làm sai liên kết giữa các bản ghi |
| dòng neo, neo ảnh | dòng mà ảnh nằm ở đó |
| hai lưới đan nhau, ổ bug, xương sống của hệ thống | nói thẳng việc đang làm là gì |

- Không dùng từ dịch máy nghe cứng. Tự hỏi "người Việt trong ngành có nói thế này không":

| Tránh | Viết |
|:---|:---|
| bảng ánh xạ, ánh xạ A sang B | bảng đối chiếu, bảng tra cứu, A tương ứng với B |
| trần điểm, chặn trần | giới hạn tối đa, mức tối đa |
| có tiền tố X | bắt đầu bằng chữ X |
| lần sửa sau cùng thắng, giá trị nào thắng | hệ thống lấy giá trị của lần sửa sau cùng |
| Must, Should, Could | Cao, Trung bình, Thấp |

- Không dùng dấu gạch dài (—) trong câu. Thay bằng dấu phẩy, dấu hai chấm, ngoặc đơn, hoặc tách câu. Tiêu đề tài liệu viết theo template thì giữ nguyên.
- Thuật ngữ nghiệp vụ chuẩn, tên màn hình, tên nút, tên trường thì giữ nguyên. Trích đúng chữ trong tài liệu nguồn thì giữ nguyên.
- Viết mộc nhưng vẫn giữ lý do nghiệp vụ ("vì …", "để …") trong quy tắc.
- **Thuật ngữ dự án:** đọc File thuật ngữ ở cấu hình dự án trước khi viết. Mỗi khái niệm chỉ dùng một tên, gặp tên ở cột "Không dùng" thì đổi. Thuật ngữ mới phát sinh thì đề xuất thêm vào file thuật ngữ và hỏi người dùng.
- Khi trao đổi với người dùng, gọi tài liệu theo tên (tên màn, tên module), không gọi bằng mã kiểu M4, SCR-03 vì tên file không chứa mã.

## 2. Không dùng cú pháp code trong phần nghiệp vụ

- Mô tả, quy tắc, AC, use case viết bằng câu: "khi tài khoản chưa xác minh KYC", không viết `kyc !== 'verified'`.
- Tên API, bảng dữ liệu, tham số chỉ xuất hiện ở bảng "Ảnh hưởng kỹ thuật (để Dev tham khảo)".

## 3. Không viết câu phủ định, không viết điều không tồn tại

- Cái gì không xảy ra thì không nhắc. Viết lại thành câu khẳng định: "không công bố cuộc nào" → "các cuộc đấu giữ nguyên trạng thái".
- Chỉ giữ chữ "không" khi đó là chữ hiển thị thật trên giao diện, giá trị cột (Bắt buộc: Không) hoặc tên trạng thái chuẩn ("Không có dữ liệu").
- Không viết câu trấn an khi không ai hỏi ("đây là điều bình thường, không phải lỗi").
- Không viết những thứ không thay đổi: dòng "Không đổi" ở bảng tác động, hàng "Không áp dụng" ở phạm vi, quy tắc chỉ để nói bản ghi khác "giữ nguyên", nhóm AC "màn giữ nguyên như trước khi có CR". Tài liệu chỉ nói phần có thay đổi.
- Không viết "nếu A thì …, nếu không A thì …" để phòng hờ. Chưa biết A thì hỏi BA rồi viết một hướng.
- BA trả lời "Không / Không có" cho một ý, hoặc bỏ một ý: xóa hẳn mọi dấu vết ý đó khỏi tài liệu, chỉ ghi ở bảng "Các điểm đã chốt" trong `.note.md`. Không đổi ý đó thành dòng "Không đổi".
- Nội dung đã lên production thì viết là hiện trạng: "Hệ thống đang chạy … như sau". Không rải "theo CR-XXX", mã màn (SCR04), mã quy tắc (BR17) hay "của SRS X" vào phần mô tả, quy tắc, AC: gọi thẳng tên màn và viết thẳng hành vi. Tham chiếu tài liệu chỉ đặt ở dòng CR phụ thuộc và bảng "Tài liệu bị ảnh hưởng".

## 3b. SRS, FSD viết mới không so sánh với tài liệu cũ

- Tài liệu cũ (SRS cũ, CR, trang đang chạy) chỉ dùng để hiểu chức năng, menu dùng để làm gì. Tài liệu mới viết lại như mô tả hệ thống từ đầu.
- Từ mục 2 trở đi: không bảng "cũ / mới", không câu "so với bố cục cũ", "bố cục mới", "thay cho", "như hiện có", "viết lại theo thiết kế mới", không tham chiếu tên tài liệu cũ hay mã CR.
- Tham chiếu tài liệu cũ, CR chỉ đặt ở mục 1 (Lịch sử thay đổi, Tài liệu tham chiếu). Mô tả ở Lịch sử thay đổi dòng đầu chỉ ghi "Khởi tạo tài liệu".
- Tên tài liệu, tiêu đề, chú thích ảnh không kèm chữ "(bố cục mới)", "(mới)".

## 4. Sửa chỗ sai

- BA chỉ ra chỗ sai: xóa hẳn chỗ đó, không giữ lại rồi thêm câu giải thích.
- Đổi một quyết định: grep lại toàn bộ tài liệu (mô tả, bảng tác động, quy tắc, AC, note) để sửa hết chỗ còn viết theo quyết định cũ.
- AC dẫn tới quy tắc cũ thì ghi thẳng chữ báo lỗi hoặc hành vi thật, không ghi "theo CR-XXX".

## 4b. Chỉ viết phần mới (CR)

- Với mỗi quy tắc định viết, tự hỏi: hệ thống đang chạy như vậy chưa? Rồi thì bỏ, hoặc gộp thành một câu "theo quy tắc hiện có của <màn>", nói rõ điểm khác.
- Hệ quả tất yếu của quy tắc cũ (ví dụ đã qua mốc mở đăng ký nên không chuyển về nháp được) thì đưa vào Rủi ro hoặc note, không viết thành quy tắc.
- Bảng luồng dữ liệu, bảng hiển thị sau thao tác chỉ giữ dòng có thay đổi.
- Trước khi tự thêm logic hiển thị mới: chạy bản thiết kế và grep SRS xem màn đó đã xử lý trường hợp này chưa.

## 5. Bảng và định dạng

- Bảng có alignment marker (`:---`, `:---:`), tiêu đề cột viết hoa chữ đầu.
- Bảng field: độ dài ghi ở cột **Loại**, đủ cả min và max: `Textbox (1–100 ký tự)`. Field bắt buộc min = 1, không bắt buộc min = 0. Cột Quy tắc nhập không lặp lại con số độ dài.
- Luồng dữ liệu viết dạng bảng `Bước | Mô tả hành động | Kết quả hệ thống thực hiện`. Logic rẽ nhánh phức tạp thì thêm Mermaid flowchart.
- Ảnh nhúng bằng `![mô tả ngắn](_attachments/<tên file>.png)`.
- Đã có thiết kế thì SRS không mô tả hình thức: bố cục (mấy hàng, góc nào, chia đều), màu, cỡ chữ, khoảng cách, kích thước khung. Dev xem ở thiết kế. SRS chỉ giữ nội dung và định dạng dữ liệu (chữ hiển thị, định dạng ngày giờ, số tiền, đếm ngược, cắt chữ), hành vi, điều kiện hiện ẩn, trạng thái và quy tắc. Quy tắc quy đổi sang hiển thị thì BR định nghĩa mức, bảng giao diện ghi "màu theo thiết kế". Ràng buộc người dùng đưa riêng (ví dụ mã màu thương hiệu) ghi một dòng ở mục Ràng buộc.

### 5b. Mỗi nội dung chỉ viết ở một chỗ

- Bảng trường thông tin, bảng nút, bảng cột đã mô tả giao diện. Business Rule chỉ viết phần bảng không nói được: điều kiện nghiệp vụ, ràng buộc giữa nhiều trường, cách chọn và sắp xếp dữ liệu, quy đổi dữ liệu sang hiển thị, hệ quả về dữ liệu, thông báo lỗi kèm quy tắc. Trước khi viết một rule, tự hỏi bảng đã nói chưa. Nói rồi thì bỏ rule, hoặc chỉ giữ phần bảng chưa nói.

| Viết ở bảng | Viết thành rule |
|:---|:---|
| Danh sách giá trị, giá trị mặc định, số thẻ, chữ hiển thị, định dạng | Khi nào giá trị bị chặn, vì sao mặc định như vậy |
| Kiểu hiển thị (badge, icon, màu theo thiết kế) | Quy tắc quy đổi dữ liệu sang hiển thị, ví dụ ngưỡng nào ra màu nào |
| Thẻ số liệu, khu dữ liệu hiển thị gì | Tính trên phạm vi nào, chọn bản ghi nào, sắp xếp theo gì, khi nào thay đổi |
| Nút bấm đi đâu, mở gì | Điều kiện được bấm, hệ quả lên dữ liệu và bản ghi khác |

- Ở bảng giao diện, chỗ nào chạm logic của rule thì chỉ nói ngắn kết quả nhìn thấy, không kèm mã BR, không câu dẫn kiểu "(cách chọn: BR04)", không chép lại nội dung rule: "Đếm ngược tới hạn đăng ký, màu chữ đổi theo thời gian còn lại". Tên BR ghi rõ khu hoặc thành phần nó áp dụng để người đọc tự tìm. Mã BR chỉ xuất hiện ở bảng BR, use case và cột Liên kết của AC.
- Business Rule viết dạng quy tắc bắt buộc: "Phải", "Chỉ được phép", "Không được" (ngoại lệ của mục 3, chữ "không" được dùng trong BR khi đó là ràng buộc). Không kể lại luồng thao tác.
- Business Rule chỉ giữ năm loại, ghi ở cột Loại: Chính sách, Dữ liệu (định nghĩa, nguồn, tiêu chí chọn), Ràng buộc, Tính toán, Logic. Quy tắc giao diện đưa lên bảng giao diện, quy tắc kỹ thuật (chịu lỗi, chống gửi trùng, hiệu năng) đưa sang Yêu cầu phi chức năng.
- Business Rule không gọi tên thành phần giao diện (khu, tab, nút, màu, bố cục, hiệu ứng). Gọi theo loại dữ liệu để đổi giao diện thì BR không phải sửa. Quy đổi sang hiển thị thì BR định nghĩa mức (ví dụ mức cảnh báo Khẩn, Sắp hết hạn), bảng giao diện ghi màu của từng mức.
- Câu thông báo viết ngay tại chỗ phát sinh, chỉ một lần.
- Hai lỗi hay gặp: chép nguyên mô tả của bảng xuống thành rule; viết rule chỉ để khẳng định một thứ không có.
- Sửa một quyết định thì rà đủ ba chỗ: bảng giao diện, Business Rules, AC.
- Bỏ hoặc đánh lại số BR thì grep mã BR trên toàn file. Ngoài bảng BR, use case và cột Liên kết của AC, chỗ nào còn mã BR (ghi chú NFR, sơ đồ, luồng tích hợp, bảng giao diện) thì thay bằng câu nói thẳng nội dung.

## 6. Thành phần giao diện mới

- SRS, FSD cho màn mới: đủ 6 trạng thái: Mặc định, Đang tải, Không có dữ liệu, Không có kết quả lọc, Lỗi hệ thống, Hết hạn phiên đăng nhập. Hết hạn phiên tách 4 bối cảnh: đang xem, đang nhập dở trong popup, đang bấm nút xử lý, bị thu hồi quyền khi phiên còn hiệu lực.
- CR: bỏ bảng Trạng thái màn hình và bảng Hết hạn phiên đăng nhập, kèm AC lỗi hệ thống, hết hạn phiên, thu hồi quyền. Thành phần mới theo xử lý chung hiện có của màn. Trạng thái nào có hành vi riêng của thay đổi (ví dụ một thông báo lỗi mới) thì viết thành quy tắc trong mục 3.x.
- Chỉ áp dụng cho thành phần mới. Thành phần giữ nguyên thì không viết lại.
- Mọi thao tác làm bản ghi đổi trạng thái: ghi rõ bản ghi hiện ở menu/tab nào, mất khỏi đâu, ảnh hưởng dây chuyền sang module nào, giao diện điều hướng đi đâu sau thao tác.

## 7. Hỏi và chờ duyệt

- **Trước khi viết:** điểm chưa rõ, hai nguồn mâu thuẫn, chưa biết chức năng làm gì thì hỏi. Biết hành vi nhưng thiếu con số thì vẫn viết, ghi chờ chốt vào note.
- **Trong lúc viết:** phát sinh câu hỏi chặn thì hỏi ngay, không gom về cuối. Chờ trả lời thì làm tiếp phần không phụ thuộc.
- **Điểm nhỏ:** tự chốt theo hướng hợp lý, ghi vào note, cuối lượt báo lại đã chốt gì.
- **Trước khi hỏi:** đọc hết tài liệu nguồn, kể cả bảng dạng ảnh và khối code. Câu nào tài liệu đã trả lời hoặc suy ra được thì không hỏi.
- **Đề xuất sau khi review:** lỗi rõ ràng thì sửa luôn. Đề xuất thêm logic nghiệp vụ mới, đổi phạm vi thì hỏi người dùng trước, đồng ý mới sửa.
- **Làm từng chặng:** xong một chặng (thiết kế, CR, SRS, testcase, automation) thì báo và dừng. Lời đồng ý cho một việc cụ thể chỉ áp cho việc đó, không phải lời duyệt cả chặng.

## 8. Trước khi báo xong

- Grep chữ "không" và rà từng chỗ theo mục 3.
- Grep các từ ở bảng mục 1 và dấu "—" trong câu.
- Grep dấu backtick trong phần nghiệp vụ theo mục 2.
