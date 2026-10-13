# Checklist Kiểm thử Luồng Máy Chấm, Người Duyệt

### File tầng 3. Áp dụng khi hệ thống **để máy đưa ra kết quả trước, rồi người có quyền xem lại, sửa hoặc phủ nhận kết quả đó**, và kết quả cuối cùng mới được dùng cho nghiệp vụ

---

## Quan hệ với các file khác

| File | Phạm vi | Quan hệ với file này |
|---|---|---|
| `Testcase_Template.md` | Nền tảng chung | **Kế thừa toàn bộ** |
| `Testcase_Template.md` Mục 8.6 (nhật ký hệ thống) | Có ghi log hay không | **Được mở rộng bởi file này.** Ở đây nhật ký không phải thứ có cũng được, nó là bằng chứng phân định trách nhiệm giữa máy và người, nên có nhóm case riêng |
| `Testcase_Template.md` Mục 25 (chuyển đổi trạng thái) | Vòng đời bản ghi, thứ tự thao tác ngược | **Kế thừa và bắc cầu.** Mục 25 lo phần thứ tự, file này lo phần bản ghi **quay lại** hàng chờ sau khi đã xử lý xong |
| `Testcase_Template.md` Mục 16 (xử lý đồng thời) | Hai người cùng sửa một bản ghi | **Kế thừa.** File này chỉ thêm phần đặc thù của hàng chờ duyệt |
| `QA-Scoring-RuleBase-Checklist.md` | Chấm điểm theo bộ quy tắc | **Bắc cầu.** File kia lo điểm máy chấm ra bao nhiêu, file này lo chuyện người sửa điểm đó và ai thắng ai |
| `QA-States-Errors-Notification-Checklist.md` | Trạng thái màn hình, thông báo | **Kế thừa** cho phần hiển thị trạng thái rỗng và lỗi của hàng chờ |
| **File này** | **Máy trả kết quả chậm hoặc lỗi · người sửa đè máy · máy không được đè lại người · quay lại hàng chờ · lịch sử xử lý · duyệt đồng thời và duyệt hàng loạt · đối soát chất lượng máy** | |

### Nguyên tắc bao trùm

> **Giả định nền tảng:** kết quả của máy là đề xuất, kết quả của người là quyết định. Mọi thiết kế đi ngược nguyên tắc này đều là lỗi nghiệp vụ chứ không phải lỗi giao diện.
>
> Ba câu hỏi phải trả lời được cho từng bản ghi, ở mọi thời điểm:
>
> 1. **Ai là người quyết định giá trị đang hiển thị**, máy hay người, và từ lúc nào.
> 2. **Máy chạy lại có đè lên quyết định của người không.** Đáp án đúng gần như luôn là không, và phải có case chứng minh.
> 3. **Nhìn lại sau ba tháng có dựng lại được diễn biến không.** Không dựng lại được thì lịch sử xử lý đang thiếu.
>
> Lỗi đắt nhất của lớp này không phải máy chấm sai. Máy chấm sai thì người sửa. Lỗi đắt nhất là **máy âm thầm sửa lại cái người đã quyết**, vì nó phá luôn niềm tin vào toàn bộ dữ liệu.

---

## Mẫu danh sách test case

Dùng bảng thống nhất quy định trong `CLAUDE.md` Mục 4.2, theo `Testcase_Template.md` Mục 24, bỏ 2 cột Automation:

| ID | Mục đích kiểm thử | Tiền điều kiện | Các bước thực hiện | Kết quả mong muốn | Kết quả thực tế | Mức độ ưu tiên | Ghi chú | Mã SRS |
|---|---|---|---|---|---|---|---|---|
| TC-[Mã]-001 | [Mô tả] | [Tiền điều kiện] | 1. …<br>2. … | [Kết quả chi tiết] | | P0 | | [Mã yêu cầu] |

- Case chạm vào **quyết định của người bị đè · mất dấu vết xử lý · bản ghi kẹt vĩnh viễn trong hàng chờ** được nâng lên `P0`.
- Phần lớn case của Mục D và F không nhìn thấy trên giao diện. Cột Ghi chú phải nói rõ verify ở bảng nào hoặc log nào.
- Tiền điều kiện phải ghi rõ **bản ghi đang ở trạng thái nào và ai đã động vào nó trước đó**.

---

## Mục lục

- [A. Bảng thông tin cần xác định trước khi viết case](#a)
- [B. Kết quả máy: đủ, thiếu, chậm, lỗi](#b)
- [C. Người xem lại và sửa kết quả máy](#c)
- [D. Máy chạy lại không được đè lên quyết định của người](#d)
- [E. Vòng đời hàng chờ và bản ghi quay lại](#e)
- [F. Lịch sử xử lý và truy vết](#f)
- [G. Nhiều người cùng xử lý một hàng chờ](#g)
- [H. Xử lý hàng loạt](#h)
- [I. Luồng khiếu nại và xem xét lại](#i)
- [J. Đối soát chất lượng của máy](#j)

---

<a name="a"></a>
## A. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo đặc tả) |
|---|---|
| Máy trả về những giá trị gì cho một bản ghi? | `[ví dụ: sắc thái và điểm rủi ro]` |
| Người duyệt sửa được những giá trị nào, trong khoảng nào? | `[...]` |
| Máy không trả kết quả thì bản ghi nằm ở trạng thái nào? | `[...]` |
| Ngưỡng chờ kết quả máy là bao lâu? Quá ngưỡng thì sao? | `[đề xuất theo thông lệ: 5 phút cho một bản ghi, quá thì chuyển sang trạng thái chờ xử lý tay và báo người vận hành. Chờ BA xác nhận]` |
| Bản ghi bắt buộc phải qua người duyệt, hay có trường hợp máy tự thông qua? | `[...]` |
| Sự kiện nào làm bản ghi đã xử lý quay lại hàng chờ? | `[...]` |
| Bản ghi quay lại hàng chờ thì điểm đã tính vào bản ghi cha xử lý ra sao? | `[...]` |
| Kết quả đã duyệt có sửa lại được không? Qua đường nào? | `[...]` |
| Ai được duyệt, ai được xem lại quyết định của người khác? | `[...]` |
| Lịch sử xử lý lưu bao lâu, ai xem được? | `[...]` |

> ⚠ Ba ô bắt buộc: **máy không trả kết quả thì bản ghi ở đâu**, **sự kiện làm bản ghi quay lại hàng chờ**, **quay lại thì điểm cha xử lý ra sao**. Thiếu thì Mục B và E chưa viết được.

---

<a name="b"></a>
## B. Kết quả máy: đủ, thiếu, chậm, lỗi

### B.1. Luồng thuận

- Bản ghi mới vào hệ thống, máy chấm xong, bản ghi xuất hiện trong hàng chờ kèm đầy đủ kết quả máy
- Khối kết quả máy là **chỉ đọc** ở mọi trạng thái, không có đường nào sửa được. Thử gọi thẳng API để sửa cũng bị từ chối. Ưu tiên `P0`
- Kết quả máy hiển thị đúng ở mọi nơi: danh sách hàng chờ, màn chi tiết, lịch sử xử lý

### B.2. Máy thiếu kết quả

- Máy chỉ trả một phần kết quả, ví dụ có sắc thái mà không có điểm: kiểm bản ghi có vào hàng chờ không, và giao diện hiển thị phần thiếu thế nào. Không được hiển thị số không thay cho không có
- Máy trả giá trị nằm ngoài khoảng cho phép: hệ thống chặn ở đầu vào chứ không lưu rồi để giao diện vỡ
- Máy trả giá trị không nằm trong tập giá trị hợp lệ, ví dụ một nhãn sắc thái lạ

### B.3. Máy chậm hoặc lỗi

- Máy chưa trả kết quả tại thời điểm người dùng mở màn: kiểm bản ghi hiện ở đâu, hiện ra sao, và **người duyệt có bị chặn thao tác không**
- Quá ngưỡng chờ mà máy vẫn chưa trả: bản ghi chuyển sang trạng thái nào, có báo cho ai không, và có kẹt vĩnh viễn không. Case chống kẹt vĩnh viễn là `P0`
- Đo thời gian từ lúc nội dung vào hệ thống tới lúc có kết quả máy: trong ngưỡng 5 phút ở điều kiện bình thường. Ghi chú `Ngưỡng theo thông lệ, chờ BA xác nhận`
- Một nghìn bản ghi vào cùng lúc sau vòng quét đêm: kiểm hàng chờ tiêu thụ hết trước giờ làm việc, không dồn ứ sang ngày hôm sau
- Dịch vụ chấm hỏng trong lúc một loạt bản ghi đang chờ: các bản ghi đó được thử lại hay nằm im, và người vận hành có biết không
- Dịch vụ chấm hồi phục: các bản ghi tồn đọng được xử lý, không mất và không trùng
- Trong lúc máy hỏng, luồng thu thập vẫn chạy: bản ghi mới xếp hàng chứ không bị bỏ

---

<a name="c"></a>
## C. Người xem lại và sửa kết quả máy

- Người duyệt giữ nguyên kết quả máy rồi thông qua: kết quả cuối bằng kết quả máy, lịch sử vẫn ghi một mốc là người đã xem và đồng ý
- Người duyệt đổi giá trị: giao diện hiện rõ **giá trị máy và giá trị người đặt cạnh nhau**, không chỉ hiện giá trị mới
- Người duyệt đổi rồi đổi lại về đúng giá trị máy trước khi lưu: kiểm hệ thống còn coi là có sửa không, và phần bắt buộc nhập lý do có còn bắt buộc không
- Sửa giá trị thì bắt buộc nhập lý do, bỏ trống thì báo lỗi và **không đổi trạng thái bản ghi**. Kiểm kỹ vế sau, đây là chỗ hay lỗi
- Nhập lý do chỉ gồm dấu cách, kiểm có bị coi là rỗng không
- Nhập lý do vượt giới hạn ký tự
- Từ chối bản ghi mà bỏ trống lý do: bị chặn
- Đang sửa dở rồi đóng modal hoặc bấm hủy: mọi thay đổi bị bỏ, bản ghi giữ nguyên trạng thái cũ. Mở lại thì không còn dấu vết bản nháp
- Bản ghi đã xử lý xong mở xem lại: khối nhập của người duyệt chuyển sang chỉ đọc, các nút xử lý không còn tác dụng, kể cả khi gọi thẳng API

---

<a name="d"></a>
## D. Máy chạy lại không được đè lên quyết định của người

> Nhóm quan trọng nhất của file. Toàn bộ nhóm này verify ở tầng dữ liệu, giao diện không giúp được gì.

- Người duyệt sửa sắc thái của một bản ghi. Chạy lại vòng quét. Giá trị người đặt **giữ nguyên**, máy không ghi đè
- Tương tự với điểm rủi ro
- Chạy lại nhiều lần liên tiếp, giá trị người đặt vẫn nguyên sau mọi lần
- Máy chạy lại ra kết quả **khác** kết quả lần đầu và khác cả giá trị người đặt: kiểm hệ thống lưu kết quả máy mới ở đâu, và giá trị đang dùng cho nghiệp vụ vẫn là giá trị người
- Bản ghi người **chưa** động vào: máy chạy lại được phép cập nhật, kiểm có cập nhật đúng không
- Người duyệt sửa xong, ngay lúc đó vòng quét đang chạy trên chính bản ghi đó: kiểm kết quả cuối cùng là giá trị người, không có cửa sổ thời gian nào để máy thắng
- Mọi giá trị hiển thị trên các màn khác, ví dụ chấm màu theo sắc thái, chip từ khóa, bộ lọc theo sắc thái, đều tính theo **giá trị cuối cùng** chứ không theo giá trị máy

---

<a name="e"></a>
## E. Vòng đời hàng chờ và bản ghi quay lại

- Bản ghi được thông qua: rời hàng chờ, xuất hiện ở nơi dành cho bản ghi đã xử lý, và bắt đầu được tính vào nghiệp vụ phía sau
- Bản ghi bị từ chối: rời hàng chờ, **không** được tính vào nghiệp vụ phía sau. Kiểm cả ở màn danh sách nội dung lẫn ở điểm của bản ghi cha
- Bản ghi đã thông qua gặp sự kiện làm nó quay lại hàng chờ: quay lại đúng, và lịch sử ghi một mốc nêu rõ lý do quay lại
- Bản ghi quay lại hàng chờ thì **điểm đã cộng cho bản ghi cha** xử lý ra sao: trừ ra trong lúc chờ, hay giữ nguyên. Chốt với BA rồi mới viết, đây là câu hỏi nghiệp vụ
- Bản ghi quay lại rồi bị từ chối: điểm đã cộng trước đó phải bị trừ ra
- Bản ghi quay lại nhiều lần: lịch sử ghi đủ các lần, không đè lên nhau
- Bản ghi đã bị từ chối gặp cùng sự kiện đó: kiểm có quay lại hàng chờ không, hay bị từ chối là xong
- Kiểm không có vòng lặp: bản ghi không được quay lại hàng chờ liên tục không dứt do một sự kiện tự lặp
- Thứ tự trong hàng chờ: bản ghi quay lại xếp ở đâu, đầu hay cuối, và có nhất quán không

---

<a name="f"></a>
## F. Lịch sử xử lý và truy vết

- Mỗi lần máy chấm ghi một mốc, có giá trị máy chấm và thời điểm
- Mỗi lần người xử lý ghi một mốc, có người thực hiện, vai trò, thời điểm, giá trị trước, giá trị sau, và lý do nếu có
- Bản ghi đi qua nhiều lượt máy chấm và nhiều lượt người sửa: lịch sử ghi đủ, đúng thứ tự thời gian, không nhảy cóc
- Mốc hiện tại được đánh dấu rõ, người đọc biết bản ghi đang ở bước nào
- Lịch sử là dữ liệu chỉ đọc: không ai sửa hay xóa được một mốc, kể cả vai trò cao nhất, kể cả gọi thẳng API. Ưu tiên `P0`
- Bản ghi có rất nhiều mốc: hiển thị vẫn dùng được, không vỡ bố cục
- Tài khoản người xử lý bị vô hiệu hóa sau đó: lịch sử vẫn hiện đúng tên người đã xử lý, không thành trống
- Ai được xem lịch sử, theo đúng ma trận phân quyền

---

<a name="g"></a>
## G. Nhiều người cùng xử lý một hàng chờ

- Hai người mở cùng một bản ghi, người thứ nhất xử lý xong: người thứ hai bấm xử lý thì bị chặn kèm thông báo rõ ràng, không được ghi đè âm thầm
- Người thứ hai được thấy trạng thái mới sau khi làm mới màn, không phải đăng nhập lại
- Hai người xử lý hai bản ghi khác nhau cùng lúc: cả hai thành công
- Một bản ghi bị một người mở lâu không thao tác: kiểm có cơ chế giữ chỗ không, nếu có thì kiểm cả lúc hết thời gian giữ
- Số đếm bản ghi chờ trên giao diện cập nhật đúng sau khi người khác xử lý xong một bản ghi
- Đang mở modal xử lý thì phiên hết hạn: bấm nút xử lý bị từ chối đúng cách, dữ liệu đã nhập không âm thầm biến mất mà không có lời giải thích

---

<a name="h"></a>
## H. Xử lý hàng loạt

> Chỉ bật nhóm này khi hệ thống có thao tác chọn nhiều bản ghi rồi xử lý một lượt.

- Chọn nhiều bản ghi rồi thông qua: tất cả đổi trạng thái, mỗi bản ghi ghi một mốc lịch sử riêng
- Một bản ghi trong lô lỗi: kiểm các bản ghi còn lại có thành công không, và kết quả từng bản ghi có được báo rõ không
- Chọn lẫn bản ghi đang chờ và bản ghi đã xử lý: hệ thống chỉ xử lý phần hợp lệ và nói rõ phần bị bỏ qua
- Chọn tất cả khi đang có bộ lọc: phạm vi chọn là các bản ghi khớp bộ lọc chứ không phải toàn bộ hệ thống, và giao diện nói rõ đang chọn bao nhiêu bản ghi
- Xử lý hàng loạt với thao tác bắt buộc nhập lý do: kiểm lý do áp cho cả lô hay từng bản ghi
- Lô rất lớn: kiểm hành vi giao diện trong lúc chạy, và kiểm không có bản ghi nào bị bỏ sót giữa chừng

---

<a name="i"></a>
## I. Luồng khiếu nại và xem xét lại

> Chỉ bật khi đối tượng bị chấm điểm có quyền yêu cầu xem xét lại kết quả.

- Gửi yêu cầu xem xét cho một bản ghi đã xử lý: yêu cầu vào đúng hàng chờ của người có quyền
- Gửi yêu cầu cho bản ghi **chưa** xử lý xong: kiểm có cho phép không
- Gửi hai yêu cầu cho cùng một bản ghi: kiểm chặn trùng hay chấp nhận
- Yêu cầu được chấp nhận: kết quả của bản ghi đổi theo, điểm của bản ghi cha cập nhật theo, lịch sử ghi rõ đổi vì yêu cầu xem xét
- Yêu cầu bị từ chối: kết quả bản ghi giữ nguyên, người gửi nhận được lý do
- Người xử lý yêu cầu chính là người đã ra quyết định ban đầu: kiểm có chặn không, đây là câu hỏi nghiệp vụ nên hỏi BA
- Bản ghi bị xóa hoặc mất hiệu lực trong lúc yêu cầu đang chờ xử lý

---

<a name="j"></a>
## J. Đối soát chất lượng của máy

- Đối chiếu được kết quả máy với kết quả cuối cùng cho từng bản ghi, phục vụ việc đánh giá máy chấm tốt tới đâu
- Thống kê tỉ lệ bản ghi bị người sửa, nếu hệ thống có màn thống kê: kiểm con số khớp với dữ liệu thật
- Chọn một tập bản ghi mẫu, người có chuyên môn chấm tay, so với kết quả máy. Đây là case thủ công, không tự động hóa được, và vẫn cần làm định kỳ
- Thay đổi phiên bản của máy chấm: kiểm hệ thống có ghi nhận bản ghi nào chấm bởi phiên bản nào không. Không ghi thì mọi so sánh theo thời gian đều vô nghĩa, ghi điểm này vào note

---

## Tự review, điểm yếu và khuyến nghị

### Điểm mạnh

- Mục D là nhóm case mà hầu như không đội nào tự nghĩ ra, vì trên giao diện không có gì gợi ý nó tồn tại, nhưng hỏng thì hỏng âm thầm và hỏng toàn bộ dữ liệu.
- Mục E xử lý đúng chỗ khó nhất của mọi hàng chờ duyệt, là bản ghi quay lại sau khi đã xử lý xong, kèm câu hỏi điểm đã cộng thì làm gì.
- Ba câu hỏi ở phần nguyên tắc bao trùm dùng được như bộ tự kiểm nhanh cho bất kỳ màn nào có máy chấm.

### Điểm yếu còn lại

- File giả định một cấp duyệt. Hệ thống có nhiều cấp, ví dụ chuyên viên duyệt rồi trưởng nhóm duyệt lại, sẽ cần thêm một nhóm về chuyển cấp và về việc cấp trên đè cấp dưới.
- Chưa phủ phần phân công bản ghi cho người duyệt. Hàng chờ hiện đang coi là ai cũng lấy được bản ghi bất kỳ.
- Mục J mới ở mức khung. Đo chất lượng máy chấm một cách nghiêm túc cần bộ dữ liệu chuẩn và cần thống nhất chỉ số, phần đó vượt phạm vi một checklist kiểm thử.
- Chưa có nhóm về ngưỡng tin cậy của máy, tức là máy tự biết mình không chắc rồi chuyển thẳng cho người. Hệ thống nào có cơ chế đó cần bổ sung.

### Khuyến nghị

- Mục D nên chạy được bằng cách ép vòng quét chạy lại theo yêu cầu. Môi trường test không ép được thì cả mục này thành nhóm bị chặn, ghi rõ vào RTM chứ đừng viết case rồi bỏ đó.
- Mỗi case của Mục C và E nên kiểm luôn hệ quả lên bản ghi cha trong cùng một case, thay vì tách ra. Tách ra thì rất dễ bỏ sót chỗ trạng thái đổi mà điểm không đổi theo.
- Nhóm Mục H chỉ bật khi giao diện thật sự có thao tác hàng loạt. Không có thì bỏ cả mục, đừng gen case cho chức năng không tồn tại.
