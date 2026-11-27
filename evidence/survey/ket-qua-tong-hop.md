# Khảo sát — kết quả tổng hợp (n = 32)

> Nguồn: Google Form của nhóm, bản tóm tắt (biểu đồ) xem 27/11/2026. Số người = % trên biểu đồ × 32, làm tròn; mọi câu cộng lại đúng 32.
> **Log từng câu trả lời:** `results.csv` (bản xuất từ Google Sheets, đã xoá cột nhận ra người trả lời) — **chờ nhóm xuất và commit**. Rubric R1 yêu cầu giữ log từng câu trả lời; cho tới khi có file này, các con số dưới đây chỉ đối chiếu được với biểu đồ tóm tắt.
> Bộ câu hỏi thực tế đã gửi: `questions.md` mục "Bản thực tế đã gửi" (nhóm bỏ bớt câu 5a, 7, 10, 11, 12 so với bản soạn trước).

## Số theo từng câu

| Câu | Lựa chọn → số người / 32 |
|---|---|
| 1. Bạn hiện là | Sinh viên 14 · Vừa học vừa làm 13 · Đi làm 5 · Khác 0 |
| 2. Số đơn đặt qua app trong 1 tháng qua | 0: **3** · 1–3: 11 · 4–8: 1 · 9–15: 12 · trên 15: 5 |
| 3. App dùng nhiều nhất | BeFood 11 · Xanh SM Ngon 11 · ShopeeFood 7 · GrabFood 2 · Khác 1 |
| 4. Số đơn bị **thiếu / sai món** trong 1 tháng qua | 0: 9 · 1: 3 · 2–3: 12 · trên 3: 8 · không nhớ: 0 |
| 5. Số đơn bị **giao trễ** khá nhiều trong 1 tháng qua | 0: 7 · 1: 5 · 2–3: 6 · trên 3: 7 · không nhớ: 7 |
| 5b. Trả hàng / đòi hoàn tiền trên sàn trong 1 tháng qua | Không 21 · Có, xử lý ổn 6 · Có, mệt / chưa xong 5 |
| 6. Lần gần nhất đơn thiếu / sai món, đã làm gì *(chọn nhiều)* | Khiếu nại trong app 31 · Nhắn shipper 29 · Gọi / nhắn quán 7 · Bỏ qua 3 |
| 8. Từ lúc báo đến lúc có kết quả | dưới 5 phút 6 · 5–15 phút 8 · 15–30 phút 8 · trên 30 phút 7 · không có kết quả / bỏ dở 1 · không khiếu nại 2 |
| 9. Kết quả cuối cùng | Được hoàn đúng phần thiếu / sai 11 · **Voucher thay vì hoàn tiền 12** · Hoàn ít hơn phần thiếu 1 · **Không được gì 6** · Chưa xong 1 · Không khiếu nại 1 |

## Đếm theo cách đã ghi trước (`questions.md` mục "Cách đếm")

- **Lệch so với cách đếm ghi trước:** mẫu số dự định là người có câu 2 ≠ 0 (29 người). Chỉ có biểu đồ tóm tắt thì không lọc được từng người, nên dưới đây tính trên **cả 32**, kể cả 3 người trả lời 0 đơn. Khi có `results.csv` sẽ đếm lại đúng mẫu số 29.
- **Giả thuyết 1** (≥30% gặp thiếu / sai món trong 1 tháng qua): **23/32 (72%)** chọn 1, 2–3 hoặc trên 3 ở câu 4 → **đúng**. *(Trên mẫu số 29, tối thiểu vẫn là 23/29 = 79% nếu cả 3 người 0 đơn đều chọn 0.)*
- **Giả thuyết 2** (trong số người gặp, ≥50% mất >15 phút / không được hoàn đúng / bỏ qua): cần ghép câu 4 với câu 8, 9 theo từng người → **chờ `results.csv`**. Từ biểu đồ: 20/32 (63%) kết quả không phải "hoàn đúng phần thiếu" (voucher 12, không được gì 6, hoàn ít hơn 1, chưa xong 1); 16/32 (50%) mất trên 15 phút hoặc không có kết quả.
- Giao trễ: **18/32 (56%)** có ít nhất 1 đơn trễ khá nhiều trong tháng; 7/32 không nhớ.

## Đọc kết quả cho đúng

- Câu 6–9 hỏi về **lần gần nhất** đơn bị thiếu / sai món, có thể đã hơn 1 tháng → người chọn 0 ở câu 4 vẫn trả lời câu 6–9 được (chỉ người *chưa từng* gặp mới bỏ qua). Vì vậy câu 6–9 có 29–32 người trả lời dù câu 4 có 9 người chọn 0.
- **Mẫu lệch về người đặt nhiều:** 17/32 đặt từ 9 đơn / tháng trở lên; đa số là sinh viên / vừa học vừa làm (27/32). Tỉ lệ app dùng nhiều nhất (BeFood, Xanh SM Ngon mỗi app 11/32) cũng khác số liệu thị trường (NielsenIQ: ShopeeFood 56% số đơn, GrabFood 36%, BeFood 8% — tháng 4/2025). Vì vậy **không dùng nguyên tỉ lệ của mẫu cho cả thị trường** — xem kịch bản impact ở `spec.md` §2.
- Không có câu tự luận (câu 11 đã bỏ) → khảo sát **không có trích dẫn nguyên văn**; trích dẫn vẫn lấy từ review (`evidence/data-mining.md`).
- Người trả lời phải là người **ngoài nhóm** (rubric R1) — nhóm xác nhận ở `questions.md` (kênh gửi).
