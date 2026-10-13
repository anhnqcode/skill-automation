# Checklist Kiểm thử Thu thập Dữ liệu từ Nguồn Ngoài

### File tầng 3. Áp dụng khi hệ thống **tự động lấy dữ liệu về từ các nguồn bên ngoài** mà người dùng không kiểm soát được: mạng xã hội, trang tin, báo chí, sàn thương mại

---

## Quan hệ với các file khác

| File | Phạm vi | Quan hệ với file này |
|---|---|---|
| `Testcase_Template.md` | Nền tảng chung | **Kế thừa toàn bộ.** File này không thay thế mục nào |
| `Testcase_Template.md` Mục 12 (đồng bộ dữ liệu) | Đồng bộ giữa module nội bộ và hệ thống ngoài | **Được mở rộng bởi file này.** Mục 12 giả định nguồn ngoài là một hệ thống có hợp đồng dữ liệu rõ ràng. Nguồn thu thập thì không: dữ liệu đổi bất kỳ lúc nào và không ai báo trước |
| `Testcase_Template.md` Mục 28 (tác vụ theo thời gian) | Lịch chạy, đếm ngược, bù trigger lỡ | **Kế thừa.** Mục 28 phủ phần *khi nào chạy*, file này phủ phần *chạy xong ra dữ liệu gì* |
| `Template_Testcase_Advanced.md` Mục A (hàng đợi) | Đảm bảo gửi tin, thứ tự, hàng đợi lỗi | **Bắc cầu.** Nếu pipeline thu thập đẩy qua hàng đợi thì dùng Mục A cho tầng vận chuyển, file này cho tầng nội dung |
| `QA-Scoring-RuleBase-Checklist.md` | Chấm điểm nội dung theo bộ quy tắc | **Bắc cầu.** File này dừng ở chỗ nội dung đã nằm trong hệ thống. Từ đó trở đi là file kia |
| **File này** | **Định danh và trùng lặp nội dung · nội dung đổi ở nguồn · giới hạn và lỗi từ nguồn · chuẩn hóa dữ liệu thô · thời gian và múi giờ · tài khoản nguồn đổi trạng thái** | |

### Nguyên tắc bao trùm

> **Giả định nền tảng:** nguồn ngoài không có nghĩa vụ ổn định. Bài đăng bị sửa, bị xóa, bị ẩn. Tài khoản đổi tên, chuyển riêng tư, bị khóa. Nguồn đổi cấu trúc trả về mà không báo. Nguồn chặn khi gọi quá nhiều.
>
> Hệ quả kiểm thử: mọi case dạng *"thu thập được đúng nội dung trên nguồn"* mới chỉ là luồng thuận, và nó là phần nhỏ nhất. Phần lớn rủi ro nằm ở câu hỏi **"nguồn thay đổi thì hệ thống còn đúng không"**.
>
> Hai lỗi đắt nhất của lớp này: **đếm trùng** (một nội dung vào hệ thống hai lần rồi cộng điểm hai lần) và **im lặng khi hỏng** (một nguồn ngừng trả dữ liệu, giao diện vẫn hiện số cũ và không ai biết).

---

## Mẫu danh sách test case

Dùng bảng thống nhất quy định trong `CLAUDE.md` Mục 4.2, theo `Testcase_Template.md` Mục 24, bỏ 2 cột Automation:

| ID | Mục đích kiểm thử | Tiền điều kiện | Các bước thực hiện | Kết quả mong muốn | Kết quả thực tế | Mức độ ưu tiên | Ghi chú | Mã SRS |
|---|---|---|---|---|---|---|---|---|
| TC-[Mã]-001 | [Mô tả] | [Tiền điều kiện] | 1. …<br>2. … | [Kết quả chi tiết] | | P0 | | [Mã yêu cầu] |

- **Kết quả thực tế** để trống khi viết.
- Case chạm vào **đếm sai dữ liệu · mất dữ liệu · hỏng ngầm không ai biết** được nâng lên `P0`.
- **Ghi chú** của nhóm này thường phải nói rõ **verify ở đâu**, vì phần lớn case không nhìn thấy trên giao diện. Ghi cụ thể: bảng dữ liệu nào, log nào, endpoint nào.
- **Mã SRS** đặt sau cột Ghi chú, case QA tự bổ sung ghi `[QA-ADD]`.

---

## Mục lục

- [A. Bảng thông tin cần xác định trước khi viết case](#a)
- [B. Cấu hình nguồn và phạm vi thu thập](#b)
- [C. Định danh nội dung và chống trùng lặp](#c)
- [D. Nội dung thay đổi ở nguồn sau khi đã thu về](#d)
- [E. Giới hạn, chặn và lỗi từ phía nguồn](#e)
- [F. Chuẩn hóa dữ liệu thô](#f)
- [G. Thời gian: thời điểm đăng, thời điểm thu thập, múi giờ](#g)
- [H. Vòng chạy theo lịch, thử lại và bù dữ liệu](#h)
- [I. Tài khoản nguồn đổi trạng thái](#i)
- [J. Hiệu năng của vòng quét](#j)
- [K. Quan sát và đối soát](#k)

---

<a name="a"></a>
## A. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo đặc tả) |
|---|---|
| Danh sách nguồn thu thập, và mỗi nguồn lấy về những loại nội dung nào? | `[ví dụ: YouTube lấy video và bình luận, báo chí lấy bài viết]` |
| Cái gì định danh duy nhất một nội dung? | `[ví dụ: đường dẫn gốc, hoặc mã bài của nền tảng]` |
| Một lần chạy lấy về tối đa bao nhiêu nội dung mỗi nguồn, mỗi hồ sơ? | `[con số]` |
| Lấy nội dung trong khoảng thời gian nào tính từ thời điểm chạy? | `[ví dụ: 24 giờ gần nhất, hoặc từ lần chạy thành công gần nhất]` |
| Nội dung cũ hơn khoảng đó có bị bỏ qua vĩnh viễn không? | `[...]` |
| Nguồn có giới hạn số lần gọi không? Giới hạn bao nhiêu? | `[con số, hoặc NEEDS REVIEW]` |
| Dữ liệu tối thiểu phải có để một nội dung được nhận vào hệ thống? | `[ví dụ: phải có phần chữ và thời điểm đăng]` |
| Nội dung không đủ dữ liệu tối thiểu thì bỏ hay nhận với phần trống? | `[...]` |
| Nội dung đã thu về mà nguồn xóa đi thì xử lý ra sao? | `[...]` |
| Ai được cấu hình nguồn, ai được xem log thu thập? | `[...]` |

> ⚠ Ba ô bắt buộc phải có câu trả lời trước khi viết case: **định danh duy nhất**, **khoảng thời gian lấy về**, **nội dung bị xóa ở nguồn**. Thiếu bất kỳ ô nào thì không viết được kết quả mong muốn cho Mục C và D, phải hỏi BA trước.

---

<a name="b"></a>
## B. Cấu hình nguồn và phạm vi thu thập

### B.1. Bật tắt một nguồn

- Bật thêm một nguồn cho hồ sơ đang giám sát, chạy lần kế tiếp, nội dung của nguồn đó bắt đầu xuất hiện. Kiểm cả **mốc bắt đầu**: nguồn mới bật có lấy cả nội dung cũ trước thời điểm bật hay chỉ lấy từ đó về sau
- Tắt một nguồn, nội dung đã thu về từ nguồn đó **còn hay mất**, và điểm đã cộng cho hồ sơ có bị trừ đi không. Đây là câu hỏi nghiệp vụ, không có đáp đúng mặc định, phải chốt với BA
- Tắt rồi bật lại cùng một nguồn, nội dung trong khoảng thời gian tắt được bù về hay bỏ luôn
- Hồ sơ không bật nguồn nào, vòng chạy xử lý đúng, không lỗi và không tạo bản ghi rỗng

### B.2. Từ khóa nhận diện và từ khóa loại trừ

- Nội dung khớp từ khóa nhận diện thì vào, không khớp thì không vào
- Nội dung vừa khớp nhận diện vừa khớp loại trừ, kiểm rõ bên nào thắng
- Sửa từ khóa nhận diện, xác nhận **thời điểm có hiệu lực**: ngay lập tức hay từ lần chạy kế tiếp. Nội dung đã thu về theo từ khóa cũ có bị gỡ ra không
- Từ khóa để trống, kiểm hành vi: lấy tất cả hay không lấy gì

### B.3. Phân loại nội dung theo quan hệ với hồ sơ

> Bật khi hệ thống phân biệt nội dung **do chính chủ hồ sơ đăng** với nội dung **của người khác nhắc tới hồ sơ**. Hai loại này thường lên hai con số khác nhau, nên phân loại sai là số sai.

- Nội dung đăng từ tài khoản đã liên kết với hồ sơ: xếp vào nhóm do chính chủ đăng
- Nội dung của tài khoản khác có nhắc tên hồ sơ: xếp vào nhóm nhắc tới
- Nội dung do chính chủ đăng nhưng có nhắc tên mình: kiểm không bị đếm vào cả hai nhóm
- Bình luận của chính chủ dưới bài của người khác: thuộc nhóm nào
- Bài chia sẻ lại bài của người khác: thuộc nhóm nào
- Nội dung nhắc tới hai hồ sơ cùng lúc: đếm cho cả hai hay chỉ một
- Nội dung nhắc tên một người không có hồ sơ trong hệ thống: không tạo hồ sơ mới và không gắn nhầm vào hồ sơ trùng tên
- Đổi liên kết tài khoản của hồ sơ: các nội dung cũ có được phân loại lại không

### B.4. Phạm vi một lần chạy

- Số nội dung thực tế lấy về không vượt giới hạn mỗi lần chạy đã đặt
- Nguồn có nhiều nội dung hơn giới hạn, kiểm phần vượt ra bị **bỏ hẳn** hay **để dành cho lần sau**. Nếu bỏ hẳn thì đây là lỗ hổng mất dữ liệu, ưu tiên `P0`
- Nguồn trả về theo nhiều trang, hệ thống lấy hết các trang trong phạm vi, không dừng ở trang đầu

---

<a name="c"></a>
## C. Định danh nội dung và chống trùng lặp

> Nhóm quan trọng nhất của cả file. Trùng lặp ở đây không chỉ làm danh sách xấu, nó **cộng điểm hai lần** và làm sai toàn bộ xếp hạng phía sau.

### C.1. Trùng trong cùng một lần chạy

- Một nội dung xuất hiện hai lần trong cùng lượt trả về của nguồn, hệ thống chỉ tạo **một** bản ghi
- Cùng một nội dung được hai hồ sơ đối tượng giám sát cùng giám sát kéo về, kiểm rõ tạo một bản ghi dùng chung hay mỗi hồ sơ một bản ghi, và điểm cộng cho hồ sơ nào

### C.2. Trùng giữa các lần chạy

- Chạy hai lần liên tiếp trên cùng dữ liệu nguồn, lần hai **không** tạo thêm bản ghi mới và **không** cộng thêm điểm
- Ép chạy lại ngay sau một lần chạy thành công, kết quả giữ nguyên
- Chạy lại sau khi lần trước hỏng giữa chừng, phần đã thu về không bị nhân đôi

### C.3. Trùng khi định danh bị đổi

- Nguồn đổi đường dẫn của một nội dung nhưng vẫn là nội dung đó, hệ thống nhận ra là một hay coi là hai. Nếu định danh dựa trên đường dẫn thì đây là điểm gãy, ghi rõ vào note
- Cùng một bài được đăng lại trên nhiều trang tin khác nhau, mỗi bản là một bản ghi riêng hay gộp. Chốt với BA rồi mới viết
- Đường dẫn có tham số theo dõi ở đuôi khác nhau nhưng trỏ cùng một bài, hệ thống chuẩn hóa trước khi so sánh

### C.4. Gọi song song và chạy chồng

- Hai tiến trình cùng thu thập cho một hồ sơ tại một thời điểm, không tạo bản ghi trùng
- Vòng chạy hôm nay bắt đầu khi vòng hôm qua chưa xong, kiểm hệ thống chặn chạy chồng hay chấp nhận. Chấp nhận thì phải chứng minh không sinh trùng

---

<a name="d"></a>
## D. Nội dung thay đổi ở nguồn sau khi đã thu về

> Lớp case này gần như luôn bị bỏ sót, vì trên giao diện không có gì gợi ý nó tồn tại.

### D.1. Nội dung bị sửa

- Tác giả sửa phần chữ sau khi hệ thống đã thu về. Lần chạy sau, hệ thống **cập nhật** bản ghi hay **giữ nguyên bản đã lưu**
- Nếu cập nhật, kiểm điểm có chấm lại không, và phần chữ cũ có được lưu lại để đối chiếu không
- Nếu giữ nguyên, kiểm giao diện có nói rõ đây là nội dung tại thời điểm thu thập không, tránh người dùng mở bài gốc thấy khác rồi mất niềm tin
- Bài sửa xong khớp thêm từ khóa mới, kiểm nội dung có quay lại hàng chờ xử lý không

### D.2. Nội dung bị xóa hoặc ẩn ở nguồn

- Bài bị tác giả xóa, bản ghi trong hệ thống còn hay bị đánh dấu. Điểm đã cộng còn hay bị trừ
- Bài chuyển sang chế độ riêng tư, hệ thống không đọc được nữa, xử lý giống trường hợp xóa hay khác
- Nút mở bài gốc trỏ tới bài đã xóa, kiểm hành vi trên giao diện, không để người dùng bấm vào rồi gặp trang lỗi của nguồn mà không có lời giải thích

### D.3. Chỉ số tương tác thay đổi

- Lượt xem và lượt thích tăng sau khi thu về, kiểm số hiển thị là số tại thời điểm thu thập hay số cập nhật mới nhất. Giao diện phải nói rõ là số nào
- Chỉ số giảm xuống, ví dụ bài bị gỡ bớt bình luận, hệ thống nhận số giảm bình thường, không chặn và không giữ số cũ
- Nguồn không trả về một chỉ số nào đó, hiển thị dấu trống chứ không hiển thị số không

---

<a name="e"></a>
## E. Giới hạn, chặn và lỗi từ phía nguồn

### E.1. Vượt giới hạn gọi

- Ép hệ thống chạm ngưỡng giới hạn của nguồn, kiểm hệ thống dừng đúng cách và ghi log, không gọi tiếp trong vô vọng
- Nguồn trả về mã báo vượt giới hạn, hệ thống chờ đúng khoảng quy định rồi mới gọi lại
- Nhiều hồ sơ cùng dùng một nguồn, kiểm giới hạn được chia sẻ chứ không tính riêng từng hồ sơ dẫn tới vượt ngưỡng chung

### E.2. Nguồn trả về sai hoặc lạ

- Nguồn trả về cấu trúc khác với cấu trúc hệ thống mong đợi, kiểm hệ thống bỏ qua bản ghi hỏng và **vẫn xử lý các bản ghi còn lại**, không đổ cả lượt
- Nguồn trả về rỗng dù có dữ liệu, phân biệt được với trường hợp thật sự không có nội dung mới
- Nguồn trả về nội dung không thuộc hồ sơ đang quét, hệ thống loại bỏ
- Nguồn trả về rất chậm, hệ thống dừng theo ngưỡng chờ đã đặt và ghi nhận là lỗi chứ không treo

### E.3. Một nguồn hỏng, các nguồn khác

- Một nguồn hỏng, các nguồn còn lại của cùng hồ sơ vẫn cập nhật bình thường
- Một hồ sơ hỏng, các hồ sơ còn lại vẫn cập nhật bình thường
- Kiểm dữ liệu của hồ sơ lỗi **giữ nguyên số của lần chạy thành công gần nhất**, không về không và không hiện số sai

---

<a name="f"></a>
## F. Chuẩn hóa dữ liệu thô

### F.1. Ký tự và ngôn ngữ

- Nội dung chứa emoji, ký tự nhiều byte, chữ Hán, chữ Ả Rập: lưu và hiển thị đúng, không thành dấu hỏi và không cắt cụt giữa ký tự
- Nội dung chứa ký tự ẩn, ký tự điều khiển, xuống dòng nhiều lần: hiển thị gọn, không phá bố cục thẻ
- Nội dung chứa mã đánh dấu hoặc mã kịch bản: hiển thị dưới dạng chữ, không được thực thi. Ưu tiên `P0`
- Nội dung rất dài vượt giới hạn trường lưu trữ: cắt đúng quy tắc đã đặt, không mất bản ghi và không cắt giữa một ký tự nhiều byte
- Nội dung chỉ có ảnh, không có chữ: nhận vào hay bỏ, chốt với BA rồi viết

### F.2. Ảnh và tệp đính kèm

- Nội dung có ảnh, ảnh hiển thị đúng
- Nội dung không có ảnh, hiển thị khung ảnh mặc định
- Đường dẫn ảnh chết hoặc nguồn chặn tải ảnh, hiển thị khung mặc định chứ không để ô vỡ
- Ảnh rất lớn hoặc rất nhiều ảnh trong một nội dung, danh sách vẫn tải được trong ngưỡng chấp nhận

### F.3. Đường dẫn gốc

- Nội dung có đường dẫn gốc, nút mở bài gốc hiện ra và mở đúng ở tab mới
- Nội dung không có đường dẫn gốc, nút không hiện
- Đường dẫn chứa ký tự cần mã hóa, mở vẫn đúng bài

---

<a name="g"></a>
## G. Thời gian: thời điểm đăng, thời điểm thu thập, múi giờ

- Phân biệt rõ **thời điểm đăng** và **thời điểm thu thập** trên cả dữ liệu lẫn giao diện. Hai mốc này không được dùng lẫn nhau
- Nguồn trả thời điểm theo múi giờ khác, hệ thống quy về đúng múi giờ hiển thị
- Nguồn chỉ trả mốc tương đối kiểu vài giờ trước, hệ thống quy ra mốc tuyệt đối và ghi rõ cách quy
- Nội dung có thời điểm đăng nằm ở tương lai, hệ thống xử lý đúng chứ không làm hỏng thứ tự danh sách
- Nội dung không có thời điểm đăng, xếp ở đâu trong danh sách sắp theo thời gian
- Sắp xếp theo thời điểm đăng giảm dần vẫn đúng khi hai nội dung trùng mốc tới từng phút
- Vào ngày đổi giờ hoặc ngày nhuận, vòng chạy vẫn đúng một lần, không chạy hai lần và không bỏ

---

<a name="h"></a>
## H. Vòng chạy theo lịch, thử lại và bù dữ liệu

> Kế thừa `Testcase_Template.md` Mục 28 cho phần lịch. Phần dưới đây là phần Mục 28 không có.

- Đúng mốc chạy theo lịch, vòng chạy khởi động. Kiểm bằng log, không kiểm bằng giao diện
- Hệ thống dừng đúng lúc tới mốc chạy, vòng chạy đó được bù khi hệ thống lên lại hay bỏ luôn
- Thử lại đúng số lần và đúng khoảng giãn đã đặt. Kiểm cả mốc cuối: sau lần thử cuối vẫn lỗi thì dừng, không thử tiếp
- Thử lại ở mức **từng hồ sơ và từng nguồn**, không chạy lại cả lượt. Chứng minh bằng cách ép một hồ sơ lỗi rồi kiểm các hồ sơ khác không bị quét lại
- Lần thử thứ hai thành công, dừng thử tiếp và ghi nhận thành công
- Sau lần thử cuối thất bại, thông báo đi tới đúng vai trò nhận, qua đúng các kênh đã quy định, đúng một lần chứ không lặp
- Nội dung thông báo có đủ thời điểm chạy, nguồn lỗi, danh sách hồ sơ chưa cập nhật
- Nhiều hồ sơ cùng lỗi trong một lượt, kiểm gộp thành một thông báo hay bắn rời từng hồ sơ
- Dòng trạng thái máy quét trên giao diện đổi mốc thời gian theo lần quét **thành công** gần nhất, không đổi theo lần chạy lỗi

---

<a name="i"></a>
## I. Tài khoản nguồn đổi trạng thái

- Tài khoản mạng xã hội đổi tên hiển thị, hệ thống cập nhật tên mới và các nội dung cũ vẫn gắn đúng hồ sơ
- Tài khoản đổi định danh, kiểm hệ thống còn theo được hay coi như tài khoản mới
- Tài khoản chuyển sang riêng tư, ngừng thu thập và báo rõ trên giao diện, không im lặng
- Tài khoản bị nền tảng khóa hoặc xóa, hồ sơ trong hệ thống xử lý ra sao, nội dung cũ còn hay mất
- Một tài khoản bị gỡ khỏi hồ sơ đối tượng giám sát, nội dung đã thu về từ tài khoản đó và điểm đã cộng xử lý ra sao
- Cùng một tài khoản bị gán cho hai hồ sơ đối tượng giám sát khác nhau, hệ thống chặn hay chấp nhận

---

<a name="j"></a>
## J. Hiệu năng của vòng quét

Đặc tả chưa ghi con số, nên bảng dưới là **số theo thông lệ**, dùng để viết được kết quả mong muốn đo đếm được. Case ghi ở cột Ghi chú: `Ngưỡng theo thông lệ, chờ BA xác nhận`.

| Chỉ số | Ngưỡng đề xuất | Vì sao chọn số này |
|---|---|---|
| Một hồ sơ, một nguồn | 60 giây | Đủ để gọi nguồn và xử lý một đợt nội dung |
| Cả lượt quét toàn hệ thống | Xong trước 6 giờ sáng | Vòng chạy bắt đầu 0 giờ, người dùng vào làm việc từ khoảng 8 giờ, cần biên an toàn 2 giờ |
| Một lần thử lại | Không làm cả lượt trễ quá mốc trên | Ba lần thử giãn 5, 15, 45 phút cộng lại là 65 phút, phải nằm gọn trong cửa sổ 6 giờ |
| Độ trễ từ lúc hệ thống nguồn đẩy hồ sơ mới tới lúc hồ sơ hiện trên giao diện | 5 phút | Đặc tả nói là đẩy ngay, nên đây là ngưỡng của từ "ngay" |

**Quy mô để đo:** 10.000 hồ sơ, mỗi hồ sơ trung bình 4 nguồn.

- Chạy cả lượt ở quy mô nêu trên: xong trong cửa sổ cho phép
- Một phần ba số hồ sơ gặp lỗi và phải thử lại đủ ba lần: cả lượt vẫn xong trong cửa sổ. Đây là case quan trọng nhất của mục này, vì thử lại là thứ làm vỡ cửa sổ thời gian
- Một nguồn phản hồi rất chậm: không kéo cả lượt chậm theo, các hồ sơ khác vẫn xong
- Vòng chạy chưa xong mà tới mốc chạy của ngày hôm sau: xử lý đúng theo Mục C.4, và có cảnh báo cho người vận hành

---

<a name="k"></a>
## K. Quan sát và đối soát

> Không có nhóm này thì mọi case phía trên đều không verify được, vì lớp thu thập chạy ngầm.

- Mỗi vòng chạy để lại bản ghi nhật ký gồm thời điểm bắt đầu, thời điểm kết thúc, số hồ sơ xử lý, số nội dung thu về, số lỗi theo từng nguồn
- Từ một nội dung trên giao diện, truy ngược được về vòng chạy đã mang nó vào
- Đối soát thủ công: chọn một hồ sơ, đếm tay số bài trên nguồn trong khoảng thời gian, so với số hệ thống thu về. Đây là case thủ công bắt buộc, không tự động hóa được, ưu tiên `P0`
- Số liệu tổng trên giao diện khớp với số bản ghi thực có trong dữ liệu
- Nhật ký không ghi dữ liệu nhạy cảm của nguồn ra ngoài phạm vi cho phép

---

## Tự review, điểm yếu và khuyến nghị

### Điểm mạnh

- Phủ đúng hai lỗi đắt nhất của lớp thu thập là đếm trùng và hỏng ngầm, đây là hai chỗ mà bộ checklist tầng 0 hoàn toàn không chạm tới.
- Mục C và D viết theo hướng buộc người viết case phải đi hỏi BA, thay vì tự đoán một hành vi rồi viết ra case không ai kiểm chứng được.
- Mục K bắt buộc mọi case phải nói được cách verify, khớp với yêu cầu về khả năng quan sát ở `CLAUDE.md` Mục 8.d.

### Điểm yếu còn lại

- File giả định mỗi nội dung là một bản ghi độc lập. Hệ thống nào gom nội dung thành chuỗi hội thoại, ví dụ bài đăng kèm chuỗi bình luận trả lời nhau, sẽ cần thêm một nhóm về quan hệ cha con giữa các nội dung.
- Chưa phủ phần kiểm chất lượng của bộ phân loại nguồn, tức là hệ thống nhận diện đúng một trang là báo chí hay trang tin.
- Ngưỡng ở Mục J là số theo thông lệ, chờ BA xác nhận. Quy mô thật khác nhiều thì phải tính lại cửa sổ thời gian.
- Chưa có nhóm về khía cạnh pháp lý của việc lưu lại nội dung bên thứ ba, phần này phụ thuộc quy định của từng dự án.

### Khuyến nghị

- Trước khi viết case theo file này, điền cho xong bảng Mục A. Ba ô đánh dấu bắt buộc mà còn trống thì Mục C và D chưa viết được.
- Case của Mục C nên viết ở mức dữ liệu chứ không ở mức giao diện, vì trùng lặp nhiều khi không hiện ra trên danh sách do giao diện đã lọc.
- Nhóm case Mục D nên chạy trên môi trường có tài khoản nguồn do đội test tự kiểm soát, để chủ động sửa và xóa bài. Không có tài khoản như vậy thì cả Mục D thành nhóm bị chặn, phải ghi rõ lý do trong RTM.
