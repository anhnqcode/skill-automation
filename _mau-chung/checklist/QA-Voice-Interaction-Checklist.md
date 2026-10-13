# Checklist Kiểm thử Tương tác bằng Giọng nói
### File tầng 3 — Áp dụng cho mọi sản phẩm có nhận lệnh bằng giọng nói (ASR / NLU / Intent)

---

## Quan hệ với các file khác

| File | Phạm vi | Quan hệ với file này |
|---|---|---|
| `Testcase_Template.md` | Nền tảng chung | **Kế thừa toàn bộ.** Đặc biệt Mục 25 (State Transition) — xem Mục E file này |
| `Template_Testcase_Advanced.md` | 7 dạng case rủi ro cao domain đặt xe | Bắc cầu khi lệnh giọng nói kích hoạt giao dịch nhiều bước |
| `QA-TV-App-Checklist.md` | App màn hình lớn | **Thay thế Mục B.2** của file đó (giọng nói ở đó chỉ có 2 gạch đầu dòng) |
| checklist riêng cho thiết bị màn hình gắn tường (không kèm trong gói) | Đặc thù thiết bị SmartScreen | Bắc cầu **Mục D (TTS)** — file đó lo phần **đọc ra**, file này lo phần **nghe vào** |
| `QA-Mobile-Native-Checklist.md` | App mobile | Bắc cầu Mục C (quyền micro) nếu chạy trên mobile |
| **File này** | **Nghe vào: nhận dạng, hiểu ý định, trích thông tin, xác nhận, thoái lui khi không chắc** | — |

**Ranh giới rõ ràng:** file này **không** kiểm thử chất lượng mô hình ASR/NLU của nhà cung cấp. Nó kiểm thử **cách sản phẩm hành xử** khi nhận dạng đúng, khi nhận dạng sai, và khi không chắc chắn — đặc biệt ở các lệnh có hậu quả không đảo ngược được.

### Nguyên tắc bao trùm

> ⛔ **Giọng nói không bao giờ được trực tiếp thực hiện hành động có hậu quả.** Mọi lệnh dẫn tới tiêu tiền, huỷ bỏ, xoá dữ liệu, hoặc gửi thông tin ra ngoài đều phải qua **một bước xác nhận tường minh**. Nhận dạng giọng nói luôn có xác suất sai — thiết kế phải giả định nó sẽ sai.
>
> Hệ quả kiểm thử: **mọi intent có hậu quả đều cần ít nhất một case chứng minh nó dừng lại chờ xác nhận**, và một case chứng minh nó **không** thực hiện khi người dùng không xác nhận.

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

- [A. Nhận diện ý định (Intent Recognition)](#a)
- [B. Trích xuất thông tin trong câu (Slot Filling)](#b)
- [C. Độ tin cậy thấp & Thoái lui (Confidence & Fallback)](#c)
- [D. Xác nhận trước hành động có hậu quả](#d)
- [E. Lệnh vượt rào trạng thái & phạm vi cho phép](#e)
- [F. Môi trường âm thanh thực tế](#f)
- [G. Ngắt lời & phối hợp với phần đọc thành tiếng](#g)
- [H. Kết quả mập mờ & nhiều lựa chọn](#h)
- [I. Quyền riêng tư và bảo mật giọng nói](#i)
- [J. Khi dịch vụ giọng nói không khả dụng](#j)

---

<a name="a"></a>
## A. Nhận diện ý định (Intent Recognition)

> **Điều kiện áp dụng:** mọi sản phẩm có nhận lệnh bằng giọng nói.

### A.0. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo hệ thống thật) |
|---|---|
| Danh sách đầy đủ các intent được hỗ trợ? | `[liệt kê hết — đây là danh sách gốc để sinh case]` |
| Intent nào có hậu quả không đảo ngược được? | `[danh sách — nhóm này bắt buộc có Mục D]` |
| Ngưỡng độ tin cậy để chấp nhận là bao nhiêu? | `[con số — nếu chưa có, ghi NEEDS REVIEW]` |
| Có từ khoá đánh thức hay phải bấm nút mic? | `[...]` |
| Ngôn ngữ và phương ngữ hỗ trợ? | `[...]` |

> ⚠ **Mỗi intent trong danh sách trên phải có tối thiểu 3 case:** một câu mẫu chuẩn, một câu diễn đạt khác cùng ý, và một câu gần giống nhưng thuộc intent khác (để kiểm tra không nhận nhầm).

### A.1. Nhận đúng intent

- Mỗi intent nhận đúng với **câu mẫu chuẩn** trong đặc tả
- Mỗi intent nhận đúng với **ít nhất 3 cách diễn đạt khác nhau** cùng một ý — người thật không nói y hệt câu mẫu
- Câu nói **có từ đệm, ngập ngừng, lặp từ** ("ờ, cho tôi… gọi xe đi bệnh viện nhé") → vẫn nhận đúng intent
- Câu nói **rút gọn tối đa** ("đi bệnh viện") → nhận đúng, hoặc hỏi lại rõ ràng, không đoán bừa sang intent khác

### A.2. Không nhận nhầm

- Hai intent **gần nghĩa nhau** → phân biệt đúng. Đây là nhóm case quan trọng nhất về độ chính xác, đặc biệt khi một trong hai có hậu quả (ví dụ cặp "kiểm tra" và "huỷ")
- Câu nói **hoàn toàn ngoài phạm vi** ("hôm nay trời đẹp nhỉ") → hệ thống trả lời không hiểu, gợi ý những gì làm được, **không** kích hoạt intent nào
- Câu nói **rỗng** hoặc chỉ có tiếng ồn → xử lý đúng, mời nói lại, không kích hoạt gì
- Người dùng nói **hai lệnh trong một câu** → xử lý theo thiết kế (chọn lệnh đầu, hoặc hỏi lại), không thực hiện cả hai một cách âm thầm

### A.3. Kích hoạt và kết thúc phiên nghe

- Kích hoạt đúng cách (bấm nút mic hoặc từ khoá đánh thức), có chỉ báo **nhìn thấy được** đang nghe
- Kích hoạt nhầm khi không có ai nói → tự kết thúc sau khoảng thời gian hợp lý, không nghe vô hạn
- Người dùng kích hoạt rồi **im lặng** → thoát êm, có thông báo, không treo
- Kích hoạt **lần hai trong lúc đang xử lý lần một** → xử lý đúng theo thiết kế, không chồng hai phiên

---

<a name="b"></a>
## B. Trích xuất thông tin trong câu (Slot Filling)

> Nhận đúng intent chưa đủ — còn phải lấy đúng các thông tin trong câu (địa điểm, tên người, thời gian, số lượng). Sai slot nguy hiểm hơn sai intent, vì hệ thống vẫn chạy đúng luồng nhưng với dữ liệu sai.
>
> **Điều kiện áp dụng:** intent có tham số kèm theo.

### B.1. Trích đúng thông tin

- Trích đúng từng loại slot với câu mẫu chuẩn
- Trích đúng khi thông tin nằm ở **vị trí khác** trong câu ("mai 6 giờ gọi xe đi sân bay" và "gọi xe đi sân bay lúc 6 giờ mai")
- Slot là **tên riêng tiếng Việt có dấu** → trích đúng cả dấu, không mất dấu, không viết sai chính tả dẫn tới tra cứu trượt
- Slot là **thời gian tương đối** ("mai", "chiều nay", "6 giờ rưỡi", "nửa tiếng nữa") → quy đổi đúng sang thời điểm tuyệt đối, đúng múi giờ

### B.2. Thiếu thông tin

- Câu nói **thiếu một slot bắt buộc** → hệ thống hỏi lại **đúng slot còn thiếu**, không hỏi lại từ đầu, không tự điền giá trị mặc định một cách âm thầm
- Người dùng bổ sung slot bằng câu trả lời ngắn ("bệnh viện Bạch Mai") → ghép đúng vào ngữ cảnh trước đó, không coi là lệnh mới
- Hỏi lại **quá số lần quy định** mà vẫn thiếu → thoái lui sang giao diện thao tác tay, không hỏi vòng vô tận

### B.3. Thông tin không hợp lệ

- Slot có giá trị **ngoài phạm vi cho phép** (thời gian trong quá khứ, thời gian vượt giới hạn đặt trước, địa điểm ngoài vùng phục vụ) → báo bằng ngôn ngữ đời thường và đề xuất giá trị hợp lệ, không báo lỗi kỹ thuật
- Slot **mâu thuẫn nội bộ** ("mai hôm qua") → hỏi lại rõ ràng
- Kiểm tra biên của slot thời gian: **đúng bằng** giới hạn nhỏ nhất và lớn nhất cho phép. Layer **API**

### B.4. Giá trị tự do không có trong danh sách sẵn

- Slot là **địa chỉ tự do** không nằm trong danh sách đã lưu → hệ thống tra cứu được, đọc lại to cho người dùng xác nhận **trước khi** dùng
- Địa chỉ tra cứu **không tìm thấy** → thông báo rõ, đề xuất cách khác (chọn từ danh sách đã lưu, nhập tay), không im lặng bỏ qua
- Địa chỉ tra cứu ra **nhiều kết quả** → xem Mục H

---

<a name="c"></a>
## C. Độ tin cậy thấp & Thoái lui (Confidence & Fallback)

> Nhóm quan trọng nhất về an toàn. Nguyên tắc: **khi không chắc chắn thì hỏi hoặc chuyển sang thao tác tay, tuyệt đối không đoán.** Đoán sai trong lệnh có hậu quả là mất tiền của người dùng.
>
> **Điều kiện áp dụng:** mọi sản phẩm có nhận lệnh bằng giọng nói.

### C.1. Dưới ngưỡng tin cậy

- Kết quả nhận dạng có **độ tin cậy dưới ngưỡng** → hệ thống **không thực hiện**, chuyển sang hỏi lại hoặc sang giao diện thao tác tay. Ép giá trị độ tin cậy để test, layer **API**
- Kết quả **đúng bằng ngưỡng** → xác định rõ thuộc nhánh nào, hành vi nhất quán
- Độ tin cậy cao nhưng nội dung nhận được **vô nghĩa** → vẫn phải xử lý an toàn, không kích hoạt intent bừa

### C.2. Thoái lui nhiều bậc

- Lần thất bại **thứ nhất** → mời nói lại, có gợi ý cách nói đúng
- Lần thất bại **thứ hai** → chuyển sang giao diện thao tác tay, **điền sẵn phần đã nghe được** để người dùng không phải làm lại từ đầu
- Chuyển sang giao diện tay → focus đặt đúng chỗ cần thao tác tiếp, người dùng không phải tìm
- Người dùng **bỏ giữa chừng** ở bất kỳ bậc nào → thoát sạch, không để lại trạng thái dở dang

### C.3. Không được đoán

- Với intent có hậu quả, khi nhận dạng không chắc chắn → hệ thống **không** chọn phương án gần đúng nhất rồi thực hiện. Đây là case bảo mật/an toàn, xếp **P0**
- Khi có nhiều khả năng → đưa ra lựa chọn cho người dùng (Mục H), không tự chọn hộ

---

<a name="d"></a>
## D. Xác nhận trước hành động có hậu quả

> Hiện thực hoá nguyên tắc bao trùm ở đầu file. **Mọi intent trong danh sách "có hậu quả" ở Mục A.0 đều bắt buộc có đủ nhóm case này.**
>
> **Điều kiện áp dụng:** có intent dẫn tới tiêu tiền, huỷ bỏ, xoá dữ liệu, hoặc gửi thông tin ra ngoài.

### D.1. Dừng lại chờ xác nhận

- Ra lệnh bằng giọng nói → hệ thống chạy tới bước **hiển thị và đọc to thông tin quyết định** (giá tiền, điểm đến, thời gian) rồi **dừng lại**. Kiểm chứng ở tầng dữ liệu rằng **chưa có** bản ghi nào được tạo. Layer **API**
- Thông tin đọc to **khớp chính xác** với thông tin hiển thị trên màn hình và với thông tin sẽ được thực thi — không được lệch nhau ở bất kỳ giá trị nào
- Chỉ khi nhận được **xác nhận tường minh** (bằng lời hoặc bằng thao tác tay) thì hành động mới được thực hiện

### D.2. Từ chối và bỏ dở

- Người dùng nói **từ chối** → không thực hiện, quay về trạng thái trước đó sạch sẽ, có phản hồi cho người dùng biết đã huỷ
- Người dùng **im lặng không trả lời** ở bước xác nhận → không tự động thực hiện sau khi hết thời gian chờ. Mặc định an toàn là **không làm gì**
- Người dùng **nói một điều khác** không phải xác nhận cũng không phải từ chối → hỏi lại, không suy diễn thành đồng ý

### D.3. Xác nhận lai giữa hai kênh

- Ra lệnh bằng giọng nói, xác nhận bằng **thao tác tay** → hoạt động đúng
- Ra lệnh bằng thao tác tay, xác nhận bằng **giọng nói** → hoạt động đúng
- Từ chối bằng kênh này sau khi đã ra lệnh bằng kênh kia → huỷ đúng

### D.4. Không tạo trùng qua kênh giọng nói

- Nói lệnh xác nhận **nhiều lần liên tiếp** → chỉ thực hiện một lần. Bắc cầu checklist riêng cho thiết bị màn hình gắn tường (không kèm trong gói) Mục H.1
- Nói xác nhận **đồng thời** với việc bấm nút xác nhận trên màn hình → chỉ một hành động được thực hiện

---

<a name="e"></a>
## E. Lệnh vượt rào trạng thái & phạm vi cho phép

> ⚠ **Nhóm case dễ bị bỏ sót nhất, và là lỗ hổng bảo mật thật sự.** Giao diện thường ẩn/vô hiệu hoá nút khi hành động không còn hợp lệ — nhưng kênh giọng nói **đi vòng qua giao diện**. Nếu chốt chặn chỉ nằm ở lớp hiển thị, lệnh nói sẽ xuyên thủng.
>
> **Điều kiện áp dụng:** có hành động bị giới hạn theo trạng thái, theo thời điểm, hoặc theo điều kiện nghiệp vụ.

### E.1. Hành động đã bị vô hiệu trên giao diện

- Đưa bản ghi về trạng thái mà hành động X **không còn được phép** → xác nhận nút X đã ẩn/vô hiệu trên giao diện → **ra lệnh X bằng giọng nói** → hệ thống **từ chối**, và từ chối ở **tầng server**, không chỉ ở tầng ứng dụng. Layer **API**, ưu tiên **P0**
- Lặp lại cho **từng cặp (hành động, trạng thái cấm)** trong đặc tả — đây là ma trận, không phải một case
- Thông báo từ chối dùng ngôn ngữ đời thường, giải thích **vì sao** không làm được, kèm hành động thay thế

### E.2. Trạng thái đổi giữa lúc đang hội thoại

- Bắt đầu ra lệnh khi hành động **còn hợp lệ**, trạng thái đổi thành **không hợp lệ** trong lúc đang chờ xác nhận → tại thời điểm xác nhận, hệ thống kiểm tra lại và từ chối đúng. Bắc cầu `Testcase_Template.md` Mục 25
- Ngược lại: bắt đầu khi **chưa hợp lệ**, trở thành hợp lệ giữa chừng → hành vi rõ ràng, không kẹt

### E.3. Phạm vi dữ liệu

- Lệnh giọng nói **không** truy cập được dữ liệu ngoài phạm vi cho phép của phiên hiện tại. Thử ra lệnh tham chiếu tới bản ghi không thuộc phạm vi → từ chối ở server. Layer **Security**
- Lệnh tham chiếu tới bản ghi **không tồn tại** → thông báo rõ ràng, không lộ thông tin về sự tồn tại của dữ liệu người khác

---

<a name="f"></a>
## F. Môi trường âm thanh thực tế

> Phòng thử nghiệm yên tĩnh không phản ánh nơi sản phẩm được dùng thật. Nhóm này là `Manual only`.
>
> **Điều kiện áp dụng:** mọi sản phẩm có nhận lệnh bằng giọng nói.

### F.0. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời |
|---|---|
| Khoảng cách nói dự kiến tới micro? | `[...]` |
| Môi trường sử dụng điển hình? | `[phòng khách có TV, ngoài trời, xe hơi...]` |
| Nhóm giọng nói mục tiêu? | `[độ tuổi, vùng miền]` |

### F.1. Tiếng ồn nền

- Có **tiếng TV hoặc loa đang phát** trong phòng → nhận dạng vẫn hoạt động ở mức chấp nhận được, hoặc thoái lui đúng khi không nghe rõ. Đây là môi trường mặc định của thiết bị đặt phòng khách
- Có **nhiều người nói chuyện** cùng lúc → không nhận nhầm lời của người khác thành lệnh
- Tiếng ồn đột ngột giữa lúc đang nói → xử lý êm, cho phép nói lại

### F.2. Đặc điểm giọng nói người dùng

- Giọng **người cao tuổi**: nói chậm, ngắt quãng, âm lượng nhỏ, phát âm không rõ → nhận dạng ở mức chấp nhận được hoặc thoái lui đúng. Nếu người dùng chính là nhóm này thì đây là case **P0**, không phải case biên
- Giọng theo **vùng miền khác nhau** → kiểm tra với ít nhất 3 vùng phương ngữ chính
- Nói **quá nhanh** hoặc **quá to** → xử lý đúng, không cắt cụt câu

### F.3. Khoảng cách và vị trí

- Nói ở khoảng cách **xa hơn dự kiến** → hoặc nhận được, hoặc báo rõ không nghe thấy, không im lặng
- Nói khi **quay lưng** hoặc đứng lệch so với micro → hành vi hợp lý
- Nói **quá sát** micro gây méo tiếng → vẫn xử lý được hoặc báo rõ

---

<a name="g"></a>
## G. Ngắt lời & phối hợp với phần đọc thành tiếng

> Bắc cầu với checklist riêng cho thiết bị màn hình gắn tường (không kèm trong gói) Mục D. File đó lo **đọc ra**, file này lo tình huống **nghe vào trong lúc đang đọc ra**.
>
> **Điều kiện áp dụng:** sản phẩm vừa đọc thành tiếng vừa nhận lệnh bằng giọng nói.

### G.1. Ngắt lời khi đang đọc

- Người dùng ra lệnh **trong lúc hệ thống đang đọc** → nếu có hỗ trợ ngắt lời: dừng đọc ngay và xử lý lệnh mới. Nếu không hỗ trợ: bỏ qua và có chỉ báo, không xử lý nửa vời
- Hệ thống **không tự nghe nhầm chính tiếng mình đang đọc** thành lệnh của người dùng — case này rất hay xảy ra với thiết bị có loa và micro gần nhau
- Ngắt lời giữa chừng rồi **không nói gì tiếp** → quay lại trạng thái ổn định, không treo giữa hai luồng

### G.2. Nhịp hội thoại

- Khoảng lặng giữa lúc hệ thống đọc xong và lúc bắt đầu nghe đủ ngắn để hội thoại tự nhiên, đủ dài để người cao tuổi kịp phản ứng
- Người dùng **trả lời trước khi hệ thống đọc xong** → không bị bỏ lỡ câu trả lời

---

<a name="h"></a>
## H. Kết quả mập mờ & nhiều lựa chọn

> **Điều kiện áp dụng:** slot có thể khớp nhiều giá trị (địa điểm trùng tên, nhiều người cùng tên).

- Có **nhiều kết quả khớp** → đọc/hiển thị **không quá số lượng tối đa quy định**, vì người nghe không nhớ được danh sách dài
- Mỗi lựa chọn được đọc kèm **thông tin phân biệt** (quận/huyện, đường), không chỉ đọc tên trùng nhau
- Người dùng chọn bằng **số thứ tự** ("cái thứ hai") và bằng **nội dung** ("cái ở Đống Đa") → cả hai cách đều hoạt động
- Người dùng nói **không cái nào đúng** → mở rộng tìm kiếm hoặc chuyển sang thao tác tay, không lặp lại đúng danh sách cũ
- Kết quả nhiều hơn số lượng tối đa → nêu rõ còn kết quả khác và cách xem thêm, không cắt im lặng

---

<a name="i"></a>
## I. Quyền riêng tư và bảo mật giọng nói

> **Điều kiện áp dụng:** mọi sản phẩm có micro.

- Micro **chỉ hoạt động khi được kích hoạt**, có chỉ báo nhìn thấy được trong toàn bộ thời gian đang nghe. Không có trạng thái nghe ngầm không chỉ báo
- **Không đọc to dữ liệu nhạy cảm** trên thiết bị dùng chung — bắc cầu checklist riêng cho thiết bị màn hình gắn tường (không kèm trong gói) Mục F.1
- Người dùng **không thể nhập mã bí mật bằng giọng nói** (PIN, mật khẩu) — nếu hệ thống cho phép, đây là lỗi thiết kế, ghi `.note.md`
- Dữ liệu âm thanh gửi lên dịch vụ nhận dạng: xác nhận đúng phạm vi được phép theo đặc tả và quy định pháp lý, có thông báo cho người dùng. Layer **Security**
- Từ chối cấp quyền micro (nếu nền tảng có xin quyền) → app vẫn dùng được đầy đủ bằng thao tác tay, có hướng dẫn bật lại. Bắc cầu `QA-Mobile-Native-Checklist.md` Mục C

---

<a name="j"></a>
## J. Khi dịch vụ giọng nói không khả dụng

> **Điều kiện áp dụng:** dịch vụ nhận dạng chạy trên hạ tầng bên ngoài.

- Dịch vụ nhận dạng **lỗi hoặc không phản hồi** → thông báo bằng ngôn ngữ đời thường, chuyển ngay sang thao tác tay, **không** treo màn hình chờ
- Dịch vụ **chậm bất thường** → có ngưỡng chờ tối đa, quá ngưỡng thì thoái lui, không để người dùng chờ vô hạn
- **Mất mạng** giữa lúc đang nói → xử lý êm, giữ lại phần thông tin đã có nếu được, không mất toàn bộ thao tác trước đó
- Mọi chức năng có thể làm bằng giọng nói đều **phải làm được bằng thao tác tay** — giọng nói là đường tắt, không bao giờ là đường duy nhất. Rà soát toàn bộ danh sách intent để chứng minh điều này
- Dịch vụ trả về **lỗi có mã kỹ thuật** → không hiển thị mã đó cho người dùng

---

## Tự review — Điểm yếu và khuyến nghị

### Điểm mạnh
- Mục E bắt được lỗ hổng thật: giao diện ẩn nút nhưng kênh giọng nói đi vòng qua giao diện. Đây là dạng lỗi bảo mật mà kiểm thử theo màn hình không bao giờ phát hiện
- Mục D biến nguyên tắc "giọng nói không tự thực hiện hành động có hậu quả" thành case kiểm chứng được ở tầng dữ liệu, không dừng ở lời khẳng định trong tài liệu
- Tách bạch rõ: file này không đánh giá chất lượng mô hình nhận dạng của nhà cung cấp, mà đánh giá cách sản phẩm hành xử khi mô hình đó sai — đúng phạm vi trách nhiệm của đội QA sản phẩm

### Điểm yếu — phát hiện khi tự rà soát

| # | Điểm yếu | Mức độ |
|---|---|---|
| 1 | **Mục F gần như không automate được và không tái lập chính xác được** — cùng một câu nói, cùng mức ồn, hai lần chạy có thể ra hai kết quả. Kết quả test mang tính thống kê chứ không nhị phân đúng/sai, trong khi bảng test case lại chỉ có ô P/F | Cao |
| 2 | **Chưa có tiêu chí định lượng cho độ chính xác nhận dạng** — bao nhiêu phần trăm câu nói được nhận đúng thì đạt? Không có ngưỡng thì Mục A và F không kết luận được | Cao |
| 3 | **Chưa cover trường hợp nhiều người cùng ra lệnh trên một thiết bị dùng chung** — hệ thống không phân biệt được ai đang nói, nên không biết lệnh có được phép hay không | Trung bình |
| 4 | **Chưa cover việc cập nhật mô hình nhận dạng** — nhà cung cấp nâng cấp mô hình có thể làm thay đổi kết quả của các case đã pass, cần chiến lược hồi quy riêng | Trung bình |
| 5 | **Mục G.1 (hệ thống nghe nhầm tiếng của chính mình)** phụ thuộc phần cứng loa/micro cụ thể, kết quả không chuyển được sang thiết bị khác | Thấp |

### Khuyến nghị
- Điểm #1, #2 xử lý cùng nhau: chuyển nhóm case môi trường âm thanh sang dạng **bộ mẫu có tỉ lệ đạt** — thu sẵn một tập câu nói cố định (nhiều giọng, nhiều mức ồn), chạy qua dịch vụ nhận dạng theo lô, đo tỉ lệ nhận đúng so với ngưỡng chốt trước. Cách này tái lập được và automate được ở layer **API**, khác hẳn việc đứng nói vào máy
- Điểm #2 phải chốt ngưỡng với BA/PO **trước** giai đoạn kiểm thử, ghi `[NEEDS REVIEW]` nếu chưa có
- Điểm #4: giữ lại bộ mẫu ở khuyến nghị trên làm **bộ hồi quy**, chạy lại mỗi khi nhà cung cấp thông báo nâng cấp mô hình
- Điểm #3, #5: ghi `.note.md` để BA/PO xác nhận phạm vi trước khi gen case
