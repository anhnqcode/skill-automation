# SRS và FSD cho nhiều kích thước màn hình (desktop, tablet, mobile)

Áp dụng khi màn có từ hai bản giao diện (máy tính, tablet, điện thoại) hoặc nhiều nền tảng dùng chung một nghiệp vụ. Chốt ngày 22/10/2026.

## 1. Nguyên tắc: tách logic dùng chung và giao diện dùng riêng

| Phần | Viết thế nào |
|---|---|
| Business Rules, dữ liệu, API, phân quyền, trạng thái, thông báo | Viết một lần duy nhất, dùng chung cho mọi kích thước màn. Logic xử lý dữ liệu giống hệt nhau dù ở nền tảng nào (điều kiện tạo, công thức tính, thứ tự dữ liệu, điều kiện hiện nút). Không chép lại cho từng bản. |
| Giao diện và tương tác | Viết riêng cho từng kích thước màn, chỉ ghi chỗ khác nhau. Ví dụ máy tính dùng thao tác di chuột (hover), tablet và điện thoại chuyển thành chạm (tap) hoặc vuốt (swipe). Máy tính hiện bảng 10 cột thì điện thoại chuyển thành thẻ (card) hoặc ẩn bớt cột phụ. |

## 2. Phần UI/UX của từng màn (SRS) hoặc từng User Story (FSD)

Chỉ cần ba thứ, không mô tả lại từng thành phần cho từng kích thước:

1. **Link thiết kế của cả ba bản** (máy tính, tablet, điện thoại), ghi tên board.
2. **Breakpoint:** kích thước màn mà giao diện đổi cấu trúc. Ghi bằng bảng: Tên bản | Chiều rộng áp dụng | Chiều rộng thiết kế chuẩn.
3. **Quy tắc hành vi của thành phần (element behavior)** khi đổi kích thước: ẩn, hiện, co giãn, xuống dòng, trượt ngang, chuyển dạng (bảng thành thẻ), đổi cách thao tác (hover thành chạm). Chỉ ghi thành phần có khác biệt. Thành phần không khác thì không ghi.

## 3. Mẫu viết

Bảng breakpoint:

| Bản | Chiều rộng áp dụng | Thiết kế chuẩn |
|:---|:---|:---|
| Máy tính | từ 1024px | 1440px |
| Tablet | từ 768px tới dưới 1024px | 768px |
| Điện thoại | dưới 768px | 375px |

Bảng hành vi thành phần (cột theo bản, ô nào không khác thì bỏ trống hoặc gộp):

| Thành phần | Máy tính | Tablet | Điện thoại |
|:---|:---|:---|:---|
| [Tên thành phần] | [Cách hiển thị và thao tác] | [Chỉ ghi chỗ khác] | [Chỉ ghi chỗ khác] |

## 4. Lưu ý khi viết

- Câu viết thẳng nội dung. Không viết "giống bản máy tính", "như SCR01", "theo BR..." (xem mục 5 `van-phong.md`). Ô cột tablet hoặc điện thoại nào khác thì viết đủ cách hiển thị ở ô đó.
- Con số kích thước, số thẻ hiển thị, số lượt, số cột lấy từ thiết kế hoặc ghi chú trên thiết kế, không tự đặt.
- Chữ hiển thị, câu thông báo, điều kiện hiện nút giống nhau ở cả ba bản thì chỉ viết ở phần dùng chung, không nhắc lại.
- Mỗi kích thước màn có AC riêng cho phần hành vi khác nhau (ẩn, hiện, co giãn, trượt, dính khi cuộn), AC nghiệp vụ chỉ viết một lần. Testcase theo cùng cách: case nghiệp vụ chạy ở bản máy tính, case giao diện chạy ở từng bản.
- Thiết kế có ghi chú về hành vi ngay trên Penpot hoặc Figma: đọc để lấy đúng quy tắc, SRS vẫn viết lại thành câu để tester không phải mở thiết kế mới hiểu hành vi.
