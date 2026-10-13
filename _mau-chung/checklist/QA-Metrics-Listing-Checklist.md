# Checklist Kiểm thử Số liệu Tổng hợp và Màn Danh sách Dữ liệu

### File tầng 3. Áp dụng khi màn hình có **thẻ số liệu tổng hợp, bộ chọn kỳ, và bảng dữ liệu mà các con số phải khớp nhau**. Phủ luôn phần tìm kiếm tiếng Việt và cuộn tải thêm

---

## Quan hệ với các file khác

| File | Phạm vi | Quan hệ với file này |
|---|---|---|
| `Testcase_Template.md` | Nền tảng chung | **Kế thừa toàn bộ** |
| `Testcase_Template.md` Mục 4 (bộ lọc và tìm kiếm) | Lọc, tìm, sắp xếp, phân trang | **Được mở rộng bởi file này.** Mục 4 phủ phân trang theo số trang, không phủ **cuộn tải thêm**, và phần tìm kiếm chỉ ở mức chung, không có biến thể tiếng Việt |
| `Testcase_Template.md` Mục 5.2 (trường số) | Nhập số và ràng buộc | **Khác phạm vi.** Mục 5.2 lo số người dùng nhập vào, file này lo **số hệ thống tính ra rồi hiển thị**, gồm rút gọn và làm tròn |
| `Testcase_Template.md` Mục 12.4 (nhất quán dữ liệu) | Cùng dữ liệu ở nhiều nơi | **Được mở rộng bởi Mục D** của file này |
| `QA-Ranking-Leaderboard-Checklist.md` Mục B | Kỳ dữ liệu của bảng xếp hạng | **Bắc cầu.** Quy tắc kỳ ở đây áp cho mọi màn danh sách, file kia áp riêng cho bảng xếp hạng. Hai nơi phải dùng cùng một định nghĩa kỳ |
| `QA-Data-Crawling-Checklist.md` Mục G | Múi giờ và mốc thời gian | **Bắc cầu.** Kỳ tính sai vì múi giờ thì lỗi nằm ở file kia |
| **File này** | **Bộ chọn kỳ · thẻ số liệu · rút gọn và làm tròn số hiển thị · nhất quán giữa thẻ, cột và màn chi tiết · tìm kiếm tiếng Việt · cuộn tải thêm** | |

### Nguyên tắc bao trùm

> **Giả định nền tảng:** người dùng tin con số trên màn hình hơn tin mọi thứ khác, và họ kiểm tra nó bằng cách tự cộng các dòng lại rồi so với thẻ tổng.
>
> Hệ quả kiểm thử: nhóm case giá trị nhất của file này không phải "thẻ hiện đúng số", mà là **"thẻ, cột trong bảng, và màn chi tiết có cùng nói một con số không"**. Lệch nhau là mất niềm tin, và mất niềm tin thì không sửa được bằng một bản vá.
>
> Ba chỗ làm số lệch mà không ai ngờ:
>
> 1. **Thẻ và bảng tính trên hai phạm vi khác nhau.** Thẻ tính toàn hệ thống, bảng tính trong bộ lọc đang đặt, mà giao diện không nói rõ.
> 2. **Số rút gọn che mất khác biệt.** Hai dòng cùng hiện `1.2K` nhưng một bên là 1180, một bên là 1249, và sắp xếp lại theo số rút gọn.
> 3. **Kỳ dữ liệu không được nói rõ.** Thẻ không phụ thuộc kỳ nằm cạnh thẻ phụ thuộc kỳ, người dùng đọc cả bốn thẻ như cùng một kỳ.

---

## Mẫu danh sách test case

Dùng bảng thống nhất quy định trong `CLAUDE.md` Mục 4.2, theo `Testcase_Template.md` Mục 24, bỏ 2 cột Automation:

| ID | Mục đích kiểm thử | Tiền điều kiện | Các bước thực hiện | Kết quả mong muốn | Kết quả thực tế | Mức độ ưu tiên | Ghi chú | Mã SRS |
|---|---|---|---|---|---|---|---|---|
| TC-[Mã]-001 | [Mô tả] | [Tiền điều kiện] | 1. …<br>2. … | [Kết quả chi tiết] | | P0 | | [Mã yêu cầu] |

- Case chạm vào **số lệch giữa hai nơi · số sai do làm tròn · sắp xếp sai do số rút gọn** được nâng lên `P0`.
- Kết quả mong muốn ghi **con số cụ thể**, không viết là hiển thị đúng.
- Tiền điều kiện ghi rõ **tập dữ liệu mẫu và số thật của từng dòng**, vì phần lớn case là so số.

---

## Mục lục

- [A. Bảng thông tin cần xác định trước khi viết case](#a)
- [B. Bộ chọn kỳ dữ liệu](#b)
- [C. Thẻ số liệu tổng hợp](#c)
- [D. Nhất quán giữa thẻ, bảng và màn chi tiết](#d)
- [E. Hiển thị số: rút gọn, làm tròn, ngăn cách](#e)
- [F. Tìm kiếm tiếng Việt](#f)
- [G. Cuộn tải thêm](#g)
- [H. Sắp xếp trên bảng có số tính ra](#h)
- [I. Hiệu năng và dữ liệu lớn](#i)
- [J. Dữ liệu cũ và chỉ báo thời điểm cập nhật](#j)

---

<a name="a"></a>
## A. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo đặc tả) |
|---|---|
| Có mấy lựa chọn kỳ, mỗi lựa chọn là khoảng nào? | `[ví dụ: 7 ngày qua, 30 ngày qua, chọn ngày]` |
| Khoảng tính từ mốc nào: từ 0 giờ của ngày đầu, hay từ đúng giờ này của N ngày trước? | `[...]` |
| Ngày hôm nay có nằm trong khoảng không? | `[...]` |
| Thẻ nào phụ thuộc kỳ, thẻ nào không? | `[liệt kê từng thẻ]` |
| Chọn ngày mà mới nhập một mốc thì tính trên phạm vi nào? | `[...]` |
| Thẻ tính trên toàn hệ thống hay trong phạm vi bộ lọc đang đặt? | `[...]` |
| Quy tắc rút gọn số: từ ngưỡng nào, mấy chữ số thập phân, làm tròn theo hướng nào? | `[...]` |
| Thẻ nào hiển thị số nguyên đầy đủ, thẻ nào rút gọn? | `[...]` |
| Ô tìm kiếm tìm trên những trường nào? | `[...]` |
| Tìm tương đối hay tìm chính xác? Có bỏ dấu tiếng Việt không? | `[...]` |
| Mỗi đợt tải thêm lấy bao nhiêu bản ghi? | `[con số]` |
| Số liệu là số thời gian thực hay số của lần quét gần nhất? | `[...]` |

> ⚠ Bốn ô bắt buộc: **mốc bắt đầu của khoảng**, **thẻ nào phụ thuộc kỳ**, **thẻ tính trong hay ngoài bộ lọc**, **quy tắc rút gọn số**. Thiếu thì Mục B, C, D, E chưa viết được case.

---

<a name="b"></a>
## B. Bộ chọn kỳ dữ liệu

### B.1. Đổi kỳ

- Đổi từ kỳ mặc định sang kỳ ngắn hơn: các thẻ phụ thuộc kỳ và các cột số liệu đều tính lại, thẻ không phụ thuộc kỳ giữ nguyên. Case ghi rõ con số trước và sau
- Đổi kỳ: bộ lọc và từ khóa tìm kiếm **được giữ nguyên**, bảng về trang một
- Đổi kỳ: thứ tự sắp xếp đang đặt được giữ hay bị đặt lại. Phải nhất quán, và case phải chốt một hướng
- Kỳ đang chọn hiển thị rõ trên giao diện, người dùng không phải đoán
- Mở lại màn sau khi rời đi: kỳ trở về mặc định hay nhớ lựa chọn cũ

### B.2. Biên của khoảng thời gian

- Bản ghi có mốc thời gian **đúng tại đầu khoảng**: kiểm được tính vào hay bị loại. Mỗi đầu một case
- Bản ghi có mốc **đúng tại cuối khoảng**, tức là đúng thời điểm hiện tại
- Bản ghi tạo ra **hôm nay**: kiểm kỳ 7 ngày qua có bao gồm hôm nay không
- Bản ghi cũ hơn kỳ dài nhất: không xuất hiện ở bất kỳ kỳ nào, nhưng vẫn phải xem được ở màn chi tiết nếu đặc tả cho
- Kiểm kỳ tính theo ngày lịch hay theo 24 giờ tròn. Hai cách cho hai kết quả khác nhau, và người dùng luôn hiểu theo ngày lịch

### B.3. Chọn ngày tùy ý

- Nhập đủ hai mốc hợp lệ: số liệu tính đúng trong khoảng đó
- Mới nhập một mốc: xử lý đúng theo đặc tả, và giao diện làm rõ đang thiếu mốc nào
- Ngày bắt đầu **sau** ngày kết thúc: bị chặn kèm thông báo rõ ràng
- Ngày bắt đầu bằng ngày kết thúc: tính đúng một ngày đó, không ra rỗng
- Chọn khoảng ở tương lai: xử lý hợp lý, không lỗi và không hiện số âm
- Chọn khoảng rất dài, ví dụ vài năm: vẫn tải được, hoặc có giới hạn rõ ràng kèm thông báo
- Chọn khoảng không có bản ghi nào: hiện trạng thái không có kết quả lọc, thẻ số liệu hiện 0 chứ không để trống
- Đang ở chế độ chọn ngày rồi bấm sang kỳ có sẵn: hai ô ngày ẩn đi và giá trị đã nhập được xóa hay giữ lại

---

<a name="c"></a>
## C. Thẻ số liệu tổng hợp

- Mỗi thẻ có dòng mô tả nói rõ nó đếm cái gì, người dùng không phải đoán
- Thẻ **không phụ thuộc kỳ** nằm cạnh thẻ phụ thuộc kỳ: giao diện phải phân biệt được hai loại. Không phân biệt được thì ghi thành phát hiện trong note, vì đây là chỗ người dùng hiểu sai nhiều nhất
- Hệ thống không có bản ghi nào: mọi thẻ hiện 0, không để trống và không hiện dấu gạch
- Dữ liệu chỉ có một bản ghi: thẻ hiện đúng 1
- Thẻ đếm theo điều kiện, ví dụ chỉ đếm bản ghi đã duyệt: thêm một bản ghi chưa duyệt thì thẻ **không** tăng. Đây là case bắt buộc, vì đây là chỗ số hay sai nhất
- Bản ghi bị từ chối: không được tính vào thẻ
- Bản ghi quay lại hàng chờ: thẻ cập nhật theo hướng đã chốt ở `QA-AI-Assisted-Review-Checklist.md` Mục E
- Thẻ tính trong phạm vi bộ lọc hay ngoài: đặt bộ lọc rồi kiểm thẻ có đổi không, đúng theo ô đã chốt ở Mục A. Nếu thẻ không đổi theo bộ lọc thì giao diện phải nói rõ, không thì người dùng cộng dòng rồi thắc mắc

---

<a name="d"></a>
## D. Nhất quán giữa thẻ, bảng và màn chi tiết

> Nhóm sinh nhiều báo lỗi từ người dùng thật nhất. Họ tự cộng các dòng rồi so với thẻ.

- Cộng tay giá trị của một cột trên toàn bộ các trang, so với thẻ tổng tương ứng: khớp. Lệch thì phải giải thích được bằng phạm vi tính, và giao diện phải nói ra
- Số bản ghi ghi ở chân bảng khớp với số dòng đếm được qua hết các trang
- Số của một dòng trong bảng khớp với số ở màn chi tiết của chính bản ghi đó, trong cùng kỳ
- Đổi kỳ rồi mở màn chi tiết: màn chi tiết có mang theo kỳ đang chọn không, hay tự quay về kỳ mặc định. Không mang theo thì người dùng so hai con số ở hai kỳ khác nhau mà không biết
- Cùng một bản ghi nhìn từ hai màn khác nhau: mức phân loại, nhãn trạng thái, badge màu đều giống nhau
- Xuất dữ liệu ra tệp: nội dung khớp đúng với những gì đang hiển thị, kể cả khi đang lọc và đang ở một kỳ cụ thể
- Hai người mở cùng một màn ở hai phiên khác nhau, cùng bộ lọc và cùng kỳ: thấy cùng con số

---

<a name="e"></a>
## E. Hiển thị số: rút gọn, làm tròn, ngăn cách

- Giá trị **ngay dưới ngưỡng rút gọn**, ví dụ 999: hiện nguyên số
- Giá trị **đúng tại ngưỡng**, ví dụ 1000: hiện dạng rút gọn đúng quy tắc
- Giá trị ngay trên ngưỡng, ví dụ 1001 và 1049 và 1050: kiểm làm tròn đúng hướng, mỗi mốc một case
- Các ngưỡng cao hơn: nghìn, triệu, tỉ, mỗi ngưỡng kiểm đủ ba mốc dưới, bằng, trên
- Giá trị 0 và giá trị âm nếu có: hiển thị đúng
- Số rất lớn: không tràn ô và không bị cắt
- Thẻ được quy định hiển thị nguyên số: có dấu ngăn cách nghìn đúng quy ước, và **không** bị rút gọn nhầm
- Hai bản ghi có số thật khác nhau nhưng số rút gọn giống nhau: kiểm thứ tự sắp xếp vẫn theo **số thật**. Đây là case bắt buộc, ưu tiên `P0`
- Di chuột hoặc mở chi tiết: có xem được số đầy đủ không, nếu đặc tả cho phép
- Cùng một giá trị hiển thị ở nhiều màn: dùng cùng một quy tắc rút gọn, không nơi rút gọn nơi không

---

<a name="f"></a>
## F. Tìm kiếm tiếng Việt

> Mục này chỉ viết được sau khi ô "tìm tương đối hay chính xác" ở Mục A có đáp.

- Nhập đúng nguyên văn một giá trị: tìm thấy
- Nhập **một phần** của giá trị, ở đầu, ở giữa, ở cuối: tìm thấy nếu là tìm tương đối
- Nhập **không dấu** để tìm giá trị có dấu, ví dụ gõ `Duong` tìm ra `Dương`: kiểm theo đúng đặc tả
- Nhập chữ `d` để tìm giá trị chứa `đ`: đây là trường hợp riêng, phải kiểm tách khỏi ca bỏ dấu thông thường
- Nhập **viết hoa toàn bộ** và **viết thường toàn bộ**: cùng kết quả
- Nhập có khoảng trắng thừa ở đầu và cuối: được bỏ trước khi tìm
- Nhập nhiều khoảng trắng giữa hai từ
- Nhập chuỗi rỗng hoặc chỉ có khoảng trắng: trở về danh sách đầy đủ, không phải danh sách rỗng
- Nhập ký tự đặc biệt, dấu phần trăm, dấu gạch dưới, dấu nháy: không làm lỗi truy vấn và không trả về toàn bộ dữ liệu. Ưu tiên `P0`
- Nhập chuỗi vượt giới hạn ký tự của ô
- Tìm theo mã bản ghi viết thường trong khi mã hệ thống viết hoa
- Tìm theo một trường thì các trường khác **không** khớp nhầm, và ngược lại phải khớp đủ mọi trường đã quy định
- Kết quả tìm kết hợp với bộ lọc đang đặt: chỉ còn bản ghi thỏa mãn hết
- Không có kết quả: hiện trạng thái không có kết quả lọc kèm đường đặt lại, phân biệt rõ với trạng thái không có dữ liệu

---

<a name="g"></a>
## G. Cuộn tải thêm

> Chỉ bật khi danh sách dùng nút tải thêm hoặc cuộn vô hạn thay cho phân trang.

- Bấm tải thêm: đợt tiếp theo **nối vào cuối**, phần đã hiện giữ nguyên, vị trí cuộn không nhảy
- Tải thêm nhiều lần liên tiếp tới hết dữ liệu: nút biến mất hoặc chuyển trạng thái đã hết, không bấm thêm được nữa
- Số bản ghi mỗi đợt đúng bằng con số đã quy định, đợt cuối có thể ít hơn
- Bấm tải thêm liên tục thật nhanh nhiều lần: không nạp trùng bản ghi và không bỏ sót đợt nào. Ưu tiên `P0`
- Lỗi xảy ra lúc tải thêm: **giữ nguyên phần đã hiện**, chỉ báo lỗi ở cuối danh sách kèm đường thử lại. Không thay cả danh sách bằng khối lỗi
- Thử lại sau lỗi: nối tiếp đúng chỗ đang dở, không nạp lại từ đầu
- Đổi bộ lọc sau khi đã tải nhiều đợt: danh sách về đợt đầu tiên của tập kết quả mới, không giữ lại bản ghi cũ
- Có bản ghi mới vào hệ thống trong lúc người dùng đang tải thêm: kiểm có bản ghi nào bị nhảy cóc hoặc lặp lại giữa hai đợt không. Đây là lỗi kinh điển của cuộn theo vị trí
- Mở một bản ghi rồi quay lại: danh sách giữ nguyên các đợt đã tải hay về đợt đầu. Về đợt đầu thì người dùng phải bấm lại nhiều lần, ghi thành phát hiện trong note
- Danh sách rất dài sau nhiều đợt: cuộn vẫn mượt, không đơ

---

<a name="h"></a>
## H. Sắp xếp trên bảng có số tính ra

- Sắp xếp theo mỗi cột cho phép: đúng thứ tự, kiểm cả hai chiều
- Bấm lần thứ hai trên cùng cột: đổi chiều. Bấm lần thứ ba: kiểm quay về chiều đầu hay về trạng thái không sắp xếp
- Cột sắp xếp mặc định khi mở màn đúng như đặc tả, và có chỉ báo trực quan
- Nhiều dòng cùng giá trị: thứ tự giữa chúng ổn định qua nhiều lần tải lại
- Dòng có giá trị trống hoặc bằng 0: xếp ở đầu hay cuối, nhất quán ở cả hai chiều
- Sắp xếp rồi đổi kỳ: số đổi thì thứ tự phải đổi theo, không giữ thứ tự cũ với số mới. Đây là case dễ sót
- Sắp xếp rồi chuyển trang: thứ tự vẫn liên tục qua các trang, không mỗi trang sắp riêng
- Sắp xếp kết hợp với bộ lọc và tìm kiếm

---

<a name="i"></a>
## I. Hiệu năng và dữ liệu lớn

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

- Mở màn danh sách ở quy mô dữ liệu nêu trên: trong ngưỡng
- Đổi kỳ sang khoảng dài nhất trên toàn bộ dữ liệu: trong ngưỡng
- Lọc ra tập kết quả rất lớn rồi sắp xếp: trong ngưỡng
- Tải thêm tới đợt thứ hai mươi: mỗi đợt vẫn trong ngưỡng, không chậm dần
- Cuộn danh sách đã tải nhiều đợt: không giật, không đơ
- Tên rất dài và số rất lớn: hiển thị gọn trong ô, không phá bố cục
- Mở màn đúng lúc vòng tính lại đang chạy: người dùng thấy dữ liệu nhất quán của một kỳ, không nửa cũ nửa mới

---

<a name="j"></a>
## J. Dữ liệu cũ và chỉ báo thời điểm cập nhật

- Màn có dòng ghi thời điểm cập nhật gần nhất: hiển thị đúng và đổi theo lần cập nhật **thành công** gần nhất
- Lần cập nhật gần nhất thất bại: dòng đó **không** đổi, người dùng nhận ra dữ liệu đang cũ
- Dữ liệu cũ quá một ngưỡng: có cảnh báo rõ hơn không, hay chỉ đổi mốc thời gian
- Mốc thời gian tương đối đổi đúng khi thời gian trôi qua, kiểm tại các mốc chuyển như từ hôm qua sang hôm kia
- Người dùng hiểu được số trên màn không phải số thời gian thực: giao diện phải nói ra chỗ nào đó, không để người dùng tự suy

---

## Tự review, điểm yếu và khuyến nghị

### Điểm mạnh

- Mục D đi đúng cách người dùng thật phát hiện lỗi, là tự cộng dòng rồi so với thẻ tổng. Không nhóm nào trong bộ checklist cũ làm việc này.
- Mục E bắt đúng một lỗi rất hay gặp mà rất khó thấy: sắp xếp theo số đã rút gọn thay vì số thật.
- Mục G phủ cuộn tải thêm, là thứ `Testcase_Template.md` Mục 4.5 không có vì mục đó viết cho phân trang theo số trang.
- Mục F đưa biến thể tiếng Việt thành case cụ thể thay vì để chung chung ở mức tìm kiếm theo từ khóa.

### Điểm yếu còn lại

- Chưa phủ biểu đồ. Màn có biểu đồ đường hoặc cột theo kỳ sẽ cần thêm một nhóm về trục thời gian, điểm dữ liệu trống, và việc biểu đồ khớp với bảng.
- Mục B giả định kỳ là khoảng lùi từ hiện tại. Hệ thống dùng kỳ cố định theo tháng hoặc quý sẽ cần thêm case về ranh giới tháng và về kỳ đang chạy dở.
- Ngưỡng hiệu năng ở Mục I là số theo thông lệ, chưa được BA xác nhận. Quy mô dữ liệu thật khác nhiều thì phải đo lại và chỉnh ngưỡng.
- Mục F chưa phủ trường hợp tìm kiếm có gợi ý tự động, vì phần đó thuộc hành vi của ô nhập chứ không thuộc kết quả tìm.

### Khuyến nghị

- Dựng một tập dữ liệu mẫu có chủ đích cho Mục D và E: vài bản ghi quanh mốc 999 và 1000, hai bản ghi cùng số rút gọn nhưng khác số thật, vài bản ghi nằm đúng biên của kỳ. Tập này chạy được phần lớn hai mục.
- Mục D nên viết case theo cặp hai màn trong cùng một case, thay vì tách ra. Tách thì không thấy chỗ lệch.
- Trước khi viết Mục C, chốt dứt điểm câu hỏi thẻ tính trong hay ngoài bộ lọc. Đây là chỗ dev và QA hay hiểu khác nhau cho tới lúc nghiệm thu.
