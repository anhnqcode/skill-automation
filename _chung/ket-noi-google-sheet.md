# Kết nối Google Sheet để ghi bug

Làm một lần trên mỗi máy. Sau khi xong, chạy automation xong là gọi `/log-bug` để Claude ghi bug thẳng vào file bug Google Sheet của bạn.

Cách hoạt động: bạn tạo một **service account**, là tài khoản máy của Google. Claude dùng file khóa của tài khoản này để đọc, ghi Google Sheet. Service account chỉ mở được những file bạn chủ động chia sẻ cho nó.

## Cần có trước

- Node.js 18 trở lên. Máy chạy automation Playwright thì đã có.
- Python và thư viện Pillow, dùng để vẽ ảnh ghi chú bug: `py -m pip install pillow`.
- Một tài khoản Google tạo được project trên Google Cloud.

## Bước 1. Tạo project và bật API

1. Mở https://console.cloud.google.com, đăng nhập tài khoản Google.
2. Thanh trên cùng, chọn project → **New Project**, đặt tên ví dụ `log-bug`, bấm **Create**, rồi chọn project vừa tạo.
3. Menu trái → **APIs & Services → Library**. Tìm và bấm **Enable** cho:
   - **Google Sheets API**
   - **Google Drive API**

## Bước 2. Tạo service account và tải khóa

1. Menu trái → **IAM & Admin → Service Accounts** → **Create service account**.
2. Đặt tên ví dụ `claude-log-bug`, bấm **Create and continue**. Bước phân quyền để trống, bấm **Done**.
3. Bấm vào service account vừa tạo → tab **Keys** → **Add key → Create new key** → chọn **JSON** → **Create**. Trình duyệt tải về một file `.json`.
4. Tạo thư mục `C:\Users\<tên máy>\.secrets\`, chuyển file khóa vào đó, đổi tên thành `google-sa.json`.

Giữ file khóa như mật khẩu:

- Không gửi qua chat, Zalo, email.
- Không để trong thư mục dự án, thư mục skill, repo automation. Không đưa lên Drive hay Git.
- Lỡ lộ thì vào tab **Keys** xóa khóa đó và tạo khóa mới.

Google Cloud của công ty có thể chặn tạo khóa (chính sách "Disable service account key creation"). Gặp chặn thì nhờ quản trị viên Google Cloud mở cho project này, hoặc dùng tài khoản Google khác được phép.

## Bước 3. Lấy email service account

Chạy trong PowerShell, thay đường dẫn cho đúng máy:

```powershell
node "<thư mục skill>/scripts/google_api.mjs" whoami --key "C:/Users/<tên máy>/.secrets/google-sa.json"
```

Lệnh in ra email dạng `claude-log-bug@log-bug-12345.iam.gserviceaccount.com`. Hoặc hỏi Claude: "chạy whoami của google_api với khóa của tôi".

## Bước 4. Chia sẻ file bug cho service account

1. Mở file bug trên Google Sheet → **Chia sẻ**.
2. Dán email ở Bước 3, chọn quyền **Người chỉnh sửa**, bỏ tích "Thông báo cho mọi người", bấm **Gửi**.

File phải là **Google Sheet**. File `.xlsx` tải lên nguyên dạng thì mở ra → **Tệp → Lưu dưới dạng Google Trang tính**, rồi dùng bản mới.

Workspace của công ty có thể chặn chia sẻ ra ngoài tên miền công ty. Khi đó nút Gửi báo lỗi, cần nhờ quản trị viên cho phép.

## Bước 5. Điền cấu hình dự án

Mở `_du-an/<tên dự án>.md` trong thư mục skill. Chưa có thì copy từ `_du-an/_mau.md`. Điền mục **Google Drive**:

| Khóa | Điền |
|:---|:---|
| Khóa service account | `C:/Users/<tên máy>/.secrets/google-sa.json`. Chỉ ghi đường dẫn, không chép nội dung khóa |
| Email service account | Email ở Bước 3 |

Thêm link file bug vào bảng **Tài liệu đã gửi** ngay bên dưới, cột Loại ghi "File bug". `/log-bug` tự tìm link ở đây khi bạn không đưa link.

## Bước 6. Thử kết nối

```powershell
node "<thư mục skill>/scripts/google_api.mjs" sheet-tabs "<link file bug>" --key "C:/Users/<tên máy>/.secrets/google-sa.json"
```

In ra danh sách tab của file là đã kết nối được.

## Dùng hằng ngày

- Chạy automation chế độ B (`/viet-automation`): khi có lỗi, skill hỏi rồi chuyển sang `/log-bug`.
- Ghi bug từ kết quả có sẵn:

  ```
  /log-bug <link file bug> | <file kết quả kiểm thử, hoặc mô tả bug>
  ```

- Kiểm lại bug dev đã sửa: `/verify-bug <link file bug>`.

Claude ghi bug theo mẫu của file, kèm ảnh có ghi chú. Bug chưa rõ là lỗi hay không thì Claude hỏi trước khi ghi.

## Lỗi thường gặp

| Báo lỗi | Cách sửa |
|:---|:---|
| 403 hoặc 404 | File chưa chia sẻ quyền Người chỉnh sửa cho email service account, hoặc chưa bật API ở Bước 1 |
| `invalid_grant` | Khóa đã bị xóa trên Google Cloud, hoặc giờ máy lệch. Tạo khóa mới, chỉnh lại giờ máy |
| Không thấy file khóa | Sai đường dẫn ở khóa **Khóa service account** của cấu hình dự án |
| Ghi được chữ nhưng thiếu ảnh ghi chú | Chưa cài Pillow: `py -m pip install pillow` |
