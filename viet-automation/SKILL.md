---
name: viet-automation
description: Automation test theo hai chế độ. Chế độ A - đã có bộ testcase duyệt - lập .auto.md và viết script còn thiếu theo quy ước repo automation. Chế độ B - dev vừa code xong, chưa có testcase - dùng Playwright kiểm thẳng bản đã deploy, phủ rộng chứ không chỉ happy path - đối chiếu UI với design và FSD, validate, CRUD, biên, dữ liệu kỳ quặc, trạng thái lỗi, hết phiên, phân quyền, ảnh hưởng chéo - chụp lại mọi lỗi, xuất file kết quả, quay video luồng E2E có chú thích khi được yêu cầu, chuyển sang /log-bug. Dùng khi gọi /viet-automation, nhờ làm automation cho bộ testcase, hoặc nhờ dùng automation kiểm hệ thống dev vừa làm xong.
argument-hint: "<đường dẫn .test.md> | hoặc: kiểm <cổng / màn> trên <link hệ thống> [| có design: <thư mục>]"
---

# Automation test: $ARGUMENTS

Trả lời người dùng bằng tiếng Việt, gọi người dùng theo cách đã lưu trong memory.

## Bước 0. Nạp cấu hình và chọn chế độ

1. Thư mục Skill BA: `cat ~/.claude/skills/.skill-ba-root`. Gọi là `<SKILL_BA>`.
2. Đọc `<SKILL_BA>/_chung/van-phong.md`.
3. Chọn file cấu hình dự án trong `<SKILL_BA>/_du-an/`. Đọc mục Automation và Ghi chú riêng của dự án.
4. Chọn chế độ, báo người dùng một dòng:

| Chế độ | Khi nào |
|:---|:---|
| **A. Viết script từ testcase** | Đã có bộ testcase manual được duyệt, có repo automation |
| **B. Kiểm hệ thống khi chưa có testcase** | Dev vừa code xong, có link hệ thống đã deploy, cần tìm lỗi sớm mà chưa có testcase |

Không rõ thì hỏi.

---

# Chế độ A. Viết script từ testcase

## A0. Đọc quy ước

1. Đọc **Quy ước của repo** (thường là `CLAUDE.md` của repo automation). Khi skill này và quy ước của repo lệch nhau, theo repo.
2. Đọc các checklist automation mà file điều phối checklist bật (bảng chọn tầng, kỹ thuật, câu hỏi rà soát). Không có thì dùng `<SKILL_BA>/_mau-chung/Automation_Checklist.md`.

## A0b. Tư duy và phân tích

Làm **đầu tiên**, trước khi đọc template hay viết: theo `<SKILL_BA>/_chung/tu-duy-phan-tich.md`, **mức gọn**. In khối "Phân tích" ngắn cho người dùng xem. Có câu hỏi chặn thì hỏi và chờ, không có thì làm tiếp. Lưu khối này vào đầu file note.

## A1. Đọc testcase

Đọc `.test.md`, `.note.md` và `.auto.md` cũ nếu có. Chỉ làm khi bộ testcase manual đã được người dùng duyệt. Chưa chắc thì hỏi.

## A2. Lập `.auto.md`

Cạnh `.test.md`, ba phần:

1. **Bảng Manual TC → Automation Layer**: mỗi TC một dòng. Tầng: E2E, API, Security, Performance, Visual, Manual only. Chọn theo bảng chọn tầng của checklist. Gợi ý mặc định: luồng chính, hậu quả sau thao tác, lọc nhiều điều kiện, xuất tải tệp (đọc tệp, so từng ô) → E2E. Validate field, phân quyền, đồng thời, thao tác bị giao diện chặn → API. Cảm quan, copy/paste, khám phá → Manual only.
2. **Danh sách script theo tầng**: `- [ ] TC-…: <tên test mô tả hành vi và kết quả>`.
3. **Ghi chú automation**: dữ liệu cần chuẩn bị, vùng cần che khi so ảnh, phụ thuộc dịch vụ ngoài, tài khoản vai trò cần có.

Thêm, sửa, xóa TC ở `.test.md` thì sửa dòng tương ứng ở `.auto.md` cùng lúc.

## A3. Viết script còn thiếu

Có repo automation thì làm luôn trong lượt này, không dừng ở trạng thái "chưa làm":

1. Tìm spec, page object có sẵn của màn. Dùng lại, viết theo đúng quy ước locator, cấu trúc test, dữ liệu test của repo.
2. Mọi TC không phải Manual only mà chưa có script thì viết script.
3. Thiếu điều kiện chạy (tài khoản vai trò tùy biến, dữ liệu đặc biệt) vẫn viết script: đọc điều kiện từ `.env` hoặc dữ liệu thật, tự bỏ qua kèm lý do khi chưa đủ.
4. Lỗi sản phẩm đã biết: để test đỏ theo cách repo quy định, không sửa kết quả mong muốn cho xanh.
5. Chỉ để Manual only khi thật sự không tự động được.

## A4. Chạy và phân loại

1. Chạy spec trên **Môi trường chạy** ở cấu hình, theo lệnh trong quy ước repo. Chạy lâu thì chạy nền.
2. Mỗi test đỏ phân loại một trong bốn: lỗi đã log / lỗi sản phẩm mới / thiếu dữ liệu môi trường / test viết sai (sửa test, chạy lại).
3. Lỗi sản phẩm mới: tái hiện độc lập, chưa rõ là lỗi hay đúng nghiệp vụ thì hỏi người dùng trước khi log.
4. Cập nhật cột Automation Status, Automation Link trong `.test.md` và trạng thái ở `.auto.md`.

## A5. Báo lại và dừng

- Link `.auto.md` và các spec đã sửa. Số TC theo tầng, số đã có script, số Manual only.
- Kết quả chạy: Pass / Fail / bỏ qua, mỗi Fail đã phân loại.
- TC tự bỏ qua vì thiếu điều kiện, kèm điều kiện cần có.

Dừng. Đồng bộ lên sheet, log bug, commit và push chỉ làm khi người dùng yêu cầu hoặc theo quy trình của repo (ví dụ `/lam-module`).

---

# Chế độ B. Kiểm hệ thống khi chưa có testcase

Đọc trọn `kiem-thu-chua-co-testcase.md` và `mau-ket-qua-va-video.md` (cùng thư mục skill) trước khi làm. Đây là quy trình đã dùng cho một dự án trước, cài đặt mẫu ở thư mục Automation của dự án mẫu (đường dẫn ghi ở `_du-an/<dự án>.md`, mục Automation).

Không chỉ chạy happy path hay E2E. Mỗi màn phải phủ đủ: đối chiếu giao diện (với design nếu có, và với FSD), validate, thêm sửa xóa, danh sách, trạng thái lỗi, phiên, phân quyền, an ninh hộp đen, ảnh hưởng chéo, và các case phi logic theo tư duy test.

## B0b. Tư duy và phân tích

Theo `<SKILL_BA>/_chung/tu-duy-phan-tich.md`, **mức gọn**, cộng 3 đến 5 câu "hệ thống này hỏng ở đâu thì thiệt hại nhất" (mục 2 của `kiem-thu-chua-co-testcase.md`). In khối này cho người dùng xem, lưu vào đầu file kết quả.

## B1. Chuẩn bị, hỏi trước khi chạy

1. Đọc FSD (BR và tiêu chí chấp nhận), file note, file câu hỏi mở. Không có FSD thì làm theo nhánh "Không có FSD" ở mục 1 của `kiem-thu-chua-co-testcase.md`. Đọc design hoặc mockup nếu có: **giải nén và liệt kê hết** các tệp.
2. Đọc `Testcase_Template.md` của dự án (hoặc `<SKILL_BA>/_mau-chung/Testcase_Template.md`), các checklist file điều phối bật, và `<SKILL_BA>/viet-testcase/tu-duy-test.md`. Luôn đọc thêm tầng 1 `<SKILL_BA>/_mau-chung/checklist/QA-Business-Risk-Core-Checklist.md`. Dự án chưa có file điều phối thì tự nhận diện theo `<SKILL_BA>/_mau-chung/checklist/_danh-muc.md` đúng như bước 1.2 của `<SKILL_BA>/viet-testcase/SKILL.md`: dò dấu hiệu, tự bật checklist, gặp năng lực hoặc domain chưa có bộ thì dừng và nhắc người dùng theo mục 5 của danh mục.
3. Đọc bảng khóa **Chế độ B** trong mục Automation của cấu hình dự án. Chỉ hỏi những khóa còn trống, gom vào một lần, rồi ghi câu trả lời ngược lại vào cấu hình:
   - Link từng cổng, file chứa thông tin đăng nhập (đọc từ file, **tuyệt đối không in ra, không ghi vào script hay kết quả**).
   - Email test gốc để tạo tài khoản dạng `+alias`; được gửi email thật không; kịch bản đọc email bằng cách nào (hộp thư bắt giữ của môi trường test, IMAP hoặc Gmail API bằng khóa người dùng cấp, hay người dùng tự dán liên kết vào file).
   - Khóa tài khoản theo tài khoản hay theo IP.
   - Thứ tự chạy (ví dụ cổng quản trị trước, rồi đăng nhập, rồi cổng còn lại, rồi ảnh hưởng chéo).
   - Thao tác cấm trên môi trường; cách dọn dữ liệu thử (xóa qua giao diện hay nhờ dev), giới hạn số bản ghi được tạo.
   - Người dùng có dùng điện thoại, Safari không.
4. Tạo thư mục Automation trong dự án: chép `mau_chung.py` của skill thành `chung.py`, viết `cau_hinh.py` đọc thông tin đăng nhập, tạo `.gitignore` (mục 6 Bảo mật), các kịch bản theo đợt, `ket-qua/`, `tep-mau/` (tệp thử mỗi định dạng, tệp biên dung lượng theo cả hai cách hiểu MB, tệp đổi đuôi, tệp nhiều trang, nhiều slide, nhiều sheet).

## B2. Bản đồ phủ, đưa người dùng duyệt

Lập bảng theo mục 3 của `kiem-thu-chua-co-testcase.md`: mỗi màn, mỗi nhóm một dòng, với các cột Mục sẽ kiểm, Nguồn (mã BR, dòng AC, mục template, hoặc "tư duy test"), Dữ liệu cần dựng, Kỹ thuật. Mục không áp dụng ghi lý do. Thêm các case phi logic chọn từ mục 4. Xếp nhóm theo ba lớp ưu tiên và áp tiêu chí dừng ở mục 2.

Đưa người dùng duyệt nhanh phạm vi, không cần viết testcase chi tiết. Nói rõ nhược điểm: người dùng duyệt mong muốn sau, trên file kết quả, chứ không duyệt trước từng case.

## B3. Chạy theo đợt

1. Mỗi đợt một kịch bản Playwright dùng `chung.py`, nhận tham số chọn nhóm. Mỗi mục kiểm gọi `ghi()` với một trong sáu giá trị Kết quả ở `mau-ket-qua-va-video.md`. Mã mục ổn định, không đánh lại giữa các đợt.
2. Tuân thủ mục 6 Quy tắc khi chạy của `kiem-thu-chua-co-testcase.md`: bảo mật, dữ liệu, email và mật khẩu, chờ và ổn định, bằng chứng, chống báo nhầm.
3. Lỗi mạng, lỗi máy chủ: chặn request bằng `page.route`. Hết phiên: xóa đúng chỗ lưu phiên (cookie hay localStorage). Phiên tự hết hạn theo thời gian thật thì ghi Chưa kiểm.
4. Mỗi nhóm bật trace và theo dõi lỗi ngầm (`theo_doi`). Mỗi mục Lỗi có ảnh 2x đúng lúc lỗi.
5. Hết mỗi đợt: ghép ảnh thành tờ xem nhanh, rà bằng mắt; **xác minh lại từng mục Lỗi và mục Đạt đáng ngờ** trước khi báo. Sửa kịch bản nếu nó đánh giá sai, chạy lại, ghi vào mục Sự cố trong lúc chạy.

## B4. Đối chiếu giao diện với design

Có design thì làm theo mục 5 của `kiem-thu-chua-co-testcase.md`, ghi ra `Đối chiếu giao diện với design.md`. Không có design thì vẫn đối chiếu giao diện với bảng trường, bảng nút, bảng cột của FSD.

## B5. File kết quả

Viết `Kết quả kiểm thử tự động - <cổng>.md` theo mẫu, gộp JSON và ảnh của các đợt vào `ket-qua/tong-hop/`. Mỗi lỗi có mức độ theo bảng Mức độ lỗi và đủ trường để chuyển sang `/log-bug`. Chỗ FSD không nói rõ ghi "Cần xác nhận". Chỗ hệ thống làm khác FSD: hỏi người dùng giữ theo hệ thống và cập nhật FSD, hay báo lỗi. Mục người dùng chốt chấp nhận thì chuyển Đóng kèm ngày, để lần chạy sau không báo lại.

## B6. Video luồng E2E (chỉ khi được yêu cầu)

Người dùng chưa yêu cầu thì **không quay**, chỉ hỏi một dòng ở cuối báo cáo. Có yêu cầu thì làm theo mục 2 của `mau-ket-qua-va-video.md`: chú thích từng bước bằng **ý nghĩa nghiệp vụ** (vì sao có bước này, ai được lợi), không chỉ mô tả thao tác.

## B7. Báo lại và dừng

- Rủi ro trọng tâm, tổng số mục theo kết quả và theo nhóm. Lỗi xếp từ nặng tới nhẹ, mỗi lỗi một dòng kèm mức độ.
- Mục Cần xác nhận và chỗ khác FSD cần người dùng chốt.
- Mục Bị chặn, Không tạo được tình huống, Chưa kiểm kèm lý do.
- Dữ liệu thử đã tạo, nhắc dọn theo cách đã ghi ở cấu hình.
- Link file kết quả, file đối chiếu giao diện, video nếu có.

Dừng. Người dùng muốn ghi lỗi cho dev thì chuyển sang `/log-bug`: xếp lỗi Cao lên đầu, ghi mức độ vào cột Note vì file bug không có cột mức độ, dùng trường "Mong muốn cho dev" làm Expect, rồi điền ID sheet bug ngược lại vào file kết quả. Người dùng muốn bộ testcase chuẩn thì chuyển file kết quả sang `/viet-testcase`.

## B8. Chạy lại sau khi dev sửa

1. Đọc file kết quả cũ, các mục đã chốt chấp nhận, cột ID và trạng thái trên sheet bug, `ket-qua/trang-thai/`.
2. Chạy lại mọi mục Lỗi, Bị chặn, Không tạo được tình huống, cộng các mục Đạt cùng màn, cùng nhóm với chỗ dev sửa (kiểm hồi quy).
3. Giữ nguyên mã mục cũ, cập nhật cột Lần (L2, L3...) và Kết quả, không tạo mã mới cho mục cũ. Lỗi mới phát hiện thì nối tiếp dãy BUG-xx.
4. Lỗi hết thì chuyển Đóng (đã sửa ở L2) kèm ngày, đề xuất người dùng chuyển Passed ở sheet bug. Lỗi còn thì giữ Mở, ghi "Vẫn còn ở L2". Lỗi đã sửa mà sinh lỗi khác thì đề xuất Reopen.
5. Giao diện đổi thì quay lại video liên quan nếu người dùng đã có video.
