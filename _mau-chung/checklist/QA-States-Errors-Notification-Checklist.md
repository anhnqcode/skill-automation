# Checklist Kiểm thử Trạng thái màn hình, Lỗi & Thông báo
### File tầng 3 — Ma trận trạng thái đặc biệt của mọi màn hình, quy tắc lỗi, và hệ thống thông báo đa kênh

---

## Quan hệ với các file khác

| File | Phạm vi | Quan hệ với file này |
|---|---|---|
| `Testcase_Template.md` | Nền tảng chung | **Kế thừa**, trừ Mục 15 và 18 — xem dưới |
| `Testcase_Template.md` **Mục 15** (xử lý lỗi hệ thống) | 6 gạch đầu dòng về lỗi server | **Bị ghi đè bởi Mục C–D file này.** Mục 15 chỉ kiểm "không crash"; sản phẩm yêu cầu *mọi lỗi kèm nút hành động tiếp theo* cần ma trận đầy đủ |
| `Testcase_Template.md` **Mục 18** (thông báo hệ thống) | Kiểm thông báo có được bắn không | **Bị ghi đè bởi Mục E–G file này.** Mục 18 không cover nội dung, kênh, thời điểm, khử trùng lặp đa kênh |
| `Template_Testcase_Advanced.md` | 7 dạng case rủi ro cao | Bắc cầu Mục A (hàng đợi) và E (webhook) cho phần thông báo bắt nguồn từ sự kiện hệ thống |
| checklist riêng cho thiết bị màn hình gắn tường (không kèm trong gói) | Đặc thù thiết bị | Bắc cầu **Mục C.5** (ngôn ngữ hiển thị lỗi) và **Mục D** (TTS đọc thông báo) |
| `QA-Public-Share-Link-Checklist.md` | Link công khai | Bắc cầu — trang công khai cũng có trạng thái hết hạn / lỗi riêng |
| **File này** | **Mọi trạng thái không phải "luồng thuận": đang tải · rỗng · lỗi · mất mạng · suy giảm dịch vụ · ngoài vùng · bảo trì. Cộng hệ thống thông báo: sự kiện, kênh, người nhận, nội dung, chống trùng** | — |

**Ranh giới rõ ràng:** phần lớn test case của một dự án tập trung vào *"làm đúng thì ra kết quả gì"*. File này lo *"khi chưa có gì, đang chờ, hoặc hỏng thì màn hình trông thế nào và người dùng làm gì tiếp"* — nhóm trạng thái chiếm phần lớn thời gian thực tế người dùng gặp phải nhưng thường được viết case sơ sài nhất.

### Nguyên tắc bao trùm

> **Không màn hình nào được là ngõ cụt.** Mọi trạng thái không phải luồng thuận đều phải trả lời được ba câu: *chuyện gì đang xảy ra · lỗi này có phải do tôi không · tôi làm gì tiếp*. Thiếu câu thứ ba là lỗi, kể cả khi thông báo hiển thị đúng.

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

- [A. Trạng thái đang tải (Loading)](#a)
- [B. Trạng thái rỗng (Empty)](#b)
- [C. Trạng thái lỗi (Error)](#c)
- [D. Mất mạng & Suy giảm dịch vụ nhiều bậc (Degradation & Fallback)](#d)
- [E. Thông báo — sự kiện, kênh, người nhận](#e)
- [F. Thông báo — nội dung và giới hạn kỹ thuật](#f)
- [G. Thông báo — chống trùng và thao tác đa kênh](#g)
- [H. Rà soát bao phủ trạng thái theo màn](#h)

---

<a name="a"></a>
## A. Trạng thái đang tải (Loading)

> **Điều kiện áp dụng:** mọi màn hình có gọi dữ liệu từ server.

### A.0. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo đặc tả) |
|---|---|
| Ngưỡng thời gian bắt đầu hiện chỉ báo chờ? | `[con số — nếu chưa có, tham số hoá]` |
| Ngưỡng thời gian coi là quá lâu, chuyển sang lỗi? | `[con số]` |
| Kiểu chỉ báo: khung xám (skeleton) hay vòng xoay? | `[...]` |

### A.1. Hiển thị chỉ báo chờ

- Màn hình chờ dữ liệu → hiện chỉ báo **đúng kiểu và đúng vị trí** theo thiết kế, không để màn trắng/đen im lặng
- Chỉ báo xuất hiện **đúng ngưỡng thời gian**: quá sớm gây nhấp nháy khó chịu với phản hồi nhanh, quá muộn khiến người dùng tưởng máy treo. Layer **Performance**
- Chỉ báo phản ánh **đúng vùng đang tải**, không phủ toàn màn khi chỉ một thẻ đang tải
- Dữ liệu về → chỉ báo biến mất hoàn toàn, không còn khung xám sót lại

### A.2. Chờ quá lâu

- Vượt ngưỡng chờ tối đa → chuyển sang trạng thái lỗi có nút hành động (Mục C), **không** quay vòng vô hạn
- Trong lúc chờ, các nút hành động liên quan bị vô hiệu hoá đúng cách, tránh bấm lặp tạo yêu cầu trùng. Bắc cầu checklist riêng cho thiết bị màn hình gắn tường (không kèm trong gói) Mục H.1
- Người dùng thoát khỏi màn giữa lúc đang tải → không lỗi, không tiếp tục cập nhật vào màn đã đóng

### A.3. Tải lại và làm mới

- Thao tác làm mới trong lúc đang tải → không chồng hai yêu cầu, không nhân đôi dữ liệu hiển thị
- Tải lại sau khi lỗi → chỉ báo chờ xuất hiện lại đúng, không giữ nguyên thông báo lỗi cũ

---

<a name="b"></a>
## B. Trạng thái rỗng (Empty)

> Trạng thái rỗng thường bị nhầm với trạng thái lỗi hoặc bị bỏ quên hoàn toàn. Với người dùng lần đầu, **trạng thái rỗng chính là màn hình đầu tiên họ nhìn thấy** — nó phải hướng dẫn được, không chỉ thông báo "không có dữ liệu".
>
> **Điều kiện áp dụng:** mọi màn hình hiển thị danh sách hoặc dữ liệu có thể chưa tồn tại.

### B.1. Phân biệt rỗng thật và rỗng do lọc

- **Chưa có dữ liệu nào** (người dùng mới) → nội dung hướng dẫn tạo dữ liệu đầu tiên, kèm **nút dẫn tới hành động tạo**
- **Có dữ liệu nhưng bộ lọc/tìm kiếm không ra kết quả** → nội dung khác hẳn trường hợp trên, kèm nút xoá bộ lọc. Hai trạng thái này **không được dùng chung một màn**
- Không được hiển thị trạng thái rỗng khi thực chất **đang tải** hoặc **đã lỗi** — ba trạng thái phải phân biệt rõ ràng bằng mắt

### B.2. Nội dung theo từng màn

- Mỗi màn có danh sách đều phải có **nội dung rỗng riêng**, phù hợp ngữ cảnh màn đó. Không dùng một câu chung chung cho mọi màn
- Nội dung viết bằng ngôn ngữ đời thường, không dùng thuật ngữ kỹ thuật, không dùng từ mang nghĩa lỗi ("không tìm thấy dữ liệu", "null")
- Với sản phẩm có yêu cầu trợ năng: nội dung rỗng cũng phải đạt ngưỡng cỡ chữ và tương phản, và **được đọc thành tiếng** nếu đặc tả yêu cầu

### B.3. Thoát khỏi trạng thái rỗng

- Tạo dữ liệu đầu tiên từ chính màn rỗng → màn cập nhật ngay sang trạng thái có dữ liệu, không cần tải lại thủ công
- Xoá hết dữ liệu → màn quay lại đúng trạng thái rỗng, không hiển thị danh sách trống không có hướng dẫn

---

<a name="c"></a>
## C. Trạng thái lỗi (Error)

> **Điều kiện áp dụng:** mọi màn hình có gọi dữ liệu hoặc thực hiện thao tác.

### C.0. Bảng chuyển đổi lỗi — điền theo đặc tả

> ⚠ Bảng này là **hợp đồng giữa dev và thiết kế**, và cũng là **nguồn sinh case**: mỗi dòng là một test case ép lỗi. Nếu đặc tả chưa có bảng này, đây là thiếu sót nghiêm trọng — ghi `[NEEDS REVIEW]` và yêu cầu BA lập trước khi viết case.

| Nguyên nhân kỹ thuật | Câu hiển thị cho người dùng | Nút hành động | TC ID |
|---|---|---|---|
| `[lỗi server]` | `[câu tiếng Việt]` | `[nút gì]` | |
| `[timeout dịch vụ ngoài]` | | | |
| `[lỗi lấy giá / lấy dữ liệu chính]` | | | |
| `[lỗi thực hiện giao dịch]` | | | |
| `[phiên hết hạn]` | | | |
| `[lỗi không xác định]` | | | |

### C.1. Không bao giờ là ngõ cụt

- **Mọi màn lỗi** có ít nhất một nút hành động. Rà soát từng dòng bảng C.0, ép lỗi tương ứng, xác nhận có nút. Đây là nhóm case bắt buộc, ưu tiên **P0** nếu người dùng là nhóm yếu thế
- Với lỗi nghiêm trọng: có đường **tới người thật** (nút gọi tổng đài/hỗ trợ), không chỉ nút thử lại
- Bấm nút hành động trên màn lỗi → thực sự dẫn tới đâu đó, không quay lại chính màn lỗi đó

### C.2. Ngôn ngữ thông báo lỗi

- **Không hiển thị mã lỗi kỹ thuật** dưới mọi hình thức: mã HTTP, tên endpoint, tên trường, vết ngăn xếp, chuỗi tiếng Anh. Rà soát bằng cách ép lỗi ở **mọi** điểm gọi dịch vụ
- Câu thông báo **nhận trách nhiệm về phía hệ thống**, không quy lỗi cho người dùng. Không dùng "Bạn đã thao tác sai" khi lỗi là của hệ thống
- Nêu **nguyên nhân bằng ngôn ngữ đời thường**, không dịch sát thuật ngữ kỹ thuật
- Biểu tượng đi kèm **trung tính**, tránh biểu tượng cảnh báo gay gắt nếu người dùng là người cao tuổi — họ dễ tưởng mình làm hỏng thiết bị
- Lỗi vẫn phải được **ghi log đầy đủ ở server** (nguyên nhân thật, mã lỗi, vết truy) — kiểm tra log có, đồng thời kiểm tra client **không** nhận được thông tin đó. Layer **API**

### C.3. Thử lại

- Lỗi mạng thoáng qua → hệ thống **tự thử lại ngầm** theo số lần quy định; nếu thành công, người dùng không thấy màn lỗi nào. Layer **API**
- Thử lại thủ công thành công → về đúng trạng thái bình thường, không còn dấu vết lỗi
- Thử lại thất bại **nhiều lần liên tiếp** → thông báo đổi nội dung, nút chính đổi thành đường tới hỗ trợ. Không để người dùng bấm thử lại vô hạn
- Nút thử lại bị bấm dồn dập → không tạo nhiều yêu cầu song song

### C.4. Phân loại trạng thái lỗi

- Lỗi **thử lại được** và lỗi **không thử lại được** hiển thị khác nhau: loại thứ hai phải ẩn nút thử lại, tránh cho người dùng hy vọng vô ích
- Lỗi thuộc về **dữ liệu đầu vào của người dùng** hiển thị tại chỗ (cạnh trường lỗi), không dùng màn lỗi toàn trang
- Lỗi có màn xử lý **chuyên biệt** (ví dụ báo giá hết hạn có màn riêng) → **không** rơi vào màn lỗi chung. Đây là case dễ sai: hệ thống bắt lỗi chung nuốt mất luồng chuyên biệt

### C.5. Lỗi ở thời điểm nhạy cảm

- Lỗi xảy ra **giữa lúc đang thực hiện giao dịch** → trạng thái dữ liệu rõ ràng, người dùng biết giao dịch đã thành công hay chưa. Không để trạng thái lửng
- Lỗi xảy ra **sau khi đã trừ tiền / đã tạo bản ghi** → thông báo phản ánh đúng thực tế, không báo thất bại khi thực chất đã thành công

---

<a name="d"></a>
## D. Mất mạng & Suy giảm dịch vụ nhiều bậc

> Nhóm này khác Mục C ở chỗ: lỗi ở đây **không dừng hẳn sản phẩm**, mà làm nó chạy ở mức thấp hơn. Thiết kế tốt có nhiều bậc thoái lui; kiểm thử phải đi hết từng bậc, kể cả bậc thấp nhất.
>
> **Điều kiện áp dụng:** sản phẩm có phụ thuộc bên ngoài có thể suy giảm (bản đồ, giọng nói, thông báo, dữ liệu thời gian thực).

### D.0. Bảng bậc thoái lui — điền theo đặc tả

| Dịch vụ | Bậc 1 (đầy đủ) | Bậc 2 | Bậc 3 | Bậc thấp nhất | Điều kiện rơi bậc |
|---|---|---|---|---|---|
| `[bản đồ]` | | | | | |
| `[giọng nói]` | | | | | |
| `[thông báo]` | | | | | |

> ⚠ **Bậc thấp nhất là bậc quan trọng nhất phải test.** Nếu sản phẩm chỉ dùng được khi mọi dịch vụ đều khoẻ thì thiết kế đã sai — và chính bậc thấp nhất là thứ chạy trong ngày đầu triển khai khi hạ tầng chưa sẵn sàng.

### D.1. Mất mạng

- Mất mạng hoàn toàn → hiển thị đúng trạng thái, **không** hiển thị dữ liệu cũ như thể vẫn đang cập nhật
- Mất mạng **một phần** (có sóng nhưng không ra được Internet) → phát hiện đúng, báo đúng. Bắc cầu checklist riêng cho thiết bị màn hình gắn tường (không kèm trong gói) Mục I.3
- Có mạng trở lại → tự đồng bộ về dữ liệu mới nhất, chỉ báo mất mạng biến mất, **không** yêu cầu người dùng tự tải lại
- Mạng chập chờn liên tục → không hiện chồng nhiều thông báo lỗi, không tạo yêu cầu trùng

### D.2. Đi hết từng bậc thoái lui

- Với mỗi dịch vụ ở bảng D.0: ép dịch vụ đó hỏng, xác nhận sản phẩm rơi xuống **đúng bậc kế tiếp**, không rơi thẳng xuống đáy, không đứng im
- Ở **mỗi bậc**, luồng nghiệp vụ chính vẫn hoàn thành được nếu đặc tả nói vậy. Đây là case nghiệm thu quan trọng: chạy trọn luồng chính ở bậc thấp nhất
- Dịch vụ hồi phục → nâng bậc trở lại đúng, không kẹt ở bậc thấp cho tới khi khởi động lại
- Nhiều dịch vụ hỏng **đồng thời** → xử lý đúng, không hiện chồng nhiều thông báo cùng lúc gây rối

### D.3. Suy giảm kênh thời gian thực

- Mất kênh đẩy dữ liệu → chuyển sang hỏi lại định kỳ, **không mất theo dõi**. Bắc cầu `Template_Testcase_Advanced.md` Mục A
- Đang ở chế độ hỏi lại định kỳ → có chỉ báo cho người dùng biết dữ liệu có thể chậm hơn bình thường
- Kênh đẩy trở lại → không nhân đôi dữ liệu do vừa đẩy vừa hỏi lại

### D.4. Bảo trì và dịch vụ tạm ngừng

- Hệ thống vào chế độ bảo trì → thông báo rõ ràng, nêu thời điểm dự kiến trở lại nếu có, kèm đường tới hỗ trợ
- Bảo trì **một phần** (chỉ một chức năng) → các chức năng khác vẫn dùng được bình thường, không khoá toàn bộ sản phẩm
- Đang thao tác dở thì hệ thống vào bảo trì → dữ liệu đang nhập được xử lý đúng theo thiết kế, người dùng được báo trước khi mất

---

<a name="e"></a>
## E. Thông báo — sự kiện, kênh, người nhận

> **Điều kiện áp dụng:** sản phẩm có gửi thông báo cho người dùng qua một hoặc nhiều kênh.

### E.0. Ma trận sự kiện → kênh → người nhận

> ⚠ Đây là **nguồn chân lý** và cũng là **nguồn sinh case**: mỗi ô ✅ trong ma trận là ít nhất một test case. Nếu đặc tả chưa có ma trận này, yêu cầu BA lập trước — không thể viết case thông báo mà không biết ai nhận cái gì ở đâu.

| # | Sự kiện | Người nhận | Kênh 1 | Kênh 2 | Kênh 3 | Mẫu nội dung | Ưu tiên |
|---|---|---|:---:|:---:|:---:|---|---|
| 1 | `[sự kiện]` | `[ai]` | ✅ | ✅ | — | `[mã mẫu]` | P0 |

**Bảng khả dụng của từng kênh:**

| Kênh | Phụ thuộc bên ngoài | Chạy được ngay không? |
|---|---|---|
| `[kênh 1]` | `[không / dịch vụ nào]` | `[có/không]` |

### E.1. Bắn đúng sự kiện

- Mỗi dòng trong ma trận E.0: kích hoạt sự kiện tương ứng, xác nhận thông báo được tạo với **đúng người nhận, đúng kênh, đúng mẫu**. Layer **API**
- Sự kiện xảy ra nhưng **điều kiện gửi không thoả** (người nhận đã tắt kênh đó, kênh chưa khả dụng) → không gửi, và **không lỗi**
- Sự kiện **không có trong ma trận** → không sinh thông báo nào. Kiểm tra hệ thống không tự bắn tin ngoài danh sách

### E.2. Đúng người nhận

- Thông báo tới **đúng người theo ma trận**, không gửi nhầm sang người khác. Đây là case bảo mật, ưu tiên **P0**. Layer **API**
- Người dùng đang **trực tiếp nhìn thấy sự kiện trên màn hình** thì không nhận thêm tin cho cùng sự kiện đó, nếu đặc tả quy định vậy
- Người nhận ngoài hệ thống (không có tài khoản) chỉ nhận đúng phần nội dung được phép. Bắc cầu `QA-Public-Share-Link-Checklist.md` Mục C

### E.3. Kênh chưa khả dụng

- Kênh phụ thuộc dịch vụ ngoài **chưa sẵn sàng** → hệ thống vẫn hoạt động đầy đủ bằng các kênh còn lại. Chạy trọn luồng nghiệp vụ với **chỉ các kênh nền tảng** bật
- Kênh lỗi giữa chừng → không chặn các kênh khác, ghi nhận thất bại để giám sát
- Kênh khả dụng trở lại → hoạt động bình thường; xác định rõ tin trong thời gian gián đoạn có được gửi bù hay không, theo đặc tả

### E.4. Thời điểm gửi

- Thông báo gửi **đúng thời điểm** so với sự kiện, độ trễ trong ngưỡng đặc tả. Layer **Performance**
- Thông báo cho sự kiện cần hành động gấp (ví dụ có cửa sổ thời gian để huỷ) phải tới **trước khi cửa sổ đó đóng**, nếu không thì vô nghĩa. Case này thường bị bỏ qua
- Sự kiện xảy ra lúc đêm khuya hoặc ngoài giờ → xử lý theo đặc tả, không tự ý gửi nếu đặc tả có quy định giờ im lặng

---

<a name="f"></a>
## F. Thông báo — nội dung và giới hạn kỹ thuật

> **Điều kiện áp dụng:** có mẫu nội dung thông báo được đặc tả.

- Nội dung gửi đi **khớp chính xác mẫu** trong đặc tả, các giá trị thay thế điền đúng (tên, địa điểm, thời gian, số tiền)
- Giá trị thay thế **dài bất thường** (tên địa điểm rất dài) → nội dung không vượt giới hạn ký tự của kênh, cắt gọn đúng quy tắc, không cắt giữa thông tin quan trọng
- Giá trị thay thế **rỗng hoặc thiếu** → có giá trị dự phòng hợp lý, không gửi đi câu có chỗ trống hoặc còn nguyên biến
- Định dạng **số tiền, ngày giờ, số điện thoại** đúng chuẩn Việt Nam trong mọi kênh
- Nội dung tuân thủ quy tắc **che dữ liệu nhạy cảm** giống trên giao diện — không được lộ qua kênh thông báo cái đã che trên màn hình. Bắc cầu checklist riêng cho thiết bị màn hình gắn tường (không kèm trong gói) Mục F.1
- Thông báo có nút/liên kết hành động → liên kết đúng đích, còn hiệu lực khi người dùng bấm, và xử lý đúng khi đã hết hiệu lực
- Nội dung không chứa mã lỗi kỹ thuật hay thuật ngữ tiếng Anh, giống quy tắc Mục C.2
- Với kênh có **quy trình đăng ký mẫu trước** (mẫu tin phải duyệt, tên miền khoá cố định lúc đăng ký): xác nhận nội dung và tên miền thực tế **khớp với mẫu đã đăng ký**, vì lệch là tin không gửi được

---

<a name="g"></a>
## G. Thông báo — chống trùng và thao tác đa kênh

> Nhóm dễ sinh lỗi nhất của hệ thống thông báo, và cũng dễ bị bỏ qua nhất vì chỉ lộ ra khi có sự kiện lặp hoặc người dùng thao tác ở nhiều nơi.
>
> **Điều kiện áp dụng:** thông báo bắt nguồn từ sự kiện hệ thống, hoặc gửi qua nhiều kênh cùng lúc.

### G.1. Một sự kiện, một tin

- Sự kiện nguồn gửi **trùng lặp** (webhook lặp, thử lại) → chỉ sinh **một** thông báo cho mỗi kênh. Bắc cầu `Template_Testcase_Advanced.md` Mục E.2. Layer **API**
- Sự kiện đến **sai thứ tự** → không gửi tin cho trạng thái đã lỗi thời (không báo "xe đang đến" sau khi đã báo "đã tới nơi")
- Nhiều sự kiện dồn dập trong thời gian ngắn → tuân thủ giới hạn số tin theo đặc tả, không dội tin
- Với sản phẩm có đọc thành tiếng: chống trùng ở tầng thông báo phải nhất quán với chống trùng ở tầng đọc. Bắc cầu checklist riêng cho thiết bị màn hình gắn tường (không kèm trong gói) Mục D.2

### G.2. Thao tác chỉ hiệu lực một lần

- Cùng một việc cần xử lý được gửi qua **nhiều kênh** → người dùng xử lý ở kênh này, các kênh còn lại chuyển sang trạng thái **đã xử lý**, không cho làm lại. Layer **API**
- Hai kênh được thao tác **gần như đồng thời** → chỉ một lần có hiệu lực, kênh còn lại nhận phản hồi rõ ràng chứ không phải lỗi kỹ thuật
- Thao tác qua kênh sau khi việc đã **hết hạn** → thông báo rõ ràng, không thực hiện

### G.3. Cấu hình của người nhận

- Người dùng tắt một kênh → không nhận qua kênh đó nữa, vẫn nhận qua các kênh bắt buộc không tắt được
- Người dùng tắt **tất cả** kênh tuỳ chọn → các thông báo bắt buộc theo đặc tả vẫn tới được
- Đổi cấu hình giữa lúc một sự kiện đang được xử lý → hành vi rõ ràng, không gửi nửa vời

---

<a name="h"></a>
## H. Rà soát bao phủ trạng thái theo màn

> Mục này **không có case riêng**. Đây là bảng rà soát bắt buộc chạy **trước khi kết thúc việc viết case** cho mỗi màn hình, để phát hiện trạng thái bị bỏ quên.

### H.1. Sáu câu hỏi cho từng màn hình

| # | Câu hỏi | Nếu chưa có case |
|---|---|---|
| 1 | Màn này lúc **đang tải** trông thế nào? | Sinh case theo Mục A |
| 2 | Màn này khi **chưa có dữ liệu** trông thế nào? | Sinh case theo Mục B (phân biệt rỗng thật và rỗng do lọc) |
| 3 | Màn này khi **dịch vụ lỗi** trông thế nào? | Sinh case theo Mục C, đủ từng dòng bảng C.0 |
| 4 | Màn này khi **mất mạng** trông thế nào? | Sinh case theo Mục D.1 |
| 5 | Màn này phụ thuộc **dịch vụ ngoài** nào? Dịch vụ đó hỏng thì sao? | Sinh case theo Mục D.2, đi hết từng bậc |
| 6 | Thao tác trên màn này có **sinh thông báo** không? | Sinh case theo Mục E–G |

### H.2. Bảng rà nhanh — điền cho toàn bộ dự án

Lập một lần cho cả dự án, đánh dấu màn nào cần biến thể nào. Ô trống là chỗ cần rà lại, không phải chỗ không cần.

| Màn hình | Đang tải | Rỗng | Lỗi | Mất mạng | Dịch vụ ngoài hỏng | Sinh thông báo |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| `[tên màn]` | | | | | | |

> Cột **"Dịch vụ ngoài hỏng"** là cột dễ bỏ sót nhất và rủi ro cao nhất, đặc biệt khi hạ tầng phụ thuộc chưa được cấp phát ở giai đoạn đầu dự án.

---

## Tự review — Điểm yếu và khuyến nghị

### Điểm mạnh
- Mục C.0 và E.0 biến hai bảng đặc tả thành **nguồn sinh case đếm được**: mỗi dòng bảng là một case, nên bao phủ kiểm chứng được thay vì dựa vào trí nhớ người viết
- Mục D tách bạch "hỏng hẳn" và "chạy ở mức thấp hơn" — nhóm thứ hai chiếm phần lớn sự cố thực tế nhưng thường không có case nào
- Mục H buộc rà soát trạng thái theo từng màn trước khi đóng việc, thay vì phát hiện thiếu sót lúc kiểm thử chấp nhận
- Mục G.2 (thao tác đa kênh chỉ hiệu lực một lần) bắt được lớp lỗi chỉ xuất hiện khi hệ thống có nhiều kênh — không file nào khác trong bộ cover

### Điểm yếu — phát hiện khi tự rà soát

| # | Điểm yếu | Mức độ |
|---|---|---|
| 1 | **Toàn bộ Mục C và E phụ thuộc hai bảng đặc tả mà nhiều dự án không có** — nếu BA chưa lập bảng chuyển đổi lỗi và ma trận thông báo thì checklist chỉ nêu được yêu cầu, không sinh được case | Cao |
| 2 | **Ép lỗi từng dòng bảng C.0 cần công cụ giả lập ở tầng dịch vụ** — nếu không có, nhiều case trở thành không chạy được và sẽ bị bỏ qua trong thực tế | Cao |
| 3 | **Chưa cover thông báo trên nhiều thiết bị của cùng một người** — một người có điện thoại và máy tính bảng, mở cả hai, đọc ở một nơi thì nơi kia xử lý ra sao | Trung bình |
| 4 | **Chưa cover việc thay đổi mẫu nội dung khi đã có tin đang chờ gửi** — tin trong hàng đợi dùng mẫu cũ hay mẫu mới | Thấp |
| 5 | **Mục D.2 yêu cầu ép hỏng từng dịch vụ ngoài** — trong môi trường thử nghiệm dùng chung, việc này ảnh hưởng người khác đang test, cần môi trường riêng | Trung bình |

### Khuyến nghị
- Điểm #1 xử lý **trước khi gen case**: yêu cầu BA lập bảng C.0 và E.0. Đây là hai bảng mà đội phát triển cũng cần, nên đề nghị này hợp lý với cả hai phía
- Điểm #2: đề nghị bổ sung công cụ giả lập lỗi ở tầng dịch vụ trung gian ngay từ đầu dự án. Không có nó, nhóm case lỗi chỉ tồn tại trên giấy
- Điểm #5: xin môi trường riêng cho nhóm case suy giảm dịch vụ, hoặc bố trí chạy vào khung giờ không ảnh hưởng người khác — ghi rõ trong kế hoạch test
- Điểm #3, #4: ghi `.note.md` để BA/PO xác nhận phạm vi trước khi gen case
