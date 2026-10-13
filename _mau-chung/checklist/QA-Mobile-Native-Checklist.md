# Checklist Kiểm thử Native Mobile App (iOS & Android)
### File thứ 3a — Bổ sung cho `Testcase_Template.md` (~95%) và `Template_Testcase_Advanced.md`

---

## Quan hệ với các file khác

| File | Phạm vi |
|---|---|
| `Testcase_Template.md` | Field validation, CRUD, phân quyền, quy tắc nghiệp vụ... — **áp dụng chung cho Web và Mobile ở mức chức năng**. Mục 21 (Responsive/Cross-platform) trong file đó chỉ nói về **layout/UI thích ứng màn hình nhỏ** (bố cục, cỡ chữ, bàn phím ảo) |
| `Template_Testcase_Advanced.md` | 7 dạng case đặc thù domain đặt hàng/đặt xe/tìm dịch vụ (Message Queue, Offline-first, Matching, Saga, Payment, Location Tracking, Rating) |
| `QA-TV-App-Checklist.md` | Checklist riêng cho TV app (điều hướng bằng remote, không có cảm ứng) — xem file đó nếu dự án có app chạy trên TV |
| **File này** | **Hành vi tương tác giữa mobile app với hệ điều hành/thiết bị** — vòng đời app, quyền truy cập, cảm biến, gián đoạn hệ thống, gesture |

**Ranh giới rõ ràng:** Mục 21 (`Testcase_Template.md`) trả lời "màn hình có hiển thị đúng trên điện thoại không?" — File này trả lời "app có sống sót và hoạt động đúng qua các tình huống thực tế của một thiết bị di động không?" (bị gọi điện, bị đẩy xuống nền, mất quyền, hết pin...).

**Nền tảng áp dụng:** Cả iOS và Android. Với mỗi mục, phần khác biệt giữa 2 nền tảng được ghi chú riêng — nếu app chỉ nhắm 1 nền tảng, bỏ qua phần ghi chú của nền tảng còn lại.

---

## Mẫu danh sách test case

> Cùng format với `Template_Testcase_Advanced.md` — không có cột Automation (quản lý automation vẫn theo `CLAUDE.md` ở file `.test.md` chính).

| ID | Mục đích kiểm thử | Tiền điều kiện | Các bước thực hiện | Kết quả mong muốn | Kết quả thực tế | Mức độ ưu tiên | Nền tảng | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| TC-[Mã]-001 | [Mô tả testcase] | [Tiền điều kiện] | 1. [Bước 1]<br>2. [Bước 2] | [Kết quả mong muốn chi tiết] | P/F | High | iOS/Android/Cả 2 | |

> Cột **Nền tảng** là điểm khác biệt so với các file trước — bắt buộc ghi rõ vì rất nhiều case trong file này chỉ đúng cho 1 nền tảng (ví dụ hành vi background của iOS khác Android).

### Quy tắc mức độ ưu tiên (riêng cho file này)

| Mức độ | Tiêu chí |
|---|---|
| **High** | Mất dữ liệu người dùng (App Lifecycle, mất kết nối giữa giao dịch), Quyền truy cập ảnh hưởng chức năng cốt lõi, Bảo mật khi khóa màn hình, Crash khi gián đoạn, **Gián đoạn luồng thanh toán/xác thực bên thứ 3 (O.1), Bấm nhầm do content shift ở control quan trọng (O.2)** |
| **Medium** | Trải nghiệm giảm nhưng không mất dữ liệu (chuyển mạng, đa cửa sổ), **Input bị autofill/autocorrect can thiệp sai (O.4), Sai sót thao tác trên bản đồ (O.7)** |
| **Low** | Case hiếm gặp, thiết bị đặc thù (foldable), thẩm mỹ giao diện, **thao tác vội trên control ít rủi ro (O.10)** |

---

## Mục lục

- [A. Vòng đời ứng dụng (App Lifecycle)](#a)
- [B. Gián đoạn hệ thống (Interruption Handling)](#b)
- [C. Quyền truy cập thiết bị (Runtime Permissions)](#c)
- [D. Phần cứng & Cảm biến (Hardware & Sensors)](#d)
- [E. Điều khiển cử chỉ (Gesture Control)](#e)
- [F. Khóa màn hình & Xác thực lại (Screen Lock & Re-authentication)](#f)
- [G. Thông báo đẩy (Push Notification)](#g)
- [H. Vòng đời Cài đặt / Cập nhật / Gỡ bỏ (Install-Update-Uninstall Lifecycle)](#h)
- [I. Tài nguyên thiết bị hạn chế (Resource Constraints)](#i)
- [J. Deep Linking / Universal Links / App Links](#j)
- [K. Đa cửa sổ / Đa nhiệm (Multi-window & Multitasking)](#k)
- [L. Đặc thù hình dạng màn hình thiết bị (Device Form Factor)](#l)
- [M. Mạng đặc thù thiết bị di động (Mobile-specific Network)](#m)
- [N. Trợ năng đặc thù Mobile (Mobile Accessibility)](#n)
- [O. Thao tác sai và Hành vi phi logic của người dùng thực tế (Real-world User Error & Illogical Interaction)](#o)
- [P. Ghi nhận sự cố & Giám sát (Crash Reporting & Monitoring)](#p)
- [Q. Bảo mật kết nối mạng ở tầng hệ điều hành (Network Transport Security)](#q)
- [R. Lưu trữ bảo mật trên thiết bị (Secure Storage — Keychain/Keystore)](#r)
- [S. Cơ chế cập nhật trong ứng dụng (In-App Update Mechanism)](#s)
- [T. Đa ngôn ngữ đặc thù Mobile (Mobile Localization)](#t)
- [U. Minh bạch khai báo quyền & dữ liệu (Privacy Declaration Compliance)](#u)

---

<a name="a"></a>
## A. Vòng đời ứng dụng (App Lifecycle)

> Đây là nhóm case quan trọng nhất và hay bị bỏ sót nhất — app di động không chạy độc lập như web, mà liên tục bị hệ điều hành đẩy vào nền, thu hồi tài nguyên, hoặc buộc dừng.
>
> **Điều kiện áp dụng:** mọi native mobile app (bắt buộc, không có ngoại lệ).

### A.0. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo app thực tế) |
|---|---|
| App có cần khôi phục đúng màn hình/trạng thái sau khi bị đẩy nền không? | `[Có/Không — nêu rõ những màn hình quan trọng]` |
| App có tác vụ nào cần tiếp tục chạy khi ở nền không? (định vị, tải file, cuộc gọi VoIP...) | `[Liệt kê tác vụ background nếu có]` |
| Có màn hình/luồng nào không được phép mất dữ liệu khi bị gián đoạn không? | `[Ví dụ: form thanh toán, form đặt xe đang nhập]` |

### A.1. Chuyển đổi Background ↔ Foreground
- Đẩy app xuống nền (bấm nút Home, vuốt sang app khác) → mở lại app **trong thời gian ngắn** → app hiển thị lại đúng ngay màn hình đang dùng, đúng trạng thái (không load lại từ đầu, không mất dữ liệu đang nhập)
- Đẩy app xuống nền → mở lại **sau thời gian dài** (vài giờ, qua đêm) → app xử lý đúng theo thiết kế: có thể cần tải lại dữ liệu mới nhất (session timeout, dữ liệu đã cũ), nhưng không crash hoặc hiển thị màn hình trắng
- Đang nhập liệu ở 1 form (chưa lưu) → chuyển sang app khác → quay lại → dữ liệu đã nhập **vẫn còn nguyên** trên form, không bị mất
- Đang có tác vụ nền được phép chạy (ví dụ định vị GPS phục vụ theo dõi đơn hàng) → xác nhận tác vụ đó **vẫn tiếp tục chạy đúng** khi app ở nền, đúng theo giới hạn thời gian hệ điều hành cho phép chạy nền (iOS giới hạn nghiêm ngặt hơn Android)

### A.2. App bị hệ điều hành thu hồi (Killed by OS)
- Hệ điều hành **tự động kill app** do thiếu RAM (thường xảy ra khi mở nhiều app cùng lúc trên thiết bị cấu hình thấp) → mở lại app từ icon → app khởi động lại đúng, khôi phục được trạng thái quan trọng nếu đã lưu tạm (ví dụ giỏ hàng, đơn hàng đang xử lý), không hiển thị lỗi khó hiểu
- Test mô phỏng: dùng công cụ dev (Android: `adb shell am kill`, iOS: Xcode debug kill) để buộc kill app ở từng màn hình quan trọng, xác nhận hành vi khôi phục đúng
- Phân biệt rõ 2 trường hợp khi mở lại app: **Cold start** (app hoàn toàn mới, chưa có tiến trình nào) vs **Warm start** (tiến trình còn nhưng bị kill) — cả 2 phải hoạt động đúng, không giả định luôn là 1 trong 2

### A.3. Force-stop / Đóng app thủ công
- Người dùng chủ động **Force Stop** app từ Cài đặt hệ thống → mở lại → app khởi động sạch (cold start), không giữ lại trạng thái tạm không mong muốn, nhưng dữ liệu đã lưu (đăng nhập, đơn hàng đã hoàn tất) vẫn còn nguyên
- Vuốt tắt app khỏi danh sách đa nhiệm (swipe away từ App Switcher/Recent Apps) → tác vụ nền (nếu có) dừng đúng theo thiết kế (một số tác vụ nên dừng ngay, một số cần cảnh báo trước khi cho phép tắt — ví dụ đang có cuốc xe đang chạy)

### A.4. Deep-link / Notification mở app khi đang ở các trạng thái khác nhau
- Mở app từ icon khi app **chưa chạy** (cold start) → khởi động đúng, vào đúng màn hình mặc định
- Mở app khi đang **chạy nền** → app được đưa lên foreground đúng, giữ nguyên trạng thái đang có trước đó (không bị reset về màn hình chính ngoài ý muốn)
- Mở app qua notification/deep link khi app đang **ở nền** → điều hướng đúng đến màn hình đích, không mất trạng thái các tab/màn hình khác đang mở

### A.5. Khác biệt nền tảng cần lưu ý
- **iOS**: thời gian cho phép chạy nền rất ngắn (thường vài chục giây) trừ khi dùng Background Modes hợp lệ (location, VoIP, audio...) — cần xác nhận đúng loại Background Mode được khai báo và test đúng giới hạn
- **Android**: có sự khác biệt lớn giữa các hãng máy (Xiaomi, Huawei, OPPO... có chính sách tối ưu pin aggressive tự kill app nền dù Android chuẩn cho phép) — cần test trên thiết bị thật của các hãng phổ biến tại thị trường mục tiêu, không chỉ test trên emulator/Pixel chuẩn

### A.6. Giới hạn dung lượng dữ liệu khôi phục trạng thái (State Restoration Size Limit)
- Dữ liệu cần lưu để khôi phục trạng thái (ví dụ toàn bộ form nhiều bước, danh sách item đã chọn) **vượt quá giới hạn dung lượng cho phép** của cơ chế lưu trạng thái hệ điều hành (Android: `Bundle` qua `onSaveInstanceState` giới hạn khoảng 1MB, vượt ngưỡng gây `TransactionTooLargeException` và **crash âm thầm khi xoay màn hình hoặc bị thu hồi**, không phải lỗi hiển thị rõ ràng) → xác nhận app dùng đúng chiến lược cho dữ liệu lớn: lưu vào local storage/ViewModel thay vì nhét toàn bộ vào Bundle
- Test cụ thể: mở màn hình có form nhiều trường/danh sách dài đã chọn nhiều item → xoay màn hình liên tục nhiều lần → không crash, không mất dữ liệu đã chọn

---

<a name="b"></a>
## B. Gián đoạn hệ thống (Interruption Handling)

> **Điều kiện áp dụng:** mọi mobile app — đặc biệt quan trọng với app dùng trong lúc di chuyển (đặt xe, giao hàng) vì tần suất gián đoạn cao hơn nhiều so với app dùng tại chỗ.

### B.1. Cuộc gọi đến / Cuộc gọi đi
- Có **cuộc gọi đến** khi đang dùng app → app tự động vào nền đúng cách, không crash; kết thúc cuộc gọi quay lại app → trạng thái được giữ nguyên như khi bị gián đoạn
- Đang trong luồng quan trọng (ví dụ đang xác nhận thanh toán) khi có cuộc gọi đến → sau cuộc gọi quay lại, luồng thanh toán không bị mất hoặc submit trùng
- App có tính năng gọi điện tích hợp (VoIP, gọi tài xế qua app) — nhận cuộc gọi thoại thông thường **trong lúc** đang gọi qua app → xử lý đúng theo thiết kế (ưu tiên cuộc nào, có thông báo xung đột không)

### B.2. Thông báo/Gián đoạn từ app khác hoặc hệ thống
- Có thông báo từ app khác hiện lên (banner notification) trong lúc đang dùng app → không làm gián đoạn thao tác đang thực hiện, không gây mất focus input đang gõ dở
- Báo thức/hẹn giờ/lịch reminder kêu giữa lúc đang dùng app → tương tự, không làm crash hoặc mất dữ liệu
- Cảnh báo pin yếu, cảnh báo bộ nhớ đầy của hệ thống hiện lên → app vẫn hoạt động bình thường phía sau, không bị treo

### B.3. Sạc pin / Kết nối phụ kiện
- Cắm/rút sạc đột ngột trong lúc dùng app → không ảnh hưởng đến trạng thái app hoặc dữ liệu đang xử lý
- Kết nối/ngắt kết nối tai nghe, Bluetooth trong lúc app đang phát âm thanh (nếu có) → xử lý đúng theo hành vi hệ điều hành chuẩn (thường tự dừng phát khi rút tai nghe)

### B.4. Chuyển đổi ứng dụng liên tục (App Switching nhanh)
- Chuyển qua lại giữa app này và app khác **nhiều lần liên tiếp trong thời gian ngắn** → không gây crash, không gây tình trạng UI hiển thị sai/chồng lấp do việc render lại không đúng lúc

---

<a name="c"></a>
## C. Quyền truy cập thiết bị (Runtime Permissions)

> **Điều kiện áp dụng:** app có sử dụng bất kỳ quyền nào cần xin phép người dùng khi chạy (camera, vị trí, danh bạ, microphone, thông báo, bộ nhớ, lịch...).

### C.0. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo app thực tế) |
|---|---|
| App yêu cầu những quyền nào? | `[Camera, Vị trí (While Using/Always), Microphone, Thông báo, Danh bạ, Bộ nhớ...]` |
| Quyền nào là bắt buộc để dùng được chức năng cốt lõi, quyền nào là tùy chọn? | `[Nêu rõ]` |
| App có giải thích lý do cần quyền trước khi xin (pre-permission prompt) không? | `[Có/Không]` |

### C.1. Luồng xin quyền lần đầu
- Xin quyền lần đầu → hiển thị đúng hộp thoại hệ thống, nội dung mô tả lý do rõ ràng (nếu có pre-permission prompt riêng của app trước khi bật hộp thoại hệ thống)
- Người dùng **Cho phép** → chức năng liên quan hoạt động đúng ngay
- Người dùng **Từ chối** → chức năng liên quan bị vô hiệu hóa đúng cách, có hướng dẫn rõ ràng cách bật lại quyền trong Cài đặt nếu người dùng muốn dùng sau, không để app crash hoặc treo khi thiếu quyền
- Với quyền vị trí trên iOS: phân biệt đúng 3 mức "Không cho phép", "Khi dùng app" (While Using), "Luôn luôn" (Always) — test riêng từng mức nếu app có tính năng cần "Always" (ví dụ theo dõi tài xế khi app ở nền)

### C.2. Thu hồi quyền giữa lúc đang dùng app
- Cấp quyền → đang dùng app bình thường → **vào Cài đặt hệ thống tắt quyền đó** (không thoát hẳn app) → quay lại app → app phát hiện đúng quyền đã bị thu hồi, xử lý đúng (vô hiệu hóa chức năng, thông báo rõ ràng), không crash khi cố truy cập tài nguyên không còn quyền
- Quyền vị trí bị đổi từ "Luôn luôn" xuống "Khi dùng app" giữa lúc có tác vụ nền đang chạy dựa vào vị trí → tác vụ đó dừng đúng cách, không silent fail không rõ lý do

### C.3. Từ chối quyền nhiều lần / Quyền bị khóa vĩnh viễn
- Từ chối quyền **2 lần liên tiếp** trên Android → hệ thống tự động chuyển sang "Không hỏi lại" — app phát hiện đúng tình huống này và hướng dẫn người dùng vào Cài đặt thủ công, không tiếp tục hiện popup xin quyền vô ích (vì hệ thống sẽ không hiện nữa)
- iOS: từ chối quyền lần đầu → app có nút/luồng để đưa người dùng đến đúng trang Cài đặt của app đó (không phải trang Cài đặt chung chung)

### C.4. Quyền theo phiên bản hệ điều hành khác nhau
- Test trên các phiên bản OS có mô hình quyền khác nhau (ví dụ Android 13+ có quyền thông báo runtime riêng biệt thay vì tự động cấp như trước; iOS có App Tracking Transparency (ATT) riêng cho theo dõi quảng cáo) — xác nhận đúng luồng xin quyền tương ứng với từng phiên bản OS mà app hỗ trợ

### C.5. Quyền truy cập media dạng hạt mịn / một phần (Granular & Partial Media Access)
- **Android 13+**: quyền ảnh/video được tách riêng (`READ_MEDIA_IMAGES`, `READ_MEDIA_VIDEO`) thay vì gộp chung `READ_EXTERNAL_STORAGE` — xác nhận app xin đúng loại quyền cần thiết, không xin thừa quyền không dùng đến
- **Android 14+ / iOS 14+**: người dùng có thể chọn **"Chỉ cho phép truy cập ảnh đã chọn"** (Selected Photos/Limited Access) thay vì cấp toàn bộ thư viện — xác nhận app hoạt động đúng với tập ảnh giới hạn này, có nút/luồng cho phép người dùng **chọn thêm ảnh** sau đó nếu cần (Android: `ACTION_PICK_IMAGES`; iOS: `PHPickerViewController` hoặc API tương đương), không coi việc chọn giới hạn là lỗi hoặc từ chối hoàn toàn
- Người dùng đã cấp "Chỉ ảnh đã chọn" → sau đó vào Cài đặt **chọn thêm ảnh khác** → quay lại app → app nhận diện đúng tập ảnh mới đã được bổ sung quyền, không cần khởi động lại app

---

<a name="d"></a>
## D. Phần cứng & Cảm biến (Hardware & Sensors)

> **Điều kiện áp dụng:** app có sử dụng camera, xác thực sinh trắc học, Bluetooth, NFC, hoặc cảm biến chuyển động của thiết bị.

### D.1. Xác thực sinh trắc học (Biometric — Face ID / Touch ID / Vân tay)
- Đăng nhập/xác nhận giao dịch bằng sinh trắc học → xác thực đúng → cho qua đúng luồng
- Xác thực **thất bại** (vân tay không khớp, khuôn mặt không nhận diện được) → có phương án dự phòng rõ ràng (nhập mật khẩu/PIN), không khóa cứng người dùng
- Thiết bị **không hỗ trợ** sinh trắc học hoặc người dùng **chưa thiết lập** trên thiết bị → app phát hiện đúng, tự động chuyển sang phương thức xác thực khác, không hiện tùy chọn sinh trắc học không dùng được
- Thêm/xóa vân tay hoặc khuôn mặt mới trong Cài đặt hệ thống sau khi đã liên kết với app → xử lý đúng theo chính sách bảo mật (có yêu cầu xác thực lại bằng phương thức khác không, vì dữ liệu sinh trắc học đã thay đổi)

### D.2. Camera
- Chụp ảnh trong app (ví dụ xác thực giấy tờ, chụp ảnh xác nhận giao hàng) → hoạt động đúng, ảnh lưu đúng chất lượng/định dạng yêu cầu
- Từ chối quyền camera → chức năng chụp ảnh vô hiệu hóa đúng (liên kết Mục C)
- Camera đang bị **app khác chiếm dụng** (ví dụ đang gọi video call app khác) → app xử lý đúng khi cố truy cập camera (thông báo lỗi rõ ràng, không crash)
- Xoay thiết bị trong lúc đang mở camera trong app → giao diện camera xử lý đúng hướng, không bị méo/lật hình

### D.3. Bluetooth / NFC (nếu áp dụng)
- Kết nối thiết bị Bluetooth ngoài (máy in hóa đơn, thiết bị POS) → kết nối đúng, dữ liệu truyền đúng
- Mất kết nối Bluetooth giữa lúc đang giao tiếp dữ liệu → app phát hiện và xử lý đúng (thông báo, thử kết nối lại), không treo vô thời hạn
- Thanh toán/quét NFC (nếu có) → đọc đúng, xử lý đúng lỗi khi thẻ/thiết bị không hợp lệ

### D.4. Cảm biến chuyển động (Accelerometer/Gyroscope) — nếu áp dụng
- Tính năng dựa vào cảm biến chuyển động (ví dụ phát hiện thiết bị đang di chuyển để tự động vào chế độ lái xe an toàn) → phản ứng đúng với các mức độ chuyển động khác nhau
- Thiết bị cũ/giá rẻ có cảm biến kém chính xác hơn → tính năng vẫn hoạt động chấp nhận được, không yêu cầu độ chính xác tuyệt đối gây lỗi liên tục

### D.5. Truy cập Clipboard (Clipboard Access Privacy)
- App **tự động đọc clipboard** (ví dụ tự dán mã giới thiệu, tự nhận diện mã OTP copy từ SMS) → trên iOS 14+/Android 12+, hệ thống hiển thị thông báo/toast cảnh báo mỗi khi app đọc clipboard — xác nhận app **chỉ đọc clipboard khi thực sự cần** (đúng lúc người dùng vào đúng màn hình liên quan), không đọc tùy tiện ở nhiều màn hình gây hiện thông báo cảnh báo liên tục làm người dùng nghi ngờ ứng dụng
- Nội dung clipboard **không phải định dạng mong đợi** (ví dụ đang mong đợi mã OTP 6 số nhưng clipboard có sẵn đoạn văn bản dài từ trước) → app nhận diện đúng, không tự động dán nhầm nội dung không liên quan vào field

---

<a name="e"></a>
## E. Điều khiển cử chỉ (Gesture Control)

> **Điều kiện áp dụng:** mọi mobile app có tương tác cảm ứng — nhưng đặc biệt cần chú ý nếu app có bản đồ, hình ảnh phóng to/thu nhỏ, hoặc danh sách có thao tác vuốt.

### E.1. Zoom (Pinch-to-zoom)
- Nơi **cho phép zoom** (ví dụ bản đồ, xem ảnh chi tiết) — zoom in/out mượt mà bằng cử chỉ 2 ngón tay, giới hạn zoom tối đa/tối thiểu hợp lý, không zoom vô hạn gây vỡ hình hoặc treo app
- Nơi **cố tình khóa zoom** (ví dụ khóa zoom trên bản đồ để buộc dùng nút +/- có kiểm soát, hoặc khóa zoom trên nội dung cố định layout) → xác nhận đúng: cử chỉ pinch không có tác dụng, không vô tình vẫn zoom được dù đã khóa
- Double-tap để zoom nhanh (nếu hỗ trợ) → hoạt động đúng, zoom về đúng mức đã định nghĩa (ví dụ 2x), double-tap lần nữa zoom về lại mức ban đầu

### E.2. Vuốt (Swipe)
- Vuốt để xóa item trong danh sách (nếu có) → đúng hướng, đúng ngưỡng khoảng cách vuốt để kích hoạt, có thể hủy nếu vuốt chưa đủ ngưỡng rồi thả tay
- Vuốt để refresh (pull-to-refresh) → kích hoạt đúng ngưỡng, hiển thị đúng animation loading, không kích hoạt nhầm khi chỉ đang cuộn danh sách bình thường
- Vuốt chuyển tab/trang (nếu có) → đúng hướng, mượt mà, không xung đột với việc vuốt để quay lại màn hình trước của hệ điều hành (đặc biệt trên iOS có edge-swipe-back, cần đảm bảo không xung đột với vuốt ngang trong app)

### E.3. Nhấn giữ (Long-press) & Đa điểm chạm (Multi-touch)
- Nhấn giữ để hiện menu ngữ cảnh (nếu có) — đúng thời gian ngưỡng kích hoạt, đúng vị trí menu hiện ra
- Đa điểm chạm không mong muốn (vô tình chạm nhiều ngón cùng lúc, ví dụ cầm điện thoại chạm cả lòng bàn tay) — app không có hành vi bất thường (không vô tình kích hoạt 2 hành động cùng lúc từ 2 điểm chạm khác nhau nếu không được thiết kế hỗ trợ multi-touch)

### E.4. Vùng chạm & Độ nhạy
- Kích thước vùng chạm của các nút/control đủ lớn theo chuẩn nền tảng (tối thiểu 44x44pt trên iOS, 48x48dp trên Android) — không quá nhỏ gây bấm nhầm
- Các control gần nhau (ví dụ nút Xóa cạnh nút Sửa) — khoảng cách đủ để tránh bấm nhầm, đặc biệt quan trọng với case rủi ro cao (xóa nhầm dữ liệu quan trọng)

---

<a name="f"></a>
## F. Khóa màn hình & Xác thực lại (Screen Lock & Re-authentication)

> **Điều kiện áp dụng:** mọi app có phiên đăng nhập, đặc biệt quan trọng với app có giao dịch tài chính.

### F.1. Khóa màn hình giữa lúc đang dùng app
- Màn hình tự khóa (hết thời gian chờ) hoặc người dùng chủ động khóa **giữa lúc đang có giao dịch dở dang** (ví dụ đang điền form thanh toán) → mở khóa quay lại app → dữ liệu đang nhập vẫn còn, giao dịch không bị submit tự động hay bị hủy ngầm
- App có yêu cầu **xác thực lại** sau khi mở khóa màn hình không (tùy chính sách bảo mật, đặc biệt app tài chính/ví điện tử thường bắt buộc) — nếu có, xác nhận đúng luồng xác thực lại, không cho phép bỏ qua vào thẳng nội dung nhạy cảm

### F.2. Thời gian phiên (Session Timeout) kết hợp với khóa màn hình
- Khóa màn hình trong **thời gian ngắn** (vài giây, vài phút) → mở lại, phiên vẫn còn hiệu lực, không bị đăng xuất
- Khóa màn hình **thời gian dài** vượt ngưỡng session timeout đã cấu hình → mở lại, app phát hiện đúng phiên đã hết hạn, yêu cầu đăng nhập lại đúng cách, không hiển thị dữ liệu cũ của phiên đã hết hạn trước khi xác thực lại

### F.3. Chụp màn hình / Ghi màn hình ở nội dung nhạy cảm
- Với màn hình có dữ liệu nhạy cảm cao (số thẻ, OTP, mật khẩu) — nếu nghiệp vụ yêu cầu chặn chụp/ghi màn hình vì lý do bảo mật, xác nhận đúng cơ chế chặn hoạt động (Android: `FLAG_SECURE`; iOS: hạn chế hơn nhưng có thể ẩn nội dung khi vào App Switcher)
- Vào App Switcher (xem danh sách đa nhiệm) — màn hình xem trước (preview/snapshot) không được lộ dữ liệu nhạy cảm nếu nghiệp vụ yêu cầu (nhiều app ngân hàng làm mờ/ẩn nội dung khi vào chế độ này)

---

<a name="g"></a>
## G. Thông báo đẩy (Push Notification)

> **Điều kiện áp dụng:** app có tích hợp push notification (hầu hết app đặt hàng/đặt xe đều có).

### G.0. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo app thực tế) |
|---|---|
| Notification có deep link đến màn hình cụ thể không? | `[Có/Không — liệt kê loại thông báo và màn hình đích tương ứng]` |
| Có notification dạng rich (kèm ảnh, action button trực tiếp trên notification) không? | `[Có/Không]` |
| Có phân loại kênh thông báo (notification channel/category) để người dùng tắt riêng từng loại không? | `[Có/Không]` |

### G.1. Nhận thông báo ở từng trạng thái app
- App **đang mở (foreground)** khi có thông báo đến → xử lý đúng theo thiết kế: hiển thị in-app banner tùy chỉnh, hay im lặng cập nhật dữ liệu, hay vẫn hiện thông báo hệ thống — cần rõ ràng theo nghiệp vụ, không mặc định giống hệt như khi app ở nền
- App **đang ở nền** khi có thông báo → hiện đúng thông báo hệ thống, bấm vào mở đúng app và điều hướng đúng màn hình
- App **đã bị tắt hẳn** (không có tiến trình) khi có thông báo → hiện đúng thông báo, bấm vào khởi động app (cold start) và điều hướng đúng đến đúng màn hình đích, không mở về màn hình mặc định sai

### G.2. Nội dung và hành động trên thông báo
- Nội dung thông báo hiển thị đúng, không bị cắt xén sai chỗ, hiển thị đúng cả khi có ký tự đặc biệt/emoji
- Notification có action button (ví dụ "Chấp nhận đơn" ngay trên thông báo, không cần mở app) → bấm hoạt động đúng, xử lý đúng ngầm và đồng bộ lại đúng khi mở app sau đó
- Nhiều thông báo cùng loại dồn dập → được gộp nhóm hợp lý (notification grouping) theo chuẩn nền tảng, không tràn ngập màn hình thông báo gây khó chịu

### G.3. Quyền và cấu hình thông báo
- Từ chối quyền thông báo → không nhận được bất kỳ thông báo nào, app không cố hiển thị fallback gây nhầm lẫn
- Tắt riêng 1 kênh thông báo cụ thể trong Cài đặt (ví dụ tắt thông báo khuyến mãi nhưng giữ thông báo đơn hàng) → chỉ đúng loại đó bị tắt, các loại khác vẫn nhận bình thường

### G.4. Làm mới Token thiết bị (Push Token Refresh/Rotation)
- Token định danh thiết bị nhận push (FCM/APNs) **tự động thay đổi** (xảy ra khi: cài lại app, khôi phục từ backup sang máy mới, hệ điều hành tự xoay vòng token định kỳ) → app phát hiện đúng token mới và **gửi lại lên server để cập nhật**, không tiếp tục dùng token cũ đã hết hiệu lực khiến người dùng ngừng nhận thông báo mà không ai biết
- Token cập nhật thất bại khi gửi lên server (mất mạng đúng lúc) → có cơ chế thử lại (retry) ở lần mở app tiếp theo, không bỏ qua vĩnh viễn
- Đăng xuất tài khoản này, đăng nhập tài khoản khác trên **cùng thiết bị** → token cũ được gỡ liên kết khỏi tài khoản trước đó và gắn đúng vào tài khoản mới, tài khoản cũ không tiếp tục nhận nhầm thông báo dành cho tài khoản mới trên thiết bị này

---

<a name="h"></a>
## H. Vòng đời Cài đặt / Cập nhật / Gỡ bỏ (Install-Update-Uninstall Lifecycle)

> **Điều kiện áp dụng:** mọi mobile app — đặc biệt quan trọng khi có thay đổi cấu trúc dữ liệu local (database schema) giữa các phiên bản.

### H.1. Cài đặt mới (Fresh Install)
- Cài đặt lần đầu trên thiết bị chưa từng có app → khởi động đúng, hiển thị đúng luồng onboarding (nếu có), không còn sót dữ liệu từ lần cài trước đó (nếu trước đó đã gỡ)

### H.2. Cập nhật phiên bản (Update)
- Cập nhật từ phiên bản cũ lên mới **khi đang có dữ liệu local quan trọng** (giỏ hàng, đơn hàng đang xử lý, cài đặt cá nhân) → dữ liệu được giữ nguyên/migrate đúng sang cấu trúc mới, không bị mất
- Cập nhật khi **schema database local thay đổi** (thêm/bớt/đổi kiểu cột) → có migration script chạy đúng, không crash khi mở app sau cập nhật do dữ liệu cũ không khớp cấu trúc mới
- Cập nhật khi app **đang chạy** (Android cho phép tải update nền) → xử lý đúng, không xung đột giữa phiên bản cũ đang chạy và phiên bản mới vừa cài

### H.3. Bắt buộc cập nhật (Force Update)
- Phiên bản hiện tại **dưới mức tối thiểu được hỗ trợ** (do API backend đã ngừng hỗ trợ version cũ) → app phát hiện đúng và chặn sử dụng, hiển thị màn hình yêu cầu cập nhật, không cho phép bỏ qua nếu là bắt buộc
- Có bản cập nhật **tùy chọn** (khuyến khích nhưng không bắt buộc) → hiển thị thông báo, cho phép bỏ qua và tiếp tục dùng phiên bản hiện tại

### H.4. Gỡ cài đặt & Cài lại
- Gỡ app khi còn dữ liệu local chưa đồng bộ lên server → xác nhận rõ hậu quả (mất dữ liệu chưa đồng bộ) là hành vi đã biết trước, không phải bug — nhưng nếu nghiệp vụ có yêu cầu cảnh báo trước khi gỡ (hiếm khi kiểm soát được ở mức app), ghi nhận rõ giới hạn này
- Gỡ rồi cài lại → coi như cài đặt mới hoàn toàn (trừ dữ liệu đã đồng bộ lên server, tài khoản đăng nhập lại vẫn thấy đúng dữ liệu từ server)

---

<a name="i"></a>
## I. Tài nguyên thiết bị hạn chế (Resource Constraints)

> **Điều kiện áp dụng:** mọi mobile app — quan trọng hơn với thị trường có nhiều thiết bị cấu hình thấp/giá rẻ.

### I.1. Bộ nhớ trong gần hết (Low Storage)
- Thiết bị gần hết dung lượng lưu trữ → thao tác cần ghi dữ liệu local (tải ảnh, cache, tải file) → xử lý đúng khi không đủ chỗ ghi (thông báo rõ ràng), không crash hoặc ghi dữ liệu lỗi (corrupt)

### I.2. RAM thấp / Nhiều app chạy nền
- Thiết bị có RAM thấp, đang mở nhiều app khác → app hoạt động chấp nhận được (có thể chậm hơn nhưng không crash liên tục) — liên quan Mục A.2 về việc bị OS kill khi thiếu RAM

### I.3. Pin yếu / Chế độ tiết kiệm pin (Low Power Mode / Battery Saver)
- Thiết bị vào chế độ tiết kiệm pin của hệ điều hành → các tác vụ nền của app (đồng bộ, định vị) có thể bị hệ điều hành hạn chế mạnh hơn bình thường — xác nhận app xử lý đúng khi tác vụ nền bị hạn chế (không giả định luôn chạy được như bình thường), có thông báo phù hợp cho người dùng nếu chức năng bị ảnh hưởng
- Pin xuống mức cảnh báo thấp (ví dụ dưới 10%, dưới 5%) trong lúc đang thực hiện giao dịch quan trọng → không có xử lý đặc biệt bắt buộc, nhưng nên đảm bảo giao dịch không bị mất dở nếu thiết bị tắt nguồn đột ngột (liên quan tính toàn vẹn dữ liệu — Mục 7, `Testcase_Template.md`)

### I.4. Kích thước cài đặt & Cập nhật ứng dụng
- Dung lượng cài đặt ban đầu và dung lượng sau khi dùng một thời gian (cache tích lũy) ở mức hợp lý, có cơ chế xóa cache nếu cần (tùy nghiệp vụ, không bắt buộc mọi app)

---

<a name="j"></a>
## J. Deep Linking / Universal Links / App Links

> **Điều kiện áp dụng:** app có xử lý link mở từ ngoài (email, SMS, mạng xã hội, trình duyệt, app khác) để điều hướng vào đúng màn hình trong app.

### J.1. Mở link khi app đã cài đặt
- Bấm link (SMS, email, web, app khác chia sẻ sang) khi **đã cài đặt** app → mở đúng app, điều hướng đúng đến màn hình/nội dung đích tương ứng với link, không mở về màn hình mặc định sai
- Link chứa tham số động (ví dụ mã đơn hàng, mã giới thiệu) → app đọc đúng tham số và xử lý đúng theo tham số đó

### J.2. Mở link khi app chưa cài đặt (Deferred Deep Linking)
- Bấm link khi **chưa cài đặt** app → điều hướng đúng đến App Store/Play Store để cài đặt
- Sau khi cài đặt và mở app lần đầu (nếu có hỗ trợ deferred deep linking) → app nhớ đúng ngữ cảnh từ link ban đầu (ví dụ mã giới thiệu) và xử lý đúng, không mất ngữ cảnh dù phải qua bước cài đặt trung gian

### J.3. Link không hợp lệ hoặc đã hết hạn
- Link trỏ đến nội dung **không còn tồn tại** (đơn hàng đã bị xóa, khuyến mãi đã hết hạn) → app xử lý đúng, thông báo rõ ràng, không crash hoặc hiển thị màn hình trắng
- Link bị chỉnh sửa sai định dạng (thử nghiệm bảo mật cơ bản) → app không crash, xử lý như link không hợp lệ thông thường

---

<a name="k"></a>
## K. Đa cửa sổ / Đa nhiệm (Multi-window & Multitasking)

> **Điều kiện áp dụng:** thiết bị Android hỗ trợ Split-screen/Multi-window, iPad hỗ trợ Slide Over/Split View, hoặc thiết bị màn hình gập (foldable).

### K.1. Chế độ chia đôi màn hình (Split-screen — Android)
- Mở app ở chế độ chia đôi màn hình cùng 1 app khác → layout hiển thị đúng, thích ứng đúng với vùng màn hình bị thu nhỏ (không giống hoàn toàn với responsive thông thường vì đây là thay đổi kích thước động trong lúc app đang chạy, không phải load lần đầu)
- Thay đổi tỷ lệ chia màn hình (kéo thanh chia để to/nhỏ hơn) trong lúc app đang chạy → app tự động re-layout đúng theo thời gian thực, không bị vỡ giao diện hoặc treo

### K.2. iPad Slide Over / Split View (iOS)
- Tương tự K.1, áp dụng cho hệ sinh thái iPad nếu app hỗ trợ

### K.3. Thiết bị màn hình gập (Foldable)
- Gập/mở thiết bị trong lúc đang dùng app → app thích ứng đúng với sự thay đổi kích thước màn hình đột ngột, không mất trạng thái, không crash
- Nội dung hiển thị đúng khi trải dài qua "bản lề" màn hình gập (không bị nội dung quan trọng nằm đúng vị trí nếp gấp che khuất) nếu thiết bị mục tiêu có loại màn hình này

---

<a name="l"></a>
## L. Đặc thù hình dạng màn hình thiết bị (Device Form Factor)

> **Điều kiện áp dụng:** mọi mobile app — bổ sung cho Mục 21 (`Testcase_Template.md`) ở góc độ **thiết bị vật lý đặc thù**, không chỉ độ phân giải màn hình.

### L.1. Notch / Dynamic Island / Vùng an toàn (Safe Area)
- Nội dung quan trọng (nút bấm, văn bản, hình ảnh chính) không bị che khuất bởi notch, camera đục lỗ, hoặc thanh điều hướng cử chỉ ở cạnh dưới màn hình
- Nội dung tôn trọng đúng vùng an toàn (Safe Area) theo chuẩn từng nền tảng, đặc biệt khi xoay ngang màn hình (notch/Dynamic Island chuyển sang cạnh bên)

### L.2. Tỷ lệ màn hình đa dạng (Aspect Ratio)
- Test trên thiết bị có tỷ lệ màn hình rất dài (18:9, 20:9, 21:9 phổ biến ở Android tầm trung/thấp) — layout không bị kéo giãn bất hợp lý hoặc để trống khoảng lớn không dùng đến

### L.3. Máy tính bảng (Tablet)
- Nếu app hỗ trợ tablet — layout tận dụng đúng không gian màn hình lớn hơn (không chỉ phóng to y nguyên layout điện thoại gây khoảng trống lãng phí), nếu nghiệp vụ có thiết kế riêng cho tablet

---

<a name="m"></a>
## M. Mạng đặc thù thiết bị di động (Mobile-specific Network)

> Bổ sung cho Mục 15 (`Testcase_Template.md` — Error handling) ở các tình huống **đặc thù riêng của thiết bị di động** mà web app không gặp phải.

### M.1. Chế độ máy bay (Airplane Mode)
- Bật chế độ máy bay giữa lúc đang dùng app → app phát hiện đúng mất kết nối, xử lý đúng theo Mục 15 (không crash, thông báo rõ ràng)
- Tắt chế độ máy bay → app tự động khôi phục kết nối và đồng bộ lại đúng dữ liệu, không cần khởi động lại app

### M.2. Chuyển đổi giữa các loại mạng
- Chuyển từ WiFi sang dữ liệu di động (4G/5G) hoặc ngược lại giữa lúc đang tải dữ liệu/thực hiện giao dịch → không làm gián đoạn hoặc lỗi giao dịch, kết nối được nối lại đúng trên mạng mới (liên quan Mục 12.2 — Real-time)
- Mạng di động yếu/chập chờn (edge case phổ biến khi di chuyển, vào hầm gửi xe, thang máy) → app xử lý đúng độ trễ cao, timeout hợp lý, không đơ giao diện vô thời hạn

### M.3. VPN
- Sử dụng VPN trong lúc dùng app → các chức năng vẫn hoạt động đúng (trừ khi app có cơ chế chặn VPN vì lý do bảo mật/chống gian lận — nếu có, xác nhận đúng cơ chế phát hiện và thông báo)

### M.4. Thiết bị 2 SIM (Dual SIM)
- Với app có xác thực qua SIM/số điện thoại — thiết bị 2 SIM chọn đúng SIM để thực hiện xác thực (OTP qua SMS) hoặc cho phép người dùng chọn đúng SIM nếu cần

---

<a name="n"></a>
## N. Trợ năng đặc thù Mobile (Mobile Accessibility)

> Khác với Mục 17 (`Testcase_Template.md` — Keyboard Navigation, dành cho web), Mục N tập trung vào công cụ trợ năng gốc của hệ điều hành di động.

### N.1. Trình đọc màn hình (VoiceOver — iOS / TalkBack — Android)
- Bật trình đọc màn hình → điều hướng qua các phần tử trên màn hình theo đúng thứ tự hợp lý, mỗi phần tử được đọc mô tả rõ ràng, đúng ngữ nghĩa (không đọc "Button" trống không mà đọc đúng "Nút Đặt xe")
- Các hành động thao tác (chụp ảnh, chọn ngày...) có thể thực hiện được hoàn toàn bằng trình đọc màn hình, không có thao tác nào chỉ làm được bằng cử chỉ nhìn thấy

### N.2. Cỡ chữ động (Dynamic Type / Font Scaling)
- Tăng cỡ chữ hệ thống lên mức lớn nhất → giao diện app co giãn theo đúng, không bị cắt chữ, không bị chữ chồng lấp lên nhau hoặc tràn ra ngoài vùng chứa
- Giảm cỡ chữ xuống mức nhỏ nhất → tương tự, vẫn đọc được và layout không vỡ

### N.3. Độ tương phản & Chế độ màu
- Bật chế độ tương phản cao (nếu hệ điều hành hỗ trợ) → nội dung vẫn phân biệt rõ ràng
- Chế độ Dark Mode (nếu app hỗ trợ) → chuyển đổi đúng, không có phần tử bị "lạc màu" (chữ tối trên nền tối, hoặc ảnh không tương thích)

---

<a name="o"></a>
## O. Thao tác sai và Hành vi phi logic của người dùng thực tế (Real-world User Error & Illogical Interaction)

> Đây là nhóm khác biệt hoàn toàn về **góc nhìn** so với Mục A–N: các mục trên kiểm tra "app có hoạt động đúng với **tính năng của hệ điều hành** không" (góc nhìn kỹ thuật), còn Mục O kiểm tra "app có sống sót đúng khi **người dùng thật, không rành công nghệ, thao tác lung tung/sai/vội vàng** không" (góc nhìn hành vi con người). Đây thường là nguồn bug production nhiều nhất với app phục vụ đại chúng (đặt xe, đặt hàng, tìm dịch vụ) — nơi đa số người dùng không phải dân kỹ thuật.
>
> **Điều kiện áp dụng:** mọi mobile app phục vụ người dùng phổ thông (bắt buộc, ưu tiên cao ngang Mục A).

### O.0. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo app thực tế) |
|---|---|
| Màn hình/luồng nào được coi là "nhạy cảm" (mất dữ liệu ở đây gây hậu quả nghiêm trọng — tiền, đơn hàng)? | `[Liệt kê: thanh toán, đặt xe, xác thực OTP...]` |
| App có mở WebView/trình duyệt trong app cho luồng thanh toán/xác thực bên thứ 3 không? | `[Có/Không — nêu rõ luồng nào]` |
| Các control quan trọng nhất (dễ bấm nhầm nếu layout dịch chuyển) là gì? | `[Ví dụ: nút Đặt xe, nút Xác nhận thanh toán]` |

### O.1. Gián đoạn luồng nhạy cảm bằng điều hướng hệ thống

> Khác với Mục A (app bị đẩy nền), đây là trường hợp **người dùng chủ động điều hướng lùi** bằng thao tác gesture/nút Back của hệ điều hành ngay giữa lúc có 1 request quan trọng đang xử lý.

- Vuốt back (iOS edge-swipe) hoặc bấm nút Back hệ thống (Android) **ngay giữa lúc** đang submit form quan trọng (đặt đơn, thanh toán) — request đã gửi đi vẫn được xử lý đúng ở server dù UI đã rời màn hình; khi quay lại app, trạng thái hiển thị đúng kết quả thực tế (không hiển thị lại form trống như chưa từng submit, gây người dùng submit lại lần 2)
- **[Mức độ ưu tiên cao nhất]** App mở WebView/trình duyệt trong app cho luồng xác thực bên thứ 3 (3D Secure ngân hàng, OAuth đăng nhập Google/Facebook) — người dùng **vuốt tắt WebView hoặc bấm Back giữa lúc đang ở trang xác thực ngân hàng, trước khi có kết quả trả về** → app phải xử lý đúng: hoặc coi giao dịch chưa hoàn tất và không trừ tiền phía hệ thống, hoặc chủ động **hỏi lại trạng thái thật** từ server/cổng thanh toán (liên quan Mục E.4, `Template_Testcase_Advanced.md`) trước khi cho phép thao tác tiếp — tuyệt đối không được để trạng thái "lấp lửng" khiến người dùng không biết tiền đã bị trừ hay chưa
- Đóng hẳn app (kill app — liên quan Mục A.2/A.3) đúng lúc WebView thanh toán đang mở — mở lại app, trạng thái giao dịch hiển thị đúng theo thực tế đã xảy ra ở server, không hiển thị sai (báo thất bại dù thực ra đã thành công, hoặc ngược lại)

### O.2. Bấm nhầm do thay đổi layout động (Content Shift Mis-tap)

> Người dùng đưa ngón tay xuống định bấm 1 nút, nhưng đúng khoảnh khắc đó nội dung phía trên load xong và đẩy layout dịch chuyển — ngón tay chạm trúng nút khác.

- Banner/quảng cáo/ảnh load bất đồng bộ (load sau, không phải load cùng lúc với phần còn lại của trang) ở phía trên các nút hành động quan trọng — xác nhận layout **đã đặt chỗ (reserve không gian) trước** cho nội dung sắp load, không đẩy các phần tử bên dưới dịch chuyển sau khi người dùng đã có thể nhìn thấy và định thao tác
- Danh sách đang cuộn, dữ liệu mới load thêm (infinite scroll) — không chèn item mới vào **phía trên hoặc giữa** vị trí đang xem gây dịch chuyển toàn bộ danh sách xuống dưới, dẫn đến bấm nhầm item khác với item đang định bấm
- Trạng thái loading kết thúc và nội dung thật thay thế skeleton/placeholder — kích thước vùng chứa nội dung thật khớp đúng với skeleton đã hiển thị trước đó, không co giãn đột ngột

### O.3. Đóng ngoài ý muốn (Accidental Dismiss)

> Người dùng không rành thường bấm ra ngoài vùng nội dung khi không chắc phải làm gì tiếp, hoặc bấm nhầm vào nút đóng/hủy.

- Bấm ra ngoài vùng modal/bottom sheet đang mở (đang có dữ liệu nhập dở, ví dụ form nhập ghi chú cho tài xế) — xác nhận đúng hành vi thiết kế: có cảnh báo xác nhận trước khi đóng và mất dữ liệu hay không (đặc biệt với form đã nhập > 1 trường), không âm thầm đóng mất dữ liệu mà không hỏi lại
- Hộp thoại xác nhận hệ thống (system alert/dialog) — bấm ra ngoài vùng dialog để tắt (một số phiên bản Android tính hành vi này tương đương "Từ chối/Hủy") — xác nhận app xử lý đúng theo đúng trạng thái đã bị hủy, **không mặc định coi như người dùng đã "Đồng ý"** chỉ vì dialog đã biến mất
- Nút "Hủy"/"Đóng" (X) nằm gần nút hành động chính (ví dụ nút X đóng modal nằm sát nút "Xác nhận") — khoảng cách đủ xa để tránh bấm nhầm, đặc biệt với case rủi ro cao (hủy đơn hàng đang xử lý)

### O.4. Nhập liệu bị can thiệp sai (Input Interference)

> Bàn phím ảo, tính năng autofill, và các công cụ hỗ trợ gõ của hệ điều hành đôi khi "giúp sai" — điền/sửa dữ liệu mà chính người dùng không chủ ý và không để ý.

- Bật Autofill của hệ điều hành (địa chỉ, số điện thoại, email đã lưu) — điền tự động vào đúng field mong muốn, không điền nhầm dữ liệu cũ/không liên quan vào field khác gây sai lệch thông tin mà người dùng không kiểm tra lại
- Autocorrect/Auto-capitalize tự động sửa dữ liệu quan trọng (ví dụ tự viết hoa chữ cái đầu của mã giảm giá, tự "sửa" chuỗi ký tự OTP thành từ có nghĩa gần giống) — với các field có định dạng nghiêm ngặt (mã OTP, mã giảm giá, email), xác nhận app **tắt đúng tính năng autocorrect/autocapitalize** ở tầng input, không để hệ điều hành tự ý sửa sai dữ liệu
- Paste nội dung từ clipboard có lẫn ký tự ẩn/khoảng trắng không nhìn thấy (copy từ tin nhắn, ứng dụng khác) — app tự động trim/làm sạch đúng trước khi validate, không để lọt ký tự ẩn gây field "trông có vẻ đúng" nhưng thực ra sai giá trị
- Chuyển đổi bàn phím ngôn ngữ (ví dụ từ tiếng Việt sang tiếng Anh) **giữa lúc đang gõ dở** 1 field — không gây lỗi ký tự lẫn lộn hoặc mất nội dung đã gõ trước đó
- Nhập bằng giọng nói (voice-to-text, nếu bàn phím hệ thống hỗ trợ và field cho phép) — kết quả nhận dạng sai/không đúng ý — người dùng có thể dễ dàng xem lại và sửa trước khi submit, không bị submit thẳng nội dung nhận dạng sai

### O.5. Thao tác lặp lại do thiếu kiên nhẫn hoặc bấm nhầm (Impatient / Repeated Interaction)

> Khác với case double-submit kỹ thuật đã có ở Mục 13.4 (`Testcase_Template.md` — chống bấm nhiều lần khi đang xử lý), Mục O.5 nhìn từ góc **tâm lý người dùng thiếu kiên nhẫn hoặc không chắc đã bấm trúng chưa**, áp dụng rộng hơn chỉ riêng nút Submit.

- Người dùng bấm liên tục nhiều lần vào bất kỳ nút nào (không chỉ nút Lưu/Gửi) khi không thấy rõ dấu hiệu loading (spinner quá nhỏ, quá nhạt, hoặc load quá nhanh không kịp nhận biết) — xác nhận **mọi** nút hành động quan trọng trong app (không chỉ nút Submit chính) đều có cơ chế chống bấm nhiều lần, đặc biệt các nút điều hướng (mở màn hình khác) tránh mở nhiều instance màn hình chồng lên nhau
- Double-tap nhầm vào 1 nút đơn (định bấm 1 lần nhưng tay chạm 2 lần liên tiếp quá nhanh, phổ biến với người dùng lớn tuổi hoặc tay ướt/đang di chuyển) — nút chỉ kích hoạt hành động **đúng 1 lần**, không kích hoạt 2 lần liên tiếp gây hành động lặp (ví dụ đặt 2 đơn hàng từ 1 lần định bấm)
- Điều hướng tới/lui rất nhanh liên tiếp (bấm vào item → Back → bấm item khác → Back liên tục trong thời gian ngắn, phổ biến khi người dùng đang "lướt xem" so sánh nhiều lựa chọn) — không gây race condition giữa các API call của từng màn hình dẫn đến hiển thị sai dữ liệu (ví dụ màn hình A hiển thị dữ liệu của màn hình B do request trả về không đúng thứ tự)

### O.6. Môi trường thiết bị bị người dùng vô tình làm sai lệch

- Đồng hồ hệ thống bị người dùng **tự chỉnh sai** (cố ý hoặc vô tình chỉnh sai giờ/ngày trong Cài đặt, hoặc tắt tự động đồng bộ giờ mạng) — các tính năng phụ thuộc thời gian (mã OTP, khuyến mãi theo khung giờ, đặt lịch — liên quan Mục 28 `Testcase_Template.md`) xử lý đúng dựa trên **giờ server**, không tin tưởng hoàn toàn vào giờ thiết bị, có thông báo phù hợp nếu phát hiện lệch giờ đáng kể ảnh hưởng đến tính năng
- Xoay thiết bị liên tục nhanh (dọc-ngang-dọc-ngang, phổ biến khi vô tình lắc trong túi hoặc trẻ em nghịch) — không gây crash, không gây tình trạng nhiều lần re-render chồng chéo làm treo giao diện
- Cuộn (scroll) rất nhanh qua danh sách rồi bấm ngay vào 1 item trước khi dữ liệu của item đó kịp tải đầy đủ (lazy loading) — bấm vào đúng item đã chọn (không bị lệch do danh sách vẫn đang dịch chuyển), và nếu dữ liệu chi tiết chưa tải xong thì hiển thị đúng trạng thái loading tại màn hình chi tiết, không hiển thị dữ liệu rỗng/sai của item khác

### O.7. Sai sót liên quan đến vị trí/bản đồ

> Áp dụng cho app có dùng bản đồ để chọn điểm đón/điểm giao — rất phổ biến với domain đặt xe/giao hàng.

- Định vị GPS ban đầu **chưa chính xác** (đang "nhảy"/hiệu chỉnh trong vài giây đầu mở bản đồ) — người dùng xác nhận điểm đón ngay trong lúc định vị chưa ổn định → app hiển thị rõ ràng trạng thái "đang định vị/độ chính xác thấp", khuyến khích chờ hoặc xác nhận lại, không để người dùng vô tình xác nhận nhầm địa chỉ do định vị sai lệch tạm thời
- Người dùng kéo bản đồ đi xa vị trí thực tế của họ mà không để ý (khi đang chọn điểm đón thủ công) rồi xác nhận luôn — có hiển thị rõ khoảng cách/địa chỉ đã chọn để người dùng dễ nhận ra sai sót trước khi xác nhận, không chỉ hiển thị tọa độ khó hiểu
- Chạm nhầm vị trí trên bản đồ do bản đồ đang zoom/di chuyển animation chưa dừng hẳn — chỉ ghi nhận điểm chạm khi bản đồ đã ở trạng thái ổn định, không ghi nhận điểm chạm giữa lúc đang animate

### O.8. Sai sót khi đăng nhập/chuyển tài khoản

- Autofill của hệ điều hành gợi ý **sai tài khoản** đã lưu trước đó (phổ biến khi thiết bị dùng chung hoặc đã từng đăng nhập nhiều tài khoản) — người dùng chọn nhầm và đăng nhập bằng tài khoản khác — sau khi đăng nhập, hiển thị rõ ràng đang đăng nhập bằng tài khoản/số điện thoại nào (không chỉ vào thẳng nội dung) để người dùng dễ nhận ra và đăng xuất đổi lại nếu nhầm
- Bấm "Quên mật khẩu" **giữa lúc** đang trong 1 luồng khác (ví dụ đang trong luồng đặt đơn cần đăng nhập lại do hết phiên) rồi hoàn tất đặt lại mật khẩu — quay lại đúng luồng đặt đơn ban đầu, không mất tiến trình đang dở hoặc phải bắt đầu lại từ đầu

### O.9. Nút vật lý thiết bị gây side-effect ngoài ý muốn

- Bấm nhầm nút âm lượng vật lý trong lúc thao tác (một số thiết bị dùng tổ hợp phím âm lượng làm phím tắt chụp màn hình) — nếu vô tình kích hoạt chụp màn hình ở màn hình có dữ liệu nhạy cảm, xác nhận hành vi này không gây rủi ro bảo mật nghiêm trọng vượt quá kiểm soát của app (liên quan Mục F.3 — chặn chụp màn hình ở màn hình nhạy cảm)
- Bấm nút nguồn tắt màn hình đột ngột giữa lúc đang có thao tác quan trọng (không phải khóa màn hình thông thường mà tắt hẳn) — mở lại, trạng thái được khôi phục đúng tương tự Mục F.1

### O.10. Chọn nhầm giá trị do thao tác vội trên control

- Date/Time Picker dạng cuộn (scroll wheel) — vuốt nhanh quá đà chọn nhầm ngày/giờ khác với dự định, rồi xác nhận luôn mà không để ý kỹ — giá trị cuối cùng hiển thị rõ ràng, dễ đọc trước khi xác nhận (không chỉ hiện số nhỏ mờ khó nhận ra đã chọn sai)
- Dropdown/danh sách chọn cuộn nhanh và bấm ngay khi ngón tay vừa dừng — chỉ chọn đúng item mà ngón tay đang dừng lại, không chọn nhầm item liền kề do độ trễ giữa lúc dừng cuộn và lúc chạm chọn
- Slider (thanh trượt, nếu có — ví dụ chọn bán kính tìm kiếm) — thao tác kéo run tay (phổ biến khi đang di chuyển, ví dụ ngồi trên xe) vẫn chọn được giá trị chính xác theo ý định, có hiển thị giá trị số rõ ràng đi kèm để xác nhận, không chỉ dựa vào vị trí trực quan của thanh trượt

---

<a name="p"></a>
## P. Ghi nhận sự cố & Giám sát (Crash Reporting & Monitoring)

> Quay lại trục kỹ thuật OS/thiết bị — nhóm P–U bổ sung các case kỹ thuật còn thiếu ở A–N.
>
> **Điều kiện áp dụng:** app có tích hợp công cụ giám sát crash (Firebase Crashlytics, Sentry, Bugsnag...).

### P.0. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời |
|---|---|
| Công cụ giám sát crash đang dùng là gì? | `[Firebase Crashlytics / Sentry / Bugsnag / khác]` |
| Có gắn user ID vào báo cáo crash không? | `[Có/Không]` |
| Có log breadcrumb trước khi crash không? | `[Có/Không]` |

### P.1. Ghi nhận Crash cơ bản
- App bị crash (mô phỏng ở môi trường test) → sự kiện được ghi nhận đầy đủ: đúng phiên bản app, thiết bị/OS, stack trace, thời điểm
- Crash xảy ra khi app **đang ở nền** → vẫn được ghi nhận đúng khi mở lại lần sau, không mất báo cáo chỉ vì xảy ra lúc không ai thấy

### P.2. Non-fatal Error / Custom Logging
- Lỗi không crash hoàn toàn nhưng ảnh hưởng nghiêm trọng (API quan trọng lỗi, thanh toán thất bại) → log dưới dạng non-fatal event, không chỉ crash cứng mới được ghi
- Breadcrumb log hành động trước lỗi → đủ chi tiết để tái hiện, nhưng **không log dữ liệu nhạy cảm** (mật khẩu, số thẻ, OTP)

### P.3. Không gián đoạn trải nghiệm khi gửi báo cáo
- Gửi báo cáo chạy ngầm, không chặn UI, không làm chậm khởi động lần sau
- Gửi thất bại do mất mạng → lưu lại và gửi lại khi có mạng, không mất báo cáo

---

<a name="q"></a>
## Q. Bảo mật kết nối mạng ở tầng hệ điều hành (Network Transport Security)

> **Điều kiện áp dụng:** mọi app gọi API qua mạng.

### Q.1. Bắt buộc kết nối HTTPS
- App không gọi được API qua HTTP thuần trên OS hiện đại (iOS: App Transport Security; Android 9+: Network Security Config) — xác nhận không vô tình khai báo ngoại lệ HTTP rộng hơn cần thiết
- Nếu có ngoại lệ hợp lệ (domain cụ thể chưa lên HTTPS) — chỉ áp dụng đúng phạm vi đó, không mở rộng toàn bộ

### Q.2. Chứng chỉ SSL/TLS không hợp lệ
- Kết nối đến server có chứng chỉ hết hạn/tự ký/bị thu hồi (môi trường test) → app từ chối đúng, hiển thị lỗi rõ ràng, không âm thầm bỏ qua cảnh báo chứng chỉ
- Test man-in-the-middle (proxy debug như Charles/Fiddler) — nếu có Certificate Pinning, xác nhận kết nối bị từ chối khi chứng chỉ không khớp

### Q.3. Certificate Pinning — Vòng đời chứng chỉ (nếu áp dụng)
- Server gia hạn chứng chỉ theo chu kỳ → nếu app pin cứng 1 chứng chỉ mà chưa cập nhật kịp, toàn bộ API bị chặn sau khi chứng chỉ cũ hết hạn — rủi ro vận hành nghiêm trọng, cần test trước mỗi đợt gia hạn; xác nhận app pin theo Public Key hoặc có backup pin dự phòng

---

<a name="r"></a>
## R. Lưu trữ bảo mật trên thiết bị (Secure Storage — Keychain/Keystore)

> **Điều kiện áp dụng:** app lưu dữ liệu nhạy cảm trên thiết bị (token, thông tin thẻ, mật khẩu).

### R.1. Lưu trữ đúng nơi an toàn
- Token/dữ liệu xác thực lưu vào Keychain (iOS)/Keystore hoặc EncryptedSharedPreferences (Android) — không lưu vào SharedPreferences/UserDefaults thường (không mã hóa)

### R.2. Vòng đời dữ liệu bảo mật qua các thao tác thiết bị
- Gỡ cài đặt app → Keystore (Android) bị xóa theo app, nhưng **Keychain (iOS) mặc định vẫn còn** sau khi gỡ — xác nhận rõ đây có mong muốn không: cài lại có tự đăng nhập lại bằng token cũ không
- Backup/khôi phục thiết bị (iCloud/Google, sang máy mới) — dữ liệu bảo mật có được khôi phục theo đúng chính sách không (khuyến nghị không khôi phục token qua backup)
- Thiết bị root/jailbreak — nếu app có cơ chế phát hiện, xác nhận đúng hành vi cảnh báo/chặn theo thiết kế

---

<a name="s"></a>
## S. Cơ chế cập nhật trong ứng dụng (In-App Update Mechanism)

> Khác Mục H.3 (Force Update tầng ứng dụng) — Mục S kiểm tra API cập nhật chính thức của nền tảng (chủ yếu Android Play Core In-App Update API; iOS không có tương đương).
>
> **Điều kiện áp dụng:** app Android tích hợp Play Core In-App Update API.

### S.1. Cập nhật linh hoạt (Flexible Update)
- Bản cập nhật khuyến khích → tải ngầm, không chặn thao tác hiện tại, thông báo khi tải xong
- Tải gián đoạn (mất mạng) → tự thử lại hợp lý, không treo vô thời hạn

### S.2. Cập nhật ngay lập tức (Immediate Update)
- Bản cập nhật bắt buộc → toàn màn hình chuyển sang luồng cập nhật, chặn thao tác khác
- Thoát giữa chừng (bấm Back hệ thống) → quay lại yêu cầu cập nhật khi mở lại, không cho vào app ở phiên bản chưa đủ điều kiện

---

<a name="t"></a>
## T. Đa ngôn ngữ đặc thù Mobile (Mobile Localization)

> Góc độ hành vi hệ điều hành cho đa ngôn ngữ — khác việc chỉ dịch đúng nội dung text.
>
> **Điều kiện áp dụng:** app hỗ trợ ≥ 2 ngôn ngữ, hoặc có kế hoạch mở rộng quốc tế.

### T.1. Bàn phím ảo theo ngôn ngữ hệ thống
- Đổi ngôn ngữ hệ thống → bàn phím ảo gợi ý đúng theo ngôn ngữ đã chọn, không cưỡng ép luôn tiếng Anh
- Nhập ký tự có dấu đặc thù ngôn ngữ (tiếng Việt, Trung/Nhật/Hàn nếu hỗ trợ) → hiển thị và lưu đúng, không lỗi encode

### T.2. Độ dài văn bản thay đổi theo ngôn ngữ (Text Expansion)
- Cùng nội dung dịch sang ngôn ngữ dài hơn đáng kể (ví dụ tiếng Đức dài hơn tiếng Anh 30-40%) — layout co giãn đúng, không cắt chữ/vỡ giao diện

### T.3. Định dạng số, ngày giờ, tiền tệ theo Locale
- Định dạng ngày/giờ, phân cách hàng nghìn/thập phân, đơn vị tiền tệ đúng theo locale hệ thống — không hardcode 1 định dạng bất kể locale

### T.4. Hỗ trợ chiều viết phải-sang-trái (RTL) — nếu áp dụng
- Đổi ngôn ngữ RTL (Ả Rập, Do Thái...) → layout lật đúng chiều (icon back, menu, nút hành động đổi bên), không chỉ dịch chữ mà giữ nguyên layout trái-sang-phải

---

<a name="u"></a>
## U. Minh bạch khai báo quyền & dữ liệu (Privacy Declaration Compliance)

> Giao thoa giữa testcase và yêu cầu tuân thủ khi submit store — kiểm tra hành vi thực tế khớp với khai báo công khai.
>
> **Điều kiện áp dụng:** app chuẩn bị phát hành lên App Store/Play Store.

### U.1. Khớp giữa khai báo và hành vi thực tế
- Đối chiếu Privacy Manifest (iOS)/Data Safety (Android) đã khai báo với hành vi thực tế: mỗi loại dữ liệu thu thập chỉ dùng đúng mục đích đã nêu, không thu thập thêm loại chưa khai báo
- Mỗi quyền runtime (Mục C) tương ứng 1 mục đích đã khai báo rõ, không xin quyền "phòng khi cần"

### U.2. Xóa dữ liệu theo yêu cầu người dùng
- Tính năng "Xóa tài khoản/Xóa dữ liệu" (bắt buộc theo chính sách nhiều nền tảng) → thực hiện đúng, dữ liệu xóa/ẩn danh đúng cam kết, không chỉ ẩn UI còn nguyên ở backend

---

## Tự review — Điểm yếu và khuyến nghị bổ sung

> Phiên bản này đã nâng từ 15 mục (A–O) lên **21 mục (A–U)**: thêm 6 mục kỹ thuật mới (P–U) và đào sâu 4 mục hiện có (A.6, C.5, D.5, G.4) để nâng độ bao phủ trục "tương tác kỹ thuật OS/thiết bị" — trực tiếp giải quyết 2 trong 5 điểm yếu đã ghi nhận ở lần rà soát trước (Crash Reporting, App Store Compliance) và 1 điểm bán phần (Localization).

### Điểm mạnh
- Cover đầy đủ 21 nhóm theo 2 trục: **Trục kỹ thuật** (A–N, P–U — 20 mục) theo góc nhìn "app có hoạt động đúng với tính năng/ràng buộc hệ điều hành không" + **Trục hành vi người dùng** (O — 10 sub-mục) theo góc nhìn "app có sống sót đúng khi người dùng thật thao tác sai/vội/phi logic không"
- Nhóm P–U bổ sung đúng các mảng kỹ thuật quan trọng mà app thực tế nào cũng cần: giám sát lỗi sau khi phát hành (P), bảo mật tầng kết nối mạng (Q), bảo mật lưu trữ local (R), cơ chế cập nhật (S), đa ngôn ngữ (T), và tuân thủ khai báo minh bạch dữ liệu (U) — đây là các mảng thường bị bỏ qua trong checklist test case truyền thống vì nằm ở ranh giới giữa "test chức năng" và "vận hành/bảo mật/compliance", nhưng đều **kiểm thử được cụ thể**, không chỉ là lý thuyết
- Mục Q (Network Transport Security) và R (Secure Storage) đưa vào những case bảo mật cụ thể, ít khi xuất hiện trong checklist QA thông thường nhưng gây hậu quả nghiêm trọng nếu bỏ sót (ví dụ Q.3 — Certificate Pinning hết hạn gây sập toàn bộ API, R.2 — Keychain iOS còn sót token sau khi gỡ cài đặt)
- 4 điểm đào sâu (A.6, C.5, D.5, G.4) đều là case thực tế đã từng gây bug production tại nhiều dự án (ví dụ A.6 — `TransactionTooLargeException` là lỗi Android kinh điển, âm thầm crash chỉ khi xoay màn hình với dữ liệu lớn, rất khó tái hiện nếu không biết trước nguyên nhân)
- Mỗi mục tiếp tục ghi chú rõ khác biệt nền tảng (iOS vs Android) thay vì viết chung chung, giữ nhất quán phong cách với 20 mục trước đó

### Điểm yếu còn lại — phát hiện khi tự rà soát lần này

| # | Điểm yếu | Mức độ |
|---|---|---|
| 1 | ~~Thiếu mục về Crash Reporting & Monitoring Integration~~ → **Đã bổ sung (Mục P)** | — |
| 2 | ~~Thiếu mục về App Store/Play Store Compliance~~ → **Đã bổ sung (Mục U)** | — |
| 3 | ~~Chưa có case về Localization đặc thù mobile~~ → **Đã bổ sung (Mục T)** | — |
| 4 | **Chưa đề cập đến Wearable companion app** (Apple Watch, Wear OS) — cố ý không viết vì đây là phạm vi UI/UX hoàn toàn khác (màn hình rất nhỏ, tương tác Digital Crown/chạm ngắn), xứng đáng thành 1 file riêng thứ 4 nếu dự án thực sự có, không nên nhồi vào file mobile hiện tại | Thấp (chỉ nếu dự án thực sự có) |
| 5 | **Chưa có ma trận thiết bị/OS version cụ thể để test thực tế** (Device/OS Fragmentation Matrix) — đây là câu hỏi về **phạm vi thiết bị cần test**, không phải "test case" theo đúng nghĩa (không có kết quả mong muốn P/F cụ thể), nên cố ý không ép vào dạng checklist. Đã bổ sung Phụ lục hướng dẫn ngắn ở cuối file thay vì viết thành 1 mục đầy đủ | Đã giảm từ Trung bình → Thấp (có phụ lục hướng dẫn) |
| 6 | **Mục Q.3 (Certificate Pinning) và Mục S (In-App Update) có thể không áp dụng nếu team Dev chưa triển khai các cơ chế này** — 2 mục này giả định app đã có kiến trúc kỹ thuật tương ứng; nếu chưa có, cần bỏ qua đúng theo phần "Điều kiện áp dụng" đã ghi rõ đầu mỗi mục, không tính là thiếu sót | Thấp — đã có điều kiện áp dụng rõ ràng |
| 7 | **Chưa có case về Widget màn hình chính (Home Screen Widget)** nếu app có tính năng này (ví dụ widget hiển thị trạng thái đơn hàng đang giao ngay trên màn hình chính) — khá phổ biến với app đặt hàng/đặt xe nhưng chưa được cover | Trung bình — nên bổ sung nếu dự án xác nhận có widget |

### Khuyến nghị
- Điểm #4 (Wearable) nên tách thành file riêng độc lập nếu dự án xác nhận có, không gộp vào file này
- Điểm #7 (Home Screen Widget) là điểm đáng cân nhắc nhất còn lại — nên xác nhận sớm với PO có kế hoạch widget không, vì đây là tính năng UI hoàn toàn tách biệt (không chạy trong tiến trình chính của app, có vòng đời và giới hạn kỹ thuật riêng — ví dụ giới hạn tần suất refresh dữ liệu) và nên bổ sung thành 1 mục riêng nếu có
- **Mục O vẫn nên được ưu tiên đọc kỹ trước khi viết testcase cho bất kỳ luồng nào liên quan đến tiền** — đây vẫn là nơi rủi ro cao nhất trong toàn bộ 21 mục (O.1)
- Mục Q, R nên được review cùng đội Dev/Security trước khi áp dụng, vì cần biết chính xác kiến trúc bảo mật thực tế (có Cert Pinning không, lưu token ở đâu) mới viết được testcase đúng, không thể đoán từ bên ngoài

### Đánh giá coverage sau đợt cập nhật này

**Trục kỹ thuật OS/thiết bị: ước tính ~96%** — đã bổ sung đủ các mảng lớn còn thiếu (Crash Reporting, Network Security, Secure Storage, In-App Update, Localization, Privacy Compliance) cộng với đào sâu 4 điểm kỹ thuật cụ thể ở các mục hiện có. Phần còn lại (~4%) là các case thực sự niche/có điều kiện (Wearable, Widget) mà bản thân việc "có áp dụng hay không" phụ thuộc hoàn toàn vào tính năng thực tế của dự án — không thể và không nên viết trước khi chưa xác nhận, vì sẽ làm phình to file với case không dùng đến.

---

## Phụ lục: Hướng dẫn xác định phạm vi thiết bị/OS cần test

> Đây là hướng dẫn **lập kế hoạch test**, không phải checklist test case (không có kết quả mong muốn P/F cụ thể) — dùng để quyết định "test trên tổ hợp thiết bị/OS nào là đủ đại diện" trước khi bắt đầu viết/thực thi testcase ở các mục A–U.

**Nguyên tắc chọn tổ hợp thiết bị:**

1. **Theo phiên bản OS**: tối thiểu — phiên bản OS mới nhất, phiên bản OS thấp nhất mà app còn hỗ trợ (`minSdkVersion`/iOS Deployment Target), và 1 phiên bản ở giữa phổ biến nhất theo số liệu thị trường thực tế (tham khảo Google Play Console/App Store Connect Analytics nếu đã có dữ liệu người dùng, hoặc số liệu thị trường công khai nếu app mới)
2. **Theo hãng máy (Android)**: ưu tiên hãng chiếm thị phần cao nhất tại thị trường mục tiêu — riêng với case liên quan Mục A.5 (chính sách tối ưu pin aggressive), bắt buộc có ít nhất 1 thiết bị Xiaomi/Huawei/OPPO thật (không dùng emulator) nếu thị trường mục tiêu có tỷ lệ dùng các hãng này cao
3. **Theo phân khúc cấu hình**: 1 thiết bị cấu hình cao (đại diện trải nghiệm tốt nhất), 1 thiết bị cấu hình thấp/giá rẻ phổ biến (đại diện đa số người dùng thực tế, đặc biệt quan trọng với case Mục I — Resource Constraints, và Mục P — hiệu năng khi giám sát crash)
4. **Theo hình dạng màn hình**: ít nhất 1 thiết bị có notch/Dynamic Island, 1 thiết bị không có (liên quan Mục L)
5. **Cập nhật ma trận định kỳ**: ma trận này không cố định — cập nhật lại mỗi 6 tháng hoặc khi có số liệu phân bổ thiết bị người dùng thực tế mới từ analytics, không dùng mãi 1 danh sách thiết bị từ lúc dự án bắt đầu
