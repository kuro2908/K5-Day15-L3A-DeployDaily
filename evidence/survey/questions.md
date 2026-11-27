# Khảo sát — bộ câu hỏi (chép sang Google Form)

> Ngưỡng: **≥20 người ngoài nhóm, đúng người dùng** (đã đặt đồ ăn qua app ≥1 lần trong 1 tháng qua). Người trong nhóm **không** trả lời.
> Hỏi **hành vi đã xảy ra**, không hỏi "có thích không", không giới thiệu sản phẩm / AI.
> Không thu tên, email, số điện thoại, mã học viên (trừ câu 12 nếu người trả lời tự để lại — bản commit phải xoá cột đó).

- **Kênh gửi:** __ (vd nhóm Zalo / Discord lớp L3A, L3B, người thân) · **Giờ mở form:** __ · **Giờ chốt:** __ (trước 09:00 Thứ Bảy 28/11)
- **Kết quả:** xuất Google Sheets → `evidence/survey/results.csv` (đã xoá cột liên hệ ở câu 12 và cột dấu thời gian nếu nhận ra được người).

## Bản thực tế đã gửi (ghi sau khi chạy form)

Nhóm rút gọn form cho người trả lời đỡ mất thời gian. Câu **đã giữ**: 1, 2, 3, 4, 5, 5b, 6, 8, 9. Câu **đã bỏ**: 5a (đặt hộ nhóm, ăn chay / dị ứng), 7 (vì sao bỏ qua), 10 (trị giá phần thiếu), 11 (điều khó chịu nhất — tự luận), 12 (hẹn phỏng vấn thêm).
Hệ quả: không có số tiền mỗi lần mất (câu 10) → impact tiền ghi *(tự ước tính)*; không có trích dẫn nguyên văn từ khảo sát (câu 11); hướng D2 trong bảng impact không có số khảo sát (câu 5a).
Số người trả lời: **32**. Kết quả: `ket-qua-tong-hop.md` · log từng câu trả lời: `results.csv` *(chờ xuất)*.

## Lời mở đầu của form (dán vào phần mô tả)

> Nhóm mình đang tìm hiểu chuyện **đặt đồ ăn qua app** của mọi người trong tháng vừa rồi. Mất khoảng 2 phút, không thu tên hay số điện thoại. Không có câu trả lời đúng/sai — bạn nhớ sao ghi vậy, không nhớ thì chọn "không nhớ". Cảm ơn bạn!

## Câu hỏi

| # | Câu hỏi | Kiểu trả lời | Dùng cho |
|---|---|---|---|
| 1 | Bạn hiện là: | Chọn một: Sinh viên · Đi làm · Vừa học vừa làm · Khác | Mô tả mẫu |
| 2 | Trong **1 tháng qua**, bạn đặt đồ ăn qua app (ShopeeFood, GrabFood, BeFood, Xanh SM Ngon…) khoảng **bao nhiêu đơn**? | Chọn một: 0 · 1–3 · 4–8 · 9–15 · Trên 15 | **Lọc mẫu số** (0 đơn → loại) · persona chi phí |
| 3 | Bạn dùng app nào **nhiều nhất**? | Chọn một: ShopeeFood · GrabFood · BeFood · Xanh SM Ngon · Khác | Mô tả mẫu |
| 4 | Trong 1 tháng qua, có bao nhiêu đơn của bạn bị **thiếu món hoặc sai món**? | Chọn một: 0 · 1 · 2–3 · Trên 3 · Không nhớ | **Giả thuyết 1** · tần suất cho impact |
| 5 | Trong 1 tháng qua, có bao nhiêu đơn bị **giao trễ hơn giờ app báo khá nhiều** (bạn thấy khó chịu)? | Chọn một: 0 · 1 · 2–3 · Trên 3 · Không nhớ | Hướng so sánh D1b (giao trễ) |
| 6 | Nghĩ về **lần gần nhất** đơn bị thiếu / sai món (nếu chưa từng, bỏ qua câu 6–10): lần đó bạn đã làm gì? | Chọn **nhiều**: Khiếu nại trong app (chat / trợ lý) · Gọi hoặc nhắn quán · Nhắn shipper · Bỏ qua, không làm gì · Khác: __ | Cách đang xoay xở |
| 7 | Nếu lần đó bạn **bỏ qua**: vì sao? | Đoạn ngắn | Lý do "chưa bỏ cách cũ" · trích dẫn |
| 8 | Từ lúc bạn báo đến lúc có kết quả, mất khoảng bao lâu? | Chọn một: Dưới 5 phút · 5–15 phút · 15–30 phút · Trên 30 phút · Không có kết quả / bỏ dở · Không khiếu nại | **Giả thuyết 2** · phút cho impact |
| 9 | Kết quả cuối cùng của lần đó là gì? | Chọn một: Được hoàn đúng phần thiếu / sai · Được voucher thay vì hoàn tiền · Được hoàn ít hơn phần thiếu · Không được gì · Chưa xong · Không khiếu nại | **Giả thuyết 2** |
| 10 | Phần bị thiếu / sai lần đó trị giá khoảng **bao nhiêu nghìn đồng**? | Số (nghìn đồng), không nhớ thì để trống | Tiền mất cho impact · hạn mức trong data dựng |
| 11 | Điều gì làm bạn **khó chịu nhất** ở lần đó? Kể ngắn chuyện đã xảy ra. | Đoạn văn | **Trích dẫn nguyên văn** · nguồn câu thử `nguoi_dung` |
| 12 | *(Tuỳ chọn)* Bạn có sẵn lòng cho nhóm hỏi thêm **10 phút** qua điện thoại / chat không? | Có — để lại cách liên hệ (không bắt buộc) · Không | Tìm người phỏng vấn |

**Thêm 2 câu ngắn để có số cho bảng ≥3 hướng (spec §2), đặt sau câu 5:**

| # | Câu hỏi | Kiểu trả lời | Dùng cho |
|---|---|---|---|
| 5a | Trong 1 tháng qua, bạn có **đặt đồ ăn hộ cả nhóm** (≥3 người) không? Trong nhóm có ai ăn chay hoặc dị ứng món gì không? | Chọn một: Không đặt hộ · Có đặt hộ, không ai ăn chay / dị ứng · Có đặt hộ, có người ăn chay / dị ứng | Hướng so sánh D2 |
| 5b | Trong 1 tháng qua, bạn có phải **trả hàng / đòi hoàn tiền** một món mua trên sàn (Shopee, Lazada, TikTok Shop…) không? | Chọn một: Không · Có, xử lý xong ổn · Có, xử lý mệt / chưa xong | Hướng so sánh D3 |

## Cách đếm — ghi TRƯỚC khi xem kết quả

- **Mẫu số (N):** số người trả lời ngoài nhóm, câu 2 ≠ "0".
- **Giả thuyết 1:** x = số người câu 4 ∈ {1, 2–3, Trên 3} → báo x/N (%).
- **Giả thuyết 2:** trong x người đó, đếm y = người có **ít nhất một**: câu 8 ∈ {15–30 phút, Trên 30 phút, Không có kết quả / bỏ dở} **hoặc** câu 9 ∈ {voucher, hoàn ít hơn, không được gì, chưa xong} **hoặc** câu 6 chỉ chọn "Bỏ qua" → báo y/x (%).
- "Không nhớ" ở câu 4 **không** tính vào x, vẫn nằm trong N (ghi riêng số người "không nhớ").
- Dưới 10 người thì chỉ ghi x/n, không ghi %.
