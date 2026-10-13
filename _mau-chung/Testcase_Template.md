# Quy tắc & Mẫu sinh Test Case
### [Mã tài liệu] — [Tên màn hình / Tên chức năng]

---

## 1. Quy tắc chung

### 1.1. Ngôn ngữ đầu ra

Bắt buộc sử dụng tiếng Việt cho toàn bộ nội dung:

- Tiêu đề nhóm testcase
- Tên testcase
- Mục đích kiểm thử
- Tiền điều kiện
- Các bước thực hiện
- Kết quả mong muốn
- Ghi chú

Không sử dụng tiêu đề tiếng Anh.

| ❌ Không dùng | ✅ Dùng |
|---|---|
| Default State Validation | Kiểm tra trạng thái mặc định |
| Field Validation | Kiểm tra trường dữ liệu |
| Business Rule Validation | Kiểm tra quy tắc nghiệp vụ |

### 1.2. Cấu trúc nhóm testcase

Testcase phải được nhóm theo **2 cấp**: cấp 1 là từng màn hình/chức năng, cấp 2 là từng loại validation áp dụng cho màn hình/chức năng đó.

**Cấp 1 — Theo màn hình/chức năng:** liệt kê tất cả màn hình/chức năng thuộc phạm vi kiểm thử, theo đúng thứ tự luồng người dùng sẽ gặp trong thực tế (ví dụ: màn Danh sách → Bộ lọc/Tìm kiếm (nếu đủ phức tạp để tách riêng) → Thêm mới → Chỉnh sửa → Xóa → các chức năng khác nếu có).

**Cấp 2 — Theo loại validation:** trong mỗi mục cấp 1, liệt kê đầy đủ các nhóm validation áp dụng cho màn hình/chức năng đó theo đúng tên gọi chuẩn đã quy định (Kiểm tra trạng thái mặc định, Kiểm tra trường dữ liệu, Kiểm tra quy tắc nghiệp vụ, Kiểm tra dữ liệu, Kiểm tra lưu trữ dữ liệu, Kiểm tra phân quyền, Kiểm tra xóa dữ liệu, Kiểm tra đồng bộ dữ liệu, Kiểm tra trạng thái Enable/Disable, Kiểm tra cấu hình...) — không cần và không được chú thêm tên màn hình/chức năng trong ngoặc đơn ở tiêu đề nhóm cấp 2, vì ngữ cảnh đã được xác định rõ ở tiêu đề cấp 1.

Khi nhóm cấp 2 là "Kiểm tra trường dữ liệu", tiếp tục tách theo từng trường cụ thể của màn hình/chức năng đó (theo đúng tên field và loại control) — đây là **cấp 3**.

**Cách đánh số:** dùng số thứ tự dạng `1.1`, `1.2`, `1.2.1`... thay vì gạch đầu dòng, để đồng nhất với cách đánh số xuyên suốt tài liệu này và để có thể tham chiếu qua lại giữa các nhóm (ví dụ "xem case nhóm 2.3"). Việc đánh số dừng lại ở cấp 3 (theo từng trường); không đánh tiếp thành cấp 4. Từng testcase cụ thể bên trong mỗi nhóm vẫn dùng ID riêng theo mẫu bảng tại Mục 23 (`TC-[Mã]-001`...), không đánh nối tiếp theo số nhóm.

**Khung cấu trúc:**

```
1. [Tên màn hình/chức năng 1]

   1.1. Kiểm tra hiển thị mặc định

   1.2. Kiểm tra trường dữ liệu

      1.2.1. Trường "[Tên trường A]" ([Loại control])
      1.2.2. Trường "[Tên trường B]" ([Loại control])

   1.3. Kiểm tra quy tắc nghiệp vụ

   1.4. Kiểm tra dữ liệu

   1.5. Kiểm tra lưu trữ dữ liệu

   1.6. Kiểm tra phân quyền

   1.7. (Các nhóm khác nếu áp dụng — xóa dữ liệu, đồng bộ dữ liệu, enable/disable, cấu hình...)

2. [Tên màn hình/chức năng 2]

   2.1. Kiểm tra hiển thị mặc định

   2.2. Kiểm tra trường dữ liệu

      2.2.1. ...

   2.3. ...
```

> Không gộp validation của nhiều màn hình/chức năng vào cùng một mục cấp 1. Không đặt tên màn hình/chức năng trong ngoặc đơn ở tiêu đề cấp 2 — tên màn hình/chức năng chỉ xuất hiện đúng một lần ở tiêu đề cấp 1.

> Không được sinh testcase ngẫu nhiên hoặc trộn nhiều nhóm validation trong cùng một nhóm.

### 1.3. Quy tắc đặt tên Control

| Tiếng Anh | Tiếng Việt |
|---|---|
| Textbox | Ô nhập liệu |
| Textarea | Ô nhập liệu nhiều dòng |
| Number Field | Trường số |
| DatePicker | Chọn ngày |
| Dropdown | Danh sách chọn |
| Select | Danh sách chọn |
| Multi Select | Danh sách chọn nhiều giá trị |
| Checkbox | Hộp kiểm |
| Radio Button | Nút chọn đơn |
| Lookup | Tra cứu dữ liệu |
| Autocomplete | Gợi ý dữ liệu |
| Upload | Tải tệp |

### 1.4. Phạm vi bao phủ bắt buộc

- Luồng thành công — xem Mục 6 (hành vi sau khi thao tác thành công)
- Dữ liệu không hợp lệ
- Giá trị biên
- Trạng thái bật/tắt (Enable/Disable) — xem Mục 13
- Cấu hình khác nhau (Config case) — xem Mục 14
- Hiển thị giao diện
- Phân quyền — xem Mục 9
- Hồi quy — xem Mục 11
- Xử lý lỗi hệ thống (kiểm thử thủ công) — xem Mục 15
- Lưu trữ dữ liệu — xem Mục 7
- Đồng bộ dữ liệu — xem Mục 12
- Bộ lọc & tìm kiếm (nếu màn hình Danh sách có chức năng này) — xem Mục 4
- Export/Print dữ liệu (nếu màn hình có chức năng này) — xem Mục 19
- **Import/Export hàng loạt dữ liệu** (nếu màn hình có chức năng tải file mẫu và nhập dữ liệu hàng loạt) — xem Mục 20
- **Chuyển đổi trạng thái và thứ tự thao tác phi logic** (nếu chức năng có trạng thái hoặc vai trò thay đổi động) — xem Mục 25
- **Hoàn tác / Khôi phục thao tác** (nếu chức năng có tính năng Undo, lịch sử phiên bản, hoặc rollback giao dịch) — xem Mục 26
- **Luồng nghiệp vụ xuyên module** (nếu chức năng liên quan đến nhiều module/portal/actor) — xem Mục 27
- **Tác vụ theo thời gian** (nếu chức năng có hành vi tự động kích hoạt theo lịch, đếm ngược, hoặc gia hạn tự động) — xem Mục 28
- Web/Mobile (nếu áp dụng) — xem Mục 21, chỉ áp dụng với module có hỗ trợ Mobile

### 1.5. Các nhóm kiểm thử bắt buộc

Bộ gốc yêu cầu tối thiểu 5 nhóm. Bản cập nhật này mở rộng thành **18 nhóm bắt buộc** để phản ánh đúng phạm vi bao phủ đã nêu ở Mục 1.4:

1. Kiểm tra trạng thái mặc định
2. Kiểm tra trường dữ liệu
3. Kiểm tra hành vi sau khi thao tác thành công *(xem Mục 6)*
4. Kiểm tra quy tắc nghiệp vụ
5. Kiểm tra dữ liệu
6. Kiểm tra lưu trữ dữ liệu *(xem Mục 7)*
7. Kiểm tra phân quyền *(xem Mục 9)*
8. Kiểm tra xóa dữ liệu *(xem Mục 10)*
9. Kiểm tra đồng bộ dữ liệu *(xem Mục 12, chỉ áp dụng nếu chức năng có chia sẻ/đồng bộ dữ liệu)*
10. Kiểm tra trạng thái Enable/Disable *(xem Mục 13, chỉ áp dụng nếu màn hình có control phụ thuộc điều kiện)*
11. Kiểm tra cấu hình *(xem Mục 14, chỉ áp dụng nếu chức năng có tham số cấu hình ảnh hưởng hành vi)*
12. Kiểm tra Bộ lọc & Tìm kiếm *(xem Mục 4, chỉ áp dụng với màn hình Danh sách có chức năng lọc/tìm kiếm)*
13. Kiểm tra Export/Print dữ liệu *(xem Mục 19, chỉ áp dụng nếu màn hình có chức năng xuất file/in)*
14. Kiểm tra Import/Export hàng loạt dữ liệu *(xem Mục 20, chỉ áp dụng nếu màn hình có chức năng nhập dữ liệu hàng loạt qua file)*
15. Kiểm tra chuyển đổi trạng thái *(xem Mục 25, chỉ áp dụng nếu chức năng có trạng thái thay đổi động hoặc có gán vai trò sau thao tác)*
16. Kiểm tra Hoàn tác / Khôi phục thao tác *(xem Mục 26, chỉ áp dụng nếu chức năng có tính năng Undo/lịch sử phiên bản/rollback)*
17. Kiểm tra luồng nghiệp vụ xuyên module *(xem Mục 27, chỉ áp dụng nếu chức năng liên quan đến nhiều module/portal/actor)*
18. Kiểm tra tác vụ theo thời gian *(xem Mục 28, chỉ áp dụng nếu chức năng có hành vi tự động kích hoạt theo lịch/đếm ngược/gia hạn tự động)*

> Kiểm tra hồi quy (Mục 11) không tính là nhóm bắt buộc theo từng bộ test case ban đầu, vì đây là hoạt động áp dụng **khi có thay đổi** trên chức năng đã tồn tại — nhưng bắt buộc phải có khi thực hiện thay đổi/nâng cấp.

> Kiểm tra xử lý lỗi hệ thống (Mục 15) khuyến nghị áp dụng cho mọi chức năng có hành động lưu/gửi dữ liệu, không tính là nhóm bắt buộc riêng theo từng trường mà áp dụng ở mức tổng thể của chức năng.

> Kiểm tra giao diện Responsive/Cross-platform (Mục 21) chỉ bắt buộc với module có hỗ trợ Mobile. Với module thuần desktop/web nội bộ, bỏ qua nhóm này và không tính là thiếu sót.

> Nếu thiếu bất kỳ nhóm nào (trừ trường hợp không áp dụng được, ví dụ màn hình không có chức năng xóa hoặc không có control phụ thuộc điều kiện) thì bộ testcase được xem là chưa hoàn chỉnh.

### 1.6. Ranh giới giữa "Kiểm tra trường dữ liệu" và "Kiểm tra dữ liệu"

Hai tên nhóm này dễ gây nhầm lẫn vì đều liên quan đến "dữ liệu". Quy ước phân biệt như sau:

| Tiêu chí | Kiểm tra trường dữ liệu (Field-level) | Kiểm tra dữ liệu (Data-level) |
|---|---|---|
| **Phạm vi** | Từng control/trường riêng lẻ, tách biệt khỏi các trường khác | Toàn bộ bản ghi, sau khi dữ liệu đã được lưu hoặc tổng hợp từ nhiều trường |
| **Mục tiêu** | Validate input ngay tại trường đó: định dạng, độ dài, kiểu dữ liệu, giá trị biên | Tính đúng đắn, toàn vẹn (integrity) và nhất quán (consistency) của dữ liệu sau xử lý |
| **Ví dụ** | Trường "Số lượng" không cho nhập số âm | Tổng tiền = Số lượng × Đơn giá phải khớp với giá trị hiển thị/lưu trong DB |
| **Thời điểm** | Ngay khi người dùng nhập/chọn, trước khi submit | Sau khi submit, khi đọc lại từ DB, khi hiển thị ở màn hình khác, hoặc khi tính toán liên trường |
| **Loại lỗi phát hiện** | Lỗi validate input (client-side) | Lỗi tính toán, mapping sai, làm tròn số, mất dữ liệu, lệch dữ liệu giữa các màn hình/module |

**Checklist con của "Kiểm tra dữ liệu" (Data-level — Mục 5.10):**

- Dữ liệu hiển thị đúng với dữ liệu đã lưu trong cơ sở dữ liệu (không bị sai lệch, không bị cắt bớt, không bị encode/decode sai)
- Dữ liệu tính toán (tổng, trung bình, %, làm tròn) cho kết quả đúng với công thức nghiệp vụ
- Dữ liệu hiển thị nhất quán giữa các màn hình khác nhau cùng tham chiếu một bản ghi
- Dữ liệu dạng số được làm tròn/định dạng đúng quy tắc (số chữ số sau phẩy, đơn vị tiền tệ)
- Dữ liệu ngày giờ hiển thị đúng theo định dạng và múi giờ quy định
- Dữ liệu liên quan (master-detail, dữ liệu cha-con) khớp nhau, không có dữ liệu con "mồ côi"
- Dữ liệu không bị thay đổi ngoài ý muốn khi thực hiện các hành động khác (sửa trường A không làm sai trường B)
- Dữ liệu lớn (nhiều bản ghi, chuỗi dài, file lớn) không gây sai lệch hoặc mất dữ liệu khi xử lý

> Quy ước áp dụng: mọi lỗi liên quan đến **một control đơn lẻ** trước khi lưu → xếp vào nhóm "Kiểm tra trường dữ liệu". Mọi lỗi liên quan đến **kết quả sau xử lý/lưu/tính toán/hiển thị lại** → xếp vào nhóm "Kiểm tra dữ liệu". Điều này tránh trùng lặp test case giữa hai nhóm.

### 1.7. Quy tắc sinh testcase

Không được tạo testcase dạng gộp như:

- TC01 Happy Case
- TC02 Invalid Case
- TC03 Boundary Case

Mỗi validation phải là **một testcase riêng biệt**. Ví dụ đúng:

- TC01 Nhập ngày hợp lệ
- TC02 Để trống ngày
- TC03 Nhập sai định dạng ngày
- TC04 Nhập ngày không tồn tại
- TC05 Chọn ngày nhỏ hơn ngày tối thiểu
- TC06 Chọn ngày lớn hơn ngày tối đa

> Không gộp nhiều validation vào cùng một testcase.

### 1.8. Quy tắc viết kết quả mong muốn

Kết quả mong muốn phải mô tả rõ:

- Hệ thống xử lý như thế nào
- Thông báo hiển thị
- Dữ liệu có được lưu hay không
- Trạng thái giao diện thay đổi ra sao

| ❌ Không dùng | ✅ Dùng |
|---|---|
| Hiển thị đúng | Hệ thống hiển thị thông báo "Lưu dữ liệu thành công" và bản ghi xuất hiện trong danh sách. |

### 1.9. Quy ước đọc bảng đặc tả trường dữ liệu

Khi người yêu cầu cung cấp bảng đặc tả trường dữ liệu (dạng bảng "Tên trường — Loại — Giá trị mặc định — Bắt buộc — Enable/Disable — Quy tắc nhập" hoặc tương đương), áp dụng quy ước đọc sau để đảm bảo sinh đúng và đủ testcase, không cần hỏi lại:

**Cột "Loại" — ghi kèm giới hạn độ dài/giá trị trong ngoặc đơn:**

| Cách ghi trong cột "Loại" | Hiểu là | Sinh case tương ứng |
|---|---|---|
| `Textbox (1-255 ký tự)`, `Textbox (1~255 ký tự)`, `Textbox (1,255 ký tự)` | min-length = 1, max-length = 255 | Để trống (vì min=1 → required theo độ dài), nhập đúng 1 ký tự (biên dưới), nhập đúng 255 ký tự (biên trên), nhập 256 ký tự (vượt biên trên) — theo checklist Mục 5.1 |
| `Textbox (0-255 ký tự)` | min-length = 0 (cho phép rỗng theo độ dài), max-length = 255 | Tương tự trên, nhưng không sinh case "để trống → báo lỗi do thiếu ký tự tối thiểu" (việc bắt buộc hay không phụ thuộc cột "Bắt buộc" riêng, xem bên dưới) |
| `Number (0-999999)` | min-value = 0, max-value = 999999, ngầm định là số nguyên | Giá trị = 0 (biên dưới), giá trị = 999999 (biên trên), giá trị = -1 (dưới biên), giá trị = 1000000 (vượt biên) — theo checklist Mục 5.2 |
| `Number (0-999999, 2 chữ số thập phân)` | min/max như trên, cho phép số thập phân tối đa 2 chữ số sau dấu phẩy | Bổ sung thêm case: nhập số thập phân hợp lệ (2 chữ số), nhập quá 2 chữ số thập phân (kiểm tra có bị từ chối hoặc tự động làm tròn) |
| `DatePicker (>= ngày hiện tại)` | min = ngày hiện tại (mốc động, không phải hằng số cố định) | Chọn đúng ngày hiện tại (biên dưới động), chọn ngày trong quá khứ (dưới biên — phải báo lỗi), không cần test "biên trên" vì không giới hạn — theo checklist Mục 5.3 |
| `DatePicker (<= ngày hiện tại)` | max = ngày hiện tại (mốc động) | Tương tự, đảo chiều biên |

> Quy ước dấu phân tách khoảng giá trị: ba ký hiệu `-` (gạch ngang), `~` (dấu ngã), và `,` (dấu phẩy) đều được hiểu là **khoảng giá trị từ — đến** (ví dụ `1-255`, `1~255`, `1,255` đều nghĩa là min=1, max=255). Không cần đồng nhất một ký hiệu duy nhất trong toàn tài liệu; cả ba cách viết trên đều được nhận diện đúng. Nếu cột "Loại" dùng dấu `,` để phân tách khoảng giá trị, không nhầm với dấu `,` dùng để liệt kê (ví dụ trong `Select box (A, B, C)` thì đây là liệt kê danh sách option, không phải khoảng giá trị — phân biệt theo ngữ cảnh: hai số ngăn bởi `,` là khoảng, danh sách chữ/nhiều phần tử ngăn bởi `,` là liệt kê).

**Cột "Bắt buộc" (Có/Không):**
- `Có` → sinh thêm case "Để trống trường" thuộc nhóm validate required (Mục 5), tách biệt với case biên độ dài/giá trị (min-maxlength) — đây là 2 loại case khác nhau dù đôi khi trùng biểu hiện (ví dụ min-length=1 và bắt buộc=Có có thể cùng dẫn đến lỗi khi để trống, nhưng vẫn viết thành 2 testcase riêng vì kiểm tra 2 quy tắc khác nhau).
- `Không` → không sinh case "Để trống → báo lỗi"; thay vào đó sinh case "Để trống → vẫn lưu được, hiển thị đúng giá trị rỗng" (Mục 2 — trạng thái mặc định, và Mục 7 — lưu trữ dữ liệu).

**Cột "Giá trị mặc định":**
- `Điền sẵn ... hiện tại` (ví dụ "Điền sẵn mã hiện tại", "Điền sẵn tên hiện tại") → áp dụng cho màn hình Chỉnh sửa: sinh case kiểm tra trường hiển thị đúng giá trị đã lưu khi mở form (Mục 2.2), không sinh case "giá trị mặc định" cho màn hình Thêm mới trừ khi ghi rõ khác.
- Một giá trị cụ thể (ví dụ "Mặc định: Hoạt động") → sinh case kiểm tra đúng giá trị này khi mở màn hình Thêm mới (Mục 2.1).
- Để trống/không ghi → hiểu là không có giá trị mặc định, trường hiển thị rỗng khi Thêm mới.

**Cột "Enable/Disable":**
- `Disable` kết hợp với quy tắc nhập kiểu "Không cho phép chỉnh sửa ... sau khi tạo" → đây là Enable/Disable phụ thuộc **vào màn hình** (Thêm mới thì Enable, Chỉnh sửa thì Disable) — sinh case theo Mục 13.2 (Phụ thuộc theo trạng thái bản ghi), không phải Mục 9 (Phân quyền), trừ khi quy tắc nhập có nhắc rõ đến vai trò/quyền người dùng.
- Nếu quy tắc nhập có nhắc đến vai trò cụ thể (ví dụ "chỉ Admin được sửa") → sinh case theo Mục 9 (Phân quyền) thay vì Mục 13.

**Cột "Quy tắc nhập":**
- Đây là nguồn chính để sinh case thuộc Mục 8 (Kiểm tra quy tắc nghiệp vụ) khi nội dung mô tả mối quan hệ giữa nhiều trường hoặc điều kiện nghiệp vụ (ví dụ "Không được lớn hơn ngày hiện tại", "Phải thuộc kỳ kế toán đang mở").
- Khi nội dung chỉ mô tả ràng buộc nội tại của một trường đơn lẻ (ví dụ "Không cho phép để trống hoặc chỉ nhập khoảng trắng") → sinh case thuộc Mục 5 (Kiểm tra trường dữ liệu) của chính trường đó, không tách sang Mục 8.

### 1.10. Quản lý dữ liệu test (Test Data Management)

> Nhiều mục trong tài liệu này (đặc biệt Mục 27 — Cross-module, Mục 28 — Rollback/Undo, Mục 3.5, Mục 16) yêu cầu **tiền điều kiện phức tạp** — dữ liệu phải tồn tại sẵn ở đúng trạng thái, đúng module, trước khi bắt đầu test. Mục 1.10 quy định cách chuẩn bị dữ liệu test nhất quán, tránh mỗi testcase tự mô tả một kiểu.

**Nguyên tắc phân loại dữ liệu test**

| Loại | Đặc điểm | Cách chuẩn bị |
|---|---|---|
| **Dữ liệu tĩnh (Fixture)** | Không đổi giữa các lần chạy test, dùng chung cho nhiều testcase (ví dụ: danh mục chuẩn, cấu hình hệ thống) | Seed sẵn 1 lần trong môi trường test, không tạo lại mỗi lần test |
| **Dữ liệu động (Generated)** | Được tạo riêng cho từng testcase, không dùng chung để tránh test này ảnh hưởng test khác | Tạo mới trong bước Setup của từng testcase, đặt tên có định danh duy nhất (ví dụ gắn timestamp/random suffix) |
| **Dữ liệu biên (Edge case data)** | Dữ liệu được thiết kế riêng để test giá trị biên (chuỗi 255 ký tự, số âm, ngày quá khứ xa...) | Định nghĩa sẵn thành bộ dữ liệu chuẩn dùng lại được (data provider), không gõ tay lại mỗi lần |

**Nguyên tắc đặt tên dữ liệu test**
- Dữ liệu test phải **nhận diện được** là dữ liệu test, không lẫn với dữ liệu thật (ví dụ tiền tố `TEST_`, `AUTO_`, hoặc domain riêng `@test.example.com`)
- Dữ liệu tạo bởi automation nên có định danh duy nhất theo từng lần chạy để tránh xung đột khi chạy song song nhiều test (ví dụ suffix theo timestamp hoặc UUID)

**Nguyên tắc dọn dẹp (Cleanup)**
- Dữ liệu động phải được **dọn dẹp sau khi test xong** (xóa qua API), không để lại rác tích lũy qua nhiều lần chạy
- Nếu testcase thất bại giữa chừng (trước bước cleanup) — có cơ chế dọn dẹp định kỳ (ví dụ job xóa dữ liệu `TEST_*` cũ hơn N giờ) để môi trường test không phình to theo thời gian
- Dữ liệu tĩnh (Fixture) **không bị xóa** bởi cleanup của từng testcase — chỉ dữ liệu động mới bị dọn

**Nguyên tắc setup cho case phức tạp (Cross-module, State Transition, Rollback)**
- Với case cần dữ liệu ở nhiều module (Mục 27) — setup **qua API** của từng module liên quan, không setup qua UI (chậm và dễ lỗi vặt không liên quan đến mục tiêu test)
- Với case cần dữ liệu ở một trạng thái cụ thể giữa chuỗi trạng thái (Mục 25, ví dụ "bản ghi đang ở trạng thái Chờ duyệt") — ưu tiên tạo thẳng ở đúng trạng thái đó qua API/seed script, không nhất thiết phải đi qua toàn bộ luồng UI để đạt được trạng thái đó (trừ khi chính luồng đạt trạng thái đó là mục tiêu test)
- Với case cần dữ liệu lịch sử để test Rollback/Undo (Mục 28) — chuẩn bị sẵn chuỗi phiên bản dữ liệu (version history) qua script, không tạo bằng cách thực hiện tay nhiều lần sửa

**Môi trường test**
- Xác định rõ dữ liệu test chạy trên môi trường nào (local, staging, riêng biệt cho automation) — không chạy test tạo/xóa dữ liệu trên môi trường có dữ liệu thật
- Với case Time-based (Mục 28) — xem thêm lưu ý riêng tại Mục 28.11 về việc mock đồng hồ hệ thống thay vì phụ thuộc dữ liệu test theo thời gian thực

---

## 2. Kiểm tra trạng thái mặc định

### 2.1. Khi mở màn hình Thêm mới

- Các trường không bắt buộc mặc định hiển thị rỗng (trừ khi có yêu cầu khác)
- Các trường dạng Danh sách chọn hoặc Nút chọn đơn có giá trị mặc định nếu tài liệu yêu cầu
- Các trường bắt buộc hiển thị dấu *
- Placeholder hiển thị đúng
- Trường chỉ đọc hiển thị đúng trạng thái
- Trường bị khóa hiển thị đúng trạng thái
- Không giữ dữ liệu từ lần nhập trước (trừ khi có yêu cầu)

### 2.2. Khi mở màn hình Chỉnh sửa

- Hiển thị đúng dữ liệu đã lưu
- Trạng thái các trường đúng theo nghiệp vụ
- Các trường chỉ đọc hoặc bị khóa hiển thị đúng

**Ví dụ testcase:**

> **TC:** Mở form tạo mới
> **Kết quả mong muốn:**
> - Các trường không bắt buộc hiển thị rỗng
> - Các trường có giá trị mặc định hiển thị đúng theo cấu hình
> - Không tự động giữ dữ liệu từ phiên làm việc trước

---

## 3. Kiểm tra tính duy nhất

Áp dụng với các trường được định nghĩa là duy nhất (đơn lẻ hoặc tổ hợp nhiều trường).

> **Pattern câu hỏi tổng quát trước khi gen case:**
> - Tính duy nhất áp dụng cho **1 trường đơn lẻ** hay **tổ hợp nhiều trường** (composite unique)?
> - Phạm vi duy nhất là **toàn hệ thống** hay **trong một phạm vi con** (ví dụ mã sản phẩm chỉ cần duy nhất trong 1 cửa hàng, không cần duy nhất toàn hệ thống)?
> - Dữ liệu đã xóa mềm có tính vào kiểm tra trùng không?

### 3.1. Trường đơn lẻ — Luồng cơ bản
> **Pattern câu hỏi:** "Giá trị này có được phép trùng với bản ghi khác không, trong phạm vi nào?"

- Tạo mới với giá trị **chưa tồn tại** → thành công
- Tạo mới với giá trị **đã tồn tại** → bị chặn, thông báo rõ ràng
- Chỉnh sửa **giữ nguyên** giá trị cũ của chính bản ghi đó → thành công (không tự báo trùng với chính nó)
- Chỉnh sửa **thành giá trị đã tồn tại** ở bản ghi khác → bị chặn
- Chỉnh sửa **thành giá trị chưa tồn tại** → thành công

### 3.2. Trường đơn lẻ — Biến thể chuỗi (String Normalization)
> **Pattern câu hỏi:** "Hệ thống có coi các biến thể viết khác nhau của cùng 1 chuỗi là trùng nhau không?"

- Khoảng trắng **đầu chuỗi** (" ABC" vs "ABC") — hệ thống coi là trùng hay khác, đúng theo quy tắc chuẩn hóa
- Khoảng trắng **cuối chuỗi** ("ABC " vs "ABC") — tương tự
- Khoảng trắng **giữa các từ** ("A  B" hai khoảng trắng vs "A B" một khoảng trắng) — nếu nghiệp vụ chuẩn hóa nhiều khoảng trắng thành một
- Phân biệt **chữ hoa/chữ thường** ("ABC" vs "abc") — hệ thống coi là trùng hay khác, đúng theo quy tắc nghiệp vụ (case-sensitive hay case-insensitive)
- Ký tự có dấu vs không dấu tiếng Việt (nếu áp dụng) — có coi là trùng không

### 3.3. Tổ hợp nhiều trường (Composite Unique)
> **Pattern câu hỏi:** "Tính duy nhất có phụ thuộc vào sự kết hợp của nhiều trường, không chỉ 1 trường không?" (ví dụ: Mã nhân viên chỉ cần duy nhất trong phạm vi 1 chi nhánh, không cần duy nhất toàn công ty)

- Tổ hợp (A, B) **hoàn toàn trùng** với bản ghi khác → bị chặn
- Chỉ **A trùng, B khác** (hoặc ngược lại) → được phép tạo (vì tổ hợp khác nhau)
- Sửa một trong các trường của tổ hợp khiến **tổ hợp mới trùng** với bản ghi khác đã tồn tại → bị chặn
- Xác định đúng **phạm vi tính duy nhất** (ví dụ: theo chi nhánh, theo năm, theo loại danh mục) — dữ liệu ở phạm vi khác nhau được phép trùng giá trị

### 3.4. Tương tác với dữ liệu đã xóa mềm (Soft Delete)
> **Pattern câu hỏi:** "Dữ liệu đã xóa mềm có tính vào kiểm tra trùng lặp không?" — xem thêm Mục 10.3

- Tạo mới với giá trị **trùng với bản ghi đã xóa mềm** — hệ thống xử lý đúng theo nghiệp vụ: cho phép tạo lại (coi bản ghi cũ như không tồn tại), hoặc vẫn chặn (coi lịch sử vẫn tính)
- Khôi phục bản ghi đã xóa mềm khi giá trị unique của nó **đã bị bản ghi khác dùng** trong lúc nó bị xóa — hệ thống xử lý đúng (chặn khôi phục, hoặc yêu cầu đổi giá trị trước khi khôi phục)

### 3.5. Tương tác với luồng nghiệp vụ khác
> **Pattern câu hỏi:** "Việc kiểm tra trùng có thể bị ảnh hưởng bởi thao tác đồng thời hoặc thứ tự thao tác không?"

- Hai người dùng **cùng lúc** tạo bản ghi với cùng giá trị unique (race condition) — chỉ 1 bản ghi được tạo thành công, người còn lại nhận thông báo trùng, không có 2 bản ghi trùng nhau lọt qua (liên quan Mục 16)
- Import hàng loạt (nếu có — xem Mục 21) có dữ liệu trùng nhau **ngay trong file import** — hệ thống phát hiện và xử lý đúng, không chỉ kiểm tra trùng với DB mà bỏ qua trùng nội bộ trong file

**Ví dụ testcase:**

> **TC:** Nhập Email đã tồn tại
> **Kết quả mong muốn:**
> - Hiển thị thông báo "Email đã tồn tại trong hệ thống"
> - Không cho phép lưu dữ liệu

---

## 4. Kiểm tra Bộ lọc & Tìm kiếm

Áp dụng cho màn hình Danh sách có chức năng lọc dữ liệu (theo nhiều điều kiện) và/hoặc tìm kiếm theo từ khóa. Nếu màn hình Danh sách đủ phức tạp (nhiều điều kiện lọc), nên tách thành một mục cấp 1 riêng theo đúng cấu trúc tại Mục 1.2, với đầy đủ các sub-mục dưới đây.

### 4.1. Từng điều kiện lọc riêng lẻ
- Áp dụng một điều kiện lọc hợp lệ — danh sách trả về đúng kết quả khớp điều kiện
- Áp dụng điều kiện lọc không có dữ liệu khớp — danh sách hiển thị trạng thái rỗng kèm thông báo phù hợp, không báo lỗi hệ thống
- Bỏ trống điều kiện lọc (không chọn) — danh sách hiển thị toàn bộ dữ liệu theo mặc định, không bị lọc nhầm
- Điều kiện lọc dạng khoảng (khoảng ngày, khoảng số) — lọc đúng tại biên (bằng giá trị đầu/cuối khoảng), lọc đúng khi khoảng rỗng hoặc khoảng không hợp lệ (giá trị đầu lớn hơn giá trị cuối)
- Điều kiện lọc dạng nhập tay (ô nhập liệu lọc theo mã, theo tên...) — áp dụng đầy đủ checklist liên quan tại Mục 5.1 (khoảng trắng, ký tự đặc biệt, chữ hoa/thường) trong ngữ cảnh lọc dữ liệu

### 4.2. Kết hợp nhiều điều kiện lọc đồng thời
- Áp dụng đồng thời 2 điều kiện lọc trở lên — kết quả trả về đúng giao (AND) của tất cả điều kiện đã chọn, không phải hợp (OR) trừ khi nghiệp vụ yêu cầu khác
- Kết hợp nhiều điều kiện mà không có bản ghi nào thỏa tất cả — danh sách hiển thị trạng thái rỗng đúng cách
- Thay đổi một điều kiện lọc trong khi các điều kiện khác đã được áp dụng từ trước — kết quả cập nhật đúng theo tổ hợp mới, không giữ lại kết quả của tổ hợp cũ
- Áp dụng đồng thời điều kiện lọc và ô tìm kiếm theo từ khóa (nếu màn hình có cả hai) — kết quả trả về đúng giao của bộ lọc và từ khóa tìm kiếm
- Tổ hợp điều kiện lọc có quan hệ phụ thuộc nhau (ví dụ chọn "Tỉnh/Thành" trước thì danh sách "Quận/Huyện" lọc theo đúng tỉnh đã chọn) — hoạt động đúng theo quy tắc phụ thuộc

### 4.3. Xóa và đặt lại điều kiện lọc (Reset)
- Xóa một điều kiện lọc cụ thể (giữ nguyên các điều kiện khác) — danh sách cập nhật đúng theo các điều kiện còn lại
- Bấm "Đặt lại" (Reset/Clear all) — toàn bộ điều kiện lọc và từ khóa tìm kiếm được xóa, danh sách trở về trạng thái mặc định ban đầu
- Đóng/mở lại khu vực bộ lọc (nếu bộ lọc ở dạng thu gọn/mở rộng) — các điều kiện đã chọn trước đó vẫn được giữ nguyên, không bị mất

### 4.4. Tìm kiếm theo từ khóa
- Tìm kiếm với từ khóa khớp chính xác — trả về đúng kết quả
- Tìm kiếm với từ khóa khớp gần đúng/một phần (nếu nghiệp vụ hỗ trợ):
  - Từ khóa là chuỗi con ở đầu — trả về đúng kết quả (ví dụ "xe" → "xe máy", "xe đạp")
  - Từ khóa là chuỗi con ở giữa — kiểm tra hệ thống có tìm được không (ví dụ "may" → "xe máy")
  - Từ khóa thiếu dấu tiếng Việt (ví dụ "xe may" thay vì "xe máy") — hành vi đúng theo nghiệp vụ (có hỗ trợ tìm không dấu không?)
  - Từ khóa quá ngắn (1–2 ký tự) — hệ thống xử lý đúng (tìm kiếm, yêu cầu nhập thêm, hoặc bỏ qua)
- Tìm kiếm không phân biệt chữ hoa/chữ thường (nếu nghiệp vụ yêu cầu) — trả về đúng kết quả dù từ khóa viết hoa/thường khác nhau
- Tìm kiếm với từ khóa có khoảng trắng đầu/cuối — hệ thống tự loại bỏ khoảng trắng dư và tìm đúng kết quả
- Tìm kiếm với từ khóa không tồn tại trong dữ liệu — hiển thị trạng thái rỗng kèm thông báo phù hợp
- Tìm kiếm với từ khóa chứa ký tự đặc biệt hoặc chuỗi SQL Injection/XSS — hệ thống xử lý an toàn, không gây lỗi hệ thống, không thực thi mã độc
- Xóa từ khóa tìm kiếm (bằng nút X hoặc xóa tay) — danh sách trở về đúng trạng thái trước khi tìm kiếm (toàn bộ dữ liệu, hoặc đúng theo các điều kiện lọc khác đang áp dụng)

### 4.5. Tương tác giữa Bộ lọc/Tìm kiếm với Phân trang và Sắp xếp
- Áp dụng bộ lọc/tìm kiếm khi đang ở trang khác trang 1 — hệ thống tự động đưa về trang 1 của kết quả mới, không giữ nguyên số trang cũ (trừ khi nghiệp vụ yêu cầu khác)
- Tổng số trang và tổng số bản ghi hiển thị cập nhật đúng theo kết quả đã lọc/tìm kiếm, không tính theo tổng dữ liệu gốc
- Thứ tự sắp xếp (sort) đã chọn trước đó vẫn được giữ nguyên và áp dụng đúng trên kết quả đã lọc/tìm kiếm
- Sắp xếp lại dữ liệu trong khi bộ lọc/tìm kiếm đang áp dụng — kết quả sắp xếp đúng trong phạm vi dữ liệu đã lọc, không sắp xếp lại toàn bộ dữ liệu gốc

### 4.6. Lưu trạng thái bộ lọc
- Tải lại trang (refresh/F5) sau khi đã áp dụng bộ lọc/tìm kiếm — hệ thống xử lý đúng theo nghiệp vụ quy định (giữ lại điều kiện đã áp dụng, hoặc đặt lại về mặc định)
- Điều hướng sang màn hình khác rồi quay lại màn hình Danh sách — điều kiện lọc/tìm kiếm đã áp dụng trước đó còn được giữ hoặc bị xóa đúng theo nghiệp vụ quy định
- Mở chi tiết một bản ghi từ kết quả đã lọc, sau đó quay lại danh sách — vẫn đang ở đúng kết quả đã lọc trước đó, không bị reset về danh sách gốc

### 4.7. Hiển thị kết quả tìm kiếm (nếu có highlight)

> Áp dụng khi hệ thống có chức năng highlight (bôi đậm/đánh dấu) từ khóa trong kết quả tìm kiếm. Nếu không có → bỏ qua mục này.

- Từ khóa tìm kiếm được highlight đúng vị trí trong kết quả (bôi đậm, màu khác, hoặc theo thiết kế)
- Highlight xuất hiện đúng trên tất cả các trường được tìm kiếm, không chỉ trường đầu tiên
- Khi xóa từ khóa — highlight biến mất, văn bản trở về định dạng bình thường
- Highlight không làm sai nội dung văn bản gốc (không thêm/bớt ký tự, không lỗi encode)
- Từ khóa khớp nhiều lần trong cùng một ô — tất cả vị trí đều được highlight, không chỉ lần đầu

### 4.8. Hiệu năng tìm kiếm (mức kiểm thử thủ công)

> Không phải load test — đây là kiểm tra cảm nhận tốc độ phản hồi bằng tay trong điều kiện dữ liệu thực tế.

- Gõ từ khóa trong danh sách có nhiều bản ghi (≥ 100 bản ghi hoặc theo mức dữ liệu thực tế) — kết quả trả về trong thời gian chấp nhận được (không bị đơ/treo giao diện)
- Trong lúc đang tìm kiếm — hiển thị indicator loading/spinner rõ ràng, danh sách không nhảy loạn hoặc hiển thị nháy
- Gõ nhanh liên tiếp nhiều ký tự (type-ahead) — hệ thống không gửi quá nhiều request song song gây kết quả hiển thị sai thứ tự (debounce hoạt động đúng)
- Kết quả tìm kiếm với dữ liệu lớn — phân trang vẫn hoạt động đúng, không bị thiếu bản ghi hoặc lặp bản ghi giữa các trang

---

## 5. Kiểm tra trường dữ liệu

### 5.1. Ô nhập liệu

- Để trống
- Nhập giá trị hợp lệ
- Độ dài tối thiểu
- Độ dài tối đa
- Vượt quá độ dài tối đa
- Khoảng trắng đầu chuỗi
- Khoảng trắng cuối chuỗi
- Chỉ nhập khoảng trắng
- Nhiều khoảng trắng liên tiếp
- Chỉ nhập chữ
- Chỉ nhập số
- Chữ và số
- Ký tự đặc biệt
- Tiếng Việt có dấu
- Copy/Paste dữ liệu
- Chuỗi SQL Injection
- Chuỗi XSS
- Dữ liệu trùng lặp (nếu có)
- Lưu và tải lại dữ liệu

### 5.2. Trường số

- Để trống
- Số nguyên hợp lệ
- Số thập phân hợp lệ
- Giá trị bằng 0
- Giá trị âm
- Giá trị dương
- Giá trị nhỏ nhất
- Giá trị lớn nhất
- Nhỏ hơn giá trị tối thiểu
- Lớn hơn giá trị tối đa
- Nhập chữ/ký tự chữ cái — xác nhận rõ hành vi UI theo 1 trong 2 kiểu (phải nhất quán, không lẫn lộn giữa các màn hình):
  - **Chặn ngay tại bàn phím**: bàn phím hiện đúng loại numeric-only (không có phím chữ), hoặc ký tự chữ gõ vào bị từ chối ngay lập tức, ô nhập không đổi giá trị
  - **Cho nhập rồi validate khi submit**: ký tự chữ vẫn gõ được vào ô, nhưng khi rời khỏi field/submit thì hiển thị đúng thông báo lỗi rõ ràng ("Chỉ được nhập số"), không cho lưu
- Nhập ký tự đặc biệt (`+`, `-`, `.`, `,`, `e`, khoảng trắng, emoji) — với mỗi ký tự, xác nhận rõ được chấp nhận (ví dụ dấu `.`/`,` cho số thập phân, dấu `-` cho số âm nếu hợp lệ) hay bị từ chối, không mặc định đối xử tất cả ký tự đặc biệt giống nhau
- Nhập nhiều dấu thập phân trong 1 giá trị (ví dụ `1.2.3`) — bị chặn hoặc báo lỗi rõ ràng, không tạo ra giá trị số không hợp lệ được lưu
- Copy/paste giá trị có lẫn ký tự chữ hoặc khoảng trắng vào field số (ví dụ paste "1,234 VNĐ" khi chỉ cần "1234") — xử lý đúng: tự động lọc bỏ ký tự không hợp lệ, hoặc từ chối toàn bộ và báo lỗi rõ ràng — không được âm thầm cắt cụt gây sai giá trị (ví dụ chỉ giữ lại "1" từ "1,234 VNĐ")
- Lưu và tải lại dữ liệu

### 5.3. Chọn ngày

**Dữ liệu cơ bản**
- Để trống
- Chọn ngày hợp lệ
- Nhập tay ngày hợp lệ
- Sai định dạng
- Sai dấu phân cách
- Nhập chữ
- Nhập ký tự đặc biệt

**Ngày không tồn tại**
- 31/02
- 30/02
- 32/01

**Năm nhuận**
- 29/02 năm nhuận
- 29/02 năm không nhuận

**Giá trị biên**
- Ngày tối thiểu
- Ngày tối đa
- Trước ngày tối thiểu
- Sau ngày tối đa

**Nghiệp vụ ngày**
- Ngày hiện tại
- Ngày trong quá khứ
- Ngày trong tương lai

**Giao diện**
- Mở lịch
- Chuyển tháng
- Chuyển năm

**Lưu trữ dữ liệu**
- Lưu thành công
- Tải lại hiển thị đúng

### 5.4. Danh sách chọn

**Cơ bản**
- Giá trị mặc định
- Không chọn giá trị
- Chọn giá trị hợp lệ
- Chọn phần tử đầu tiên
- Chọn phần tử cuối cùng

**Xóa dữ liệu**
- Xóa bằng nút X
- Xóa giá trị của trường bắt buộc
- Xóa giá trị của trường không bắt buộc
- Xóa rồi chọn lại

**Tìm kiếm**
- Tìm chính xác
- Tìm gần đúng
- Không có kết quả

**Chọn nhiều giá trị**
- Chọn nhiều giá trị
- Xóa một giá trị đã chọn
- Xóa nhiều giá trị đã chọn
- Xóa tất cả
- Chọn lại giá trị đã xóa

**Lưu dữ liệu**
- Lưu
- Tải lại
- Chỉnh sửa

### 5.5. Hộp kiểm

- Được chọn
- Không được chọn
- Trạng thái mặc định
- Chuyển đổi nhiều lần
- Lưu dữ liệu khi được chọn
- Lưu dữ liệu khi không được chọn
- Kiểm tra ảnh hưởng đến các trường phụ thuộc

### 5.6. Nút chọn đơn

- Giá trị mặc định
- Thay đổi lựa chọn
- Chỉ được chọn một giá trị
- Lưu và tải lại dữ liệu

### 5.7. Ô nhập liệu nhiều dòng

Ngoài checklist của Ô nhập liệu (4.1), bắt buộc cover thêm:

- Xuống dòng
- Nội dung nhiều dòng
- Nội dung rất dài
- Copy/Paste đoạn văn bản dài

### 5.8. Tra cứu dữ liệu

- Tìm dữ liệu hợp lệ
- Tìm dữ liệu không tồn tại
- Chọn dữ liệu
- Xóa dữ liệu đã chọn
- Không có dữ liệu trả về
- API timeout
- API lỗi
- Lưu và tải lại dữ liệu

### 5.9. Tải tệp

- Tải lên đúng định dạng
- Tải lên sai định dạng
- Tải lên vượt dung lượng cho phép
- Tải lên nhiều tệp
- Xóa tệp đã tải lên
- Tải tệp xuống
- Thay thế tệp
- Tải lại màn hình và kiểm tra dữ liệu

### 5.10. Tra cứu dữ liệu dạng cây (Tree Select)

- Hiển thị đúng cấu trúc cây (cha - con) theo dữ liệu nguồn
- Mở rộng (expand) một nhánh
- Thu gọn (collapse) một nhánh
- Mở rộng/thu gọn tất cả
- Chọn một node lá (không có node con)
- Chọn một node cha — kiểm tra có tự động chọn tất cả node con hay không (theo nghiệp vụ)
- Bỏ chọn một node con — kiểm tra trạng thái node cha có chuyển thành "chọn một phần" (indeterminate) hay không
- Chọn nhiều node ở các nhánh khác nhau
- Tìm kiếm node theo từ khóa — cây tự động mở rộng đến node khớp kết quả
- Tìm kiếm không có kết quả
- Xóa giá trị đã chọn (xóa từng node / xóa tất cả)
- Cây dữ liệu rỗng (không có node nào)
- Cây dữ liệu nhiều cấp (từ 3 cấp trở lên) hiển thị đúng thụt lề (indent) từng cấp
- Cây dữ liệu lớn (nhiều node) — kiểm tra hiệu năng load và cuộn (scroll)
- Lưu giá trị đã chọn và tải lại — hiển thị đúng trạng thái cây đã chọn trước đó
- Chỉnh sửa: mở lại màn hình hiển thị đúng các node đã được chọn trước đó

### 5.11. Lưu ý: "Kiểm tra dữ liệu" không thuộc nhóm này

> "Kiểm tra dữ liệu" (Data-level) là một **nhóm kiểm thử bắt buộc riêng**, không phải sub-mục của "Kiểm tra trường dữ liệu". Xem định nghĩa, ranh giới và checklist chi tiết tại **Mục 1.6**.

---

## 6. Kiểm tra hành vi sau khi thao tác thành công (Post-action Behavior)

> Áp dụng sau khi đã nhập/chọn đầy đủ dữ liệu hợp lệ (đã đi qua hết checklist tại Mục 5) và thực hiện hành động Thêm mới, Chỉnh sửa, hoặc Xóa. Mục này tập trung vào **những gì xảy ra trên giao diện ngay sau khi hành động thành công** (thông báo, trạng thái form, cập nhật danh sách, điều hướng) — khác với Mục 5 (vốn tập trung vào validate dữ liệu đầu vào trước khi lưu) và khác với Mục 7 — Kiểm tra lưu trữ dữ liệu (vốn tập trung vào tính đúng đắn của dữ liệu sau khi lưu vào hệ thống/CSDL — ví dụ: dữ liệu tải lại có khớp với dữ liệu đã nhập không).

### 6.1. Thông báo kết quả thành công
- Thông báo "Thêm mới thành công" hiển thị đúng nội dung, đúng vị trí (toast/banner/inline) ngay sau khi Lưu
- Thông báo "Cập nhật/Chỉnh sửa thành công" hiển thị đúng nội dung, đúng vị trí ngay sau khi Lưu
- Thông báo "Xóa thành công" hiển thị đúng nội dung, đúng vị trí ngay sau khi xác nhận xóa
- Thông báo tự động ẩn sau khoảng thời gian quy định (nếu là dạng toast tự ẩn), hoặc có nút đóng rõ ràng (nếu là dạng banner/inline)
- Xóa/thêm/sửa hàng loạt nhiều bản ghi — thông báo hiển thị đúng số lượng bản ghi đã xử lý thành công (ví dụ "Đã xóa 5 bản ghi")

### 6.2. Trạng thái form sau khi Lưu
- Sau khi Thêm mới thành công — form xử lý đúng theo thiết kế: đóng dialog/đóng trang và quay về danh sách, hoặc reset trắng để tiếp tục nhập bản ghi mới, hoặc chuyển sang chế độ xem/chỉnh sửa bản ghi vừa tạo (tùy nghiệp vụ)
- Sau khi Chỉnh sửa thành công — form xử lý đúng theo thiết kế: đóng dialog/đóng trang và quay về danh sách, hoặc giữ lại form hiển thị đúng dữ liệu mới đã lưu (không hiển thị dữ liệu cũ trước khi sửa)
- Nút Lưu/Gửi trở lại đúng trạng thái sau khi xử lý xong (không bị kẹt ở trạng thái loading/disable)

### 6.3. Cập nhật danh sách sau hành động
- Bản ghi vừa Thêm mới xuất hiện đúng trong danh sách mà không cần tải lại trang (F5) thủ công, đúng vị trí theo thứ tự sắp xếp hiện tại (ví dụ: lên đầu nếu sort theo ngày tạo giảm dần)
- Bản ghi vừa Chỉnh sửa hiển thị đúng dữ liệu mới trong danh sách, không cần tải lại trang
- Bản ghi vừa Xóa biến mất khỏi danh sách ngay, không cần tải lại trang
- Tổng số bản ghi hiển thị (đếm/phân trang) cập nhật đúng ngay sau khi Thêm mới hoặc Xóa
- Xóa bản ghi cuối cùng của trang hiện tại (khi đang ở trang khác trang 1) — hệ thống tự điều chỉnh về trang hợp lệ gần nhất, không hiển thị trang rỗng
- Bản ghi vừa Thêm mới/Chỉnh sửa vẫn xuất hiện đúng vị trí phù hợp nếu đang áp dụng bộ lọc/tìm kiếm (xem thêm Mục 4) — không bị ẩn đi do tác động ngoài ý muốn của bộ lọc đang áp dụng

### 6.4. Điều hướng sau hành động
- Sau khi thao tác thành công, người dùng được đưa về đúng màn hình kỳ vọng theo thiết kế (ở lại trang hiện tại, quay về danh sách, hoặc chuyển sang trang chi tiết của bản ghi vừa tạo/sửa)
- Trạng thái trang đang xem trước khi thao tác (số trang, điều kiện lọc, từ khóa tìm kiếm, thứ tự sắp xếp) được giữ nguyên sau khi quay lại danh sách, không bị reset về mặc định ngoài ý muốn
- Nếu thao tác được thực hiện từ một màn hình khác (ví dụ thêm nhanh từ popup trong màn hình khác), sau khi thành công người dùng được đưa về đúng vị trí/ngữ cảnh ban đầu, không bị điều hướng nhầm sang màn hình không liên quan

### 6.5. Hành vi khi thao tác thất bại (Negative Post-action)

> Phân biệt với Mục 15 (xử lý lỗi hệ thống — mất mạng, server 500): Mục 6.5 tập trung vào lỗi **nghiệp vụ** trả về sau khi submit (validate phía server, ràng buộc dữ liệu, điều kiện không thỏa) — loại lỗi phổ biến nhất trong thực tế nhưng hay bị bỏ sót.

**Khi Lưu/Submit thất bại do lỗi nghiệp vụ:**
- Form giữ nguyên toàn bộ dữ liệu người dùng đã nhập, không bị xóa trắng khi server trả lỗi
- Thông báo lỗi hiển thị đúng vị trí (inline dưới field vi phạm, hoặc banner trên cùng form), nội dung mô tả rõ lỗi gì
- Nếu có nhiều lỗi cùng lúc — tất cả lỗi đều được hiển thị, không chỉ lỗi đầu tiên
- Nút Lưu/Gửi trở lại trạng thái enable sau khi server trả lỗi, người dùng có thể sửa và thử lại mà không cần tải lại trang
- Lỗi server-side trả về field nào — đúng field đó được highlight/đánh dấu trên giao diện (validate 2 lớp client + server khớp nhau)

**Khi Xóa thất bại do ràng buộc nghiệp vụ:**
- Popup xác nhận xóa đóng lại hay vẫn còn mở — đúng theo thiết kế
- Thông báo lý do bị chặn hiển thị rõ ràng (ví dụ "Không thể xóa vì đang được tham chiếu bởi N bản ghi khác")
- Danh sách không thay đổi — bản ghi vẫn còn nguyên, không bị xóa một phần
- Người dùng có thể thực hiện hành động khác sau khi xóa thất bại, không bị kẹt giao diện

**Khi thao tác thất bại do hết session giữa chừng:**
- Người dùng nhận thông báo rõ ràng (không im lặng mất dữ liệu)
- Dữ liệu đã nhập được bảo toàn tối đa hoặc có hướng dẫn tiếp theo — xem thêm Mục 16.2

### 6.6. Hành vi theo từng điểm vào (Entry Point)

> Cùng một hành động (Thêm mới/Sửa/Xóa) nhưng được thực hiện từ các nơi khác nhau — kết quả redirect và trạng thái sau đó phải đúng ngữ cảnh của từng nơi, không áp dụng chung một hành vi.

Khi phân tích chức năng, đặt câu hỏi: **"Người dùng có thể thực hiện hành động này từ bao nhiêu nơi?"** rồi sinh case cho từng nơi:

| Entry point phổ biến | Kết quả redirect kỳ vọng sau thành công |
|---|---|
| Từ màn hình Danh sách chính (nút Thêm mới trên toolbar) | Quay về Danh sách, bản ghi mới xuất hiện đúng vị trí |
| Từ popup/modal trong màn hình khác | Đóng popup, quay về màn hình cha, dữ liệu liên quan cập nhật nếu cần |
| Từ màn hình Chi tiết (nút Sửa inline) | Ở lại màn hình Chi tiết, hiển thị dữ liệu mới vừa sửa |
| Từ Breadcrumb / Deep link trực tiếp | Quay về đúng màn hình context trước đó, không về trang chủ |
| Từ danh sách đang có bộ lọc/tìm kiếm | Quay về danh sách, bộ lọc vẫn còn, bản ghi mới xuất hiện (hoặc ẩn nếu không thỏa điều kiện lọc — đúng theo nghiệp vụ) |
| Từ màn hình trên mobile (nếu áp dụng) | Back button về đúng màn hình trước, không bị stack navigation |

> Không cần sinh case cho tất cả entry point mọi lúc — chỉ sinh case cho các entry point **thực sự tồn tại** trong chức năng đang test (đọc từ SRS/wireframe). Dùng bảng trên như checklist đối chiếu.

---

## 7. Kiểm tra lưu trữ dữ liệu

> Khác với Mục 6 (tập trung vào hành vi *giao diện* ngay sau khi thao tác thành công), mục này tập trung vào tính đúng đắn của *dữ liệu thực tế* sau khi đã lưu vào hệ thống/CSDL — kiểm tra bằng cách tải lại, mở lại, hoặc xem từ một nơi khác.

### 7.1. Tính đúng đắn của dữ liệu sau khi lưu
- Tải lại trang (F5) ngay sau khi lưu — dữ liệu hiển thị đúng khớp 100% với dữ liệu đã nhập, không bị sai lệch
- Đóng và mở lại màn hình chi tiết/chỉnh sửa của bản ghi vừa lưu — dữ liệu hiển thị đúng từng trường, không thiếu, không lẫn dữ liệu của bản ghi khác
- Dữ liệu dạng số/ngày/tiền tệ được lưu và hiển thị lại đúng định dạng, đúng giá trị (không bị làm tròn sai, không bị lệch múi giờ, không bị đổi dấu thập phân ngoài ý muốn)
- Dữ liệu dạng chuỗi có ký tự đặc biệt, tiếng Việt có dấu, khoảng trắng — được lưu và hiển thị lại đúng nguyên vẹn, không bị lỗi encode (ô vuông, dấu hỏi, ký tự lạ)
- Dữ liệu dạng danh sách chọn/nhiều giá trị — được lưu và hiển thị lại đúng đầy đủ các giá trị đã chọn, đúng thứ tự nếu nghiệp vụ yêu cầu giữ thứ tự
- Trường không bắt buộc được để trống khi nhập — sau khi lưu và tải lại vẫn hiển thị đúng là rỗng, không tự sinh ra giá trị mặc định ngoài ý muốn

### 7.2. Tính nhất quán dữ liệu giữa các nơi hiển thị
- Dữ liệu vừa lưu hiển thị đúng và giống nhau ở mọi nơi có tham chiếu đến bản ghi đó (màn hình danh sách, màn hình chi tiết, các màn hình/báo cáo khác có liên kết tới bản ghi)
- Sau khi Chỉnh sửa, dữ liệu cũ không còn xuất hiện ở bất kỳ nơi nào đang hiển thị bản ghi đó (không bị cache hiển thị dữ liệu cũ)
- Mở đồng thời bản ghi đó trên nhiều tab/thiết bị sau khi đã lưu — tất cả đều hiển thị đúng dữ liệu mới nhất khi tải lại

### 7.3. Toàn vẹn dữ liệu khi lưu nhiều trường/nhiều bảng liên quan
- Lưu một bản ghi có dữ liệu liên quan đến nhiều bảng/nhiều entity (ví dụ thông tin chính và danh sách chi tiết con) — tất cả các phần đều được lưu đầy đủ, không bị thiếu phần con khi phần chính đã lưu thành công hoặc ngược lại
- Lưu thất bại ở một phần dữ liệu liên quan — toàn bộ giao dịch lưu được hủy đúng theo nguyên tắc toàn vẹn (all-or-nothing), không để lại dữ liệu lưu một phần gây sai lệch
- Xóa một bản ghi có dữ liệu liên quan ở nhiều bảng — dữ liệu liên quan được xử lý đúng theo nghiệp vụ (xóa theo, hoặc giữ lại có đánh dấu, tùy thiết kế), không để lại dữ liệu "mồ côi"

---

## 8. Kiểm tra quy tắc nghiệp vụ

Bắt buộc cover. Với mỗi bullet dưới đây, đặt **pattern câu hỏi** tương ứng khi đọc SRS để nhận diện và sinh đúng case — không bỏ sót do chỉ đọc qua:

### 8.1. Kiểm tra giữa nhiều trường dữ liệu
> **Pattern câu hỏi:** "Trường A và trường B có ràng buộc với nhau không?"

- Trường A và B có ràng buộc **thứ tự/so sánh** (A < B, A ≤ B, A phải trước B về ngày) → sinh case: hợp lệ (A < B), vi phạm (A > B), bằng nhau (A = B nếu không được phép)
- Trường A và B có ràng buộc **tổng/tỷ lệ** (A + B ≤ 100%, tổng không vượt ngưỡng) → sinh case: đúng ngưỡng, vượt ngưỡng, bằng đúng ngưỡng (biên)
- Trường A có ảnh hưởng đến **giá trị hợp lệ** của trường B (chọn A thì B chỉ được chọn trong tập con) → sinh case: chọn A hợp lệ rồi chọn B hợp lệ; chọn A rồi chọn B vi phạm
- **Thay đổi A sau khi đã nhập B** → B có bị reset, cảnh báo, hay giữ nguyên? → sinh case theo đúng hành vi nghiệp vụ

### 8.2. Kiểm tra phụ thuộc dữ liệu
> **Pattern câu hỏi:** "Trường/chức năng này có phụ thuộc vào dữ liệu đã tồn tại ở nơi khác không?"

- Dữ liệu phụ thuộc **tồn tại và hợp lệ** → chức năng hoạt động đúng
- Dữ liệu phụ thuộc **không tồn tại** → hệ thống báo lỗi rõ, không crash
- Dữ liệu phụ thuộc **tồn tại nhưng ở trạng thái không hợp lệ** (vô hiệu, đang xử lý, bị khóa) → hệ thống nhận diện đúng, không nhầm với "không tồn tại"
- Dữ liệu phụ thuộc bị **xóa/vô hiệu sau khi** đã tham chiếu → xem thêm Mục 27.2 và 27.3

### 8.3. Kiểm tra bắt buộc có điều kiện (Conditional Required)
> **Pattern câu hỏi:** "Trường X có trở thành bắt buộc khi [điều kiện Y] xảy ra không?"

- Khi điều kiện Y **chưa thỏa** → trường X không bắt buộc, có thể để trống và lưu thành công
- Khi điều kiện Y **thỏa** → trường X trở thành bắt buộc, để trống phải báo lỗi đúng
- **Thay đổi điều kiện Y sau khi đã nhập X** → trường X còn bắt buộc không? Giá trị X còn hợp lệ không?
- UI phản ánh đúng trạng thái bắt buộc/không bắt buộc theo điều kiện (dấu *, label thay đổi)

### 8.4. Kiểm tra luồng nghiệp vụ (Business Flow)
> **Pattern câu hỏi:** "Nghiệp vụ này có nhiều bước phải thực hiện theo thứ tự không?"

- Thực hiện đúng thứ tự các bước → kết quả đúng theo nghiệp vụ
- **Bỏ qua một bước** giữa chừng → hệ thống chặn hoặc cảnh báo, không cho phép tiếp tục
- **Quay lại bước trước** sau khi đã làm bước sau → dữ liệu xử lý đúng (không bị lỗi trạng thái)
- Thực hiện lại cùng một bước **2 lần** (double action) → hệ thống xử lý idempotent, không tạo dữ liệu trùng

### 8.5. Kiểm tra trạng thái (Status/State)
> **Pattern câu hỏi:** "Bản ghi này có thể ở những trạng thái nào? Từ trạng thái A có thể chuyển sang trạng thái nào?"

- Vẽ (trong đầu hoặc trên giấy) **sơ đồ trạng thái**: mỗi cạnh là một chuyển đổi hợp lệ
- **Chuyển đổi hợp lệ** (A → B theo nghiệp vụ) → thực hiện được, trạng thái cập nhật đúng
- **Chuyển đổi không hợp lệ** (A → C khi nghiệp vụ không cho phép) → hệ thống chặn và thông báo rõ
- Mỗi trạng thái có **hành động nào được phép/bị cấm** → sinh case kiểm tra từng hành động ở từng trạng thái
- Trạng thái hiển thị **nhất quán** ở mọi nơi có tham chiếu bản ghi đó
- Xem thêm Mục 25 nếu trạng thái có thể bị thay đổi từ module khác hoặc theo thứ tự thao tác phi logic

### 8.6. Kiểm tra nhật ký hệ thống (Audit Log)
> **Pattern câu hỏi:** "Hành động này có cần ghi log không? Log phải ghi những gì?"

- Hành động được thực hiện thành công → log ghi đầy đủ: **ai làm, làm gì, lúc nào, trên dữ liệu nào**
- Log ghi **giá trị trước và sau** khi thay đổi (với hành động sửa)
- Hành động bị **từ chối/thất bại** → log có ghi nhận không (tùy nghiệp vụ)
- Log **không thể bị sửa/xóa** bởi người dùng thông thường
- Tra cứu log theo các tiêu chí (người dùng, thời gian, loại hành động) trả về đúng kết quả

### 8.7. Kiểm tra tích hợp dữ liệu (điều kiện kích hoạt)
> Giới hạn ở việc kiểm tra **điều kiện/trạng thái nghiệp vụ nào kích hoạt** việc dữ liệu được chia sẻ, công khai, hoặc gửi sang module/hệ thống khác. Checklist chi tiết hành vi đồng bộ xem tại **Mục 12.5**, và luồng tích hợp xuyên module xem tại **Mục 27**.

- Bản ghi **chưa đạt** điều kiện kích hoạt → không được chia sẻ/gửi đi
- Bản ghi **vừa đạt** điều kiện kích hoạt → được chia sẻ/gửi đúng thời điểm, đúng nội dung
- **Thu hồi** điều kiện kích hoạt sau khi đã chia sẻ → xử lý đúng theo nghiệp vụ

### 8.8. Kiểm tra chuyển đổi trạng thái và thứ tự thao tác phi logic
> Xem **Mục 25** để biết checklist đầy đủ. Đặc biệt chú ý khi nghiệp vụ có các từ khóa: "chỉ được phép khi...", "sau khi được gán...", "không được thực hiện khi đang ở trạng thái...", "người dùng thực hiện A trước rồi mới bị áp điều kiện B".

**Ví dụ minh họa pattern câu hỏi áp dụng — Nếu chức năng là "Ngày tác động":**

| Pattern câu hỏi | Case sinh ra |
|---|---|
| A và B có ràng buộc thứ tự không? | Ngày tác động không được lớn hơn ngày hiện tại; không được nhỏ hơn ngày tạo giao dịch |
| Phụ thuộc vào dữ liệu khác? | Ngày tác động phải thuộc kỳ kế toán đang mở |
| Trạng thái bản ghi ảnh hưởng đến hành động? | Không được chỉnh sửa khi chứng từ đã được duyệt |
| Có thể thao tác theo thứ tự khác? | Nhập ngày tác động trước khi kỳ kế toán được mở → xử lý thế nào? |

---

## 9. Kiểm tra phân quyền

Bắt buộc cover theo từng vai trò (role) được định nghĩa trong tài liệu nghiệp vụ.

> **Pattern câu hỏi tổng quát trước khi gen case:**
> - Hệ thống có bao nhiêu vai trò? Vai trò nào được phép làm gì?
> - Có hành động nào chỉ 1 số vai trò nhất định được làm không?
> - Cùng một bản ghi, các vai trò khác nhau có nhìn thấy thông tin khác nhau không? (→ 9.6)
> - Quyền có thể thay đổi trong khi đang sử dụng không? (→ 9.5)

### 9.1. Quyền truy cập màn hình
- Vai trò có quyền truy cập màn hình — hiển thị đầy đủ chức năng
- Vai trò không có quyền truy cập màn hình — bị chặn truy cập hoặc ẩn menu
- Truy cập trực tiếp bằng URL khi không có quyền — hệ thống chặn và hiển thị thông báo phù hợp (không lộ dữ liệu)
- **Bypass qua API** khi không có quyền (gọi trực tiếp endpoint) → bị từ chối 403, không trả về dữ liệu

### 9.2. Quyền theo hành động (CRUD)
> **Pattern câu hỏi:** Với từng hành động (Tạo/Sửa/Xóa/Duyệt/Export...), ai được làm và ai không?

- Vai trò **có quyền** → thực hiện được, nút/chức năng hiển thị
- Vai trò **không có quyền** → nút bị ẩn hoặc disable; gọi API trực tiếp cũng bị từ chối (không chỉ ẩn UI)
- Áp dụng cho từng hành động: Tạo mới, Chỉnh sửa, Xóa, Duyệt/Từ chối, Xuất dữ liệu, In

### 9.3. Quyền theo phạm vi dữ liệu (Data Scope)
> **Pattern câu hỏi:** Vai trò này có được xem/sửa dữ liệu của người khác không?

- Vai trò chỉ xem được dữ liệu do mình tạo → không thấy dữ liệu người khác trong danh sách
- Vai trò xem được dữ liệu của cả phòng/ban → thấy đúng phạm vi, không thấy ngoài phạm vi
- Vai trò xem được toàn bộ → thấy tất cả
- **Cố ý truy cập dữ liệu ngoài phạm vi** (đổi ID trên URL, gọi API với ID người khác) → bị chặn 403/404, không lộ dữ liệu

### 9.4. Quyền theo trạng thái dữ liệu
> **Pattern câu hỏi:** Cùng vai trò đó, khi bản ghi ở trạng thái khác nhau thì được làm gì khác nhau?

- Sinh case cho **mỗi tổ hợp (vai trò × trạng thái)** theo bảng phân quyền trong SRS
- Vai trò thông thường không làm được hành động X khi bản ghi ở trạng thái Y → bị chặn đúng
- Vai trò đặc biệt (Admin) có thể vượt giới hạn trạng thái → thực hiện được (nếu nghiệp vụ cho phép)

### 9.5. Thay đổi phân quyền khi đang sử dụng
> **Pattern câu hỏi:** Điều gì xảy ra nếu quyền thay đổi trong lúc người dùng đang làm việc?

- Thu hồi quyền khi đang có session mở → hành động tiếp theo bị chặn đúng theo quyền mới (không cần đăng xuất mới có hiệu lực)
- Gán thêm quyền mới → chức năng mới xuất hiện đúng sau khi làm mới quyền hoặc đăng nhập lại
- Xem thêm Mục 25.2 nếu việc thay đổi quyền xảy ra từ module/màn hình khác

### 9.6. Phân biệt nội dung hiển thị theo vai trò (Role-based Data Visibility)
> **Pattern câu hỏi:** "Cùng một bản ghi, vai trò A thấy những trường nào? Vai trò B thấy gì khác?"
> Khác với 9.1–9.4 (ai được làm gì), 9.6 kiểm tra **nội dung** hiển thị khác nhau cho từng vai trò trên cùng một bản ghi.

- Xác định từng vai trò và **tập trường được phép thấy** (lấy từ SRS/đặc tả phân quyền hiển thị)
- Vai trò A xem bản ghi → thấy đúng tập trường của A, **không thấy trường chỉ dành cho vai trò khác**
- Trường nhạy cảm (giá gốc, thông tin cá nhân đầy đủ, ghi chú nội bộ) không lộ ra với vai trò không được phép, **kể cả khi gọi API trực tiếp**
- Dữ liệu được tính toán/hiển thị khác nhau có chủ đích theo vai trò (ví dụ: Admin thấy giá gốc, Customer thấy giá sau thuế) → tính toán đúng cho từng vai trò
- Khi vai trò A sửa trường mà vai trò B không thấy → vai trò B không bị ảnh hưởng bởi thay đổi đó

---

## 10. Kiểm tra xóa dữ liệu

Bắt buộc cover với các chức năng có hành động xóa (xóa cứng hoặc xóa mềm):

### 10.1. Xóa cơ bản
- Xóa một bản ghi hợp lệ — hiển thị thông báo xác nhận trước khi xóa
- Xác nhận xóa — bản ghi bị xóa khỏi danh sách và thông báo "Xóa thành công"
- Hủy xác nhận xóa — bản ghi không bị xóa, đóng popup xác nhận
- Xóa nhiều bản ghi cùng lúc (xóa hàng loạt)
- Xóa khi không chọn bản ghi nào — nút xóa bị khóa hoặc hiển thị thông báo yêu cầu chọn dữ liệu

### 10.2. Ràng buộc nghiệp vụ khi xóa
- Xóa bản ghi đang được tham chiếu bởi dữ liệu khác — hệ thống chặn xóa và hiển thị thông báo lý do
- Xóa bản ghi đang ở trạng thái không cho phép xóa (ví dụ: đã duyệt, đang xử lý) — hệ thống chặn và thông báo rõ
- Xóa bản ghi đang được người khác mở để chỉnh sửa — kiểm tra xử lý xung đột

### 10.3. Xóa mềm (Soft Delete) và khôi phục
- Bản ghi sau khi xóa mềm không còn hiển thị ở danh sách chính nhưng vẫn còn trong cơ sở dữ liệu
- Bản ghi đã xóa mềm không được tính vào kiểm tra tính duy nhất (hoặc có tính, tùy nghiệp vụ — xem Mục 3)
- Khôi phục bản ghi đã xóa mềm — bản ghi hiển thị lại đúng dữ liệu trước khi xóa
- Xóa cứng (permanent delete) sau khi đã xóa mềm — không thể khôi phục, có cảnh báo rõ ràng trước khi thực hiện

### 10.4. Hậu kiểm sau khi xóa
- Tải lại danh sách sau khi xóa — bản ghi không còn xuất hiện
- Kiểm tra các màn hình/báo cáo khác có tham chiếu bản ghi đã xóa — hiển thị đúng theo nghiệp vụ (ẩn, hiển thị "đã xóa", hoặc báo lỗi tham chiếu)
- Nhật ký hệ thống (log) ghi nhận đầy đủ hành động xóa: người thực hiện, thời gian, bản ghi bị xóa

---

## 11. Kiểm tra hồi quy (Regression)

Áp dụng khi có thay đổi (thêm field mới, sửa quy tắc nghiệp vụ, sửa lỗi, nâng cấp hệ thống) trên màn hình/chức năng đã tồn tại.

> **Pattern câu hỏi trước khi xác định phạm vi hồi quy:**
> - Thay đổi này chạm vào code/API/bảng dữ liệu nào?
> - Màn hình/chức năng nào khác dùng chung code/API/bảng đó?
> - Có module/portal nào khác hiển thị hoặc tính toán dựa trên dữ liệu vừa thay đổi không?
> - Có rule nghiệp vụ nào liên quan bị ảnh hưởng gián tiếp không?

### 11.1. Phạm vi xác định hồi quy
- Liệt kê các chức năng liên quan **trực tiếp** đến phần vừa thay đổi (cùng màn hình, cùng API, cùng bảng dữ liệu)
- Liệt kê các chức năng liên quan **gián tiếp** (màn hình khác có hiển thị/tính toán dựa trên dữ liệu vừa thay đổi)
- Liệt kê các **module/portal khác** có tích hợp với chức năng vừa thay đổi (áp dụng khi hệ thống có nhiều module — xem Mục 27)
- Với mỗi thay đổi, phân loại: thay đổi **logic nghiệp vụ** (ảnh hưởng rộng) hay thay đổi **UI thuần** (ảnh hưởng hẹp)

### 11.2. Test case hồi quy bắt buộc
> **Pattern câu hỏi:** "Điều gì đang hoạt động đúng trước đây có thể bị vỡ sau thay đổi này?"

- Các **luồng nghiệp vụ chính (happy path)** trước đây vẫn hoạt động đúng sau khi thay đổi
- Các **quy tắc nghiệp vụ cũ** không bị thay đổi ngoài ý muốn (sửa validate trường A không làm ảnh hưởng trường B)
- **Dữ liệu cũ** (đã tồn tại trước khi thay đổi) vẫn hiển thị và xử lý đúng với phiên bản mới — không bị mất, không bị hiển thị sai
- **Dữ liệu mới** (tạo sau khi thay đổi) hoạt động đúng theo logic mới
- Các **báo cáo/màn hình khác** có sử dụng dữ liệu từ chức năng vừa thay đổi vẫn hiển thị đúng
- **Phân quyền cũ** không bị ảnh hưởng bởi thay đổi mới
- **Tích hợp với module/hệ thống ngoài** (nếu có) vẫn hoạt động đúng sau khi thay đổi

### 11.3. Quản lý bộ test hồi quy
- Đánh dấu (tag) các test case thuộc bộ hồi quy để tái sử dụng cho các lần phát hành tiếp theo
- Cập nhật bộ test hồi quy mỗi khi có thay đổi nghiệp vụ được duyệt
- Ưu tiên chạy hồi quy theo mức độ: **High** (luồng chính) trước, **Medium** (validate/biên) sau

### 11.4. Hồi quy xuyên module (Cross-module Regression)
> Áp dụng khi thay đổi ở module A có thể ảnh hưởng đến module B hoặc C. Đây là loại hồi quy hay bị bỏ sót nhất vì tester chỉ test lại module vừa thay đổi.

> **Pattern câu hỏi:** "Nếu tôi thay đổi [X] ở module A, module B và C có bị ảnh hưởng không?"

- **Thay đổi cấu trúc dữ liệu** (thêm/đổi tên field, thay đổi kiểu dữ liệu) → kiểm tra tất cả module hiển thị field đó còn đúng không
- **Thay đổi API** (response format, status code, endpoint path) → kiểm tra tất cả module/portal đang dùng API đó còn hoạt động không
- **Thay đổi quy tắc nghiệp vụ** (điều kiện validation, điều kiện kích hoạt) → kiểm tra luồng tích hợp (Mục 27) còn đúng không
- **Thay đổi phân quyền** → kiểm tra các module khác đang dùng chung quyền đó không bị ảnh hưởng ngoài ý muốn
- **Danh sách module cần kiểm tra hồi quy**: lấy từ `module-map.md` — đọc trước khi xác định phạm vi

---

## 12. Kiểm tra đồng bộ dữ liệu

Áp dụng khi dữ liệu được chia sẻ, sao chép, hoặc đồng bộ giữa nhiều màn hình, nhiều module, hoặc với hệ thống ngoài.

### 12.1. Đồng bộ giữa các màn hình/module nội bộ
- Dữ liệu vừa tạo/sửa ở màn hình A hiển thị đúng và ngay lập tức ở màn hình B có tham chiếu
- Dữ liệu vừa xóa ở màn hình A không còn xuất hiện ở màn hình B
- Dữ liệu tổng hợp (báo cáo, dashboard) phản ánh đúng sau khi dữ liệu nguồn thay đổi

### 12.2. Đồng bộ thời gian thực (Real-time)

> Áp dụng khi hệ thống dùng cơ chế đẩy dữ liệu tức thời (WebSocket, Server-Sent Events, polling ngắn) để cập nhật giao diện mà không cần người dùng tải lại trang.

**Cơ chế cập nhật cơ bản**
- Hai người dùng cùng xem một màn hình — thay đổi của người này cập nhật cho người khác đúng theo cơ chế đã thiết kế (real-time tức thời, cần tải lại thủ công, hoặc có thông báo "có dữ liệu mới" để người dùng chủ động làm mới)
- Độ trễ đồng bộ nằm trong ngưỡng cho phép theo yêu cầu nghiệp vụ (ví dụ: cập nhật trong vòng 1-2 giây)
- Nhiều thay đổi xảy ra liên tiếp trong thời gian ngắn — giao diện cập nhật đúng theo đúng thứ tự xảy ra, không bị đảo thứ tự hoặc chỉ nhận bản cập nhật cuối cùng bỏ qua các bản ở giữa (tùy nghiệp vụ có yêu cầu giữ đủ lịch sử hay chỉ cần trạng thái mới nhất)

**Kết nối và ngắt kết nối (Connection lifecycle)**
- Mất kết nối real-time (rớt mạng, đóng tab, mất WebSocket) — giao diện nhận biết đúng trạng thái mất kết nối, hiển thị chỉ báo phù hợp (ví dụ icon "đang kết nối lại"), không tiếp tục hiển thị dữ liệu như đang cập nhật bình thường trong khi thực ra đã ngắt
- Kết nối lại (reconnect) sau khi mất kết nối — hệ thống tự động đồng bộ lại đúng dữ liệu mới nhất đã xảy ra trong lúc mất kết nối, không bỏ sót các thay đổi
- Mở nhiều tab cùng lúc trên cùng một trình duyệt — mỗi tab duy trì kết nối và cập nhật độc lập đúng, không xung đột hoặc chỉ 1 tab nhận được cập nhật
- Thiết bị chuyển từ mạng WiFi sang 4G hoặc ngược lại (trên mobile) giữa lúc đang kết nối real-time — kết nối được thiết lập lại đúng, không bị treo vĩnh viễn ở trạng thái mất kết nối

**Trùng lặp và thứ tự sự kiện (Event ordering & deduplication)**
- Cùng một sự kiện được gửi/nhận **2 lần** do lỗi mạng hoặc retry — giao diện xử lý đúng, không hiển thị trùng lặp hoặc áp dụng thay đổi 2 lần
- Sự kiện đến **sai thứ tự** so với thời điểm xảy ra thực tế (do độ trễ mạng khác nhau giữa các client) — hệ thống có cơ chế sắp xếp đúng (theo timestamp/version) hoặc chấp nhận "eventual consistency" theo đúng thiết kế
- Client nhận sự kiện cập nhật cho dữ liệu **không còn tồn tại** trên client đó (ví dụ đã bị xóa/lọc khỏi view) — xử lý đúng, không gây lỗi giao diện

**Tải cao và giới hạn (Scale & throttling — mức kiểm thử thủ công)**
- Nhiều client cùng kết nối real-time đến cùng 1 kênh/phòng dữ liệu — tất cả đều nhận cập nhật đúng, không có client bị bỏ sót (test tay ở mức vài chục kết nối; số lượng lớn hơn thuộc phạm vi Performance — xem Mục 15/`QA-Automation-Checklist.md`)
- Tần suất cập nhật rất nhanh liên tiếp (ví dụ nhiều người cùng thao tác dồn dập) — giao diện không bị giật/lag do xử lý quá nhiều sự kiện cùng lúc, có cơ chế gộp/throttle cập nhật nếu cần

### 12.3. Đồng bộ với hệ thống ngoài (tích hợp)
- Đồng bộ dữ liệu thành công với hệ thống ngoài — dữ liệu khớp ở cả hai phía
- Đồng bộ thất bại do hệ thống ngoài lỗi/timeout — có cơ chế báo lỗi, ghi log, và cho phép đồng bộ lại (retry)
- Đồng bộ một phần (partial sync) khi xử lý hàng loạt — xác định rõ bản ghi nào thành công, bản ghi nào lỗi
- Dữ liệu trùng lặp khi đồng bộ nhiều lần (đảm bảo idempotent — không tạo trùng bản ghi)
- Xung đột dữ liệu (conflict) khi cùng một bản ghi bị sửa ở cả hai hệ thống — kiểm tra quy tắc ưu tiên xử lý xung đột

### 12.4. Đồng bộ và tính nhất quán dữ liệu
- Dữ liệu nhất quán giữa giao diện và cơ sở dữ liệu sau mọi hành động đồng bộ
- Tải lại trang/đăng nhập lại sau khi đồng bộ — dữ liệu hiển thị đúng trạng thái mới nhất

### 12.5. Đồng bộ có điều kiện kích hoạt và khác biệt tập hiển thị (Conditional publish / Cross-audience visibility)

> Áp dụng cho các luồng mà dữ liệu được tạo/quản lý ở một module (ví dụ module nội bộ, quản trị, đối tác) nhưng chỉ được hiển thị sang module khác (ví dụ module khách hàng, module công khai, module đối tác khác) **khi thỏa một điều kiện nghiệp vụ cụ thể** — khác với đồng bộ thông thường ở Mục 12.1–12.4 vì có "cổng" kích hoạt và có thể có sự khác biệt về tập dữ liệu hiển thị giữa hai phía.

**Điều kiện kích hoạt việc hiển thị/chia sẻ**
- Dữ liệu chưa thỏa điều kiện kích hoạt (ví dụ chưa chuyển đúng trạng thái) — không hiển thị, không thể truy cập được ở module đích, kể cả khi biết ID/đường dẫn trực tiếp
- Dữ liệu vừa thỏa điều kiện kích hoạt — xuất hiện đúng, đúng thời điểm, đúng nội dung ở module đích
- Dữ liệu thỏa điều kiện nhưng thiếu một trường bắt buộc khác để hiển thị hợp lệ (nếu có) — hệ thống xử lý đúng theo nghiệp vụ (chặn kích hoạt, hoặc hiển thị với cảnh báo/thiếu sót)

**Khác biệt tập dữ liệu hiển thị giữa hai phía**
- Module đích chỉ nhận/hiển thị đúng tập trường được phép công khai/chia sẻ, không lộ các trường nội bộ hoặc nhạy cảm
- Module nguồn vẫn hiển thị đầy đủ thông tin nội bộ như trước, không bị ảnh hưởng bởi việc dữ liệu đã được chia sẻ
- Trường dữ liệu được tính toán/hiển thị khác nhau có chủ đích giữa hai module (ví dụ rút gọn, làm tròn, ẩn danh một phần) được áp dụng đúng quy tắc

**Cập nhật sau khi đã kích hoạt**
- Sửa dữ liệu ở module nguồn sau khi đã kích hoạt hiển thị — module đích cập nhật đúng theo, hoặc giữ nguyên bản đã chia sẻ nếu nghiệp vụ yêu cầu "đóng băng" dữ liệu sau khi chia sẻ
- Nhiều bản ghi được kích hoạt hiển thị cùng lúc (hàng loạt) — tất cả xuất hiện đúng và đầy đủ ở module đích, không thiếu/lặp bản ghi

**Thu hồi điều kiện kích hoạt (chiều ngược)**
- Hủy/thu hồi điều kiện kích hoạt (đổi trạng thái ngược lại) — dữ liệu biến mất hoặc chuyển trạng thái phù hợp ở module đích, không còn truy cập được như trước
- Xóa dữ liệu ở module nguồn khi đang ở trạng thái đã kích hoạt hiển thị — kiểm tra ràng buộc cho phép/không cho phép xóa, và module đích xử lý đúng theo (ẩn dữ liệu, báo lỗi tham chiếu, hoặc giữ bản ghi đã lưu tùy nghiệp vụ)
- Thu hồi rồi kích hoạt lại — dữ liệu hiển thị đúng trở lại ở module đích, không để lại dữ liệu cũ sai lệch từ lần thu hồi trước

---
**Cách cụ thể hóa Mục 12.5 khi áp dụng cho chức năng thực tế**

> Mục 12.5 là nguyên tắc khung — khi gen test case cho một chức năng cụ thể có luồng conditional publish, QA cần điền vào template dưới đây trước khi bắt đầu viết testcase. Template này thay thế các cụm từ trừu tượng ("module nguồn", "điều kiện kích hoạt"...) bằng đúng tên nghiệp vụ thực tế của chức năng đang test.

**Bước 1 — Điền thông tin đặc tả chức năng:**

| Câu hỏi | Trả lời (điền theo nghiệp vụ thực tế) |
|---|---|
| **Module nguồn** là gì? (bên tạo/quản lý dữ liệu) | `[Tên module — ví dụ: Quản trị / Đối tác / Nội bộ]` |
| **Module đích** là gì? (bên nhận/hiển thị dữ liệu) | `[Tên module — ví dụ: Khách hàng / Công khai / Đối tác B]` |
| **Điều kiện kích hoạt** là gì? (trạng thái/hành động nào làm dữ liệu lộ ra module đích) | `[Tên trạng thái hoặc hành động — ví dụ: Trạng thái = "Đã duyệt" / Bật công tắc "Công khai" / Bấm nút "Phát hành"]` |
| **Điều kiện thu hồi** là gì? (ngược lại với kích hoạt) | `[Tên trạng thái hoặc hành động ngược — ví dụ: Trạng thái = "Tạm ngưng" / Tắt công tắc / Bấm "Gỡ xuống"]` |
| **Tập trường được hiển thị ở module đích** (chỉ liệt kê những trường được phép lộ ra) | `[Trường A, Trường B, Trường C, ...]` |
| **Tập trường bị ẩn ở module đích** (trường nội bộ/nhạy cảm không được lộ) | `[Trường X, Trường Y, ...]` |
| Sau khi kích hoạt, **dữ liệu nguồn bị sửa** thì module đích xử lý thế nào? | `[Cập nhật theo / Đóng băng bản cũ / Cập nhật một phần — ghi rõ theo nghiệp vụ]` |
| Module đích có **hiển thị realtime** hay cần tải lại? | `[Realtime / Cần F5 / Cần đăng xuất-đăng nhập lại]` |

**Bước 2 — Thay thế vào checklist, sinh testcase theo từng dòng:**

Sau khi điền Bước 1, ánh xạ từng nguyên tắc trong Mục 12.5 sang testcase cụ thể theo bảng dưới:

| Nguyên tắc trong Mục 12.5 | Testcase cụ thể sau khi thay thế |
|---|---|
| "Dữ liệu chưa thỏa điều kiện kích hoạt — không hiển thị ở module đích" | **TC:** Bản ghi ở `[module nguồn]` chưa chuyển sang `[điều kiện kích hoạt]` — truy cập từ `[module đích]` không thấy bản ghi, kể cả nhập trực tiếp URL |
| "Dữ liệu vừa thỏa điều kiện kích hoạt — xuất hiện đúng ở module đích" | **TC:** Chuyển bản ghi sang `[điều kiện kích hoạt]` tại `[module nguồn]` — bản ghi xuất hiện đúng tại `[module đích]` trong `[thời gian tải/realtime]` |
| "Module đích chỉ nhận đúng tập trường được phép" | **TC:** Mở bản ghi tại `[module đích]` — chỉ thấy `[danh sách trường được phép]`, không thấy `[danh sách trường bị ẩn]` |
| "Module nguồn vẫn hiển thị đầy đủ" | **TC:** Sau khi kích hoạt, mở lại bản ghi tại `[module nguồn]` — vẫn thấy đầy đủ tất cả trường kể cả trường nội bộ |
| "Sửa dữ liệu ở module nguồn sau khi đã kích hoạt" | **TC:** Sửa `[trường A]` tại `[module nguồn]` khi bản ghi đang ở `[điều kiện kích hoạt]` — kiểm tra `[module đích]` hiển thị `[cập nhật theo / giữ bản cũ]` theo đúng nghiệp vụ |
| "Thu hồi điều kiện kích hoạt" | **TC:** Chuyển bản ghi từ `[điều kiện kích hoạt]` sang `[điều kiện thu hồi]` tại `[module nguồn]` — bản ghi biến mất / ẩn đúng tại `[module đích]` |
| "Xóa dữ liệu khi đang ở trạng thái đã kích hoạt" | **TC:** Thử xóa bản ghi đang ở `[điều kiện kích hoạt]` tại `[module nguồn]` — kiểm tra hệ thống `[chặn xóa / cho xóa và module đích xử lý thế nào]` |
| "Thu hồi rồi kích hoạt lại" | **TC:** Thu hồi bản ghi về `[điều kiện thu hồi]` → kích hoạt lại → `[module đích]` hiển thị đúng dữ liệu mới nhất, không còn dữ liệu cũ từ lần thu hồi trước |
| "Kích hoạt hàng loạt nhiều bản ghi" | **TC:** Chọn N bản ghi tại `[module nguồn]` → kích hoạt cùng lúc → tất cả N bản ghi xuất hiện đúng tại `[module đích]`, không thiếu, không lặp |
| "Truy cập bằng URL trực tiếp khi chưa kích hoạt" | **TC:** Lấy URL/ID bản ghi chưa ở `[điều kiện kích hoạt]` → truy cập từ `[module đích]` → nhận `[404 / thông báo không có quyền]`, không lộ dữ liệu |

**Bước 3 — Đặt tên nhóm testcase trong bảng theo chuẩn Mục 1.2:**

```
[Số thứ tự]. Kiểm tra đồng bộ có điều kiện: [Module nguồn] → [Module đích]

   [Số].1. Kiểm tra điều kiện kích hoạt ([Tên điều kiện kích hoạt])
   [Số].2. Kiểm tra tập trường hiển thị tại [Module đích]
   [Số].3. Kiểm tra cập nhật sau khi đã kích hoạt
   [Số].4. Kiểm tra thu hồi và kích hoạt lại ([Tên điều kiện thu hồi])
```

## 13. Kiểm tra trạng thái Enable/Disable

Áp dụng cho mọi control hoặc nút bấm mà trạng thái bật/tắt phụ thuộc vào điều kiện (khác với phân quyền ở Mục 9, vốn phụ thuộc vai trò người dùng). Đây là điều kiện phụ thuộc **dữ liệu/nghiệp vụ**, không phải phụ thuộc **vai trò**.

### 13.1. Phụ thuộc giữa các trường (Field dependency)
- Trường B mặc định bị khóa (disable) khi trường A chưa có giá trị
- Trường B tự động mở khóa (enable) ngay khi trường A được nhập/chọn giá trị hợp lệ
- Trường B tự động khóa lại khi giá trị trường A bị xóa hoặc đổi sang giá trị không thỏa điều kiện
- Trường B giữ nguyên giá trị đã nhập trước đó khi bị khóa lại, hoặc bị xóa trắng (theo đúng nghiệp vụ yêu cầu)

### 13.2. Phụ thuộc theo trạng thái bản ghi
- Toàn bộ form chuyển sang chỉ đọc (read-only) khi bản ghi ở trạng thái đã duyệt/đã khóa
- Một số trường cụ thể bị khóa còn một số trường khác vẫn chỉnh sửa được, theo đúng từng trạng thái nghiệp vụ
- Nút hành động (Lưu, Gửi, Duyệt, Xóa...) tự động enable/disable theo đúng trạng thái hiện tại của bản ghi

### 13.3. Phụ thuộc theo lựa chọn của control khác
- Chọn một giá trị ở Danh sách chọn/Nút chọn đơn làm xuất hiện (enable) thêm các trường nhập liệu liên quan
- Bỏ chọn giá trị đó làm các trường liên quan biến mất hoặc bị khóa lại, đồng thời dữ liệu đã nhập trong các trường đó được xử lý đúng theo nghiệp vụ (xóa trắng hoặc giữ nguyên)
- Hộp kiểm (checkbox) được chọn làm enable/disable một nhóm control liên quan (đã có cơ sở từ Mục 5.5, bổ sung thêm theo nhóm điều kiện)

### 13.4. Nút hành động (Button state)
- Nút "Lưu"/"Gửi" mặc định bị disable khi form chưa có thay đổi hoặc chưa nhập đủ dữ liệu bắt buộc
- Nút tự động enable ngay khi đủ điều kiện (đã nhập đủ trường bắt buộc, dữ liệu hợp lệ)
- Nút tự động disable lại (chống bấm nhiều lần / double-submit) trong lúc hệ thống đang xử lý yêu cầu
- Nút trở lại trạng thái enable sau khi xử lý hoàn tất (thành công hoặc thất bại)

### 13.5. Disable theo thời gian (Time-based Disable)

> Khác với 13.1–13.4 (phụ thuộc dữ liệu tĩnh tại 1 thời điểm), Mục 13.5 kiểm tra trạng thái Enable/Disable phụ thuộc **đồng hồ đang chạy liên tục** — liên kết chặt với Mục 28 (Kiểm tra tác vụ theo thời gian). Đây là loại case dễ có bug "vùng xám" nhất: nút bấm và logic xử lý không đồng bộ đúng tại đúng khoảnh khắc chuyển trạng thái.
>
> **Điều kiện áp dụng:** có nút hành động mà khả năng bấm được phụ thuộc vào mốc thời gian (đếm ngược về 0, ngoài khung giờ cho phép, hết hạn phiên...).

- Nút hành động (ví dụ "Đặt giá", "Xác nhận") **tự động disable đúng thời điểm** đồng hồ đếm ngược về 0 — không disable sớm hơn (mất cơ hội thao tác hợp lệ) và không disable muộn hơn (cho phép bấm vào thời điểm đã hết hạn, dẫn đến server từ chối gây trải nghiệm khó hiểu)
- Trong khoảng **"vùng xám"** giữa lúc hết giờ cũ và thời điểm gia hạn mới được xác nhận (nếu có độ trễ xử lý gia hạn — xem Mục 28.3) — nút giữ đúng trạng thái nhất quán theo 1 quy tắc rõ ràng, không nhấp nháy qua lại enable/disable gây rối mắt hoặc cho phép bấm vào đúng khoảnh khắc không xác định
- Nút tự động **enable lại** ngay khi có gia hạn thành công (thời gian được nối dài) — không giữ nguyên trạng thái disable dù thực tế đã còn thời gian để thao tác
- Hành động chỉ được phép trong **một khung giờ nhất định** (ví dụ chỉ sửa đơn hàng trong giờ hành chính, chỉ hủy chuyến trước giờ khởi hành X phút) — nút tự động disable đúng khi ra khỏi khung giờ cho phép, không cần người dùng tải lại trang mới cập nhật trạng thái
- Test tại đúng ranh giới: thao tác ở **[mốc - 1 giây]**, **[đúng mốc]**, **[mốc + 1 giây]** — xác nhận trạng thái nút nhất quán ở cả 3 thời điểm, không có khoảng "vùng xám" xử lý sai (liên kết trực tiếp Mục 28.6 — Race condition tại ranh giới thời gian)
- Trạng thái disable do hết thời gian hiển thị đúng **lý do** cho người dùng (ví dụ tooltip/label "Đã hết thời gian đặt giá") — phân biệt rõ với disable do thiếu dữ liệu (13.4) hoặc do thiếu quyền (Mục 9.2), tránh người dùng nhầm lẫn nguyên nhân

---

## 14. Kiểm tra cấu hình (Config case)

Áp dụng khi màn hình/chức năng có các tham số cấu hình hệ thống làm thay đổi hành vi hoặc giao diện (ví dụ: cấu hình theo công ty, theo chi nhánh, theo loại hợp đồng, bật/tắt tính năng...).

### 14.1. Xác định các tổ hợp cấu hình cần test
- Liệt kê toàn bộ tham số cấu hình ảnh hưởng đến màn hình/chức năng đang test (lấy từ tài liệu nghiệp vụ hoặc màn hình cấu hình hệ thống)
- Với mỗi tham số, xác định các giá trị có thể có (ví dụ: Bật/Tắt, hoặc danh sách lựa chọn cấu hình)
- Ưu tiên kiểm thử các tổ hợp cấu hình có ảnh hưởng nghiệp vụ cao trước (theo nguyên tắc cặp đôi/pairwise nếu số tổ hợp quá lớn để test hết)

### 14.2. Test case theo từng cấu hình
- Cấu hình A được Bật — chức năng/trường liên quan hiển thị và hoạt động đúng theo mô tả nghiệp vụ của cấu hình đó
- Cấu hình A được Tắt — chức năng/trường liên quan bị ẩn hoặc vô hiệu hóa đúng theo mô tả nghiệp vụ
- Thay đổi cấu hình từ Bật sang Tắt (hoặc ngược lại) khi đã có dữ liệu cũ — kiểm tra dữ liệu cũ hiển thị/xử lý đúng với cấu hình mới (không bị mất dữ liệu, không gây lỗi)

### 14.3. Tổ hợp nhiều cấu hình
- Hai hoặc nhiều cấu hình cùng ảnh hưởng đến một trường/chức năng — kiểm tra thứ tự ưu tiên áp dụng đúng theo nghiệp vụ khi các cấu hình có xung đột nhau
- Cấu hình mặc định của hệ thống khi chưa có ai thiết lập — đúng theo giá trị mặc định tài liệu yêu cầu

### 14.4. Phạm vi áp dụng cấu hình
- Cấu hình áp dụng đúng phạm vi đã thiết lập (toàn hệ thống / theo công ty / theo chi nhánh / theo nhóm người dùng)
- Người dùng thuộc phạm vi không áp dụng cấu hình vẫn giữ hành vi mặc định/cấu hình khác, không bị ảnh hưởng

---

## 15. Kiểm tra xử lý lỗi hệ thống (Error handling — kiểm thử thủ công)

> Phạm vi: kiểm thử thủ công (manual) các tình huống lỗi hệ thống có thể mô phỏng được bằng tay (tắt mạng, dùng DevTools chặn request, chờ timeout thực tế...). Không bao gồm kiểm thử hiệu năng/tải (load test, stress test) — các nội dung đó cần công cụ và môi trường chuyên biệt, nằm ngoài phạm vi test case thủ công.

### 15.1. Mất kết nối mạng
- Mất mạng ngay trước khi bấm Lưu/Gửi — hệ thống hiển thị thông báo lỗi kết nối rõ ràng, không làm mất dữ liệu đã nhập trên form
- Mất mạng ngay sau khi bấm Lưu/Gửi (trong lúc đang xử lý) — hệ thống không tạo dữ liệu trùng/lỗi, hiển thị thông báo phù hợp khi có mạng trở lại
- Mất mạng khi đang tải dữ liệu lên màn hình (load danh sách, mở form chỉnh sửa) — hiển thị thông báo lỗi tải dữ liệu, có tùy chọn thử lại

### 15.2. Server lỗi / Timeout
- Server trả lỗi 500 (lỗi hệ thống) khi lưu dữ liệu — hệ thống hiển thị thông báo lỗi thân thiện, không hiển thị lỗi kỹ thuật thô cho người dùng cuối, dữ liệu đã nhập không bị mất
- Server phản hồi chậm/timeout khi lưu hoặc tải dữ liệu — hệ thống hiển thị trạng thái đang xử lý (loading) và thông báo timeout rõ ràng nếu vượt ngưỡng thời gian quy định
- Server trả về dữ liệu sai định dạng (lỗi tích hợp) — giao diện không bị crash, hiển thị thông báo lỗi phù hợp

### 15.3. Hành vi double-submit / thao tác lặp lại khi có lỗi
- Bấm nhiều lần liên tiếp vào nút Lưu/Gửi khi mạng chậm — hệ thống chỉ xử lý một lần, không tạo dữ liệu trùng lặp
- Thử lại (retry) sau khi gặp lỗi — hệ thống xử lý đúng, không phát sinh dữ liệu trùng hoặc xung đột với lần xử lý trước đó (nếu có)

### 15.4. Khôi phục sau lỗi
- Sau khi gặp lỗi và người dùng sửa lại dữ liệu hợp lệ — hệ thống lưu thành công ở lần thử tiếp theo
- Tải lại trang sau khi gặp lỗi — kiểm tra dữ liệu có bị lưu một phần (partial save) hay không; nếu nghiệp vụ yêu cầu toàn vẹn dữ liệu (all or nothing) thì không được có dữ liệu lưu một phần

---

## 16. Kiểm tra xử lý đồng thời & phiên làm việc (Concurrency & Session)

> Phạm vi: kiểm thử thủ công bằng cách mở nhiều tab/nhiều trình duyệt/nhiều thiết bị, hoặc chủ động làm hết hạn session (xóa cookie, chờ timeout thực tế, dùng tài khoản phụ) — không cần công cụ load test chuyên biệt.

### 16.1. Nhiều người dùng cùng thao tác trên một bản ghi
- Hai người dùng cùng mở một bản ghi để chỉnh sửa — cả hai đều xem được dữ liệu, không bị chặn truy cập chỉ vì người khác đang mở
- Hai người dùng cùng sửa và lưu một bản ghi ở các thời điểm gần nhau — xác định rõ hành vi hệ thống: ai lưu sau sẽ ghi đè hoàn toàn (last write wins), hay hệ thống cảnh báo xung đột (conflict) và yêu cầu xác nhận trước khi ghi đè
- Một người dùng đang sửa, người khác xóa chính bản ghi đó — người đang sửa khi bấm Lưu nhận được thông báo phù hợp (không lưu thành công vào bản ghi đã bị xóa, không phát sinh lỗi hệ thống)
- Một người dùng đang sửa, người khác thay đổi trạng thái bản ghi (ví dụ duyệt/khóa) — người đang sửa khi bấm Lưu nhận được thông báo phù hợp theo đúng quy tắc nghiệp vụ mới nhất

### 16.2. Hết hạn phiên làm việc (Session timeout)
- Phiên làm việc hết hạn trong lúc người dùng đang điền form (form dài, nhiều bước) — khi bấm Lưu/Gửi, hệ thống thông báo rõ phiên đã hết hạn và hướng dẫn đăng nhập lại, không làm mất toàn bộ dữ liệu đã nhập một cách âm thầm (ưu tiên giữ lại dữ liệu nhập để người dùng đăng nhập lại và tiếp tục, nếu nghiệp vụ cho phép)
- Đăng nhập lại sau khi hết phiên — hệ thống đưa người dùng trở lại đúng màn hình/thao tác đang thực hiện trước đó (nếu nghiệp vụ yêu cầu), hoặc về màn hình mặc định kèm thông báo rõ ràng
- Đăng xuất ở một tab/thiết bị trong khi đang mở phiên làm việc ở tab/thiết bị khác — hành vi của các tab/thiết bị còn lại đúng theo quy tắc bảo mật của hệ thống (đăng xuất toàn bộ hoặc giữ riêng từng phiên, tùy thiết kế)

---

## 17. Kiểm tra điều hướng bàn phím cơ bản (Keyboard Navigation)

> Phạm vi: kiểm thử thủ công bằng phím Tab, Shift+Tab, Enter, Esc, phím mũi tên — ở mức cơ bản phục vụ trải nghiệm sử dụng hàng ngày. Không bao gồm kiểm thử Accessibility/a11y chuyên sâu theo chuẩn WCAG (screen reader, ARIA, contrast ratio...) — các nội dung đó cần quy trình và tiêu chuẩn riêng, nằm ngoài phạm vi test case thủ công này.

### 17.1. Thứ tự di chuyển (Tab order)
- Nhấn Tab di chuyển qua các trường theo đúng thứ tự hợp lý trên giao diện (trái → phải, trên → dưới, hoặc theo đúng luồng nhập liệu tự nhiên), không nhảy lộn xộn
- Nhấn Shift+Tab di chuyển ngược lại đúng theo thứ tự đã đi qua
- Trường/control bị ẩn hoặc bị disable không nằm trong thứ tự Tab (không vô tình nhận được focus)
- Focus hiển thị rõ ràng bằng mắt thường tại control đang được chọn (không bị mất dấu focus)

### 17.2. Phím tắt thao tác phổ biến
- Nhấn Enter trong một ô nhập liệu không vô tình submit toàn bộ form nếu chưa đủ điều kiện hoặc nếu nghiệp vụ không yêu cầu submit bằng Enter
- Nhấn Enter khi đang focus vào nút Lưu/Gửi thực hiện đúng hành động của nút đó
- Nhấn Esc đóng đúng popup/dialog đang mở (xác nhận, chọn ngày, danh sách chọn...) mà không làm mất dữ liệu đã nhập ở các trường khác trên form
- Dùng phím mũi tên để di chuyển/chọn giá trị trong Danh sách chọn, Nút chọn đơn hoạt động đúng

---

## 18. Kiểm tra thông báo hệ thống (Notification Trigger)

> Áp dụng khi hành động tạo mới/chỉnh sửa/xóa/duyệt... có kích hoạt gửi thông báo (email, SMS, thông báo trong hệ thống/in-app). Nếu chức năng đang test không có bất kỳ loại thông báo nào, bỏ qua toàn bộ mục này, không tính là thiếu sót.

### 18.1. Điều kiện kích hoạt thông báo
- Hành động đúng điều kiện kích hoạt — thông báo được gửi đúng thời điểm, đúng người nhận
- Hành động không đủ điều kiện kích hoạt (ví dụ nghiệp vụ chỉ gửi thông báo khi chuyển sang một trạng thái cụ thể) — không gửi thông báo khi chưa đạt điều kiện đó
- Thực hiện lại cùng hành động nhiều lần — không gửi thông báo trùng lặp nếu nghiệp vụ chỉ yêu cầu gửi một lần

### 18.2. Nội dung và người nhận thông báo
- Nội dung thông báo (tiêu đề, nội dung, các thông tin động như tên/mã/ngày) hiển thị đúng, khớp với dữ liệu thực tế của bản ghi vừa thao tác
- Thông báo được gửi đúng đến người nhận theo quy tắc nghiệp vụ (người tạo, người được phân công, người quản lý liên quan...)
- Trường hợp nhiều người nhận — tất cả người nhận hợp lệ đều nhận được, không thiếu, không gửi nhầm cho người không liên quan

### 18.3. Liên kết và trạng thái thông báo
- Đường dẫn/liên kết trong thông báo (nếu có) dẫn đúng đến đúng bản ghi/màn hình liên quan
- Thông báo trong hệ thống (in-app) hiển thị đúng trạng thái đã đọc/chưa đọc, và cập nhật đúng khi người dùng mở xem
- Xóa hoặc đánh dấu đã đọc thông báo — trạng thái được lưu đúng và hiển thị nhất quán khi tải lại

---

## 19. Kiểm tra Export/Print dữ liệu

> Áp dụng cho màn hình/chức năng có hỗ trợ xuất dữ liệu (Excel, CSV, PDF...) hoặc in trực tiếp. Nếu chức năng đang test không có chức năng xuất/in, bỏ qua toàn bộ mục này, không tính là thiếu sót.

### 19.1. Phạm vi dữ liệu xuất/in
- Xuất/in khi đã chọn một hoặc nhiều bản ghi cụ thể — chỉ các bản ghi đã chọn được xuất/in, không lẫn bản ghi khác
- Xuất/in toàn bộ danh sách khi không chọn bản ghi nào (nếu nghiệp vụ cho phép) — toàn bộ dữ liệu hiện có được xuất/in đầy đủ
- Xuất/in khi đang áp dụng bộ lọc/tìm kiếm (xem Mục 4) — chỉ xuất/in đúng tập dữ liệu đã lọc, không xuất toàn bộ dữ liệu gốc
- Xuất/in khi danh sách đang phân trang — xuất/in đúng theo phạm vi đã chọn (toàn bộ kết quả lọc/tìm kiếm, không chỉ riêng trang hiện tại, trừ khi nghiệp vụ quy định khác)
- Xuất/in khi không có dữ liệu nào (danh sách rỗng hoặc lọc ra kết quả rỗng) — hệ thống xử lý đúng (chặn xuất kèm thông báo, hoặc xuất file/in trang chỉ có tiêu đề cột), không phát sinh lỗi hệ thống
- Xuất/in với số lượng bản ghi rất lớn — hệ thống xử lý đúng (có thể giới hạn số lượng, xử lý theo lô, hoặc hiển thị tiến trình), không bị treo hoặc timeout không rõ nguyên nhân

### 19.2. Nội dung và định dạng file xuất
- Dữ liệu trong file xuất khớp đúng với dữ liệu hiển thị trên giao diện (đúng giá trị, đúng định dạng số/ngày/tiền tệ, không bị lệch cột)
- Tên cột/tiêu đề trong file xuất đúng và khớp với tên cột hiển thị trên giao diện
- Dữ liệu dạng danh sách chọn/nhiều giá trị được xuất đúng, đầy đủ (không bị cắt, không hiển thị mã thay vì tên hiển thị nếu nghiệp vụ yêu cầu hiển thị tên)
- Ký tự đặc biệt, tiếng Việt có dấu trong dữ liệu được xuất đúng, không bị lỗi encode (ô vuông, ký tự lạ) khi mở file bằng phần mềm tương ứng (Excel, trình đọc PDF...)
- Tên file xuất ra đúng quy tắc đặt tên theo nghiệp vụ (ví dụ có ngày giờ xuất, tên màn hình), không trùng lặp gây nhầm lẫn giữa các lần xuất khác nhau
- File xuất mở được đúng bằng phần mềm tương ứng, không bị lỗi/hỏng file

### 19.3. Phân quyền và bảo mật khi xuất/in
- Vai trò có quyền xuất/in — thực hiện được, nút/chức năng hiển thị
- Vai trò không có quyền xuất/in — nút bị ẩn hoặc khóa, không xuất/in được dù gọi trực tiếp
- Dữ liệu xuất ra chỉ chứa các trường mà vai trò hiện tại được phép xem (không lộ trường nhạy cảm nếu vai trò đó bị ẩn trường tương ứng trên giao diện — xem Mục 9.3)
- Hành động xuất/in được ghi nhận vào nhật ký hệ thống (nếu nghiệp vụ yêu cầu log truy xuất dữ liệu)

### 19.4. Hành vi giao diện khi xuất/in
- Bấm nút Xuất/In — hệ thống hiển thị trạng thái đang xử lý (loading) trong lúc tạo file, không cho bấm nhiều lần liên tiếp gây tạo nhiều file trùng
- Xuất/in thành công — thông báo rõ ràng (tải file tự động, hoặc thông báo "Xuất file thành công" kèm đường dẫn tải)
- Xuất/in thất bại (lỗi hệ thống, dữ liệu quá lớn, mất kết nối giữa lúc xử lý) — thông báo lỗi rõ ràng, không để người dùng chờ vô thời hạn
- Hộp thoại in (Print dialog) hiển thị đúng nội dung xem trước (print preview) khớp với dữ liệu thực tế trước khi in

---

## 20. Kiểm tra Import/Export hàng loạt dữ liệu (Bulk Import/Export)

> Khác với Mục 19 (xuất dữ liệu hiện có để xem/lưu trữ), Mục 20 tập trung vào việc **đưa dữ liệu vào hệ thống hàng loạt** qua file (Import) và **xuất dữ liệu ra file theo mẫu chuẩn để dùng lại/chỉnh sửa rồi import lại** (Export phục vụ Import). Áp dụng cho màn hình/chức năng có hỗ trợ tải file mẫu, tải lên file dữ liệu hàng loạt (Excel, CSV...). Nếu chức năng không có Import hàng loạt, bỏ qua toàn bộ mục này, không tính là thiếu sót.

### 20.1. Tải file mẫu (Template Download)
- Tải file mẫu — file có đúng cấu trúc cột theo quy định, đúng tên cột, đúng thứ tự
- File mẫu có hướng dẫn/ví dụ mẫu (nếu thiết kế có) — nội dung hướng dẫn rõ ràng, không gây hiểu nhầm định dạng
- File mẫu tải về có định dạng đúng (mở được bằng phần mềm tương ứng, không lỗi/hỏng)

### 20.2. Validate file trước khi Import
- Tải lên **đúng định dạng** file (theo quy định đuôi file, ví dụ .xlsx) — được chấp nhận
- Tải lên **sai định dạng** file (ví dụ tải file .pdf khi chỉ chấp nhận .xlsx) — bị từ chối, thông báo rõ định dạng yêu cầu
- Tải lên file **đúng định dạng nhưng sai cấu trúc cột** (thiếu cột, thừa cột, sai tên cột, sai thứ tự cột) — hệ thống phát hiện và thông báo rõ cột nào sai, không cố xử lý mù mờ theo cấu trúc sai
- Tải lên file **rỗng** (không có dữ liệu, chỉ có header) — hệ thống xử lý đúng, không báo lỗi hệ thống hoặc crash
- Tải lên file **vượt dung lượng cho phép** — bị từ chối, thông báo rõ giới hạn dung lượng
- Tải lên file **vượt số dòng dữ liệu cho phép** (nếu có giới hạn) — bị từ chối hoặc xử lý theo lô, đúng theo thiết kế

### 20.3. Validate dữ liệu bên trong file Import
> Áp dụng lại toàn bộ checklist tương ứng của Mục 5 (Kiểm tra trường dữ liệu) cho **từng cột dữ liệu trong file**, không phải chỉ validate khi nhập tay qua UI.

- Mỗi dòng dữ liệu trong file được validate đúng theo quy tắc của trường tương ứng (bắt buộc, định dạng, độ dài, giá trị biên) — áp dụng checklist Mục 5 cho từng cột
- Dòng dữ liệu **hợp lệ toàn bộ** — được import thành công
- Dòng dữ liệu **có ít nhất 1 cột không hợp lệ** — dòng đó bị từ chối/đánh dấu lỗi, có báo cáo rõ **dòng nào, cột nào, lỗi gì** (không chỉ báo "file có lỗi" chung chung)
- Dữ liệu trong file **trùng nhau ngay trong file** (composite hoặc đơn lẻ, xem Mục 3.5) — hệ thống phát hiện và xử lý đúng, không chỉ kiểm tra trùng với dữ liệu đã có trong DB
- Dữ liệu trong file **trùng với dữ liệu đã tồn tại** trong hệ thống — xử lý đúng theo thiết kế (từ chối dòng đó, ghi đè, hoặc bỏ qua — cần rõ ràng trong nghiệp vụ)
- Dữ liệu tham chiếu đến bản ghi khác (ví dụ mã danh mục) **không tồn tại** trong hệ thống — dòng đó bị từ chối, báo lỗi rõ tham chiếu nào không hợp lệ

### 20.4. Xử lý kết quả Import (thành công một phần / toàn phần)
- Toàn bộ dòng **hợp lệ** — import thành công 100%, thông báo rõ số lượng bản ghi đã tạo
- **Một số dòng lỗi, một số dòng hợp lệ** — hệ thống xử lý đúng theo chiến lược đã thiết kế:
  - **All-or-nothing**: nếu có bất kỳ dòng lỗi nào, không import dòng nào cả, giữ nguyên trạng thái trước khi import
  - **Partial import**: các dòng hợp lệ được import, các dòng lỗi bị bỏ qua và báo cáo riêng
  - *(Xác nhận rõ chiến lược nào được áp dụng trước khi viết kết quả mong muốn)*
- Có **file/báo cáo kết quả** liệt kê chi tiết dòng nào thành công, dòng nào thất bại kèm lý do — tải về được để người dùng sửa và import lại
- Import file với **số lượng dòng lớn** — hệt thống xử lý đúng (theo lô, hiển thị tiến trình, không timeout), không bị treo giao diện
- Hủy quá trình import giữa chừng (nếu hỗ trợ) — dữ liệu đã xử lý đến thời điểm hủy được giữ lại hoặc rollback toàn bộ, đúng theo thiết kế, không để trạng thái dữ liệu nửa vời

### 20.5. Post-action & tích hợp sau Import
- Sau khi import thành công — danh sách cập nhật đúng, hiển thị đầy đủ các bản ghi vừa import (liên quan Mục 6 — Post-action Behavior)
- Bản ghi được tạo qua Import áp dụng đúng **toàn bộ quy tắc nghiệp vụ** giống như tạo qua UI thủ công (không có "đường tắt" bỏ qua validate nghiệp vụ chỉ vì đi qua đường Import) — xem Mục 8
- Nếu dữ liệu import có liên quan đến module khác (xem Mục 27 — Cross-module) — dữ liệu sau import hiển thị đúng ở các module liên quan
- Import hàng loạt có kích hoạt thông báo không (nếu nghiệp vụ yêu cầu) — xem Mục 18

### 20.6. Phân quyền Import/Export hàng loạt
- Vai trò có quyền Import/Export hàng loạt — thực hiện được
- Vai trò không có quyền — nút bị ẩn/khóa, gọi API trực tiếp cũng bị từ chối
- Hành động Import/Export hàng loạt được ghi nhận vào nhật ký hệ thống — ghi rõ người thực hiện, thời gian, số lượng bản ghi bị ảnh hưởng (xem Mục 8.6)

---

## 21. Kiểm tra giao diện Responsive / Cross-platform (Web ↔ Mobile)

> **Điều kiện áp dụng:** Nhóm này **chỉ áp dụng cho module/màn hình có hỗ trợ Mobile** (responsive web trên trình duyệt mobile, hoặc có app/màn hình mobile riêng). **Không áp dụng** với các module thuần desktop/web nội bộ không có yêu cầu hiển thị trên mobile — với các module đó, bỏ qua toàn bộ Mục 21 và không tính là thiếu sót khi rà soát coverage.
>
> Trước khi áp dụng nhóm này, xác nhận trong tài liệu nghiệp vụ hoặc với BA/PO: màn hình đang test có nằm trong phạm vi hỗ trợ Mobile hay không.

### 21.1. Bố cục & hiển thị responsive
- Giao diện hiển thị đúng bố cục trên kích thước màn hình mobile (không bị vỡ layout, không bị che/chồng lấp giữa các control)
- Các trường nhập liệu, nút bấm tự động điều chỉnh kích thước/vị trí phù hợp với màn hình nhỏ (không bị tràn ra ngoài viewport)
- Văn bản dài (label, thông báo lỗi, nội dung ô nhập liệu nhiều dòng) tự động xuống dòng hoặc cắt gọn đúng quy tắc, không bị tràn layout
- Bảng dữ liệu (danh sách) hiển thị đúng trên mobile — tự động chuyển sang dạng cuộn ngang, dạng thẻ (card), hoặc ẩn cột phụ theo đúng thiết kế
- Hình ảnh/tệp đính kèm hiển thị đúng kích thước, không bị vỡ tỷ lệ trên màn hình nhỏ

### 21.2. Tương tác đặc thù trên Mobile
- Bàn phím ảo (virtual keyboard) hiện đúng loại theo kiểu dữ liệu của trường (bàn phím số cho Trường số, bàn phím ngày cho Chọn ngày)
- Bàn phím ảo không che mất trường đang nhập hoặc nút Lưu/Gửi
- Cảm ứng (tap) hoạt động chính xác trên các control nhỏ (checkbox, radio button, icon) — vùng chạm đủ lớn để không bấm nhầm sang control liền kề
- Vuốt (swipe), kéo-thả (drag), cuộn (scroll) hoạt động đúng nếu màn hình có sử dụng các thao tác này (ví dụ: vuốt để xóa, kéo sắp xếp danh sách)
- Mở Chọn ngày/Danh sách chọn hiển thị đúng dạng picker phù hợp với nền tảng mobile (không bị che bởi bàn phím hoặc tràn màn hình)
- Popup xác nhận (xóa, lưu, cảnh báo) hiển thị đúng vị trí, đầy đủ nội dung và nút bấm trên màn hình nhỏ

### 21.3. Xoay màn hình (Orientation)
- Giao diện hiển thị đúng ở chế độ dọc (portrait)
- Giao diện hiển thị đúng ở chế độ ngang (landscape), nếu màn hình cho phép xoay
- Xoay màn hình giữa lúc đang nhập dữ liệu — không làm mất dữ liệu đã nhập, không làm mất focus một cách bất thường

### 21.4. Đồng nhất hành vi giữa Web và Mobile
- Cùng một luồng nghiệp vụ (ví dụ: tạo mới, chỉnh sửa, xóa) cho kết quả giống nhau khi thực hiện trên Web và trên Mobile
- Quy tắc validate dữ liệu (định dạng, giá trị biên, bắt buộc...) áp dụng nhất quán trên cả hai nền tảng — không có trường hợp Web chặn nhưng Mobile cho qua hoặc ngược lại
- Dữ liệu tạo/sửa trên Mobile hiển thị đúng khi mở lại trên Web (và ngược lại)
- Thông báo lỗi, label, placeholder hiển thị nội dung giống nhau (chỉ khác cách trình bày do giới hạn không gian màn hình) trên cả hai nền tảng

### 21.5. Hiệu năng tải trên môi trường mobile (mức thủ công)
- Thời gian tải màn hình/dữ liệu trên kết nối mạng di động (3G/4G mô phỏng qua DevTools) ở mức chấp nhận được, có hiển thị trạng thái loading rõ ràng
- Màn hình không bị treo/giật khi cuộn danh sách dài trên thiết bị mobile

---

## 22. Yêu cầu bắt buộc

- Không bỏ sót testcase theo checklist của từng loại control.
- Không gộp nhiều validation vào cùng một testcase.
- Mỗi testcase chỉ kiểm tra một mục tiêu.
- Nếu phát hiện control đặc biệt (Lookup, Upload, Multi Select, Auto Complete, Tree Select...) thì phải tự động sinh thêm testcase tương ứng.
- Trước khi hoàn thành, rà soát lại để đảm bảo đủ các nhóm kiểm thử bắt buộc theo Mục 1.5, và đã bao gồm Mục 4 (Bộ lọc & Tìm kiếm) nếu màn hình Danh sách có chức năng lọc/tìm kiếm.
- Khi viết file testcase sẽ chỉ viết từ phần Tổng hợp số lượng testcase và tới Danh sách testcase, không viết thừa thêm các mục mô tả khác.

---
## 23.Tổng hợp số lượng testcase theo mức độ ưu tiên

| Ưu tiên | Số TC |
|---|---|
| High (P0) | [số lượng] |
| Medium (P1) | [số lượng] |
| Low (P2) | [số lượng] |
---

## 24. Mẫu danh sách test case

| ID | Mục đích kiểm thử | Tiền điều kiện | Các bước thực hiện | Kết quả mong muốn | Kết quả thực tế | Mức độ ưu tiên | Automation Status | Automation Link | Ghi chú | Mã SRS |
|---|---|---|---|---|---|---|---|---|---|---|
| TC-[Mã]-001 | [Mô tả testcase] | [Tiền điều kiện] | 1. [Bước 1]<br>2. [Bước 2]<br>3. [Bước 3] | [Kết quả mong muốn chi tiết] | | P0 | ✅ Automated | e2e/[module]/[screen].spec.ts | | [Mã yêu cầu] |
| TC-[Mã]-002 | [Mô tả testcase] | [Tiền điều kiện] | 1. [Bước 1]<br>2. [Bước 2]<br>3. [Bước 3] | [Kết quả mong muốn chi tiết] | | P1 | ✅ Automated | api/[module].test.ts | | [Mã yêu cầu] |
| TC-[Mã]-003 | [Mô tả testcase] | [Tiền điều kiện] | 1. [Bước 1]<br>2. [Bước 2]<br>3. [Bước 3] | [Kết quả mong muốn chi tiết] | | P1 | 🔵 Manual only | — | | [Mã yêu cầu] |
| TC-[Mã]-004 | [Mô tả testcase] | [Tiền điều kiện] | 1. [Bước 1]<br>2. [Bước 2]<br>3. [Bước 3] | [Kết quả mong muốn chi tiết] | | P2 | ⏳ Planned | — | Sprint 3 | [Mã yêu cầu] |

**Quy tắc điền các cột:**

| Cột | Quy tắc |
|---|---|
| **Kết quả thực tế** | **Để trống khi viết testcase.** Người thực thi điền `P` (Pass) hoặc `F` (Fail) sau khi chạy |
| **Mức độ ưu tiên** | Ghi `P0` / `P1` / `P2` — xem bảng quy đổi bên dưới |
| **Ghi chú** | **Chỉ điền khi có điều cần lưu ý thật sự** (phát hiện nghiêm trọng, yêu cầu công cụ đặc biệt, tham số chưa chốt). Không có gì đặc biệt thì để trống, tránh làm rối bảng |
| **Mã SRS** | Mã yêu cầu trong tài liệu nghiệp vụ mà case này kiểm chứng. Dùng để dựng ma trận truy vết. Case do QA tự bổ sung, không bám mã nào thì ghi `[QA-ADD]` |

### Quy tắc mức độ ưu tiên

| Mức độ | Ghi trong bảng | Tiêu chí |
|---|---|---|
| **High** | `P0` | Luồng nghiệp vụ chính, Tạo mới dữ liệu, Chỉnh sửa dữ liệu, Xóa dữ liệu, Lưu dữ liệu, Phân quyền, Điều kiện nghiệp vụ quan trọng |
| **Medium** | `P1` | Validation dữ liệu, Giá trị biên, Trạng thái giao diện, Cấu hình hệ thống |
| **Low** | `P2` | Hiển thị giao diện, Responsive, Trường hợp hiếm gặp, Trường hợp ít ảnh hưởng đến nghiệp vụ |

**Luật nâng bậc — luôn thắng bảng trên.** Một case được đẩy lên `P0` bất kể xếp loại ban đầu, nếu nó chạm vào **tiền** (số tiền sai, tạo trùng giao dịch), **an toàn người dùng**, **rò rỉ dữ liệu**, hoặc **mất dữ liệu**.

### Quy tắc cột Automation Status

| Giá trị | Ý nghĩa | Khi nào dùng |
|---|---|---|
| ✅ Automated | Đã có test automation tương ứng | Đã viết xong script, đang chạy trong CI/CD |
| ⏳ Planned | Dự kiến sẽ automate | Đã lên kế hoạch nhưng chưa viết script |
| 🔵 Manual only | Chỉ test tay, không automate | Thao tác cảm quan, exploratory, quá khó automate ổn định |
| ❌ Cannot automate | Không thể automate | Phụ thuộc phần cứng, cảm giác người dùng, môi trường đặc thù không thể tái tạo |

### Quy tắc cột Automation Link

- Với case **✅ Automated**: ghi đường dẫn tương đối tới file test trong repo (ví dụ `e2e/category/create.spec.ts#L45`) hoặc tên test function nếu không có dòng cố định
- Với case **⏳ Planned**: ghi tên file dự kiến hoặc link ticket/task automation tương ứng
- Với case **🔵 Manual only** hoặc **❌ Cannot automate**: để `—`
- Cột này là **cầu nối** giữa file manual này và file `QA-Automation-Checklist.md` — xem file automation để biết chi tiết layer (E2E/API/Security...) và cấu trúc script tương ứng

---

## 25. Kiểm tra chuyển đổi trạng thái (State Transition Testing)

> Áp dụng cho mọi chức năng có **trạng thái thay đổi động** (trạng thái bản ghi, vai trò người dùng, điều kiện nghiệp vụ) khi thao tác theo thứ tự khác nhau có thể dẫn đến kết quả khác nhau. Đây là loại bug thường bị bỏ sót nhất vì chỉ xuất hiện khi thực hiện thao tác **ngoài thứ tự bình thường** mà tài liệu đặc tả không đề cập tường minh.
>
> **Dấu hiệu nhận biết cần áp dụng Mục này:** nghiệp vụ có các từ khóa như "chỉ được phép khi...", "sau khi được gán...", "không được thực hiện khi đang ở trạng thái...", "tự động bị hủy nếu...".

### 25.1. Thứ tự thao tác ngược (Reverse Order)

> Loại bug xảy ra khi người dùng thực hiện B trước rồi A sau, trong khi nghiệp vụ chỉ kiểm soát A → B.

- Xác định các cặp thao tác có quan hệ điều kiện (A phải xảy ra trước B): liệt kê tất cả cặp liên quan trong nghiệp vụ đang test
- **Luồng bình thường (A → B):** thực hiện A trước → hệ thống áp điều kiện → B bị chặn đúng theo nghiệp vụ
- **Luồng đảo ngược (B → A):** thực hiện B trước khi A xảy ra → sau đó áp A → hệ thống **phải rà soát lại và xử lý đúng**, không cho phép B tiếp tục có hiệu lực nếu không còn thỏa điều kiện

*Ví dụ minh họa cách tư duy (không phải case cứng):*
```
Nghiệp vụ: "Vai trò X không được phép thực hiện hành động Y"
Luồng bình thường:  Gán vai trò X → Thử hành động Y → Bị chặn ✓
Luồng đảo ngược:    Thực hiện Y trước → Sau đó gán vai trò X → Y đã thực hiện có còn hợp lệ không?
                    → Hệ thống phải rà soát lại và xử lý tương ứng (hủy, cảnh báo, giữ nguyên có log)
```

### 25.2. Thay đổi trạng thái sau khi đã thực hiện (Post-action State Change)

> Loại bug xảy ra khi điều kiện thay đổi sau khi thao tác đã được thực hiện thành công — hệ thống không rà soát lại các thao tác đã tồn tại.

- Thực hiện thao tác X thành công → sau đó điều kiện ràng buộc thay đổi (trạng thái bản ghi, vai trò, cấu hình) → hệ thống **phải xử lý đúng** các thao tác đã tồn tại theo quy tắc nghiệp vụ (giữ nguyên có cảnh báo, hủy tự động, yêu cầu xác nhận lại)
- Thay đổi điều kiện ràng buộc → hệ thống **không im lặng** giữ nguyên trạng thái cũ mà không thông báo (nếu nghiệp vụ yêu cầu phải xử lý)
- Dữ liệu hoặc quyền đã được cấp trước đó không bị "trôi nổi" tự do sau khi điều kiện ban đầu không còn hợp lệ

### 25.3. Thay đổi trạng thái từ module/màn hình khác (Cross-module State Change)

> Loại bug xảy ra khi Module A thay đổi dữ liệu/điều kiện nhưng Module B không cập nhật validate tương ứng.

- Thay đổi điều kiện ràng buộc ở **Module A** → mở màn hình liên quan ở **Module B** → Module B phải phản ánh đúng điều kiện mới, không dùng điều kiện cũ đã cache
- Thực hiện thao tác ở Module B ngay sau khi Module A thay đổi điều kiện (không tải lại trang) → kết quả đúng theo điều kiện mới nhất, không dựa vào trạng thái cũ còn trong bộ nhớ trình duyệt
- Khi 2 người dùng cùng tương tác: người dùng 1 thay đổi điều kiện → người dùng 2 đang thao tác dựa trên điều kiện cũ → hệ thống xử lý xung đột đúng (thông báo, từ chối, hoặc buộc tải lại)

### 25.4. Trạng thái trung gian và bị gián đoạn (Intermediate & Interrupted State)

> Loại bug xảy ra khi luồng nhiều bước bị gián đoạn giữa chừng — hệ thống xử lý không nhất quán với trạng thái đang dở dang.

- Bắt đầu thực hiện luồng nhiều bước → gián đoạn giữa chừng (đóng tab, mất mạng, hết session) → mở lại → hệ thống xử lý đúng (tiếp tục từ bước đang dở, hoặc hủy và bắt đầu lại, không để trạng thái nửa vời)
- Điều kiện thay đổi **trong lúc đang thực hiện** bước giữa của luồng nhiều bước → kết quả cuối cùng đúng theo điều kiện tại thời điểm hoàn thành, không bị ảnh hưởng bởi điều kiện đã thay đổi giữa lúc đang làm
- Dữ liệu không bị lưu một phần (partial save) khi luồng bị gián đoạn sau khi đã vượt qua một số bước — xem thêm Mục 7.3 (Toàn vẹn dữ liệu)

### 25.5. Checklist câu hỏi — Nhận diện case cần test

Khi phân tích nghiệp vụ, dùng các câu hỏi dưới đây để xác định có cần sinh case State Transition không:

| Câu hỏi | Nếu trả lời CÓ → cần sinh case |
|---|---|
| Chức năng có trạng thái bản ghi thay đổi theo thời gian? | Case 24.1 + 24.2 |
| Có vai trò/quyền người dùng có thể thay đổi sau khi đã thực hiện thao tác? | Case 24.1 + 24.2 |
| Có điều kiện ràng buộc phụ thuộc vào module/màn hình khác? | Case 24.3 |
| Luồng thực hiện có nhiều bước và có thể bị gián đoạn? | Case 24.4 |
| Tài liệu có câu nào dạng "chỉ được phép khi...", "sau khi được gán...", "không được khi đang..."? | Tất cả case 24.x |
| Có thể thực hiện thao tác theo thứ tự khác với thứ tự bình thường tài liệu mô tả? | Case 24.1 |

### 25.6. Quy tắc viết testcase State Transition

Mỗi testcase State Transition phải nêu rõ trong **Tiền điều kiện** và **Các bước thực hiện**:

1. **Tiền điều kiện:** mô tả rõ trạng thái ban đầu của hệ thống trước khi bắt đầu — không viết chung chung "đã đăng nhập" mà phải nêu đầy đủ trạng thái liên quan (ví dụ "tài khoản A chưa được gán vai trò X", "bản ghi Y đang ở trạng thái Z")
2. **Các bước:** liệt kê đúng thứ tự cần test — đặc biệt nhấn mạnh bước nào là "thao tác bất thường" (khác với luồng bình thường)
3. **Kết quả mong muốn:** mô tả rõ hệ thống phải xử lý thế nào — không chỉ "báo lỗi" mà phải nêu cụ thể: thông báo gì, dữ liệu nào bị ảnh hưởng, trạng thái cuối cùng là gì

**Mức độ ưu tiên:** luôn là **High** — vì đây là loại bug ảnh hưởng trực tiếp đến tính toàn vẹn nghiệp vụ, thường không được phát hiện ở test thông thường và hay xuất hiện ở production.

---

## 26. Kiểm tra Hoàn tác / Khôi phục thao tác (Rollback / Undo Testing)

> Áp dụng cho mọi chức năng có khả năng **hoàn tác một thao tác đã thực hiện** hoặc **khôi phục về một phiên bản dữ liệu trước đó** — dù là hoàn tác đơn giản (nút "Undo" sau khi xóa), hoàn tác nhiều bước (lịch sử phiên bản tài liệu), hay rollback tự động khi giao dịch thất bại giữa chừng. Nếu chức năng không có tính năng hoàn tác/khôi phục, bỏ qua toàn bộ mục này, không tính là thiếu sót.
>
> **Áp dụng đa domain** — một số ví dụ minh họa (không phải danh sách đầy đủ):
> - Trình soạn thảo tài liệu: Undo/Redo từng thao tác gõ phím, khôi phục phiên bản cũ
> - Quy trình duyệt (Workflow/Approval): thu hồi yêu cầu đã gửi trước khi được duyệt, trả về bước trước trong quy trình nhiều cấp
> - Giao dịch tài chính: hoàn tác giao dịch trong khoảng thời gian cho phép, rollback tự động khi 1 bước trong chuỗi giao dịch thất bại
> - Quản lý đơn hàng/booking: hủy đặt chỗ và khôi phục slot đã giữ, hoàn tác trạng thái đơn hàng về bước trước
> - Hệ thống có "Thùng rác" (Recycle bin): khôi phục dữ liệu đã xóa mềm — xem thêm Mục 10.3
>
> **Điều kiện áp dụng:** chức năng đang test có ít nhất 1 trong các dấu hiệu sau:
> - Có nút/hành động "Hoàn tác", "Undo", "Khôi phục", "Thu hồi" trong đặc tả
> - Hệ thống lưu lịch sử phiên bản (version history) của dữ liệu
> - Có giao dịch/quy trình nhiều bước cần rollback tự động khi 1 bước thất bại giữa chừng

### 26.0. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo nghiệp vụ thực tế) |
|---|---|
| Hoàn tác áp dụng cho hành động nào? (Xóa, Sửa, Duyệt, Chuyển trạng thái...) | `[Danh sách hành động có thể hoàn tác]` |
| Hoàn tác được **trong khoảng thời gian nào** hay **không giới hạn thời gian**? | `[Ví dụ: trong 30 giây sau khi xóa / bất kỳ lúc nào trước khi có thao tác khác]` |
| Hoàn tác **1 bước gần nhất** hay **nhiều bước** (về đúng phiên bản bất kỳ trong lịch sử)? | `[1 bước / N bước / về mốc bất kỳ]` |
| Sau khi hoàn tác, dữ liệu liên quan ở nơi khác có được khôi phục theo không? | `[Có/Không — nêu rõ phạm vi]` |
| Ai được phép hoàn tác? (chỉ người thực hiện thao tác gốc, hay bất kỳ ai có quyền) | `[Nêu rõ theo phân quyền — xem Mục 9]` |
| Hoàn tác có giới hạn số lần hoặc phụ thuộc điều kiện gì không? | `[Ví dụ: không hoàn tác được nếu đã có người khác thao tác tiếp theo]` |

### 26.1. Hoàn tác cơ bản (Basic Undo)

> **Câu hỏi nhận diện:** "Sau khi thực hiện [hành động X], người dùng có thể hoàn tác ngay lập tức không?"

- Thực hiện hành động → bấm Hoàn tác **ngay sau đó** → hệ thống khôi phục đúng về trạng thái/dữ liệu trước khi thực hiện hành động, không thiếu không thừa
- Thực hiện hành động → **không** bấm Hoàn tác trong thời gian cho phép (nếu có giới hạn thời gian) → hết thời gian, tùy chọn Hoàn tác biến mất/bị khóa, hành động trở thành vĩnh viễn
- Hoàn tác thành công → thông báo rõ ràng xác nhận đã khôi phục, danh sách/giao diện cập nhật đúng ngay
- Bấm Hoàn tác nhưng dữ liệu **không còn đủ điều kiện** để khôi phục (ví dụ bản ghi liên quan đã bị xóa bởi thao tác khác trong lúc chờ) → hệ thống báo lỗi rõ ràng, không hoàn tác một phần gây sai lệch dữ liệu

### 26.2. Hoàn tác nhiều bước / Khôi phục phiên bản (Multi-step Undo / Version Restore)

> **Câu hỏi nhận diện:** "Hệ thống có lưu lại nhiều phiên bản lịch sử của dữ liệu, và người dùng có thể chọn khôi phục về một mốc bất kỳ không?"

- Khôi phục về **phiên bản gần nhất** trước đó — dữ liệu đúng như phiên bản đó, không lẫn dữ liệu của phiên bản hiện tại
- Khôi phục về **phiên bản xa hơn** (bỏ qua nhiều phiên bản ở giữa) — dữ liệu đúng chính xác của phiên bản được chọn, không bị trộn lẫn các thay đổi ở giữa
- Sau khi khôi phục về phiên bản cũ, **các phiên bản đã bị bỏ qua** xử lý thế nào — bị xóa khỏi lịch sử, hay vẫn giữ lại và bản khôi phục trở thành phiên bản mới nhất (đúng theo thiết kế: linear history vs branching history)
- Khôi phục nhiều lần liên tiếp (khôi phục A → rồi lại khôi phục về B) — mỗi lần đều đúng, lịch sử phiên bản được ghi nhận đúng, không bị lẫn lộn
- Xem/so sánh sự khác biệt giữa 2 phiên bản (nếu có tính năng diff) — hiển thị đúng phần nào đã thay đổi

### 26.3. Rollback tự động khi giao dịch/quy trình thất bại giữa chừng

> **Câu hỏi nhận diện:** "Nếu một quy trình gồm nhiều bước, và 1 bước ở giữa thất bại, các bước đã thực hiện trước đó có bị hoàn tác không?"

- Quy trình nhiều bước thực hiện đến bước N thì thất bại → toàn bộ các thay đổi từ bước 1 đến bước N-1 được **rollback đúng** (all-or-nothing), không để lại dữ liệu nửa vời — liên quan Mục 7.3 (Toàn vẹn dữ liệu)
- Rollback tự động **thành công hoàn toàn** — hệ thống trở về đúng trạng thái trước khi bắt đầu quy trình, không có dữ liệu rác sót lại
- Rollback tự động **bản thân nó cũng thất bại** (ví dụ mất kết nối DB giữa lúc đang rollback) — hệ thống có cơ chế phát hiện và xử lý (retry, cảnh báo Admin, đánh dấu dữ liệu cần kiểm tra thủ công), không âm thầm để dữ liệu sai lệch
- Thông báo cho người dùng khi rollback xảy ra — rõ ràng về việc thao tác đã bị hủy hoàn toàn, không gây hiểu nhầm là đã thành công một phần

### 26.4. Hoàn tác và tương tác với module/người dùng khác

> **Câu hỏi nhận diện:** "Nếu dữ liệu đã bị thay đổi bởi người khác hoặc module khác sau hành động gốc, việc hoàn tác còn hợp lệ không?"

- Hoàn tác một hành động, nhưng **sau hành động đó** đã có người dùng khác thao tác tiếp trên cùng dữ liệu → hệ thống xử lý đúng theo nghiệp vụ: chặn hoàn tác kèm cảnh báo xung đột, hoặc cho hoàn tác nhưng cảnh báo rõ có thể ảnh hưởng đến thay đổi sau đó (liên quan Mục 16 — Concurrency)
- Hoàn tác dữ liệu đã được **đồng bộ/chia sẻ sang module khác** (xem Mục 27) — module khác có được cập nhật lại theo đúng dữ liệu đã hoàn tác không, hay giữ nguyên bản đã chia sẻ trước đó (cần xác nhận theo đúng nghiệp vụ "sống hay đóng băng" — xem Mục 27.4)
- Hoàn tác một hành động đã **kích hoạt thông báo** (email, SMS đã gửi) — hệ thống không thể thu hồi thông báo đã gửi, nhưng cần xử lý đúng phần dữ liệu còn kiểm soát được, và có thể cần gửi thông báo mới về việc đã hoàn tác

### 26.5. Phân quyền hoàn tác

- Chỉ người **thực hiện hành động gốc** được hoàn tác (nếu nghiệp vụ giới hạn) — người khác không thấy hoặc không dùng được tùy chọn hoàn tác
- Vai trò đặc biệt (Admin) có thể hoàn tác hành động của người khác (nếu nghiệp vụ cho phép) — thực hiện được, có ghi log rõ ai hoàn tác hành động của ai
- Hoàn tác được ghi nhận vào nhật ký hệ thống — ghi rõ hành động gốc, người hoàn tác, thời điểm, dữ liệu trước/sau hoàn tác (liên quan Mục 8.6)

### 26.6. Checklist câu hỏi nhận diện — Cần sinh case Rollback/Undo không?

| Câu hỏi | Nếu CÓ → sinh case |
|---|---|
| Có nút/hành động "Hoàn tác", "Undo", "Khôi phục" trong đặc tả không? | 26.1 |
| Hệ thống có lưu lịch sử nhiều phiên bản dữ liệu không? | 26.2 |
| Có quy trình/giao dịch nhiều bước cần đảm bảo toàn vẹn nếu 1 bước thất bại không? | 26.3 |
| Dữ liệu có thể bị thay đổi bởi người khác/module khác trong lúc chờ hoàn tác không? | 26.4 |
| Việc hoàn tác có giới hạn theo vai trò không? | 26.5 |

### 26.7. Quy tắc viết testcase Rollback/Undo

**Tiền điều kiện** phải nêu rõ trạng thái dữ liệu **trước** hành động gốc, để có thể so sánh chính xác sau khi hoàn tác:
```
Đúng:  "Bản ghi X đang có giá trị Tên = 'ABC', Trạng thái = 'Hoạt động'.
        Thực hiện sửa Tên thành 'XYZ' trước khi test hoàn tác."

Sai:   "Đã sửa dữ liệu."
```

**Kết quả mong muốn** phải khẳng định rõ dữ liệu sau hoàn tác **khớp chính xác** với trạng thái trước hành động gốc — không chỉ nói "khôi phục thành công":
```
Đúng:  "Sau khi hoàn tác, Tên = 'ABC' (khớp đúng giá trị trước khi sửa),
        Trạng thái = 'Hoạt động' (không đổi), thời gian cập nhật (updatedAt)
        phản ánh đúng lần hoàn tác vừa thực hiện."
```

**Mức độ ưu tiên:** luôn là **High** — lỗi rollback/undo thường dẫn đến sai lệch dữ liệu âm thầm, khó phát hiện ngay lập tức và ảnh hưởng đến tính toàn vẹn dữ liệu về lâu dài.

---

## 27. Kiểm tra luồng nghiệp vụ xuyên module (Cross-module Integration Testing)

> Áp dụng khi hệ thống có **nhiều module/portal/actor** phối hợp với nhau để hoàn thành một nghiệp vụ — dữ liệu được tạo ở module A, dùng ở module B, hiển thị ở module C. Khác với Mục 12 (đồng bộ dữ liệu kỹ thuật), Mục 27 tập trung vào **luồng nghiệp vụ từ đầu đến cuối** theo góc nhìn người dùng thực tế.
>
> **Điều kiện áp dụng:** chức năng đang test có ít nhất 1 trong các dấu hiệu sau:
> - Dữ liệu tạo ở module này được dùng làm dữ liệu đầu vào ở module khác
> - Nhiều loại dữ liệu từ nhiều nơi phải sẵn sàng trước thì mới thực hiện được một nghiệp vụ
> - Hành động ở module A làm thay đổi hiển thị/trạng thái ở module B hoặc C
>
> **Trước khi gen testcase Mục 27:** bắt buộc đọc `module-map.md` và `actor-overview.md` để hiểu luồng dữ liệu tổng thể. Nếu chưa có, hỏi BA/PO và điền vào Bảng thông tin Mục 27.0 trước khi viết case.

### 27.0. Bảng thông tin cần xác định trước khi viết case tích hợp

| Câu hỏi | Trả lời (điền theo hệ thống thực tế) |
|---|---|
| Có bao nhiêu module/portal liên quan? | `[Module A, Module B, Module C...]` |
| Dữ liệu chảy theo hướng nào? | `[A → B → C / A ↔ B / chỉ 1 chiều]` |
| Dữ liệu tiền đề nào phải có trước? | `[Danh sách dữ liệu cần setup trước khi test luồng]` |
| Xóa dữ liệu ở tầng trên, tầng dưới xử lý thế nào? | `[Cascade delete / Restrict / Set null / theo nghiệp vụ]` |
| Vai trò nào thấy dữ liệu theo cách khác nhau? | `[Role A thấy X, Role B thấy Y trên cùng bản ghi]` |
| Hành động ở module nào kích hoạt thông báo cho module nào? | `[Module A hành động → Module B và C nhận thông báo]` |

### 27.1. Vertical Data Flow — Dữ liệu chảy xuống theo nhiều tầng

> Pattern: Dữ liệu được tạo ở tầng trên (Admin/CMS) → dùng làm nguồn ở tầng giữa (Staff/Partner) → hiển thị ở tầng dưới (End user/Customer).
>
> **Câu hỏi nhận diện:** "Nếu tôi không tạo [dữ liệu X] ở [Module A], thì [Module B] có thể làm gì không?"

- Dữ liệu tầng trên được tạo với trạng thái **kích hoạt** → tầng dưới thấy đúng và có thể dùng
- Dữ liệu tầng trên được tạo với trạng thái **chưa kích hoạt** → tầng dưới **không thấy**, không thể dùng
- Dữ liệu tầng trên bị **vô hiệu hóa sau khi** tầng dưới đã dùng → tầng dưới xử lý đúng (hiển thị cảnh báo, khóa chức năng, hoặc tiếp tục theo nghiệp vụ)
- Dữ liệu tầng trên bị **xóa** khi tầng dưới đang tham chiếu → hệ thống chặn xóa hoặc xử lý cascade đúng, không để dữ liệu tầng dưới bị "mồ côi" (orphan)
- Sửa dữ liệu ở tầng trên → tầng dưới phản ánh đúng thay đổi (hoặc giữ bản cũ nếu đã "đóng băng" — xem Mục 12.5)
- Dữ liệu từ tầng trên khi xuất hiện ở tầng dưới **chỉ hiển thị đúng tập trường được phép** (không lộ trường nội bộ)

### 27.2. Prerequisite Dependency Chain — Chuỗi dữ liệu tiền đề

> Pattern: Để làm được nghiệp vụ X, phải có dữ liệu A + B + C sẵn sàng trước. Thiếu 1 thứ → X không làm được.
>
> **Câu hỏi nhận diện:** "Cần chuẩn bị những gì trước khi tạo/thực hiện [nghiệp vụ này]?"

- Thực hiện nghiệp vụ khi **đủ tất cả** dữ liệu tiền đề → thành công
- Thực hiện nghiệp vụ khi **thiếu 1 trong N** dữ liệu tiền đề → hệ thống chặn và thông báo rõ **thiếu cái gì**, không để người dùng tự đoán
- Thực hiện nghiệp vụ khi **thiếu nhiều** dữ liệu tiền đề → thông báo liệt kê đủ những gì còn thiếu (không chỉ báo lỗi đầu tiên rồi dừng)
- Dữ liệu tiền đề đã có nhưng ở **trạng thái không hợp lệ** (vô hiệu, đang xử lý, bị khóa) → hệ thống nhận diện và báo đúng trạng thái, không báo "không tìm thấy"
- Sau khi xóa/vô hiệu hóa dữ liệu tiền đề → các nghiệp vụ đang phụ thuộc vào nó được xử lý đúng (chặn thực hiện mới, cảnh báo bản ghi hiện tại, hoặc theo nghiệp vụ)

### 27.3. Cascade Delete / Broken Reference — Phá một thứ, kiểm tra tác động lan rộng

> Pattern: Xóa hoặc vô hiệu hóa dữ liệu ở module A → kiểm tra tác động lan đến module B, C.
>
> **Câu hỏi nhận diện:** "Nếu tôi xóa [dữ liệu X], những thứ nào khác trong hệ thống đang dùng nó sẽ bị ảnh hưởng?"

- Xóa bản ghi **đang được tham chiếu** ở module khác → hệ thống chặn xóa và nêu rõ lý do (bao nhiêu bản ghi khác đang dùng), hoặc cascade xóa theo nếu nghiệp vụ cho phép
- Vô hiệu hóa (không xóa) bản ghi đang được tham chiếu → các bản ghi đang dùng nó hiển thị đúng trạng thái (cảnh báo, đánh dấu không hợp lệ, hoặc tiếp tục bình thường tùy nghiệp vụ)
- Sau khi xóa cascade thành công → kiểm tra **không còn dữ liệu orphan** ở bất kỳ module nào (dữ liệu con mà bản ghi cha đã bị xóa)
- Khôi phục bản ghi đã xóa mềm (nếu hệ thống hỗ trợ) → các tham chiếu từ module khác phục hồi đúng

### 27.4. Bidirectional Sync — Đồng bộ 2 chiều và câu hỏi "sống hay đóng băng"

> Pattern: Dữ liệu đã được chia sẻ sang module khác, sau đó bị sửa ở nguồn — module đích cập nhật theo hay giữ bản cũ?
>
> **Câu hỏi nhận diện:** "Nếu dữ liệu đã được dùng/chia sẻ rồi mà bị sửa ở nguồn, điều gì xảy ra?"

- Sửa dữ liệu nguồn **trước khi** chia sẻ/sử dụng → module đích thấy bản mới nhất ✓ (expected)
- Sửa dữ liệu nguồn **sau khi** đã chia sẻ → module đích **phải cập nhật theo** (nếu dữ liệu "sống") hoặc **giữ nguyên bản đã chia sẻ** (nếu "đóng băng") — đây là quyết định nghiệp vụ cần xác nhận rõ trong SRS trước khi viết kết quả mong muốn
- Dữ liệu hiển thị **nhất quán** ở tất cả nơi tham chiếu — không xảy ra trường hợp module A thấy bản mới, module B vẫn thấy bản cũ
- Sửa đồng thời ở cả 2 phía (nếu có thể) → hệ thống xử lý xung đột đúng, không để lost update

### 27.5. Role-based Data Visibility — Cùng bản ghi, nhìn từ vai trò khác thấy khác nhau

> Pattern: Không phải ai có/không có quyền truy cập — mà là cùng một bản ghi, nhưng mỗi vai trò thấy tập thông tin **khác nhau**.
> Khác với Mục 9 (Phân quyền CRUD — ai được làm gì), Mục 27.5 kiểm tra **nội dung hiển thị khác nhau** cho từng vai trò.
>
> **Câu hỏi nhận diện:** "Với bản ghi này, vai trò A thấy những trường nào? Vai trò B thấy những trường nào khác?"

- Với cùng một bản ghi: mỗi vai trò thấy đúng **tập trường được phép** theo nghiệp vụ, không thừa không thiếu
- Trường nhạy cảm/nội bộ (giá gốc, thông tin cá nhân đầy đủ, ghi chú nội bộ) **không lộ** ra với vai trò không được phép, kể cả khi truy cập trực tiếp qua URL/API
- Dữ liệu được **tính toán/hiển thị khác nhau** có chủ đích giữa các vai trò (ví dụ: Admin thấy giá gốc, Customer thấy giá sau thuế) — tính toán đúng cho từng vai trò
- Khi một vai trò sửa trường mà vai trò khác không thấy → vai trò không thấy không bị ảnh hưởng bởi thay đổi đó

### 27.6. Cross-portal Notification Chain — Hành động ở portal A kích hoạt thông báo ở portal B, C

> Pattern: Người dùng ở portal A thực hiện hành động → hệ thống tự động gửi thông báo đến người dùng ở portal B và/hoặc C.
> Liên quan đến Mục 18 (Notification Trigger đơn lẻ) nhưng Mục 27.6 kiểm tra **chuỗi thông báo xuyên portal**.
>
> **Câu hỏi nhận diện:** "Khi [actor A] thực hiện [hành động X], [actor B] và [actor C] sẽ nhận được thông báo gì?"

- Hành động ở portal A → tất cả actor nhận thông báo theo đúng danh sách nghiệp vụ quy định (không thiếu ai, không gửi nhầm)
- Nội dung thông báo mỗi actor nhận **phù hợp với vai trò** đó (Admin nhận nội dung đầy đủ, Customer nhận nội dung rút gọn)
- Thứ tự thông báo đúng theo nghiệp vụ (nếu có quy định thứ tự ưu tiên)
- Khi 1 bước trong chuỗi thông báo thất bại → các bước còn lại xử lý thế nào (tiếp tục gửi hay dừng hết)
- Không gửi thông báo trùng lặp khi cùng sự kiện xảy ra nhiều lần liên tiếp (idempotent)

### 27.7. Checklist câu hỏi nhận diện — Cần sinh case Cross-module không?

| Câu hỏi | Nếu CÓ → sinh case |
|---|---|
| Dữ liệu tạo ở module này có được dùng làm dữ liệu đầu vào ở module khác không? | 25.1 + 25.2 |
| Để thực hiện nghiệp vụ này, cần nhiều loại dữ liệu từ nhiều nơi khác nhau không? | 25.2 |
| Nếu xóa/sửa/vô hiệu dữ liệu ở module A, module B có bị ảnh hưởng không? | 25.3 + 25.4 |
| Cùng một bản ghi, các vai trò khác nhau có nhìn thấy thông tin khác nhau không? | 25.5 |
| Hành động ở portal này có kích hoạt thông báo đến portal khác không? | 25.6 |
| SRS có mô tả luồng liên quan đến nhiều hơn 1 actor/portal không? | Tất cả 25.x |

### 27.8. Quy tắc viết testcase Cross-module

**Tiền điều kiện** phải mô tả đầy đủ trạng thái của **tất cả** module liên quan — không chỉ module đang test:
```
Đúng:  "Module CMS đã có danh mục 'Bất động sản' trạng thái Hoạt động.
        Partner A đã có tài khoản nhận tiền và thành viên ban tổ chức.
        Chưa có tài sản nào được tạo."

Sai:   "Đã đăng nhập Partner."
```

**Các bước** phải ghi rõ **chuyển đổi giữa portal** — ai làm gì ở đâu:
```
1. [CMS Admin] Tạo danh mục "Bất động sản", trạng thái Hoạt động
2. [Partner] Đăng nhập portal Partner, vào màn Tạo tài sản
3. [Partner] Kiểm tra dropdown Danh mục
```

**Kết quả mong muốn** phải nêu kết quả ở **từng module** có liên quan, không chỉ module cuối:
```
- [Portal Partner] Dropdown hiển thị "Bất động sản"
- [Portal Customer] Chưa thấy tài sản (chưa được công bố)
- [CMS] Danh mục vẫn hiển thị đúng trạng thái Hoạt động
```

**Mức độ ưu tiên:** luôn là **High** — bug tích hợp xuyên module thường ảnh hưởng nghiêm trọng đến nghiệp vụ và khó phát hiện khi test từng module riêng lẻ.

---

## 28. Kiểm tra tác vụ theo thời gian (Time-based / Schedule Testing)

> Áp dụng cho mọi chức năng có **hành vi tự động kích hoạt theo thời gian** — không cần người dùng thao tác, hệ thống tự chuyển trạng thái khi đến một mốc thời gian nhất định. Đây là loại case thường bị bỏ sót vì khó test bằng thao tác tay thông thường (phải chờ đúng thời điểm) và dễ có bug tại đúng ranh giới thời gian.
>
> **Áp dụng đa domain — không giới hạn ở một nghiệp vụ cụ thể.** Một số ví dụ minh họa (không phải danh sách đầy đủ):
> - Đấu giá: đến giờ mở phiên đấu giá, tự động gia hạn khi có người đặt giá phút chót, tự động đóng phiên khi hết giờ
> - Đặt lịch/giao hàng (booking, logistics): đến giờ hẹn giao tự động chuyển trạng thái "Đang giao", quá giờ hẹn mà chưa xử lý tự động báo trễ
> - HRM: tự động khóa tài khoản sau N ngày nghỉ không lương, tự động tính phép còn lại vào đầu kỳ
> - Thương mại điện tử: flash sale tự động mở/đóng theo khung giờ, mã giảm giá tự động hết hạn
> - Hợp đồng/tài chính: tự động nhắc thanh toán trước hạn N ngày, tự động chuyển trạng thái quá hạn
>
> **Điều kiện áp dụng:** chức năng đang test có ít nhất 1 trong các dấu hiệu sau:
> - Có mốc thời gian cố định hoặc do người dùng thiết lập, đến giờ hệ thống tự động thực hiện hành động
> - Có điều kiện "nếu xảy ra sự kiện X trong khoảng thời gian gần mốc kết thúc, thời gian kết thúc được gia hạn"
> - Có countdown/đếm ngược hiển thị cho người dùng
> - Có tác vụ chạy nền theo lịch (cron job, scheduled job) không gắn với hành động trực tiếp của người dùng

### 28.0. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo nghiệp vụ thực tế) |
|---|---|
| Mốc thời gian kích hoạt là gì? (cố định hay do người dùng đặt) | `[Ví dụ: giờ mở phiên do Admin đặt / giờ hẹn do khách chọn]` |
| Hành động tự động khi đến mốc là gì? | `[Ví dụ: chuyển trạng thái, gửi thông báo, khóa chức năng]` |
| Có điều kiện gia hạn không? Điều kiện gia hạn là gì? | `[Ví dụ: có người đặt giá trong X phút cuối → +Y phút]` |
| Gia hạn có giới hạn số lần / tổng thời gian tối đa không? | `[Ví dụ: tối đa gia hạn 5 lần / tổng không quá 30 phút]` |
| Thời gian tính theo múi giờ nào? (server hay client) | `[Ví dụ: server UTC+7, hiển thị theo múi giờ client]` |
| Nếu hệ thống down đúng lúc trigger, xử lý thế nào khi phục hồi? | `[Ví dụ: chạy bù ngay khi phục hồi / bỏ qua / cảnh báo Admin]` |

### 28.1. Kích hoạt theo lịch (Scheduled Activation)

> **Câu hỏi nhận diện:** "Có mốc thời gian nào mà khi đến giờ, hệ thống tự chuyển trạng thái mà không cần ai bấm gì không?"

- Đến đúng mốc thời gian kích hoạt — hệ thống tự động chuyển trạng thái đúng, không cần thao tác thủ công
- Trước mốc thời gian kích hoạt (dù chỉ 1 giây) — trạng thái vẫn ở mức chưa kích hoạt, chức năng liên quan chưa khả dụng
- Ngay tại thời điểm biên (đúng giây/phút kích hoạt) — không có độ trễ vượt quá ngưỡng cho phép giữa thời gian đặt và thời gian thực tế kích hoạt
- Đặt mốc kích hoạt trong quá khứ (do lỗi nhập liệu hoặc nghiệp vụ cho phép) — hệ thống xử lý đúng (kích hoạt ngay, báo lỗi, hoặc chặn không cho đặt) theo đúng quy tắc
- Nhiều bản ghi có cùng mốc kích hoạt — tất cả được xử lý đúng và đầy đủ, không bị bỏ sót do xử lý hàng loạt

### 28.2. Tự động đóng / kết thúc theo lịch (Scheduled Auto-close / Expiry)

> **Câu hỏi nhận diện:** "Có mốc thời gian nào mà khi đến giờ, hệ thống tự động khóa/đóng/kết thúc một tiến trình đang mở không?"

- Đến đúng mốc thời gian kết thúc — hệ thống tự động chuyển sang trạng thái đã đóng/kết thúc, không cho phép thao tác tiếp tục
- Thao tác được gửi lên **đúng vào khoảnh khắc** hết giờ (ví dụ request đến server ở mili-giây cuối cùng) — hệ thống xử lý nhất quán theo một quy tắc rõ ràng (chấp nhận nếu request đến trước mốc, từ chối nếu sau — không random)
- Sau khi đã đóng — không thể thực hiện lại các hành động vốn chỉ hợp lệ khi đang mở (đặt giá, xác nhận, chỉnh sửa...)
- Trường hợp đóng do "không đủ điều kiện" (ví dụ hết giờ mà không đủ số lượng người tham gia tối thiểu) — hệ thống xử lý đúng luồng thất bại: hoàn tác dữ liệu liên quan, thông báo đúng đối tượng, trạng thái cuối cùng đúng (Hủy/Thất bại, không nhầm với Hoàn thành)
- Đóng thành công (đủ điều kiện) — trạng thái cuối cùng đúng (Hoàn thành/Thành công), dữ liệu kết quả được chốt đúng, không thể thay đổi sau đó (trừ khi nghiệp vụ cho phép)

### 28.3. Gia hạn tự động theo điều kiện (Auto-extend)

> **Câu hỏi nhận diện:** "Nếu có [sự kiện X] xảy ra gần đến giờ kết thúc, thời gian kết thúc có bị đẩy lùi không?"

- Sự kiện kích hoạt gia hạn xảy ra **trong khoảng thời gian được tính** (gần mốc kết thúc) — thời gian kết thúc được gia hạn đúng theo quy tắc (cộng thêm bao nhiêu, tính từ mốc nào)
- Sự kiện xảy ra **ngoài khoảng thời gian tính gia hạn** (còn quá sớm để tính) — không gia hạn, thời gian kết thúc giữ nguyên
- Sự kiện xảy ra **liên tiếp nhiều lần** trong khoảng gia hạn — kiểm tra đúng quy tắc: gia hạn cộng dồn từng lần, hay chỉ tính từ lần gần nhất
- Đạt **giới hạn tối đa** số lần gia hạn hoặc tổng thời gian gia hạn (nếu nghiệp vụ có giới hạn) — không gia hạn thêm dù điều kiện vẫn thỏa, hệ thống xử lý đóng đúng hạn cuối
- Countdown/đồng hồ đếm ngược hiển thị **cập nhật ngay** sau khi gia hạn — không hiển thị sai thời gian cũ dù chỉ trong khoảnh khắc
- Nhiều người dùng cùng kích hoạt điều kiện gia hạn **gần như đồng thời** — chỉ tính gia hạn đúng 1 lần hoặc đúng theo quy tắc, không bị cộng dồn sai do race condition (liên quan Mục 16 — Concurrency)

### 28.4. Đồng hồ đếm ngược & hiển thị thời gian thực

> **Câu hỏi nhận diện:** "Có đồng hồ đếm ngược hoặc hiển thị thời gian còn lại cho người dùng không?"

- Đồng hồ đếm ngược hiển thị đúng, giảm dần theo thời gian thực, không bị đứng yên hoặc nhảy số bất thường
- Đồng hồ đếm ngược dựa trên **thời gian server**, không phải thời gian máy khách hàng (tránh trường hợp người dùng chỉnh giờ máy để gian lận)
- Tải lại trang (F5) giữa lúc đang đếm ngược — đồng hồ hiển thị lại đúng thời gian còn lại thực tế, không reset về ban đầu
- Đồng hồ đếm ngược về đúng 0 — hành động tương ứng (đóng, chuyển trạng thái) được kích hoạt đúng lúc, không bị trễ hoặc sớm
- Nhiều người dùng xem cùng một đồng hồ đếm ngược ở các thiết bị khác nhau — tất cả hiển thị đồng bộ, sai lệch không vượt quá ngưỡng chấp nhận được

### 28.5. Múi giờ và đồng bộ thời gian Server–Client (Timezone & Clock Sync)

> **Câu hỏi nhận diện:** "Hệ thống có người dùng ở nhiều múi giờ khác nhau không? Thời gian hiển thị có bị lệch giữa các nơi không?"

- Người dùng ở múi giờ khác nhau xem cùng một mốc thời gian — mỗi người thấy đúng giờ địa phương quy đổi chính xác, nhưng **thời điểm kích hoạt thực tế vẫn là một mốc duy nhất và đồng nhất** cho tất cả
- Server và client lệch giờ hệ thống (client bị chỉnh sai giờ) — kết quả kích hoạt/đóng vẫn tính theo **giờ server**, không bị ảnh hưởng bởi giờ máy khách hàng
- Thời điểm chuyển đổi giờ mùa hè/mùa đông (Daylight Saving Time — nếu hệ thống phục vụ khu vực áp dụng) — mốc thời gian không bị lệch 1 giờ do quy đổi sai
- Nhập liệu mốc thời gian có chọn múi giờ (nếu nghiệp vụ cho phép người dùng chọn) — lưu và hiển thị lại đúng, không bị quy đổi sai qua nhiều lần chuyển đổi

### 28.6. Xử lý tại đúng ranh giới thời gian (Boundary Timing / Race Condition)

> **Câu hỏi nhận diện:** "Điều gì xảy ra nếu có 2 sự kiện xảy ra ở đúng cùng một thời điểm, một cái ngay trước và một cái ngay sau mốc kích hoạt?"

- Request/thao tác đến server tại **đúng mili-giây** của mốc thời gian — hệ thống xử lý nhất quán, có quy tắc rõ ràng để xác định "trước" hay "sau" (không random giữa các lần chạy)
- Tác vụ theo lịch (scheduled job) và thao tác thủ công của người dùng xảy ra **gần như đồng thời** tại đúng mốc — không có tình trạng cả 2 cùng chỉnh sửa dữ liệu gây sai lệch (liên quan Mục 16.1)
- Sinh case cụ thể: thao tác ở [mốc - 1 giây], [đúng mốc], [mốc + 1 giây] — xác nhận ranh giới xử lý đúng, không có "vùng xám" xử lý sai ở gần biên

### 28.7. Khôi phục sau khi hệ thống gián đoạn đúng lúc trigger (Missed Trigger Recovery)

> **Câu hỏi nhận diện:** "Nếu hệ thống bị down/restart đúng lúc phải kích hoạt một tác vụ theo lịch, điều gì xảy ra khi hệ thống phục hồi?"

- Hệ thống down **trước** mốc kích hoạt, phục hồi **sau** mốc kích hoạt — tác vụ bị bỏ lỡ được xử lý đúng theo nghiệp vụ (chạy bù ngay khi phục hồi, hoặc coi như đã kích hoạt đúng giờ gốc, tùy thiết kế) — không được **im lặng bỏ qua**
- Nhiều tác vụ theo lịch bị dồn lại trong thời gian downtime — khi phục hồi, tất cả được xử lý đầy đủ, đúng thứ tự, không bị trùng lặp hoặc bỏ sót
- Tác vụ được xử lý bù chạy **2 lần** do lỗi retry — đảm bảo idempotent, không tạo kết quả trùng lặp (gửi thông báo 2 lần, đóng phiên 2 lần...)

### 28.8. Lịch lặp lại (Recurring Schedule)

> Áp dụng nếu chức năng có tác vụ lặp lại theo chu kỳ (hàng ngày, hàng tuần, hàng tháng). Nếu không có → bỏ qua mục này.

- Tác vụ lặp lại đúng theo chu kỳ đã thiết lập, không bị trôi lịch qua nhiều lần lặp (ví dụ lặp hàng ngày lúc 00:00 không bị trễ dần thành 00:05, 00:10...)
- Thay đổi cấu hình chu kỳ **giữa lúc** đang chờ lần lặp tiếp theo — áp dụng đúng theo cấu hình mới hay vẫn theo cấu hình cũ cho lần sắp tới (cần xác nhận rõ trong nghiệp vụ)
- Hủy lịch lặp lại — không còn tác vụ nào được kích hoạt tiếp theo, tác vụ đã chạy trước đó không bị ảnh hưởng ngược

### 28.9. Hủy hoặc đổi lịch trước khi đến giờ kích hoạt

> **Câu hỏi nhận diện:** "Người dùng có thể hủy hoặc đổi mốc thời gian sau khi đã đặt lịch không?"

- Hủy lịch **trước** mốc kích hoạt — tác vụ không còn được thực hiện, trạng thái liên quan cập nhật đúng
- Đổi mốc thời gian **trước** mốc kích hoạt cũ — tác vụ chạy theo đúng mốc mới, không chạy nhầm theo mốc cũ
- Cố gắng hủy/đổi lịch **sau khi đã kích hoạt** — hệ thống chặn đúng, thông báo rõ lý do (đã kích hoạt, không thể thay đổi)
- Đồng hồ đếm ngược (nếu có) cập nhật ngay khi mốc thời gian bị đổi, không hiển thị sai thời gian cũ

### 28.10. Checklist câu hỏi nhận diện — Cần sinh case Time-based không?

| Câu hỏi | Nếu CÓ → sinh case |
|---|---|
| Có mốc thời gian nào hệ thống tự kích hoạt mà không cần người dùng thao tác? | 26.1 |
| Có tiến trình nào tự động đóng/kết thúc khi hết thời gian? | 26.2 |
| Có điều kiện nào làm thời gian kết thúc bị đẩy lùi (gia hạn)? | 26.3 |
| Có hiển thị đồng hồ đếm ngược cho người dùng? | 26.4 |
| Hệ thống phục vụ người dùng ở nhiều múi giờ, hoặc có xử lý ngầm liên quan thời gian? | 26.5 |
| Có khả năng 2 sự kiện xảy ra rất gần một mốc thời gian quan trọng? | 26.6 |
| Có tác vụ chạy nền theo lịch (cron/scheduled job) không? | 26.7 |
| Tác vụ có lặp lại theo chu kỳ không? | 26.8 |
| Người dùng có thể hủy/đổi lịch đã đặt không? | 26.9 |

### 28.11. Quy tắc viết testcase Time-based

**Tiền điều kiện** phải nêu rõ mốc thời gian cụ thể (không viết mơ hồ "gần hết giờ"):
```
Đúng:  "Phiên đấu giá có thời gian kết thúc là 15:00:00. Quy tắc gia hạn:
        nếu có đặt giá trong 5 phút cuối, gia hạn thêm 5 phút, tối đa 3 lần."

Sai:   "Phiên đấu giá sắp kết thúc."
```

**Các bước** nên ghi rõ **thời điểm tương đối** so với mốc kích hoạt, không phụ thuộc giờ thực tế lúc test:
```
1. Tại thời điểm [mốc kết thúc - 3 phút], thực hiện đặt giá
2. Quan sát thời gian kết thúc mới của phiên
3. Tại thời điểm [mốc kết thúc mới - 1 giây], thực hiện đặt giá lần 2
```

**Kết quả mong muốn** phải nêu rõ mốc thời gian cụ thể dự kiến, không chỉ mô tả hành vi chung:
```
- Thời gian kết thúc được gia hạn thành [mốc cũ + 5 phút]
- Đồng hồ đếm ngược hiển thị đúng thời gian mới ngay sau khi đặt giá thành công
```

**Lưu ý cho Automation (nếu case này được automate — xem `CLAUDE.md`):**
- Không nên chờ thời gian thực khi automate (test sẽ rất chậm) — ưu tiên: mock/điều chỉnh đồng hồ hệ thống (time travel) trong môi trường test, hoặc cấu hình khoảng thời gian ngắn hơn dành riêng cho test (ví dụ 5 giây thay vì 5 phút) nếu hệ thống hỗ trợ cấu hình linh hoạt
- Case liên quan đến race condition (26.6) nên test ở tầng **API**, dễ kiểm soát thời điểm gửi request chính xác hơn tầng E2E

**Mức độ ưu tiên:** luôn là **High** — bug time-based thường chỉ xuất hiện đúng vào thời điểm sản xuất thực tế (không phải lúc dev/test thông thường), khó tái hiện, và ảnh hưởng trực tiếp đến tính đúng đắn của nghiệp vụ cốt lõi.
