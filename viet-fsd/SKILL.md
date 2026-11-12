---
name: viet-fsd
description: Viết FSD theo cổng/module: quy định dùng chung, từng màn có User story và Pre/Post-condition, BR, AC, sơ đồ, xuất docx. Dùng khi gọi /viet-fsd hoặc nhờ viết FSD.
argument-hint: "<tên cổng / phân hệ> | <nguồn: BRD, design, Figma, video, biên bản>"
---

# Viết FSD: $ARGUMENTS

Vai trò: senior BA. FSD là tài liệu để Dev code và Tester viết testcase mà không phải hỏi lại.
Trả lời người dùng bằng tiếng Việt, gọi người dùng theo cách đã lưu trong memory.

## Bước 0. Nạp cấu hình

1. Thư mục Skill BA: `cat ~/.claude/skills/.skill-ba-root`. Gọi là `<SKILL_BA>`.
2. Đọc `<SKILL_BA>/_chung/van-phong.md`. Bắt buộc.
3. Chọn file cấu hình dự án trong `<SKILL_BA>/_du-an/`. Chưa có thì hỏi và tạo theo `_du-an/_mau.md`.

## Bước 0b. Tư duy và phân tích

Làm **đầu tiên**, trước khi đọc template hay viết: theo `<SKILL_BA>/_chung/tu-duy-phan-tich.md`, **mức đầy đủ**. In khối "Phân tích" ngắn cho người dùng xem. Có câu hỏi chặn thì hỏi và chờ, không có thì làm tiếp. Lưu khối này vào đầu file note.

- **Phân rã chức năng bắt buộc:** dùng lại cây phân rã của BRD nếu đã có. Chưa có thì làm theo `<SKILL_BA>/phan-ra-chuc-nang/SKILL.md` trước, dừng chờ duyệt. Danh sách màn và module của FSD phải phủ đủ các nút trong phạm vi của cây.
- Chọn sơ đồ theo `<SKILL_BA>/_chung/chon-so-do.md` mục 3 (bộ sơ đồ của FSD/SRS đầy đủ).

## Bước 1. Đọc template rồi mới đọc mẫu

1. Đọc template FSD của dự án nếu cấu hình có, không có thì `<SKILL_BA>/_mau-chung/FSD_Template.md`. Đủ mục, đúng thứ tự, đúng cột.
2. Cấu hình dự án có khóa **FSD mẫu** thì đọc để bắt giọng và độ chi tiết, không chép nội dung. Không có thì chỉ dùng template và `van-phong.md`.

## Bước 2. Đọc nguồn và dựng khung màn hình

1. Đọc BRD đã duyệt (nếu có) và mọi nguồn: design, ghi chú trên Figma, video, transcript, biên bản. Đọc cả bảng dạng ảnh.
2. Dự án chưa có danh sách màn: lập trước file **Screen flow** (theo khóa **Screen flow mẫu** ở cấu hình nếu có): bối cảnh, danh sách màn theo cổng có mã SCR, luồng chuyển màn, dữ liệu chảy giữa các cổng, chỗ design lệch nhau, câu hỏi cần chốt. Báo người dùng và chờ duyệt khung màn rồi mới viết FSD.
3. Thống nhất mã màn: `SCR-<chữ cái cổng><số>`, ví dụ SCR-A01 cho Cổng quản trị, SCR-G01 cho Cổng giáo viên.
4. **Chọn bố cục** từ danh sách màn và cổng, báo người dùng một dòng trước khi viết:
   - Dự án nhỏ, một file FSD: Quy định dùng chung là mục 1 của FSD.
   - Dự án nhiều module hoặc nhiều cổng: tách Quy định dùng chung thành file riêng `FSD - Quy định dùng chung.md` (viết trước), mỗi FSD module bỏ mục 1 và trỏ sang file đó.
   - Các mục "theo điều kiện" của template: Ảnh hưởng chéo giữa các cổng chỉ viết khi có từ hai site/cổng dùng chung dữ liệu. Luồng tích hợp giữa các module chỉ viết khi có nhiều module trao đổi dữ liệu. Lưu ý kỹ thuật chỉ viết khi có điểm tốn công hoặc rủi ro thật. Không có điều kiện thì xóa cả mục, không viết câu "không áp dụng".

## Bước 3. Hỏi trước và trong khi viết

Theo mục 7 của `van-phong.md`. Câu hỏi chưa trả lời được ghi vào file **Câu hỏi mở** của dự án (theo khóa **Câu hỏi mở mẫu** ở cấu hình nếu có), đánh mã, nhóm theo Nghiệp vụ / Phạm vi và nền tảng. Biết hành vi nhưng thiếu con số thì vẫn viết, đánh dấu [Chờ chốt] tại chỗ. Chỗ tự đề xuất đánh dấu [Đề xuất].

## Bước 4. Viết FSD

Một cổng hoặc một module một file: `FSD - <Tên cổng / module>.md`. Bố cục theo lựa chọn ở Bước 2.

Quy tắc viết (chuẩn đã chốt ở các dự án trước):

- **Quy định dùng chung** viết trước. Phần luôn có: phạm vi dữ liệu và phân quyền (chặn ở phía máy chủ), quy tắc dữ liệu chung, vòng đời trạng thái từng đối tượng, trạng thái màn hình chuẩn, phiên đăng nhập (đủ 4 bối cảnh), định dạng, tệp tải lên, tìm kiếm, sơ đồ luồng tổng thể. Phần theo điều kiện: như Bước 2.
- **Mỗi màn một mục** `SCR-xx: <Tên màn>` gồm:
  - **Tổng quan:** User story, Pre-condition, Post-condition. Có BRD thì ghi mã user story của BRD ở đầu mỗi story. Post-condition chỉ viết cho màn có làm đổi dữ liệu. Popup con dùng chung story của màn cha.
  - **Đặc tả màn hình:** ảnh design, bảng Trường thông tin, bảng Cột bảng dữ liệu, bảng Nút chức năng, Business Rules. Bảng nào màn không có thì bỏ bảng đó.
  - **Use case** chỉ viết khi màn có luồng nhiều bước hoặc nhiều nhánh ngoại lệ (import, duyệt, cấp phát...). Màn chỉ xem hoặc thêm/sửa/xóa đơn giản thì BR và AC đã đủ. Use case viết đủ điều kiện và kết quả bằng lời, không dẫn mã BR ("theo BR09").
- **Bảng Nút chức năng chỉ hai cột** Tên nút | Mô tả. Mô tả viết liền: bấm thì làm gì, mở màn nào, mang dữ liệu gì, rồi điều kiện hiện hoặc khóa (chỉ ghi khi có điều kiện). Không mô tả vị trí nút vì đã có design. Không tự đặt điều kiện khóa nút khi nghiệp vụ không cần.
- **Nhiều kích thước màn hình:** User story có từ hai bản giao diện (máy tính, tablet, điện thoại) thì theo `<SKILL_BA>/_chung/da-nen-tang.md`. Business Rules, dữ liệu, phân quyền viết một lần. Phần UI/UX của User story chỉ gồm link thiết kế cả ba bản, breakpoint và quy tắc hành vi thành phần (ẩn, hiện, co giãn, chuyển dạng, hover thành chạm). Không lặp lại bảng đặc tả cho từng bản.
- **Không dùng mã thông báo (MSG-xx), không có bảng Thông báo.** Câu thông báo viết nguyên văn tại chỗ phát sinh.
- **Không viết "theo BR-xx", "áp BR-xx", "theo mục 1.6".** Viết thẳng nội dung quy tắc tại chỗ, kể cả phải lặp lại ngắn gọn. BR con trỏ tới BR anh em ngay trên thì viết "ở trên".
- **BR mỗi BR một ý.** BR dài gộp nhiều ý thì tách BR con a, b, c. Danh sách điều kiện viết thành gạch đầu dòng con. Giữ lý do nghiệp vụ.
- Field: Loại kèm min–max ký tự, câu báo lỗi nguyên văn ở cột Mô tả.
- Mọi thao tác đổi trạng thái bản ghi: ghi bản ghi hiện ở đâu, mất khỏi đâu, cổng khác thấy gì.
- **Yêu cầu phi chức năng:** viết trong Quy định dùng chung, đi qua `<SKILL_BA>/_chung/nfr-checklist.md`, nhóm nào liên quan thì viết có con số đo được.
- **Tiêu chí chấp nhận** ở cuối file, chia theo màn, mỗi màn chia nhóm (Hiển thị, Tạo mới, Sửa, Lọc và xuất...), thêm nhóm "Dùng chung mọi màn" (phân quyền, trạng thái màn và lỗi, hết hạn phiên, định dạng chung). Checklist `- [ ]`, mỗi AC có điều kiện cụ thể và kết quả đo được.
- Tên đơn vị, vai trò, tên menu đúng như đã chốt ở cấu hình dự án.

## Bước 5. Sơ đồ

- Sơ đồ luồng tổng thể: dùng lại ảnh của BRD, hoặc vẽ bằng `/ve-so-do-lan`.
- Sơ đồ màn hình của cổng (các màn nối với nhau bằng mũi tên có nhãn thao tác): dựng file JSON theo `<SKILL_BA>/scripts/ve_so_do_lan.py` với một làn cho mỗi nhóm màn, hoặc viết Mermaid `flowchart` rồi dựng ảnh bằng `<SKILL_BA>/scripts/ve_mermaid.py` khi cần bố cục tự do. Xuất PNG, không dùng Mermaid vì FSD sẽ xuất docx.

## Bước 6. Tự review

**Có BRD** thì lập bảng đối chiếu trong file note của FSD: User story BRD | Màn (SCR) | BR | AC. Story nào chưa có màn, hoặc màn chưa có AC, thì bổ sung hoặc đưa vào danh sách đề xuất. Chưa có BRD thì bỏ bảng này.

Đọc `tu-review.md` (cùng thư mục skill này) và đi hết từng mục. Thiếu sót rõ ràng thì sửa luôn. Điểm cần thêm logic nghiệp vụ mới thì đưa vào danh sách đề xuất, hỏi người dùng trước khi thêm.

## Bước review độc lập

Sau khi tự review, giao FSD cho một agent mới review theo `<SKILL_BA>/_chung/review-doc-lap.md`. Chạy song song 2 agent (góc A và B). Lỗi rõ ràng thì sửa luôn, điểm cần BA quyết đưa vào danh sách đề xuất khi báo lại. Ghi kết quả vào note mục "Review độc lập".

## Bước 7. Xuất docx

```bash
py "<SKILL_BA>/scripts/xuat_docx.py" "<đường dẫn FSD>.md"
```

## Bước 8. Báo lại và dừng

- Link FSD md, docx, ảnh sơ đồ, file câu hỏi mở.
- Số màn, số BR, số AC. Các điểm [Đề xuất] và [Chờ chốt] quan trọng nhất.
- Danh sách đề xuất bổ sung từ bước tự review.

Dừng, chờ duyệt. Hệ thống nhiều cổng thì chỉ sang FSD cổng tiếp theo khi người dùng nói rõ đã review xong FSD này.

## Khi sửa theo góp ý

- Không tự thêm dòng vào Nhật ký thay đổi. Sửa xong hỏi người dùng một dòng "có ghi vào Nhật ký thay đổi không", đồng ý mới thêm.
- Góp ý nằm trong comment docx: trả kèm danh sách câu trả lời xếp theo thứ tự trang, mục chỉ đồng ý sửa ghi "approved".
- Đồng bộ các quyết định mới sang BRD, file câu hỏi mở, FSD cổng khác. Sửa xong xuất lại docx.
