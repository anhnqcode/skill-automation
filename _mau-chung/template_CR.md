# CR-[YYMM-NNN] — [Tên thay đổi ngắn gọn]

> Dòng bắt đầu bằng `>` là hướng dẫn, xóa khi viết thật.
> Nguyên tắc chung:
> - CR chỉ viết phần **mới hoặc thay đổi**. Hành vi giữ nguyên thì gói một câu "theo quy tắc hiện có của <màn>", nói rõ điểm khác nếu có.
> - Viết giọng thường, câu ngắn. Không dùng cú pháp code trong mô tả, quy tắc, AC. Tên API, bảng dữ liệu chỉ ghi ở bảng Ảnh hưởng kỹ thuật.
> - Không viết câu phủ định, không viết điều không xảy ra. Viết thành câu khẳng định.
> - Không viết những thứ không thay đổi: dòng "Không đổi", hàng "Không áp dụng", quy tắc hay AC chỉ để nói phần khác "giữ nguyên".
> - Hành vi đã lên production thì viết là hiện trạng: "Hệ thống đang …". Không rải mã CR, mã màn (SCR04), mã quy tắc (BR17) vào mô tả, quy tắc, AC: gọi thẳng tên màn, viết thẳng hành vi. Mã CR cũ chỉ ghi ở dòng CR phụ thuộc và bảng Tài liệu bị ảnh hưởng.
> - Mỗi quy tắc ở mục 3 có ít nhất một AC ở mục 4.

---

## Thông tin tài liệu

| Trường | Nội dung |
|--------|----------|
| **Mã CR** | CR-[YYMM-NNN] |
| **Ngày tạo** | [YYYY-MM-DD] |
| **Người yêu cầu** | [Tên / Vai trò, hoặc —] |
| **Người phân tích** | [BA phụ trách] |
| **Trạng thái** | [Draft / Review / Approved / Rejected / Implemented] |
| **Độ ưu tiên** | [High / Medium / Low] |
| **Sprint / Release dự kiến** | [Sprint XX / v1.X.X, hoặc —] |
| **CR phụ thuộc** | [CR-YYMM-NNN (nói ngắn CR đó làm gì), hoặc —] |

### Lịch sử phê duyệt

| Ngày | Người | Hành động | Ghi chú |
|------|-------|-----------|---------|
| [YYYY-MM-DD] | [Tên] | Tạo CR |  |

> Thêm dòng khi: PO duyệt / từ chối (kèm lý do), cập nhật SRS theo CR (ghi tên các SRS đã sửa).

---

## 1. Mô tả thay đổi

### Hiện trạng (As-Is)

> Hệ thống đang chạy thế nào, ở màn nào, vai trò nào. Dùng gạch đầu dòng có tên trường in đậm khi mô tả nhiều trường. Có số liệu thật thì ghi kèm ngày kiểm tra. Có thể kèm ảnh màn hiện tại.

[Mô tả hiện trạng]

### Yêu cầu thay đổi (To-Be)

> Đánh số từng ý. Mỗi ý một thay đổi, nêu kết quả người dùng thấy được. Ghi cả phạm vi áp dụng (luồng nào, dữ liệu cũ thế nào).

1. [Thay đổi 1]
2. [Thay đổi 2]

### Lý do thay đổi

> Góc nghiệp vụ: người dùng đang mất công ở đâu, rủi ro gì, ai được lợi. Có phản hồi, số liệu thì ghi.

[Lý do]

---

## 2. Phân tích tác động (Impact Analysis)

### Tài liệu bị ảnh hưởng

| Tài liệu | Loại thay đổi | Ghi chú |
|:---|:---|:---|
| `SRS/[đường dẫn tương đối].md` | Cập nhật | [Mục cụ thể cần sửa và sửa theo mục 3.x nào của CR. Ví dụ: Mục 5.6, nhóm Lịch trình: cột Giá trị mặc định đổi theo mục 3.3. Mục 9: thêm AC] |
| `CR/CR-YYMM/[tên CR cũ].md` | Thay thế một phần | [Câu hoặc quy tắc nào của CR cũ bị thay, thay theo mục nào] |

> Grep cả cây SRS (kể cả thư mục lồng sâu) và các CR cũ cùng màn, không chỉ SRS người yêu cầu nêu tên.

### Màn hình / tính năng bị ảnh hưởng

| Màn hình | Platform | Mức ảnh hưởng | Ghi chú |
|:---|:---|:---|:---|
| [Tên màn, tab] | [Web (CMS) / Web (Partner) / Web (Customer) / Mobile (Customer)...] | [Lớn / Vừa / Nhỏ] | [Thay đổi gì] |

### Ảnh hưởng kỹ thuật (để Dev tham khảo)

| Thành phần | Loại thay đổi | Ghi chú |
|:---|:---|:---|
| [DB / API / màn Web / dịch vụ / app] | [Thêm / Sửa / Xóa] | [Mô tả. Có trường mới thì ghi migration cho dữ liệu cũ. API dùng chung với màn khác thì ghi cách giữ nguyên hành vi màn khác] |

---

## 3. Đặc tả thay đổi chi tiết

> Đủ chi tiết để Dev làm và QA viết case mà không cần hỏi lại.

### 3.1 Phạm vi áp dụng

| Điều kiện | Mô tả |
|:---|:---|
| Portal | [Portal nào cấu hình, portal nào áp dụng] |
| Vai trò | [Ai làm gì] |
| Phân hệ / luồng | [Phân hệ, luồng tạo thủ công / nhân bản / AI... nào áp dụng] |
| Dữ liệu cũ | [Bản ghi tạo trước CR xử lý ra sao] |

---

### 3.2 [Tên thay đổi 1, đặt theo thành phần trên giao diện]

**Vị trí:** [Portal, menu → màn → tab / khối, đặt ở đâu so với thành phần có sẵn].

**Trước:** [Hành vi hiện tại của đúng chỗ này, 1–3 câu].

**Sau:**

![Mô tả ngắn của ảnh](_attachments/crNNN-scrNN-[ten-ngan].png)

> Thành phần giao diện mới (tiêu đề khối, mô tả, chú thích): bảng Thành phần | Loại | Mô tả, chữ hiển thị ghi nguyên văn trong ngoặc kép.

| Thành phần | Loại | Mô tả |
|:---|:---|:---|
| [Tiêu đề khối] | Text | "[Chữ hiển thị nguyên văn]" |

> Field mới hoặc field đổi: độ dài ghi ở cột Loại, đủ cả min và max, ví dụ `Textbox (1–100 ký tự)`, `Number (0–2 ký tự)`, `Date time picker (dd/mm/yyyy HH:mm:ss)`. Cột Quy tắc nhập không lặp lại con số độ dài.

| Tên trường | Loại | Giá trị mặc định | Bắt buộc | Quy tắc nhập |
|:-----------|:-----|:-----------------|:--------:|:-------------|
| [Tên field] | [Loại (min–max ký tự)] | [Mặc định, có điều kiện thì ghi đủ từng trường hợp] | [Có / Không] | [Loại ký tự, khoảng giá trị, danh sách giá trị, chữ báo lỗi nguyên văn] |

| Nút chức năng | Mô tả |
|:---|:---|
| [Tên nút] | [Bấm thì làm gì, popup xác nhận, chữ thông báo sau xử lý, điều kiện hiện / khóa nếu có] |

**Quy tắc:**

> Mỗi gạch đầu dòng một ý, mở đầu bằng nhãn in đậm. Ghi lý do nghiệp vụ khi cần ("vì …"). Có ví dụ số liệu cụ thể cho quy tắc dễ hiểu sai.

- **[Nhãn quy tắc]:** [Nội dung]
- **[Nhãn quy tắc]:** [Nội dung. Ví dụ: …]

> Trạng thái màn hình, lỗi hệ thống, hết hạn phiên của thành phần mới theo xử lý chung hiện có của màn, không viết bảng riêng. Trạng thái nào có hành vi riêng của thay đổi (ví dụ một thông báo lỗi mới) thì viết thành quy tắc ở đây.

---

### 3.3 [Tên thay đổi 2]

*(Thêm mục 3.x cho mỗi thay đổi. Mục chỉ có quy tắc, không có giao diện mới thì bỏ bảng.)*

---

### 3.[n] Luồng dữ liệu

> Có khi bản ghi đổi trạng thái hoặc dữ liệu đi qua nhiều portal, module. Chỉ ghi các bước có thay đổi. Logic rẽ nhánh phức tạp thì thêm sơ đồ Mermaid.

| Bước | Mô tả hành động | Kết quả hệ thống thực hiện |
|:---|:---|:---|
| 1 | [Ai làm gì, ở đâu] | [Hệ thống làm gì, bản ghi hiện ở đâu, mất khỏi đâu, module nào bị ảnh hưởng] |

---

## 4. Tiêu chí chấp nhận (Acceptance Criteria)

> Checklist `- [ ]`, nhóm theo mục 3.x. Mỗi AC gồm: điều kiện đầu vào cụ thể (vai trò, cấu hình, dữ liệu, giá trị) → kết quả đo được (số lượng, trạng thái, chữ hiển thị nguyên văn trong ngoặc kép, giá trị trong ô).
> Phủ: luồng chính, dữ liệu sai, biên (min, max, 0, rỗng, đúng mốc), bật/tắt, cấu hình, dữ liệu cũ trước CR, thao tác sai thứ tự, phân quyền riêng của thay đổi.
> Không viết nhóm AC lỗi hệ thống, hết hạn phiên, thu hồi quyền (theo xử lý chung), không viết AC "màn giữ nguyên như trước khi có CR".
> Không dùng chữ chung chung như "hiển thị đúng", "hoạt động bình thường".

**Mục 3.2: [Tên thay đổi 1]**

- [ ] [Điều kiện]: [kết quả đo được].
- [ ] [Điều kiện biên]: [kết quả].

**Mục 3.3: [Tên thay đổi 2]**

- [ ] [Điều kiện]: [kết quả].

---

## 5. Ghi chú thêm

**Rủi ro và biện pháp**

| Rủi ro | Mức độ | Biện pháp |
|:---|:---|:---|
| [Rủi ro khi triển khai hoặc khi dùng] | [Cao / Trung bình / Thấp] | [Cách xử lý, hoặc chấp nhận và theo dõi] |

**Phụ thuộc**

- [Việc phải có trước: CR khác, dữ liệu, cấu hình, phát hành app. Không có thì xóa mục này]
