# Danh mục bộ checklist sinh testcase

`/viet-testcase` và `/viet-automation` đọc file này trước khi sinh case. Skill dò **dấu hiệu** trong tài liệu đặc tả (SRS, FSD, CR, BRD) để tự bật checklist, không hỏi người dùng. Gặp năng lực hoặc domain **chưa có bộ** thì skill dừng và nhắc người dùng theo mục 5, người dùng đồng ý mới tạo.

---

## 1. Bốn tầng

| Tầng | File | Bật khi |
|:---|:---|:---|
| 0. Giao diện và dữ liệu | `../Testcase_Template.md` (mục 1 đến 37) | Luôn bật |
| 1. Rủi ro nghiệp vụ chung | `QA-Business-Risk-Core-Checklist.md` (17 nhóm) | Luôn bật. Từng nhóm tự bật theo dấu hiệu ghi ở đầu nhóm |
| 2. Năng lực | Các file `QA-*` và `Template_Testcase_Advanced.md` ở mục 2 | Theo dấu hiệu ở mục 2 |
| 3. Domain | Các file `domain/domain-*.md` ở mục 3 | Theo dấu hiệu ở mục 3 |
| Tư duy test | `../../viet-testcase/tu-duy-test.md` | Luôn chạy sau cùng để tìm case ngoài tài liệu |

Thứ tự chạy: tầng 0 → tầng 1 → tầng 2 → tầng 3 → tư duy test → `QA-States-Errors-Notification-Checklist.md` Mục H (rà soát cuối) → đối chiếu mọi BR/AC có ít nhất một case.

---

## 2. Checklist năng lực đã có (tầng 2)

| File | Dấu hiệu trong tài liệu | Bật |
|:---|:---|:---|
| `QA-States-Errors-Notification-Checklist.md` | Mọi màn hình. Thêm khi có thông báo, email, SMS, push, chuông | Luôn bật |
| `QA-Adversarial-Integrity-Checklist.md` | Tiền, điểm, xếp hạng, quyền duyệt, dữ liệu nhạy cảm, kết quả có hậu quả với người thật | Khi có từ 1 dấu hiệu |
| `Template_Testcase_Advanced.md` | Realtime, WebSocket, hàng đợi, offline, ghép nối, chuỗi nhiều bước, cổng thanh toán, webhook, đối soát, theo dõi vị trí, đánh giá hai chiều | Từng mục theo dấu hiệu |
| `QA-Mobile-Native-Checklist.md` | App iOS, Android, cài từ store, thông báo đẩy, quyền camera, vị trí | Khi có app |
| `QA-Identity-Account-Linking-Checklist.md` | Tài khoản, đăng ký, đăng nhập Google/Facebook, xác minh danh tính, eKYC, trùng tài khoản | Khi có tài khoản người dùng |
| `QA-Metrics-Listing-Checklist.md` | Dashboard, báo cáo, thống kê, biểu đồ, danh sách có bộ lọc, xuất báo cáo | Khi có |
| `QA-Public-Share-Link-Checklist.md` | Chia sẻ liên kết, mã QR, trang công khai không cần đăng nhập | Khi có |
| `QA-AI-Assisted-Review-Checklist.md` | AI, máy đề xuất, trích xuất tự động, người duyệt kết quả máy | Khi có |
| `QA-Data-Crawling-Checklist.md` | Thu thập dữ liệu, quét nguồn ngoài, crawl, đồng bộ từ nền tảng khác | Khi có |
| `QA-Scoring-RuleBase-Checklist.md` | Bộ tiêu chí, trọng số, điểm, ngưỡng, chấm điểm theo quy tắc | Khi có |
| `QA-Ranking-Leaderboard-Checklist.md` | Xếp hạng, bảng xếp hạng, top, thứ hạng theo kỳ | Khi có |
| `QA-TV-App-Checklist.md` | App TV, điều khiển D-pad, màn hình lớn | Khi có |
| `QA-Voice-Interaction-Checklist.md` | Ra lệnh giọng nói, đọc thành tiếng, trợ lý giọng nói | Khi có |
| checklist riêng cho thiết bị màn hình gắn tường (không kèm trong gói) | Thiết bị màn hình gắn tường dùng chung, AOSP không GMS | Khi có |

---

## 3. Thư viện domain (tầng 3)

| Domain | File | Trạng thái | Dấu hiệu nhận biết (đủ từ 3 dấu hiệu thì coi là thuộc domain) |
|:---|:---|:---|:---|
| Đấu giá trực tuyến | `domain/domain-dau-gia.md` | Chưa có bộ | phiên, cuộc đấu, giá khởi điểm, bước giá, trả giá, giá trúng; tiền đặt trước, hoàn cọc, mất cọc; gia hạn, đếm ngược; rút lại giá, điểm danh; quy chế, biên bản đấu giá |
| Giám sát dữ liệu, chấm điểm | `domain/domain-giam-sat-cham-diem.md` | Chưa có bộ | quét theo lịch, nguồn, nền tảng mạng xã hội; bộ tiêu chí, trọng số, ngưỡng; từ khóa loại trừ; sắc thái nội dung; hồ sơ đối tượng bị giám sát; cảnh báo, danh sách theo dõi |

Domain khác chưa có bộ. Gặp thì nhắc theo mục 5. Một số domain hay gặp và dấu hiệu, để nhận diện:

| Domain | Dấu hiệu |
|:---|:---|
| Thương mại điện tử | giỏ hàng, đơn hàng, tồn kho, mã giảm giá, vận chuyển, đổi trả |
| Đặt lịch, đặt chỗ | khung giờ, giữ chỗ, hết chỗ, danh sách chờ, đổi lịch, hủy lịch, check-in |
| Học tập, đào tạo | khóa học, bài học, học liệu, tiến độ học, bài kiểm tra, chứng chỉ |
| Tài chính, ví | ví, số dư, nạp, rút, chuyển tiền, hạn mức giao dịch, sao kê, đối soát |
| Quy trình hồ sơ, phê duyệt | hồ sơ, trình duyệt, cấp duyệt, trả lại, ủy quyền, văn bản, ký số |
| Mạng xã hội, nội dung | bài đăng, bình luận, thích, theo dõi, báo cáo vi phạm, kiểm duyệt |
| Y tế | bệnh nhân, lịch khám, đơn thuốc, kết quả xét nghiệm, hồ sơ bệnh án |
| Vận chuyển | vận đơn, tài xế, lộ trình, trạng thái giao hàng, COD |
| Nhân sự | chấm công, nghỉ phép, bảng lương, ca làm, hợp đồng lao động |
| IoT, thiết bị | thiết bị, cảm biến, firmware, kết nối, điều khiển từ xa |

---

## 4. Năng lực chưa có checklist (tạo khi gặp)

| Năng lực | Dấu hiệu trong tài liệu | Đang phủ một phần ở | Mức cần |
|:---|:---|:---|:---|
| Xác thực nâng cao (MFA, SSO, đổi email/SĐT đăng nhập) | xác thực hai lớp, SSO, đăng nhập một lần, đổi số điện thoại đăng nhập | Testcase_Template 29 | Cao |
| Quy trình phê duyệt nhiều cấp | duyệt, trình duyệt, cấp duyệt, trả lại, ngưỡng duyệt theo số tiền | Testcase_Template 25, 26; tầng 1 nhóm 7 | Cao |
| Văn bản từ mẫu, ký số, hóa đơn điện tử | hợp đồng, mẫu in, xuất PDF, chữ ký số, USB token, hóa đơn điện tử, số hiệu văn bản | Testcase_Template 19; tầng 1 nhóm 11 | Cao |
| Đa tổ chức, gói dịch vụ | tổ chức, chi nhánh, workspace, gói, dùng thử, nâng cấp gói | tầng 1 nhóm 12, 17 | Cao với SaaS |
| Đặt lịch và giữ chỗ | đặt lịch, khung giờ, giữ chỗ, hết chỗ, danh sách chờ | Testcase_Template 28; tầng 1 nhóm 2, 8 | Trung bình |
| Ví, số dư, sổ cái | ví, số dư, nạp, rút, điểm thưởng, công nợ | Template_Testcase_Advanced E; tầng 1 nhóm 1 | Trung bình |
| Tính giá, khuyến mãi | bảng giá, khuyến mãi, voucher, chiết khấu, phí vận chuyển | Testcase_Template 32.3; tầng 1 nhóm 4 | Trung bình |
| Đa ngôn ngữ cho web | đa ngôn ngữ, chuyển ngôn ngữ, bản dịch, đơn vị tiền khác | Testcase_Template 32 | Trung bình |
| Kho tài liệu | thư mục, phiên bản tệp, chia sẻ tệp, xem trước | Testcase_Template 35 | Trung bình |
| Nhắn tin, bình luận realtime | chat, tin nhắn, bình luận, nhắc tên, đã xem | Testcase_Template 12.2 | Trung bình |
| API mở cho bên thứ ba | API key, đối tác tích hợp, webhook gửi ra, giới hạn gọi | Template_Testcase_Advanced E | Trung bình |
| Tìm kiếm toàn văn có xếp hạng | tìm kiếm thông minh, gợi ý từ khóa, mức độ liên quan | Testcase_Template 4.4 | Thấp |
| Quét mã, bản đồ | quét mã vạch, ghim bản đồ, tọa độ | QA-Mobile-Native D, O | Thấp |

---

## 5. Khi gặp phần chưa có bộ: nhắc người dùng

Skill dừng sau bước nhận diện và báo:

```
Dự án có [năng lực / domain] chưa có checklist riêng: <tên>.
- Dấu hiệu thấy trong tài liệu: <3 đến 5 trích dẫn ngắn>
- Độ phủ ước tính nếu chạy tầng chung: <x>%. Nếu có bộ riêng: khoảng 95%.
- Bộ riêng dự kiến có: <8 đến 10 rủi ro chính, mỗi rủi ro một dòng>
Chọn: (1) Tạo bộ ngay rồi sinh case  (2) Chạy tạm với tầng chung, ghi khoảng trống vào note  (3) Bỏ qua
```

Người dùng chọn (1): dựng bộ theo `domain/_mau-bo-domain.md` (domain) hoặc theo cấu trúc một file `QA-*` (năng lực). Chạy review độc lập cho bộ mới (`_chung/review-doc-lap.md`), báo người dùng duyệt, rồi thêm dòng vào mục 2 hoặc mục 3 của file này. Dự án sau cùng domain dùng lại, không phải làm lại.

---

## 6. Đo độ phủ

Chấm theo 19 nhóm rủi ro chuẩn (gộp ISO/IEC 25010, ISTQB, OWASP, WCAG 2.2 và nhóm thực tế). Độ phủ là mức checklist có câu hỏi và case mẫu dẫn tới case cho nhóm đó, không phải tỷ lệ lỗi tìm ra.

| # | Nhóm rủi ro | Trọng số | Bộ chung (13/10/2026) | Phủ chính |
|:--|:---|---:|---:|:---|
| 1 | Tính đúng chức năng: field, CRUD, quy tắc, phân vùng, biên | 13 | 92% | T0 mục 2 đến 10; T1 |
| 2 | Kỹ thuật thiết kế test: bảng quyết định, chuyển trạng thái, đoán lỗi | 6 | 80% | T0 25, 27, 36.2; tư duy test |
| 3 | Kiểm soát truy cập, phân quyền, đổi ID | 7 | 90% | T0 9, 30; Adversarial |
| 4 | Xác thực, mật khẩu, OTP, phiên | 6 | 80% | T0 16.2, 29 |
| 5 | Đầu vào độc hại, lộ thông tin, tải tệp nguy hiểm | 7 | 75% | T0 30, 35 |
| 6 | Dữ liệu cá nhân và riêng tư | 4 | 75% | T1 nhóm 12; Identity |
| 7 | Độ tin cậy: lỗi, khôi phục, idempotency | 7 | 85% | T0 15, 26, 31; Advanced D, E; T1 nhóm 8, 17 |
| 8 | Đồng thời, đồng bộ, tích hợp, đối chiếu dữ liệu giữa portal | 5 | 90% | T0 12, 16, 27 (27.9); T1 nhóm 9 |
| 9 | Hiệu năng và dữ liệu lớn | 6 | 55% | T0 37; Metrics, Ranking, Crawling |
| 10 | Khả dụng: trạng thái màn, thông báo, sau thao tác | 5 | 85% | T0 6, 31; QA-States |
| 11 | Trợ năng | 5 | 75% | T0 17, 33 |
| 12 | Tương thích trình duyệt, thiết bị | 5 | 70% | T0 21, 31; Mobile |
| 13 | Định dạng số tiền, ngày giờ, múi giờ, đa ngôn ngữ | 5 | 75% | T0 32, 28.5 |
| 14 | Tải tệp, xuất, nhập | 4 | 90% | T0 19, 20, 35 |
| 15 | Email, SMS, push | 2 | 90% | T0 18, 30; QA-States |
| 16 | Tác vụ theo thời gian và lịch | 3 | 95% | T0 28; T1 nhóm 2 |
| 17 | Cấu hình, đa tổ chức, cờ tính năng | 3 | 75% | T0 14; T1 nhóm 12, 14, 17 |
| 18 | Bảo trì: dữ liệu cũ, di chuyển dữ liệu, nâng cấp | 4 | 80% | T0 11, 36; T1 nhóm 14, 17 |
| 19 | Nhật ký và giám sát | 3 | 85% | T0 8.6; T1 nhóm 13 |
| | **Tổng có trọng số** | **100** | **≈ 81%** | Trước khi bổ sung: ≈ 62% |

**Kiểm chứng 13/10/2026** trên một module 354 testcase của dự án giám sát dữ liệu mạng xã hội: bộ chung sinh ra được 343 case (96,9%), 1 case cần kiến thức domain, 10 case là khoảng trống xuyên domain (đã bổ sung: Testcase_Template 4.1, 4.8, 5.4, 7.2, 13.6, 30, 31; tầng 1 nhóm 14; QA-Metrics mục K). Con số cao vì nhiều file tầng 2 được rút ra từ chính dự án đó. Bỏ phần tầng 2 mang màu domain thì còn khoảng 86%, gần với độ phủ ban đầu ở một domain mới chưa có bộ.

Phần còn thiếu để lên 95% ở một dự án cụ thể nằm ở: checklist năng lực của dự án (mục 4, tạo khi gặp), bộ domain (mục 3, tạo khi gặp), và hiệu năng, tương thích cần công cụ ngoài kiểm thử thủ công.

Khi sinh case cho một dự án, skill ghi bảng này vào file note với cột độ phủ **của dự án đó**: nhóm nào không liên quan thì bỏ khỏi mẫu số, nhóm nào thiếu bộ thì ghi rõ.
