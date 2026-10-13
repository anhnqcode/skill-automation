# Checklist Kiểm thử Link & QR Chia sẻ Công khai
### File tầng 3 — Áp dụng khi hệ thống cho phép người **không có tài khoản** xem dữ liệu qua một liên kết

---

## Quan hệ với các file khác

| File | Phạm vi | Quan hệ với file này |
|---|---|---|
| `Testcase_Template.md` | Nền tảng chung | **Kế thừa**, trừ Mục 9 — xem ghi chú bên dưới |
| `Testcase_Template.md` **Mục 9** (phân quyền theo vai trò) | Phân quyền theo tài khoản/vai trò | **Bị thay thế bởi file này.** Người xem link **không có tài khoản** — quyền truy cập gắn vào **mã**, không gắn vào người |
| `Template_Testcase_Advanced.md` | 7 dạng case rủi ro cao | **Bắc cầu Mục F** nếu trang công khai có bản đồ theo dõi realtime |
| checklist riêng cho thiết bị màn hình gắn tường (không kèm trong gói) | Thiết bị SmartScreen | **Bắc cầu Mục F.4** — phần hiển thị QR trên thiết bị ở file đó, phần trang web ở file này |
| `QA-Mobile-Native-Checklist.md` | App mobile | Bắc cầu Mục J (deep link) nếu link mở được trong app |
| **File này** | **Vòng đời mã truy cập · phạm vi dữ liệu lộ ra · chống dò mã · trải nghiệm người nhận không có tài khoản** | — |

**Ranh giới rõ ràng:** đây **không phải** checklist bảo mật tổng quát. Nó tập trung vào một mô hình truy cập cụ thể: **ai cầm được mã thì xem được** (capability-based). Mô hình này đánh đổi tiện lợi lấy rủi ro, nên toàn bộ an toàn nằm ở ba chỗ: **mã đủ khó đoán · phạm vi dữ liệu đủ hẹp · vòng đời đủ ngắn**. Ba trục đó là Mục A, C, B của file này.

### Nguyên tắc bao trùm

> **Giả định nền tảng:** mã sẽ bị chia sẻ lại ngoài tầm kiểm soát. Người nhận chụp màn hình, chuyển tiếp cho người khác, đăng lên nhóm chat. Thiết kế phải đúng **kể cả khi điều đó xảy ra** — nghĩa là dữ liệu lộ ra qua link phải hẹp tới mức chấp nhận được ngay cả với người lạ.
>
> Hệ quả kiểm thử: mọi case dạng *"chỉ người được chia sẻ mới xem được"* đều **sai giả định**. Case đúng phải là *"người cầm mã xem được đúng phạm vi này, không hơn"* và *"mã hết hiệu lực đúng lúc"*.

---

## Mẫu danh sách test case

Dùng bảng thống nhất quy định trong `CLAUDE.md` Mục 4.2 — theo `Testcase_Template.md` Mục 24, bỏ 2 cột Automation:

| ID | Mục đích kiểm thử | Tiền điều kiện | Các bước thực hiện | Kết quả mong muốn | Kết quả thực tế | Mức độ ưu tiên | Ghi chú | Mã SRS |
|---|---|---|---|---|---|---|---|---|
| TC-[Mã]-001 | [Mô tả] | [Tiền điều kiện] | 1. …<br>2. … | [Kết quả chi tiết] | | P0 | | [Mã yêu cầu] |

- **Kết quả thực tế** để trống khi viết; người thực thi điền `P`/`F` sau khi chạy.
- **Mức độ ưu tiên** ghi `P0`/`P1`/`P2`. Case chạm vào **tiền · an toàn người dùng · rò rỉ dữ liệu · mất dữ liệu** được nâng lên `P0` bất kể xếp loại ban đầu.
- **Ghi chú** chỉ điền khi thật sự cần lưu ý (phát hiện nghiêm trọng, cần công cụ đặc biệt, tham số chưa chốt). Không có gì thì để trống.
- **Mã SRS** đặt sau cột Ghi chú; case do QA tự bổ sung ghi `[QA-ADD]`.
- **Không dùng cột Layer.** Ghi chú về tầng automation (nếu cần) để ở `.note.md`.

---

## Mục lục

- [A. Sinh mã truy cập](#a)
- [B. Vòng đời mã: hạn dùng, thu hồi, hết hiệu lực](#b)
- [C. Phạm vi dữ liệu lộ ra](#c)
- [D. Chống dò mã & lạm dụng](#d)
- [E. Trải nghiệm người nhận không có tài khoản](#e)
- [F. Dữ liệu cập nhật liên tục trên trang công khai](#f)
- [G. Rò rỉ qua đường phụ](#g)
- [H. Kênh phân phối: QR, liên kết, chuyển tiếp](#h)
- [I. Quản lý từ phía người chia sẻ](#i)
- [J. Khi dịch vụ lỗi](#j)

---

<a name="a"></a>
## A. Sinh mã truy cập

> **Điều kiện áp dụng:** mọi hệ thống có link chia sẻ công khai.

### A.0. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo đặc tả) |
|---|---|
| Độ dài / độ mạnh tối thiểu của mã? | `[ví dụ: ngẫu nhiên ≥128 bit]` |
| Một mã gắn với bao nhiêu bản ghi? | `[ví dụ: đúng 1]` |
| Hạn dùng mặc định là bao lâu? | `[con số — nếu đặc tả chỉ ghi "cấu hình", ghi NEEDS REVIEW]` |
| Mã có thu hồi được không? Ai thu hồi được? | `[...]` |
| Một bản ghi có thể có nhiều mã cùng lúc không? | `[...]` |

> ⚠ Nếu ô "hạn dùng" chưa có con số, **dừng lại và hỏi BA/PO** trước khi viết Mục B — không có số thì không có kết quả mong muốn.

### A.1. Thuộc tính của mã

- Mã sinh ra đạt **độ dài và độ mạnh tối thiểu** theo đặc tả. Layer **API**
- Sinh nhiều mã liên tiếp (tối thiểu 1000) → **không trùng nhau**, **không có quy luật đoán được** (không phải số tăng dần, không chứa mốc thời gian dễ đoán, không chứa mã bản ghi gốc)
- Mã **không chứa dữ liệu nhạy cảm** dưới dạng có thể giải mã ngược (không nhúng mã hộ, số điện thoại, mã đơn vào chính chuỗi mã)
- Hai bản ghi khác nhau → mã khác nhau. Cùng một bản ghi chia sẻ hai lần → hành vi đúng theo đặc tả (cùng mã hay mã mới), nhất quán

### A.2. Ràng buộc phạm vi của mã

- Một mã chỉ mở được **đúng bản ghi mà nó gắn vào**. Dùng mã của bản ghi A để truy cập bản ghi B → từ chối. Layer **Security**
- Mã **chỉ cho quyền đọc** — thử mọi thao tác ghi/sửa/xoá qua mã này đều bị từ chối ở tầng server, kể cả khi gọi thẳng API. Layer **API**, ưu tiên **P0**
- Mã không dùng được để suy ra hoặc truy cập **các bản ghi liên quan** (bản ghi trước đó của cùng người, danh sách bản ghi khác)

---

<a name="b"></a>
## B. Vòng đời mã: hạn dùng, thu hồi, hết hiệu lực

> **Điều kiện áp dụng:** mã có thời hạn hoặc có thể bị thu hồi.

### B.1. Hết hạn theo thời gian

- Truy cập bằng mã **còn hạn** → xem được đúng nội dung
- Truy cập bằng mã **đã quá hạn** → từ chối, hiện trang thông báo hết hiệu lực bằng ngôn ngữ đời thường, **không** hiện mã lỗi kỹ thuật, **không** lộ bất kỳ dữ liệu nào của bản ghi
- Truy cập **đúng quanh mốc hết hạn** (trước/sau vài giây) → hành vi nhất quán, không có vùng xám. Layer **API**
- Đang **mở sẵn trang** thì mã hết hạn → trang tự chuyển sang trạng thái hết hiệu lực, **không** tiếp tục hiển thị và cập nhật dữ liệu. Đây là case dễ sót nhất của nhóm này
- Mã hết hạn rồi thì **không hồi sinh được** — thử truy cập lại nhiều lần, thử tải lại trang, thử xoá bộ nhớ đệm

### B.2. Hết hiệu lực theo sự kiện nghiệp vụ

- Sự kiện kết thúc vòng đời bản ghi xảy ra (hoàn thành, huỷ) → mã hết hiệu lực **đúng thời điểm quy định** (ngay lập tức, hoặc sau khoảng thời gian đặc tả)
- Trong khoảng thời gian ân hạn (nếu có) → nội dung hiển thị đúng trạng thái cuối cùng, không hiển thị dữ liệu đang cập nhật nữa
- Bản ghi bị xoá ở hệ thống gốc → mã trỏ tới nó xử lý đúng, không lỗi kỹ thuật, không lộ dấu vết dữ liệu cũ

### B.3. Thu hồi chủ động

- Người có quyền thu hồi mã → mã **mất hiệu lực ngay lập tức**, kể cả với người đang mở sẵn trang
- Thu hồi rồi chia sẻ lại → mã mới hoạt động, **mã cũ vẫn chết**
- Thu hồi một mã **không** ảnh hưởng tới các mã khác còn hiệu lực (nếu hệ thống cho phép nhiều mã)
- Người **không có quyền** thu hồi → bị từ chối ở tầng server. Layer **API**

### B.4. Kiểm tra ở tầng server, không ở tầng giao diện

- Với **mọi** trạng thái mã không hợp lệ ở B.1–B.3, gọi thẳng API bằng mã đó → server từ chối. Không có trường hợp giao diện chặn nhưng API vẫn trả dữ liệu. Layer **API**, ưu tiên **P0**

---

<a name="c"></a>
## C. Phạm vi dữ liệu lộ ra

> Trục an toàn quan trọng nhất. Vì phải giả định mã sẽ bị chuyển tiếp cho người lạ, câu hỏi không phải *"ai xem được?"* mà là *"xem được **những gì**?"*.
>
> **Điều kiện áp dụng:** mọi hệ thống có link chia sẻ công khai.

### C.0. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo đặc tả) |
|---|---|
| Trường dữ liệu nào **được phép** hiển thị công khai? | `[danh sách đóng — cái gì không có trong danh sách là không được phép]` |
| Trường nào phải **che một phần**, che theo định dạng nào? | `[ví dụ: 09xx xxx 127]` |
| Trường nào **tuyệt đối không** được xuất hiện? | `[...]` |

### C.1. Dữ liệu trả về đúng phạm vi

- Gọi API của trang công khai bằng mã hợp lệ → **so từng trường** trong dữ liệu trả về với danh sách được phép ở C.0. Bất kỳ trường nào ngoài danh sách xuất hiện đều là lỗi, kể cả khi giao diện không hiển thị nó. Layer **API**, ưu tiên **P0**
- Dữ liệu nhạy cảm được **che ngay từ server**, không phải che ở giao diện. Kiểm chứng: dữ liệu trả về chứa giá trị đã che, **không** chứa giá trị đầy đủ
- Không lộ **mã định danh nội bộ** (mã người dùng, mã hộ, mã đơn nội bộ) có thể dùng để dò dữ liệu khác
- Không lộ thông tin về **các bản ghi khác** của cùng chủ sở hữu

### C.2. Giao diện không lộ thêm

- Xem mã nguồn trang, dữ liệu nhúng sẵn, và dữ liệu lưu tạm ở trình duyệt → không chứa trường ngoài danh sách cho phép. Layer **E2E**
- Ảnh, tệp đính kèm hiển thị trên trang → đường dẫn tới chúng cũng phải được bảo vệ, không truy cập trực tiếp được khi không có mã
- Thông báo lỗi trên trang không tiết lộ thông tin về dữ liệu bên trong

### C.3. Không suy ra được sự tồn tại của dữ liệu khác

- Mã sai và mã đúng-nhưng-hết-hạn trả về phản hồi **không giúp phân biệt** bản ghi có tồn tại hay không, nếu đặc tả yêu cầu điều này. Layer **Security**
- Thời gian phản hồi giữa hai trường hợp trên không chênh lệch đáng kể tới mức suy đoán được

---

<a name="d"></a>
## D. Chống dò mã & lạm dụng

> **Điều kiện áp dụng:** mã truy cập nằm trên đường dẫn công khai, không có bước xác thực nào khác.

### D.1. Dò mã

- Gửi **lượng lớn yêu cầu với mã ngẫu nhiên sai** → hệ thống giới hạn tần suất đúng, khoá tạm theo đúng quy tắc đặc tả, ghi nhận để cảnh báo. Layer **Security**
- Giới hạn áp dụng theo **cả hai chiều**: theo địa chỉ nguồn, và theo mã bị thử. Chỉ giới hạn một chiều là không đủ
- Dò từ **nhiều nguồn khác nhau** → vẫn phát hiện được mẫu hành vi bất thường ở mức hệ thống
- Bị khoá tạm rồi → **mã hợp lệ của người dùng bình thường vẫn truy cập được**, không bị vạ lây. Đây là case dễ sót và ảnh hưởng người dùng thật

### D.2. Lạm dụng mã hợp lệ

- Một mã hợp lệ bị truy cập **rất nhiều lần trong thời gian ngắn** → xử lý đúng theo đặc tả (giới hạn hoặc chấp nhận), không làm sập dịch vụ
- Một mã được mở **đồng thời từ nhiều nơi** → hành vi đúng theo thiết kế. Nếu đặc tả không nói gì, ghi `[NEEDS REVIEW]` — đây là câu hỏi thật, vì gia đình chia sẻ cho nhiều người là kịch bản bình thường
- Truy cập bằng công cụ tự động thay vì trình duyệt → xử lý đúng theo đặc tả

### D.3. Đầu vào bất thường trên đường dẫn

- Mã có **độ dài sai**, chứa ký tự đặc biệt, chứa chuỗi tấn công phổ biến → từ chối sạch, không lỗi kỹ thuật, không lộ dấu vết hệ thống. Layer **Security**
- Đường dẫn thiếu mã hoàn toàn → trang thông báo hợp lý

---

<a name="e"></a>
## E. Trải nghiệm người nhận không có tài khoản

> Người nhận thường là người lớn tuổi hoặc người ít dùng công nghệ, mở link trên điện thoại, không cài ứng dụng, không đăng nhập. Trải nghiệm phải hoạt động ngay lần chạm đầu tiên.
>
> **Điều kiện áp dụng:** mọi hệ thống có link chia sẻ công khai.

### E.1. Mở được ngay

- Mở link trên **điện thoại phổ thông**, trình duyệt mặc định, không cài gì thêm → xem được ngay, **không** bị chặn bởi yêu cầu đăng nhập, đăng ký, hay cài ứng dụng
- Mở trên nhiều trình duyệt và nhiều kích thước màn hình → bố cục đúng, không vỡ, chữ đọc được
- Mở trên **mạng di động chậm** → có trạng thái đang tải rõ ràng, nội dung chính hiện sớm

### E.2. Hiểu ngay đang xem gì

- Trang nêu rõ **đây là nội dung gì, của ai chia sẻ** ở mức được phép, để người nhận không nghĩ là link lừa đảo
- Trạng thái hiển thị bằng ngôn ngữ đời thường, không dùng thuật ngữ nội bộ hay mã trạng thái kỹ thuật
- Có chỉ báo rõ dữ liệu **cập nhật lần cuối lúc nào**, để người xem biết mình đang xem thông tin mới hay cũ

### E.3. Trang chỉ đọc

- **Không có** thao tác nào làm thay đổi dữ liệu trên trang. Rà soát toàn bộ phần tử tương tác
- Nếu trang có nút hành động được phép (ví dụ gọi điện) → chỉ mở ứng dụng ngoài, không gửi dữ liệu ngược về hệ thống

### E.4. Trạng thái đặc biệt

- Mã hết hạn, mã sai, bản ghi đã kết thúc → mỗi trạng thái có **trang riêng dễ hiểu**, nói rõ nên làm gì tiếp (liên hệ người chia sẻ), không phải trang lỗi trống

---

<a name="f"></a>
## F. Dữ liệu cập nhật liên tục trên trang công khai

> **Điều kiện áp dụng:** trang công khai hiển thị dữ liệu thay đổi theo thời gian thực (vị trí, trạng thái, tiến trình).
>
> Bắc cầu `Template_Testcase_Advanced.md` Mục F — file đó lo tính đúng đắn của dữ liệu vị trí, mục này lo phần **hiển thị trên kênh công khai**.

- Dữ liệu trên trang công khai cập nhật đúng nhịp, **đồng bộ** với dữ liệu người dùng chính nhìn thấy, không lệch kéo dài
- **Nhiều người cùng xem một mã** → tất cả nhận cập nhật như nhau, không ai bị đóng băng ở dữ liệu cũ
- Người xem **mất mạng rồi có lại** → trang đồng bộ về dữ liệu mới nhất, có chỉ báo trong lúc mất kết nối, không hiển thị dữ liệu cũ mà không báo
- Mở trang **rất lâu** (hàng giờ) → vẫn cập nhật, không rò rỉ bộ nhớ trên điện thoại, không hao pin bất thường
- Kết nối cập nhật của trang công khai **không** dùng được để lấy dữ liệu ngoài phạm vi mã cho phép. Layer **Security**
- Bản ghi kết thúc → luồng cập nhật liên tục **dừng hẳn**, không tiếp tục gửi dữ liệu

---

<a name="g"></a>
## G. Rò rỉ qua đường phụ

> Nhóm case kiểm tra dữ liệu thoát ra ngoài qua những con đường không ai để ý.
>
> **Điều kiện áp dụng:** mọi hệ thống có link chia sẻ công khai.

- **Không đưa dữ liệu nhạy cảm vào đường dẫn** — đường dẫn xuất hiện trong lịch sử trình duyệt, nhật ký máy chủ, thanh địa chỉ chụp màn hình. Chỉ mã truy cập được phép nằm ở đó
- Trang **không gửi mã truy cập sang bên thứ ba** qua tiêu đề chuyển hướng khi người dùng bấm vào liên kết ra ngoài
- Xem trước liên kết trong ứng dụng nhắn tin (ảnh, tiêu đề, mô tả tự sinh) → **không lộ dữ liệu nhạy cảm** ra ngay ở màn hình chat, nơi nhiều người trong nhóm nhìn thấy mà chưa cần mở link. Case này rất hay bị bỏ sót
- Trang **không bị lưu bộ nhớ đệm công khai** ở mức khiến người khác mở lại được sau khi mã đã hết hạn
- Trang **không bị công cụ tìm kiếm lập chỉ mục** — kiểm tra cấu hình chặn thu thập
- Nhật ký hệ thống ghi lại truy cập → không ghi kèm dữ liệu nhạy cảm ở dạng đọc được

---

<a name="h"></a>
## H. Kênh phân phối: QR, liên kết, chuyển tiếp

> **Điều kiện áp dụng:** mã được phát qua QR hoặc qua liên kết gửi đi.
>
> Phần hiển thị QR trên thiết bị màn hình lớn nằm ở checklist riêng cho thiết bị màn hình gắn tường (không kèm trong gói) Mục F.4.

- QR quét được bằng **camera mặc định** của điện thoại phổ thông, mở đúng trang, không cần ứng dụng quét riêng
- QR và liên kết dạng chữ trỏ tới **cùng một nội dung**
- Liên kết chuyển tiếp qua các ứng dụng nhắn tin phổ biến → không bị cắt, không bị thêm ký tự, vẫn mở đúng
- Liên kết dạng rút gọn (nếu có) → vẫn giữ nguyên các ràng buộc bảo mật ở Mục B, C
- Chia sẻ lại cho người thứ ba → hoạt động đúng như đã thiết kế, và **đây là hành vi phải được chấp nhận trong thiết kế**, không phải lỗi. Nếu đặc tả coi đây là vấn đề thì mô hình mã công khai là sai lựa chọn — ghi `.note.md`

---

<a name="i"></a>
## I. Quản lý từ phía người chia sẻ

> **Điều kiện áp dụng:** người dùng chính có màn hình quản lý các mã đã chia sẻ.

- Người chia sẻ **thấy được** những mã đang còn hiệu lực của mình, kèm thời điểm hết hạn
- Thu hồi được từng mã, có xác nhận trước khi thu hồi, có phản hồi sau khi thu hồi thành công
- Sau khi thu hồi → danh sách cập nhật đúng, mã biến mất khỏi trạng thái còn hiệu lực
- Bắc cầu `Testcase_Template.md` Mục 25: thu hồi mã **trong lúc** người khác đang mở trang → xem B.3
- Số lượng mã tạo ra có giới hạn không → nếu có, kiểm tra biên. Nếu đặc tả không nói, ghi `[NEEDS REVIEW]`

---

<a name="j"></a>
## J. Khi dịch vụ lỗi

> **Điều kiện áp dụng:** mọi hệ thống có link chia sẻ công khai.

- Dịch vụ cấp mã lỗi → người dùng chính nhận thông báo dễ hiểu, luồng chính **không bị chặn**, có cách thay thế
- Dịch vụ đọc dữ liệu cho trang công khai lỗi → trang hiện thông báo hợp lý, tự thử lại hợp lý, không treo
- Hệ thống gốc tạm ngừng → trang công khai xử lý đúng, **không** hiển thị dữ liệu sai hoặc dữ liệu cũ mà không báo
- Mọi thông báo lỗi trên trang công khai đều **không** chứa mã lỗi kỹ thuật, tên dịch vụ nội bộ, hay dấu vết hệ thống

---

## Tự review — Điểm yếu và khuyến nghị

### Điểm mạnh
- Đặt đúng giả định nền tảng ngay từ đầu: mã **sẽ** bị chuyển tiếp. Nhờ đó các case tập trung vào thu hẹp phạm vi dữ liệu và rút ngắn vòng đời, thay vì đuổi theo một mục tiêu không đạt được là "chỉ người được chia sẻ mới xem được"
- Mục C.1 và B.4 chốt đúng chỗ dễ sai nhất: giao diện che nhưng dữ liệu trả về vẫn lộ, giao diện chặn nhưng máy chủ vẫn cho qua
- Mục G bắt được các đường rò rỉ mà kiểm thử theo màn hình bỏ qua hoàn toàn — đặc biệt phần xem trước liên kết trong ứng dụng nhắn tin, nơi dữ liệu lộ ra trước cả khi ai đó mở link

### Điểm yếu — phát hiện khi tự rà soát

| # | Điểm yếu | Mức độ |
|---|---|---|
| 1 | **Phụ thuộc hoàn toàn vào danh sách trường được phép ở C.0** — nếu BA chưa liệt kê danh sách đóng này thì Mục C không kiểm được, mà đây lại là mục quan trọng nhất | Cao |
| 2 | **Chưa có cách kiểm chứng tính ngẫu nhiên thật của mã** — A.1 chỉ kiểm được không trùng và không có quy luật rõ ràng, không kết luận được về chất lượng nguồn ngẫu nhiên. Việc này cần rà soát mã nguồn hoặc kiểm định riêng, ngoài phạm vi kiểm thử hộp đen | Trung bình |
| 3 | **Mục D.1 khó test ở môi trường thử nghiệm** — giới hạn tần suất thường cấu hình khác giữa môi trường thử và môi trường thật, kết quả test có thể không phản ánh hành vi thật | Trung bình |
| 4 | **Chưa cover việc rút ngắn hạn dùng của mã đã phát** — nếu hệ thống cho phép đổi cấu hình hạn dùng, các mã đã phát trước đó chịu ảnh hưởng thế nào | Thấp |
| 5 | **Chưa cover trường hợp cùng một người nhận nhiều mã của nhiều bản ghi khác nhau** — có ghép được thành bức tranh rộng hơn phạm vi cho phép không | Thấp |

### Khuyến nghị
- Điểm #1 xử lý **trước khi gen case**: yêu cầu BA cung cấp danh sách trường được phép ở dạng **danh sách đóng** (cái gì không có trong danh sách là không được phép), không phải danh sách mở
- Điểm #2: đề nghị đội phát triển xác nhận nguồn sinh ngẫu nhiên bằng rà soát mã nguồn, ghi kết quả vào `.note.md` như một bằng chứng kèm theo — kiểm thử hộp đen không thay thế được việc này
- Điểm #3: yêu cầu môi trường thử nghiệm cấu hình **giống môi trường thật** ở phần giới hạn tần suất, hoặc ghi rõ trong kế hoạch test rằng nhóm case này chỉ kết luận được ở môi trường thật
- Điểm #4, #5: ghi `.note.md` để BA/PO xác nhận phạm vi trước khi gen case
