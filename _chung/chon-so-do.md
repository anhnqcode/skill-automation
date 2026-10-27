# Khi nào dùng sơ đồ nào

Các skill viết tài liệu đọc file này trước khi chèn sơ đồ. Mỗi sơ đồ phải trả lời một câu hỏi mà bảng hoặc câu chữ trả lời kém hơn. Không vẽ sơ đồ chỉ để tài liệu có sơ đồ. Chọn xong thì ghi một dòng lý do trong khối Phân tích.

## 1. Bảng chọn

| Sơ đồ | Trả lời câu hỏi | Dùng khi | Đặt ở | Người đọc chính |
|:---|:---|:---|:---|:---|
| **Phân rã chức năng** | Hệ thống / chức năng gồm những phần nào | Đầu dự án, module mới, chức năng mới có từ 2 chức năng con. Dùng để chốt phạm vi | BRD, đầu FSD/SRS, CR lớn | Sếp, BA, PM |
| **Use case diagram** | Ai được làm gì | Có từ 3 vai trò trở lên, quyền khác nhau | BRD hoặc phần tổng quan FSD/SRS | Sếp, BA, tester |
| **Sơ đồ làn** | Ai làm bước nào, việc chuyển giữa các vai trò ra sao | Quy trình qua nhiều vai trò, có chuyển giao, có việc ngoài hệ thống | BRD (luồng tổng thể), FSD/SRS (luồng chi tiết) | Sếp, BA, dev |
| **BPMN** | Như sơ đồ làn, kèm sự kiện và điều kiện chính xác | Quy trình có sự kiện hẹn giờ (hết hạn, nhắc lịch), nhánh chạy song song, chờ tín hiệu bên ngoài, hoặc khách hàng quen đọc BPMN | FSD/SRS, tài liệu quy trình | BA, dev, khách hàng |
| **User flow / Screen flow** | Người dùng đi qua những màn nào để làm xong một việc | Có từ 3 màn nối nhau, có rẽ nhánh theo lựa chọn của người dùng. Làm trước khi đặc tả từng màn | FSD/SRS, trước phần đặc tả màn | Designer, dev, tester |
| **Flowchart (activity)** | Hệ thống xử lý một việc theo các điều kiện nào | Logic có nhiều điều kiện lồng nhau: import, kiểm tra hợp lệ, tính toán, phân bổ | FSD/SRS, CR | Dev, tester |
| **Sequence** | Các hệ thống gọi nhau theo thứ tự nào | Có tích hợp: API ngoài, thanh toán, webhook, ký số, đăng nhập một lần, hàng đợi. Cần thứ tự gọi, hết giờ chờ, gọi lại, xử lý khi bên kia lỗi | FSD/SRS phần tích hợp | Dev |
| **State (vòng đời trạng thái)** | Đối tượng chuyển trạng thái thế nào | Đối tượng có từ 3 trạng thái, chuyển có điều kiện hoặc có chuyển ngược | FSD/SRS, CR đổi trạng thái | Dev, tester |
| **User journey map** | Khách trải qua những bước, kênh nào, khó chịu ở đâu | Giai đoạn khảo sát, cải tiến trải nghiệm, so sánh trước và sau. Không dùng làm đặc tả cho dev | BRD, tài liệu khảo sát | Sếp, designer |
| **Context diagram** | Hệ thống trao đổi dữ liệu với những ai bên ngoài | Hệ thống có từ 2 hệ thống ngoài hoặc đơn vị ngoài | BRD, phần tổng quan FSD | Sếp, dev |
| **ERD (mô hình dữ liệu)** | Các đối tượng dữ liệu liên quan nhau thế nào | Nhiều đối tượng có quan hệ một-nhiều, nhiều-nhiều, dev chưa có thiết kế dữ liệu | FSD/SRS phụ lục | Dev |

## 2. Sơ đồ nào thay được sơ đồ nào

- Quy trình ít vai trò (1 đến 2) và không có việc ngoài hệ thống: flowchart là đủ, không cần sơ đồ làn.
- Sơ đồ làn đã có sự kiện bắt đầu, kết thúc, hẹn giờ: đủ cho đa số trường hợp. Chỉ dùng BPMN đầy đủ khi khách yêu cầu hoặc có nhánh song song.
- Vòng đời có 2 trạng thái: bảng trạng thái là đủ, không cần sơ đồ state.
- Use case diagram chỉ có 1 vai trò: bỏ, danh sách chức năng là đủ.
- Đã có phân rã chức năng và user flow: use case diagram thường thừa, chỉ vẽ khi quyền giữa các vai trò phức tạp.

## 3. Bộ sơ đồ theo loại tài liệu

| Tài liệu | Bắt buộc | Thêm khi có điều kiện ở bảng 1 |
|:---|:---|:---|
| BRD | Phân rã chức năng, sơ đồ làn luồng tổng thể | Use case diagram, context diagram, user journey map |
| FSD / SRS đầy đủ (dự án mới) | Phân rã chức năng (dùng lại của BRD), user flow / screen flow | Sơ đồ làn hoặc BPMN cho luồng chi tiết, flowchart, sequence, state, ERD |
| SRS một màn (dự án đang chạy) | Không bắt buộc | Flowchart, state, sequence |
| CR | Không bắt buộc | Phân rã (chức năng mới lớn), flowchart, state, sequence |

## 4. Định dạng và công cụ

Xem khóa "Dạng sơ đồ trong tài liệu" ở cấu hình dự án.

| Sơ đồ | Dự án xuất docx (ảnh PNG) | Dự án đọc bằng Markdown |
|:---|:---|:---|
| Phân rã chức năng | `py scripts/ve_so_do_phan_ra.py` | Như cột bên |
| Sơ đồ làn, BPMN cơ bản | `py scripts/ve_so_do_lan.py` | Như cột bên |
| Flowchart, sequence, state, ERD, use case, user flow | Viết Mermaid rồi dựng ảnh: `py scripts/ve_mermaid.py <file.mmd>` | Mermaid trong khối ```` ```mermaid ```` |
| User journey map | Mermaid `journey`, hoặc bảng: Giai đoạn, Việc khách làm, Kênh, Cảm nhận, Điểm khó chịu, Cơ hội | Như cột bên |
| Context diagram | Mermaid `flowchart` với hệ thống ở giữa | Như cột bên |

Quy tắc chung cho mọi sơ đồ:

- Chữ trên sơ đồ theo `van-phong.md`: tên vai trò, màn, trạng thái đúng như tài liệu.
- Sơ đồ đi kèm bảng diễn giải khi người đọc cần làm theo từng bước (sơ đồ làn, flowchart).
- Giữ file nguồn (JSON, .mmd) trong `_src/` cạnh ảnh để sửa sau.
- Một ảnh đọc được trên khổ A4 ngang: phân rã quá 20 nút lá hoặc sơ đồ làn quá 10 cột thì tách thành nhiều ảnh.
