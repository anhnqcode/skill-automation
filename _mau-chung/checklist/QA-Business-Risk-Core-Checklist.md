# Checklist rủi ro nghiệp vụ chung (tầng 1)

File tầng 1 trong bộ checklist sinh testcase. Áp dụng cho **mọi domain**, chạy sau `Testcase_Template.md` (tầng 0, phần giao diện và dữ liệu) và trước các checklist năng lực `QA-*` (tầng 2) và bộ domain (tầng 3).

Mục đích: tầng 0 hỏi "ô nhập, nút, danh sách có chạy đúng không". File này hỏi "nghiệp vụ có sai ở chỗ gây thiệt hại không": tiền, mốc thời gian, trạng thái, tư cách, kết quả cuối, quyền quyết định, dữ liệu cá nhân, bằng chứng. Mỗi nhóm có **dấu hiệu trong tài liệu** để tự bật, **câu hỏi** để suy ra case từ tài liệu đặc tả, **case mẫu** và **quy tắc nâng mức ưu tiên**.

---

### Cách dùng

1. Đọc tài liệu của chức năng, dò bảng **Dấu hiệu trong tài liệu** của từng nhóm. Thấy từ khóa thì bật nhóm đó.
2. Với mỗi nhóm được bật, trả lời từng câu hỏi bằng quy tắc lấy từ SRS, FSD, CR. Câu nào tài liệu không trả lời được thì ghi vào file ghi chú làm câu hỏi chặn, không viết kết quả mong muốn đoán mò.
3. Mỗi câu trả lời sinh một hoặc vài case. Case nào khớp **quy tắc nâng mức ưu tiên** của nhóm thì để High.
4. Phần riêng của domain (mục 2) chạy sau, ở bộ checklist domain.

### Năm nguyên tắc dùng cho mọi nhóm

1. **Máy chủ quyết định, giao diện chỉ hiển thị.** Mọi thao tác bị chặn trên giao diện phải có thêm case gửi thẳng lên máy chủ. Ẩn nút hay khóa ô không chứng minh được gì.
2. **Không có con số thì chưa viết được kết quả mong muốn.** Case chạm tiền, điểm, mốc thời gian phải có số cụ thể trong tiền điều kiện và kết quả.
3. **Kết quả mong muốn theo tài liệu mới nhất đã duyệt và theo hệ thống thật.** Văn bản luật, thông lệ ngành chỉ để hiểu bối cảnh. Tài liệu lệch nhau thì ghi vào file ghi chú.
4. **Ghi cả cái đổi lẫn cái không đổi.** Lỗi hay lọt nhất là thứ lẽ ra giữ nguyên lại đổi theo.
5. **Biết sai hướng nào nặng hơn.** Trước khi viết case, xác định với chức năng này thì bỏ sót hay bắt nhầm, cấp thiếu hay cấp thừa, ghi thiếu hay ghi trùng gây thiệt hại lớn hơn, rồi dồn case vào hướng nặng hơn.

### Danh sách nhóm

| # | Nhóm rủi ro |
|---|---|
| 1 | Giá trị và tiền: thu, giữ, hoàn, mất |
| 2 | Mốc thời gian, hạn và tác vụ chạy theo lịch |
| 3 | Vòng đời trạng thái và khóa theo giai đoạn |
| 4 | Tính toán, cộng dồn, làm tròn và số liệu khớp nhau |
| 5 | Điều kiện tham gia, tư cách và mất tư cách |
| 6 | Xác định kết quả cuối, đề xuất của máy và quyết định của người |
| 7 | Duyệt nhiều cấp, ký và quyền quyết định |
| 8 | Thao tác đồng thời, lặp lại và tranh chấp tài nguyên |
| 9 | Tích hợp hệ thống ngoài và nguồn dữ liệu |
| 10 | Gắn đúng chủ thể: trùng, gộp, quy nhầm |
| 11 | Văn bản, tệp sinh ra, tệp xuất và chứng từ |
| 12 | Dữ liệu cá nhân, hiển thị theo vai trò và phạm vi dữ liệu |
| 13 | Nhật ký, bằng chứng và dựng lại sự việc |
| 14 | Cấu hình, tham số và đổi quy tắc giữa chừng |
| 15 | Gian lận, lạm quyền và thông đồng |
| 16 | Thông báo nghiệp vụ |
| 17 | Vận hành hệ thống: mã tự sinh, danh mục có hiệu lực, hạn mức, triển khai, di chuyển dữ liệu, sao lưu |

---

### Nhóm 1. Giá trị và tiền: thu, giữ, hoàn, mất

**Dấu hiệu trong tài liệu:** thanh toán, chuyển khoản, QR, cổng thanh toán, ví, số dư, đặt cọc, tiền đặt trước, ký quỹ, phí, lệ phí, hoàn tiền, hoàn cọc, mất cọc, phạt, khấu trừ, công nợ, đối soát, hóa đơn, VAT, hoa hồng, điểm thưởng, voucher, tín dụng.

**Câu hỏi suy ra case:**
1. Khi khoản tiền về đúng số tiền và đúng mã tham chiếu thì hệ thống ghi nhận trong bao lâu, ghi ở những nơi nào, và các nơi đó có khớp nhau không?
2. Khi khoản tiền về thiếu dù một đồng, thừa, hoặc chia làm nhiều lần cho đủ tổng thì hệ thống xử lý thế nào, và có chắc là **không** tự ghi nhận sai không?
3. Khi cùng một khoản được báo về hai lần, đến sai thứ tự, hoặc báo về mà không có chữ ký hợp lệ thì hệ thống có ghi nhận hai lần hoặc ghi nhận khoản giả không?
4. Khi mã tham chiếu thuộc khoản khác, người khác, đơn khác thì hệ thống có gắn nhầm tiền sang khoản đó không?
5. Khi tiền về sau hạn, hoặc người dùng chuyển trước hạn mà bên ngân hàng ghi nhận sau hạn, thì hệ thống tính theo mốc nào?
6. Khi tiền về lúc giao dịch đã bị hủy, hồ sơ đã bị từ chối, hoặc đã ghi nhận đủ rồi thì hệ thống làm gì với khoản đó?
7. Khi người nội bộ cập nhật tay trạng thái tiền, cập nhật nhầm người, hoặc cập nhật đúng lúc đối soát tự động đang chạy thì có bị ghi hai lần không, có để lại dấu vết không?
8. Khi một bên bị phạt, mất tiền, bị khấu trừ thì mỗi lý do có được xử lý riêng không, và người **không** vi phạm có chắc không bị trừ oan ở mọi nhánh kết thúc không?
9. Khi giao dịch bị hủy, dừng, hoặc không thành thì ai được hoàn, hoàn bao nhiêu, ai tự đổi trạng thái hoàn, trạng thái đó có bị khóa không?
10. Khi số tiền phải trả được tính từ nhiều khoản (giá cuối trừ khoản đã nộp, phí cơ bản cộng phần trăm) thì con số có đúng ở mọi đơn vị tính không?
11. Khi tổng tiền trên báo cáo được đối chiếu với tổng giao dịch gốc trong kỳ thì hai bên có khớp không, và mỗi dòng báo cáo có truy ngược được ra giao dịch gốc không?
12. Khi người dùng yêu cầu xóa tài khoản lúc còn tiền đang giữ hoặc nghĩa vụ chưa xong thì hệ thống chặn hay xử lý ra sao, dữ liệu giao dịch có bị xóa theo không?

**Case mẫu:**
- Khoản chuyển thiếu 1 đồng so với số tiền yêu cầu. Kết quả: trạng thái giữ nguyên Chưa nộp, giao dịch vẫn hiện ở lịch sử để người nội bộ xử lý, không nơi nào báo đã nộp. Ví dụ ở sàn đấu giá là tiền đặt trước, ở sàn thương mại điện tử là đơn hàng trả trước.
- Cổng thanh toán báo cùng một giao dịch hai lần cách nhau 10 giây. Kết quả: số tiền đã nộp chỉ tăng một lần, lịch sử có một dòng ghi nhận và một dòng ghi bỏ qua trùng.
- Phiên giao dịch bị hủy khi đã có ba người nộp tiền giữ chỗ. Kết quả: không ai bị đặt trạng thái mất tiền, cả ba ở trạng thái chờ hoàn theo đúng quy tắc.

**Quy tắc nâng mức ưu tiên:** mọi case làm ghi nhận sai số tiền, ghi hai lần, hoàn sai người, trừ oan, hoặc không trừ khi đúng ra phải trừ đều là High.

**Kỹ thuật đã có ở:** Template_Testcase_Advanced Mục E (cổng thanh toán, webhook, đối soát).

---

### Nhóm 2. Mốc thời gian, hạn và tác vụ chạy theo lịch

**Dấu hiệu trong tài liệu:** hạn, hết hạn, thời hạn, mốc, giờ mở, giờ đóng, đếm ngược, gia hạn, kéo dài, cộng thêm, trước X phút, trong vòng, ngày làm việc, ngày lễ, theo kỳ, hằng ngày, 0 giờ, tự động công bố, tự động đóng, lịch chạy, chu kỳ, tần suất, bù dữ liệu.

**Câu hỏi suy ra case:**
1. Khi các mốc của một đối tượng bị đặt sai thứ tự, bằng nhau, hoặc nằm trong quá khứ thì hệ thống chặn ở đâu, kể cả khi gửi thẳng lên máy chủ?
2. Khi một mốc phụ thuộc mốc khác (hạn nộp bằng hạn đăng ký) thì đổi mốc gốc có kéo mốc phụ theo không, và gửi hai mốc lệch nhau lên máy chủ thì sao?
3. Khi thao tác xảy ra ở giây trước mốc, đúng mốc, và giây sau mốc thì kết quả có nhất quán qua nhiều lần chạy không?
4. Khi mốc kết thúc được kéo dài theo hành vi của người dùng thì điều kiện mở thêm, độ dài, số lần tối đa, và cách đếm có đúng không? Hai loại kéo dài đan xen thì bộ đếm có bị reset nhầm không?
5. Khi giờ máy người dùng chạy nhanh hoặc chậm thì hệ thống có vẫn tính theo giờ máy chủ không, và case đã ghi rõ đang so với giờ nào chưa?
6. Khi hạn tính theo ngày làm việc thì hệ thống có bỏ qua cuối tuần và ngày lễ không, lịch nghỉ lấy từ đâu?
7. Khi tác vụ tự động chạy đúng mốc thì nó chạy trong bao lâu, chạy mấy lần, và có xét lại đối tượng đã xử lý không?
8. Khi máy chủ dừng qua mốc rồi chạy lại thì tác vụ có chạy bù không, và chạy bù có làm sai đối tượng đã đổi trạng thái trong lúc dừng không?
9. Khi người dùng thao tác tay đúng lúc tác vụ tự động đang chạy trên cùng đối tượng thì hệ thống có xử lý hai lần không?
10. Khi tác vụ tự động gặp đối tượng thiếu dữ liệu bắt buộc thì nó bỏ qua, báo lỗi, hay xử lý dở dang?
11. Khi bộ đếm theo ngày hoặc theo kỳ sang ngày mới thì cái gì về 0, cái gì phải giữ nguyên?
12. Khi giao dịch rơi sát ranh giới kỳ (23:59:59 và 00:00:00) thì nó vào đúng kỳ theo múi giờ đã chốt không?

**Case mẫu:**
- Hạn nộp là 10:00:00. Gửi thao tác lúc 09:59:59, 10:00:00 và 10:00:01 theo giờ máy chủ, mỗi mốc chạy ba lần. Kết quả: ba lần cho cùng một kết quả ở mỗi mốc, đúng với quy tắc mốc đóng hay mốc mở trong tài liệu.
- Tác vụ tự động đóng đối tượng lúc 12:30, máy chủ dừng từ 12:20 tới 12:40. Kết quả: khi chạy lại, đối tượng được đóng một lần, lịch sử chỉ một dòng do Hệ thống thực hiện. Ví dụ ở hệ thống tuyển dụng là tự đóng tin tuyển dụng hết hạn, ở hệ thống giám sát là vòng quét 0 giờ.
- Bộ đếm "đã xử lý hôm nay" đang là 5. Đổi giờ hệ thống sang 00:00 ngày hôm sau. Kết quả: bộ đếm về 0, năm bản ghi đã xử lý vẫn giữ trạng thái cũ.

**Quy tắc nâng mức ưu tiên:** thao tác đúng mốc quyết định bị nhận hoặc bị từ chối không nhất quán, kéo dài sai loại hoặc sai số lần, tác vụ tự động chạy hai lần hoặc bỏ sót đều là High.

**Kỹ thuật đã có ở:** Testcase_Template Mục 13.5, 28. Data-Crawling Mục G, H.

---

### Nhóm 3. Vòng đời trạng thái và khóa theo giai đoạn

**Dấu hiệu trong tài liệu:** trạng thái, nháp, đã công bố, đang diễn ra, đã kết thúc, đã hủy, tạm dừng, kích hoạt, thu hồi, khóa, chỉ xem, không sửa được sau khi, chuyển sang, quay lại, hàng chờ.

**Câu hỏi suy ra case:**
1. Khi vẽ sơ đồ trạng thái thì mỗi mũi tên có điều kiện kích hoạt rõ không, và mỗi mũi tên **không có** trong sơ đồ có bị chặn ở máy chủ không?
2. Khi đối tượng đi qua từng giai đoạn thì trường nào còn sửa được, trường nào khóa? Đã lập bảng trường nhân giai đoạn và thử từng ô qua cả giao diện lẫn máy chủ chưa?
3. Khi đối tượng đang mở trong form mà vừa qua mốc khóa thì form có tự chuyển sang khóa không, lần lưu gửi sau mốc có bị từ chối không?
4. Khi một trường vẫn được sửa sau khi công bố thì mỗi lần sửa có ghi giá trị cũ, giá trị mới, và có báo cho người bị ảnh hưởng không?
5. Khi trạng thái cha đổi (tạm dừng nhóm) thì trạng thái riêng của từng phần tử con có bị ghi đè không, và bật lại thì mỗi con có về đúng trạng thái riêng của nó không?
6. Khi đối tượng đã về trạng thái cuối (hủy, kết thúc) thì có đường nào đảo ngược được không, kể cả qua máy chủ?
7. Khi gửi lệnh chuyển sang chính trạng thái hiện tại thì hệ thống có tạo bản ghi thừa hay lỗi không?
8. Khi đối tượng quay lại trạng thái trước (quay lại hàng chờ, thu hồi về nháp) thì số liệu và giá trị đã tính từ trạng thái sau xử lý thế nào?
9. Khi đối tượng đổi trạng thái do module khác thì màn đang mở có phản ánh đúng không, thao tác dựa trên trạng thái cũ có bị chặn không?
10. Khi một trạng thái chỉ được ghi một lần (ký, xác nhận, chốt) thì gửi lần thứ hai có bị chặn không?

**Case mẫu:**
- Đối tượng đã qua giai đoạn mở nhận đăng ký. Gửi thẳng lệnh sửa giá trị bị khóa lên máy chủ. Kết quả: máy chủ từ chối, giá trị không đổi, nhật ký ghi lần thử bị từ chối nếu tài liệu yêu cầu. Ví dụ ở sàn đấu giá là giá khởi điểm, ở hệ thống bảo hiểm là mức phí sau khi hợp đồng có hiệu lực.
- Nhóm có ba phần tử con, một con đang tắt riêng. Tạm dừng nhóm rồi bật lại. Kết quả: con đang tắt vẫn tắt, hai con còn lại hoạt động, không con nào bị bật hết.
- Bản ghi đã duyệt quay lại hàng chờ. Kết quả: số liệu đã cộng từ bản ghi đó giữ nguyên hay trừ ra đúng theo quy tắc, và mọi nơi hiển thị xử lý giống nhau.

**Quy tắc nâng mức ưu tiên:** sửa được trường đã khóa qua máy chủ, đảo ngược được trạng thái cuối, trạng thái cha ghi đè trạng thái con làm sai kết quả đều là High.

**Kỹ thuật đã có ở:** Testcase_Template Mục 8.5, 8.8, 13.2, 25.

---

### Nhóm 4. Tính toán, cộng dồn, làm tròn và số liệu khớp nhau

**Dấu hiệu trong tài liệu:** công thức, tính, tổng, cộng dồn, nhân, chia, phần trăm, tỉ lệ, làm tròn, bước, đơn vị, theo m², điểm, trọng số, trung bình, tăng giảm so với kỳ trước, thẻ số liệu, báo cáo, dashboard.

**Câu hỏi suy ra case:**
1. Khi tài liệu có công thức thì đã có ít nhất một bộ số tính tay để so chưa, kể cả giá trị biên (0, rất lớn, số lẻ)?
2. Khi một giá trị được tính theo đơn vị (theo m², theo người, theo tháng) thì khoản nào nhân theo đơn vị, khoản nào không?
3. Khi đổi đơn vị hoặc kiểu tính trên cùng đối tượng thì hệ thống có tự quy đổi số không, và có nên quy đổi không?
4. Khi cùng một yếu tố xuất hiện nhiều lần trong một bản ghi thì nó được tính một lần hay nhiều lần?
5. Khi hai yếu tố chồng lấn nhau thì có bị tính hai lần cho cùng một hành vi không?
6. Khi làm tròn thì làm tròn ở bước nào, mấy chữ số, và các tỉ lệ cộng lại có ra 100 phần trăm trong sai số cho phép không?
7. Khi kỳ trước bằng 0 thì tỉ lệ tăng giảm hiển thị thế nào, có lỗi chia cho 0 không?
8. Khi cùng một con số hiện ở nhiều nơi (thẻ, bảng, màn chi tiết, báo cáo, tệp xuất) thì các nơi có khớp nhau không?
9. Khi chỉ một số trạng thái được tính vào tổng (đã duyệt, đã thanh toán) thì bản ghi ở trạng thái khác có bị tính nhầm vào không?
10. Khi bản ghi con đổi giá trị thì số dồn lên bản ghi cha có cập nhật đúng không, cập nhật lúc nào?

**Case mẫu:**
- Giá cuối 1.200.000.000 đồng, tiền đã nộp trước 120.000.000 đồng. Kết quả: số còn phải trả hiện 1.080.000.000 đồng ở mọi màn và tệp xuất. Với đơn vị theo m², nhân diện tích trước khi trừ.
- Một bản ghi khớp cùng một yếu tố 5 điểm lặp năm lần. Kết quả: điểm là 5, không phải 25. Ví dụ ở hệ thống giám sát nội dung là từ khóa, ở hệ thống chấm điểm tín dụng là một hành vi trễ hạn ghi nhận trùng.
- Hồ sơ có 5 bản ghi đã duyệt, 3 chờ duyệt, 2 bị từ chối. Kết quả: thẻ số liệu, cột ở bảng và màn chi tiết đều hiện 5.

**Quy tắc nâng mức ưu tiên:** số sai mà người ra quyết định vẫn tin (thẻ lệch bảng, cộng trùng, tính nhầm trạng thái) là High.

**Kỹ thuật đã có ở:** Metrics-Listing (thẻ, kỳ, rút gọn số, nhất quán). Scoring-RuleBase Mục C, H, I.

---

### Nhóm 5. Điều kiện tham gia, tư cách và mất tư cách

**Dấu hiệu trong tài liệu:** điều kiện, đủ điều kiện, tư cách, được phép, xác thực danh tính, KYC, eKYC, xác minh, duyệt hồ sơ, đồng ý điều khoản, quy chế, cấm, khóa, truất quyền, bị loại, danh sách đen, hạn chế.

**Câu hỏi suy ra case:**
1. Khi người dùng ở từng trạng thái xác minh (chưa gửi, chờ duyệt, bị từ chối, đã duyệt rồi bị hủy duyệt) thì chức năng phía sau mở hay chặn đúng chưa?
2. Khi người dùng đang bị khóa, bị cấm có thời hạn, hoặc thuộc nhóm bị chặn theo tài liệu thì họ có đăng ký, vào, hoặc thao tác được qua bất kỳ đường nào không?
3. Khi điều kiện cần đọc và đồng ý văn bản thì gửi thẳng lên máy chủ mà không kèm xác nhận đồng ý có bị chặn không? Hệ thống lưu người dùng đã đồng ý phiên bản nào?
4. Khi văn bản điều kiện được thay sau khi người dùng đã đồng ý thì hệ thống xử lý người đã đồng ý bản cũ ra sao?
5. Khi người dùng đủ điều kiện rồi mất điều kiện giữa chừng (tiền bị chuyển về chưa nộp, đổi người đại diện, giấy tờ hết hạn) thì hệ thống giữ, cảnh báo, hay thu hồi?
6. Khi người duyệt xét điều kiện thì điều kiện được xét tại lúc nào (lúc mở form hay lúc bấm xác nhận), và còn bao lâu trước mốc thì không duyệt được nữa?
7. Khi người đã bị loại vẫn còn phiên đăng nhập hoặc còn tab đang mở thì thao tác của họ có bị chặn ở máy chủ không?
8. Khi người không đủ điều kiện bị chặn thì họ có được biết lý do và biết làm gì tiếp không?
9. Khi người đã đủ điều kiện và đã được duyệt thì họ có còn sửa được hồ sơ đã nộp không, kể cả qua máy chủ?
10. Khi đối tượng bị cấm có thời hạn thì thời hạn tính từ ngày nào và hết hạn có tự mở lại không?

**Case mẫu:**
- Tài khoản đã xác minh rồi bị hủy xác minh, vẫn còn phiên đăng nhập. Gửi thẳng lệnh đăng ký tham gia. Kết quả: máy chủ từ chối, không tạo bản ghi đăng ký.
- Người dùng đã đồng ý điều khoản bản 1, sau đó điều khoản lên bản 2. Kết quả: hồ sơ lưu đúng bản 1 kèm thời điểm đồng ý. Ví dụ ở sàn đấu giá là quy chế phiên, ở ứng dụng tài chính là điều khoản vay.
- Người duyệt mở hồ sơ lúc còn 4 phút trước mốc, bấm duyệt lúc còn 2 phút 59 giây. Kết quả: bị chặn vì điều kiện xét tại lúc bấm.

**Quy tắc nâng mức ưu tiên:** người không đủ điều kiện theo tài liệu vẫn tham gia, vào, hoặc tạo ra kết quả được là High.

**Kỹ thuật đã có ở:** Identity-Account-Linking Mục F, G. Testcase_Template Mục 9.4.

---

### Nhóm 6. Xác định kết quả cuối, đề xuất của máy và quyết định của người

**Dấu hiệu trong tài liệu:** kết quả, thành công, không thành, người thắng, trúng, xếp hạng, điểm cuối, mức rủi ro, đề xuất, gợi ý, AI, máy chấm, tự động phân loại, người duyệt xác nhận, ghi đè, sửa kết quả, khiếu nại, xem xét lại.

**Câu hỏi suy ra case:**
1. Khi liệt kê mọi nhánh dẫn tới kết quả "không thành" thì mỗi nhánh đã có một case riêng chưa?
2. Khi lượt tốt nhất bị rút lại hoặc bị loại thì kết quả có tự rơi về người liền kề không, và tài liệu có cho phép điều đó không?
3. Khi có điều kiện ngưỡng (giá tối thiểu, điểm tối thiểu, số người tối thiểu) thì đúng bằng ngưỡng, dưới ngưỡng, và không cấu hình ngưỡng cho kết quả gì?
4. Khi máy đưa ra kết quả trước và người sửa sau thì mọi nơi dùng kết quả (điểm cha, báo cáo, xếp hạng) có lấy giá trị của người không?
5. Khi máy chạy lại trên bản ghi người đã sửa thì giá trị của người có bị ghi đè không? Đã kiểm ở tầng dữ liệu chưa?
6. Khi người sửa lại kết quả đã chốt thì có bắt buộc lý do không, có ghi trước sau không, và số liệu phía sau tính lại đúng không?
7. Khi kết quả chưa chốt thì màn kết quả, tệp kết quả, lệnh gọi máy chủ có bị chặn không?
8. Khi bản ghi đang có khiếu nại chờ xử lý mà người duyệt sửa kết quả thì khiếu nại xử lý thế nào? Người xử lý khiếu nại có phải người đã ra quyết định bị khiếu nại không?
9. Khi máy không trả được kết quả (thiếu, chậm, lỗi) thì bản ghi nằm ở đâu, có bị coi là kết quả hợp lệ không?

**Case mẫu:**
- Lượt cao nhất bị rút, sau đó không ai làm gì thêm tới hết giờ. Kết quả: không thành, người liền kề không tự thành người thắng. Ví dụ ở sàn đấu giá là rút giá, ở hệ thống đấu thầu là nhà thầu xếp đầu rút hồ sơ.
- Máy chấm 4 điểm, người duyệt chốt 2 điểm, chạy lại tác vụ chấm ba lần. Kết quả: giá trị vẫn là 2 sau cả ba lần, điểm hồ sơ cha tính theo 2.
- Gọi thẳng lệnh lấy kết quả khi phiên chưa kết thúc. Kết quả: máy chủ từ chối, không trả dữ liệu.

**Quy tắc nâng mức ưu tiên:** xác định sai người thắng, kết quả thành và không thành bị đảo, máy ghi đè quyết định của người đều là High.

**Kỹ thuật đã có ở:** AI-Assisted-Review (toàn bộ). Ranking-Leaderboard Mục C, J.

---

### Nhóm 7. Duyệt nhiều cấp, ký và quyền quyết định

**Dấu hiệu trong tài liệu:** trình duyệt, phê duyệt, kiểm tra, ký nháy, ký số, chữ ký, chứng thư, OTP xác nhận, người bắt buộc, người không bắt buộc, từ chối, trình lại, luồng duyệt, cấp duyệt, đồng ý, ý kiến.

**Câu hỏi suy ra case:**
1. Khi luồng có nhiều bên, nhiều cấp thì thứ tự bắt buộc là gì, và thao tác sớm hơn thứ tự có bị chặn ở máy chủ không?
2. Khi người bắt buộc từ chối và người không bắt buộc từ chối thì luồng đi tiếp hay dừng?
3. Khi bị từ chối rồi trình lại thì mọi người có phải xử lý lại từ đầu không, chữ ký cũ có bị xóa khỏi tệp mới không, lịch sử vòng trước có còn tra được không?
4. Khi đã cho ý kiến thì còn đổi được không? Đang mở hộp thoại mà người khác vừa từ chối thì có bị chặn không?
5. Khi một người được gán hai vai trò trên cùng văn bản thì hệ thống có chặn không, ngoại lệ là gì?
6. Khi ký giữa chừng bị lỗi (mất mạng, hủy nhập mã, quá thời gian) thì tệp có ở trạng thái ký dở không?
7. Khi văn bản đã có chữ ký thì nội dung có bị khóa ở mọi phía, kể cả qua máy chủ không?
8. Khi chứng thư hết hạn, sai số serial, sai mã số thuế, hoặc chưa đăng ký thì việc ký có bị chặn không?
9. Khi thao tác có hậu quả nặng cần mã xác nhận thì mã hết hạn, nhập sai quá số lần, và thao tác của người khác trong lúc đang nhập mã xử lý ra sao?
10. Khi người được gán duyệt bị vô hiệu hóa giữa chừng thì luồng có kẹt không?

**Câu hỏi bổ sung:**
- Khi người tạo cũng là người duyệt bản ghi của chính mình thì hệ thống chặn hay cho phép, và có ghi rõ trong nhật ký không?
- Khi người duyệt ủy quyền cho người khác thì ủy quyền có thời hạn không, hết hạn giữa chừng thì việc đang chờ chuyển về đâu, nhật ký ghi tên người nào?
- Khi quản trị đăng nhập thay người dùng để hỗ trợ thì các thao tác nhạy cảm (duyệt, chi tiền, ký) có bị chặn không?

**Case mẫu:**
- Văn bản cần cả hai bên phê duyệt mới mở ký. Gửi thẳng lệnh ký khi mới một bên duyệt. Kết quả: máy chủ từ chối, văn bản giữ trạng thái chờ duyệt. Ví dụ ở hồ sơ hợp đồng là ký số, ở hệ thống nhân sự là quyết định bổ nhiệm.
- Mất mạng giữa lượt ký. Kết quả: tệp giữ nguyên bản trước khi ký, không có chữ ký dở dang, trạng thái không đổi.
- Người bắt buộc từ chối sau khi hai bên đã ký nháy. Kết quả: văn bản về Từ chối, trình lại thì tệp mới không còn chữ ký cũ, lịch sử vòng trước vẫn xem được.

**Quy tắc nâng mức ưu tiên:** ký sai người, ký dở dang, sửa được nội dung sau khi ký, vượt được bước duyệt bắt buộc đều là High.

**Kỹ thuật đã có ở:** Testcase_Template Mục 25, 26. Advanced Mục D (chuỗi nhiều bước).

---

### Nhóm 8. Thao tác đồng thời, lặp lại và tranh chấp tài nguyên

**Dấu hiệu trong tài liệu:** cùng lúc, đồng thời, realtime, nhiều người, nhiều thiết bị, đến trước, giữ chỗ, tồn kho, suất, slot, khóa bản ghi, duy nhất, chỉ một, không trùng, hàng chờ.

**Câu hỏi suy ra case:**
1. Khi hai người cùng tranh một tài nguyên duy nhất thì ai thắng, người thua nhận thông báo gì, và kết quả có ổn định qua nhiều lần chạy không?
2. Khi hai thao tác ngược chiều đến gần như cùng lúc (rút và đặt, hủy và xác nhận) thì quy tắc thứ tự đã chốt chưa, mỗi thứ tự có case chưa?
3. Khi người dùng bấm nút xác nhận nhiều lần thật nhanh thì có tạo bản ghi trùng, trừ tiền trùng, đếm trùng không?
4. Khi gửi lại đúng một yêu cầu cũ đã thành công thì hệ thống có tạo kết quả thứ hai không?
5. Khi hai người cùng sửa một bản ghi thì người lưu sau có được báo dữ liệu đã đổi không, hay ghi đè âm thầm?
6. Khi một người đang sửa bản ghi mà người khác xóa nó thì lần lưu có tạo lại bản ghi đã xóa không?
7. Khi cùng một tài khoản thao tác ở hai thiết bị thì hai nơi có thấy cùng một trạng thái không, thao tác ở thiết bị cũ sau khi đổi trạng thái ở thiết bị mới có bị chặn không?
8. Khi chỉ được tồn tại một đối tượng theo một khóa (một hợp đồng mỗi bộ hồ sơ, một phiên chưa kết thúc mỗi tài sản) thì hai người cùng tạo có ra hai bản ghi không?
9. Khi nhiều thao tác dồn vào cùng vài giây cuối thì có mất thao tác, đảo thứ tự, hoặc kích hoạt hai lần cùng một hệ quả không?
10. Khi người dùng mở lần đầu một màn sinh mã ở hai thiết bị cùng lúc thì hệ thống sinh một mã hay hai?

**Case mẫu:**
- Hai người gửi cùng một mức trong cùng 50 mili giây. Kết quả: yêu cầu đến trước được ghi nhận, yêu cầu sau bị từ chối kèm thông báo theo tài liệu, chạy lại mười lần đều cho kết quả cùng kiểu. Ví dụ ở sàn đấu giá là trả giá, ở hệ thống đặt lịch là hai người đặt cùng một khung giờ.
- Hai người cùng bấm Phê duyệt trên một bản ghi. Kết quả: chỉ một mốc lịch sử, người sau được báo bản ghi đã xử lý, bộ đếm chỉ tăng 1.
- Người A đang sửa, người B xóa bản ghi, người A bấm lưu. Kết quả: A được báo bản ghi không còn tồn tại, không có bản ghi mới nào được tạo.

**Quy tắc nâng mức ưu tiên:** tranh chấp làm sai kết quả cuối, sai tiền, hoặc mất thao tác của người dùng là High.

**Kỹ thuật đã có ở:** Testcase_Template Mục 12.2, 15.3, 16. Advanced Mục A. AI-Assisted-Review Mục G.

---

### Nhóm 9. Tích hợp hệ thống ngoài và nguồn dữ liệu

**Dấu hiệu trong tài liệu:** đồng bộ, tích hợp, API bên thứ ba, webhook, ngân hàng, cổng thanh toán, hệ thống nguồn, CRM, ERP, thu thập, quét, crawl, nhập từ, đẩy sang, nhận về, đối soát, nguồn dữ liệu.

**Câu hỏi suy ra case:**
1. Khi hệ thống ngoài gửi dữ liệu đúng thì dữ liệu hiện ở đâu, sau bao lâu, và có cần chờ tác vụ theo lịch không?
2. Khi hệ thống ngoài gửi dữ liệu nhưng bước cập nhật nội bộ lỗi thì có nơi nào ghi lỗi để người nội bộ xử lý không, và người dùng có bị báo thành công giả không?
3. Khi hệ thống ngoài chậm, lỗi, hoặc không truy cập được thì phần còn lại có chạy bình thường không, dữ liệu cũ có bị về 0 không?
4. Khi một nguồn lỗi liên tiếp thì sau bao nhiêu lần màn hình mới báo, hay nguồn chết âm thầm?
5. Khi dữ liệu trường nào do hệ thống ngoài quyết định thì hệ thống này có cho sửa trường đó không, kể cả qua máy chủ?
6. Khi dữ liệu đã nhận về bị sửa hoặc bị xóa ở bên ngoài thì hệ thống này cập nhật theo, giữ nguyên, hay đánh dấu?
7. Khi cùng một bản ghi đến từ hai nguồn hoặc hai đường dẫn khác nhau thì có bị tính hai lần không?
8. Khi tắt hoặc xóa một nguồn thì dữ liệu đã nhận từ nguồn đó còn hay mất, và có ai biết đang thiếu dữ liệu từ khoảng nào không?
9. Khi chuỗi nhiều hệ thống chạy qua nhiều bước mà gãy ở giữa thì dữ liệu dừng ở đâu, có ở trạng thái nửa vời không?
10. Khi dữ liệu nhận về có ký tự lạ, múi giờ khác, định dạng tiền khác thì có được chuẩn hóa đúng không?

**Câu hỏi bổ sung:**
- Khi bản ghi tạo ở một portal hoặc module (nguồn) được xem ở portal, vai trò, tệp xuất, báo cáo khác thì nơi nhận có đủ trường, đúng giá trị, đúng định dạng, đúng nhãn trạng thái và ẩn đúng trường nội bộ không? Lập bảng đối chiếu theo Testcase_Template Mục 27.9.

**Case mẫu:**
- Thông báo nhận tiền đến nhưng bước cập nhật hồ sơ người dùng lỗi. Kết quả: màn lịch sử giao dịch nội bộ ghi trạng thái Lỗi kèm lý do, người dùng vẫn ở Chưa nộp. Ví dụ ở sàn đấu giá là tiền đặt trước, ở hệ thống học phí là học phí kỳ.
- Vòng lấy dữ liệu lỗi với một hồ sơ. Kết quả: hồ sơ đó giữ số của lần thành công gần nhất, các hồ sơ khác vẫn cập nhật.
- Cùng một bài xuất hiện ở hai tên miền con của một trang. Kết quả: chỉ một bản ghi, không cộng điểm hai lần.

**Quy tắc nâng mức ưu tiên:** dữ liệu ngoài làm ghi nhận sai tiền, sai kết quả, mất dữ liệu âm thầm, hoặc báo thành công giả là High.

**Kỹ thuật đã có ở:** Testcase_Template Mục 12.3, 27. Advanced Mục A, D, E. Data-Crawling (toàn bộ). Identity-Account-Linking Mục C.

---

### Nhóm 10. Gắn đúng chủ thể: trùng, gộp, quy nhầm

**Dấu hiệu trong tài liệu:** mã tham chiếu, nội dung chuyển khoản, mã khách hàng, định danh, trùng, gộp, tách, hợp nhất, gán cho, thuộc về, liên kết tài khoản, hồ sơ trùng, một người nhiều tài khoản.

**Câu hỏi suy ra case:**
1. Khi hệ thống sinh mã để gắn dữ liệu về một chủ thể thì mã có duy nhất theo chủ thể, theo đối tượng, theo loại khoản không, và có đổi giữa các lần mở không?
2. Khi nhiều người thao tác cùng lúc thì tệp hay bản ghi sinh ra có lẫn thông tin của người khác không?
3. Khi hai chủ thể khác nhau trùng tên hiển thị thì hệ thống có gộp nhầm không?
4. Khi một người thật có nhiều tài khoản hoặc dùng cùng giấy tờ ở hai loại tài khoản thì quy tắc là gì?
5. Khi gộp hai hồ sơ thì toàn bộ dữ liệu con có chuyển đủ không, bản ghi trùng có bị cộng hai lần không?
6. Khi hoàn tác một lượt gộp thì mọi thứ có về đúng chủ cũ, số liệu có tính lại không, gộp rồi hoàn tác nhiều lần có lệch dần không?
7. Khi gộp nối tiếp (A vào B, B vào C) rồi hoàn tác lượt đầu thì hệ thống xử lý xác định được không?
8. Khi tác vụ tự động gộp thì có ghi căn cứ không, có hoàn tác được không, có gộp lại ngay sau khi người vừa tách ra không?
9. Khi chủ thể đổi thông tin định danh (đổi tên, cấp lại giấy tờ) giữa chừng thì dữ liệu đang chạy có bị đứt khỏi chủ thể không?

**Case mẫu:**
- Khách A dùng mã tham chiếu của khách B để chuyển tiền. Kết quả: tiền không được ghi cho A, cũng không được ghi đủ cho B nếu sai số tiền, giao dịch hiện ở danh sách chờ xử lý tay.
- Gộp hồ sơ X (3 kênh) vào hồ sơ Y (4 kênh) rồi hoàn tác. Kết quả: X có lại đúng 3 kênh, Y có lại đúng 4 kênh, điểm của cả hai tính lại. Ví dụ ở hệ thống CRM là gộp khách hàng trùng, ở hệ thống y tế là gộp hồ sơ bệnh nhân.
- Hai người khác nhau trùng họ tên. Kết quả: hai bản ghi riêng, hai mã riêng, số liệu không cộng gộp.

**Quy tắc nâng mức ưu tiên:** dữ liệu, tiền, điểm hoặc trách nhiệm bị gắn nhầm sang người khác là High.

**Kỹ thuật đã có ở:** Identity-Account-Linking Mục B. Testcase_Template Mục 26.

---

### Nhóm 11. Văn bản, tệp sinh ra, tệp xuất và chứng từ

**Dấu hiệu trong tài liệu:** biên bản, hợp đồng, phiếu, quyết định, giấy xác nhận, mẫu văn bản, sinh tự động, tạo lại, xuất Excel, xuất PDF, in, tải về, báo cáo, hóa đơn, tệp đính kèm, chứng từ.

**Câu hỏi suy ra case:**
1. Khi hệ thống sinh văn bản từ dữ liệu thì mọi dòng trong văn bản có khớp dữ liệu gốc không, kể cả bản ghi đã bị rút hoặc bị loại?
2. Khi có bản xem trước và bản chính thức thì bản xem trước có bị lưu vào hồ sơ hoặc gửi đi không?
3. Khi mỗi tổ chức có mẫu riêng thì tổ chức không có mẫu có bị dùng nhầm mẫu của tổ chức khác không?
4. Khi thay, tắt, xóa mẫu lúc đang có văn bản trong luồng thì văn bản cũ có bị đổi theo không?
5. Khi tạo lại văn bản thì phần nào đổi, phần nào giữ, chữ ký cũ xử lý ra sao, có cảnh báo trước không?
6. Khi văn bản đã sinh thì trường hợp nào không được sinh (không có dữ liệu, phiên không thành)?
7. Khi xuất tệp thì số liệu có đúng kỳ và đúng bộ lọc đang chọn không, kỳ rỗng có ra tệp hỏng không?
8. Khi xuất tệp thì tệp có chứa trường vượt quyền của người xuất không?
9. Khi dữ liệu bắt đầu bằng ký tự công thức thì mở tệp xuất ra có bị hiểu thành công thức không?
10. Khi tệp tự sinh tính vào giới hạn số tệp tải lên thì giới hạn còn lại có đúng không?

**Case mẫu:**
- So từng dòng của biên bản với dữ liệu gốc của một phiên có 12 lượt, trong đó 2 lượt bị rút. Kết quả: biên bản có đủ 12 dòng, nhãn ghi chú đúng, tổng số lượt khớp.
- Ô dữ liệu bắt đầu bằng dấu bằng. Xuất Excel rồi mở. Kết quả: ô hiển thị như chữ. Ví dụ ở hệ thống giám sát là nội dung do người ngoài viết, ở hệ thống bán hàng là ghi chú đơn hàng của khách.
- Tổ chức B chưa có mẫu riêng, tổ chức A có mẫu riêng. Khách của B sinh văn bản. Kết quả: không dùng mẫu của A, dùng mẫu mặc định hoặc luồng cũ theo tài liệu.

**Quy tắc nâng mức ưu tiên:** văn bản có giá trị pháp lý lệch dữ liệu gốc, sinh sai người, hoặc tệp xuất lộ dữ liệu vượt quyền là High.

**Kỹ thuật đã có ở:** Testcase_Template Mục 19, 20.

---

### Nhóm 12. Dữ liệu cá nhân, hiển thị theo vai trò và phạm vi dữ liệu

**Dấu hiệu trong tài liệu:** CCCD, số điện thoại, email, ảnh giấy tờ, số tài khoản, thông tin cá nhân, che, ẩn, mã hóa, chỉ xem, quyền xem, ẩn danh, đồng ý thu thập, tổ chức, chi nhánh, phòng ban, đối tác, chỉ thấy dữ liệu của mình, nhiều tổ chức.

**Câu hỏi suy ra case:**
1. Khi lập ma trận vai trò nhân trường thông tin nhân màn hình nhân giai đoạn thì mỗi ô đã được kiểm ở mọi đường chưa: màn hình, phản hồi máy chủ, sự kiện realtime, mã nguồn trang, tệp xuất, văn bản, thông báo và email?
2. Khi vai trò không được thấy một trường thì phản hồi máy chủ có chứa trường đó không, dù giao diện đã ẩn?
3. Khi quyền chỉ có hiệu lực sau một mốc thì trước mốc gọi máy chủ có bị chặn không?
4. Khi một người được cấp hai quyền có phạm vi mâu thuẫn thì hệ thống tính theo quyền nào?
5. Khi quyền bị thu hồi lúc phiên còn chạy thì hiệu lực từ khi nào?
6. Khi người dùng đổi mã định danh trên đường dẫn hoặc trong yêu cầu thì có xem được dữ liệu không thuộc về mình không?
7. Khi mỗi tổ chức chỉ thấy dữ liệu của mình thì danh sách, báo cáo, tệp xuất, tìm kiếm có lọt dữ liệu tổ chức khác không?
8. Khi thu thập dữ liệu nhạy cảm cần đồng ý thì không đồng ý hoặc đóng hộp thoại có chặn việc gửi không, và mỗi phản hồi có được ghi lại không?
9. Khi xem ảnh giấy tờ thì đường dẫn có hết hạn không, mở thẳng khi chưa đăng nhập có được không?
10. Khi người dùng rời hệ thống hoặc thay giấy tờ thì dữ liệu cũ giữ bao lâu, ai xem được?
11. Khi trang công khai mở cho người chưa đăng nhập thì có lộ dữ liệu chỉ dành cho người đã đăng nhập không?

**Câu hỏi bổ sung:**
- Khi một người dùng thuộc nhiều tổ chức thì đổi tổ chức đang làm việc có đổi theo đủ dữ liệu, quyền, cấu hình, mã tự sinh, mẫu thông báo không? Báo cáo tổng có cộng lẫn tổ chức khác không?
- Khi đặc tả yêu cầu thu đồng ý xử lý dữ liệu cá nhân thì bằng chứng đồng ý lưu ở đâu, rút đồng ý thì luồng nào phải dừng?
- Khi dữ liệu có thời hạn lưu giữ thì hết hạn được xóa, ẩn hay ẩn danh, và bản sao trong tệp xuất, nhật ký xử lý ra sao?

**Case mẫu:**
- Vai trò không có quyền xem danh sách người đăng ký mở màn danh sách. Kết quả: giao diện chỉ hiện Có hoặc Không, phản hồi máy chủ không chứa số lượng hay danh sách.
- Người dùng tổ chức A đổi mã bản ghi trên đường dẫn sang mã của tổ chức B. Kết quả: máy chủ từ chối, không trả dữ liệu. Ví dụ ở hệ thống đa chi nhánh ngân hàng, ở hệ thống trường học nhiều cơ sở.
- Vai trò chỉ xem đọc màn danh sách hồ sơ. Kết quả: email và số điện thoại không có trên giao diện và không có trong phản hồi máy chủ.

**Quy tắc nâng mức ưu tiên:** vai trò không được phép thấy dữ liệu cá nhân hoặc dữ liệu của tổ chức khác qua bất kỳ đường nào là High.

**Kỹ thuật đã có ở:** Testcase_Template Mục 9 (đặc biệt 9.3, 9.6). Identity-Account-Linking Mục H, I. Public-Share-Link Mục C, G.

---

### Nhóm 13. Nhật ký, bằng chứng và dựng lại sự việc

**Dấu hiệu trong tài liệu:** nhật ký, lịch sử, log, lịch sử thay đổi, lịch sử xử lý, người thực hiện, thời điểm, giá trị cũ, giá trị mới, lưu vết, truy vết, bằng chứng, khiếu nại, tranh chấp, lưu trữ 12 tháng.

**Câu hỏi suy ra case:**
1. Khi ba tháng sau có người khiếu nại "tôi không làm việc đó" hoặc "tôi làm trước người kia" thì hệ thống có đủ dữ liệu để trả lời không?
2. Khi một thao tác quan trọng xảy ra thì nhật ký có ghi đủ người làm, thời điểm máy chủ nhận, giá trị cũ, giá trị mới, kênh, thiết bị không?
3. Khi thao tác bị từ chối thì có được ghi lại kèm lý do không?
4. Khi giá trị bị đổi rồi trả về đúng ban đầu thì nhật ký có ghi đủ hai lần không?
5. Khi người có quyền cao nhất thử sửa hoặc xóa một dòng nhật ký, kể cả qua máy chủ, thì có làm được không?
6. Khi bản ghi được phê duyệt mà không sửa gì thì lịch sử có vẫn ghi người đã xem và đồng ý không?
7. Khi tài khoản của người từng thao tác bị vô hiệu hóa hoặc bị xóa thì lịch sử còn hiện đúng tên họ không?
8. Khi chọn một ngày trong quá khứ thì có dựng lại được cấu hình đang hiệu lực ngày đó không?
9. Khi truy ngược từ kết quả cuối về từng bản ghi con, quy tắc đã dùng và người đã xử lý thì có thiếu mắt xích nào không?
10. Khi việc xem và xuất nhật ký cũng là thao tác nhạy cảm thì việc đó có được ghi lại không?
11. Khi các nơi hiển thị cùng một diễn biến (màn diễn biến, văn bản, màn kết quả) thì có khớp nhau từng dòng không?

**Case mẫu:**
- Chọn ngẫu nhiên một phiên đã kết thúc, dựng lại ai vào lúc nào, từng thao tác, từng lần kéo dài và lý do, kết quả. Kết quả: dựng được đủ từ dữ liệu, ghi rõ mắt xích nào thiếu.
- Một giá trị bị sửa năm lần bởi hai người. Kết quả: lịch sử có năm mốc, mỗi mốc có người, thời điểm, trước và sau. Ví dụ ở hệ thống giám sát là sắc thái nội dung, ở hệ thống kho là số lượng tồn điều chỉnh tay.
- Quản trị cao nhất gọi thẳng lệnh xóa một dòng nhật ký. Kết quả: máy chủ từ chối, dòng nhật ký còn nguyên.

**Quy tắc nâng mức ưu tiên:** không dựng lại được ai làm gì lúc nào với kết quả, tiền, cấu hình hoặc quyền là High.

**Kỹ thuật đã có ở:** Testcase_Template Mục 8.6. Adversarial-Integrity Mục H. AI-Assisted-Review Mục F.

---

### Nhóm 14. Cấu hình, tham số và đổi quy tắc giữa chừng

**Dấu hiệu trong tài liệu:** cấu hình, tham số, thiết lập, bật, tắt, mặc định, theo tổ chức, theo danh mục, theo gói, quy tắc, bộ quy tắc, ngưỡng, áp dụng từ, có hiệu lực, hồi tố, dữ liệu cũ, thuế suất, phiên bản.

**Câu hỏi suy ra case:**
1. Khi đổi một cấu hình thì nó áp cho đối tượng tạo sau thời điểm đổi, hay cả đối tượng đang chạy, hay cả dữ liệu đã có? Tài liệu nói gì?
2. Khi cấu hình có phạm vi (tổ chức, danh mục, gói) thì đổi ở phạm vi này có lan sang phạm vi khác không?
3. Khi cấu hình chỉ được sửa ở một giai đoạn thì sửa qua máy chủ ở giai đoạn khác có bị bỏ qua hoặc từ chối không?
4. Khi một vai trò không được sửa cấu hình của cấp trên thì gọi thẳng máy chủ có bị chặn không?
5. Khi để trống một tham số thì hệ thống hiểu là không giới hạn, bằng 0, hay lỗi?
6. Khi sửa quy tắc thì dữ liệu cũ có bị tính lại không? Hai bản ghi giống nhau nhưng tính ở hai thời điểm có mang hai kết quả khác nhau không, và giao diện có cho biết điều đó không?
7. Khi tạm dừng hoặc xóa một quy tắc thì kết quả cũ đã tính theo quy tắc đó còn giữ không, còn đọc được tên quy tắc không?
8. Khi một quy tắc bị tắt trong vài ngày rồi bật lại thì dữ liệu trong khoảng tắt có bị thiếu vĩnh viễn không, có ai biết không?
9. Khi tính năng phụ thuộc gói hoặc giới hạn số lượng thì vượt giới hạn có bị chặn không, đổi gói có đổi giới hạn không?
10. Khi bật một cấu hình mà điều kiện tiên quyết chưa có thì có bật được không, kể cả qua máy chủ?
11. Khi các tài liệu nói khác nhau về một quy tắc thì đã ghi câu hỏi chặn vào file ghi chú chưa?

**Câu hỏi bổ sung:**
- Khi cấu hình có nhiều cấp bật tắt lồng nhau (bật chung, bật theo từng loại) thì tắt cấp trên có làm dừng cấp dưới không, bật lại cấp trên thì cấp dưới về trạng thái riêng trước đó hay bật hết?

**Case mẫu:**
- Đổi thuế suất từ 8 phần trăm lên 10 phần trăm lúc 10:00. Kết quả: giao dịch tạo trước 10:00 giữ 8 phần trăm, giao dịch sau 10:00 dùng 10 phần trăm.
- Sửa điểm của một quy tắc từ 5 xuống 2. Kết quả: ba bản ghi cũ giữ 5, bản ghi mới nhận 2. Ví dụ ở hệ thống giám sát là điểm từ khóa, ở hệ thống khuyến mãi là mức chiết khấu.
- Bật tự động công bố khi chưa có văn bản tiên quyết, gửi thẳng lên máy chủ. Kết quả: máy chủ từ chối, cấu hình giữ Tắt.

**Quy tắc nâng mức ưu tiên:** cấu hình lan sai phạm vi, đổi quy tắc làm thay đổi âm thầm kết quả đã chốt, hoặc không truy được quy tắc đã dùng tại thời điểm tính là High.

**Kỹ thuật đã có ở:** Testcase_Template Mục 14. Scoring-RuleBase Mục E, F, J.

---

### Nhóm 15. Gian lận, lạm quyền và thông đồng

**Dấu hiệu trong tài liệu:** quản trị, toàn quyền, sửa tay, cập nhật tay, ghi đè, dừng, hủy, vô hiệu hóa, đặt lại mật khẩu, đổi vai trò, nhiều tài khoản, cùng thiết bị, cùng IP, giới hạn tần suất, khóa tài khoản, thông đồng, gian lận, né.

**Câu hỏi suy ra case:**
1. Khi người có quyền dùng quyền vào đúng thời điểm có lợi (sát hạn, ngay sau một thao tác cụ thể) thì hệ thống chặn, hay cho làm nhưng để lại dấu vết đủ phát hiện?
2. Khi người duyệt tự duyệt hồ sơ của chính mình hoặc người liên quan thì hệ thống có chặn không?
3. Khi người vai trò thấp tự nâng quyền mình, tạo tài khoản quyền cao hơn mình, hoặc gửi giá trị vai trò lạ thì máy chủ có từ chối không?
4. Khi xóa hoặc hạ quyền tài khoản quản trị cuối cùng thì có bị chặn không?
5. Khi quản trị đặt lại mật khẩu người khác thì có đường nào để họ đăng nhập thay người đó mà không bị phát hiện không?
6. Khi nhiều tài khoản thao tác từ cùng thiết bị hoặc cùng địa chỉ mạng trong cùng một sự kiện thì hệ thống có ghi đủ dữ liệu để phát hiện sau không?
7. Khi đối tượng bị giám sát hoặc bị chấm điểm cố né quy tắc (viết chệch, đổi nguồn) thì hệ thống có bắt được không? Không bắt được thì đã ghi thành giới hạn đã biết chưa?
8. Khi thao tác được gửi bằng công cụ tự động với tần suất cao thì có giới hạn không, có làm chậm người khác không?
9. Khi tắt rồi bật lại, sửa rồi sửa về, xóa rồi tạo lại để che một khoảng dữ liệu thì có để lại dấu vết không?
10. Khi nhập liệu hàng loạt được dùng làm đường vòng để sửa dữ liệu đã có thì hệ thống có chặn không?

**Case mẫu:**
- Người nội bộ đổi một cấu hình có lợi cho một bên lúc còn 6 phút trước mốc khóa. Kết quả: thao tác được hoặc bị chặn theo tài liệu, nếu được thì nhật ký ghi đủ người, thời điểm, giá trị cũ và mới, và có thông báo cho bên bị ảnh hưởng.
- Gửi lệnh tự nâng vai trò của chính mình. Kết quả: máy chủ từ chối, vai trò không đổi, nhật ký ghi lần thử.
- Tạm dừng một nguồn dữ liệu ba ngày rồi bật lại. Kết quả: nhật ký đủ để người rà soát thấy khoảng ba ngày đó thiếu dữ liệu từ nguồn nào. Ví dụ ở hệ thống giám sát là nguồn tin, ở hệ thống chấm công là tắt máy chấm công một chi nhánh.

**Quy tắc nâng mức ưu tiên:** người trong hệ thống làm lệch kết quả mà không để lại dấu vết, leo thang đặc quyền, tự khóa cả hệ thống ra ngoài là High.

**Kỹ thuật đã có ở:** Adversarial-Integrity Mục B, C, F. Advanced Mục C.6.

---

### Nhóm 16. Thông báo nghiệp vụ

**Dấu hiệu trong tài liệu:** thông báo, email, chuông, popup, toast, push, SMS, Zalo, gửi cho, người nhận, khi có kết quả, khi bị từ chối, khi bị hủy, ma trận thông báo.

**Câu hỏi suy ra case:**
1. Khi sự kiện nghiệp vụ xảy ra thì đúng nhóm người nhận nào nhận, và người **không** liên quan có chắc không nhận không?
2. Khi có nhiều nhóm nhận khác nhau (người thắng, người thua, người bị phạt) thì mỗi nhóm có nhận đúng nội dung của nhóm mình không?
3. Khi một kênh lỗi thì kênh khác có vẫn gửi không, lỗi có được ghi trạng thái không?
4. Khi sự kiện kích hoạt hai lần hoặc người dùng mở nhiều thiết bị thì mỗi kênh có gửi trùng không?
5. Khi người dùng không online lúc sự kiện xảy ra thì họ biết kết quả bằng đường nào sau đó?
6. Khi người dùng đóng thông báo trước khi đọc thì có nơi nào xem lại được không?
7. Khi nội dung thông báo chứa dữ liệu cá nhân thì có lộ dữ liệu của người khác không?
8. Khi tác vụ tự động gặp lỗi thì có gửi thông báo sai không?
9. Khi thông báo có ngưỡng thời gian trong tài liệu thì có đạt ngưỡng không?

**Case mẫu:**
- Đối tượng bị hủy khi đã có ba người đăng ký và một người chưa duyệt. Kết quả: chỉ những người đúng điều kiện trong tài liệu nhận thông báo, mỗi kênh một lần, tiêu đề email đúng loại sự kiện.
- Email lỗi khi gửi kết quả. Kết quả: chuông và popup vẫn tới, email được ghi trạng thái lỗi. Ví dụ ở sàn đấu giá là kết quả phiên, ở hệ thống tuyển sinh là kết quả xét tuyển.

**Quy tắc nâng mức ưu tiên:** gửi kết quả sai người, gửi cho người không liên quan, hoặc thông báo chứa dữ liệu cá nhân của người khác là High.

**Kỹ thuật đã có ở:** States-Errors-Notification Mục E, F, G. Testcase_Template Mục 18.

---

### Nhóm 17. Vận hành hệ thống: mã tự sinh, danh mục có hiệu lực, hạn mức, triển khai, di chuyển dữ liệu, sao lưu

**Dấu hiệu trong tài liệu:** mã tự sinh, số hiệu, số thứ tự, tiền tố, theo năm; ngày hiệu lực, áp dụng từ ngày, biểu phí, thuế suất; gói, giới hạn, tối đa, hạn mức, dung lượng; phiên bản, ứng dụng di động, cập nhật bản mới, cờ tính năng; nhập dữ liệu ban đầu, chuyển đổi dữ liệu, hệ thống cũ; gửi SMS, gửi email, OTP cho người chưa đăng nhập; sao lưu, khôi phục, chạy lại.

**Câu hỏi suy ra case:**
1. Khi mã được sinh tự động thì quy tắc là gì (tiền tố, theo năm, theo đơn vị), lưu thất bại có làm nhảy số không, hai người lưu cùng giây có trùng mã không, sang kỳ mới có đặt lại không, xóa bản ghi thì số đó có được dùng lại không?
2. Khi danh mục hoặc biểu phí có ngày hiệu lực thì giá trị lấy theo ngày tạo, ngày giao dịch hay ngày hiện tại? Bản ghi cũ hiển thị giá trị cũ hay mới? Báo cáo kỳ trước có bị tính lại không?
3. Khi có giới hạn số lượng (người dùng, bản ghi, lượt, dung lượng) thì chạm đúng giới hạn và vượt 1 đơn vị xử lý ra sao, hai người cùng dùng lượt cuối thì sao, hạn mức đặt lại lúc nào và theo giờ nào?
4. Khi hạ gói hoặc giảm hạn mức lúc đang vượt mức mới thì dữ liệu đã có xử lý thế nào?
5. Khi triển khai bản mới thì ứng dụng bản cũ gọi API đã đổi có hỏng không, người đang mở trang có mất dữ liệu đang nhập không, tính năng bật theo cờ có chặn được người chưa được bật gọi thẳng API không?
6. Khi đưa hệ thống vào dùng có nhập dữ liệu từ hệ thống cũ thì trạng thái, danh mục cũ tương ứng với cái nào ở hệ thống mới, bản ghi không qua kiểm tra mới xử lý ra sao, số lượng và tổng tiền trước và sau có khớp không, mã cũ có giữ để tra cứu không?
7. Khi chức năng gửi SMS, email, OTP hoặc gọi dịch vụ trả phí mà người chưa đăng nhập dùng được thì có giới hạn theo số điện thoại, IP, thiết bị không, chạm giới hạn thì báo gì, quản trị có được cảnh báo không?
8. Khi khôi phục dữ liệu từ bản sao lưu thì dữ liệu, tệp đính kèm và hàng chờ có khớp nhau không? Tác vụ nào được chạy lại, chạy lại có cộng dồn hai lần không, ai được chạy lại?

**Case mẫu:**
- Hai người lưu hồ sơ cùng một giây. Kết quả: hai mã khác nhau, liên tiếp theo quy tắc, không nhảy số khi một trong hai lần lưu bị lỗi kiểm tra.
- Biểu phí đổi từ ngày 01/11. Giao dịch tạo ngày 31/10, sửa ngày 02/11. Kết quả: phí giữ theo biểu phí cũ nếu đặc tả tính theo ngày tạo. Báo cáo tháng 10 giữ nguyên số.
- Bấm Gửi lại OTP 10 lần trong 1 phút với cùng số điện thoại. Kết quả: từ lần vượt giới hạn hiện thông báo chờ, không gửi thêm tin.

**Quy tắc nâng mức ưu tiên:** trùng mã chứng từ, tính sai theo ngày hiệu lực, vượt hạn mức có tính tiền, mất dữ liệu khi triển khai hoặc di chuyển, chạy lại làm cộng hai lần đều là High.

**Kỹ thuật đã có ở:** Testcase_Template Mục 11, 14, 31, 36. Template_Testcase_Advanced Mục A, D.

---

### Bảng nâng mức ưu tiên chung

Một case luôn là High nếu chạm vào một trong các điều sau, bất kể bảng xếp hạng chung xếp ở mức nào.

| Điều | Nhóm liên quan |
|---|---|
| Tiền bị ghi sai, ghi trùng, hoàn sai, trừ oan | 1 |
| Thao tác đúng mốc quyết định cho kết quả không nhất quán | 2, 8 |
| Kết quả cuối sai người, sai giá trị, đảo thành và không thành | 6 |
| Người không đủ điều kiện vẫn tạo ra kết quả | 5 |
| Dữ liệu hoặc trách nhiệm bị gắn nhầm sang người khác | 10 |
| Văn bản pháp lý lệch dữ liệu, ký sai, ký dở | 7, 11 |
| Lộ dữ liệu cá nhân hoặc dữ liệu tổ chức khác | 12 |
| Số sai mà người ra quyết định vẫn tin | 4 |
| Mất dấu vết | 13 |
| Người trong hệ thống làm lệch kết quả không để lại dấu vết | 15 |

---
