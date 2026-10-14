# Sửa tài liệu đã hoàn thành

Áp dụng cho mọi skill và cả khi người dùng nhờ sửa ngoài skill.

**Tài liệu đã hoàn thành** là tài liệu đã được duyệt, đã push hoặc đã gửi đi (Drive, Jira, cho người khác). Tài liệu đang viết dở trong cùng lượt thì sửa thẳng, không cần làm theo file này.

Mục đích: một thay đổi nhỏ ở một chỗ thường kéo theo nhiều chỗ khác. Sửa một chỗ mà bỏ sót chỗ khác thì tài liệu tự mâu thuẫn, dev và tester làm theo bản cũ.

## Bước 1. Xác định thay đổi

Ghi rõ ba ý: đang viết gì, sẽ đổi thành gì, vì sao đổi. Lấy ra các **từ khóa cũ** để dò: tên màn, tên nút, tên field, tên trạng thái, con số, câu chữ quy tắc.

## Bước 2. Dò chỗ bị ảnh hưởng

Trong chính tài liệu:

- Mô tả, tiền điều kiện, hậu điều kiện.
- Bảng thành phần giao diện, thông báo lỗi.
- Business Rules, Use case, AC.
- Sơ đồ (Mermaid, sơ đồ làn, phân rã), ảnh màn hình.
- Bảng tác động, lịch sử thay đổi, file note đi kèm.

Sang file khác (grep từ khóa cũ trên toàn thư mục dự án, cả thư mục lồng sâu):

| Nơi | Ví dụ |
|:---|:---|
| Tài liệu yêu cầu cùng màn hoặc dùng chung dữ liệu | SRS, CR, FSD, BRD, cây phân rã, file thuật ngữ, quy tắc nghiệp vụ |
| Testcase và automation | `.test.md`, `.auto.md`, script trong repo automation, Testcase List trên sheet |
| Design | Repo thiết kế (Vue), ảnh trong `_attachments` |
| Bản đã gửi đi | Google Doc, Google Sheet trong bảng Tài liệu đã gửi của cấu hình dự án, mô tả task Jira |

## Bước 3. Báo trước và chờ duyệt

Báo người dùng một bảng, chưa sửa gì:

| # | File | Vị trí | Đang viết | Sẽ sửa thành |
|:---:|:---|:---|:---|:---|

Cuối bảng ghi riêng các chỗ cần người dùng quyết:

- Chỗ nên sửa nhưng thuộc tài liệu của người khác.
- Bản đã gửi đi (Google Doc, Jira) mà người khác có thể đang đọc.
- Script automation, Testcase List trên sheet.
- Chỗ không chắc có cùng nghĩa với thay đổi hay không.

Chờ người dùng duyệt. Người dùng duyệt từng dòng hoặc từng nhóm được.

Ngoại lệ: lỗi chính tả, câu chữ không đổi nghĩa và không xuất hiện ở chỗ nào khác thì sửa luôn, báo một dòng.

## Bước 4. Sửa toàn bộ chỗ đã duyệt

1. Sửa từng chỗ theo bảng. Sửa cả ảnh, sơ đồ nếu nằm trong bảng.
2. Tài liệu có lịch sử thay đổi thì thêm một dòng.
3. Grep lại từ khóa cũ trên toàn thư mục dự án. Còn sót thì sửa nốt nếu cùng nghĩa, không chắc thì báo.
4. Báo lại: các file đã sửa (link), chỗ chưa sửa và lý do, bản đã gửi đi cần đồng bộ lại.
