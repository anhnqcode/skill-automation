# Checklist domain: <Tên domain>

> Mẫu cho một bộ domain (tầng 3). Đặt file thật tên `domain-<ten-domain>.md` trong thư mục này và thêm một dòng vào `../_danh-muc.md`. Dòng bắt đầu bằng `>` là hướng dẫn, xóa khi viết thật.
> Chỉ ghi rủi ro **riêng của domain**. Rủi ro đã có ở tầng 1 (`QA-Business-Risk-Core-Checklist.md`) thì trỏ sang nhóm tương ứng, không chép lại. Mục tiêu 80 đến 200 dòng.

Áp dụng cho: <loại hệ thống, ví dụ sàn đấu giá trực tuyến, đặt lịch khám, ví điện tử>.
Dùng cùng: tầng 0, tầng 1 nhóm <số các nhóm hay bật>, tầng 2 <các file QA-* hay bật>.

---

## 1. Dấu hiệu nhận biết

<8 đến 12 từ khóa hoặc khái niệm trong tài liệu đặc tả cho thấy dự án thuộc domain này.>

## 2. Bảng tham số phải điền trước khi viết case

> Các con số, quy tắc mà mọi case của domain phụ thuộc vào. Ô trống là câu hỏi chặn.

| Tham số | Giá trị theo tài liệu | Nguồn |
|:---|:---|:---|
| <ví dụ: bước giá, hạn hoàn tiền, số lần đổi lịch tối đa> | | |

## 3. Rủi ro đặc thù

### 3.1 <Tên nhóm rủi ro riêng của domain>

**Vì sao nguy hiểm:** <thiệt hại thật nếu sai: tiền, pháp lý, uy tín, an toàn>.

**Câu hỏi suy ra case:**
1. Khi ... thì hệ thống ...?

**Case mẫu:**
- <Tiền điều kiện có số cụ thể>. Kết quả: <đo được>.

### 3.2 <...>

## 4. Hành vi người dùng đặc thù của domain

> Thao tác "lạ" hay gặp ở người dùng thật của domain này (ví dụ đặt lịch rồi bỏ không đến, trả giá phút cuối, đổi ý sau khi thanh toán).

- <Hành vi> → <hệ thống phải làm gì>

## 5. Quy tắc nâng mức ưu tiên riêng

- <Case chạm vào ... luôn ở mức cao nhất>

## 6. Thuật ngữ và bẫy hiểu nhầm

| Thuật ngữ | Nghĩa trong domain | Hay bị hiểu nhầm thành |
|:---|:---|:---|
