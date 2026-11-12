---
name: truy-vet
description: Lập ma trận truy vết User story → phân rã → BR/AC → testcase → bug, báo chỗ hở (yêu cầu chưa có testcase, mã sai, chức năng chưa có đặc tả) và phạm vi cần test lại khi có CR. Dùng khi gọi /truy-vet hoặc nhờ kiểm tra độ phủ, truy vết.
argument-hint: "<module / thư mục / mã CR> [| có bug: <link file bug>]"
---

# Truy vết: $ARGUMENTS

Vai trò: BA kiêm QA lead. Mục tiêu là trả lời ba câu: yêu cầu nào chưa được test, test nào không gắn yêu cầu, và khi đổi một yêu cầu thì phải test lại những gì.
Trả lời người dùng bằng tiếng Việt, gọi người dùng theo cách đã lưu trong memory.

## Bước 0. Nạp cấu hình

1. Thư mục Skill BA: `cat ~/.claude/skills/.skill-ba-root`. Gọi là `<SKILL_BA>`.
2. Đọc `<SKILL_BA>/_chung/van-phong.md`.
3. Chọn file cấu hình dự án trong `<SKILL_BA>/_du-an/`. Lấy: Thư mục SRS, nơi đặt file testcase, mẫu bảng testcase, khóa **Mã truy vết** (các tiền tố mã được tính độ phủ), mục Google Drive (file bug).

## Bước 0b. Tư duy và phân tích

Theo `<SKILL_BA>/_chung/tu-duy-phan-tich.md`, mức gọn: phạm vi truy vết (một module, một màn, hay theo một CR), có những tầng nào (BRD, phân rã, SRS/FSD, testcase, bug), người nhận báo cáo là ai.

## Bước 1. Gom nguồn

- **Yêu cầu:** BRD, FSD/SRS, CR của phạm vi. Theo một CR thì lấy CR đó cộng các SRS trong bảng Tài liệu bị ảnh hưởng.
- **Testcase:** các file testcase cạnh SRS hoặc trong thư mục testcase của dự án.
- **Phân rã:** file JSON của sơ đồ phân rã nếu có.
- **Bug:** người dùng đưa link file bug thì đọc bằng `node "<SKILL_BA>/scripts/google_api.mjs" sheet-read <link> "<tab>!A1:Z2000" --key "<khóa>"`, lưu ra file JSON tạm. Dự án dùng Bug List của repo e2e thì đọc từ đó.

## Bước 2. Chạy script

```bash
py "<SKILL_BA>/scripts/truy_vet.py" --yeu-cau <file/thư mục ...> --testcase <file/thư mục ...> \
   --tien-to <Mã truy vết của dự án> [--phan-ra <json>] [--bug <json>] --ra "<thư mục dự án>/_session_ai/truy-vet-<phạm vi>.md"
```

Script nhận diện mã theo mẫu chung (US-01, YC-01, SCR-A01, UC01, BR-C02a, AC-POP-01, TC-TT-001...). Dự án dùng tiền tố khác thì truyền thêm vào `--tien-to`.

## Bước 3. Đọc kết quả, không tin mù vào con số

Script chỉ khớp mã. Mỗi chỗ hở cần xem lại bằng mắt:

1. **Mã chưa có testcase:** mở định nghĩa. Có thể là mã tiêu đề, mã nhóm, hoặc quy tắc đã được test dưới mã khác. Còn lại là thiếu thật.
2. **Testcase dẫn mã lạ:** mã gõ sai hoặc yêu cầu đã bị xóa. Ghi cụ thể sửa thành mã nào.
3. **Testcase không dẫn mã:** phần lớn là case ngoài SRS, điều này bình thường. Case nào thật ra kiểm một quy tắc có mã thì ghi lại.
4. **Nút phân rã chưa có đặc tả:** chức năng đã chốt trong phạm vi mà chưa có SRS/FSD.
5. **Có bug:** yêu cầu nào nhiều bug, bug đang mở gắn với yêu cầu nào.

Theo một CR: liệt kê thêm **phạm vi test lại**, gồm các testcase gắn với mã BR/AC mà CR sửa hoặc thay thế, và testcase của màn dùng chung dữ liệu.

## Bước 4. Báo lại và dừng

Viết báo cáo ngắn (đặt cạnh file kết quả của script, cùng tên thêm `- tom-tat.md`):

| Mục | Nội dung |
|:---|:---|
| Độ phủ | Bảng theo loại mã, chỉ tính các loại trong Mã truy vết |
| Thiếu thật | Danh sách mã cần viết thêm testcase, xếp theo mức rủi ro (tiền, dữ liệu cá nhân, trạng thái trước) |
| Cần sửa mã | Testcase dẫn mã sai, case nên gắn mã |
| Chức năng chưa đặc tả | Từ phân rã |
| Test lại theo CR | Nếu truy vết theo CR |

Hỏi người dùng có muốn chạy `/viet-testcase` để bổ sung các case thiếu không. Không tự sửa file testcase trong skill này.
