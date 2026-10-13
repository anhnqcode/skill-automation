# Checklist Kiểm thử Danh tính và Liên kết Tài khoản

### File tầng 3. Áp dụng khi hệ thống **quản lý hồ sơ của người thật, đồng bộ hồ sơ đó từ hệ thống nguồn, và gắn hồ sơ với các tài khoản mạng xã hội** để giám sát hoặc đối chiếu

---

## Quan hệ với các file khác

| File | Phạm vi | Quan hệ với file này |
|---|---|---|
| `Testcase_Template.md` | Nền tảng chung | **Kế thừa toàn bộ.** Phần thêm sửa xóa hồ sơ dùng Mục 3, 5, 10 của tầng 0 |
| `Testcase_Template.md` Mục 3 (tính duy nhất) | Trùng bản ghi | **Được mở rộng bởi Mục B.** Trùng hồ sơ người thật khó hơn trùng một mã, vì một người có nhiều cách viết tên và nhiều tài khoản |
| `Testcase_Template.md` Mục 12.3 (đồng bộ hệ thống ngoài) | Đồng bộ hai chiều | **Được mở rộng bởi Mục C.** Hồ sơ đẩy một chiều từ hệ thống nguồn có luật riêng: trường nào là gốc, sửa ở đích thì lần đồng bộ sau có bị ghi đè không |
| `Template_Testcase_Advanced.md` Mục D (giao dịch nhiều bước) | Saga và bù trừ | **Bắc cầu** nếu hồ sơ đi qua nhiều hệ thống trước khi tới đích |
| `QA-Data-Crawling-Checklist.md` Mục I | Tài khoản nguồn đổi trạng thái | **Bắc cầu.** File kia lo tài khoản đổi trạng thái ảnh hưởng việc thu thập, file này lo việc gắn tài khoản với hồ sơ có đúng người không |
| `QA-Adversarial-Integrity-Checklist.md` | Đối kháng và liêm chính | **Bắc cầu Mục B.** Giả mạo tài khoản là một dạng tấn công, phần phòng thủ nằm ở file kia |
| **File này** | **Vòng đời hồ sơ từ hệ thống nguồn · trùng hồ sơ người thật · liên kết và gỡ liên kết tài khoản · xác minh quyền sở hữu · hồ sơ mất điều kiện tham gia** | |

### Nguyên tắc bao trùm

> **Giả định nền tảng:** hồ sơ trong hệ thống là một người thật, và mọi sai sót ở lớp danh tính đều dẫn tới quy kết nhầm người.
>
> Ba câu hỏi phải trả lời được cho mọi hồ sơ:
>
> 1. **Hồ sơ này là một người hay nhiều người bị gộp nhầm.** Hai người trùng tên, hoặc một người có hai hồ sơ vì đồng bộ hai lần.
> 2. **Tài khoản mạng xã hội gắn vào hồ sơ có đúng là của người đó không.** Gắn nhầm thì mọi nội dung của người khác bị tính cho người này.
> 3. **Người này còn thuộc phạm vi giám sát không.** Hết điều kiện tham gia mà hệ thống vẫn giám sát là vượt quyền.
>
> Lỗi đắt nhất của lớp này không phải hiển thị sai tên. Đó là **gắn nội dung của người A vào hồ sơ người B**, vì hậu quả rơi vào một người thật và thường chỉ phát hiện khi người đó khiếu nại.

---

## Mẫu danh sách test case

Dùng bảng thống nhất quy định trong `CLAUDE.md` Mục 4.2, theo `Testcase_Template.md` Mục 24, bỏ 2 cột Automation:

| ID | Mục đích kiểm thử | Tiền điều kiện | Các bước thực hiện | Kết quả mong muốn | Kết quả thực tế | Mức độ ưu tiên | Ghi chú | Mã SRS |
|---|---|---|---|---|---|---|---|---|
| TC-[Mã]-001 | [Mô tả] | [Tiền điều kiện] | 1. …<br>2. … | [Kết quả chi tiết] | | P0 | | [Mã yêu cầu] |

- Case chạm vào **gắn nhầm người · gộp nhầm hai người · giám sát người ngoài phạm vi · lộ dữ liệu cá nhân** được nâng lên `P0`.
- Tiền điều kiện ghi rõ **hồ sơ đang ở trạng thái nào và đã liên kết những tài khoản nào**.

---

## Mục lục

- [A. Bảng thông tin cần xác định trước khi viết case](#a)
- [B. Trùng hồ sơ và gộp nhầm người](#b)
- [C. Hồ sơ đồng bộ từ hệ thống nguồn](#c)
- [D. Liên kết và gỡ liên kết tài khoản mạng xã hội](#d)
- [E. Xác minh quyền sở hữu tài khoản](#e)
- [F. Vòng đời trạng thái hồ sơ](#f)
- [G. Hồ sơ mất điều kiện tham gia](#g)
- [H. Dữ liệu cá nhân trên hồ sơ](#h)
- [I. Hồ sơ và dữ liệu liên quan khi rời hệ thống](#i)

---

<a name="a"></a>
## A. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo đặc tả) |
|---|---|
| Hồ sơ vào hệ thống bằng những đường nào? | `[ví dụ: đồng bộ từ hệ thống nguồn, tạo tay, nhập hàng loạt]` |
| Cái gì định danh duy nhất một người? | `[ví dụ: mã từ hệ thống nguồn, số giấy tờ, số điện thoại]` |
| Trường nào do hệ thống nguồn giữ làm gốc, trường nào sửa được tại đích? | `[liệt kê]` |
| Sửa trường tại đích rồi hệ thống nguồn đồng bộ lại thì ai thắng? | `[...]` |
| Một hồ sơ gắn tối đa bao nhiêu tài khoản? Cùng một nền tảng có gắn nhiều tài khoản không? | `[...]` |
| Một tài khoản có gắn được vào hai hồ sơ không? | `[...]` |
| Có bước xác minh quyền sở hữu tài khoản không? Xác minh bằng cách nào? | `[...]` |
| Hồ sơ có mấy trạng thái, điều kiện chuyển giữa các trạng thái? | `[...]` |
| Người mất điều kiện tham gia thì hồ sơ xử lý ra sao? | `[...]` |
| Dữ liệu đã thu thập của một hồ sơ bị gỡ thì giữ bao lâu, ai xem được? | `[...]` |

> ⚠ Bốn ô bắt buộc: **định danh duy nhất**, **trường nào là gốc**, **một tài khoản gắn được mấy hồ sơ**, **mất điều kiện tham gia thì xử lý ra sao**. Thiếu thì Mục B, C, G chưa viết được.

---

<a name="b"></a>
## B. Trùng hồ sơ và gộp nhầm người

- Hệ thống nguồn đẩy cùng một người hai lần: chỉ tạo **một** hồ sơ
- Hai người **trùng họ tên hoàn toàn**: tạo hai hồ sơ riêng, không gộp. Đây là case bắt buộc, ưu tiên `P0`
- Hai người trùng tên và trùng cả nghệ danh: vẫn phải phân biệt được bằng định danh
- Một người được đẩy sang với định danh khác so với lần trước: kiểm hệ thống nhận ra là một người hay tạo hồ sơ mới
- Tên viết khác nhau về dấu, về hoa thường, về khoảng trắng: kiểm có bị coi là hai người không
- Tạo tay một hồ sơ trùng với hồ sơ đã đồng bộ về: bị chặn hoặc cảnh báo
- Có chức năng gộp hai hồ sơ thì kiểm riêng: nội dung, điểm, lịch sử của cả hai đi về đâu, và gộp nhầm có hoàn tác được không
- Sau khi gộp, mọi liên kết cũ trỏ tới hồ sơ bị gộp vẫn dẫn về đúng hồ sơ còn lại, không dẫn tới trang lỗi

---

<a name="c"></a>
## C. Hồ sơ đồng bộ từ hệ thống nguồn

- Hệ thống nguồn đẩy hồ sơ mới: xuất hiện đúng lúc theo đặc tả, không chờ vòng chạy nếu đặc tả nói là đẩy ngay
- Hồ sơ mới xuất hiện với đầy đủ các trường bắt buộc: thiếu trường thì kiểm hệ thống từ chối nhận hay nhận với phần trống
- Hệ thống nguồn cập nhật một trường: hồ sơ tại đích đổi theo, đúng trường đó, không đụng trường khác
- Người dùng sửa một trường tại đích rồi hệ thống nguồn đồng bộ lại: kiểm ai thắng, đúng theo ô đã chốt ở Mục A. Đây là chỗ mất dữ liệu thầm lặng, ưu tiên `P0`
- Hệ thống nguồn gửi dữ liệu sai định dạng hoặc thiếu trường bắt buộc: bị từ chối và ghi log, không tạo hồ sơ hỏng
- Hệ thống nguồn không kết nối được: hồ sơ hiện có giữ nguyên, có báo cho người vận hành, và hồ sơ mới được bù khi kết nối trở lại
- Cùng một hồ sơ được đẩy nhiều lần liên tiếp rất nhanh: không tạo trùng, kết quả cuối cùng là lần đẩy mới nhất
- Hồ sơ bị xóa ở hệ thống nguồn: kiểm tại đích xử lý ra sao, và dữ liệu đã thu thập của hồ sơ đó đi đâu
- Hồ sơ đang có nội dung nằm trong hàng chờ duyệt mà bị đồng bộ thay đổi: các nội dung đó không bị mất

---

<a name="d"></a>
## D. Liên kết và gỡ liên kết tài khoản mạng xã hội

- Gắn một tài khoản vào hồ sơ: gắn được, và từ vòng chạy kế tiếp bắt đầu thu thập nội dung của tài khoản đó
- Gắn nhiều tài khoản **trên cùng một nền tảng** vào một hồ sơ: kiểm cho phép không, và giao diện hiển thị ra sao
- Gắn **cùng một tài khoản vào hai hồ sơ khác nhau**: kiểm chặn hay cho phép. Cho phép thì nội dung được tính cho ai. Đây là case bắt buộc, ưu tiên `P0`
- Gắn một đường dẫn tài khoản không tồn tại, hoặc sai định dạng: bị chặn kèm thông báo rõ
- Gắn tài khoản của nền tảng không nằm trong danh sách hỗ trợ
- Gỡ một tài khoản khỏi hồ sơ: nội dung đã thu về từ tài khoản đó **còn hay mất**, và điểm đã cộng có bị trừ không. Đây là câu hỏi nghiệp vụ, chốt trước khi viết
- Gỡ rồi gắn lại cùng tài khoản: nội dung cũ có được nối lại hay coi như dữ liệu mới
- Hồ sơ không có tài khoản nào: hiển thị đúng trạng thái rỗng, các màn phía sau không lỗi
- Bật tắt giám sát ở nhiều mức lồng nhau, ví dụ mức hồ sơ, mức từng tài khoản, mức từng nguồn bổ sung: tắt mức trên thì mọi mức dưới dừng theo, bật lại mức trên thì mức dưới trở về đúng trạng thái riêng của nó chứ không bật hết. Kiểm đủ các tổ hợp bật tắt
- Mọi thay đổi trong màn cấu hình chỉ có hiệu lực sau khi lưu: thêm tài khoản rồi đóng màn không lưu thì không có gì thay đổi. Kiểm cả trường hợp **có hai cấp lưu lồng nhau**, ví dụ lưu từng dòng rồi lưu cả màn, và làm rõ dòng đã lưu ở cấp trong nhưng chưa lưu ở cấp ngoài thì thực sự tồn tại chưa

---

<a name="e"></a>
## E. Xác minh quyền sở hữu tài khoản

> Chỉ bật khi hệ thống có bước chứng minh tài khoản thuộc về người trong hồ sơ.

- Luồng xác minh thành công: tài khoản chuyển sang trạng thái đã xác minh, có ghi người xác minh và thời điểm
- Luồng xác minh thất bại: tài khoản giữ trạng thái chờ, nêu rõ lý do, và cho làm lại
- Từ chối xác minh: bắt buộc nhập lý do, và người gửi nhận được lý do đó
- Tài khoản chưa xác minh: kiểm nội dung của nó có được thu thập và tính điểm không. Nếu có thì đây là rủi ro quy kết nhầm, ghi vào note
- Xác minh rồi tài khoản đổi chủ hoặc đổi định danh: trạng thái xác minh còn hiệu lực không
- Thu hồi xác minh: tài khoản trở về trạng thái chờ, và nội dung đã thu thập xử lý theo hướng đã chốt
- Gửi yêu cầu xác minh hai lần cho cùng một tài khoản: chặn trùng
- Người không đủ quyền thực hiện xác minh: bị từ chối ở tầng máy chủ, không chỉ ẩn nút

---

<a name="f"></a>
## F. Vòng đời trạng thái hồ sơ

- Mỗi trạng thái của hồ sơ có điều kiện chuyển rõ ràng, mỗi đường chuyển một case
- Thao tác theo thứ tự ngược, ví dụ đưa hồ sơ về trạng thái trước đó: kiểm được phép hay bị chặn. Kế thừa `Testcase_Template.md` Mục 25
- Trạng thái hồ sơ đổi thì các màn khác cập nhật theo, gồm danh sách, bảng xếp hạng, hàng chờ duyệt
- Bộ lọc theo trạng thái trả về đúng tập hồ sơ
- Trạng thái đổi trong lúc người dùng đang mở màn chi tiết: thao tác tiếp theo bị chặn đúng cách, không âm thầm thất bại
- Điều kiện chuyển trạng thái chưa được đặc tả chốt: **không gen case đoán mò**, ghi câu hỏi vào note. Vẫn gen được case ràng buộc bất biến, ví dụ hồ sơ luôn phải ở đúng một trạng thái tại một thời điểm và không bao giờ ở trạng thái trống

---

<a name="g"></a>
## G. Hồ sơ mất điều kiện tham gia

> Nhóm này gần như luôn bị bỏ sót vì đặc tả chỉ viết luồng đi vào, không viết luồng đi ra.

- Người bị thu hồi điều kiện tham gia ở hệ thống nguồn: hồ sơ tại đích đổi trạng thái đúng, và **việc thu thập dừng lại**
- Việc thu thập không dừng: đây là lỗi vượt quyền giám sát, ưu tiên `P0`
- Hồ sơ đã dừng giám sát: còn xuất hiện trong danh sách không, còn tính vào thẻ số liệu và bảng xếp hạng không
- Người lấy lại điều kiện tham gia: hồ sơ hoạt động trở lại, và khoảng thời gian bị dừng có được thu thập bù không
- Hồ sơ bị dừng giữa kỳ: số liệu của kỳ đó tính tới thời điểm dừng hay tính cả kỳ
- Người dùng chủ động yêu cầu ngừng giám sát, nếu đặc tả cho phép: luồng đó chạy đúng và có ghi nhật ký

---

<a name="h"></a>
## H. Dữ liệu cá nhân trên hồ sơ

- Trường dữ liệu cá nhân chỉ hiện với vai trò có quyền, các vai trò khác không thấy và gọi thẳng API cũng không lấy được. Ưu tiên `P0`
- Dữ liệu nhạy cảm hiển thị dạng che một phần ở các màn danh sách, chỉ hiện đầy đủ ở màn chi tiết với người đủ quyền, nếu đặc tả quy định vậy
- Xuất dữ liệu ra tệp: phạm vi trường xuất đúng với quyền của người xuất, không xuất thừa
- Tìm kiếm theo trường nhạy cảm: kiểm có cho phép không, vì cho phép tìm là một cách dò dữ liệu
- Nhật ký ghi lại việc ai đã xem hồ sơ nào, nếu đặc tả yêu cầu
- Ảnh đại diện và nội dung lấy từ nguồn ngoài: hiển thị đúng và không dẫn tới việc tải dữ liệu từ nguồn mỗi lần mở màn, nếu đặc tả quy định phải lưu lại

---

<a name="i"></a>
## I. Hồ sơ và dữ liệu liên quan khi rời hệ thống

- Xóa một hồ sơ: kiểm ràng buộc theo `Testcase_Template.md` Mục 10, và kiểm thêm phần dữ liệu đã thu thập, điểm, lịch sử xử lý, vị trí trong bảng xếp hạng
- Xóa hồ sơ đang có nội dung trong hàng chờ duyệt: các nội dung đó xử lý ra sao
- Xóa mềm rồi khôi phục: dữ liệu liên quan trở lại đầy đủ
- Sau khi xóa, các liên kết trỏ tới hồ sơ đó từ màn khác không dẫn tới trang lỗi
- Số liệu tổng hợp và bảng xếp hạng cập nhật lại sau khi xóa, không còn đếm hồ sơ đã xóa
- Có yêu cầu xóa dữ liệu cá nhân theo quy định thì kiểm riêng: dữ liệu nào bắt buộc xóa, dữ liệu nào được giữ lại vì lý do đối soát, và hệ thống làm được tới đâu

---

## Tự review, điểm yếu và khuyến nghị

### Điểm mạnh

- Mục B và D phủ đúng hai cách quy kết nhầm người: gộp nhầm hai người thành một hồ sơ, và gắn tài khoản của người khác vào hồ sơ.
- Mục G là luồng đi ra, thứ mà đặc tả gần như luôn quên vì chỉ viết luồng đi vào.
- Mục C xử lý đúng chỗ khó của đồng bộ một chiều: sửa tại đích rồi bị nguồn ghi đè, một kiểu mất dữ liệu không ai thấy.

### Điểm yếu còn lại

- Chưa phủ trường hợp một người có hồ sơ ở nhiều tổ chức hoặc nhiều không gian dữ liệu tách biệt.
- Mục E giả định xác minh do người trong hệ thống thực hiện. Hệ thống nào để chính chủ tài khoản tự xác minh bằng mã hoặc bằng đăng nhập sẽ cần thêm một nhóm về luồng của người ngoài.
- Chưa có nhóm về nhập hồ sơ hàng loạt bằng tệp, phần đó nằm ở `Testcase_Template.md` Mục 20 nhưng khía cạnh trùng người thì chưa nối vào.
- Phần dữ liệu cá nhân ở Mục H mới ở mức kiểm được bằng thao tác. Khía cạnh pháp lý phải do bên nghiệp vụ chốt, checklist không thay thế được.

### Khuyến nghị

- Dựng sẵn hai hồ sơ trùng họ tên hoàn toàn trong dữ liệu mẫu. Không có cặp này thì cả Mục B không chạy được.
- Mục D nên kiểm bằng cách gắn một tài khoản có nội dung rõ ràng rồi xem nội dung đó chảy vào đúng hồ sơ nào, thay vì chỉ kiểm màn cấu hình lưu được hay không.
- Mục G cần môi trường mô phỏng được việc hệ thống nguồn thu hồi điều kiện tham gia. Không mô phỏng được thì ghi là nhóm bị chặn trong RTM, đừng bỏ qua im lặng.
