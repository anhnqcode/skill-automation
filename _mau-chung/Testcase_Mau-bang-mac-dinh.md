# Mẫu bảng testcase mặc định

Lấy theo bộ testcase thật đã dùng. Dùng khi dự án chưa có cấu hình "Mẫu bảng testcase" và chưa có file testcase nào để làm theo.

## Tên file

- Testcase: `Testcase - <Tên module>.testcase.md`
- Ghi chú: `Testcase - <Tên module>.note.md`, cùng thư mục

## Đầu file

```markdown
# Testcase - <Tên module>

## Tổng hợp số lượng testcase

| Ưu tiên | Số TC |
|---|---|
| High (P0) | 0 |
| Medium (P1) | 0 |
| Low (P2) | 0 |
| **Tổng** | **0** |

| Phần | Màn hình | P0 | P1 | P2 | Tổng |
|---|---|---|---|---|---|
| PHẦN A | <TÊN MÀN VIẾT HOA> | 0 | 0 | 0 | 0 |
| | **Tổng cộng** | **0** | **0** | **0** | **0** |
```

## Cách nhóm

```markdown
# PHẦN A — <TÊN MÀN VIẾT HOA>

## 1. <Khu vực trên màn>

### 1.1. Kiểm tra trạng thái mặc định

| ID | ... |
```

Ba cấp: Phần theo màn hình → khu vực trên màn → loại kiểm tra (tên loại kiểm tra theo Testcase_Template). Phần cuối có thể là "TƯ DUY ĐỐI KHÁNG VÀ LIÊM CHÍNH DỮ LIỆU" nếu checklist đối kháng được bật.

## Bảng: đúng 10 cột

| ID | Mục đích kiểm thử | Tiền điều kiện | Các bước thực hiện | Kết quả mong muốn | Kết quả thực tế | Mức độ ưu tiên | Ghi chú | Mã SRS | Mã UC - TKCT |
|---|---|---|---|---|---|---|---|---|---|

| Cột | Cách điền |
|---|---|
| ID | `TC-001`, `TC-002`... đánh liên tục trong file |
| Mục đích kiểm thử | Bắt đầu bằng "Kiểm tra ...", một câu |
| Tiền điều kiện | Đánh số, xuống dòng bằng `<br>`: tài khoản, dữ liệu cần có |
| Các bước thực hiện | Đánh số, mỗi bước một thao tác, xuống dòng bằng `<br>` |
| Kết quả mong muốn | Cụ thể, đo được. Có thể chèn ảnh design: `<br>![tên màn](đường dẫn ảnh)` |
| Kết quả thực tế | Để trống khi viết |
| Mức độ ưu tiên | P0 / P1 / P2 |
| Ghi chú | Chỉ điền khi có điều cần lưu ý thật: lệch giữa bản chạy và FSD, tham số chưa chốt, cần công cụ |
| Mã SRS | Mã màn trong FSD: `SCR-01`, `SCR-A01`... |
| Mã UC - TKCT | Mã use case hoặc mã mục trong tài liệu thiết kế chi tiết: `UC01`. Không có thì để trống |

Không có cột Automation Status, Automation Link. Không ghi "(QA-ADD)".
