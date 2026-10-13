# Review độc lập bằng agent riêng

Người viết tự review thường bỏ sót lỗi của chính mình vì đã quen giả định lúc viết. Sau bước tự review, giao tài liệu cho **một agent mới** (công cụ Agent, loại `general-purpose`) chỉ đọc tài liệu và nguồn, không biết quá trình viết, để soi lại.

## Khi nào chạy

| Tài liệu | Chạy |
|:---|:---|
| BRD, FSD, SRS mới, CR | Luôn chạy, sau bước tự review, trước khi báo người dùng |
| Cập nhật SRS theo CR | Chạy khi sửa từ 2 SRS trở lên |
| Testcase | Chạy khi bộ case có từ 30 case trở lên |
| `/review-tai-lieu` | Đây là việc chính của skill đó |

Tài liệu dài (FSD nhiều màn, SRS lớn) thì chạy song song 2 agent, mỗi agent một góc nhìn: (A) Dev và Tester, (B) Nghiệp vụ, văn phong và đối chiếu nguồn.

## Lời giao việc cho agent

Điền phần trong ngoặc vuông rồi gửi nguyên văn. Không kể cho agent quá trình viết, không kể các điểm đã tự chốt, để agent đọc như người mới.

```
Bạn là senior BA kiêm senior tester, review độc lập một tài liệu [loại tài liệu] bằng tiếng Việt.
Bạn chưa từng thấy tài liệu này. Chỉ đọc, không sửa file nào.

Tài liệu cần review: [đường dẫn]
Nguồn để đối chiếu: [đường dẫn SRS cũ, CR liên quan, BRD, cây phân rã, thiết kế... hoặc "không có"]
Đọc trước để biết chuẩn:
- Template: [đường dẫn template]
- Quy tắc văn phong: [<SKILL_BA>/_chung/van-phong.md]
- Checklist review: [đường dẫn tu-review.md của skill, nếu có]
- Checklist phi chức năng: [<SKILL_BA>/_chung/nfr-checklist.md] (chỉ với SRS, FSD)
- Thuật ngữ dự án: [đường dẫn file thuật ngữ, nếu có]

Góc nhìn: [A: Dev có code được không, Tester có viết case được không / B: nghiệp vụ có hở không, văn phong, khớp nguồn / cả hai]

Tìm:
1. Chỗ Dev phải đoán: quy tắc thiếu điều kiện, thiếu giá trị, thiếu chữ thông báo, hai cách hiểu.
2. Chỗ Tester không viết được case: AC mơ hồ, quy tắc không có AC, AC không đo được.
3. Lỗ hổng nghiệp vụ: trường hợp biên, thao tác sai thứ tự, dữ liệu cũ, đồng thời, phân quyền, ảnh hưởng sang màn hoặc module khác.
4. Mâu thuẫn: giữa các mục trong tài liệu, giữa tài liệu và nguồn.
5. Sai template, sai văn phong (câu phủ định, từ hoa mỹ, cú pháp code, dòng "Không đổi"...).

Trả về bảng markdown, xếp theo mức độ từ cao xuống thấp:
| # | Mức độ (Cao / Trung bình / Thấp) | Vị trí (mục, dòng trích ngắn) | Vấn đề | Đề xuất sửa cụ thể | Loại (Lỗi rõ ràng / Cần BA quyết) |
Chỉ ghi vấn đề có thật, kèm trích dẫn chỗ sai. Không khen, không tóm tắt tài liệu. Không có vấn đề ở nhóm nào thì bỏ qua nhóm đó.
```

## Xử lý kết quả

1. Đọc từng dòng, tự kiểm tra lại với tài liệu. Dòng agent hiểu sai thì bỏ, ghi lý do ngắn trong note.
2. **Lỗi rõ ràng** (sai văn phong, sai template, quy tắc thiếu AC, hai mục mâu thuẫn, thiếu chữ thông báo đã có trong nguồn): sửa luôn.
3. **Cần BA quyết** (thêm logic nghiệp vụ mới, đổi phạm vi, chọn giữa hai hướng): không tự sửa. Đưa vào danh sách đề xuất khi báo người dùng, kèm hướng đề xuất.
4. Ghi vào note mục "Review độc lập": số vấn đề theo mức độ, số đã sửa, số chờ BA quyết.
