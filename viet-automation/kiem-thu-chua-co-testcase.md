# Kiểm hệ thống bằng automation khi chưa có testcase

Dùng cho chế độ B của skill `viet-automation`: dev vừa code xong, bản đã deploy, chưa có bộ testcase manual. Mục tiêu là tìm lỗi sớm và phủ rộng, không chỉ chạy happy path hay E2E.

Bài học từ lần làm đầu (một dự án trước): lần chạy đầu chỉ lấy 69 mục chọn lọc từ BR và AC, bị hụt cả một lớp case biên, dữ liệu kỳ quặc, trạng thái lỗi, hết phiên, phân quyền. Bảng ở mục 3 là danh sách tối thiểu để không lặp lại.

## 1. Nguồn sinh case

| Nguồn | Phủ phần nào | Cách dùng |
|:---|:---|:---|
| FSD: Business Rules và Tiêu chí chấp nhận | Phần riêng của dự án: luồng nghiệp vụ, quy tắc, câu thông báo, ảnh hưởng chéo giữa các cổng | Mỗi BR và mỗi dòng AC có ít nhất một mục luồng thuận và một mục ngoại lệ. Câu thông báo so **nguyên văn** |
| Checklist chung: `Testcase_Template.md` tầng 0, cộng các checklist mà file điều phối của dự án bật | Phần dự án nào cũng có: biên, ký tự đặc biệt, phân trang, lọc kết hợp, trạng thái rỗng, lỗi, hết phiên, phân quyền, bấm nhiều lần, xuất nhập file | Đi lần lượt các nhóm ở bảng mục 3, mỗi mục ghi rõ đang lấy từ mục nào của template |
| Tư duy test: `<SKILL_BA>/viet-testcase/tu-duy-test.md` và mục 4 file này | Chỗ FSD và checklist không nói tới: dữ liệu kỳ quặc, thao tác sai thứ tự, đồng thời, đổi đường dẫn, khổ màn hình | Mỗi màn tự đặt câu hỏi "người dùng thật hoặc người phá có thể làm gì mà tài liệu không nghĩ tới" |
| Design hoặc mockup (nếu có) | Bố cục, chữ hiển thị, thành phần, màu và cỡ | Theo mục 5 |

FSD không nói hệ thống phải làm gì ở một tình huống thì ghi "Cần xác nhận", không kết luận là lỗi. Hệ thống làm khác FSD nhưng hợp lý thì hỏi người dùng có cập nhật FSD theo hệ thống không.

**Không có FSD và tiêu chí chấp nhận:** mong muốn lấy từ checklist chung, quy ước phổ biến của web và sự nhất quán của chính hệ thống (cùng một quy tắc ở hai màn phải giống nhau). Mục hệ thống chạy được nhưng không có căn cứ thì ghi Cần xác nhận kèm hành vi đang thấy, không ghi Đạt. Cuối báo cáo liệt kê các quy tắc suy ra để người dùng chốt, dùng làm đầu vào cho FSD.

## 2. Phân tích rủi ro, ưu tiên và tiêu chí dừng

Trước khi lập bản đồ phủ, viết 3 đến 5 câu "hệ thống này hỏng ở đâu thì thiệt hại nhất", ví dụ: mất dữ liệu người dùng vừa nhập, lộ dữ liệu cá nhân, sai quyền, sai số liệu dùng để báo cáo, khóa nhầm người dùng. Lưu ở đầu file kết quả.

| Lớp | Nhóm | Lý do |
|:---|:---|:---|
| Chạy trước | Phân quyền, an ninh hộp đen, ảnh hưởng chéo, chuyển trạng thái, mất dữ liệu khi lỗi hoặc hết phiên, xuất nhập file | Lỗi ở đây gây thiệt hại lớn nhất |
| Chạy sau | Trường nhập, tính duy nhất, ngày tháng, tệp tải lên, thêm sửa xóa, danh sách, thông báo | Lỗi thường gặp nhất |
| Chạy cuối | Giao diện, khổ màn hình, bàn phím, nhóm khóa tài khoản, nhóm thử giới hạn tần suất | Ít ảnh hưởng nghiệp vụ, hoặc làm khóa tài khoản |

**Dừng mở rộng một màn** khi: mọi dòng của bản đồ phủ đã có kết quả hoặc lý do không chạy; mỗi BR có ít nhất một mục luồng thuận và một mục ngoại lệ. Gặp 3 lỗi cùng một nguyên nhân thì gộp thành một lỗi, không sinh thêm biến thể.

## 3. Bản đồ phủ tối thiểu cho mỗi màn

Trước khi chạy, lập bảng cho từng màn, mỗi nhóm một dòng gồm các cột: **Màn | Nhóm | Mục sẽ kiểm | Nguồn | Dữ liệu cần dựng | Kỹ thuật**. Dữ liệu cần dựng là trạng thái bản ghi, tài khoản vai trò, tệp đặc biệt phải có trước. Kỹ thuật là biên, phân vùng tương đương, bảng quyết định, chuyển trạng thái, đoán lỗi. Đưa người dùng duyệt nhanh phạm vi, không cần viết testcase chi tiết.

Màn có bản ghi nhiều trạng thái thì liệt kê các trạng thái, các chuyển hợp lệ và không hợp lệ trước khi chạy. Mỗi chuyển là một mục kiểm.

Cột Mục template ghi số kèm tên mục để vẫn tra được khi template của dự án đánh số khác template chung.

| Nhóm | Mục bắt buộc kiểm | Mục template |
|:---|:---|:---|
| Giao diện so với FSD | Đủ trường, đủ cột, đủ nút; nút hiện ẩn, bật tắt đúng điều kiện; giá trị mặc định; gợi ý trong ô; tiêu đề màn | 2 Trạng thái mặc định, 13 Enable/Disable |
| Trường nhập | Bỏ trống; chỉ gồm khoảng trắng; nhập **đúng giới hạn** ký tự rồi lưu được; gõ ký tự **vượt giới hạn 1** bị chặn; gọi thẳng API với chuỗi vượt giới hạn bị máy chủ từ chối; ký tự đặc biệt, emoji, tiếng Việt có dấu; đoạn mã `<script>`, `<img onerror>` hiển thị nguyên văn và không chạy ở mọi nơi hiện lại; khoảng trắng đầu cuối bị cắt | 5.1 Ô nhập liệu, 5.7 Nhiều dòng |
| Tính duy nhất | Trùng tên khác chữ hoa chữ thường, khác khoảng trắng hai đầu; trùng trong phạm vi cha khác thì vẫn được; trùng với bản ghi đã xóa mềm | 3.2 Biến thể chuỗi, 3.3 Tổ hợp, 3.4 Xóa mềm |
| Ngày tháng | Kết thúc trước bắt đầu; hai ngày bằng nhau; chỉ nhập một ngày; ngày trong quá khứ; định dạng hiển thị | 5.3 Chọn ngày, 8.1 Giữa nhiều trường |
| Tệp tải lên | Mỗi định dạng hợp lệ một tệp; định dạng sai; **đổi đuôi** để lách; tệp đúng bằng dung lượng tối đa và vượt 1 byte, kiểm **cả hai cách hiểu MB** (100 × 10^6 và 100 × 2^20 byte), lệch nhau thì ghi Cần xác nhận; tệp biên là tệp hợp lệ được độn thêm nội dung, không phải tệp toàn số 0 đổi đuôi; Đạt khi tải xong, có trên danh sách, tải về đúng kích thước; tệp 0 byte; mất mạng giữa lúc tải; chọn tệp thứ hai thay tệp đầu; gọi thẳng API với tệp vượt giới hạn | 5.9 Tải tệp, 15.1 Mất mạng |
| Thêm, sửa, xóa | Thêm thành công và vị trí bản ghi mới; sửa rồi thấy giá trị mới ở mọi nơi hiện; xóa có hỏi xác nhận, Hủy thì còn nguyên; câu thông báo sau mỗi thao tác; **bấm lưu hai lần liên tiếp** chỉ tạo một bản ghi; mở cùng màn từ các lối vào khác nhau; có Hoàn tác, khôi phục thì kiểm; có nhật ký thao tác thì kiểm người, hành động, giá trị cũ và mới | 6 Post-action, 6.6 Theo lối vào, 7 Lưu trữ, 10 Xóa, 15.3 Double-submit, 26 Hoàn tác, 8.6 Nhật ký |
| Danh sách | Sắp xếp mặc định; phân trang khi **vượt** số dòng mỗi trang; đổi số dòng mỗi trang; tìm không dấu, tìm một phần; lọc kết hợp nhiều điều kiện; đổi bộ lọc khi đang ở trang 2 thì về trang 1; Xóa bộ lọc; giữ bộ lọc, trang khi quay lại từ màn chi tiết; không có kết quả; chưa có dữ liệu | 4.1 tới 4.6 |
| Nhập hàng loạt | Sai mẫu; chỉ có dòng tiêu đề; dòng lỗi lẫn dòng đúng; trùng trong file; trùng với dữ liệu đã có; dữ liệu phụ thuộc sai (xã không thuộc tỉnh); số điện thoại mất số 0 đầu do Excel; file vượt dung lượng; file vượt số dòng tối đa; nhập lại cùng file. Mục kiểm giới hạn dùng dữ liệu cố tình sai ở mọi dòng để không tạo bản ghi và không gửi email | 20.1 tới 20.5 |
| Xuất file | Tải về rồi **mở file đọc từng cột**, không chỉ kiểm có file; xuất khi đang lọc; xuất khi không có dòng nào; tên file; giá trị bắt đầu bằng `=`, `+`, `-`, `@` không thành công thức khi mở bằng Excel | 19.1 tới 19.3 |
| Thông báo, email | Đúng người nhận, đúng điều kiện gửi, không gửi trùng khi bấm lại, giá trị động đúng, liên kết trong email mở đúng màn và hết hạn đúng | 18.1 tới 18.3 |
| Cấu hình bật tắt | Chức năng có bật tắt thì kiểm cả hai trạng thái. Không tự bật được thì ghi Bị chặn kèm câu hỏi cho dev: tắt có chủ ý không, bật ở đâu | 14 Cấu hình |
| Trạng thái màn hình | Đang tải; rỗng; không có kết quả lọc; **lỗi mạng** và **máy chủ báo lỗi** (chặn request bằng `page.route`) khi tải và khi lưu, dữ liệu đang nhập còn nguyên; trang không tồn tại | 15.1, 15.2, 15.4 |
| Phiên đăng nhập | Trước khi kiểm, xác định phiên lưu ở cookie hay localStorage, xóa đúng chỗ đó. Hết phiên khi đang xem, khi đang nhập dở popup, khi bấm lưu; đăng nhập lại quay về đúng màn; **quyền bị thu hồi khi phiên còn hiệu lực** (khóa tài khoản, gỡ khỏi phạm vi, đổi vai trò ở cổng quản trị rồi thao tác tiếp ở phiên đang mở); đăng xuất ở tab này thì tab kia ra sao; Ghi nhớ đăng nhập; đăng xuất rồi bấm Back | 16.2 Session timeout, 9.5 Đổi quyền khi đang dùng |
| Đăng nhập, mật khẩu | Sai mật khẩu và tài khoản không tồn tại cùng một câu báo; khóa sau N lần sai (chạy cuối, hỏi trước khóa theo tài khoản hay IP); quên mật khẩu với tài khoản có và không có; liên kết đặt lại chỉ dùng một lần; đổi mật khẩu đủ mọi điều kiện độ mạnh, trùng mật khẩu cũ, xác nhận lệch | 5.1, 9.1, 16.2 |
| Phân quyền | Vai trò này mở đường dẫn của vai trò khác; tài khoản cổng này đăng nhập cổng kia; đổi ID trên đường dẫn sang bản ghi người khác; **gọi thẳng API** khi giao diện đã ẩn nút; mỗi vai trò thấy đúng tập trường | 9.1 tới 9.6 |
| An ninh hộp đen | Mở từng API của màn, đối chiếu trường trả về với trường hiện trên màn, có dữ liệu cá nhân thừa là Lỗi Cao. Đường dẫn tải đã lấy **trước** khi bị ẩn hoặc gỡ quyền còn dùng được không, dùng được bao lâu. Gửi quên mật khẩu 10 lần liền xem có giới hạn không (chạy cuối). Tải lên SVG có script, tệp tên chứa mã hoặc `../`. Cookie phiên có HttpOnly, Secure, SameSite | 9.3, 19.3, tư duy test |
| Chuyển trạng thái | Mỗi trạng thái kiểm thao tác được và không được; đổi trạng thái thì hệ quả ở nơi khác; thao tác bị chặn ở máy chủ chứ không chỉ ẩn nút; thứ tự thao tác ngược | 25.1 tới 25.4, 8.8 |
| Ảnh hưởng chéo | Dữ liệu cổng này tạo hiện ở cổng kia; ẩn, xóa, dừng ở cổng này thì cổng kia mất quyền ngay, kể cả đường dẫn cũ đang giữ; số liệu tổng hợp cập nhật theo; nhiều người cùng sửa | 12.1, 16.1, 27.1 tới 27.6 |
| Thời gian | Hiệu lực có hạn (mật khẩu tạm, liên kết có chữ ký, khóa tạm thời); đếm ngược; tự đổi trạng thái theo ngày | 28.1 tới 28.6 |
| Bàn phím, trợ năng cơ bản | Mở popup thì con trỏ ở ô đầu; Tab đi đúng thứ tự, bỏ qua phần tử ẩn hoặc khóa; Enter không gửi form khi chưa đủ điều kiện; Esc đóng popup và có hỏi khi có thay đổi chưa lưu; nhãn gắn với ô nhập. Chạy axe-core ở mỗi màn, chỉ báo vi phạm mức critical và serious | 17.1, 17.2 |
| Khổ màn hình, trình duyệt, ngôn ngữ | Chụp ở 1280, 1366, 1440, 1920: cột bảng không bị bóp, chữ dài không tràn, nút không bị đẩy ra ngoài. Cấu hình dự án ghi có người dùng điện thoại thì thêm 390 × 844 và 768. Ghi có người dùng Safari thì chạy luồng chính một lần trên WebKit. Có chọn ngôn ngữ thì đổi ngôn ngữ, rà chữ chưa dịch, chữ dài làm vỡ bố cục, định dạng ngày | 21.1, 21.4 |

Mục nào không áp dụng cho màn thì ghi lý do ở bản đồ phủ, không bỏ im lặng.

## 4. Tư duy sinh case phi logic

Những case dưới đây hay tìm ra lỗi thật mà FSD không bao giờ nhắc. Chọn cái hợp với màn, không cần chạy hết.

**Dữ liệu kỳ quặc**
- Chuỗi 255 ký tự **không có dấu cách** ở cột tên: hay làm bảng tràn ngang, mất nút thao tác.
- Họ tên bắt đầu bằng ký tự đặc biệt hoặc số, ví dụ `[Nhóm 1] Nguyễn Văn A` (chỉ dùng cho mục kiểm avatar, tên dữ liệu thử vẫn theo quy ước `Thử nghiệm ...`): avatar chữ cái đầu lấy sai.
- Tên toàn emoji, toàn số, toàn dấu chấm; tên có dấu nháy đơn, dấu `&`, `<`, `>`; tên bắt đầu bằng `=1+1`.
- Số điện thoại có dấu cách, dấu chấm, `+84`, 9 chữ số; email có chữ hoa, có dấu `+alias`.
- Tệp trùng tên với tệp đã tải; tệp tên tiếng Việt có dấu và dấu cách; tệp nhiều trang, nhiều slide, nhiều sheet (kiểm xem trước có lật trang).

**Thao tác sai thứ tự, sai lúc**
- Bấm Back của trình duyệt sau khi lưu, sau khi đăng xuất.
- F5 giữa lúc đang tải tệp hoặc đang nhập dở.
- Mở lại đường dẫn của bản ghi vừa bị xóa, bị ẩn; mở liên kết đã dùng một lần.
- Bấm lưu rồi đóng popup ngay; bấm lưu khi tệp còn đang tải.
- Thao tác ở tab cũ sau khi tab khác đã đổi trạng thái.

**Nhiều người, nhiều lần**
- Hai tab cùng sửa một bản ghi, tab sau lưu đè.
- Bấm nút lưu, nút import liên tục.
- Người A đang xem thì người B xóa hoặc ẩn dữ liệu đó, A bấm tiếp.

**Phá từ bên ngoài giao diện**
- Đổi ID, đổi đường dẫn, thêm tham số vào URL.
- Gọi thẳng API xin dữ liệu, xin đường dẫn tải sau khi đã mất quyền; dùng lại đường dẫn có chữ ký đã cấp trước đó.
- Dán liên kết `javascript:` vào ô soạn thảo, rồi bên xem lại bấm vào.

**Hiển thị**
- Số lớn, số 0, giá trị trống hiện gì ("Chưa cập nhật", "-").
- Số đếm ở tab, ở thẻ tổng hợp khớp với số dòng thật.
- Phần trăm làm tròn đúng chiều.

## 5. Đối chiếu giao diện với design

Làm khi dự án có design hoặc mockup.

1. **Liệt kê hết** các tệp trong bộ design (giải nén, đọc toàn bộ danh sách, không chỉ vài chục tệp đầu). Lần làm đầu bỏ sót ba khung design mới vì chỉ đọc 60 tệp đầu của file zip, dẫn tới hai kết luận sai.
2. Ghi tên tệp và ngày của bộ design đã dùng ở đầu file đối chiếu.
3. Xác định khổ khung của design (ảnh xuất thường ở tỉ lệ 2x). Chụp hệ thống đúng khổ đó, `device_scale_factor=2`.
4. Ghép ảnh design và ảnh hệ thống cạnh nhau, so từng màn theo bốn điểm: bố cục và thứ tự khối; chữ hiển thị (tiêu đề, nhãn, gợi ý, chữ trên nút); thành phần có hoặc thiếu; màu, cỡ chữ, kiểu nút (lấy mẫu mã màu trên ảnh, đọc `getComputedStyle` trên trang).
5. Bảng chụp thêm ở 1280, 1440, 1920. Modal xem trước kiểm bằng tệp nhiều trang, nhiều slide, nhiều sheet (tạo tệp thử, tải lên, kiểm xong xóa).
6. Phân mỗi chỗ lệch vào một trong bốn loại: lỗi cần báo dev; lệch nhưng hệ thống đúng FSD (design cần cập nhật); cần người dùng chốt; lỗi chép của design (báo designer). Nghiệp vụ theo FSD, bố cục theo design, trừ khi cấu hình dự án quy định khác.
7. Ghi vào file `Đối chiếu giao diện với design.md`, mỗi lỗi kèm ảnh cắt hai bên. Lỗi giao diện dùng chung dãy mã BUG-xx với file kết quả.
8. Chạy lại khi dev sửa: phạm vi gồm các màn dev báo đã sửa, cộng mọi lỗi giao diện đang Mở của cổng đó. Lỗi không chạy lại thì giữ trạng thái cũ và ghi "chưa chạy lại ở L2". Kết luận cũ sai thì sửa lại và nói rõ đã sửa.

## 6. Quy tắc khi chạy

**Bảo mật**
- Thông tin đăng nhập và email test đọc từ file dữ liệu hoặc cấu hình dự án, không in ra, không viết cứng vào kịch bản, kết quả hay ảnh.
- Che vùng tài khoản bằng `screenshot(mask=[locator])` theo phần tử, không theo tọa độ cố định. Che xong mở lại một ảnh mỗi khổ màn hình để kiểm.
- Lọc thông tin nhạy cảm ở **mọi chỗ ghi ra**: JSON, chữ in ra màn hình, file md.
- Tệp phiên (`storage_state`), trace, HAR, tệp tải về có dữ liệu cá nhân chỉ để trong thư mục tạm ngoài dự án, xóa khi chạy xong. Trace chứa cookie và chữ đã gõ, chỉ lưu máy, không gửi ai.
- Tạo `.gitignore` trong thư mục Automation cho file thông tin đăng nhập, `ket-qua/**/trace*`, `*.har`, tệp phiên, tệp xuất có dữ liệu cá nhân.

**Dữ liệu**
- Chỉ sửa, ẩn, dừng bản ghi do chính lần chạy tạo ra. Bản ghi của người khác chỉ đọc.
- Trước khi sửa, lưu giá trị cũ. Trả lại trong `try/finally` và ghi một mục kiểm "đã trả lại".
- Tên dữ liệu thử: `Thử nghiệm DD/MM/YYYY hh:MM:ss`. Ghi mã và đường dẫn bản ghi đã tạo vào `ket-qua/trang-thai/*.json` để đợt sau, bước chạy lại và việc dọn dùng tiếp.
- Tài khoản thử dùng email `+alias` của email test gốc.
- Import hay tạo tài khoản hàng loạt có gửi email thật thì hỏi trước.

**Email và mật khẩu**
- Nhóm cần đọc email tách thành đợt riêng có điểm dừng: kịch bản báo "cần dán liên kết của <alias> vào <file>", thiếu thì ghi Không tạo được tình huống.
- **Mật khẩu mới** sinh ra khi kiểm đổi mật khẩu: ghi vào file dữ liệu **trước** khi bấm lưu. Trước khi chạy nhóm này, thử ghi vào file dữ liệu; ghi không được (file đang mở trong Word bị Windows khóa) thì dừng và nhắc người dùng đóng file, không bấm lưu.
- Nhóm khóa tài khoản và nhóm thử giới hạn tần suất chạy cuối, báo người dùng thời gian bị khóa.

**Chờ và ổn định**
- Chờ theo điều kiện, không chờ cứng: chờ phần tử hiện hoặc ẩn, chờ đúng phản hồi API (`expect_response` theo đường dẫn và mã trả về), chờ URL. Hạn chế `wait_for_timeout`.
- Mục ra Lỗi thì tự chạy lại 2 lần. Kết quả không ổn định thì ghi "Không ổn định" ở cột Thực tế và xem tay, không kết luận Lỗi.

**Bằng chứng**
- Bật `context.tracing` (có ảnh từng bước) cho mỗi nhóm. Nhóm có mục Lỗi thì giữ trace để dựng lại chuỗi thao tác, nhóm không lỗi thì xóa.
- Mỗi mục Lỗi có ảnh chụp đúng lúc lỗi ở tỉ lệ 2x, ghi khổ khung nhìn vào JSON, kèm bước tái hiện.
- Bắt lỗi ngầm: `page.on("console")` mức error, `page.on("pageerror")`, phản hồi từ 500 trở lên hoặc 4xx ngoài chủ đích, cảnh báo mixed content. Ghi vào trường `loi_ngam` của mục đang chạy. Lỗi JS hoặc 5xx xuất hiện trong luồng Đạt thì vẫn tạo mục Lỗi riêng.

**Chống báo nhầm**
1. Mong muốn là một giá trị cụ thể, không viết "A hoặc B". Chưa biết giá trị đúng thì ghi Cần xác nhận.
2. Câu thông báo so nguyên văn, không kiểm "có chứa số".
3. Kiểm vắng mặt (không tạo, đã mất) phải kèm đối chứng: cùng cách tìm phải tìm ra được một bản ghi có thật.
4. Lỗi giao diện đo bằng số: `scrollWidth > clientWidth`, vị trí `getBoundingClientRect` nằm ngoài khung nhìn, `document.activeElement`, `getComputedStyle`. Ghi số đo vào cột Thực tế.
5. Hết mỗi đợt, ghép mọi ảnh thành một tờ xem nhanh rồi rà bằng mắt. Lỗi thấy trên ảnh mà kịch bản chưa có thì thêm mục kiểm có mã, không chỉ ghi chú.
6. Mở lại từng mục Lỗi bằng tay hoặc bằng một kịch bản nhỏ riêng trước khi báo. Lần làm đầu có cả báo nhầm Đạt (bộ đọc thẻ sai, đánh giá ảnh sai) lẫn báo nhầm Lỗi.

**Tổ chức kịch bản**
- Chép `mau_chung.py` của skill vào thư mục Automation thành `chung.py`: ghi kết quả, chụp và che, chờ API, bắt lỗi ngầm, trace, lưu trạng thái, thử ghi file.
- Mỗi kịch bản đợt nhận tham số chọn nhóm để chạy lại riêng một nhóm.
- Chạy lâu thì chạy nền, chia đợt theo màn hoặc theo cổng.

## 7. Case chính và phần chạy ngầm

Dùng khi người dùng yêu cầu xem trình duyệt trong lúc chạy. Không yêu cầu xem thì mọi thứ chạy ngầm.

**Case chính (bật cửa sổ khi được yêu cầu xem):**

| # | Nhóm | Gồm những gì |
|:---|:---|:---|
| 1 | Luồng nghiệp vụ từ đầu tới cuối | Đi trọn một vòng nghiệp vụ qua mọi vai trò, ví dụ: quản trị tạo dữ liệu gốc, người dùng cuối dùng dữ liệu đó và tạo kết quả, quản trị xem kết quả và ra quyết định, người dùng cuối thấy quyết định |
| 2 | Luồng tích hợp giữa các cổng | Dữ liệu cổng này tạo hiện đúng ở cổng kia; đổi trạng thái ở cổng này (ẩn, dừng, cấp, xóa) thì cổng kia đổi theo ngay; số liệu tổng hợp cập nhật |
| 3 | Happy case từng màn | Mỗi thao tác chính của mỗi màn làm thành công một lần |
| 4 | Validate cơ bản | Bỏ trống trường bắt buộc, chỉ gồm khoảng trắng, giới hạn ký tự, trùng, ngày sai, tệp sai định dạng hoặc quá dung lượng, import sai mẫu, mật khẩu không đủ điều kiện |
| 5 | Thêm sửa xóa cơ bản và hệ quả hiển thị | Thêm xong ở đúng vị trí và có thông báo; sửa xong giá trị mới hiện mọi nơi; xóa có hỏi lại, Hủy thì còn nguyên; số đếm cập nhật |

**Luôn chạy ngầm:**

| Nhóm | Lý do |
|:---|:---|
| Responsive | Kết quả là số đo tràn ngang, xem cửa sổ đổi khổ liên tục không có ích |
| An ninh hộp đen | Phần lớn diễn ra ngoài giao diện |
| Biên tệp lớn, tệp 0 byte, tệp có mã | Tải tệp lớn rất lâu, giao diện không đổi |
| Bàn phím, trợ năng | Kết quả là danh sách vi phạm |
| Lỗi mạng, lỗi 5xx, hết phiên | Giả lập bằng chặn request, xóa cookie |
| Case phi logic | Cần kiểm bằng số liệu, xem nhanh dễ hiểu nhầm |
| Phân trang, lọc kết hợp, xuất file đọc từng cột | Nhiều bước lặp, kết quả đọc từ bảng và file |
| Đối chiếu design | Chụp ảnh rồi so trên ảnh ghép |
| Đăng nhập sai, khóa tài khoản, giới hạn tần suất | Lặp cùng một thao tác, làm khóa tài khoản |
| Chạy lại sau khi sửa kịch bản | Chỉ để lấy lại kết quả |

Bản đồ phủ (mục 3) đánh dấu nhóm nào là case chính để bộ chạy biết bật cửa sổ ở bước nào.


## 8. Chạy ngầm không được giấu lỗi

Chạy ngầm là mặc định, nên mọi khác biệt giữa trình duyệt chạy ngầm và trình duyệt người dùng thật đều là chỗ lọt lỗi. Ví dụ đã gặp: nút Tải xuống ở popup Xem trước PDF trên Chrome thật mở đè PDF lên trang, mất phần đang sửa; bản chạy ngầm rút gọn của Playwright lại tải tệp về bình thường nên kịch bản chấm Đạt.

**Ba lớp chặn, áp cho mọi lần chạy ngầm:**

| Lớp | Làm gì | Cách làm |
|:---|:---|:---|
| 1. Chạy ngầm bằng Chrome đầy đủ | Không dùng bản `chromium-headless-shell` rút gọn (mặc định của Playwright khi chỉ ghi `headless=True`). Bản rút gọn không có trình xem PDF và xử lý tải tệp, mở tab, in khác Chrome thật | Python `launch(headless=True, channel="chromium")`. TypeScript `channel: 'chromium'` trong `playwright.config`. `mo()` của `<SKILL_BA>/verify-bug/mau_verify.py` đã làm sẵn |
| 2. Kiểm hậu quả sau mỗi thao tác tải, xuất, in, mở liên kết | Bắt buộc có tệp tải về thật và đúng tên; trang chính không tự chuyển sang địa chỉ khác (`blob:`, `data:`, tệp PDF); không mở tab lạ; popup đang mở vẫn còn và giữ phần đang sửa | `kiem_tai(page, bam, duong_dan)` trong `mau_verify.py`, kết quả `dat` False là Lỗi |
| 3. Soi cách code tạo liên kết | Ghi lại mọi liên kết được bấm. Liên kết `blob:`, `data:` không có thuộc tính `download` là rủi ro, kể cả khi trình duyệt chạy ngầm không lộ hậu quả. Đây cũng là chỗ dev cần sửa, ghi vào Note của bug | `gan_canh_gac(ctx)` (mo() tự gắn), đọc ở trường `link_rui_ro` của `kiem_tai` |

**Thao tác phải đi qua `kiem_tai` hoặc kiểm tương đương:** tải tệp, xuất Excel/PDF, xem trước rồi tải, in, mở liên kết ngoài, sao chép vào bộ nhớ tạm, mở tệp trong tab mới.

**Khác biệt còn lại cần biết khi đọc kết quả chạy ngầm:**

- Trang chạy ngầm không giữ focus cửa sổ (`document.hasFocus()` có thể là false): case focus, phím tắt, bộ nhớ tạm kiểm lại bằng một lượt có giao diện nếu nghi ngờ.
- Hộp thoại gốc của trình duyệt (in, chọn tệp hệ điều hành, xác nhận rời trang) không hiện ra: kiểm bằng sự kiện, không kiểm bằng ảnh.
- Phông chữ, độ mượt hình ảnh có thể khác chút ít: đối chiếu design chỉ kết luận lệch khi chênh rõ, không kết luận theo từng pixel.

Lỗi chỉ lộ khi bật cửa sổ mà ba lớp trên không bắt được thì ghi thêm vào mục này để lần sau chặn được.
