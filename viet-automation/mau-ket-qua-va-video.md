# Mẫu file kết quả và video luồng

## 1. File kết quả kiểm thử

Mỗi cổng hoặc mỗi phân hệ một file: `Kết quả kiểm thử tự động - <tên cổng>.md`, đặt trong thư mục Automation của dự án. Kết quả gốc dạng JSON và ảnh đặt trong `ket-qua/<thời điểm chạy>/`, sau mỗi đợt gộp vào `ket-qua/tong-hop/`.

```markdown
# Kết quả kiểm thử tự động - <tên cổng>

| | |
|:---|:---|
| Ngày chạy | <ngày, các lần chạy L1, L2...> |
| Phạm vi | <các nhóm đã kiểm> |
| Đối chiếu với | <FSD, tiêu chí chấp nhận, checklist, bộ design (tên tệp, ngày)> |
| Công cụ | Playwright, kịch bản <tên file> |
| Dữ liệu kiểm thử | Xem mục Dữ liệu kiểm thử đã tạo |

## 1. Rủi ro trọng tâm         (3 đến 5 câu từ bước phân tích)
## 2. Tổng quan                (đếm từ cột Kết quả, bảng theo nhóm, ba đến năm dòng nhận xét)
## 3. Danh sách lỗi
## 4. Bị chặn
## 5. Cần xác nhận             (ghi đề xuất)
## 6. Chỗ khác FSD             (đã cập nhật FSD theo hệ thống / cần chốt)
## 7. Chỗ lệch với design      (trỏ sang file Đối chiếu giao diện với design.md)
## 8. Chưa kiểm                (kèm lý do từng mục)
## 9. Sự cố trong lúc chạy     (kịch bản đánh giá sai, dữ liệu bị ảnh hưởng, đã khắc phục ra sao)
## 10. Dữ liệu kiểm thử đã tạo
## 11. Chi tiết từng mục kiểm tra
| Mã | Lần | Màn | Nội dung kiểm tra | Mong muốn | Thực tế | Kết quả | Quy tắc |
```

File này dùng được như một bộ testcase đã chạy. Khi cần, chuyển sang mẫu testcase chuẩn của dự án bằng `/viet-testcase` mà không phải viết lại.

### Giá trị Kết quả

Mỗi mục chỉ có một giá trị. Bảng Tổng quan đếm từ cột Kết quả, không đếm tay. Hàm ghi kết quả nhận thẳng giá trị này, không nhận đúng hoặc sai.

| Giá trị | Nghĩa |
|:---|:---|
| Đạt | Thực tế khớp mong muốn cụ thể |
| Lỗi | Lệch FSD, tiêu chí chấp nhận hoặc quy tắc chung, đã xác minh lại |
| Cần xác nhận | FSD không nói, hoặc hệ thống làm khác FSD nhưng hợp lý |
| Bị chặn | Chức năng đang tắt hoặc môi trường thiếu, không chạy được. Ghi điều kiện để mở |
| Không tạo được tình huống | Thiếu dữ liệu tiền đề. Ghi dữ liệu cần dựng |
| Chưa kiểm | Chủ động để kiểm tay. Ghi lý do |

### Mức độ lỗi

Ghi kèm một câu lý do.

| Mức | Khi nào |
|:---|:---|
| Cao | Chặn luồng chính; mất hoặc sai dữ liệu; sai quyền; lộ dữ liệu cá nhân; sai số liệu dùng để báo cáo; mã độc chạy được |
| Trung bình | Chức năng chạy nhưng sai quy tắc FSD, có đường vòng; mất thao tác ở khổ màn hình phổ biến (1280, 1366); thông báo sai làm người dùng hiểu nhầm |
| Thấp | Chữ, màu, cỡ, bố cục lệch design, không ảnh hưởng thao tác |

### Mỗi lỗi BUG-xx

Một dãy mã duy nhất cho mọi nguồn: kịch bản, đối chiếu design, phát hiện khi xem ảnh. Mỗi lỗi một bảng gồm:

| Trường | Ghi gì |
|:---|:---|
| Trạng thái | Mở / Đóng (đã sửa ở L2) / Đóng (chấp nhận theo hệ thống, kèm ngày) |
| Mức độ | Theo bảng trên, kèm lý do |
| Cổng, Màn, Tab hoặc khu vực | Tách riêng để `/log-bug` dựng Summary `[Cổng][Màn][Tab]` |
| Quy tắc | Mã BR hoặc mục AC, mục template (để truy vết, không gửi dev) |
| Bước tái hiện | Đánh số |
| Mong muốn | Có thể dẫn quy tắc |
| Mong muốn cho dev | Bằng lời thường, không mã BR, dùng làm Expect khi log bug |
| Thực tế | Có số đo nếu là lỗi giao diện |
| Ảnh, khổ chụp | Ảnh 2x, khổ khung nhìn lúc thấy lỗi |
| Trace | Đường dẫn trace trong thư mục tạm, nếu còn |
| ID sheet bug, Trạng thái sheet | Điền sau khi log bằng `/log-bug` |

Tương ứng trạng thái với sheet bug: Mở là Todo; Đóng (chấp nhận) là Closed; Đóng (đã sửa ở L2) là Passed.

### Mã mục kiểm

- Mã ổn định theo dự án: `<nhóm>-<số>` (A-01, DMK-05, CH-08). Không đánh lại mã giữa các đợt, các lần chạy.
- Chạy lại thì giữ mã cũ, cập nhật cột Lần (L1, L2...) và Kết quả, không tạo mã mới cho mục cũ.

### JSON kết quả

Mỗi mục gồm: `ma`, `lan`, `phan`, `noi_dung`, `mong_muon`, `thuc_te`, `ket_qua`, `anh`, `kho`, `nguon` (mã BR, mục AC hoặc mục template), `loi_ngam` (lỗi console, lỗi JS, phản hồi 4xx/5xx phát sinh trong lúc chạy mục đó). Hàm `ghi()` trong `mau_chung.py` đã dựng sẵn các trường này.

## 2. Video luồng E2E có chú thích

**Chỉ làm khi người dùng yêu cầu.** Mục đích: người dùng chưa có thời gian test vẫn nắm được hệ thống chạy thế nào và mỗi bước có ý nghĩa nghiệp vụ gì.

| Việc | Cách làm |
|:---|:---|
| Đăng nhập | Đăng nhập ngầm ngoài video, lưu cookie phiên của từng vai trò. Chuyển vai trò bằng cách thay cookie, video không quay màn nhập tài khoản |
| Chú thích | Chèn khung chú thích bằng `add_init_script`: số bước, tiêu đề ngắn, một hai câu **ý nghĩa nghiệp vụ**. Ví dụ: "Quản trị tạo chiến dịch tập huấn. Chiến dịch là khung chứa chủ đề, học liệu và danh sách giáo viên; giáo viên được thêm vào chiến dịch mới xem được học liệu của nó." Không chỉ mô tả thao tác bấm gì |
| Che thông tin | Một khối che cố định vùng tài khoản ở góc trên phải trong suốt video. Kiểm lại khung hình đầu và cuối |
| Nhịp | Gõ chữ chậm có độ trễ, dừng 5 đến 7 giây ở mỗi chú thích |
| Xuất | Quay bằng `record_video_dir`, đổi sang mp4 bằng ffmpeg, khổ 1440 × 900 |
| Ảnh từng bước | Chụp một ảnh mỗi bước, lưu `buoc-v<số video>-<số bước>.png` và `buoc.json` |
| File mô tả | `Luồng E2E - <tên>.md`: link video, rồi từng bước gồm tiêu đề, ý nghĩa, ảnh |
| Dữ liệu | Video tạo dữ liệu thì đặt tên `Thử nghiệm ...`, tránh trùng với lần quay trước. Video sau xóa dữ liệu video trước tạo ra nếu luồng cho phép |

Nên chia: một video luồng chính của từng cổng, một video ảnh hưởng chéo giữa các cổng.

Giao diện đổi (dev sửa theo design mới) thì quay lại video liên quan, sửa chú thích cho khớp, cập nhật file mô tả và xóa bản quay cũ khi không còn file nào trỏ tới.

Cài đặt mẫu: thư mục Automation của dự án mẫu (đường dẫn ghi ở `_du-an/<dự án>.md`, mục Automation), các file `e2e_luong_nghiep_vu.py` (khung chú thích, hàm `chu_thich`, `go_cham`) và `e2e_video_2cong.py` (đổi vai trò bằng cookie, xuất mp4).
