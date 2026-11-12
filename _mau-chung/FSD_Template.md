# FSD - [Tên cổng / module]

> Dòng bắt đầu bằng `>` là hướng dẫn, xóa khi viết thật.
>
> **Chọn bố cục trước khi viết:**
> - Dự án nhỏ, một file FSD: giữ mục 1 Quy định dùng chung trong file này.
> - Dự án nhiều module hoặc nhiều cổng: tách mục 1 thành file riêng `FSD - Quy định dùng chung.md` (giữ nguyên các mục con), mỗi FSD module bỏ mục 1, chỉ ghi một câu ở mục 0 trỏ sang file đó.
>
> Mục nào ghi "(theo điều kiện)" thì chỉ viết khi dự án có điều kiện đó, không có thì xóa cả mục.

## 0. Thông tin chung

[2 đến 3 câu: hệ thống gì, cổng/module này dùng để làm gì, ai dùng. Chỉ nhắc tới site, cổng khác khi hệ thống thật sự có.]

![Sơ đồ phân rã chức năng [tên cổng / module]](Hinh/so-do-phan-ra-[ten].png)

> Dùng lại sơ đồ phân rã đã duyệt (của BRD hoặc vẽ bằng /phan-ra-chuc-nang). Mỗi nút trong phạm vi phải có màn hoặc quy tắc tương ứng trong FSD.

![Sơ đồ phân rã chức năng [tên cổng / module]](Hinh/so-do-phan-ra-[ten].png)

> Dùng lại sơ đồ phân rã đã duyệt (của BRD hoặc vẽ bằng /phan-ra-chuc-nang). Mỗi nút trong phạm vi phải có màn hoặc quy tắc tương ứng trong FSD.

---

## 1. Quy định dùng chung

### 1.1 Phạm vi dữ liệu và phân quyền

- **BR-C01:** [Ai đăng nhập được, tài khoản được tạo ra sao]
- **BR-C02a:** [Người dùng chỉ thấy dữ liệu nào]
- **BR-C02b:** [Giới hạn được chặn ở phía máy chủ, gọi thẳng đường dẫn thì bị từ chối]

### 1.2 Quy tắc dữ liệu chung

- **BR-C03:** [Danh mục dùng chung, quy tắc trùng, chuẩn hóa dữ liệu, quan hệ giữa các đối tượng]

### 1.3 Vòng đời trạng thái

| Đối tượng | Trạng thái | Ảnh hưởng khi ở trạng thái này | Chuyển được sang |
|---|---|---|---|
| [Đối tượng] | [Trạng thái] | [Ai làm được gì, ai thấy gì] | [Trạng thái kế tiếp] |

- **BR-C04:** [Ai đổi trạng thái, có tự đổi theo thời gian không]

### 1.4 Trạng thái màn hình chuẩn

Áp cho mọi màn. Màn nào làm khác thì ghi thành BR của màn đó.

| Trạng thái | Điều kiện xảy ra | Hiển thị | Thông báo |
|---|---|---|---|
| Mặc định | Mở màn lần đầu | [Bộ lọc mặc định, thứ tự dữ liệu] | |
| Đang tải | Đã gọi dữ liệu, chưa có phản hồi | [Khung giữ chỗ, nút nào bị khóa] | |
| Không có dữ liệu | Chưa có bản ghi nào thuộc phạm vi màn | [Cách hiện] | Câu riêng của từng màn, ghi ở Business Rules của màn |
| Không có kết quả lọc | Có dữ liệu nhưng không bản ghi nào khớp | [Cách hiện, bộ lọc giữ nguyên] | "[Câu thông báo]" |
| Lỗi hệ thống khi tải | Mất kết nối, lỗi máy chủ, hết thời gian chờ | [Khối lỗi, nút Thử lại] | "[Câu thông báo]" |
| Lỗi hệ thống khi lưu | Như trên, xảy ra lúc bấm lưu | [Popup không đóng, dữ liệu giữ nguyên] | "[Câu thông báo]" |
| Hết hạn phiên | Phiên hết hiệu lực, hoặc tài khoản bị khóa khi đang dùng | [Đưa về trang đăng nhập] | "[Câu thông báo]" |

### 1.5 Quy định phiên đăng nhập

- **BR-C05:** [Thời gian hết phiên, thao tác nào tính là đang dùng]
- **BR-C06:** Hết phiên khi đang xem màn: [hành vi]
- **BR-C07:** Hết phiên khi đang nhập dở trong popup: [hành vi]
- **BR-C08:** Hết phiên đúng lúc bấm nút xử lý: [hành vi]
- **BR-C09:** Bị khóa hoặc mất quyền khi phiên còn hiệu lực: [hành vi]

### 1.6 Quy ước định dạng, tệp tải lên, tìm kiếm

**Định dạng hiển thị**

- **BR-C10:** [Ngày, số, tiền, dung lượng, trường trống, chữ dài]

**Tệp tải lên** (bỏ nếu hệ thống không có tải tệp)

| Loại tệp | Định dạng | Dung lượng | Số tệp |
|---|---|---|---|
| [Loại] | [Đuôi tệp] | [Tối đa] | [Tối thiểu, tối đa] |

- **BR-C11a:** [Kiểm tra định dạng theo nội dung tệp]
- **BR-C11b:** [Câu báo khi sai định dạng, vượt dung lượng, tải lỗi]

**Tìm kiếm**

- **BR-C12:** [Hoa thường, dấu tiếng Việt, khớp một phần, khoảng trắng, thời điểm cập nhật kết quả, về trang một]

### 1.7 Ảnh hưởng chéo giữa các cổng (theo điều kiện: hệ thống có từ hai site/cổng dùng chung dữ liệu)

| Thao tác ở [Cổng A] | Ảnh hưởng ở [Cổng B] |
|---|---|
| [Thao tác] | [Dữ liệu, màn nào đổi, người đang mở màn thì thấy gì] |

### 1.8 Luồng tích hợp giữa các module (theo điều kiện: có nhiều module trao đổi dữ liệu)

| Thao tác | Bản ghi hiện ở | Bản ghi mất khỏi | Module bị ảnh hưởng dây chuyền |
|---|---|---|---|
| [Thao tác] | [Menu, tab] | [Menu, tab] | [Dữ liệu nào đổi theo] |

### 1.9 Lưu ý kỹ thuật cần dev xác nhận sớm (theo điều kiện: có điểm tốn công hoặc có rủi ro thật)

Các mục dưới đây không đặc tả cách làm, chỉ nêu để dev ước lượng.

1. **[Chủ đề]:** [Vì sao tốn công hoặc có rủi ro]

### 1.10 Sơ đồ luồng tổng thể

![Luồng tổng quan [tên hệ thống]](Hinh/so-do-luong-tong-the.png)

---

## 2. Sơ đồ màn hình [tên cổng / module]

Mã màn trong sơ đồ dùng để tra sang các mục bên dưới.

![Sơ đồ màn hình [tên cổng]](Hinh/so-do-man-hinh-[ten].png)

---

## 3. SCR-[X]01: [Tên màn]

### 3.1 Tổng quan

> Popup con dùng chung User story của màn cha, chỉ viết Pre/Post-condition nếu khác màn cha.

**User story**

- [US-xx] Là [vai trò], tôi muốn [việc làm trên màn này] để [lợi ích].

> Có BRD thì ghi mã user story của BRD ở đầu dòng. Một màn có thể ứng với nhiều story. Chưa có BRD thì bỏ mã.

**Pre-condition**

- [Người dùng đã đăng nhập, có quyền gì, dữ liệu nào phải có sẵn]

**Post-condition**

> Chỉ viết cho màn có làm đổi dữ liệu. Màn chỉ để xem thì bỏ phần này.

- [Trạng thái hệ thống sau khi hoàn tất thao tác: bản ghi mới, trạng thái mới, ai nhận được gì]

### 3.2 Đặc tả màn hình

![SCR-[X]01 [Tên màn]](<Mockup/[tên ảnh].png>)

**Trường thông tin**

| Tên trường | Loại | Bắt buộc | Giá trị mặc định | Mô tả |
|---|---|---|---|---|
| [Tên] | [Textbox (1–255 ký tự) / Dropdown<br>(Chọn một giá trị) / ...] | [Có/Không] | [Mặc định] | [Quy tắc nhập, danh sách giá trị, câu báo lỗi nguyên văn] |

**Cột bảng dữ liệu**

| Tên cột | Kiểu hiển thị | Mô tả dữ liệu |
|---|---|---|
| [Tên cột] | [Text, ngày, badge, link...] | [Lấy dữ liệu gì, trống thì hiện gì] |

**Nút chức năng**

| Tên nút | Mô tả |
|---|---|
| [Tên nút] | [Bấm thì làm gì, mở màn nào, mang dữ liệu gì. Điều kiện hiện hoặc khóa nếu có] |

**Business Rules**

- **BR-[X]01:** [Một ý một BR. Câu thông báo viết nguyên văn tại chỗ]
- **BR-[X]02a:** [BR dài thì tách BR con a, b, c]
- **BR-[X]02b:** [Điều kiện liệt kê thành gạch đầu dòng con]

**Giao diện theo kích thước màn hình** (theo điều kiện: User story có bản tablet hoặc điện thoại)

> Business Rules, dữ liệu, phân quyền viết một lần. Phần này chỉ gồm link thiết kế cả ba bản, breakpoint và hành vi thành phần khác nhau. Xem `_chung/da-nen-tang.md`.

- Thiết kế: [link máy tính], [link tablet], [link điện thoại].
- Breakpoint: [máy tính từ ...px, tablet từ ...px tới dưới ...px, điện thoại dưới ...px].
- Hành vi thành phần: [thành phần] ở [bản] thì [ẩn, hiện, co giãn, chuyển dạng, đổi hover thành chạm...].

### 3.3 Use case (theo điều kiện: màn có luồng nhiều bước hoặc nhiều nhánh ngoại lệ, ví dụ import, duyệt, cấp phát)

| Mục | Nội dung |
|---|---|
| Tác nhân | [Vai trò] |
| Luồng chính | 1. [Bước]<br>2. [Bước]<br>#Kết thúc |
| Luồng ngoại lệ | 2a. [Điều kiện]: [hệ thống làm gì]<br>#Kết thúc |

---

## [N]. Tiêu chí chấp nhận

### [Tên màn]

**[Nhóm: Hiển thị / Tạo mới / Lọc, phân trang, xuất báo cáo...]:**

- [ ] [Điều kiện cụ thể thì kết quả đo được, câu thông báo nguyên văn]

### Dùng chung mọi màn

**Phân quyền:**

- [ ] [AC]

**Trạng thái màn và lỗi:**

- [ ] [AC]

**Hết hạn phiên:**

- [ ] [AC]

**Định dạng chung:**

- [ ] [AC]

---

## Nhật ký thay đổi

| Phiên bản | Ngày | Nội dung |
|---|---|---|
| 0.1 | [DD/MM/YYYY] | Viết lần đầu theo [nguồn: design, biên bản họp...] |
