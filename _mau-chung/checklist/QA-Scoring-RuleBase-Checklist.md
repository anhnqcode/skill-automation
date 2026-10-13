# Checklist Kiểm thử Bộ Quy tắc và Chấm điểm

### File tầng 3. Áp dụng khi hệ thống **chấm điểm bản ghi theo một bộ quy tắc do người dùng cấu hình**, rồi dùng điểm đó để phân loại, cảnh báo hoặc xếp hạng

---

## Quan hệ với các file khác

| File | Phạm vi | Quan hệ với file này |
|---|---|---|
| `Testcase_Template.md` | Nền tảng chung | **Kế thừa toàn bộ.** Phần thêm sửa xóa quy tắc dùng Mục 3, 5, 10 của tầng 0, file này không viết lại |
| `Testcase_Template.md` Mục 14 (kiểm tra cấu hình) | Đổi cấu hình rồi kiểm hành vi | **Được mở rộng bởi file này.** Mục 14 kiểm cấu hình đổi thì màn hình hiện khác. Ở đây cấu hình đổi thì **dữ liệu lịch sử cũng có thể đổi theo**, đó là lớp rủi ro Mục 14 không có |
| `Testcase_Template.md` Mục 27 (xuyên module) | Dữ liệu chảy qua nhiều tầng | **Bắc cầu.** Chuỗi từ khóa tới nội dung tới hồ sơ tới bảng xếp hạng đúng là một luồng xuyên module |
| `Template_Testcase_Advanced.md` Mục C (ghép nối, gợi ý) | Thuật toán có yếu tố xác suất | **Loại trừ.** Mục C viết cho thuật toán không tất định, đánh giá bằng độ hợp lý. Bộ quy tắc ở đây là tất định, đánh giá bằng đúng sai. Bật cả hai sẽ sinh case mâu thuẫn |
| `QA-Data-Crawling-Checklist.md` | Thu thập dữ liệu về | **Bắc cầu.** File kia dừng khi bản ghi đã nằm trong hệ thống, file này bắt đầu từ đó |
| `QA-Ranking-Leaderboard-Checklist.md` | Xếp hạng theo kỳ | **Bắc cầu.** File này dừng ở điểm của một hồ sơ, file kia lo phần sắp thứ tự |
| **File này** | **Quy tắc khớp · cộng dồn · quan hệ nhóm quy tắc · hiệu lực hồi tố khi sửa quy tắc · ngưỡng phân loại · dồn điểm lên bản ghi cha · số học và làm tròn** | |

### Nguyên tắc bao trùm

> **Giả định nền tảng:** bộ quy tắc sẽ được sửa, và nó sẽ được sửa nhiều lần sau khi hệ thống đã chấm xong hàng nghìn bản ghi.
>
> Hệ quả kiểm thử: câu hỏi trung tâm của cả file không phải *"chấm đúng không"* mà là **"sửa quy tắc rồi thì dữ liệu cũ tính theo quy tắc nào"**. Hệ thống chỉ có hai lựa chọn, và cả hai đều có giá:
>
> - **Không tính lại:** cùng một từ khóa cho hai mức điểm khác nhau tùy bản ghi vào trước hay sau khi sửa. Bảng xếp hạng so hai hồ sơ bằng hai thước đo khác nhau.
> - **Tính lại toàn bộ:** điểm của bản ghi đã được người kiểm duyệt xác nhận bị máy đổi lại sau lưng, lịch sử xử lý mất ý nghĩa.
>
> Đặc tả phải chọn một, và case phải chứng minh hệ thống làm đúng cái đã chọn. Đặc tả chưa chọn thì đây là câu hỏi chặn, ghi vào note và hỏi BA trước khi viết Mục E.

---

## Mẫu danh sách test case

Dùng bảng thống nhất quy định trong `CLAUDE.md` Mục 4.2, theo `Testcase_Template.md` Mục 24, bỏ 2 cột Automation:

| ID | Mục đích kiểm thử | Tiền điều kiện | Các bước thực hiện | Kết quả mong muốn | Kết quả thực tế | Mức độ ưu tiên | Ghi chú | Mã SRS |
|---|---|---|---|---|---|---|---|---|
| TC-[Mã]-001 | [Mô tả] | [Tiền điều kiện] | 1. …<br>2. … | [Kết quả chi tiết] | | P0 | | [Mã yêu cầu] |

- Case chạm vào **điểm sai · phân loại sai mức rủi ro · dữ liệu lịch sử bị đổi ngầm** được nâng lên `P0`.
- Kết quả mong muốn của nhóm này phải là **một con số cụ thể**, không được viết kiểu tăng lên hoặc giảm đi. Không tính ra được con số thì case chưa viết được.
- Tiền điều kiện phải ghi rõ **bộ quy tắc tại thời điểm chạy case**, gồm danh sách từ khóa và điểm của từng từ. Thiếu phần này thì người sau chạy lại ra kết quả khác.

---

## Mục lục

- [A. Bảng thông tin cần xác định trước khi viết case](#a)
- [B. Quy tắc khớp từ khóa](#b)
- [C. Cộng dồn điểm trong một bản ghi](#c)
- [D. Quan hệ giữa bộ tiêu chí, tiêu chí và từ khóa](#d)
- [E. Hiệu lực khi sửa quy tắc](#e)
- [F. Xóa và vô hiệu hóa quy tắc](#f)
- [G. Ngưỡng phân loại mức rủi ro](#g)
- [H. Dồn điểm từ bản ghi con lên bản ghi cha](#h)
- [I. Số học: thập phân, làm tròn, giá trị biên](#i)
- [J. Phân quyền và nhật ký thay đổi quy tắc](#j)

---

<a name="a"></a>
## A. Bảng thông tin cần xác định trước khi viết case

| Câu hỏi | Trả lời (điền theo đặc tả) |
|---|---|
| Thang điểm của một quy tắc: từ bao nhiêu tới bao nhiêu, mấy chữ số thập phân? | `[...]` |
| Khớp từ khóa theo cách nào: đúng cả từ, một phần từ, hay theo mẫu? | `[...]` |
| Có phân biệt chữ hoa chữ thường không? | `[...]` |
| Có phân biệt dấu tiếng Việt không? | `[...]` |
| Một từ khóa xuất hiện nhiều lần trong một bản ghi tính mấy lần? | `[...]` |
| Một từ khóa có thuộc nhiều tiêu chí cùng lúc không? Nếu có thì tính điểm mấy lần? | `[...]` |
| Điểm cộng dồn có trần không? | `[...]` |
| Ngưỡng phân loại mức rủi ro của một bản ghi? | `[các con số, hoặc NEEDS REVIEW]` |
| Điểm của các bản ghi con dồn lên bản ghi cha theo công thức nào? | `[...]` |
| Một bản ghi được chấm mấy lần: một lần khi vào hệ thống, hay chấm lại mỗi lần quét? | `[...]` |
| Sửa điểm một quy tắc thì bản ghi đã chấm có tính lại không? | `[...]` |
| Xóa một quy tắc thì điểm đã cộng theo quy tắc đó xử lý ra sao? | `[...]` |
| Ai được sửa quy tắc? Có bước duyệt trước khi quy tắc có hiệu lực không? | `[...]` |

> ⚠ Bốn ô bắt buộc: **cách khớp**, **ngưỡng phân loại**, **sửa quy tắc có tính lại không**, **xóa quy tắc xử lý điểm cũ ra sao**. Thiếu bất kỳ ô nào thì phần lớn file này chưa viết được case, chỉ viết được câu hỏi vào note.

---

<a name="b"></a>
## B. Quy tắc khớp từ khóa

> Nhóm này chỉ viết được sau khi ô "cách khớp" ở Mục A có đáp. Đây là nhóm sinh ra nhiều lỗi thật nhất, vì đội phát triển thường chọn cách khớp đơn giản nhất mà không ai hỏi lại.

### B.1. Khớp cơ bản

- Bản ghi chứa đúng từ khóa, khớp và cộng điểm
- Bản ghi không chứa từ khóa, không khớp và không cộng điểm
- Bản ghi chứa từ khóa ở đầu câu, giữa câu, cuối câu, đều khớp như nhau
- Bản ghi chứa từ khóa ngay sát dấu câu, ví dụ liền dấu phẩy hoặc trong ngoặc kép, vẫn khớp

### B.2. Khớp một phần từ

- Từ khóa là một từ ngắn nằm bên trong một từ dài hơn, ví dụ từ khóa `lừa` trong chữ `lừa đảo` và trong chữ `con lừa`. Kiểm đúng theo cách khớp đã chốt, và đây là case bắt buộc dù chốt theo hướng nào
- Từ khóa có nhiều tiếng, bản ghi chứa các tiếng đó nhưng rời nhau và không liền kề, kiểm có khớp không
- Từ khóa nằm trong một đường dẫn hoặc trong tên tài khoản chứ không nằm trong phần chữ, kiểm phạm vi tìm có bao gồm phần đó không

### B.3. Hoa thường, dấu và biến thể chữ

- Từ khóa viết thường, bản ghi viết hoa toàn bộ
- Từ khóa có dấu, bản ghi viết không dấu, và ngược lại
- Bản ghi viết cách quãng giữa các chữ cái để né từ khóa, ví dụ chèn dấu chấm hoặc dấu cách giữa các ký tự. Kiểm hệ thống có xử lý hay không, và ghi rõ giới hạn vào note nếu không xử lý
- Bản ghi dùng ký tự nhìn giống nhưng khác mã, ví dụ chữ cái Latinh thay bằng chữ cái bảng khác
- Bản ghi có nhiều dấu cách liên tiếp hoặc xuống dòng giữa hai tiếng của từ khóa

### B.4. Từ khóa chồng lấn nhau

- Hai từ khóa mà từ này nằm trong từ kia, ví dụ `vi phạm` và `vi phạm nghiêm trọng`, bản ghi chứa cụm dài. Kiểm tính điểm của một từ hay của cả hai. Đây là case bắt buộc, ưu tiên `P0` vì nó quyết định điểm
- Hai từ khóa chồng lấn một phần trên cùng một đoạn chữ
- Bản ghi chứa đúng một cụm nhưng cụm đó khớp ba từ khóa của ba tiêu chí khác nhau

### B.5. Từ khóa loại trừ và thứ tự ưu tiên

> Bật khi hệ thống có cả từ khóa nhận diện lẫn từ khóa loại trừ, hoặc có hai lớp quy tắc ngược chiều nhau.

- Bản ghi khớp từ khóa nhận diện, không khớp loại trừ: vào hệ thống và được chấm điểm
- Bản ghi khớp **cả hai loại**: kiểm bên nào thắng, đúng theo đặc tả. Đây là case bắt buộc
- Bản ghi bị từ khóa loại trừ chặn: kiểm nó bị bỏ hẳn hay vẫn vào hệ thống với điểm bằng 0. Hai hướng cho hai ý nghĩa khác hẳn nhau
- Từ khóa loại trừ trùng chữ với một từ khóa chấm điểm: kiểm hệ thống xử lý ra sao, và cảnh báo khi cấu hình
- Thêm từ khóa loại trừ mới: bản ghi cũ vốn khớp nó có bị gỡ ra không, hay chỉ áp cho bản ghi mới
- Xóa hết từ khóa loại trừ: mọi bản ghi khớp nhận diện đều vào
- Chỉ có từ khóa loại trừ, không có từ khóa nhận diện: kiểm hành vi, không được lỗi
- Từ khóa loại trừ khớp một phần từ trong một từ dài hơn: cùng quy tắc khớp với Mục B.2, kiểm nhất quán giữa hai loại

### B.6. Đầu vào bất thường của từ khóa

- Tạo từ khóa chỉ gồm dấu cách, chỉ gồm dấu câu, hoặc rỗng: bị chặn khi tạo
- Tạo từ khóa rất ngắn, một ký tự: kiểm có chặn không, vì nó sẽ khớp gần như mọi bản ghi
- Tạo từ khóa rất dài, tới giới hạn trường nhập
- Tạo hai từ khóa giống hệt nhau trong cùng một tiêu chí: bị chặn theo Mục 3 của tầng 0
- Tạo hai từ khóa chỉ khác nhau ở khoảng trắng đầu cuối: kiểm có coi là trùng không

---

<a name="c"></a>
## C. Cộng dồn điểm trong một bản ghi

- Bản ghi khớp một từ khóa, điểm đúng bằng điểm từ khóa đó
- Bản ghi khớp ba từ khóa điểm 3, 4 và 5, điểm hiển thị đúng bằng 12.0. Viết case với con số cụ thể, không viết là tổng của ba từ
- Bản ghi khớp một từ khóa lặp lại năm lần, chỉ tính một lần, điểm không nhân lên
- Bản ghi không khớp từ khóa nào, điểm bằng 0 và hiển thị đúng chứ không để trống
- Bản ghi khớp rất nhiều từ khóa, kiểm điểm có chạm trần không. Nếu đặc tả nói không có trần thì viết case với số lớn để chứng minh không bị chặn ngầm ở tầng dữ liệu
- Số lần xuất hiện của từng từ khóa hiển thị trên giao diện khớp với số đếm thật trong phần chữ
- Từ khóa khớp được tô nổi bật đúng vị trí trong phần chữ, tô đủ mọi lần xuất hiện, và không tô nhầm sang chữ khác

---

<a name="d"></a>
## D. Quan hệ giữa bộ tiêu chí, tiêu chí và từ khóa

- Tạo bộ tiêu chí rỗng, chưa có tiêu chí nào: kiểm hành vi, không được lỗi
- Tạo tiêu chí chưa có từ khóa nào: bản ghi không bao giờ khớp tiêu chí đó, không lỗi
- Một từ khóa gán vào hai tiêu chí cùng lúc: kiểm điểm tính một lần hay hai lần. Đây là câu hỏi chặn, phải có đáp trước khi viết
- Một tiêu chí thuộc hai bộ tiêu chí: kiểm có cho phép không, và nếu có thì điểm tính ra sao
- Hồ sơ được cấu hình giám sát theo một bộ tiêu chí, từ khóa của bộ khác không được tính vào hồ sơ đó
- Đổi bộ tiêu chí của một hồ sơ sang bộ khác: kiểm các bản ghi đã chấm theo bộ cũ xử lý ra sao
- Một hồ sơ không được gán bộ tiêu chí nào: kiểm hành vi, bản ghi của hồ sơ đó có được chấm không

---

<a name="e"></a>
## E. Hiệu lực khi sửa quy tắc

> Nhóm trung tâm của cả file. Mỗi case dưới đây đều phải nêu rõ **trước khi sửa điểm là bao nhiêu, sau khi sửa điểm là bao nhiêu**, kiểm trên cả bản ghi cũ lẫn bản ghi mới.

### E.1. Sửa điểm của một từ khóa

- Sửa điểm từ khóa từ 3 lên 5. Bản ghi **thu về sau khi sửa** tính theo 5
- Cùng lúc đó, bản ghi **đã chấm trước khi sửa** giữ 3 hay đổi thành 5, theo đúng hướng đã chốt ở Mục A
- Nếu hệ thống không tính lại: kiểm giao diện có cách nào cho người dùng biết hai bản ghi đang dùng hai mức điểm khác nhau không. Không có thì ghi thành rủi ro trong note
- Nếu hệ thống có tính lại: kiểm phạm vi tính lại tới đâu, và điểm của hồ sơ cha có được cập nhật theo không
- Sửa điểm rồi sửa lại về giá trị cũ, kết quả trở lại đúng như ban đầu

### E.2. Thêm từ khóa mới

- Thêm từ khóa mới, bản ghi thu về sau đó khớp và cộng điểm
- Bản ghi cũ trong hệ thống vốn có chứa từ khóa vừa thêm: kiểm có được quét lại và cộng thêm điểm không
- Nếu bản ghi cũ được cộng thêm điểm và bản ghi đó đã qua bước kiểm duyệt: kiểm nó có quay lại hàng chờ không, bắc cầu sang `QA-AI-Assisted-Review-Checklist.md` Mục E

### E.3. Sửa nội dung một từ khóa

- Sửa chữ của từ khóa, kiểm điểm của bản ghi cũ vốn khớp từ khóa cũ xử lý ra sao. Đây là trường hợp dễ sinh dữ liệu mồ côi nhất
- Sửa từ khóa thành một từ đã tồn tại trong cùng tiêu chí, bị chặn vì trùng

### E.4. Thời điểm có hiệu lực

- Sửa quy tắc xong, kiểm hiệu lực **ngay lập tức** hay **từ vòng chạy kế tiếp**, theo đúng đặc tả
- Sửa quy tắc đúng lúc một vòng chạy đang diễn ra: kiểm các bản ghi trong vòng chạy đó dùng quy tắc cũ hay mới, và quan trọng hơn là **cả vòng chạy dùng nhất quán một bộ**, không nửa nọ nửa kia
- Hai người sửa hai từ khóa cùng lúc, cả hai thay đổi đều được ghi nhận, không cái nào đè cái nào

---

<a name="f"></a>
## F. Xóa và vô hiệu hóa quy tắc

- Xóa một từ khóa đang không có bản ghi nào khớp: xóa được bình thường
- Xóa một từ khóa đang có bản ghi khớp: kiểm hệ thống chặn, cảnh báo, hay cho xóa thẳng
- Cho xóa thẳng thì kiểm điểm đã cộng theo từ khóa đó **còn hay bị trừ ra**, và chip từ khóa trên bản ghi cũ hiển thị thế nào khi từ khóa không còn tồn tại
- Xóa một tiêu chí đang có từ khóa bên trong, và xóa một bộ tiêu chí đang được hồ sơ sử dụng: kiểm ràng buộc theo Mục 10 của tầng 0, và kiểm thêm phần điểm
- Có cơ chế vô hiệu hóa thay vì xóa thì kiểm riêng: quy tắc bị tắt không tính cho bản ghi mới, điểm cũ giữ nguyên, bật lại thì hoạt động trở lại
- Khôi phục một quy tắc đã xóa, nếu hệ thống hỗ trợ: điểm có được khôi phục theo không

---

<a name="g"></a>
## G. Ngưỡng phân loại mức rủi ro

> Không có con số ngưỡng thì cả nhóm này chưa viết được case, chỉ ghi câu hỏi vào note. Đây là loại thứ hai ở `CLAUDE.md` Mục 4.4.d.

- Điểm nằm **ngay tại** mỗi mốc ngưỡng: kiểm rơi vào mức nào. Ngưỡng ghi lớn hơn hay lớn hơn bằng phải rõ ràng, mỗi mốc một case
- Điểm nằm ngay dưới và ngay trên mỗi mốc, cách mốc đúng một đơn vị nhỏ nhất của thang điểm
- Điểm bằng 0, mức rủi ro hiển thị đúng chứ không để trống
- Điểm rất lớn vượt xa mốc cao nhất, vẫn xếp vào mức cao nhất chứ không lỗi
- Màu nền và nhãn của badge khớp đúng mức rủi ro ở mọi nơi hiển thị: danh sách, chi tiết, bảng xếp hạng. Cùng một bản ghi không được có hai màu ở hai màn
- Đổi ngưỡng trong cấu hình, kiểm các bản ghi đã có được phân loại lại theo ngưỡng mới hay giữ nguyên nhãn cũ

---

<a name="h"></a>
## H. Dồn điểm từ bản ghi con lên bản ghi cha

- Hồ sơ chưa có bản ghi con nào, điểm hiển thị đúng chứ không để trống và không lỗi
- Hồ sơ có một bản ghi con, điểm hồ sơ khớp đúng công thức đã chốt
- Hồ sơ có nhiều bản ghi con, tính tay ra con số rồi so với con số hệ thống hiển thị. Case phải ghi rõ con số đó
- Thêm một bản ghi con mới, điểm hồ sơ cập nhật đúng và cập nhật **vào thời điểm nào**: ngay lập tức hay theo vòng chạy
- Bản ghi con bị từ chối ở bước kiểm duyệt, điểm của nó **không** được tính vào hồ sơ
- Bản ghi con đã tính vào hồ sơ rồi quay lại hàng chờ, điểm hồ sơ có bị trừ ra trong lúc chờ không
- Người kiểm duyệt sửa điểm của một bản ghi con, điểm hồ sơ cập nhật theo điểm đã sửa chứ không theo điểm máy chấm
- Công thức có yếu tố thời gian, ví dụ chỉ tính bản ghi trong 30 ngày gần nhất: kiểm bản ghi rơi ra khỏi khoảng thì điểm hồ sơ tự giảm
- Số bản ghi và các số đếm hiển thị trên hồ sơ khớp với số bản ghi thật đang được tính điểm

---

<a name="i"></a>
## I. Số học: thập phân, làm tròn, giá trị biên

- Nhập điểm quy tắc ở đúng hai đầu thang, ví dụ 1 và 5: chấp nhận
- Nhập ngay ngoài hai đầu thang, ví dụ 0.9 và 5.1: bị chặn kèm đúng câu thông báo
- Nhập số âm, nhập chữ, nhập nhiều dấu chấm, dán một chuỗi dài vào ô điểm
- Nhập nhiều chữ số thập phân hơn mức cho phép: kiểm bị chặn hay bị làm tròn, và làm tròn theo hướng nào
- Cộng nhiều điểm lẻ, ví dụ 2.5 cộng 2.5 cộng 2.5, kết quả hiển thị đúng 7.5 chứ không ra số lẻ do sai số tính toán
- Điểm hiển thị đúng số chữ số thập phân đã quy định ở mọi màn, không nơi hiện 12 nơi hiện 12.0
- Điểm dùng để sắp xếp là điểm đầy đủ chứ không phải điểm đã làm tròn để hiển thị. Hai bản ghi hiện cùng 4.5 nhưng thực tế khác nhau thì thứ tự vẫn phải ổn định
- Tổng điểm rất lớn, kiểm không tràn và không bị cắt khi hiển thị

---

<a name="j"></a>
## J. Phân quyền và nhật ký thay đổi quy tắc

- Vai trò không có quyền sửa quy tắc: không thấy nút, và gọi thẳng API cũng bị từ chối. Ưu tiên `P0`
- Mọi thay đổi quy tắc ghi nhật ký gồm người thực hiện, thời điểm, giá trị trước và sau
- Từ một thay đổi trong nhật ký, truy được ra các bản ghi bị ảnh hưởng
- Có bước duyệt trước khi quy tắc có hiệu lực thì kiểm: quy tắc chờ duyệt chưa được đem ra chấm điểm
- Người dùng bị thu quyền trong lúc đang mở màn sửa quy tắc, bấm lưu thì bị từ chối ở tầng máy chủ

---

## Tự review, điểm yếu và khuyến nghị

### Điểm mạnh

- Đặt đúng trọng tâm vào Mục E, là chỗ mà mọi hệ thống chấm điểm theo cấu hình đều gãy, và không có file nào trong bộ hiện tại chạm tới.
- Buộc kết quả mong muốn phải là con số cụ thể và buộc tiền điều kiện phải ghi bộ quy tắc tại thời điểm chạy. Không có hai ràng buộc này thì case của nhóm chấm điểm chạy lại lần sau sẽ ra kết quả khác mà không ai biết vì sao.
- Mục B tách rõ các biến thể chữ, đây là nhóm mà đội phát triển hay bỏ qua và người dùng thật thì né từ khóa hằng ngày.

### Điểm yếu còn lại

- File giả định bộ quy tắc là danh sách phẳng gồm nhóm, tiêu chí và từ khóa. Hệ thống nào cho viết điều kiện kết hợp, ví dụ khớp từ này mà không khớp từ kia, sẽ cần thêm một nhóm về tổ hợp điều kiện.
- Chưa phủ trường hợp điểm do mô hình học máy sinh ra thay vì do quy tắc. Phần đó thuộc `QA-AI-Assisted-Review-Checklist.md`, nhưng ranh giới giữa hai file sẽ mờ nếu hệ thống trộn cả hai cách chấm.
- Chưa có nhóm về hiệu năng khi bộ quy tắc rất lớn, ví dụ vài nghìn từ khóa nhân với vài nghìn bản ghi mỗi vòng chạy.
- Mục G phụ thuộc hoàn toàn vào con số ngưỡng. Dự án chưa chốt ngưỡng thì cả mục này nằm ở trạng thái chờ tham số trong RTM.

### Khuyến nghị

- Dựng sẵn một bộ dữ liệu mẫu cố định gồm khoảng mười bản ghi với điểm đã tính tay, dùng chung cho mọi case của file này. Có nó thì mỗi lần sửa quy tắc chỉ cần chạy lại bộ mẫu là biết ngay hệ thống lệch chỗ nào.
- Case của Mục E nên chạy theo cặp: một bản ghi cũ và một bản ghi mới, kiểm cùng lúc trong một case. Tách ra hai case sẽ khó thấy chỗ hai bản ghi đang dùng hai thước đo khác nhau.
- Mục I nên verify ở tầng dữ liệu chứ không chỉ ở giao diện, vì sai số tính toán thường bị lớp hiển thị làm tròn che mất.
