# Checklist Kiểm thử Xếp hạng và Bảng Xếp hạng

### File tầng 3. Áp dụng khi hệ thống **sắp thứ tự các đối tượng theo một chỉ số tính được**, hiển thị thành bảng xếp hạng, và người dùng ra quyết định dựa trên thứ hạng đó

---

## Quan hệ với các file khác

| File | Phạm vi | Quan hệ với file này |
|---|---|---|
| `Testcase_Template.md` | Nền tảng chung | **Kế thừa toàn bộ.** Phần bộ lọc, tìm kiếm, phân trang của bảng xếp hạng dùng Mục 4, file này không viết lại |
| `Testcase_Template.md` Mục 12.4 (nhất quán dữ liệu) | Cùng một dữ liệu hiển thị nhiều nơi | **Được mở rộng bởi file này.** Bảng xếp hạng và màn chi tiết rất hay lệch nhau vì hai nơi tính theo hai mốc thời gian khác nhau |
| `Testcase_Template.md` Mục 28 (tác vụ theo thời gian) | Lịch chạy, kỳ dữ liệu | **Kế thừa.** Bảng xếp hạng theo kỳ là một dạng tác vụ theo lịch |
| `QA-Scoring-RuleBase-Checklist.md` | Chấm điểm theo bộ quy tắc | **Bắc cầu.** File kia lo điểm của một đối tượng đúng chưa, file này lo việc sắp thứ tự các điểm đó |
| `Template_Testcase_Advanced.md` Mục C.2 (công bằng trong phân phối) | Công bằng của thuật toán | **Bắc cầu một phần** nếu thứ hạng ảnh hưởng tới quyền lợi của đối tượng được xếp hạng |
| **File này** | **Kỳ dữ liệu và mốc tính · thứ tự và đồng hạng · top N thiếu dữ liệu · so sánh giữa hai kỳ · đối tượng vào và ra khỏi phạm vi · nhất quán giữa bảng và chi tiết** | |

### Nguyên tắc bao trùm

> **Giả định nền tảng:** bảng xếp hạng là một bức ảnh chụp tại một mốc thời gian, không phải số liệu thời gian thực. Người dùng thì luôn đọc nó như số thời gian thực.
>
> Hệ quả kiểm thử: hai câu hỏi phải trả lời được cho mọi bảng xếp hạng.
>
> 1. **Bảng này tính trên khoảng thời gian nào, và tính lúc mấy giờ.** Không trả lời được thì mọi case so sánh đều vô nghĩa, vì chạy hai lần ra hai kết quả mà không ai biết đúng sai.
> 2. **Hai đối tượng bằng điểm thì ai đứng trên.** Không có quy tắc phụ thì thứ tự sẽ nhảy mỗi lần tải lại, người dùng thấy ngay và mất niềm tin.
>
> Bảng xếp hạng dạng so sánh hai kỳ, ví dụ tăng mạnh nhất hoặc giảm mạnh nhất, có thêm một lớp rủi ro riêng: **đối tượng không có dữ liệu ở kỳ trước**. Xử lý sai chỗ này thì đối tượng mới vào hệ thống luôn đứng đầu bảng tăng mạnh nhất, và bảng đó thành vô dụng.

---

## Mẫu danh sách test case

Dùng bảng thống nhất quy định trong `CLAUDE.md` Mục 4.2, theo `Testcase_Template.md` Mục 24, bỏ 2 cột Automation:

| ID | Mục đích kiểm thử | Tiền điều kiện | Các bước thực hiện | Kết quả mong muốn | Kết quả thực tế | Mức độ ưu tiên | Ghi chú | Mã SRS |
|---|---|---|---|---|---|---|---|---|
| TC-[Mã]-001 | [Mô tả] | [Tiền điều kiện] | 1. …<br>2. … | [Kết quả chi tiết] | | P0 | | [Mã yêu cầu] |

- Case chạm vào **xếp sai thứ tự · số liệu lệch giữa hai màn · đối tượng bị xếp hạng oan** được nâng lên `P0`.
- Tiền điều kiện phải ghi rõ **tập dữ liệu mẫu và điểm của từng đối tượng**. Đây là nhóm case bắt buộc phải có dữ liệu dựng sẵn, không chạy được trên dữ liệu ngẫu nhiên.
- Kết quả mong muốn phải ghi **thứ tự cụ thể của các đối tượng**, không viết kiểu xếp đúng theo điểm giảm dần.

---

## Mục lục

- [A. Bảng thông tin cần xác định trước khi viết case](#a)
- [B. Kỳ dữ liệu và mốc tính](#b)
- [C. Thứ tự và đồng hạng](#c)
- [D. Top N và dữ liệu thiếu](#d)
- [E. Bảng so sánh giữa hai kỳ](#e)
- [F. Đối tượng vào và ra khỏi phạm vi xếp hạng](#f)
- [G. Nhất quán giữa bảng xếp hạng và các màn khác](#g)
- [H. Bộ lọc trên bảng xếp hạng](#h)
- [I. Dữ liệu lớn và hiệu năng](#i)
- [J. Công bằng và hệ quả với đối tượng được xếp hạng](#j)

---

<a name="a"></a>
## A. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo đặc tả) |
|---|---|
| Có mấy bảng xếp hạng, mỗi bảng sắp theo chỉ số nào? | `[...]` |
| Mỗi bảng tính trên khoảng thời gian nào? | `[ví dụ: 30 ngày gần nhất, hoặc từ đầu tới nay]` |
| Bảng tính lại vào lúc nào: thời gian thực, theo lịch, hay khi người dùng mở màn? | `[...]` |
| Hai đối tượng bằng điểm thì sắp theo quy tắc phụ nào? | `[...]` |
| Bảng hiển thị top bao nhiêu? Có xem được phần còn lại không? | `[con số]` |
| Điều kiện để một đối tượng được đưa vào xếp hạng? | `[ví dụ: đang được giám sát, và có ít nhất một bản ghi]` |
| Đối tượng chưa đủ dữ liệu tối thiểu thì xếp hạng hay để ngoài? | `[...]` |
| Bảng so sánh hai kỳ thì kỳ trước là khoảng nào? | `[...]` |
| Đối tượng không có dữ liệu ở kỳ trước thì tính mức tăng ra sao? | `[...]` |
| Thứ hạng có ảnh hưởng tới quyền lợi hoặc nghĩa vụ của đối tượng không? | `[...]` |
| Ai xem được bảng xếp hạng? Đối tượng có tự xem thứ hạng của mình không? | `[...]` |

> ⚠ Bốn ô bắt buộc: **khoảng thời gian**, **thời điểm tính lại**, **quy tắc phụ khi bằng điểm**, **đối tượng thiếu dữ liệu kỳ trước**. Thiếu thì Mục B, C, E chưa viết được case.

---

<a name="b"></a>
## B. Kỳ dữ liệu và mốc tính

- Bảng hiển thị rõ đang tính trên khoảng thời gian nào và tính vào lúc nào. Thiếu thông tin này trên giao diện thì ghi thành phát hiện trong note
- Thêm một bản ghi mới cho một đối tượng: kiểm bảng cập nhật **ngay** hay **chờ tới lần tính kế tiếp**, đúng theo đặc tả
- Nếu tính theo lịch: đúng mốc thì bảng được tính lại, kiểm bằng dữ liệu chứ không bằng cảm nhận
- Bản ghi có thời điểm **đúng tại biên** của khoảng thời gian, ví dụ đúng mốc 30 ngày trước: kiểm được tính vào hay bị loại, mỗi biên một case
- Bản ghi trôi ra ngoài khoảng theo thời gian: điểm của đối tượng giảm và thứ hạng tụt tương ứng, không cần thao tác gì thêm
- Đổi ngày trên máy chủ để mô phỏng sang kỳ mới: bảng chuyển kỳ đúng, kỳ cũ còn xem lại được hay mất
- Tải lại trang hai lần liên tiếp mà không có dữ liệu mới: thứ tự **giống hệt nhau**, không xáo trộn

---

<a name="c"></a>
## C. Thứ tự và đồng hạng

- Tập dữ liệu mẫu có điểm khác nhau rõ ràng: thứ tự đúng từ trên xuống, case ghi rõ thứ tự mong muốn
- Hai đối tượng **bằng điểm chính xác**: thứ tự theo đúng quy tắc phụ đã chốt, và tải lại nhiều lần vẫn giữ nguyên thứ tự đó
- Ba đối tượng trở lên cùng bằng điểm
- Hai đối tượng bằng nhau cả ở quy tắc phụ: phải còn một quy tắc phụ nữa để thứ tự ổn định, thường là mã định danh. Không có thì đây là lỗi thiết kế, ưu tiên `P0`
- Số thứ hạng hiển thị khi có đồng hạng: kiểm hai đối tượng cùng hạng 3 thì đối tượng kế tiếp là hạng 4 hay hạng 5. Quy tắc nào cũng được, miễn nhất quán và khớp đặc tả
- Đối tượng có điểm bằng 0: xếp cuối chứ không bị loại khỏi bảng, trừ khi đặc tả nói khác
- Điểm hiển thị đã làm tròn nhưng điểm thật khác nhau: thứ tự vẫn theo điểm thật. Case này bắc cầu sang `QA-Scoring-RuleBase-Checklist.md` Mục I
- Bảng sắp theo chỉ số giảm dần và bảng sắp theo chỉ số tăng dần, nếu hệ thống có cả hai, đều đúng ở hai đầu

---

<a name="d"></a>
## D. Top N và dữ liệu thiếu

- Hệ thống có nhiều hơn N đối tượng đủ điều kiện: bảng hiện đúng N, và có đường xem phần còn lại nếu đặc tả quy định
- Hệ thống có **ít hơn N** đối tượng: bảng hiện hết số đang có, không để dòng trống và không hiện dòng giả
- Hệ thống có **đúng N** đối tượng
- Hệ thống **chưa có đối tượng nào** đủ điều kiện: hiện trạng thái không có dữ liệu đúng theo quy ước chung, không hiện bảng rỗng có tiêu đề cột lơ lửng
- Chỉ có một đối tượng: bảng vẫn hiển thị đúng, các con số so sánh nếu có thì xử lý hợp lý
- Đối tượng ở ngay ranh giới vị trí thứ N và N cộng một, hai đối tượng đó bằng điểm: kiểm ai được vào bảng, và kết quả có ổn định qua nhiều lần tải không
- Đối tượng chưa đủ dữ liệu tối thiểu: xử lý đúng theo ô đã chốt ở Mục A, để ngoài bảng hoặc xếp cuối, và giao diện nói rõ lý do nếu để ngoài

---

<a name="e"></a>
## E. Bảng so sánh giữa hai kỳ

> Chỉ bật khi có bảng dạng tăng mạnh nhất, giảm mạnh nhất, hoặc có cột biến động so với kỳ trước.

- Đối tượng có dữ liệu ở **cả hai kỳ**: mức biến động tính đúng, case ghi rõ con số của cả hai kỳ và con số biến động mong muốn
- Đối tượng có dữ liệu ở kỳ này nhưng **không có ở kỳ trước**: kiểm tính ra sao. Đây là case bắt buộc, ưu tiên `P0`, vì cách tính sai làm cả bảng vô nghĩa
- Đối tượng có dữ liệu ở kỳ trước nhưng **không có ở kỳ này**: kiểm có nằm trong bảng giảm mạnh nhất không
- Đối tượng có điểm kỳ trước bằng 0: kiểm phép tính theo tỉ lệ có bị chia cho 0 không, và hệ thống hiển thị gì
- Hai đối tượng biến động bằng nhau: quy tắc phụ giống Mục C
- Biến động bằng đúng 0: xuất hiện ở bảng nào, hay không xuất hiện ở bảng nào
- Biến động âm trong bảng tăng mạnh nhất: bị loại khỏi bảng đó
- Kỳ trước là kỳ đầu tiên của hệ thống, chưa có dữ liệu nào: cả bảng so sánh xử lý đúng, không lỗi và không hiện số vô nghĩa
- Mũi tên và màu chỉ hướng biến động khớp đúng dấu của con số

---

<a name="f"></a>
## F. Đối tượng vào và ra khỏi phạm vi xếp hạng

- Đối tượng mới được thêm vào hệ thống: xuất hiện trong bảng ở lần tính kế tiếp, không sớm hơn
- Đối tượng bị ngừng giám sát giữa kỳ: rời bảng ngay hay ở lại tới hết kỳ, theo đúng đặc tả
- Đối tượng bị xóa: rời bảng, và thứ hạng của các đối tượng phía sau dồn lên đúng
- Đối tượng bị ngừng rồi bật lại trong cùng một kỳ: dữ liệu của khoảng thời gian tắt có được tính không
- Đối tượng đổi tên hoặc đổi ảnh đại diện: bảng hiện thông tin mới, thứ hạng không đổi
- Đối tượng có bản ghi bị từ chối ở bước kiểm duyệt: bản ghi đó **không** được tính vào điểm xếp hạng. Bắc cầu sang `QA-AI-Assisted-Review-Checklist.md` Mục E
- Đối tượng có bản ghi quay lại hàng chờ: điểm và thứ hạng xử lý đúng theo hướng đã chốt

---

<a name="g"></a>
## G. Nhất quán giữa bảng xếp hạng và các màn khác

> Đây là nhóm sinh ra nhiều báo lỗi từ người dùng thật nhất, vì họ tự so hai màn với nhau.

- Điểm của một đối tượng trên bảng xếp hạng khớp với điểm trên màn chi tiết của chính đối tượng đó. Lệch thì phải giải thích được bằng mốc thời gian tính, và giao diện phải nói rõ
- Số bản ghi hiển thị trên bảng khớp với số bản ghi thật đếm được ở màn chi tiết, trong cùng khoảng thời gian
- Mức rủi ro hiển thị trên bảng khớp với mức trên màn chi tiết và trên màn danh sách
- Bấm vào một dòng trong bảng: mở đúng đối tượng đó, không lệch dòng khi bảng đang có bộ lọc hoặc đang ở trang thứ hai
- Sửa dữ liệu ở màn chi tiết rồi quay lại bảng: kiểm bảng cập nhật theo mốc nào, và người dùng có bị hiểu nhầm là hệ thống quên mất thay đổi của mình không
- Xuất dữ liệu bảng xếp hạng ra tệp, nếu có chức năng đó: nội dung tệp khớp đúng thứ tự và con số đang hiển thị, kể cả khi đang lọc

---

<a name="h"></a>
## H. Bộ lọc trên bảng xếp hạng

- Lọc theo một điều kiện: bảng chỉ còn đối tượng khớp, và **số thứ hạng tính lại trong phạm vi lọc** hay **giữ nguyên thứ hạng toàn cục**. Đây là câu hỏi bắt buộc chốt với BA, hai cách cho hai ý nghĩa khác hẳn nhau
- Kết hợp nhiều điều kiện lọc cùng lúc
- Lọc ra tập rỗng: hiện trạng thái không có kết quả lọc kèm nút đặt lại, phân biệt rõ với trạng thái không có dữ liệu
- Đặt lại bộ lọc: bảng trở về đúng trạng thái ban đầu
- Đổi kỳ hoặc đổi chỉ số sắp xếp trong lúc đang lọc: bộ lọc được giữ hay bị xóa, phải nhất quán
- Bảng có nhiều trang: lọc xong thì về trang đầu, không để người dùng đứng ở trang 5 của một tập chỉ còn 2 dòng

---

<a name="i"></a>
## I. Dữ liệu lớn và hiệu năng


### Ngưỡng hiệu năng dùng cho file này

Đặc tả chưa ghi con số nào, nên bảng dưới đây là **số theo thông lệ của web quản trị nội bộ**, dùng để viết được kết quả mong muốn đo đếm được. Case ghi ở cột Ghi chú: `Ngưỡng theo thông lệ, chờ BA xác nhận`.

| Thao tác | Ngưỡng đề xuất | Đo thế nào |
|---|---|---|
| Mở màn danh sách, tới khi hiện đủ dữ liệu | 3 giây | Từ lúc bấm mục menu tới lúc bảng hiện dòng đầu tiên |
| Đổi bộ lọc, đổi kỳ, tìm kiếm | 2 giây | Từ lúc thả chuột tới lúc bảng cập nhật xong |
| Mở modal chi tiết | 2 giây | Từ lúc bấm tới lúc modal hiện đủ nội dung |
| Lưu một thao tác | 3 giây | Từ lúc bấm nút tới lúc hiện thông báo kết quả |
| Tải thêm một đợt | 2 giây | Từ lúc bấm tới lúc đợt mới hiện xong |
| Màn tổng hợp nặng, bảng xếp hạng | 5 giây | Như trên |
| Xuất tệp 10.000 dòng | 30 giây | Từ lúc bấm tới lúc tệp tải xong |

**Quy mô dữ liệu để đo:** 10.000 hồ sơ, 1.000.000 nội dung, 5.000 từ khóa. Quy mô thật khác nhiều thì đổi lại và ghi vào file ghi chú.

**Luật đọc kết quả:** quá ngưỡng dưới hai lần thì ghi là cảnh báo, quá từ hai lần trở lên thì mở phiếu lỗi. Đo ba lần lấy số ở giữa, không lấy lần nhanh nhất.

- Bảng với số lượng đối tượng ở quy mô nêu trên: trong ngưỡng 5 giây
- Đổi kỳ trên bảng đầy dữ liệu: trong ngưỡng
- Rất nhiều đối tượng cùng điểm: thứ tự vẫn ổn định và không chậm bất thường
- Tên đối tượng rất dài: hiển thị gọn trong ô, không phá bố cục bảng
- Con số rất lớn: hiển thị đúng quy ước ngăn cách, không tràn ô
- Mở bảng xếp hạng đúng lúc vòng tính lại đang chạy: người dùng thấy dữ liệu nhất quán của một kỳ, không thấy nửa cũ nửa mới

---

<a name="j"></a>
## J. Công bằng và hệ quả với đối tượng được xếp hạng

> Chỉ bật khi thứ hạng kéo theo hệ quả thật cho đối tượng, ví dụ bị cảnh báo, bị hạn chế, hoặc bị đưa vào diện theo dõi.

- Đối tượng mới vào hệ thống chưa đủ dữ liệu: không bị xếp vào nhóm xấu nhất chỉ vì thiếu dữ liệu
- Đối tượng có nhiều bản ghi hơn hẳn do được giám sát nhiều nguồn hơn: kiểm chỉ số có bị lệch theo số nguồn không, và đặc tả có chuẩn hóa không
- Một bản ghi bị chấm sai rồi được người duyệt sửa lại: thứ hạng cập nhật theo, không giữ hậu quả của lần chấm sai
- Đối tượng xem được cơ sở của thứ hạng mình, nếu đặc tả cho phép: các con số đưa ra khớp với dữ liệu thật
- Thứ hạng trong quá khứ được lưu lại hay bị ghi đè mỗi kỳ. Bị ghi đè thì không đối chiếu lại được khiếu nại cũ, ghi điểm này vào note
- Phân quyền xem bảng: vai trò không đủ quyền không xem được, kể cả gọi thẳng API

---

## Tự review, điểm yếu và khuyến nghị

### Điểm mạnh

- Mục C và E phủ hai chỗ mà bảng xếp hạng nào cũng gãy: đồng hạng không có quy tắc phụ, và đối tượng không có dữ liệu ở kỳ trước.
- Mục G viết theo đúng cách người dùng thật phát hiện lỗi, tức là tự so hai màn với nhau, thay vì chỉ kiểm từng màn riêng lẻ.
- Buộc kết quả mong muốn phải ghi thứ tự cụ thể, nhờ đó case chạy lại lần sau vẫn kiểm chứng được.

### Điểm yếu còn lại

- File giả định thứ hạng tính từ một chỉ số đơn. Bảng xếp hạng tổng hợp nhiều chỉ số có trọng số sẽ cần thêm một nhóm về trọng số và về việc đổi trọng số.
- Chưa phủ phần lưu lịch sử thứ hạng theo thời gian và vẽ biểu đồ xu hướng, nếu hệ thống có.
- Ngưỡng ở Mục I là số theo thông lệ, chờ BA xác nhận. Bảng xếp hạng tính lại theo lịch thì còn cần thêm ngưỡng cho chính vòng tính đó.
- Chưa có nhóm về việc cố tình tác động để đổi thứ hạng, phần này gần với Mục C.6 của `Template_Testcase_Advanced.md` và chỉ cần khi thứ hạng gắn với quyền lợi lớn.

### Khuyến nghị

- Dựng một tập dữ liệu mẫu cố định khoảng mười đối tượng, trong đó cố ý có hai cặp bằng điểm, một đối tượng điểm 0, một đối tượng không có dữ liệu kỳ trước. Tập này chạy được gần hết Mục C, D, E.
- Trước khi viết Mục H, chốt dứt điểm câu hỏi thứ hạng khi lọc là thứ hạng toàn cục hay thứ hạng trong phạm vi lọc. Đây là chỗ dev và QA hay hiểu khác nhau mà không ai phát hiện cho tới lúc nghiệm thu.
- Case của Mục B nên chạy được bằng cách can thiệp mốc thời gian. Không can thiệp được thì phần kiểm biên khoảng thời gian thành nhóm bị chặn, ghi rõ lý do trong RTM.
