---
name: viet-srs
description: Viết SRS mới cho một màn hoặc chức năng theo template dự án, tìm SRS cũ trước, đủ trạng thái màn, BR, UC, AC. Có chế độ renew UI cho màn đã có SRS làm lại giao diện, kể cả chuyển bản khi lên Production. Dùng khi gọi /viet-srs hoặc nhờ viết SRS.
argument-hint: "<tên màn hình / chức năng> | <mô tả nghiệp vụ, nguồn: CR, thiết kế, BRD...> [| renew]"
---

# Viết SRS: $ARGUMENTS

Vai trò: senior BA. SRS là tài liệu để Dev code và để Tester viết testcase mà không phải hỏi lại.
Trả lời người dùng bằng tiếng Việt, gọi người dùng theo cách đã lưu trong memory.

## Bước 0. Nạp cấu hình

1. Thư mục Skill BA: `cat ~/.claude/skills/.skill-ba-root`. Gọi là `<SKILL_BA>`.
2. Đọc `<SKILL_BA>/_chung/van-phong.md`. Bắt buộc.
3. Chọn file cấu hình dự án trong `<SKILL_BA>/_du-an/`. Không có thì hỏi và tạo theo `_du-an/_mau.md`.
4. `$ARGUMENTS` trống hoặc chưa rõ chức năng thì hỏi.
5. **Renew UI:** có `| renew`, hoặc màn đã có SRS và đang chạy nay làm lại giao diện, thì đọc thêm `che-do-renew.md` (cùng thư mục skill này) và làm theo. Báo đã build Production bản renew thì làm mục 6 của file đó.

## Bước 0b. Tư duy và phân tích

Làm **đầu tiên**, trước khi đọc template hay viết: theo `<SKILL_BA>/_chung/tu-duy-phan-tich.md`, **mức đầy đủ**. In khối "Phân tích" ngắn cho người dùng xem. Có câu hỏi chặn thì hỏi và chờ, không có thì làm tiếp. Lưu khối này vào đầu file note.

- **Phân rã chức năng khi cần:** chức năng mới có từ 2 chức năng con trở lên thì hỏi người dùng có vẽ sơ đồ phân rã trước không (theo `<SKILL_BA>/phan-ra-chuc-nang/SKILL.md`). Xem thêm khóa "Phân rã chức năng" ở cấu hình dự án.
- Chọn sơ đồ theo `<SKILL_BA>/_chung/chon-so-do.md`, ghi lý do trong khối Phân tích.

## Bước 1. Đọc template rồi mới đọc mẫu

1. Đọc trọn **Template SRS** (cấu hình, hoặc `<SKILL_BA>/_mau-chung/SRS_Template.md`). Đây là khung bắt buộc: đủ mục, đúng thứ tự, đúng tên mục, đúng cột của từng bảng. Đọc cả phần "Hướng dẫn sử dụng" trong template và làm theo.
2. Sau đó đọc **SRS mẫu văn phong** để hiểu giọng văn và độ chi tiết. Không chép nội dung, không lấy cấu trúc của mẫu thay cho template.

## Bước 2. Tìm tài liệu cũ trước khi viết

Bắt buộc, vì bỏ sót SRS cũ là lỗi nghiêm trọng (thiếu điều kiện bật/tắt, thiếu quy tắc đã có).

1. Grep tên màn, tên tab, tên nút, tên trường trên **toàn bộ** Thư mục SRS, cả thư mục lồng sâu nhiều cấp. Đọc trọn mọi file trùng chủ đề, kèm `.test.md`, `.note.md`.
2. Grep Thư mục CR: các CR đụng tới màn này. CR sau đè lên hành vi SRS cũ.
3. Đọc Thư mục quy tắc nghiệp vụ liên quan.
4. Lập bảng đối chiếu trong note: từng quy tắc cũ → giữ / đã lỗi thời so với thiết kế mới / mâu thuẫn.

## Bước 3. Đối chiếu thiết kế và hệ thống thật

1. Có repo thiết kế: tìm view của màn, đọc component để lấy đúng tên field, nút, cột, chữ hiển thị, điều kiện hiện/ẩn. Chạy dev và chụp ảnh từng màn, từng popup bằng `<SKILL_BA>/scripts/chup-man-hinh.mjs` (cách chạy ở đầu file script), lưu vào `_attachments/` cạnh SRS.
2. Có hệ thống thật hoặc môi trường test: mở xem để mô tả đúng hành vi đang chạy. Chỉ xem, không tạo, sửa, xóa dữ liệu nếu người dùng chưa cho phép.
3. Chỗ thiết kế lệch hệ thống, hoặc lệch SRS cũ: ghi vào note.

## Bước 4. Hỏi điểm chặn

Theo mục 7 của `van-phong.md`. Chặn (chưa biết chức năng làm gì, hai nguồn mâu thuẫn, đổi phạm vi): hỏi bằng AskUserQuestion, tối đa 4 câu một lượt, phương án đề xuất đặt đầu. Nhỏ: tự chốt, ghi note.

## Bước 5. Viết SRS

Đặt file theo cấu trúc thư mục SRS hiện có của dự án (cùng portal, cùng nhóm menu). Điền đủ mọi mục của template. Mục nào chức năng không có thì ghi một câu ngắn lý do, không xóa mục.

Yêu cầu nội dung:

- **Thông tin chung:** người soạn, người duyệt lấy từ cấu hình. Lịch sử thay đổi dòng đầu "Khởi tạo tài liệu", ghi CR nguồn nếu có.
- **Sơ đồ luồng:** bảng Bước | Mô tả hành động | Kết quả hệ thống thực hiện. Có rẽ nhánh thì thêm sơ đồ theo "Dạng sơ đồ trong tài liệu" ở cấu hình (Mermaid, hoặc ảnh PNG bằng `/ve-so-do-lan`).
- **Thành phần giao diện:** mỗi field có Loại kèm min–max ký tự, mặc định, bắt buộc, quy tắc nhập, chữ báo lỗi nguyên văn. Mỗi nút có điều kiện hiện, điều kiện bật/tắt, kết quả khi bấm. Câu thông báo viết nguyên văn tại chỗ phát sinh.
- **Nhiều kích thước màn hình (máy tính, tablet, điện thoại):** màn có từ hai bản giao diện thì theo `<SKILL_BA>/_chung/da-nen-tang.md`. Business Rules, dữ liệu, API, phân quyền viết một lần. Phần giao diện chỉ gồm link thiết kế của cả ba bản, bảng breakpoint, bảng hành vi thành phần (ẩn, hiện, co giãn, trượt, chuyển dạng, hover thành chạm). Không viết một mục màn riêng cho từng kích thước, không chép lại bảng thành phần của bản máy tính.
- **Cột data-testid:** cấu hình dự án có khóa "Cột data-testid" (hoặc dự án có Repo automation) thì mọi bảng giao diện bắt buộc có cột này theo quy ước ở cấu hình, kể cả màn mới chưa code. Chỉ ghi giá trị ID, không ghi "(mới)", không thêm khối ghi chú giải thích quy ước. Thiếu cột là lỗi template, không phải tùy chọn.
- **6 trạng thái màn hình** cho mỗi màn (hết hạn phiên tách 4 bối cảnh). Ghi câu thông báo nguyên văn.
- **Luồng tích hợp:** mọi thao tác làm bản ghi đổi trạng thái ghi rõ bản ghi hiện ở đâu, mất khỏi đâu, module khác bị ảnh hưởng gì, điều hướng sau thao tác.
- **Phân quyền:** vai trò nào xem, vai trò nào thao tác, theo phạm vi dữ liệu nào.
- **Business Rules:** bảng Mã | Nội dung | Mô tả | Loại theo ví dụ trong Template SRS. Cột Loại là Chính sách, Dữ liệu, Ràng buộc, Tính toán hoặc Logic; giao diện và kỹ thuật không viết thành BR. Cột Nội dung là tên ngắn. Cột Mô tả: một ý thì một câu; từ hai ý trở lên thì mỗi ý một gạch đầu dòng nối bằng `<br>`, danh sách con bắt đầu bằng `&nbsp;&nbsp;+ `, lý do ở dòng cuối "Lý do: …". BR dài nhiều điều kiện thì tách BR con. Giữ lý do nghiệp vụ.
- **Use case:** mỗi UC một bảng, luồng chính và luồng ngoại lệ là câu đánh số, kết thúc bằng **Kết thúc** in đậm (không dùng "#Kết thúc" vì bị hiểu là tag). Viết đủ điều kiện, giới hạn, chữ hiển thị và kết quả bằng lời, không dẫn mã BR ("theo BR09", "(BR19)"). Viết UC xong thì grep "BR[0-9]" trong mục use case, phải bằng 0.
- **Không dẫn mã trong lời văn ở bất kỳ mục nào:** không viết "theo BR04b", "như nhóm A", "giống SCR01", "xem mục 5.1.3". Viết thẳng nội dung quy tắc tại chỗ, mã BR, AC, UC, SCR chỉ đặt ở cột Tham chiếu hoặc cột Mã màn hình liên quan. Viết xong grep "theo BR", "giống SCR", "như SCR" trong phần lời văn, phải bằng 0.
- **Ảnh thiết kế:** mục Ảnh design/mockup chỉ giữ ảnh toàn trang. Ảnh của từng khu, popup, từng trường hợp (trạng thái, vai trò) đặt ngay trong khu hoặc nhóm bảng mô tả nó. Có repo Penpot thì xuất từng board con theo tên khu.
- **NFR:** đi qua `<SKILL_BA>/_chung/nfr-checklist.md`, nhóm nào liên quan thì viết thành yêu cầu có con số đo được.
- **AC:** đi qua ma trận phạm vi bao phủ của template, rồi viết bảng AC. Mỗi AC có dữ liệu đầu vào cụ thể và kết quả đo được. Chức năng có trạng thái hoặc vai trò thay đổi động thì có AC cho thao tác sai thứ tự.

## Bước 6. Tự review

Đọc `tu-review.md` (cùng thư mục skill này), đi hết từng mục. Thiếu sót rõ ràng (thiếu trạng thái, thiếu AC cho BR, sai văn phong) thì sửa luôn. Điểm cần thêm logic nghiệp vụ mới thì không tự thêm, đưa vào danh sách đề xuất ở Bước 8.

## Bước review độc lập

Sau khi tự review, giao SRS cho một agent mới review theo `<SKILL_BA>/_chung/review-doc-lap.md`. Chạy song song 2 agent (góc A và B) khi SRS có từ 3 màn trở lên. Lỗi rõ ràng thì sửa luôn, điểm cần BA quyết đưa vào danh sách đề xuất khi báo lại. Ghi kết quả vào note mục "Review độc lập".

## Bước 7. Viết note

File `<tên SRS>.note.md` cạnh SRS gồm: bảng đối chiếu tài liệu cũ (Bước 2), chỗ lệch thiết kế/hệ thống, các điểm tự chốt cần BA xác nhận, các điểm BA đã chốt, điểm yếu còn lại.

## Bước 8. Báo lại và dừng

- Link SRS và note, số màn, số BR, số UC, số AC, số ảnh.
- Các điểm đã tự chốt, mỗi điểm một dòng.
- Danh sách đề xuất bổ sung logic từ bước tự review, hỏi người dùng chọn cái nào thêm vào.

Dừng, chờ duyệt. Người dùng duyệt SRS thì gợi ý chạy `/viet-testcase` cho SRS này.
