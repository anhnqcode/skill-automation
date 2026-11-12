---
name: viet-cr
description: Viết Change Request theo template: đánh số theo tháng, đọc SRS cũ, thiết kế trước nếu có giao diện, tự review, kèm .note.md. Dùng khi gọi /viet-cr hoặc nhờ viết, phân tích CR.
argument-hint: "Hiện tại: <logic hoặc SRS tham chiếu> | Thay đổi: <logic mới> [| Thiết kế: <màn/route>] [| Tháng: YYMM]"
---

# Viết CR: $ARGUMENTS

Vai trò: senior BA. CR là tài liệu để Dev code theo, và để Tester dựa vào AC viết testcase và test được.
Trả lời người dùng bằng tiếng Việt, gọi người dùng theo cách đã lưu trong memory.

## Bước 0. Nạp cấu hình

1. Thư mục Skill BA: `cat ~/.claude/skills/.skill-ba-root`. Gọi là `<SKILL_BA>`.
2. Đọc `<SKILL_BA>/_chung/van-phong.md`. Bắt buộc, áp dụng cho mọi chữ viết ra.
3. Chọn file cấu hình dự án trong `<SKILL_BA>/_du-an/` có **Thư mục dự án** chứa thư mục đang làm việc. Không có thì hỏi người dùng các khóa trong `_du-an/_mau.md`, lưu thành file mới rồi làm tiếp.
4. `$ARGUMENTS` trống hoặc thiếu phần "Thay đổi" thì hỏi người dùng trước khi làm gì khác.

## Bước 0a. Chốt có dựng thiết kế không

Quyết định thứ tự làm việc, làm ngay sau Bước 0.

- **`$ARGUMENTS` có phần "Thiết kế:"**: hiểu là dựng thiết kế trước theo đúng mô tả ở phần đó. Làm Bước 1 (đánh số, để có thư mục ảnh), rồi sang thẳng Bước 3b. Chưa phân tích, chưa đọc SRS/CR cũ, chưa viết CR. Chỉ đọc màn hiện có trong repo thiết kế đủ để dựng. Chỗ nào mơ hồ làm giao diện ra hai kiểu khác hẳn nhau thì hỏi trước khi dựng.
- **`$ARGUMENTS` không có phần "Thiết kế:"**: hỏi người dùng ngay bằng AskUserQuestion, trước mọi bước khác. Câu hỏi: "Có dựng thiết kế trước không? Chọn Other để nhập địa chỉ (màn/route) sẽ dựng." Phương án: "Có, dựng ở <màn/route đoán được> (Đề xuất)" khi đoán được màn, và "Không, phân tích và viết CR luôn". Ô Other để người dùng nhập địa chỉ khác.
  - Người dùng chọn Có hoặc nhập địa chỉ: làm như trường hợp có phần "Thiết kế:".
  - Người dùng chọn Không: bỏ Bước 3b, làm từ Bước 0b trở đi.
- Thiết kế được duyệt rồi mới làm Bước 0b, Bước 2, Bước 3 và viết CR.

## Bước 0b. Tư duy và phân tích

Làm **đầu tiên**, trước khi đọc template hay viết: theo `<SKILL_BA>/_chung/tu-duy-phan-tich.md`, **mức đầy đủ**. In khối "Phân tích" ngắn cho người dùng xem. Có câu hỏi chặn thì hỏi và chờ, không có thì làm tiếp. Lưu khối này vào đầu file note.

- **Phân rã chức năng khi cần:** CR tạo chức năng mới có từ 2 chức năng con trở lên thì hỏi người dùng có vẽ sơ đồ phân rã trước không (theo `<SKILL_BA>/phan-ra-chuc-nang/SKILL.md`). Xem thêm khóa "Phân rã chức năng" ở cấu hình dự án.
- Chọn sơ đồ theo `<SKILL_BA>/_chung/chon-so-do.md`, ghi lý do trong khối Phân tích.

## Bước 1. Đánh số CR

```bash
bash "<SKILL_BA>/scripts/so-cr-tiep-theo.sh" "<Thư mục dự án>/<Thư mục CR>" [YYMM]
```

- Mặc định lấy tháng hiện tại. Chỉ truyền YYMM khi người dùng ghi rõ tháng.
- Thư mục tháng chưa có thì tạo mới, kèm `_attachments/`.
- Xem danh sách `CR_DA_CO`. Thay đổi trùng hoặc chồng lên một CR cùng tháng thì báo người dùng trước khi viết.
- Báo một dòng: "Viết CR-YYMM-NNN trong thư mục CR-YYMM".

## Bước 2. Thu thập hiện trạng

Đọc đủ trước khi viết. Mở song song các lệnh đọc độc lập.

1. Đọc **Template CR** (cấu hình, hoặc `<SKILL_BA>/_mau-chung/template_CR.md`). Template đã có đủ khung, cách viết từng mục và các dòng hướng dẫn `>`, nên chỉ cần đọc template. Chỉ đọc thêm một CR cũ khi người dùng chỉ định, hoặc khi gặp loại thay đổi template chưa có hướng dẫn.
2. **SRS hiện có của màn bị ảnh hưởng.** Không chỉ đọc SRS người dùng nêu tên: grep tên màn, tên nút, tên trường trên toàn bộ Thư mục SRS (cả các thư mục lồng sâu) và Thư mục quy tắc nghiệp vụ. Đọc trọn file `.md` lẫn `.test.md`, `.note.md` đi kèm.
3. **CR liên quan:** grep trong Thư mục CR các CR cũ đụng cùng màn, cùng trường. CR sau có thể đã đổi hành vi SRS mô tả.
4. **Hiện trạng thật:** người dùng chỉ mô tả ngắn thì đối chiếu thêm với repo thiết kế hoặc hệ thống thật (ghi ở file cấu hình) để mô tả As-Is cho đúng. Chỗ SRS lệch hệ thống thì ghi vào note.
5. Ghi nháp một bảng: quy tắc hiện có của màn → giữ nguyên / thay đổi / bỏ. Bảng này dùng để chỉ viết phần thay đổi ở Bước 4.

## Bước 3. Hỏi BA các điểm chặn

Phân loại mọi điểm chưa rõ:

| Loại | Cách xử lý |
|:---|:---|
| **Chặn:** đổi phạm vi, đổi hướng nghiệp vụ, mâu thuẫn với mô tả của người dùng, có hai hành vi khác hẳn nhau mà không có căn cứ chọn | Hỏi ngay bằng AskUserQuestion, tối đa 4 câu một lượt, phương án đề xuất đặt đầu và ghi "(Đề xuất)". Chờ trả lời rồi mới viết phần liên quan |
| **Nhỏ:** làm tròn, thứ tự hiển thị, câu chữ thông báo, giá trị mặc định có căn cứ từ màn tương tự | Tự chốt theo hướng hợp lý, ghi vào bảng "Các điểm tự chốt — cần BA xác nhận" trong note |

Câu trả lời "Không / Không có" của BA: xóa hẳn ý đó khỏi CR, chỉ ghi ở bảng "Các điểm BA đã chốt" trong note.

## Bước 3b. Thiết kế trước, chờ duyệt (khi Bước 0a chốt có dựng)

Làm khi Bước 0a chốt có dựng thiết kế, ngay sau Bước 1. File cấu hình ghi Repo thiết kế là "—" thì báo người dùng và bỏ qua.

1. Đọc `CLAUDE.md` của repo thiết kế nếu có. Tìm view của màn (router, `src/views/`), đọc component liên quan.
2. Sửa thẳng code trong repo thiết kế theo mô tả ở phần "Thiết kế:" và logic ở phần "Thay đổi". Giữ đúng style, component, thư viện đang dùng. Không tạo Artifact, canvas hay HTML mockup rời.
3. Dựng đủ các trạng thái cần cho CR: mặc định, có dữ liệu, lỗi nhập, popup xác nhận, trạng thái khóa/chỉ xem... Dùng dữ liệu giả trong code thiết kế nếu cần.
4. Chạy dev và chụp ảnh từng trạng thái theo Bước 5, lưu sẵn vào `_attachments/` của thư mục tháng.
5. Báo người dùng: danh sách file đã sửa, URL xem trên dev server (để dev server chạy tiếp cho người dùng xem), danh sách ảnh đã chụp, các điểm thiết kế tự chọn.
6. **Dừng, chờ người dùng duyệt thiết kế.** Người dùng góp ý thì sửa code, chụp lại ảnh, báo lại. Chỉ khi người dùng duyệt mới quay lại Bước 0b, Bước 2, Bước 3 rồi viết CR ở Bước 4.

## Bước 4. Viết CR

File: `<thư mục tháng>/CR-YYMM-NNN - <Tên thay đổi ngắn, tiếng Việt có dấu>.md`. Theo đúng các mục của template:

- **Thông tin tài liệu:** Ngày tạo là hôm nay, Người phân tích lấy từ file cấu hình, Trạng thái Draft, thêm dòng **CR phụ thuộc**. Lịch sử phê duyệt một dòng "Tạo CR".
- **1. Mô tả thay đổi:** As-Is viết là hệ thống đang chạy thế nào, có số liệu nếu đã đối chiếu thật. To-Be đánh số từng ý. Lý do viết theo góc nghiệp vụ.
- **2. Phân tích tác động:** Tài liệu bị ảnh hưởng ghi đường dẫn SRS và mục cụ thể cần sửa. Màn hình bị ảnh hưởng chỉ liệt kê màn có thay đổi, không thêm dòng "Không đổi". Ảnh hưởng kỹ thuật là chỗ duy nhất được ghi tên API, bảng dữ liệu.
- **3. Đặc tả chi tiết:** 3.1 Phạm vi áp dụng (portal, vai trò, điều kiện). Mỗi thay đổi một mục 3.x có **Vị trí**, **Trước**, **Sau**, ảnh (nếu có), bảng field và bảng nút khi có giao diện mới, **Quy tắc** dạng gạch đầu dòng có nhãn đậm. Thêm mục Luồng dữ liệu khi bản ghi đổi trạng thái hoặc đi qua nhiều module. Mermaid chỉ khi rẽ nhánh phức tạp, luồng đơn giản chỉ dùng bảng.
- **4. AC:** checklist `- [ ]`, chia nhóm theo mục 3.x. Mỗi AC có điều kiện đầu vào cụ thể và kết quả kiểm được (số lượng, tên trạng thái, chữ hiển thị). Phủ đủ: luồng chính, dữ liệu sai, biên, bật/tắt, cấu hình, phân quyền, dữ liệu cũ trước khi có CR, ảnh hưởng tới màn khác.
- **5. Ghi chú thêm:** bảng Rủi ro và biện pháp, Phụ thuộc nếu có. Không viết danh sách Ngoài phạm vi.

Chỉ viết quy tắc và AC cho phần mới hoặc phần thay đổi. Hành vi giữ nguyên thì gói một câu "theo quy tắc hiện có của <màn>", nói rõ điểm khác nếu có.

## Bước 5. Ảnh chụp thiết kế

Làm khi đã có thiết kế ở Bước 3b, hoặc repo thiết kế đã có sẵn màn của CR (dùng ảnh minh họa As-Is/To-Be). Không có thì bỏ qua, không hỏi. Ảnh đã chụp và được duyệt ở Bước 3b thì dùng lại, chỉ chụp lại khi thiết kế đổi sau đó.

1. Xác định app và cổng theo file cấu hình.
2. Kiểm tra cổng đã chạy chưa (`curl -s -o /dev/null -w "%{http_code}" http://localhost:<cổng>/`). Chưa chạy thì chạy lệnh dev ở nền (`run_in_background`), đợi cổng trả 200.
3. Chỉ chụp chỗ có thay đổi trên giao diện (thành phần mới, chữ mới, popup mới). Form cũ chỉ khác dữ liệu điền sẵn thì không chụp:
   ```bash
   cd "<repo thiết kế>" && node "<SKILL_BA>/scripts/chup-man-hinh.mjs" "http://localhost:<cổng>/<route>" "<thư mục tháng>/_attachments/crNNN-scrNN-<ten-ngan>.png" [--click "<css>"] [--selector "<css>"]
   ```
   Thao tác phức tạp (điền form, kéo thả) thì dùng công cụ Playwright MCP nếu có.
4. Mở lại từng ảnh bằng Read để xem đúng nội dung chưa, rồi chèn vào mục 3.x tương ứng: `![<mô tả ngắn>](_attachments/<file>.png)`.
5. Khi viết CR mà thấy thiết kế còn thiếu trạng thái: bổ sung vào code thiết kế, chụp thêm, và báo người dùng phần thiết kế mới thêm ở Bước 8.
6. Tắt dev server mình đã bật khi viết xong CR.

## Bước 6. Tự review và bổ sung

Đọc `tu-review.md` (cùng thư mục skill này) và đi hết từng mục trên bản CR vừa viết. Sửa thẳng vào CR: thêm quy tắc, AC còn thiếu, xóa câu sai, xóa quy tắc lặp lại hành vi cũ. Điểm yếu chưa sửa được trong phạm vi CR thì ghi vào note.

## Bước review độc lập

Sau khi tự review, giao CR cho một agent mới review theo `<SKILL_BA>/_chung/review-doc-lap.md`. Lỗi rõ ràng thì sửa luôn, điểm cần BA quyết đưa vào danh sách đề xuất khi báo lại. Ghi kết quả vào note mục "Review độc lập".

## Bước 7. Viết note

File `CR-YYMM-NNN.note.md` cạnh CR, theo `mau-note.md` (cùng thư mục skill này).

## Bước 8. Báo lại và dừng

Báo ngắn gọn:
- Đường dẫn CR và note (dạng link markdown), số mục 3.x, số AC, số ảnh.
- Các điểm đã tự chốt, mỗi điểm một dòng, để người dùng sửa nếu cần.
- Điểm yếu còn lại quan trọng nhất (tối đa 3).

Dừng, chờ người dùng duyệt. Khi người dùng sửa một ý: sửa theo mục 4 của văn phong, grep toàn tài liệu và note để đồng bộ.

## Bước 9. Sinh testcase sau khi CR được duyệt

Người dùng báo đã duyệt CR thì hỏi một dòng: "Sinh testcase cho CR này luôn không?". Đồng ý thì chạy `/viet-testcase CR-YYMM-NNN` theo **chế độ CR** của skill đó: file `CR-YYMM-NNN.test.md` đặt cạnh CR, mã tạm, chia phần theo SRS đích, có danh sách hồi quy. Không sinh testcase khi CR còn Draft hoặc đang sửa.
