---
name: viet-testcase
description: Viết testcase manual cho SRS/FSD/CR theo checklist và template dự án, tự nhận mẫu bảng, phủ cả case ngoài SRS. Dùng khi gọi /viet-testcase hoặc nhờ viết testcase.
argument-hint: "<đường dẫn hoặc tên SRS / mã CR> [| phạm vi: cả file / màn X]"
---

# Viết testcase manual: $ARGUMENTS

Vai trò: senior tester. Testcase phải đủ để người khác test theo mà không cần hỏi lại, và phủ cả chỗ SRS còn thiếu.
Trả lời người dùng bằng tiếng Việt, gọi người dùng theo cách đã lưu trong memory.

## Bước 0. Nạp cấu hình

1. Thư mục Skill BA: `cat ~/.claude/skills/.skill-ba-root`. Gọi là `<SKILL_BA>`.
2. Đọc `<SKILL_BA>/_chung/van-phong.md` và `tu-duy-test.md` (cùng thư mục skill này). Bắt buộc.
3. Chọn file cấu hình dự án trong `<SKILL_BA>/_du-an/`. Đọc kỹ mục Testcase và Ghi chú riêng của dự án.
4. `$ARGUMENTS` trống thì hỏi SRS nào.

## Bước 0b. Tư duy và phân tích

Làm **đầu tiên**, trước khi đọc template hay viết: theo `<SKILL_BA>/_chung/tu-duy-phan-tich.md`, **mức đầy đủ**. In khối "Phân tích" ngắn cho người dùng xem. Có câu hỏi chặn thì hỏi và chờ, không có thì làm tiếp. Lưu khối này vào đầu file note.

- Có cây phân rã chức năng thì dùng để soát độ phủ: mỗi nút trong phạm vi có ít nhất một nhóm case.

## Bước 1. Nạp checklist theo đúng thứ tự

1. Đọc **File điều phối checklist** của dự án. File này quyết định thứ tự chạy, file nào bật, mục nào tắt, mẫu bảng, quy tắc nâng High. Làm đúng theo nó, không đảo thứ tự, không tự bật mục đã tắt.
2. **Dự án chưa có file điều phối: tự nhận diện, không hỏi người dùng chọn checklist.**
   1. Đọc `<SKILL_BA>/_mau-chung/checklist/_danh-muc.md` (thư mục checklist theo khóa **Thư mục checklist dùng chung** ở cấu hình, để trống thì dùng thư mục này).
   2. Dò dấu hiệu trong tài liệu đặc tả (SRS, FSD, CR, BRD) theo mục 2, 3, 4 của danh mục: bật tầng 0, tầng 1 (từng nhóm theo dấu hiệu ở đầu nhóm), các file năng lực và bộ domain khớp dấu hiệu.
   3. Tự tạo file điều phối theo khóa **File điều phối mẫu** ở cấu hình, không có thì theo `<SKILL_BA>/_mau-chung/00-checklist-ap-dung_mau.md`. Mỗi dòng bật ghi kèm dấu hiệu đã thấy trong tài liệu.
   4. **Năng lực hoặc domain khớp dấu hiệu mà chưa có bộ** (danh mục mục 3 trạng thái chưa tách, hoặc mục 4): dừng và nhắc người dùng đúng mẫu ở mục 5 của danh mục, kèm độ phủ ước tính và 8 đến 10 rủi ro chính dự kiến. Người dùng chọn tạo bộ thì dựng bộ, review độc lập, chờ duyệt, thêm vào danh mục rồi mới sinh case. Chọn chạy tạm thì ghi khoảng trống vào note.
   5. Không có phần nào thiếu bộ: báo một dòng danh sách checklist đã bật rồi làm tiếp, không chờ duyệt.
3. Đọc **Template testcase** trọn vẹn (cấu hình, hoặc `<SKILL_BA>/_mau-chung/Testcase_Template.md`). Mọi quy tắc trong đó là bắt buộc: ngôn ngữ, cấu trúc nhóm 2 cấp, đặt tên control, các nhóm kiểm thử bắt buộc, quy tắc viết kết quả mong muốn, cách đọc bảng đặc tả field.
4. Đọc các checklist được bật, theo đúng mục được bật. Luôn gồm `<SKILL_BA>/_mau-chung/checklist/QA-Business-Risk-Core-Checklist.md` (tầng 1). Bản ghi hiện ở từ hai portal, vai trò hoặc nơi xuất trở lên thì lập bảng đối chiếu theo Testcase_Template Mục 27.9.
5. **Chọn mẫu bảng testcase**, xét theo thứ tự, gặp cái nào thì dùng cái đó:
   1. Khóa **Mẫu bảng testcase** trong cấu hình dự án.
   2. Dự án đã có file testcase (grep `*.test.md`, `*.testcase.md` trong thư mục dự án): đọc dòng tiêu đề bảng, cách đặt tên file, cách nhóm, thang ưu tiên của một file gần nhất và làm đúng như vậy. Lưu lại vào cấu hình dự án để lần sau khỏi dò.
   3. Chưa có gì: dùng `<SKILL_BA>/_mau-chung/Testcase_Mau-bang-mac-dinh.md` (mẫu mặc định: 10 cột, P0/P1/P2, có Mã SRS và Mã UC - TKCT, không có cột Automation).

   Báo người dùng một dòng đang dùng mẫu nào. Template testcase hay checklist dùng chung có mẫu bảng khác thì vẫn theo mẫu vừa chọn, chỉ quy đổi thang ưu tiên cho khớp (P0 ↔ High, P1 ↔ Medium, P2 ↔ Low).

## Chế độ CR (đầu vào là một CR đã duyệt)

Gọi bằng `/viet-testcase CR-YYMM-NNN`, thường từ Bước 9 của `/viet-cr`. Chỉ chạy khi người dùng đã duyệt CR. Các bước khác của skill vẫn làm đủ, riêng các điểm sau khác chế độ thường:

1. **File:** `CR-YYMM-NNN.test.md` đặt cạnh CR, cùng mẫu bảng của dự án (chọn theo Bước 1.5). File này giữ lại sau khi gộp để tra lịch sử.
2. **Phạm vi:** chạy đủ checklist theo thứ tự nhưng chỉ cho **phần mới hoặc thay đổi** của CR. Mọi AC ở mục 4 của CR có ít nhất một case. Hành vi giữ nguyên thì không viết case mới, đưa vào phần hồi quy.
   **Lọc nhóm phi chức năng:** chỉ sinh nhóm dưới đây khi CR thật sự chạm tới, và chỉ cho đúng phần CR đổi:

   | Nhóm | Chỉ sinh khi CR... |
   |:---|:---|
   | Lỗi mạng, lỗi 5xx khi lưu | Thêm hoặc đổi thao tác lưu, gửi, thanh toán, tải tệp, hay gọi một API hoặc hệ thống ngoài mới |
   | Bấm nhiều lần, hai người cùng sửa | Đổi chỗ có tiền, trạng thái, số lượng |
   | Responsive | Đổi bố cục hoặc thêm thành phần giao diện. Chỉ kiểm thành phần đó, ở các khổ dự án hỗ trợ |
   | Phân quyền, lộ dữ liệu | Thêm field, thêm màn, hoặc đổi người được xem, được làm |
   | Hiệu năng | Có con số về thời gian, số lượng bản ghi, hoặc thêm danh sách, xuất file lớn |
   | Hết phiên, trợ năng, an ninh hộp đen chung | Bỏ |

   Đầu file ghi một dòng "Nhóm không kiểm vì CR không chạm tới: …" để biết bỏ có chủ ý. Các nhóm này để cho đợt hồi quy toàn hệ thống hoặc trước khi lên Production.
3. **Mã tạm:** `TC-CR<YYMMNNN>-<số>`, ví dụ `TC-CR2610011-001`, để không trùng mã trong `.test.md` của SRS. Mã chính thức được cấp khi gộp bằng `/cap-nhat-srs`.
4. **Chia phần theo SRS đích:** mỗi SRS trong bảng "Tài liệu bị ảnh hưởng" của CR là một phần `# PHẦN A — <tên SRS>`, ghi đường dẫn `.test.md` sẽ gộp vào và nhóm đích. Trong mỗi phần nhóm case theo cấp như file testcase của SRS đó.
5. **Loại gộp:** cột Ghi chú của mỗi case mở đầu bằng một trong ba dấu:
   - `Gộp: Mới` thêm case mới.
   - `Gộp: Sửa TC-xxx` thay nội dung case cũ TC-xxx (hành vi cũ bị CR đổi), giữ mã cũ.
   - Case cũ bị CR làm lỗi thời mà không có case thay thì liệt kê ở bảng "Case cũ bỏ khi gộp" cuối mỗi phần: Mã TC | Lý do.
   Tra mã case cũ bằng cách đọc `.test.md` của SRS đích, đối chiếu với phần "Thay thế một phần" và các mục sửa của CR.
6. **Phần hồi quy** cuối file: bảng Mã TC trong SRS | File | Lý do chạy lại. Chọn các case cũ quanh chỗ thay đổi: cùng màn, cùng thành phần dùng chung, luồng trước và sau, màn khác dùng chung dữ liệu. Chỉ ghi mã, không chép nội dung.
7. **Automation:** cột Automation Status chỉ ghi gợi ý tầng (E2E / API / Manual only). Chưa lập `.auto.md`, chưa viết script, vì mã còn là mã tạm. Trong sprint muốn kiểm bản dev vừa làm thì dùng `/viet-automation` chế độ B với danh sách case này.
8. **Testcase List trên sheet:** chưa đẩy. Chỉ đẩy sau khi gộp vào SRS.
9. Đầu file ghi: Mã CR, ngày sinh, trạng thái **Chưa gộp**, tổng số case theo mức ưu tiên và theo phần.

## Bước 2. Đọc nguồn

1. SRS trọn vẹn, kèm `.note.md`. CR đã duyệt đụng tới màn này. Quy tắc nghiệp vụ liên quan.
2. File testcase cũ nếu có: giữ mã TC còn đúng, TC mới lấy số kế tiếp, TC lỗi thời thì xóa và ghi vào note.
3. Thiết kế hoặc hệ thống thật nếu cần làm rõ hành vi (chỉ xem).
4. Lập trong note: rủi ro trọng tâm của chức năng, bảng tham số (con số, mốc thời gian, giới hạn), mâu thuẫn giữa các tài liệu.

## Bước 3. Hỏi điểm chặn

- Tham số trống hoặc tài liệu mâu thuẫn mà ảnh hưởng tới kết quả mong muốn: hỏi trước, không viết case đoán mò.
- Chưa biết chức năng làm gì: hỏi. Biết hành vi nhưng thiếu con số: vẫn viết case, Ghi chú "chờ chốt tham số X", câu hỏi ghi vào note.
- Kết quả mong muốn theo SRS, CR và hệ thống đang chạy. Không tự sửa SRS, CR khi đang viết testcase.

## Bước 4. Sinh case

Chạy lần lượt các bước của file điều phối. Ở mỗi màn, mỗi quy tắc:

1. Sinh case từ SRS/FSD: mọi BR và AC có ít nhất một case. Ghi mã truy vết theo mẫu bảng đã chọn: mẫu có cột Automation ghi mã BR/AC trong ngoặc ở cuối Kết quả mong muốn, mẫu mặc định ghi mã màn ở cột Mã SRS và mã use case ở cột Mã UC - TKCT.
2. Sinh case **ngoài SRS** theo `tu-duy-test.md`. Case nào SRS chưa nói kết quả: kết quả lấy theo hệ thống đang chạy hoặc hành vi hợp lý của màn tương tự, và ghi vào note mục "SRS thiếu" để BA bổ sung. Chưa biết hệ thống làm gì thì đưa vào danh sách câu hỏi, chưa viết kết quả.
3. Mỗi quy tắc viết đủ hai lớp: hệ thống xử lý đúng, và người dùng nhìn thấy đúng trên màn (con số, trạng thái, thông báo có cập nhật không).
4. Điền bảng đúng mẫu bảng đã chọn ở Bước 1. Mức ưu tiên theo quy tắc nâng mức cao nhất của dự án. Kết quả thực tế để trống. Ghi chú chỉ điền khi có điều cần lưu ý thật.

Cách viết từng ô:

- **Mục đích:** một câu nói rõ kiểm tra gì, trong điều kiện nào.
- **Tiền điều kiện:** vai trò đăng nhập, trạng thái bản ghi, dữ liệu cần có, con số cụ thể.
- **Các bước:** đánh số, mỗi bước một thao tác, gọi đúng tên nút, tên field như trên giao diện. Xuống dòng bằng `<br>`.
- **Kết quả mong muốn:** cụ thể, đo được: chữ thông báo nguyên văn, số bản ghi, trạng thái mới, bản ghi xuất hiện ở đâu. Lọc và xuất viết "đúng các bản ghi thỏa điều kiện, đủ và chỉ những bản ghi đó".

## Bước 5. Rà soát cuối

1. Chạy bảng rà soát cuối của file điều phối (6 trạng thái màn hình, các câu hỏi rà soát).
2. Đối chiếu: liệt kê mọi BR/AC của SRS, đánh dấu mã TC phủ. BR/AC nào chưa có TC thì viết thêm. AC nào không sinh được case đo được thì ghi note là AC chưa đạt.
3. Đếm số case theo mức ưu tiên, cập nhật bảng tổng hợp ở đầu file.
4. **Đo độ phủ:** chấm bảng 19 nhóm ở mục 6 của `_danh-muc.md` cho chức năng này: nhóm không liên quan bỏ khỏi mẫu số, nhóm còn mỏng thì bổ sung case từ checklist tương ứng. Ghi bảng vào note. Dưới 95% thì ghi rõ nhóm nào thiếu, thiếu vì chưa có bộ (đã nhắc ở bước 1) hay vì tài liệu chưa đủ (câu hỏi chặn).
5. Rà văn phong theo mục 8 của `van-phong.md`.
6. Định dạng đúng mẫu để công cụ đồng bộ đọc được (mã TC dạng `TC-<MÃ>-<số>`, nhóm theo tiêu đề `##` / `###`).

## Bước review độc lập

Sau khi tự review, giao bộ testcase (chỉ khi có từ 30 case trở lên), nguồn đối chiếu là SRS/FSD/CR; agent tìm BR/AC chưa có case, case trùng, kết quả mong muốn không đo được, nhóm case còn thiếu theo `tu-duy-test.md` cho một agent mới review theo `<SKILL_BA>/_chung/review-doc-lap.md`. Lỗi rõ ràng thì sửa luôn, điểm cần BA quyết đưa vào danh sách đề xuất khi báo lại. Ghi kết quả vào note mục "Review độc lập".

## Bước 6. Viết note

`<tên>.note.md` cạnh SRS (có rồi thì cập nhật): rủi ro trọng tâm, bảng tham số, mâu thuẫn tài liệu, SRS thiếu, câu hỏi chờ chốt, bảng đối chiếu BR/AC → TC, bảng đối chiếu checklist đã chạy.

## Bước 7. Báo lại và dừng

- Link file testcase và note. Số case theo từng mức ưu tiên. Số case ngoài SRS.
- Các điểm SRS thiếu và câu hỏi chờ chốt (tối đa 5 điểm quan trọng nhất).

Dừng, chờ người dùng duyệt. Duyệt xong, chỉ khi cấu hình dự án có **Repo automation** thì gợi ý chạy `/viet-automation`.
