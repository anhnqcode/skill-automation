# Checklist Kiểm thử TV App
### File thứ 3b — Bổ sung cho `Testcase_Template.md` (~95%) và `Template_Testcase_Advanced.md`

---

## Quan hệ với các file khác

| File | Phạm vi |
|---|---|
| `Testcase_Template.md` | Field validation, CRUD, phân quyền, quy tắc nghiệp vụ... — nền tảng chung cho mọi loại giao diện |
| `Template_Testcase_Advanced.md` | 7 dạng case đặc thù domain đặt hàng/đặt xe/tìm dịch vụ |
| `QA-Mobile-Native-Checklist.md` | Checklist riêng cho Mobile app (iOS/Android) — vòng đời app, permission, gesture cảm ứng |
| **File này** | **Hành vi đặc thù của app chạy trên TV** — điều hướng bằng remote (không cảm ứng), khoảng cách xem xa, tích hợp nền tảng TV |
| checklist riêng cho thiết bị màn hình gắn tường (không kèm trong gói) | Kế thừa file này cho thiết bị **SmartScreen AOSP không GMS, có cả chạm lẫn D-pad, dùng chung cả hộ**. Ghi đè Mục C (ngưỡng trợ năng định tính → số cứng), tắt Mục D.2/D.3/D.4/E |
| `QA-Voice-Interaction-Checklist.md` | Thay thế Mục B.2 của file này khi sản phẩm có điều khiển bằng giọng nói ở mức intent/slot |
| `QA-Public-Share-Link-Checklist.md` | Áp dụng khi TV app hiện QR/link cho người khác truy cập dữ liệu mà không cần tài khoản |

**Ranh giới rõ ràng:** TV app **không dùng chung checklist tương tác với Mobile** — bản chất điều khiển hoàn toàn khác nhau (chạm tay vs bấm remote 5 nút), nên tách file riêng thay vì làm "Phần II" của file Mobile.

**Nền tảng áp dụng:** Android TV/Google TV, Apple tvOS, Amazon Fire TV, Samsung Tizen, LG webOS. Với mỗi mục, phần khác biệt giữa các nền tảng được ghi chú riêng — nếu app chỉ nhắm 1 nền tảng, bỏ qua phần ghi chú của nền tảng còn lại.

---

## Mẫu danh sách test case

> Cùng format với các file khác — không có cột Automation.

| ID | Mục đích kiểm thử | Tiền điều kiện | Các bước thực hiện | Kết quả mong muốn | Kết quả thực tế | Mức độ ưu tiên | Nền tảng TV | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| TC-[Mã]-001 | [Mô tả testcase] | [Tiền điều kiện] | 1. [Bước 1]<br>2. [Bước 2] | [Kết quả mong muốn chi tiết] | P/F | High | Android TV/Fire TV/tvOS/Tizen/webOS | |

> Cột **Nền tảng TV** bắt buộc ghi rõ — khác với giả định "Android TV và Fire TV giống nhau vì cùng nền Android", thực tế 2 nền tảng có remote và launcher khác biệt đáng kể.

### Quy tắc mức độ ưu tiên (riêng cho file này)

| Mức độ | Tiêu chí |
|---|---|
| **High** | Focus bị "vùng chết" khiến người dùng không thao tác được (Mục A), Focus Trap sai trong modal, Back button gây kẹt màn hình |
| **Medium** | Đặc thù từng nền tảng TV (Mục D.4), Route/media playback nếu có |
| **Low** | Ambient mode, thẩm mỹ 10-foot UI ở mức tinh chỉnh nhỏ |

---

## Mục lục

- [A. Điều hướng & Quản lý Focus bằng Remote (D-pad Navigation & Focus Management)](#a)
- [B. Phương thức nhập liệu đặc thù TV (TV Input Methods)](#b)
- [C. Khoảng cách xem & Khả năng đọc (10-foot UI & Readability)](#c)
- [D. Vòng đời & Tích hợp nền tảng TV (TV Platform Lifecycle)](#d)
- [E. Phát media trên TV (nếu app có video/audio)](#e)
- [F. Ma trận thiết bị & Hiệu năng phần cứng TV (Device Matrix & Performance)](#f)

---

<a name="a"></a>
## A. Điều hướng & Quản lý Focus bằng Remote (D-pad Navigation & Focus Management)

> Đây là nhóm quan trọng nhất của TV app — khác biệt cốt lõi so với mobile: **không có cảm ứng, chỉ điều khiển bằng remote với 4-5 nút hướng + OK**. Toàn bộ UI phải điều hướng được hoàn toàn bằng D-pad (lên/xuống/trái/phải/OK/Back).
>
> **Điều kiện áp dụng:** mọi TV app (bắt buộc).

### A.0. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo app thực tế) |
|---|---|
| Nền tảng TV mục tiêu là gì? | `[Android TV/Google TV, Fire TV, tvOS, Samsung Tizen, LG webOS...]` |
| Remote hỗ trợ những nút gì ngoài D-pad cơ bản? | `[Voice, số, màu (đỏ/xanh/vàng/xanh lá nếu có), phím tắt riêng]` |
| Có hỗ trợ điều khiển bằng gamepad/tay cầm chơi game không? | `[Có/Không]` |

### A.1. Điều hướng cơ bản bằng D-pad
- Mọi phần tử có thể tương tác (nút, item danh sách, ô nhập liệu) đều **nhận được focus** khi điều hướng bằng D-pad — không có "vùng chết" (phần tử tồn tại trên giao diện nhưng không bao giờ nhận được focus khi bấm hướng)
- Di chuyển focus theo đúng hướng logic, nhất quán về mặt không gian: bấm phải thì focus chuyển sang phần tử bên phải (không nhảy lung tung sang phần tử khác hướng)
- Focus hiện tại **luôn hiển thị rõ ràng bằng mắt thường** (viền sáng, phóng to, đổi màu nền...) — người dùng luôn biết đang ở đâu trên màn hình mà không cần đoán

### A.2. Bẫy Focus (Focus Trap) & Điểm biên
- Focus ở phần tử **nằm ở biên** màn hình (trên cùng, dưới cùng, trái/phải cùng) — bấm tiếp hướng đó có hành vi nhất quán: hoặc không di chuyển (không có gì để focus), hoặc cuộn màn hình đúng để lộ thêm nội dung, tùy thiết kế nhưng phải nhất quán toàn app
- Mở modal/dialog → focus **tự động chuyển vào trong modal** và bị giữ (trap) trong đó, không thể vô tình bấm hướng để focus "xuyên qua" ra ngoài modal về phần tử phía sau
- Đóng modal → focus **quay lại đúng phần tử** đã mở modal trước đó, không bị mất focus hoặc nhảy về đầu màn hình

### A.3. Nút Back/Quay lại
- Bấm Back ở màn hình con → quay về đúng màn hình cha, giữ đúng vị trí focus đã có trước khi vào màn hình con (không reset focus về đầu danh sách)
- Bấm Back liên tục nhiều lần → quay lại đúng theo lịch sử điều hướng, cuối cùng thoát app đúng cách (hoặc về màn hình chờ của launcher tùy thiết kế) — không bị kẹt ở 1 màn hình lặp vô hạn
- Bấm Back khi đang có tác vụ đang xử lý (đang tải dữ liệu) → xử lý đúng (hủy tác vụ, hoặc chặn Back đến khi xử lý xong tùy thiết kế), không gây trạng thái crash hoặc treo

### A.4. Cuộn danh sách dài bằng D-pad
- Danh sách dài (ví dụ danh sách sản phẩm/dịch vụ) — cuộn bằng D-pad mượt mà, tự động cuộn màn hình để giữ phần tử đang focus luôn hiển thị trong khung nhìn, không bị focus "biến mất" ra ngoài vùng nhìn thấy
- Giữ nút hướng lâu (fast scroll / long-press D-pad nếu remote hỗ trợ lặp phím) → cuộn nhanh hơn hợp lý, không bị giật/nhảy cóc bỏ sót item

### A.5. Focus ban đầu khi vào màn hình
- Mở màn hình mới → focus mặc định đặt đúng vào phần tử hợp lý đầu tiên (thường là item đầu danh sách hoặc nút hành động chính), không để trống focus (không phần tử nào được focus, khiến người dùng phải bấm hướng "mò" mới tìm ra được vị trí)

---

<a name="b"></a>
## B. Phương thức nhập liệu đặc thù TV (TV Input Methods)

> **Điều kiện áp dụng:** TV app có ô nhập liệu (tìm kiếm, đăng nhập) hoặc hỗ trợ điều khiển giọng nói/gamepad.

### B.1. Nhập liệu bằng bàn phím ảo trên màn hình (On-screen Keyboard)
- Focus vào ô nhập liệu → bàn phím ảo hiện đúng, điều hướng chọn từng ký tự bằng D-pad hoạt động chính xác, không bỏ sót phím hoặc focus nhảy sai hàng
- Nhập liệu dài (ví dụ mật khẩu, email) bằng cách chọn từng ký tự — trải nghiệm hợp lý, có gợi ý/autocomplete nếu nghiệp vụ hỗ trợ để giảm số lần bấm

### B.2. Điều khiển bằng giọng nói (Voice Remote) — nếu áp dụng
- Remote có nút mic riêng → kích hoạt tìm kiếm/điều khiển bằng giọng nói đúng, kết quả trả về chính xác với các câu lệnh thường dùng
- Giọng nói không rõ/có tiếng ồn nền → xử lý lỗi hợp lý, không crash, cho phép thử lại dễ dàng

### B.3. Gamepad/Tay cầm chơi game (nếu áp dụng)
- Nếu app hỗ trợ điều khiển bằng gamepad ngoài remote chuẩn — ánh xạ nút bấm đúng, tương đương với D-pad + OK + Back của remote chuẩn

### B.4. Khác biệt bộ nút giữa các loại Remote
- Test trên **nhiều loại remote khác nhau** của cùng nền tảng nếu có (ví dụ remote Android TV cơ bản khác remote có thêm nút màu/số của một số hãng TV) — các nút không chuẩn không được là con đường **duy nhất** để thực hiện 1 chức năng quan trọng (luôn phải có cách làm bằng D-pad+OK cơ bản)

---

<a name="c"></a>
## C. Khoảng cách xem & Khả năng đọc (10-foot UI & Readability)

> TV được xem từ khoảng cách xa (khoảng 3 mét / 10 feet, khác hẳn mobile cầm gần mắt) — đây là nguyên tắc thiết kế "10-foot UI" mà kiểm thử cần xác nhận.
>
> **Điều kiện áp dụng:** mọi TV app.

### C.1. Kích thước chữ và phần tử
- Toàn bộ văn bản quan trọng đọc được rõ ràng ở khoảng cách xem TV thông thường (test thực tế bằng cách lùi ra xa màn hình, không chỉ nhìn gần khi dev/test)
- Không có văn bản/thông tin quan trọng nào bị thu nhỏ đến mức chỉ đọc được khi đứng sát màn hình

### C.2. Độ tương phản và màu sắc
- Độ tương phản giữa chữ/nền đủ cao để đọc từ xa, kể cả trong phòng có ánh sáng khác nhau (phòng tối khi xem phim, phòng sáng ban ngày)
- Không dùng các cặp màu khó phân biệt ở khoảng cách xa (ví dụ đỏ/xanh lá cạnh nhau) — cũng liên quan đến người dùng mù màu

### C.3. An toàn vùng hiển thị (TV Safe Zone / Overscan)
- Nội dung quan trọng không đặt quá sát viền màn hình — một số TV (đặc biệt loại cũ hoặc chưa hiệu chỉnh overscan) cắt mất phần rìa hình ảnh; nội dung cốt lõi cần nằm trong "vùng an toàn" tiêu chuẩn (thường 90% vùng trung tâm màn hình)

---

<a name="d"></a>
## D. Vòng đời & Tích hợp nền tảng TV (TV Platform Lifecycle)

> Tương tự App Lifecycle của mobile nhưng có đặc thù riêng của TV: launcher tích hợp sẵn trên màn hình chờ, cơ chế "leanback", và các quy định riêng theo từng nền tảng TV.

### D.0. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo app thực tế) |
|---|---|
| App có card hiển thị trên màn hình chủ (Home Screen Channel/Row) của nền tảng TV không? | `[Có/Không]` |
| App có hỗ trợ tiếp tục xem (Continue Watching) từ màn hình chủ không? | `[Có/Không — chỉ áp dụng nếu có nội dung media]` |

### D.1. Khởi động lạnh & Khởi động lại (Cold Start & Resume)
- Mở app lần đầu sau khi bật TV → thời gian khởi động hợp lý, hiển thị màn hình chờ/loading rõ ràng, không để màn hình đen/trắng kéo dài không phản hồi
- Chuyển sang app khác rồi quay lại (resume) → giữ đúng trạng thái/màn hình đang xem trước đó — cần test riêng vì cơ chế quản lý tiến trình của từng nền tảng TV khác biệt đáng kể so với mobile

### D.2. Tích hợp Launcher / Màn hình chủ
- App hiển thị đúng card/preview trên màn hình chủ của nền tảng (nếu có tích hợp) — hình ảnh, tiêu đề hiển thị đúng, bấm vào mở đúng app đến đúng nội dung
- Tính năng "Tiếp tục xem" (Continue Watching) trên màn hình chủ (nếu áp dụng, thường cho app có video) — hiển thị đúng tiến độ đã xem, bấm vào tiếp tục đúng vị trí

### D.3. Đa người dùng / Hồ sơ (Multi-user Profiles) — nếu áp dụng
- TV thường có nhiều người dùng chung 1 thiết bị — nếu app hỗ trợ nhiều hồ sơ, chuyển đổi hồ sơ trên TV hoạt động đúng, mỗi hồ sơ có dữ liệu/cài đặt riêng biệt không lẫn lộn

### D.4. Đặc thù theo từng nền tảng TV
- **Android TV/Google TV**: tuân thủ đúng chuẩn Leanback hoặc Compose for TV (tùy công nghệ dùng), kiểm tra hoạt động đúng trên các thiết bị Android TV của nhiều hãng khác nhau (Sony, TCL, Xiaomi...) không chỉ trên Chromecast with Google TV chuẩn
- **Amazon Fire TV**: kiểm tra tương thích với remote Fire TV (có nút riêng biệt so với Android TV chuẩn dù cùng nền Android)
- **Apple tvOS**: tuân thủ chuẩn Focus Engine của Apple, kiểm tra hoạt động đúng với Siri Remote (cả thao tác chạm trên mặt touchpad của remote, không chỉ D-pad vật lý)
- **Samsung Tizen / LG webOS**: đây là nền tảng riêng biệt hoàn toàn (không phải Android) — cần test độc lập, không giả định hành vi giống Android TV dù giao diện có thể trông tương tự

### D.5. Màn hình chờ & Chế độ nền (Screensaver / Ambient Mode) — nếu áp dụng

> **Điều kiện áp dụng:** nền tảng TV có chế độ màn hình chờ riêng (Android TV Ambient Mode, Fire TV Screensaver, tvOS Aerial), hoặc app có tích hợp hiển thị thông tin ở chế độ chờ.

- Để app **đứng yên không thao tác** đủ lâu → màn hình chờ của hệ thống kích hoạt đúng thời điểm, không bị app chặn ngoài ý muốn
- Ngược lại: **app đang ở trạng thái không được phép ngủ** (đang phát media, đang đếm ngược, đang chờ xác nhận giao dịch) → màn hình chờ **không** được kích hoạt cắt ngang. Đây là case dễ sót nhất của nhóm này
- Thoát khỏi màn hình chờ (bấm phím bất kỳ) → app quay lại **đúng màn hình và đúng vị trí focus** trước đó, không reset về trang chủ
- Nếu app có nội dung hiển thị ở chế độ ambient — nội dung hiển thị đúng, cập nhật đúng, và **không lộ thông tin nhạy cảm** khi không có ai đứng trước màn hình

### D.6. Điều khiển thiết bị qua HDMI-CEC — nếu áp dụng

> **Điều kiện áp dụng:** app có tính năng điều khiển TV/thiết bị ngoại vi (bật/tắt nguồn, đổi nguồn vào, chỉnh âm lượng) qua giao thức HDMI-CEC. Khá hiếm, chỉ bật khi đặc tả có nhắc.

- Mở app từ trạng thái TV đang ở nguồn vào khác → app kích hoạt CEC chuyển nguồn đúng, không gây vòng lặp chuyển nguồn qua lại
- Tắt thiết bị phát (set-top box / dongle) trong lúc app đang chạy → TV xử lý đúng theo cấu hình, app không rơi vào trạng thái lửng
- Thiết bị **không hỗ trợ CEC** hoặc CEC bị tắt trong cài đặt TV → app thoái lui êm (graceful degradation), vẫn dùng được bằng remote thường, không hiện lỗi kỹ thuật

---

<a name="e"></a>
## E. Phát media trên TV (nếu app có video/audio)

> Chỉ áp dụng nếu TV app có chức năng phát video/nhạc (ví dụ app đặt hàng có thể không cần, nhưng ghi chú lại vì rất phổ biến ở TV app nói chung). Nếu app không có nội dung media, bỏ qua toàn bộ mục này.

### E.1. Điều khiển phát bằng Remote
- Play/Pause/Tua tới/Tua lui bằng nút chuyên dụng trên remote (nếu có) hoạt động đúng, phản hồi tức thời
- Thanh tua (seek bar) điều hướng bằng D-pad — tua đến đúng vị trí mong muốn, hiển thị thumbnail preview khi tua (nếu có hỗ trợ)

### E.2. Chuyển đổi chất lượng phát (Adaptive Bitrate)
- Mạng chậm đi giữa lúc đang phát → tự động giảm chất lượng để tránh giật/buffer liên tục, không dừng phát đột ngột
- Mạng khôi phục tốt hơn → tự động tăng lại chất lượng hợp lý

### E.3. Gián đoạn khi đang phát
- Có cuộc gọi/thông báo hệ thống hiện lên trong lúc đang phát toàn màn hình → xử lý đúng (tạm dừng hoặc tiếp tục phát tùy thiết kế), không crash
- Tắt TV rồi bật lại (hoặc app bị đưa vào chế độ chờ) trong lúc đang phát → khi quay lại, tiếp tục đúng từ vị trí đã dừng (nếu nghiệp vụ yêu cầu resume) hoặc quay về màn hình chi tiết nội dung, không tự động phát lại từ đầu ngoài ý muốn

---

<a name="f"></a>
## F. Ma trận thiết bị & Hiệu năng phần cứng TV (Device Matrix & Performance)

> Nhóm này trả lời câu hỏi mà 5 mục trên không trả lời: **"test trên tổ hợp thiết bị nào thì đủ đại diện, và app có chạy nổi trên phần cứng thật của người dùng cuối không?"**. Mức độ phân mảnh của TV cao hơn mobile đáng kể — 5 hệ sinh thái riêng biệt, mỗi hệ sinh thái lại nhiều hãng, nhiều đời chip.
>
> **Điều kiện áp dụng:** mọi TV app. Nếu sản phẩm chỉ nhắm **một** model thiết bị duy nhất (ví dụ thiết bị do nhà mạng cấp), Mục F.1 rút gọn còn 1 dòng nhưng **F.2 vẫn bắt buộc**.

### F.0. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo dự án thực tế) |
|---|---|
| Sản phẩm phát hành trên bao nhiêu nền tảng TV? | `[1 nền tảng riêng / nhiều nền tảng]` |
| Model thiết bị **yếu nhất** được cam kết hỗ trợ là gì? | `[tên model, RAM, chip]` |
| Độ phân giải và tần số quét mục tiêu? | `[1920×1080 @60Hz / 4K...]` |
| Có emulator/thiết bị ảo dùng được không, hay bắt buộc thiết bị thật? | `[có/không]` |

### F.1. Ma trận thiết bị đại diện

- Lập **ma trận thiết bị tối thiểu** trước khi bắt đầu chu kỳ test, theo 3 trục: **nền tảng** (Android TV / Fire TV / tvOS / Tizen / webOS) × **phân khúc phần cứng** (cao / trung / thấp) × **phiên bản hệ điều hành** (mới nhất / cũ nhất còn hỗ trợ)
- Mỗi ô trong ma trận phải chỉ đích danh **một model thật**, không ghi chung chung "một máy Android TV bất kỳ" — vì hành vi launcher và remote khác nhau theo hãng
- Bắt buộc có **ít nhất 1 thiết bị thật ở phân khúc thấp**. Emulator và Chromecast/thiết bị dev cao cấp **không thay thế được** cho việc phát hiện lỗi hiệu năng
- Với sản phẩm chỉ chạy trên 1 model do nhà cung cấp cấp phát: vẫn phải test trên **đúng model đó**, đúng bản firmware sẽ triển khai thực tế — không dùng máy tablet Android để thay thế

### F.2. Hiệu năng render trên phần cứng yếu

- Animation và hiệu ứng chuyển màn chạy **mượt trên thiết bị yếu nhất** trong ma trận, không giật khung hình rõ rệt bằng mắt thường ở khoảng cách xem 3m
- Cuộn danh sách dài có nhiều ảnh (poster, thẻ hình lớn) trên thiết bị yếu → không giật, không hiện ô trống kéo dài, không tụt khung hình khi giữ nút hướng để cuộn nhanh
- Thời gian **khởi động lạnh** trên thiết bị yếu nhất vẫn nằm trong ngưỡng chấp nhận được của đặc tả — đo bằng số, không đánh giá cảm quan
- Sử dụng bộ nhớ ổn định khi thao tác lặp lại (vào/ra màn hình chi tiết 20–30 lần) → không tăng dần dẫn tới bị hệ điều hành thu hồi tiến trình
- Nếu app có bản đồ, video, hoặc cập nhật dữ liệu liên tục → kiểm tra riêng mức tiêu thụ tài nguyên của các thành phần này trên thiết bị yếu, vì đây là nguồn giật lag phổ biến nhất

### F.3. Độ phân giải & tỉ lệ hiển thị

- App hiển thị đúng ở các độ phân giải được cam kết hỗ trợ (1080p, 4K nếu có) — không bị chữ nhoè do scale sai, không bị bố cục giãn lệch
- TV cấu hình sẵn ở chế độ hiển thị khác thường (zoom, tỉ lệ khung hình 4:3, chế độ trò chơi) → nội dung vẫn đọc được, kết hợp kiểm tra cùng Mục C.3 (vùng an toàn)

---

## Tự review — Điểm yếu và khuyến nghị bổ sung

### Điểm mạnh
- Tập trung đúng trọng tâm khác biệt cốt lõi của TV — Focus Management (Mục A) là phần chi tiết nhất và đúng bản chất khó nhất khi test TV app
- Ghi chú rõ khác biệt giữa các nền tảng TV (Mục D.4) thay vì giả định Android TV và Fire TV giống hệt nhau dù cùng nền Android
- Mục E (Media Playback) được đánh dấu rõ là điều kiện, không ép buộc nếu app không có nội dung media

### Điểm yếu đã được xử lý ở bản cập nhật này

| # | Điểm yếu ghi nhận trước đây | Đã xử lý bằng |
|---|---|---|
| 1 | Chưa có case về Ambient Mode / Screensaver | **Mục D.5** — kèm case ngược quan trọng: màn hình chờ **không** được cắt ngang khi app đang chờ xác nhận giao dịch |
| 2 | Chưa có case về điều khiển TV qua HDMI-CEC | **Mục D.6** — đánh dấu rõ là mục có điều kiện, chỉ bật khi đặc tả nhắc |
| 3 | Chưa có ma trận thiết bị/nền tảng TV cụ thể | **Mục F.1** — ma trận 3 trục, bắt buộc chỉ đích danh model thật, bắt buộc có thiết bị phân khúc thấp |
| 4 | Chưa có case hiệu năng render trên phần cứng TV yếu | **Mục F.2** — đo bằng số trên thiết bị yếu nhất trong ma trận, kèm case rò rỉ bộ nhớ khi thao tác lặp |

### Điểm yếu còn lại — phát hiện khi rà soát lần này

| # | Điểm yếu | Mức độ |
|---|---|---|
| 5 | **Chưa cover thiết bị lai vừa chạm vừa D-pad** — file này giả định TV *không có cảm ứng*. Thiết bị màn hình gắn tường (SmartScreen, kiosk, màn hình hội nghị) có **cả hai**, và chuyển qua lại giữa 2 kiểu điều khiển là ổ bug về focus. Đã tách sang checklist riêng cho thiết bị màn hình gắn tường (không kèm trong gói) | Trung bình |
| 6 | **Chưa cover nền tảng Android không có Google Mobile Services** — Mục D.4 mặc định Android TV luôn có GMS. Thiết bị AOSP thuần không có Google TTS, FCM, Google Maps SDK, Play Services. Đã tách sang checklist riêng cho thiết bị màn hình gắn tường (không kèm trong gói) | Trung bình |
| 7 | **Mục C (10-foot UI) hoàn toàn định tính** — "đọc được rõ ràng", "tương phản đủ cao" không assert được, không log bug được, hai tester dễ kết luận trái nhau. Khi đặc tả có ngưỡng số (sp, dp, tỉ lệ tương phản) thì phải dùng bản ghi đè ở checklist tầng 3 | Cao |
| 8 | **Chưa có case cho thiết bị TV dùng chung không đăng nhập cá nhân** — Mục D.3 giả định "có nhiều hồ sơ thì chuyển hồ sơ đúng", nhưng bỏ qua trường hợp **không có hồ sơ nào cả** mà vẫn hiển thị dữ liệu riêng tư trên màn hình giữa phòng khách | Trung bình |

### Khuyến nghị
- Điểm #7 nên ưu tiên xử lý cho mọi dự án có yêu cầu trợ năng: chuyển toàn bộ tiêu chí Mục C từ mô tả định tính sang ngưỡng đo được, mỗi ngưỡng là một test case riêng
- Điểm #5, #6, #8 đã có lời giải ở checklist tầng 3 — với dự án dùng thiết bị lai, **bắt buộc** bật file tầng 3 kèm theo, không dùng file này một mình
- Mục F.1 nên chốt ma trận thiết bị **trước** khi viết case, không phải sau — vì ma trận quyết định case nào cần nhân bản theo thiết bị
