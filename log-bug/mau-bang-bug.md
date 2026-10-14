# Mẫu file bug và văn phong ghi bug

File bug là một Google Sheet, mỗi dự án một file. Mẫu gốc: sheet "Bug Tập huấn" của dự án mẫu.

## 1. Bố cục sheet

```
        A     B        C         D          E                              F                   G         H       I
 1                                          REPORT * (gộp E1:F1)
 2                                          Mã trường hợp kiểm thử         B
 3                                          Số bugs chưa fix (Todo)        =đếm
 4                                          Số bugs đang fix (Inprogress)  =đếm
 5                                          Số bugs đã fix (Resolved)      =đếm
 6                                          Số bugs không đạt (Reopen)     =đếm
 7                                          Số bugs đang xem xét (Pending) =đếm
 8                                          Số bugs đạt (Passed)           =đếm
 9                                          Tổng số bugs                   =tổng
10
11  ID    Status   Asignee   Reporter   Summary                        Step to reproduce   Result    Image   Note
12  1     Todo     Đức       Q.Anh      ...
```

| Phần | Quy định |
|---|---|
| Ô F2 | Chữ cái của cột Status. Công thức đếm trên cột này, đổi bố cục thì chỉ sửa F2 |
| F3 tới F8 | `=COUNTIF(INDIRECT($F$2&"12:"&$F$2);REGEXEXTRACT(E3;"\(([^)]+)\)"))`: lấy trạng thái trong ngoặc ở cột E rồi đếm. Thêm dòng báo cáo mới chỉ cần ghi đúng tên trạng thái trong ngoặc |
| F9 | `=COUNTA(INDIRECT($F$2&"12:"&$F$2))`: đếm mọi dòng có Status, kể cả Closed và Testing |
| Dấu ngăn tham số | Sheet locale vi_VN dùng dấu `;`. Locale en dùng dấu `,`. Xem locale bằng `sheet-info` |
| Status | Danh sách chọn bắt buộc: Passed, Todo, Inprogress, Resolved, Reopen, Pending, Closed, Testing. Mỗi giá trị một màu nền và màu chữ |
| Asignee | Danh sách chọn, mặc định Đức, vẫn gõ được tên khác |
| Reporter | Danh sách chọn, mặc định Q.Anh, nền xanh nhạt |
| Font | Times New Roman. Bảng REPORT cỡ 13, vùng dữ liệu cỡ 12, các cột Summary, Step, Result, Note xuống dòng tự động |
| Bug mới | Status Todo. ID đánh liên tiếp theo dòng cuối đang có |

Màu theo trạng thái (nền / chữ): Passed `#c9daf8 / #1c4587`, Todo `#fcd5b4 / #7f3f00`, Inprogress `#b6e7f0 / #0c5460`, Resolved `#ffe5a0 / #7f6000`, Reopen `#b4e5e0 / #134f4a`, Pending `#ffcfc9 / #990000`, Closed `#e6cff2 / #4a148c`, Testing `#d4edbc / #274e13`.

API không đặt được màu cho từng nhãn dạng chip trong danh sách chọn, nên màu tô bằng định dạng có điều kiện. Muốn nhãn chip có màu thì người dùng chọn màu trong Dữ liệu > Xác thực dữ liệu.

## 2. Văn phong từng cột

Người đọc là dev. Dev không đọc FSD, nên viết đủ để dev tái hiện và biết sửa thành gì mà không phải mở tài liệu.

| Cột | Cách viết | Ví dụ |
|---|---|---|
| Summary | `[Cổng][Màn][Tab hoặc khu vực] <mô tả ngắn>`. Cổng luôn đứng đầu: `[Quản trị]`, `[Giáo viên]`. Dự án chỉ có một cổng thì bắt đầu từ màn | `[Quản trị][Chi tiết chiến dịch][Chủ đề] Mở popup Thêm chủ đề ko focus vào ô Tên chủ đề` |
| | Bug chỉnh giao diện nhiều chỗ trên cùng màn thì viết gọn rồi để ảnh nói | `[Chi tiết hồ sơ][Tab tổng quan]Tab Nội dung giám sát- Chỉnh sửa hiển thị` |
| Step to reproduce | Đánh số `1.` `2.`, mỗi bước một dòng, bắt đầu bằng động từ: Truy cập menu, Click, Chọn, Nhập, Xem. Có dữ liệu cụ thể thì ghi luôn | `1. Truy cập menu Quản lý tập huấn`<br>`2. Click Xuất báo cáo` |
| Result | Hai dòng `- Actual:` và `- Expect:`. Actual nói đúng cái đang thấy. Expect nói cái muốn thấy bằng lời thường | `- Actual: Từ chối thành công, ko có popup confirm`<br>`- Expect: Bổ sung popup confirm` |
| | Expect nhiều ý thì xuống dòng bằng dấu `+` | `- Expect:`<br>`+ Khi mở modal có nút Sửa kết quả`<br>`+ Mọi thông tin ở chế độ readonly` |
| | Bug giao diện nhiều chỗ đã ghi đủ trên ảnh thì viết một dòng | `- Actual + Expect: Chi tiết như hình` |
| Image | Liên kết "Xem ảnh" mở ảnh ghi chú trên Drive (công thức HYPERLINK). Không chèn ảnh vào ô vì ảnh quá nhỏ, dev không đọc được. Bug không cần hình thì để trống | `=HYPERLINK("https://drive.google.com/file/d/<id>/view";"Xem ảnh")` |
| Note | Chỉ ghi khi có thêm thông tin cho dev: chỗ khác cũng bị, điều kiện tái hiện đặc biệt, gốc lỗi kỹ thuật đã thấy. Không ghi mức độ (Cao, Trung bình) vào Note. Không có thì để trống | `Popup xem trước ở Cổng quản trị cũng bị` |

**Không viết:**
- Mã quy tắc, mã màn, tên tài liệu (BR-C19, SCR-A05, FSD mục 3.2). Dev không tra những mã này.
- "Theo design", "theo FSD" mà không nói design hay FSD muốn gì. Thay bằng mô tả cụ thể, có thể mở đầu bằng "Như design:" rồi nêu luôn.
- Văn phong trang trọng. Được viết tắt quen dùng của team: ko, VD, hover, tooltip, popup, click.

## 3. Ảnh ghi chú

Mẫu: ảnh chụp màn hình bên trái, bên phải là hộp xám chữ đen ghi lại Actual và Expect, mũi tên xám từ hộp chỉ vào khung đỏ khoanh chỗ lỗi.

| Quy định | Chi tiết |
|---|---|
| Khung đỏ | Khoanh đúng chỗ lỗi, khung đầu tiên là chỗ mũi tên chỉ vào. Thiếu phần tử thì khoanh chỗ đáng lẽ phải có nó |
| Mũi tên | Không đè lên chữ, nút hay số liệu khác. Cho mũi tên chạy dọc đường kẻ giữa hai dòng bảng, hoặc chỉ vào cạnh dưới của khung |
| Hộp xám | Chữ Times New Roman, nội dung giống cột Result |
| Che thông tin | Che vùng tên, email tài khoản đăng nhập. Không để lộ mật khẩu, token |
| Tên tệp | `<ID>-<mã nội bộ>-<mô tả ngắn không dấu>.png`, ví dụ `05-BUG-06-ten-dai-tran-bang.png`. ID ở đầu tên để ghép đúng dòng khi gắn liên kết |
| Nơi lưu | Thư mục ảnh bug trên Drive của dự án, chia sẻ cho service account và dev. Người dùng kéo ảnh lên, skill gắn liên kết |
| Kiểm tra | Mở lại từng ảnh sau khi vẽ: khung có đúng chỗ, mũi tên có đè nội dung không, hộp xám có bị cắt không |
