---
name: review-tai-lieu
description: Review độc lập một tài liệu BRD, FSD, SRS, CR hoặc bộ testcase (của mình hay người khác) bằng agent riêng theo checklist và văn phong, xuất báo cáo vấn đề xếp theo mức độ. Dùng khi gọi /review-tai-lieu hoặc nhờ review, soát tài liệu.
argument-hint: "<đường dẫn tài liệu hoặc link Google Doc> [| nguồn đối chiếu: ...] [| trọng tâm: ...]"
---

# Review tài liệu: $ARGUMENTS

Vai trò: senior BA kiêm senior tester, đọc như người mới nhận tài liệu. Skill này chỉ review, **không sửa tài liệu** trừ khi người dùng yêu cầu sau khi xem báo cáo.
Trả lời người dùng bằng tiếng Việt, gọi người dùng theo cách đã lưu trong memory.

## Bước 0. Nạp cấu hình

1. Thư mục Skill BA: `cat ~/.claude/skills/.skill-ba-root`. Gọi là `<SKILL_BA>`.
2. Đọc `<SKILL_BA>/_chung/van-phong.md` và `<SKILL_BA>/_chung/review-doc-lap.md`.
3. Chọn file cấu hình dự án trong `<SKILL_BA>/_du-an/` (template, file thuật ngữ, mẫu bảng testcase).
4. Tài liệu là link Google Doc: đọc bằng `node "<SKILL_BA>/scripts/google_api.mjs" doc-read <link> --key "<khóa>"`, lưu bản chữ ra file tạm để agent đọc.

## Bước 0b. Tư duy và phân tích

Theo `<SKILL_BA>/_chung/tu-duy-phan-tich.md`, mức gọn, cộng thêm: tài liệu loại gì, ai viết (mình, đồng nghiệp, dev, khách), ai sẽ dùng nó để làm gì, người dùng muốn soi kỹ phần nào. Tài liệu của khách hoặc bên ngoài thì chú trọng chỗ mơ hồ và chỗ thiếu, bỏ qua lỗi văn phong nhỏ.

## Bước 1. Chọn bộ tiêu chí theo loại tài liệu

| Loại | Template | Checklist review | Thêm |
|:---|:---|:---|:---|
| CR | Template CR của dự án | `<SKILL_BA>/viet-cr/tu-review.md` | Đối chiếu SRS trong bảng tác động |
| SRS | Template SRS của dự án | `<SKILL_BA>/viet-srs/tu-review.md` | `<SKILL_BA>/_chung/nfr-checklist.md` |
| FSD | Template FSD của dự án | `<SKILL_BA>/viet-fsd/tu-review.md` | `<SKILL_BA>/_chung/nfr-checklist.md`, BRD nếu có |
| BRD | Template BRD của dự án | Mục "Tự review" trong `<SKILL_BA>/viet-brd/SKILL.md` | Góc nhìn người duyệt: hiểu ngay vấn đề, mục tiêu, phạm vi |
| Testcase | Template testcase, mẫu bảng của dự án | `<SKILL_BA>/viet-testcase/tu-duy-test.md` | SRS/FSD nguồn, chạy thêm `/truy-vet` cho phần độ phủ |

Nguồn đối chiếu: người dùng chỉ định, hoặc tự tìm (SRS cũ cùng màn, CR liên quan, BRD, cây phân rã).

## Bước 2. Chạy agent review

Theo `review-doc-lap.md`: dùng agent `general-purpose`: tài liệu thường một agent làm cả hai góc, tài liệu dài thì chạy song song 2 agent, góc A (Dev và Tester) và góc B (nghiệp vụ, văn phong, khớp nguồn). Gửi kèm đường dẫn `_du-an/<dự án>.md`. Người dùng nêu trọng tâm thì thêm vào lời giao việc. Tài liệu rất dài (trên 15 màn hoặc trên 300 testcase) thì chia theo phần, mỗi agent một phần.

## Bước 3. Gộp và kiểm lại

1. Gộp kết quả hai agent, bỏ dòng trùng.
2. Tự mở tài liệu kiểm từng dòng. Dòng agent hiểu sai thì bỏ.
3. Xếp mức độ:
   - **Cao:** Dev làm sai, hoặc tester không test được, hoặc chạm tiền, dữ liệu cá nhân, văn bản pháp lý.
   - **Trung bình:** thiếu trường hợp biên, mâu thuẫn nhỏ, AC chưa đo được.
   - **Thấp:** văn phong, định dạng, sai template.

## Bước 4. Xuất báo cáo và dừng

File `<tên tài liệu> - review.md` đặt trong `<thư mục dự án>/_session_ai/` (tài liệu của người khác thì không đặt cạnh tài liệu gốc):

- Đầu file: tài liệu, ngày review, nguồn đối chiếu, số vấn đề theo mức độ, nhận xét chung 3 đến 5 dòng (đủ để giao dev chưa, chỗ yếu nhất ở đâu).
- Bảng: # | Mức độ | Vị trí (mục, trích ngắn) | Vấn đề | Đề xuất sửa | Loại (Lỗi rõ ràng / Cần BA quyết).

Báo người dùng: link báo cáo, 3 đến 5 vấn đề mức Cao. Hỏi người dùng muốn:

- sửa luôn các lỗi rõ ràng (tài liệu của mình),
- gửi danh sách cho người viết (tài liệu của người khác: viết sẵn đoạn nhận xét để dán),
- hay chỉ giữ báo cáo.
