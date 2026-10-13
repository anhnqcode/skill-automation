# Mẫu bug trên Jira

Dùng khi cấu hình dự án có **Nơi ghi bug: Jira**. Văn phong từng ý giống mục 2 của `mau-bang-bug.md` (người đọc là dev, không dẫn mã BR, mã màn, tên tài liệu).
Lệnh `JIRA` như ở `/lam-task-jira` Bước 0.

## 1. Các trường

| Trường | Cách điền |
|:---|:---|
| Project | Project của task test |
| Issue Type | Bug |
| Summary | `[Cổng][Màn][Tab hoặc khu vực] <mô tả ngắn>`, cổng luôn đứng đầu. VD `[CMS][Tài sản đấu giá] Biên bản xác nhận đấu giá chưa đúng file` |
| Priority | Theo mức độ: Cao → High (chạm tiền, kết quả đấu giá, lộ dữ liệu, chặn luồng chính thì Highest), Trung bình → Medium, Thấp → Low. Tên priority lấy đúng như Jira của dự án |
| Sprint | Sprint của task test (id sprint đang chạy trong `JIRA issue <task>`) |
| Fix Version/s | Version của task test |
| Env | Môi trường đang test (stg, prod ...). Trường tùy chỉnh, id ghi trong cấu hình dự án |
| Assignee | Theo **Người nhận bug** trong cấu hình. Để "—" thì không điền, người dùng tự giao |
| Description | Theo mẫu ở mục 2 |
| Tệp đính kèm | Bug có ảnh thì **luôn tải ảnh lên Jira, đính kèm vào bug**: ảnh ghi chú vẽ theo `/log-bug` Bước 5, ảnh chụp lỗi, ảnh người dùng gửi. Không dùng thư mục ảnh trên Drive |
| Liên kết | Relates tới task test |

## 2. Mô tả (Jira wiki markup)

```
* *Environment*: Stg
* *Summary*: Biên bản xác nhận đấu giá chưa đúng file
* *Pre-conditions*: Tài sản đã có kết quả đấu giá
* *Step to reproduce*:
# Admin truy cập menu Tài sản đấu giá > sub-menu TSK/ SS/BĐS
# Click more menu
# Chọn in/ tải biên bản xác nhận
# Xem thông tin
* *Actual results*: Biên bản đang là biên bản đấu giá tương tự ở tab kết quả
* *Expect results*: Hiển thị đúng biên bản xác nhận theo mẫu.

!01-bien-ban-xac-nhan.png|thumbnail!
```

- Summary trong mô tả là phần mô tả ngắn, bỏ các ngoặc cổng, màn.
- Pre-conditions không có thì để trống sau dấu hai chấm, vẫn giữ dòng.
- Step đánh số bằng `#`, mỗi bước một dòng, bắt đầu bằng động từ.
- Expect nhiều ý thì xuống dòng, mỗi ý một dòng `** ` (gạch con).
- Mức độ Cao hoặc Trung bình có lý do đáng nói thì thêm dòng `* *Note*: ...` trước ảnh.
- Ảnh chỉ khi bug cần hình. Tên tệp trong `!...!` phải trùng tên tệp đã đính kèm.

## 3. Các bước tạo

1. `JIRA issue <task test>`: lấy project, id sprint, version, ghi chú `sprintFieldId`.
2. Lần đầu ở dự án: `JIRA fields env` tìm id trường Env, ghi vào cấu hình dự án. Trường dạng nhãn (labels) thì giá trị là mảng `["stg"]`, dạng chọn một thì `{"value": "stg"}`.
3. Trước khi tạo, tìm bug trùng: `JIRA search 'project = <mã> AND issuetype = Bug AND statusCategory != Done AND summary ~ "<vài từ khóa>"'`. Trùng thì báo người dùng, không tạo.
4. Ghi file `<tạm>.json`:

   ```json
   {"fields": {
     "project": {"key": "UGTSK"},
     "issuetype": {"name": "Bug"},
     "summary": "[CMS][Tài sản đấu giá] Biên bản xác nhận đấu giá chưa đúng file",
     "priority": {"name": "High"},
     "fixVersions": [{"id": "<id version>"}],
     "<sprintFieldId>": <id sprint>,
     "<id trường Env>": ["stg"],
     "description": "<mô tả theo mục 2>"
   }}
   ```

   Cloud: trường sprint vẫn là số id. Lỗi "Field cannot be set" thì trường đó không có trên màn tạo bug, bỏ trường ra, tạo xong sửa lại bằng `JIRA update`.
5. `JIRA create <tạm>.json`, rồi `JIRA attach <bug> <ảnh 1> <ảnh 2> ...` cho mọi ảnh của bug, rồi `JIRA link <bug> <task test>`. Ảnh người dùng dán vào chat mà không có đường dẫn tệp thì hỏi người dùng lưu ra tệp, hoặc tự chụp lại trên hệ thống.
6. Đọc lại `JIRA issue <bug>`: sprint, version, priority đúng, mục attachments có đủ ảnh.

## 4. Trạng thái khi kiểm lại

| Kết quả | Việc làm |
|:---|:---|
| Đạt | `JIRA transition <bug> Done` |
| Còn lỗi | `JIRA transition <bug> Reopen --comment <file>`. Comment: `Verify <dd/mm> trên <môi trường>: <hiện tượng còn lại, thực tế so với mong muốn>`, kèm ảnh mới đính bằng `attach` và chèn `!tên ảnh|thumbnail!` vào comment |
| Không kiểm được | Giữ Resolved, báo người dùng lý do |

Tên trạng thái khác trong Jira của dự án (VD Reopened, Closed) thì theo cấu hình **Trạng thái bug** của dự án.
