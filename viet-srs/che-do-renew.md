# Chế độ renew UI

Dùng khi một màn hoặc một nhóm màn **đã có SRS và đang chạy**, nay làm lại giao diện theo thiết kế mới. Gọi bằng `/viet-srs <tên màn> | renew`, hoặc khi người dùng nói làm lại giao diện, renew, thiết kế mới cho màn đã có.

Các bước của `SKILL.md` vẫn làm đủ. Chế độ này thêm và thay các điểm dưới đây.

## 1. File

- Viết SRS mới thành file `<tên SRS cũ> (new).md` đặt cạnh SRS cũ, cùng thư mục. Kèm `(new).note.md`, sau này có `(new).test.md`, `(new).auto.md`.
- Nhóm nhiều màn cùng renew (cả một cổng, một phân hệ) thì đặt chung một thư mục con `Renew/` trong thư mục của cổng, giữ tên file theo màn.
- SRS cũ giữ nguyên, không sửa, cho tới khi bản mới lên Production (mục 6).

## 2. So thiết kế mới với hệ thống đang chạy

Bước 3 của `SKILL.md` làm kỹ hơn. Mở trang đang chạy (Production chỉ xem) và đặt cạnh thiết kế mới, ghi vào đầu note một đoạn "So với trang thật ngày <ngày>":

- Khu nào thêm, bỏ, đổi vị trí.
- Số lượng hiển thị đổi (số thẻ, số dòng, số tab).
- Kiểu hiển thị đổi (băng trượt thành lưới, popup thành nhập ngay trong danh sách).
- Chữ hiển thị, màu chính, field, nút, cột thêm hoặc bỏ.

## 3. Bảng kế thừa quy tắc

Thay cho bảng đối chiếu ở Bước 2.4. Nguồn gồm SRS cũ và **mọi CR đã lên Production** chạm màn này (CR sau đè CR trước).

| Nguồn | Quy tắc cũ | Xử lý trong SRS mới |
|:---|:---|:---|

Cột Xử lý mở đầu bằng một trong năm chữ:

- **Giữ:** quy tắc nghiệp vụ không đổi. Viết lại đầy đủ trong SRS mới, không dẫn sang file cũ.
- **Đổi:** quy tắc còn nhưng con số, chữ, cách hiển thị đổi theo thiết kế. Ghi đổi thế nào.
- **Lỗi thời:** thiết kế mới thay bằng thứ khác. Ghi thay bằng gì.
- **Bỏ:** thiết kế mới không còn. Ghi ai chốt bỏ.
- **Mâu thuẫn:** SRS cũ, CR và hệ thống đang chạy nói khác nhau. Ghi bên nào đúng và vì sao, không rõ thì hỏi.

CR còn Draft chạm màn này: ghi riêng một dòng, không tính vào quy tắc.

Quy tắc nghiệp vụ (chia tỷ lệ, quyền, dữ liệu theo domain, tính toán) thường **Giữ** dù giao diện đổi hết. Soát kỹ nhóm này, đây là chỗ hay bị rơi khi viết lại.

## 4. Viết SRS mới

- Lịch sử thay đổi dòng đầu: "Khởi tạo bản renew giao diện", cột Tham chiếu ghi SRS cũ.
- SRS mới là tài liệu đầy đủ, đọc riêng vẫn đủ để dev code và tester viết testcase. Không viết "như bản cũ", "giữ nguyên SRS cũ".
- Chữ hiển thị, màu, kích thước lấy từ thiết kế mới. Chỗ thiết kế lệch hệ thống đang chạy hoặc lệch quy tắc giữ lại thì ghi vào note bảng "Chỗ lệch thiết kế và hệ thống", hỏi người dùng chỗ chặn.
- Cột data-testid đặt theo quy ước dự án cho cả thành phần mới.

## 5. Testcase

Duyệt SRS xong, gợi ý `/viet-testcase` cho file `(new)`. Note của testcase ghi bảng case cũ ở `.test.md` của SRS cũ: Mã TC | Xử lý (Dùng lại, Sửa, Bỏ). Testcase List trên sheet và script automation chỉ đổi khi chuyển bản ở mục 6.

## 6. Khi bản mới lên Production: chuyển bản

Làm khi người dùng báo đã build Production bản có màn renew (hoặc trong Bước 7 của `/lam-task-jira`). Theo `<SKILL_BA>/_chung/sua-tai-lieu-da-xong.md`: lập bảng việc sẽ làm, người dùng duyệt rồi mới làm.

1. **Lưu bản cũ:** chuyển SRS cũ cùng `.test.md`, `.auto.md`, `.note.md` vào **Thư mục lưu trữ SRS** (khóa ở cấu hình, mặc định `<Thư mục SRS>/_luu-tru/`), giữ nguyên cây thư mục con. Tên file thêm hậu tố ngày thôi dùng, ví dụ `Trang chủ (đến 2026-10-30).md`. Dùng `git mv` để giữ lịch sử.
2. **Ghi chú đầu bản lưu:** thêm một dòng trích dẫn ở đầu file lưu "Bản lưu trữ, không còn hiệu lực từ <ngày>. Bản hiện hành: <link file mới>".
3. **Ảnh:** ảnh trong `_attachments` chỉ bản cũ dùng thì chuyển theo vào thư mục lưu trữ, ảnh dùng chung thì giữ chỗ cũ. Sửa đường dẫn ảnh trong bản lưu cho mở được.
4. **Đổi tên bản mới:** bỏ hậu tố ` (new)` ở SRS và các file đi kèm, dùng `git mv`. Lịch sử thay đổi thêm dòng "Áp dụng chính thức".
5. **Sửa tham chiếu:** grep tên file cũ và tên `(new)` trên toàn thư mục tài liệu (CR, SRS khác, README, mục lục), sửa link trỏ về bản hiện hành. CR cũ giữ nguyên link nếu đó là lịch sử.
6. **Testcase và automation:** báo người dùng Testcase List trên sheet cần đồng bộ lại theo tên file mới, script automation có tham chiếu tên file hay mã case cũ cần đổi. Chỉ làm khi người dùng đồng ý.
7. Báo lại: file đã lưu, file đã đổi tên, link đã sửa, việc còn chờ.
