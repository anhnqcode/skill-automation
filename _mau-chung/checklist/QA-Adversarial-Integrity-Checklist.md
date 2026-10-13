# Checklist Tư duy Đối kháng và Liêm chính Dữ liệu

### File tầng 3. Áp dụng khi kết quả của hệ thống **ảnh hưởng tới quyền lợi hoặc danh dự của một người thật**, và khi có người có động cơ làm sai lệch kết quả đó

---

## Quan hệ với các file khác

| File | Phạm vi | Quan hệ với file này |
|---|---|---|
| `Testcase_Template.md` | Nền tảng chung | **Kế thừa toàn bộ** |
| `Testcase_Template.md` Mục 9 (phân quyền) | Ai được làm gì | **Được mở rộng bởi Mục C.** Mục 9 kiểm người **không có quyền** bị chặn. File này kiểm người **có quyền** dùng quyền đó sai mục đích, đó là lớp rủi ro Mục 9 không chạm tới |
| `Testcase_Template.md` Mục 8.6 (nhật ký) | Có ghi log không | **Được mở rộng bởi Mục H.** Ở đây nhật ký là bằng chứng dựng lại hiện trường, không phải thứ có cũng được |
| `QA-Scoring-RuleBase-Checklist.md` Mục B | Quy tắc khớp từ khóa | **Bắc cầu Mục B.** File kia kiểm khớp đúng chưa, file này kiểm người ta né được không |
| `QA-AI-Assisted-Review-Checklist.md` | Máy chấm, người duyệt | **Bắc cầu Mục C và E.** File kia kiểm luồng chạy đúng, file này kiểm người duyệt có bị đẩy vào thế làm ẩu không |
| `QA-Identity-Account-Linking-Checklist.md` | Danh tính và liên kết | **Bắc cầu Mục D.** Gắn nhầm người là một nguồn của quy kết oan |
| `Template_Testcase_Advanced.md` Mục C.6 | Gian lận thuật toán | **Bắc cầu.** Mục C.6 viết cho thuật toán gợi ý, Mục B của file này viết cho bộ quy tắc tất định |
| **File này** | **Đối tượng né hệ thống · người trong hệ thống làm lệch kết quả · quy kết oan người thật · khối lượng công việc của người duyệt · thao tác đối kháng trên giao diện · đầu vào độc hại · dựng lại hiện trường** | |

### Vì sao cần một file riêng cho tư duy, không phải cho chức năng

Các file checklist khác đi theo **chức năng**: màn này có gì, nút này làm gì, dữ liệu chảy đi đâu. Chúng chống sót. Nhưng có một loại lỗi mà không checklist chức năng nào bắt được, vì nó không nằm ở chức năng nào cả:

- Hệ thống làm **đúng mọi thứ đặc tả ghi**, và vẫn quy kết oan một người, vì không ai viết đặc tả cho trường hợp đó.
- Một chức năng **chạy đúng khi dùng đúng cách**, và bị lợi dụng khi dùng sai cách.
- Một luồng **đúng về logic**, và người thật không làm nổi vì phải lặp lại hai trăm lần mỗi ngày.

File này chống **sai trọng tâm**, không chống sót. Dùng nó sau khi đã chạy các file kia, và dùng nó để quyết định case nào đáng nâng lên `P0`.

### Bốn nhóm tư duy bắt buộc chạy trước khi gen

> **1. Bắt đầu từ rủi ro, không bắt đầu từ mục lục.**
> Viết ra 3 tới 5 câu *"hệ thống này hỏng ở đâu thì thiệt hại nhất"* rồi đặt lên đầu file ghi chú, trước khi mở bất kỳ checklist nào. Với một hệ thống giám sát người thật, câu trả lời thường là: quy kết oan một người · để lọt người vi phạm thật · số liệu sai làm người ra quyết định tin nhầm · dữ liệu cá nhân lộ ra ngoài phạm vi.
>
> **2. Người dùng thật, không phải người dùng lý tưởng.**
> Người kiểm duyệt xử lý hàng trăm bản ghi một ngày, không đọc kỹ từng câu, bấm theo thói quen. Người ra quyết định đọc con số trên màn mà không mở chi tiết. Đặc tả không mô tả những người này, nên phải tự nghĩ ra họ.
>
> **3. Tư duy đối kháng đúng bối cảnh.**
> Đối tượng bị giám sát có động cơ né. Người trong hệ thống có thể có quan hệ với đối tượng. Nội dung đưa vào hệ thống do người ngoài viết ra, và họ viết được bất cứ thứ gì.
>
> **4. Không verify được thì không phải test case.**
> Phần lớn rủi ro của lớp này nằm ở tầng dữ liệu. Mỗi case phải nói rõ verify ở bảng nào, log nào, endpoint nào.

---

## Mẫu danh sách test case

Dùng bảng thống nhất quy định trong `CLAUDE.md` Mục 4.2, theo `Testcase_Template.md` Mục 24, bỏ 2 cột Automation:

| ID | Mục đích kiểm thử | Tiền điều kiện | Các bước thực hiện | Kết quả mong muốn | Kết quả thực tế | Mức độ ưu tiên | Ghi chú | Mã SRS |
|---|---|---|---|---|---|---|---|---|
| TC-[Mã]-001 | [Mô tả] | [Tiền điều kiện] | 1. …<br>2. … | [Kết quả chi tiết] | | P0 | | [Mã yêu cầu] |

**Luật nâng bậc riêng của file này.** Một case lên `P0` bất kể checklist khác xếp hạng gì, nếu nó chạm vào:

| Nhóm | Ví dụ |
|---|---|
| **Quy kết oan người thật** | Nội dung của người khác bị tính cho hồ sơ này, nội dung hợp lệ bị chấm là vi phạm, điểm cao do lỗi kỹ thuật |
| **Để lọt có hệ thống** | Một cách né từ khóa làm cả nhóm nội dung không bao giờ bị phát hiện |
| **Người trong hệ thống làm lệch kết quả** | Sửa điểm không để lại dấu vết, xóa nội dung bất lợi cho một hồ sơ |
| **Rò rỉ dữ liệu cá nhân** | Vai trò không đủ quyền đọc được dữ liệu nhạy cảm, tệp xuất ra chứa trường không được phép |
| **Mất dấu vết** | Không dựng lại được ai đã đổi cái gì, khi nào, vì sao |

- Phần lớn case của file này là **thủ công**, không tự động hóa được. Đó không phải lý do để bỏ.
- Case nào cũng phải ghi cách verify ở cột Ghi chú.

---

## Mục lục

- [A. Lập danh sách rủi ro trọng tâm](#a)
- [B. Đối tượng bị giám sát né hệ thống](#b)
- [C. Người trong hệ thống làm lệch kết quả](#c)
- [D. Quy kết oan và quyền của người bị ảnh hưởng](#d)
- [E. Khối lượng công việc của người xử lý](#e)
- [F. Thao tác đối kháng trên giao diện](#f)
- [G. Đầu vào độc hại từ nội dung bên ngoài](#g)
- [H. Dựng lại hiện trường](#h)

---

<a name="a"></a>
## A. Lập danh sách rủi ro trọng tâm

> Đây không phải nhóm test case. Đây là việc phải làm **trước** khi mở các file checklist khác. Kết quả đặt ở đầu file ghi chú của dự án.

| Câu hỏi | Trả lời cho dự án đang làm |
|---|---|
| Kết quả của hệ thống ảnh hưởng tới ai, theo cách nào? | `[...]` |
| Sai theo hướng nào thì thiệt hại lớn hơn: bắt nhầm hay bỏ sót? | `[...]` |
| Ai có động cơ làm sai lệch kết quả? Họ làm được gì trong hệ thống? | `[...]` |
| Người bị ảnh hưởng có biết mình đang bị đánh giá không? Có đường phản hồi không? | `[...]` |
| Con số nào trên màn hình được dùng để ra quyết định thật? | `[...]` |
| Nếu một kết quả sai lọt ra ngoài, mất bao lâu để phát hiện? | `[...]` |

Ba tới năm câu trả lời gọn nhất sẽ thành danh sách rủi ro trọng tâm. Mọi case chạm vào chúng đều là `P0`, kể cả khi checklist chức năng xếp chúng thấp hơn.

---

<a name="b"></a>
## B. Đối tượng bị giám sát né hệ thống

> Giả định: người bị giám sát biết mình đang bị giám sát, và biết đại khái hệ thống tìm cái gì.

### B.1. Né ở tầng chữ

- Viết chệch từ khóa: chèn dấu cách, dấu chấm, gạch nối giữa các chữ cái
- Thay chữ bằng ký tự nhìn giống nhưng khác mã
- Viết không dấu, viết tắt, viết lóng, dùng từ đồng nghĩa
- Chèn ký tự ẩn hoặc ký tự không chiều rộng vào giữa từ khóa
- Đặt nội dung vi phạm trong ảnh thay vì trong chữ
- Đặt nội dung ở phần bình luận của chính mình thay vì trong bài
- Với mỗi cách trên: hệ thống bắt được hay không. Bắt không được thì **không phải lỗi cần sửa ngay**, nhưng phải được ghi lại thành giới hạn đã biết của hệ thống, để người ra quyết định không tin quá vào con số

### B.2. Né ở tầng nguồn

- Đăng ở nguồn không nằm trong danh sách giám sát
- Đăng rồi xóa nhanh trước giờ chạy của vòng quét: kiểm hệ thống có bắt kịp không, và đây là lỗ hổng cố hữu của việc quét theo lịch
- Chuyển tài khoản sang riêng tư trong khoảng thời gian có nội dung nhạy cảm rồi mở lại
- Đăng bằng tài khoản chưa khai báo với hệ thống
- Sửa nội dung sau khi hệ thống đã thu về, để bản lưu khác bản đang hiển thị công khai

### B.3. Làm nhiễu theo hướng ngược lại

- Tạo lượng lớn nội dung vô hại để làm loãng tỉ lệ vi phạm, nếu chỉ số có yếu tố tỉ lệ
- Dùng từ khóa loại trừ để đẩy nội dung ra khỏi phạm vi thu thập, nếu người bị giám sát tác động được vào cấu hình
- Người khác cố ý đăng nội dung nhắc tên một hồ sơ để đẩy điểm hồ sơ đó lên: kiểm hệ thống có phân biệt nội dung do chính chủ đăng với nội dung người khác nhắc tới không. Không phân biệt được là lỗ hổng bị lợi dụng để hại người khác, ưu tiên `P0`

---

<a name="c"></a>
## C. Người trong hệ thống làm lệch kết quả

> Mục 9 của tầng 0 kiểm người không có quyền bị chặn. Mục này kiểm người **có quyền** dùng quyền sai.

- Người kiểm duyệt hạ điểm một nội dung xuống thấp nhất: làm được, nhưng **phải để lại dấu vết đầy đủ** gồm giá trị cũ, giá trị mới, người thực hiện, thời điểm, lý do
- Sửa đi sửa lại nhiều lần: mọi lần đều để lại dấu vết, không lần nào bị đè mất
- Sửa rồi trả về đúng giá trị ban đầu: vẫn phải thấy được là đã có người động vào
- Từ chối một nội dung mà không nêu lý do: bị chặn
- Xóa hoặc vô hiệu hóa một từ khóa để một nhóm nội dung không còn bị bắt: được ghi nhật ký, và truy được ra những nội dung bị ảnh hưởng
- Tắt giám sát của một hồ sơ: ghi nhật ký kèm người thực hiện, và có cách phát hiện hồ sơ nào bị tắt lâu bất thường
- Người xử lý chính là người có quan hệ với đối tượng: hệ thống có cách phát hiện hoặc chặn không. Không có thì đây là rủi ro quy trình, ghi vào note để bên nghiệp vụ quyết
- Một người vừa ra quyết định vừa xử lý khiếu nại cho chính quyết định đó: kiểm có chặn không
- Sửa dữ liệu ngay trước thời điểm chốt số liệu kỳ: kiểm số liệu kỳ có bị ảnh hưởng không, và có ai biết không
- Người bị thu quyền vẫn còn phiên đang mở: mọi thao tác ghi bị chặn ở tầng máy chủ

---

<a name="d"></a>
## D. Quy kết oan và quyền của người bị ảnh hưởng

- Nội dung của người khác bị gắn vào hồ sơ này: đi ngược từ một nội dung bất kỳ, kiểm nó thuộc đúng hồ sơ. Bắc cầu sang `QA-Identity-Account-Linking-Checklist.md` Mục B và D
- Nội dung hợp lệ bị chấm là vi phạm do khớp từ khóa trong ngữ cảnh vô hại: chọn vài nội dung có từ khóa nhưng nghĩa ngược lại, kiểm hệ thống xử lý ra sao và người duyệt có đủ thông tin để sửa không
- Một hồ sơ có điểm cao bất thường: truy ngược ra được chính xác những nội dung nào tạo nên con số đó, và những từ khóa nào đã khớp
- Người bị đánh giá xem được cơ sở của kết quả, nếu đặc tả cho phép: các con số đưa ra khớp với dữ liệu thật
- Người bị đánh giá gửi khiếu nại: luồng chạy đúng, có thời hạn xử lý, và kết quả khiếu nại phản hồi ngược lại đúng chỗ. Bắc cầu sang `QA-AI-Assisted-Review-Checklist.md` Mục I
- Khiếu nại được chấp nhận: kết quả cũ được sửa, điểm và thứ hạng cập nhật theo, và **hậu quả của lần chấm sai không còn lưu lại** ở bất kỳ màn nào
- Kết quả trong quá khứ bị ghi đè mỗi kỳ: không đối chiếu lại được khiếu nại cũ. Ghi thành phát hiện trong note
- Hồ sơ mới chưa đủ dữ liệu: không bị xếp vào nhóm xấu nhất chỉ vì thiếu dữ liệu
- Hồ sơ được giám sát nhiều nguồn hơn hồ sơ khác: kiểm chỉ số có bị lệch theo số nguồn không

---

<a name="e"></a>
## E. Khối lượng công việc của người xử lý

> Nhóm định lượng cho persona. Đây là `Manual only`, và vẫn là `P0` khi sai sót của người xử lý gây hậu quả cho người thật.

- Đo **thời gian xử lý một bản ghi** từ lúc mở tới lúc ra quyết định, với người chưa quen hệ thống và với người đã quen
- Đo **số thao tác** cần cho một bản ghi. Số thao tác thừa là nguyên nhân trực tiếp của việc làm ẩu
- Xử lý liên tiếp 50 bản ghi: đo tỉ lệ thao tác nhầm, và kiểm hệ thống có chỗ nào khiến người dùng bấm nhầm theo quán tính không
- Nút mang hậu quả nặng, ví dụ từ chối, có nằm ngay cạnh nút thông thường không. Nằm cạnh thì đo tỉ lệ bấm nhầm
- Bấm nhầm rồi: có đường sửa lại không, mất bao lâu, có để lại dấu vết gì không
- Người xử lý có đủ thông tin trên một màn để ra quyết định không, hay phải mở thêm màn khác. Phải mở thêm thì đếm số lần mở
- Hàng chờ rất dài: người xử lý biết mình đang ở đâu, còn bao nhiêu, và quay lại được chỗ đang dở sau khi rời đi
- Người xử lý rời đi giữa chừng rồi quay lại: bản ghi đang dở ở trạng thái nào, và dữ liệu đã nhập còn không
- Đo tỉ lệ bản ghi được xử lý trong thời gian ngắn bất thường, ví dụ dưới vài giây: đây là chỉ dấu của việc bấm cho xong, và hệ thống nên đo được

---

<a name="f"></a>
## F. Thao tác đối kháng trên giao diện

- Bấm nút xử lý **nhiều lần thật nhanh liên tiếp**: chỉ ghi nhận một lần, không tạo bản ghi trùng và không ghi nhiều mốc lịch sử. Ưu tiên `P0`
- Bấm nút lưu nhiều lần khi mạng chậm
- Mở hai tab cùng một bản ghi rồi xử lý ở cả hai
- Bấm quay lại của trình duyệt giữa lúc đang xử lý, rồi thao tác tiếp
- Đóng trình duyệt giữa lúc đang lưu: kiểm dữ liệu ở trạng thái nào, không được nửa vời
- Sửa tham số trên đường dẫn để mở bản ghi mình không có quyền: bị chặn ở tầng máy chủ
- Gọi thẳng API để thực hiện thao tác mà giao diện đã ẩn nút: bị chặn. Đây là case bắt buộc cho **mọi** nút bị ẩn theo quyền hoặc theo trạng thái
- Gửi giá trị ngoài khoảng cho phép qua API, bỏ qua kiểm tra của giao diện
- Gửi thao tác lên một bản ghi đang ở trạng thái không cho phép thao tác đó
- Tải lại trang liên tục trên màn có số liệu nặng
- Để màn hình mở rất lâu rồi thao tác: phiên hết hạn được xử lý đúng, không mất dữ liệu một cách im lặng

---

<a name="g"></a>
## G. Đầu vào độc hại từ nội dung bên ngoài

> Nội dung trong hệ thống do người ngoài viết. Họ viết được bất cứ thứ gì, và hệ thống hiển thị lại nguyên văn.

- Nội dung chứa mã kịch bản: hiển thị dưới dạng chữ, không được thực thi ở bất kỳ màn nào, gồm danh sách, chi tiết, tệp xuất ra. Ưu tiên `P0`
- Nội dung chứa mã đánh dấu làm vỡ bố cục
- Nội dung chứa đường dẫn tới nơi độc hại: mở ở tab mới và có cảnh báo rời khỏi hệ thống, nếu đặc tả quy định
- Nội dung rất dài, một từ rất dài không có khoảng trắng: không phá bố cục
- Tên tài khoản hoặc nghệ danh chứa ký tự đặc biệt: hiển thị đúng ở mọi nơi, gồm cả tệp xuất ra
- Nội dung chứa chuỗi trông giống câu lệnh của hệ thống hoặc giống một mẫu thông báo: không bị hiểu nhầm thành lệnh
- Tệp xuất ra chứa nội dung bắt đầu bằng ký tự làm phần mềm bảng tính hiểu thành công thức: bị xử lý an toàn
- Ảnh từ nguồn ngoài: không tải trực tiếp theo cách làm lộ thông tin người xem, nếu đặc tả quy định phải lưu lại

---

<a name="h"></a>
## H. Dựng lại hiện trường

> Câu hỏi kiểm tra cuối cùng: ba tháng sau, có ai hỏi *"vì sao hồ sơ này bị đánh giá như vậy"*, hệ thống trả lời được không.

- Chọn một hồ sơ bất kỳ, dựng lại đầy đủ: điểm hiện tại gồm những nội dung nào, mỗi nội dung khớp từ khóa nào, ai đã duyệt, ai đã sửa gì
- Chọn một nội dung bất kỳ, truy ngược ra vòng quét đã mang nó vào và bộ quy tắc đã dùng để chấm nó
- Chọn một thay đổi quy tắc trong nhật ký, truy ra những nội dung bị ảnh hưởng
- Kết quả trong quá khứ còn xem lại được sau khi dữ liệu đã đổi nhiều lần
- Nhật ký không bị ghi đè, không bị xóa, kể cả bởi vai trò cao nhất
- Nhật ký lưu đủ lâu theo quy định, và có cách xuất ra khi cần giải trình
- Nhật ký không chứa dữ liệu nhạy cảm vượt phạm vi cho phép
- Thời điểm trong nhật ký dùng thống nhất một múi giờ, không lẫn lộn

---

## Tự review, điểm yếu và khuyến nghị

### Điểm mạnh

- Đây là file duy nhất trong bộ chống **sai trọng tâm** thay vì chống sót, và nó bổ khuyết đúng chỗ các checklist chức năng không với tới.
- Mục C đặt ra một câu hỏi mà bộ checklist cũ không hỏi bao giờ: người có quyền dùng quyền sai thì hệ thống thấy được không.
- Mục E biến persona từ một câu khẩu hiệu thành các phép đo cụ thể, đo được và lặp lại được.
- Bảng luật nâng bậc ở đầu file dùng được như tiêu chí quyết định `P0` cho toàn bộ dự án, không riêng file này.

### Điểm yếu còn lại

- Mục B không thể liệt kê hết cách né. Người né luôn sáng tạo hơn checklist. Mục này nên được cập nhật lại sau mỗi lần phát hiện cách né mới trong vận hành thật.
- Mục C chạm tới vấn đề quy trình nhiều hơn vấn đề kỹ thuật. Kiểm thử chỉ chứng minh được hệ thống có ghi dấu vết hay không, còn việc có ai đọc dấu vết đó không thì nằm ngoài phạm vi.
- Mục E cần người thật tham gia và cần thời gian, nên rất dễ bị cắt khi tiến độ gấp. Cắt thì phải ghi rõ là đã cắt, không lặng lẽ bỏ.
- Chưa phủ khía cạnh mô hình học máy bị tác động có chủ đích qua dữ liệu đầu vào, vì phần đó chỉ áp dụng cho hệ thống có học lại từ dữ liệu vận hành.

### Khuyến nghị

- Chạy Mục A **trước tiên**, trước cả khi mở các file checklist khác. Danh sách rủi ro trọng tâm quyết định thứ tự ưu tiên của toàn bộ phần còn lại.
- Mục F nên chạy sớm, ngay khi có bản chạy được, vì lỗi của nhóm này thường nằm ở kiến trúc và sửa muộn rất đắt.
- Mục H nên chạy một lần ở giai đoạn cuối như một bài tập dựng lại hiện trường trọn vẹn, thay vì tách thành nhiều case rời. Làm được trọn vẹn thì mới kết luận là hệ thống truy vết được.
- Kết quả của Mục B và E phần lớn không phải lỗi cần sửa, mà là **giới hạn đã biết**. Ghi chúng vào file ghi chú và báo cho bên nghiệp vụ, đừng để chúng biến mất chỉ vì không mở được phiếu lỗi.
