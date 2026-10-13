# Checklist Nâng Cao — 7 Dạng Case Đặc Thù
### Bổ sung cho `Testcase_Template.md` (~95% coverage) — dành riêng cho domain Đặt hàng / Đặt xe / Tìm dịch vụ (Booking, Dispatch, Marketplace)

> **Tên gọi khác:** trước đây file này được các file `QA-*-Checklist.md` tham chiếu dưới tên `QA-Advanced-Domain-Checklist.md`. Tên thật trên đĩa là `Template_Testcase_Advanced.md` — mọi tham chiếu đã được thống nhất về tên thật.

---

## Quan hệ với `Testcase_Template.md`

File này **không thay thế** `Testcase_Template.md` — đây là phần mở rộng cho 5 dạng case đã xác định là "khó tổng quát" trong lần đánh giá coverage trước (Mục A–E), cộng thêm 2 mục phát hiện thêm khi tự rà soát sát với đúng domain (Mục F, G), đặc biệt liên quan đến domain **đặt hàng/đặt xe/tìm giúp việc** (dạng mini app: giao đồ ăn, gọi xe, tìm thợ/người giúp việc).

| Vẫn dùng `Testcase_Template.md` cho | Dùng thêm file này khi |
|---|---|
| Field validation, CRUD, phân quyền, State Transition, Cross-module... (Mục 1–28) | Có thuật toán ghép nối (matching tài xế/thợ), có giao dịch nhiều bước qua nhiều service, có app tài xế/shipper hoạt động offline, có thanh toán qua cổng/ví, có hệ thống hàng đợi điều phối đơn, có theo dõi vị trí real-time, có đánh giá 2 chiều |

**Nguyên tắc áp dụng:** Đọc phần "Điều kiện áp dụng" đầu mỗi mục — nếu chức năng đang test không có dấu hiệu tương ứng, bỏ qua mục đó, không tính là thiếu sót.

---

## Mẫu danh sách test case

> Dùng đúng format này khi gen testcase cho các mục A–G. Khác với bảng mẫu ở `Testcase_Template.md` (Mục 24), bảng này **bỏ 2 cột Automation Status và Automation Link** — file này chỉ tập trung mô tả nghiệp vụ đặc thù domain, không quản lý trạng thái automation (việc đó vẫn track ở file `.test.md` chính theo đúng quy tắc đã có trong `CLAUDE.md`).

| ID | Mục đích kiểm thử | Tiền điều kiện | Các bước thực hiện | Kết quả mong muốn | Kết quả thực tế | Mức độ ưu tiên | Ghi chú |
|---|---|---|---|---|---|---|---|
| TC-[Mã]-001 | [Mô tả testcase] | [Tiền điều kiện] | 1. [Bước 1]<br>2. [Bước 2]<br>3. [Bước 3] | [Kết quả mong muốn chi tiết] | P/F | High | |
| TC-[Mã]-002 | [Mô tả testcase] | [Tiền điều kiện] | 1. [Bước 1]<br>2. [Bước 2]<br>3. [Bước 3] | [Kết quả mong muốn chi tiết] | P/F | Medium | |

### Quy tắc mức độ ưu tiên (riêng cho các mục A–G)

| Mức độ | Tiêu chí |
|---|---|
| **High** | Idempotency của webhook/message (A.1, E.2), Compensating transaction khi rollback (D.2–D.3), Gian lận thuật toán (C.6), Đối soát thanh toán (E.5), Xung đột dữ liệu khi đồng bộ offline (B.3) — bất kỳ case nào liên quan trực tiếp đến **tiền, dữ liệu bị mất, hoặc an toàn nền tảng** |
| **Medium** | Độ trễ/thứ tự xử lý (A.2, F.2), Xử lý no-match (C.3), Timeout giữa các bước Saga (D.4), Tính điểm trung bình rating (G.2), Route & ETA (F.4) |
| **Low** | Hiệu năng bản đồ mức thủ công (F.5), Hiển thị/UX khi offline (B.5), Trường hợp hiếm gặp ít ảnh hưởng nghiệp vụ cốt lõi |

> Khác với `Testcase_Template.md` (ưu tiên dựa trên loại hành động CRUD/validate thông thường), bảng ưu tiên ở đây dựa trên **mức độ ảnh hưởng đến tiền, dữ liệu, và an toàn nền tảng** — vì bản chất 7 mục A–G đều là các case rủi ro cao, không phải case field-level thông thường.

### Cách đặt tên nhóm testcase (áp dụng chuẩn Mục 1.2 của `Testcase_Template.md`)

```
[Số]. [Tên chức năng cụ thể — ví dụ: Ghép tài xế cho đơn đặt xe]

   [Số].1. Kiểm tra ghép nối cơ bản (theo Mục C.1, C.2)
   [Số].2. Kiểm tra xử lý khi không tìm được tài xế (theo Mục C.3)
   [Số].3. Kiểm tra ghép nối đồng thời (theo Mục C.4)
   [Số].4. Kiểm tra chống gian lận (theo Mục C.6)
```

> Luôn ghi rõ trong tên nhóm testcase đang áp dụng theo sub-mục nào của A–G (ví dụ "theo Mục C.6") để dễ truy vết ngược lại checklist gốc khi review.

---

## Mục lục

- [A. Hệ thống hàng đợi / Nhắn tin phân tán theo công nghệ cụ thể](#a)
- [B. Đồng bộ Offline-first (App Tài xế / Shipper / Nhân viên hiện trường)](#b)
- [C. Thuật toán Ghép nối & Gợi ý (Matching / Dispatch / Recommendation)](#c)
- [D. Giao dịch phân tán nhiều bước (Saga / Distributed Transaction)](#d)
- [E. Cổng thanh toán & Webhook bên thứ ba (Payment Gateway & Webhook)](#e)
- [F. Theo dõi vị trí Real-time (Real-time Location Tracking)](#f)
- [G. Đánh giá 2 chiều (Rating / Review)](#g)

---

<a name="a"></a>
## A. Hệ thống hàng đợi / Nhắn tin phân tán theo công nghệ cụ thể

> Khác với Mục 12 (`Testcase_Template.md`) vốn kiểm tra đồng bộ dữ liệu ở mức khái niệm chung, Mục A kiểm tra **hành vi đặc thù của từng công nghệ hàng đợi** — vì mỗi công nghệ có cơ chế đảm bảo (delivery guarantee) khác nhau, và bug thường nằm ở đúng chỗ khác biệt này.
>
> **Điều kiện áp dụng:** hệ thống dùng message queue/pub-sub để xử lý các luồng như: phát đơn hàng mới đến tài xế/thợ gần đó, đồng bộ vị trí GPS real-time, xử lý hàng loạt thông báo, xử lý sự kiện giữa các service (order-service, dispatch-service, payment-service...).

### A.0. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo hệ thống thực tế) |
|---|---|
| Công nghệ hàng đợi/pub-sub đang dùng là gì? | `[Kafka / RabbitMQ / SQS / Redis Pub-Sub / khác]` |
| Cơ chế đảm bảo gửi tin là gì? | `[At-most-once / At-least-once / Exactly-once]` |
| Có đảm bảo thứ tự message không? Theo phạm vi nào? | `[Không đảm bảo / Đảm bảo trong 1 partition-key (ví dụ theo mã đơn hàng)]` |
| Message xử lý thất bại thì đi đâu? | `[Retry N lần / Dead Letter Queue / Mất luôn]` |
| Điều gì xảy ra nếu consumer offline khi message được gửi? | `[Message được giữ lại chờ / Bị mất nếu không ai subscribe tại thời điểm đó]` |

### A.1. Đảm bảo gửi tin (Delivery Guarantee)
- Publish message khi tất cả consumer đang hoạt động bình thường → nhận đúng, đúng nội dung
- **Consumer offline/crash đúng lúc** message được publish → hành vi đúng theo cơ chế đã xác định ở A.0 (giữ lại chờ hay mất luôn) — đây là điểm khác biệt lớn nhất giữa các công nghệ, cần test rõ ràng theo đúng công nghệ đang dùng
- Message được xử lý nhưng **chưa kịp commit/ack** thì consumer crash → khi consumer phục hồi, message có bị xử lý lại không (duplicate) → nếu có, phần xử lý phía sau phải **idempotent** (ví dụ: gửi thông báo mời tài xế nhận đơn 2 lần không được tạo 2 lời mời)

### A.2. Thứ tự xử lý message (Ordering)
- Nhiều message cùng liên quan đến **1 đối tượng** (ví dụ nhiều cập nhật trạng thái liên tiếp của cùng 1 đơn hàng: "Đã nhận đơn" → "Đang giao" → "Hoàn thành") — xử lý đúng thứ tự, không bị đảo lộn khiến trạng thái cuối cùng sai (ví dụ hiển thị "Đã nhận đơn" sau khi thực ra đã "Hoàn thành")
- Message liên quan đến **các đối tượng khác nhau** (đơn hàng A và đơn hàng B) — không bắt buộc thứ tự giữa chúng, nhưng không được xử lý sai lẫn dữ liệu giữa 2 đối tượng

### A.3. Consumer Group & Load Balancing (nếu áp dụng — Kafka, SQS...)
- Nhiều instance của cùng 1 service (ví dụ nhiều instance dispatch-service) cùng đọc từ 1 topic/queue — mỗi message chỉ được xử lý bởi đúng 1 instance, không bị xử lý trùng bởi nhiều instance
- Thêm/bớt instance consumer khi hệ thống đang chạy (scale up/down) — không làm mất message đang xử lý dở, phân phối lại tải đúng

### A.4. Dead Letter Queue & Retry Policy
- Message xử lý thất bại **lần đầu** → được retry theo đúng chính sách (số lần, khoảng cách giữa các lần retry)
- Message thất bại **vượt quá số lần retry tối đa** → rơi đúng vào Dead Letter Queue (hoặc cơ chế tương đương), không bị mất âm thầm
- Có cơ chế giám sát/cảnh báo khi Dead Letter Queue có message tích tụ (dấu hiệu có lỗi hệ thống cần xử lý) — kiểm tra Admin có nhìn thấy và xử lý lại được các message này không

### A.5. Đặc thù theo công nghệ (điền theo hệ thống thực tế đang dùng)

**Nếu dùng Kafka:**
- Offset được commit đúng sau khi xử lý thành công, không commit sớm khi chưa xử lý xong (gây mất message nếu crash giữa chừng)
- Partition key được chọn đúng để đảm bảo message cùng 1 đơn hàng/tài xế luôn vào cùng 1 partition (giữ đúng thứ tự)

**Nếu dùng RabbitMQ:**
- Message được ACK đúng thời điểm (sau khi xử lý xong, không ACK trước)
- Exchange & routing key đưa message đến đúng queue mong muốn, không bị route nhầm

**Nếu dùng Redis Pub-Sub:**
- **Lưu ý đặc biệt:** Redis Pub-Sub truyền thống **không lưu lại message** nếu không có subscriber tại thời điểm publish — nếu dùng cho việc phát đơn hàng đến tài xế, cần xác nhận rõ: tài xế mất kết nối đúng lúc có đơn mới thì có bị bỏ lỡ vĩnh viễn không, hay hệ thống có cơ chế bù (ví dụ polling định kỳ song song, hoặc dùng Redis Streams thay vì Pub-Sub thuần)

**Nếu dùng SQS:**
- Visibility timeout đủ dài để consumer xử lý xong trước khi message hiện lại cho consumer khác (tránh xử lý trùng)
- Với hàng đợi FIFO: message cùng Group ID được xử lý đúng thứ tự

---

<a name="b"></a>
## B. Đồng bộ Offline-first (App Tài xế / Shipper / Nhân viên hiện trường)

> Áp dụng cho app dành cho tài xế, shipper, thợ/nhân viên dịch vụ — nhóm người dùng thường xuyên ở khu vực sóng yếu (hầm gửi xe, thang máy, vùng ngoại thành) và cần app vẫn hoạt động được để không bỏ lỡ đơn hoặc mất thao tác.
>
> **Điều kiện áp dụng:** app có cho phép thao tác khi mất mạng (nhận/cập nhật trạng thái đơn, ghi nhận vị trí, chụp ảnh xác nhận giao hàng...) và tự đồng bộ khi có mạng trở lại.

### B.0. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo hệ thống thực tế) |
|---|---|
| Những thao tác nào được phép thực hiện khi offline? | `[Ví dụ: cập nhật trạng thái đơn, chụp ảnh POD, ghi nhận vị trí]` |
| Dữ liệu offline được lưu ở đâu trên thiết bị? | `[Local DB/SQLite, cache, file hệ thống...]` |
| Khi có mạng trở lại, đồng bộ theo cơ chế nào? | `[Tự động ngay lập tức / Định kỳ / Người dùng bấm nút đồng bộ]` |
| Nếu server đã có dữ liệu mới hơn khi đồng bộ (xung đột), ưu tiên bên nào? | `[Server thắng / Client thắng / Hỏi người dùng / Merge theo quy tắc]` |

### B.1. Thao tác khi offline
- Thực hiện thao tác được phép khi **không có mạng** → lưu đúng vào hàng đợi local, giao diện phản hồi ngay (không chờ mạng), có chỉ báo rõ ràng "đang chờ đồng bộ" để người dùng biết
- Thực hiện thao tác **không được phép** khi offline (ví dụ thao tác cần xác thực real-time với server) → hệ thống chặn đúng và thông báo rõ cần có mạng
- Thực hiện **nhiều thao tác liên tiếp** khi offline (ví dụ cập nhật trạng thái đơn 3 lần liên tiếp: Nhận đơn → Đang giao → Hoàn thành, tất cả khi chưa có mạng) — tất cả được lưu đúng thứ tự trong hàng đợi local

### B.2. Đồng bộ khi có mạng trở lại
- Có mạng trở lại → hàng đợi thao tác local được gửi lên server **đúng thứ tự đã thực hiện**, không bị đảo lộn
- Đồng bộ thành công → xóa đúng các thao tác đã đồng bộ khỏi hàng đợi local, không gửi lại lần 2
- Đồng bộ **một phần thất bại** (ví dụ 3 thao tác, thao tác thứ 2 lỗi) → xử lý đúng theo thiết kế: dừng lại chờ xử lý thao tác lỗi trước khi tiếp tục (giữ đúng thứ tự), hay bỏ qua và tiếp tục các thao tác sau (cần xác nhận rõ vì ảnh hưởng tính đúng đắn nghiệp vụ)
- Mất mạng **giữa lúc đang đồng bộ** (một số thao tác đã gửi thành công, một số chưa) → khi có mạng lại, tiếp tục đúng từ điểm dở dang, không gửi trùng các thao tác đã thành công

### B.3. Xung đột dữ liệu (Conflict Resolution)
- Dữ liệu trên server đã bị thay đổi bởi nguồn khác (ví dụ Admin can thiệp, hoặc chính tài xế đó thao tác từ thiết bị khác) **trong lúc** app đang offline → khi đồng bộ, xử lý đúng theo quy tắc ưu tiên đã xác định ở B.0, không âm thầm ghi đè gây sai lệch dữ liệu quan trọng (ví dụ trạng thái đơn hàng)
- Trường hợp đặc biệt cần lưu ý: đơn hàng đã bị **hủy bởi khách hàng hoặc hệ thống** trong lúc tài xế offline và vẫn đang thao tác trên đơn đó (ví dụ tài xế offline vẫn bấm "Đã giao hàng") → khi đồng bộ, hệ thống phải phát hiện đơn đã bị hủy và xử lý đúng (không tính hoàn thành đơn đã hủy), thông báo rõ cho tài xế

### B.4. Độ tin cậy của việc đồng bộ nền (Background Sync Reliability)
- App bị hệ điều hành **tắt nền** (background kill) giữa lúc đang có dữ liệu chờ đồng bộ — dữ liệu vẫn còn nguyên trong local storage khi mở lại app, không bị mất
- App bị **gỡ cài đặt rồi cài lại** khi vẫn còn dữ liệu chưa đồng bộ (trường hợp hiếm nhưng cần biết rõ hành vi) — dữ liệu chưa đồng bộ có bị mất vĩnh viễn không, có cảnh báo gì trước khi gỡ không (nếu kiểm soát được)
- Đồng bộ vị trí GPS liên tục khi có mạng chập chờn (on-off liên tục) — không tạo ra hàng loạt request đồng bộ trùng lặp gây tốn pin/dữ liệu di động bất thường

### B.5. Trải nghiệm người dùng khi offline
- Giao diện hiển thị rõ ràng trạng thái **đang offline** và **có bao nhiêu thao tác đang chờ đồng bộ**
- Khi đồng bộ thành công — thông báo rõ ràng, không để người dùng nghi ngờ dữ liệu có được lưu hay chưa
- Khi đồng bộ thất bại vĩnh viễn (ví dụ dữ liệu xung đột không tự giải quyết được) — thông báo rõ và hướng dẫn hành động tiếp theo, không để dữ liệu "treo" vô thời hạn trong hàng đợi local mà người dùng không biết

---

<a name="c"></a>
## C. Thuật toán Ghép nối & Gợi ý (Matching / Dispatch / Recommendation)

> Khác với phần lớn checklist trong `Testcase_Template.md` (vốn giả định kết quả đúng là 1 giá trị xác định), Mục C kiểm tra hệ thống có đầu ra **không cố định hoàn toàn** — thuật toán chọn tài xế/thợ phù hợp, gợi ý món ăn/dịch vụ. Không thể viết "kết quả mong muốn = giá trị cụ thể" như test field thông thường.
>
> **Điều kiện áp dụng:** hệ thống có thuật toán ghép nối tài xế-khách hàng, thợ-khách hàng, hoặc gợi ý sản phẩm/dịch vụ/nhà hàng dựa trên nhiều tiêu chí (khoảng cách, đánh giá, mức độ phù hợp...).

### C.0. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo hệ thống thực tế) |
|---|---|
| Thuật toán ghép nối dựa trên tiêu chí nào? | `[Khoảng cách, đánh giá, thời gian rảnh, mức độ ưu tiên...]` |
| Có ngưỡng chất lượng tối thiểu để coi là "ghép đúng" không? | `[Ví dụ: tài xế trong bán kính 5km, đánh giá >= 4 sao]` |
| Khi không tìm được kết quả phù hợp thì xử lý sao? | `[Mở rộng bán kính tìm kiếm / Báo không tìm thấy / Đưa vào hàng đợi chờ]` |
| Thuật toán có học/thay đổi theo thời gian không (ML-based)? | `[Có/Không — nếu có, ai giám sát chất lượng theo thời gian]` |

### C.1. Tính hợp lý của kết quả ghép nối (Relevance — không phải Exact Match)
- Kết quả ghép nối/gợi ý nằm trong **ràng buộc bắt buộc** đã định nghĩa (ví dụ: tài xế được gợi ý phải đang online, đang trong bán kính cho phép, đúng loại xe khách yêu cầu) — đây là ràng buộc cứng, luôn test được đúng/sai như bình thường
- Kết quả **không vi phạm quy tắc loại trừ** (ví dụ: không gợi ý tài xế đang bị khách hàng đó chặn/đánh giá thấp trước đó, không gợi ý nhà hàng đã đóng cửa)
- Với tiêu chí "mềm" (độ phù hợp, mức độ liên quan) — test theo **ngưỡng chấp nhận được** trên bộ dữ liệu mẫu đã biết trước kết quả kỳ vọng, không test "đúng tuyệt đối 1 kết quả"

### C.2. Công bằng & Đa dạng trong phân phối (Fairness & Distribution)
- Nhiều tài xế/thợ cùng thỏa điều kiện như nhau (cùng khoảng cách, cùng đánh giá) — hệ thống có phân phối đơn công bằng không, hay luôn ưu tiên 1 người cố định (gây khiếu nại từ các tài xế/thợ khác)
- Gợi ý sản phẩm/nhà hàng không bị lặp lại quá mức (luôn hiện đúng vài kết quả giống nhau) nếu nghiệp vụ yêu cầu đa dạng hóa kết quả

### C.3. Xử lý khi không tìm được kết quả phù hợp (No-match Handling)
- Không có tài xế/thợ nào thỏa điều kiện trong bán kính/tiêu chí ban đầu — hệ thống xử lý đúng theo thiết kế: tự động mở rộng phạm vi tìm kiếm, đưa vào hàng đợi chờ, hay thông báo không tìm thấy ngay
- Thời gian chờ tìm kiếm vượt ngưỡng cho phép (ví dụ tìm tài xế quá 2 phút không có ai nhận) — hệ thống có hành động tiếp theo đúng (hủy tự động, báo khách hàng, thử tiêu chí nới lỏng hơn) — liên quan Mục 28 (Time-based) của file chính

### C.4. Ghép nối đồng thời & Race Condition
- Nhiều đơn hàng cùng được gợi ý đến **cùng 1 tài xế/thợ** gần như đồng thời — chỉ 1 đơn được xác nhận ghép thành công, các đơn còn lại tự động tìm người khác, không bị "khóa" nhầm nhiều đơn vào 1 người
- Tài xế/thợ **nhận đơn** đúng lúc hệ thống đang tính lại danh sách ghép nối (ví dụ do có tài xế mới online) — không xảy ra tình trạng đơn bị gán cho 2 người cùng lúc (liên quan Mục 16 — Concurrency của file chính)

### C.5. Giám sát chất lượng theo thời gian (nếu thuật toán có yếu tố học máy)
- Có cơ chế theo dõi tỷ lệ ghép nối thành công / tỷ lệ khách hàng hủy sau khi được ghép — phát hiện sớm nếu chất lượng thuật toán suy giảm theo thời gian (model drift)
- Test **không phải một lần rồi xong** — cần có kế hoạch kiểm tra định kỳ (không thuộc phạm vi test case thủ công một lần, ghi chú rõ đây là hoạt động giám sát liên tục, không phải regression test thông thường)

### C.6. Gian lận thuật toán (Algorithm Gaming / Fraud)

> Khác với các mục trên (kiểm tra thuật toán hoạt động đúng), Mục C.6 kiểm tra hệ thống có **chống được hành vi cố tình lợi dụng quy tắc ghép nối** để trục lợi không — đây là rủi ro nghiệp vụ/an toàn nền tảng, không chỉ là bug thông thường.
>
> **Câu hỏi nhận diện:** "Nếu tài xế/thợ biết chính xác thuật toán ưu tiên theo tiêu chí gì, họ có thể lợi dụng cách nào để được ưu tiên bất chính không?"

**Giả mạo vị trí (Fake GPS / Location Spoofing)**
- Tài xế/thợ dùng app giả lập GPS để hiển thị vị trí **gần khách hàng hơn thực tế** (nhằm được ưu tiên ghép nối) — hệ thống có cơ chế phát hiện bất thường không (ví dụ: vị trí nhảy cóc bất hợp lý giữa 2 lần cập nhật liên tiếp — di chuyển hàng chục km trong vài giây; tốc độ di chuyển vượt ngưỡng vật lý hợp lý)
- Vị trí được báo cáo **không khớp** với dữ liệu mạng/cảm biến khác của thiết bị (nếu hệ thống có thu thập thêm tín hiệu để đối chiếu, ví dụ tốc độ từ accelerometer, WiFi/cell tower gần đó) — có cơ chế đối chiếu chéo hay chỉ tin tuyệt đối vào tọa độ GPS báo lên
- Tài khoản bị phát hiện dùng vị trí giả — hệ thống xử lý đúng theo chính sách (cảnh cáo, tạm khóa, giảm ưu tiên ghép nối, chấm dứt hợp tác), có ghi log đầy đủ bằng chứng để tra soát

**Thao túng trạng thái Online/Offline (Status Spam)**
- Tài xế/thợ **bật/tắt trạng thái sẵn sàng liên tục trong thời gian ngắn** (spam online-offline) nhằm "làm mới" vị trí trong hàng đợi ghép nối hoặc né các đơn không mong muốn trong khi vẫn giữ được ưu tiên nhận đơn tốt — hệ thống có phát hiện và xử lý hành vi bất thường này không (ví dụ giới hạn số lần đổi trạng thái trong 1 khoảng thời gian, hoặc tính điểm uy tín bị ảnh hưởng)
- Tài xế/thợ **từ chối đơn liên tục có chọn lọc** (chỉ nhận đơn ngắn/gần, từ chối đơn xa) để tối ưu thu nhập theo cách không công bằng với hệ thống điều phối chung — có cơ chế theo dõi tỷ lệ từ chối bất thường và xử lý đúng theo chính sách (ảnh hưởng độ ưu tiên, cảnh báo)

**Tài khoản giả / Đa tài khoản (Multi-accounting)**
- Một người dùng tạo **nhiều tài khoản khách hàng** để lợi dụng khuyến mãi/ưu đãi dành cho người dùng mới nhiều lần — hệ thống có cơ chế phát hiện (theo thiết bị, số điện thoại, phương thức thanh toán trùng lặp) không
- Tài xế/thợ tạo nhiều tài khoản để **né các mức phạt/giảm điểm uy tín** ở tài khoản cũ rồi hoạt động lại bằng tài khoản mới — có cơ chế xác thực danh tính chặn được tình trạng này không (liên quan đến KYC nếu hệ thống có)

**Thông đồng giữa các bên (Collusion)**
- Tài xế/thợ và khách hàng **thông đồng đặt đơn ảo** (không có nhu cầu thật) để trục lợi khuyến mãi hoặc làm giả số liệu hoạt động — hệ thống có cơ chế phát hiện mẫu hình bất thường (ví dụ cùng cặp tài khoản lặp lại giao dịch nhiều lần bất thường trong thời gian ngắn) không

---

<a name="d"></a>
## D. Giao dịch phân tán nhiều bước (Saga / Distributed Transaction)

> Mở rộng của Mục 26.3 (`Testcase_Template.md`) cho trường hợp phức tạp hơn: giao dịch trải qua **nhiều service độc lập, mỗi service có dữ liệu riêng** — rollback không phải 1 lệnh đơn giản mà là chuỗi "giao dịch bù trừ" (compensating transaction) ở từng service.
>
> **Điều kiện áp dụng:** một nghiệp vụ (ví dụ: Đặt đơn hàng) chạy qua ≥ 3 service độc lập, có giữ/trừ tài nguyên (tiền, chỗ, tài xế) ở nhiều nơi khác nhau.
>
> **Ví dụ luồng điển hình trong domain đặt xe/đặt hàng:**
> ```
> [Order Service] Tạo đơn → [Dispatch Service] Giữ chỗ tài xế →
> [Payment Service] Trừ tiền/giữ tiền → [Notification Service] Báo tài xế
> ```
> Nếu bước "Trừ tiền" thất bại → phải tự động **nhả tài xế đã giữ** (compensating action ở Dispatch Service) và **hủy đơn** (compensating action ở Order Service) — không chỉ dừng lại ở bước lỗi.

### D.0. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo hệ thống thực tế) |
|---|---|
| Các bước trong giao dịch là gì, theo thứ tự nào? | `[Liệt kê từng bước và service tương ứng]` |
| Mỗi bước có hành động bù trừ (compensating action) tương ứng là gì? | `[Bước 1 → bù bằng hành động X, Bước 2 → bù bằng hành động Y...]` |
| Cơ chế điều phối Saga là gì? | `[Orchestration (có 1 service điều phối trung tâm) / Choreography (từng service tự lắng nghe sự kiện)]` |
| Timeout cho mỗi bước là bao lâu? | `[Ví dụ: bước giữ tài xế timeout sau 30 giây]` |

### D.1. Luồng thành công (Happy Path)
- Tất cả các bước thực hiện thành công theo đúng thứ tự → giao dịch hoàn tất, trạng thái cuối cùng đúng ở **tất cả** các service liên quan, không chỉ service cuối cùng
- Dữ liệu nhất quán giữa các service sau khi hoàn tất (ví dụ: Order Service hiển thị "Đã thanh toán", Payment Service cũng có bản ghi giao dịch tương ứng khớp số tiền)

### D.2. Thất bại tại từng bước — Compensating Transaction
- Thất bại ở **bước đầu tiên** → không cần bù trừ gì (chưa có gì để hoàn tác), báo lỗi ngay
- Thất bại ở **bước giữa** (ví dụ bước Trừ tiền thất bại sau khi đã giữ chỗ tài xế) → hành động bù trừ của **các bước trước đó** được thực hiện đúng và đầy đủ (nhả tài xế), không chỉ dừng giao dịch mà bỏ quên tài nguyên đã giữ
- Thất bại ở **bước cuối cùng** → toàn bộ chuỗi bù trừ từ bước áp chót về bước đầu được thực hiện đúng thứ tự **ngược lại**
- Với mỗi bước thất bại, sinh riêng 1 testcase xác nhận đúng hành động bù trừ tương ứng — không gộp chung "giao dịch thất bại thì rollback" như 1 case duy nhất

### D.3. Hành động bù trừ tự nó cũng thất bại
- Hành động bù trừ (ví dụ lệnh "nhả tài xế") **bị lỗi** khi thực hiện (mất kết nối, service đích down) — hệ thống có cơ chế retry hoặc đánh dấu cần xử lý thủ công, **không được bỏ qua âm thầm** để tài nguyên bị "kẹt" vĩnh viễn (ví dụ tài xế bị giữ mãi mãi dù đơn đã hủy)
- Có cơ chế giám sát các giao dịch "bù trừ chưa hoàn tất" (tương tự Dead Letter Queue ở Mục A.4) để Admin phát hiện và xử lý

### D.4. Timeout giữa các bước
- Một bước **không phản hồi trong thời gian cho phép** (ví dụ tài xế không xác nhận nhận đơn trong 30 giây) — hệ thống coi đây là thất bại và kích hoạt đúng chuỗi bù trừ, không chờ vô thời hạn
- Bước phản hồi **đúng lúc vừa hết timeout** (ranh giới) — hệ thống xử lý nhất quán theo 1 quy tắc rõ ràng (chấp nhận nếu phản hồi đến trước, từ chối nếu sau) — liên quan Mục 28.6 (Race condition tại ranh giới thời gian) của file chính

### D.5. Idempotency xuyên suốt chuỗi Saga
- Một bước được **gọi lại 2 lần** do lỗi mạng/retry (ví dụ lệnh "trừ tiền" gửi 2 lần) — chỉ trừ tiền đúng 1 lần, không trừ 2 lần
- Một sự kiện hoàn tất bước được **nhận 2 lần** bởi service điều phối (nếu dùng cơ chế Choreography) — không kích hoạt bước tiếp theo 2 lần

### D.6. Quan sát và truy vết (Observability)
- Có thể **truy vết toàn bộ hành trình** của 1 giao dịch qua tất cả các service (ví dụ dùng 1 Transaction ID/Correlation ID xuyên suốt) — phục vụ việc điều tra khi có sự cố, không phải tìm log rời rạc ở từng service
- Trạng thái trung gian của giao dịch (đang ở bước nào) hiển thị được cho Admin/hỗ trợ khách hàng khi cần tra cứu

---

<a name="e"></a>
## E. Cổng thanh toán & Webhook bên thứ ba (Payment Gateway & Webhook)

> Mở rộng của Mục 4.4 (`Testcase_Template.md` — External API) cho trường hợp đặc thù nhất và rủi ro cao nhất: xử lý **tiền thật**, có xác nhận bất đồng bộ qua webhook, và luôn cần khả năng **đối soát** (reconciliation) để đảm bảo dữ liệu khớp với bên thứ ba.
>
> **Điều kiện áp dụng:** hệ thống tích hợp cổng thanh toán (thẻ, ví điện tử, chuyển khoản), hoặc có ví nội bộ/thanh toán COD, hoặc có chi trả cho tài xế/thợ (payout/settlement).

### E.0. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo hệ thống thực tế) |
|---|---|
| Các phương thức thanh toán hỗ trợ là gì? | `[Thẻ, ví điện tử, chuyển khoản, COD, ví nội bộ...]` |
| Webhook xác nhận thanh toán có cơ chế xác thực chữ ký không? | `[Có/Không — nêu rõ cơ chế]` |
| Có cơ chế đối soát định kỳ với cổng thanh toán không? | `[Có/Không — tần suất]` |
| Chính sách hoàn tiền/hủy giao dịch là gì? | `[Điều kiện, thời gian xử lý]` |

### E.1. Luồng thanh toán cơ bản & Rời trang giữa chừng
- Người dùng thanh toán thành công và ở lại xem kết quả → hiển thị đúng ngay
- Người dùng **rời khỏi trang/app** ngay sau khi bấm thanh toán, **trước khi** thấy kết quả (chuyển app khác, mất mạng, tắt màn hình) — webhook xác nhận đến sau đó vẫn được xử lý đúng ở phía server, trạng thái đơn hàng cập nhật đúng dù người dùng không còn xem màn hình đó; khi người dùng mở lại app, thấy đúng trạng thái mới nhất

### E.2. Webhook — Tính Idempotent (quan trọng nhất)
- Webhook xác nhận thanh toán đến **đúng 1 lần** — xử lý đúng, cộng/trừ tiền đúng 1 lần
- Webhook đến **2 lần trở lên** cho cùng 1 giao dịch (cổng thanh toán retry do không nhận được response kịp thời từ hệ thống) — chỉ xử lý đúng 1 lần, **không cộng tiền/xác nhận đơn 2 lần** — đây là lỗi nghiêm trọng nhất trong nhóm case này, luôn ưu tiên **High**
- Webhook đến với dữ liệu có vẻ giống nhưng **mã giao dịch khác nhau** (ví dụ do người dùng thanh toán lại sau khi lần đầu lỗi) — xử lý đúng, không nhầm lẫn giữa 2 giao dịch riêng biệt

### E.3. Webhook — Thứ tự và tính xác thực
- Webhook đến **sai thứ tự** so với thực tế (ví dụ webhook "Hoàn tiền" đến trước webhook "Thanh toán thành công" do độ trễ mạng) — hệ thống xử lý đúng dựa trên timestamp/trạng thái thực tế, không áp dụng mù quáng theo thứ tự đến
- Webhook giả mạo (không đến từ cổng thanh toán thật, không có chữ ký hợp lệ) — bị từ chối, không xử lý, có ghi log cảnh báo bảo mật
- Webhook đến khi hệ thống **đang bảo trì/down** — cổng thanh toán thường tự retry theo lịch riêng; xác nhận hệ thống có xử lý đúng khi webhook đến muộn sau khi phục hồi, không bỏ sót

### E.4. Trạng thái trung gian & Timeout
- Giao dịch ở trạng thái **"Đang xử lý"** quá lâu (webhook chưa đến, có thể do lỗi mạng phía cổng thanh toán) — hệ thống có cơ chế chủ động **hỏi lại** trạng thái thật từ cổng thanh toán (query API) sau một khoảng thời gian, không chỉ ngồi chờ webhook mãi mãi
- Kết quả từ việc chủ động hỏi lại **khác** với trạng thái hệ thống đang lưu (ví dụ cổng thanh toán báo đã thành công nhưng hệ thống vẫn đang "Đang xử lý" do lỡ webhook) — cập nhật lại đúng theo kết quả xác thực mới nhất

### E.5. Đối soát (Reconciliation)
- Có báo cáo/cơ chế đối soát định kỳ so sánh giao dịch trong hệ thống với giao dịch bên cổng thanh toán — phát hiện được các trường hợp lệch (hệ thống báo thành công nhưng cổng thanh toán không có, hoặc ngược lại)
- Phát hiện giao dịch lệch qua đối soát → có quy trình xử lý rõ ràng (tự động điều chỉnh, hay cảnh báo cho bộ phận vận hành xử lý thủ công)

### E.6. Hoàn tiền (Refund)
- Hoàn tiền **toàn phần** — số tiền đúng, trạng thái đơn hàng cập nhật đúng, người dùng nhận được tiền đúng kênh đã thanh toán (hoặc kênh khác nếu nghiệp vụ quy định)
- Hoàn tiền **một phần** (nếu nghiệp vụ hỗ trợ, ví dụ hủy 1 phần đơn hàng) — số tiền hoàn đúng, phần còn lại của giao dịch giữ nguyên đúng
- Webhook xác nhận hoàn tiền cũng phải qua kiểm tra Idempotent như E.2 (hoàn tiền 2 lần là lỗi nghiêm trọng)
- Yêu cầu hoàn tiền khi giao dịch gốc **chưa từng thành công** (dữ liệu không nhất quán, có thể do thao tác thủ công sai) — hệ thống chặn đúng, không hoàn tiền cho giao dịch không tồn tại/chưa hoàn tất

### E.7. Chi trả cho Tài xế / Thợ (Payout / Settlement)
> Đặc thù riêng của domain marketplace 2 chiều (khách hàng trả tiền, tài xế/thợ nhận tiền) — không phải mọi hệ thống thanh toán đều có chiều này.

- Tính đúng số tiền tài xế/thợ được nhận sau khi trừ phí nền tảng (hoa hồng, phí dịch vụ) theo đúng công thức nghiệp vụ
- Đợt chi trả định kỳ (ví dụ hàng tuần) — tổng hợp đúng tất cả giao dịch trong kỳ, không thiếu không thừa, không tính trùng giao dịch đã chi trả ở kỳ trước
- Tài xế/thợ có giao dịch bị hoàn tiền/tranh chấp **sau khi** đã được đưa vào đợt chi trả — xử lý đúng ở kỳ tiếp theo (trừ lại), có thông báo rõ ràng để tài xế/thợ hiểu tại sao bị trừ
- Chi trả thất bại (sai thông tin tài khoản ngân hàng, tài khoản bị khóa) — có cơ chế phát hiện, thông báo, và giữ lại đúng số tiền để chi trả lại, không bị mất

---

<a name="f"></a>
## F. Theo dõi vị trí Real-time (Real-time Location Tracking)

> Tính năng lõi của app đặt xe/giao hàng — khách hàng theo dõi tài xế/shipper di chuyển trên bản đồ theo thời gian thực. Khác với Mục A (cơ chế truyền tin nói chung), Mục F tập trung vào **tính đúng đắn và mượt mà của trải nghiệm bản đồ**, và khác với Mục C.6 (phát hiện gian lận vị trí ở góc độ nghiệp vụ/an toàn), Mục F kiểm tra vị trí hiển thị **đúng, mượt, kịp thời** ở góc độ trải nghiệm kỹ thuật thông thường.
>
> **Điều kiện áp dụng:** app có bản đồ hiển thị vị trí tài xế/shipper/thợ di chuyển real-time cho khách hàng theo dõi, hoặc ngược lại (tài xế thấy vị trí điểm đón/điểm giao).

### F.0. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo hệ thống thực tế) |
|---|---|
| Tần suất cập nhật vị trí là bao lâu? | `[Ví dụ: mỗi 3-5 giây, hoặc theo khoảng cách di chuyển]` |
| Cơ chế truyền vị trí là gì? | `[WebSocket / Polling định kỳ / Kết hợp cả hai khi mất kết nối]` |
| Bản đồ dùng nhà cung cấp nào? | `[Google Maps / Mapbox / OpenStreetMap / khác]` |
| Có tính năng chỉ đường (route) và ETA (thời gian dự kiến đến) không? | `[Có/Không]` |

### F.1. Độ chính xác và cập nhật vị trí
- Vị trí hiển thị trên bản đồ khớp đúng với vị trí thực tế của thiết bị (trong sai số GPS thông thường), cập nhật đúng tần suất đã cấu hình
- Vị trí cập nhật **mượt mà** trên bản đồ (marker di chuyển liên tục hợp lý), không bị "nhảy cóc" giật cục giữa các điểm cập nhật nếu nghiệp vụ yêu cầu animation mượt
- Thiết bị đứng yên (tài xế dừng đèn đỏ, dừng chờ) — vị trí không dao động lung tung do sai số GPS nhỏ (jitter), marker giữ ổn định hợp lý
- Vị trí không hợp lệ (ví dụ tọa độ (0,0), tọa độ ngoài phạm vi phục vụ, giá trị null do mất tín hiệu GPS tạm thời) — hệ thống lọc bỏ đúng, không hiển thị marker nhảy về sai vị trí

### F.2. Độ trễ và đồng bộ đa người xem
- Độ trễ giữa vị trí thực tế và vị trí hiển thị trên bản đồ khách hàng nằm trong ngưỡng chấp nhận được theo yêu cầu nghiệp vụ
- Nhiều người cùng theo dõi 1 tài xế/đơn hàng (ví dụ khách hàng và người thân được chia sẻ theo dõi đơn) — tất cả nhận cập nhật vị trí đồng bộ, không người này thấy vị trí mới còn người kia thấy vị trí cũ kéo dài
- Khách hàng theo dõi nhiều đơn hàng cùng lúc (nếu nghiệp vụ cho phép) — mỗi bản đồ/marker cập nhật đúng, không lẫn vị trí giữa các đơn khác nhau

### F.3. Mất tín hiệu GPS / Kết nối
- Tài xế đi vào khu vực mất tín hiệu GPS (hầm, nhà cao tầng, khu vực sóng yếu) — bản đồ hiển thị đúng trạng thái "mất tín hiệu" thay vì đứng yên mãi ở vị trí cũ mà không có chỉ báo, hoặc nội suy hợp lý theo hướng di chuyển gần nhất (tùy thiết kế)
- Có tín hiệu GPS trở lại sau khi mất — vị trí cập nhật lại đúng ngay, không hiển thị đường di chuyển sai (đường thẳng nhảy vọt từ vị trí cũ đến vị trí mới thay vì theo đúng lộ trình thực nếu nghiệp vụ có snap-to-road)
- Kết nối mạng của khách hàng (người xem bản đồ) bị gián đoạn — khi có mạng lại, bản đồ đồng bộ về đúng vị trí mới nhất ngay, không hiển thị vị trí đã lỗi thời kéo dài mà không có chỉ báo

### F.4. Route & ETA (nếu áp dụng)
- Tuyến đường hiển thị hợp lý, khớp với đường đi thực tế của tài xế (nếu có snap-to-road)
- Tài xế **đi lệch khỏi tuyến đường đã đề xuất** ban đầu (do tắc đường, chọn đường khác) — bản đồ và ETA cập nhật lại đúng theo tuyến đường thực tế, không giữ tuyến cũ đã sai
- ETA (thời gian dự kiến đến) cập nhật hợp lý theo tình hình di chuyển thực tế (tài xế đi chậm/nhanh hơn dự kiến), không giữ cố định một giá trị ước tính ban đầu suốt hành trình
- Tài xế đến gần điểm đích — có thông báo/chỉ báo phù hợp (ví dụ "tài xế sắp đến"), đúng ngưỡng khoảng cách/thời gian đã cấu hình

### F.5. Hiệu năng bản đồ ở mức thủ công
- Bản đồ tải và hiển thị mượt trên thiết bị cấu hình trung bình/thấp, không giật lag đáng kể khi có animation di chuyển marker
- Zoom in/out, kéo bản đồ trong lúc đang có cập nhật vị trí real-time — thao tác người dùng không bị gián đoạn hoặc bản đồ tự động nhảy về vị trí tài xế một cách khó chịu (trừ khi người dùng chủ động bấm nút "quay về vị trí hiện tại")
- Chạy nền lâu (theo dõi đơn hàng thời gian dài) — không gây hao pin bất thường hoặc tăng dữ liệu di động vượt mức hợp lý, không bị hệ điều hành tự động dừng cập nhật vị trí nền quá sớm

---

<a name="g"></a>
## G. Đánh giá 2 chiều (Rating / Review)

> Đặc thù của marketplace 2 chiều: không chỉ khách hàng đánh giá tài xế/thợ, mà tài xế/thợ cũng đánh giá ngược lại khách hàng. Đây vừa là 1 luồng CRUD thông thường (áp dụng trực tiếp Mục 1–11 của `Testcase_Template.md`), vừa có phần đặc thù riêng vì rating là **dữ liệu đầu vào trực tiếp cho thuật toán Matching (Mục C)** — sai sót ở đây ảnh hưởng dây chuyền sang cả trải nghiệm ghép nối.
>
> **Điều kiện áp dụng:** hệ thống có tính năng đánh giá sau khi hoàn thành đơn hàng/chuyến đi/dịch vụ, ở một hoặc cả hai chiều (khách ↔ tài xế/thợ).

### G.0. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo hệ thống thực tế) |
|---|---|
| Đánh giá áp dụng theo chiều nào? | `[Chỉ khách đánh giá tài xế / Cả hai chiều]` |
| Thang điểm đánh giá là gì? | `[Ví dụ: 1-5 sao, có kèm nhận xét chữ hay không]` |
| Đánh giá có bắt buộc không, hay có thể bỏ qua? | `[Bắt buộc / Tùy chọn]` |
| Điểm trung bình được tính như thế nào? | `[Trung bình cộng đơn giản / Có trọng số theo thời gian (đánh giá gần đây quan trọng hơn) / khác]` |
| Có cơ chế ẩn danh đánh giá không? | `[Có/Không]` |

### G.1. Luồng đánh giá cơ bản
- Hoàn thành đơn hàng/chuyến đi → màn hình đánh giá hiển thị đúng thời điểm, đúng đối tượng cần đánh giá
- Gửi đánh giá hợp lệ (điểm số, kèm/không kèm nhận xét theo đúng quy định bắt buộc/tùy chọn) — lưu thành công, không cho đánh giá trùng lặp cho cùng 1 đơn hàng
- Bỏ qua đánh giá (nếu không bắt buộc) — không ảnh hưởng đến các luồng khác (thanh toán, lịch sử đơn hàng vẫn hoạt động bình thường)
- Đánh giá kèm nhận xét chữ chứa nội dung không phù hợp (ngôn từ thô tục, thông tin cá nhân, link ngoài) — hệ thống có cơ chế lọc/kiểm duyệt trước khi hiển thị công khai (nếu nghiệp vụ yêu cầu)

### G.2. Tính toán điểm trung bình & Hiển thị
- Điểm trung bình của tài xế/thợ/khách hàng được tính đúng theo công thức đã xác định ở G.0, cập nhật ngay sau mỗi đánh giá mới
- Số lượng đánh giá còn **quá ít** (ví dụ tài xế mới chỉ có 1-2 đánh giá) — điểm trung bình hiển thị đúng nhưng cần cân nhắc: có gắn nhãn "mới" hay áp dụng công thức làm mượt (Bayesian average) để tránh 1 đánh giá cực đoan làm lệch điểm quá mức không
- Điểm trung bình được làm tròn đúng quy tắc hiển thị (ví dụ 4.7 sao không hiển thị 4.66666...)

### G.3. Tương tác với Thuật toán Matching (liên kết Mục C)
- Đối tượng có điểm đánh giá **thấp hơn ngưỡng tối thiểu** (nếu nghiệp vụ có quy định) — bị giảm ưu tiên ghép nối, hoặc bị tạm ngưng hoạt động đúng theo chính sách, xem thêm Mục C.1
- Đánh giá mới vừa được gửi — có cập nhật **ngay lập tức** vào tiêu chí ghép nối cho lần ghép tiếp theo hay có độ trễ (batch cập nhật định kỳ) — cần xác nhận rõ để không hiểu nhầm là bug nếu có độ trễ theo thiết kế

### G.4. Tranh chấp & Xử lý đánh giá không công bằng
- Đối tượng bị đánh giá cho rằng đánh giá **không công bằng/sai sự thật** — có cơ chế khiếu nại/báo cáo đánh giá đó không, quy trình xử lý thế nào (ẩn tạm thời chờ xét duyệt, giữ nguyên, gỡ bỏ)
- Đánh giá bị gỡ bỏ sau khiếu nại thành công — điểm trung bình được **tính toán lại đúng**, không giữ nguyên điểm cũ đã bị ảnh hưởng bởi đánh giá đã gỡ
- Phát hiện đánh giá từ **đơn hàng không có thật** (liên quan Mục C.6 — thông đồng tạo đơn ảo để đánh giá) — có cơ chế phát hiện và loại bỏ đánh giá giả không

### G.5. Chỉnh sửa và thu hồi đánh giá
- Cho phép **sửa đánh giá** trong khoảng thời gian nhất định sau khi gửi (nếu nghiệp vụ hỗ trợ) — điểm trung bình cập nhật đúng theo giá trị mới, không cộng dồn cả giá trị cũ và mới
- Hết thời gian cho phép sửa — tùy chọn sửa bị khóa, thông báo rõ ràng
- Xóa đơn hàng/tài khoản có liên quan đến đánh giá đã tồn tại (xem Mục 10 — Kiểm tra xóa dữ liệu của file chính) — đánh giá được xử lý đúng theo nghiệp vụ (giữ lại ẩn danh, hay xóa theo, ảnh hưởng đến điểm trung bình thế nào)

### G.6. Phân quyền & Hiển thị
- Người đánh giá và người được đánh giá thấy đúng nội dung theo quyền hạn (ví dụ tài xế không thấy được ai đã cho mình bao nhiêu sao cho từng đơn cụ thể nếu nghiệp vụ yêu cầu ẩn danh, chỉ thấy điểm trung bình tổng)
- Đánh giá hiển thị công khai (nếu có) đúng theo bộ lọc/kiểm duyệt nội dung đã áp dụng ở G.1

---

## Tự review — Điểm yếu và khuyến nghị bổ sung

### Điểm mạnh
- Đã bổ sung đầy đủ 2 mục phát hiện thiếu ở lần rà soát trước (Mục F — Real-time Location, Mục G — Rating/Review 2 chiều), và bổ sung góc nhìn gian lận thuật toán vào Mục C.6 — cả 3 điểm yếu mức độ Cao/Trung bình đã xác định trước đó đều được xử lý
- Mục F phân biệt rõ với Mục A (cơ chế truyền tin) và Mục C.6 (phát hiện gian lận vị trí) — tránh trùng lặp nội dung dù cùng chủ đề "vị trí GPS", mỗi mục nhìn từ góc độ khác nhau (kỹ thuật truyền tin / trải nghiệm bản đồ / an toàn-gian lận)
- Mục G liên kết chặt với Mục C (rating là input của matching) thay vì viết tách rời không liên quan
- Mục C.6 cover đủ 4 loại gian lận phổ biến nhất trong marketplace 2 chiều: giả mạo vị trí, thao túng trạng thái, đa tài khoản, thông đồng — không chỉ dừng ở "fake GPS" như yêu cầu ban đầu mà mở rộng đúng hướng

### Điểm yếu còn lại — phát hiện khi tự rà soát lần này

| # | Điểm yếu | Mức độ |
|---|---|---|
| 1 | **Mục D (Saga) chưa đề cập nhánh song song (Parallel Saga)** — đã ghi nhận từ lần trước, vẫn chưa xử lý. Ví dụ: giữ chỗ tài xế và xác thực mã giảm giá chạy song song thay vì tuần tự | Trung bình |
| 2 | **Mục E chưa có case đa tiền tệ** — đã ghi nhận từ lần trước, vẫn chưa xử lý. Chỉ cần thiết nếu dự án có kế hoạch mở rộng đa quốc gia, chưa chắc cần ngay giai đoạn đầu | Thấp |
| 3 | **Mục F chưa đề cập đến quyền riêng tư vị trí** (Location Privacy) — ví dụ: khách hàng có thể tắt chia sẻ vị trí chính xác cho tài xế trước khi đơn được xác nhận không, dữ liệu lịch sử vị trí được lưu trữ/xóa theo chính sách nào (liên quan GDPR/quy định bảo vệ dữ liệu cá nhân nếu áp dụng) | Trung bình |
| 4 | **Mục G chưa đề cập đánh giá theo từng khía cạnh cụ thể** (multi-aspect rating — ví dụ đánh giá riêng về "thái độ", "đúng giờ", "chất lượng dịch vụ" thay ví chỉ 1 điểm số tổng) — chỉ cần thiết nếu nghiệp vụ thiết kế theo hướng này, không phải mọi hệ thống đều cần | Thấp |
| 5 | **Chưa có mục về Khuyến mãi / Mã giảm giá (Promotion Engine)** — đây là tính năng rất phổ biến trong domain đặt hàng/đặt xe (mã giảm giá, chương trình khách hàng thân thiết, ưu đãi theo khung giờ) có nhiều quy tắc phức tạp riêng (điều kiện áp dụng, chồng mã, giới hạn số lần dùng) — có thể cần 1 mục H riêng nếu dự án có tính năng này ở mức phức tạp | Trung bình-Cao |

### Khuyến nghị
- Ưu tiên theo dõi điểm #5 (Khuyến mãi) trong quá trình phân tích SRS thực tế của dự án — nếu hệ thống có mã giảm giá phức tạp (chồng mã, theo tầng khách hàng, giới hạn ngân sách chương trình), nên đề xuất bổ sung Mục H khi bắt tay vào phân tích SRS module đó, thay vì viết trước khi biết rõ độ phức tạp thực tế của nghiệp vụ khuyến mãi dự án này
- Điểm #3 (Location Privacy) nên xác nhận sớm với BA/Legal nếu dự án phục vụ thị trường có quy định bảo vệ dữ liệu cá nhân nghiêm ngặt
- Các điểm còn lại (#1, #2, #4) giữ nguyên trạng thái theo dõi, bổ sung khi gặp đúng tình huống thực tế trong dự án — không cần viết trước khi chưa rõ mức độ liên quan

**Đề xuất tiếp theo:** Nếu bạn xác nhận dự án có tính năng bản đồ/vị trí real-time, tôi khuyến nghị viết thêm **Mục F** vào file này trước khi bắt tay vào dự án — đây là khoảng trống có xác suất cao sẽ dùng đến ngay từ những testcase đầu tiên.
