# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1.
> Ba nguồn ngang nhau — tối thiểu **≥1 nguồn đạt ngưỡng**. Mạnh nhất: đào data ra insight → hỏi người dùng để kiểm lại (hoặc ngược lại).

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☑ (100 review, 6 ví dụ) | `evidence/data-mining.md` · `evidence/reviews/` |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | ☐ | `evidence/interviews/P1.md`… |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | ☑ n = 32 *(log từng câu trả lời `results.csv`: chờ xuất)* | `evidence/survey/ket-qua-tong-hop.md` · `questions.md` |

## 2. Số chính

- Đào data: 100 review Google Play ShopeeFood mới nhất (16–26/11/2026) — **giao trễ 11/100 (11%)**, 10/30 review 1–2 sao · thiếu / sai món hoặc khiếu nại khó **2/100 (2%)** · lỗi app 14/100 · khen 61/100
- Phỏng vấn: **chưa làm** (không có file `evidence/interviews/P*.md`) — nguồn thứ hai đang dùng là khảo sát.
- Khảo sát: n = 32 (27/11/2026) · **23/32 (72%) có ≥1 đơn thiếu / sai món** trong tháng qua · **18/32 (56%) có đơn giao trễ** khá nhiều (7/32 không nhớ) · lần gần nhất: 31/32 khiếu nại trong app, 15/32 mất trên 15 phút hoặc không có kết quả, chỉ 11/32 được hoàn đúng phần thiếu (12/32 nhận voucher thay vì tiền, 6/32 không được gì) · chi tiết `evidence/survey/ket-qua-tong-hop.md`

Phỏng vấn nhiều vai thì đếm theo từng vai, không cộng chung.

| | Vai | Gặp pain? | Số lần / 1 tháng qua | Lần gần nhất mất | Đang xoay xở bằng |
|---|---|---|---|---|---|
| P1 | | | | | |
| P2 | | | | | |
| P3 | | | | | |

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

Nguồn: 100 review Google Play ShopeeFood mới nhất (`evidence/reviews/shopeefood-gp-100.csv`, cột `stt`), xem 27/11/2026. Trích ≤2 câu, không ghi tên người viết.

1. "đặt từ 10h37 mà 12h07 mới nhận đồ ăn. đồ nóng để trong hộp nhựa mà ngâm 1 TIẾNG RƯỠI đồng hồ…" — review stt 54, 21/11/2026, 1★, nhãn `tre`
2. "ghép đơn quá nhiều dẫn đến giao lâu, đợi mòn mỏi từ mới nấu đến khi nguội chưa có ăn" — review stt 70, 20/11/2026, 2★, `tre`
3. "Tệ thật sự. chờ cả tiếng đồng hồ." — review stt 53, 21/11/2026, 1★, `tre`
4. "quá tệ, shop không có hàng vẫn giao loại ko đúng, ko cho hủy đơn, ép người mua nhận hàng, quá gian dối" — review stt 52, 21/11/2026, 1★, `thieu_sai_mon`
5. "Đơn hàng bị hủy do ship nhưng 2 tháng trời bên shopee food ko hoàn lại tiền. Đòi t gửi sao kê giấy nhưng lại ko gửi cho t chứng từ hoàn tiền thành công." — review stt 15, 24/11/2026, 1★, `khieu_nai_kho`
6. "giao không như thần gian đã dự đoán, mất cụ tiền" — review stt 39, 22/11/2026, 1★, `tre`

*(Khảo sát đã bỏ câu tự luận nên không có trích dẫn; phỏng vấn chưa làm.)*

## 4. Các nguồn có khớp nhau không

**Hai nguồn đạt ngưỡng: đào review (N = 100) và khảo sát (n = 32).**
- **Giao trễ — khớp:** review 11/100, 10/30 review 1–2 sao; khảo sát 18/32 (56%) gặp trong tháng qua. Cả hai nguồn đều cho thấy giao trễ là chuyện thường gặp.
- **Thiếu / sai món — lệch, giải thích được:** review chỉ 2/100, nhưng khảo sát 23/32 (72%) gặp trong tháng qua. Lý do: khi đơn thiếu món, khách **khiếu nại ngay trong app** (31/32) và nhắn shipper (29/32), ít người viết review lên Google Play; review chủ yếu chấm cả app (lỗi app 14/100). Đây là đúng giới hạn đã ghi trước ở `evidence/data-mining.md` mục 5 ("review có thể đếm thiếu chuyện thiếu / sai món").
- **Quá trình khiếu nại — khớp với review "khiếu nại khó":** khảo sát cho thấy chỉ 11/32 được hoàn đúng phần thiếu, 15/32 mất trên 15 phút hoặc không có kết quả — cùng hướng với review stt 15 ("2 tháng trời … ko hoàn lại tiền").
- **Giới hạn khảo sát:** mẫu lệch về sinh viên và người đặt nhiều (17/32 đặt từ 9 đơn / tháng), app dùng nhiều nhất khác số liệu thị trường; chỉ có biểu đồ tóm tắt nên chưa lọc đúng mẫu số 29 như đã ghi trước (3 người trả lời 0 đơn vẫn nằm trong 32); không có câu tự luận nên không có trích dẫn từ khảo sát.

## 5. Kết luận

Giả thuyết ở `evidence/hypothesis.md`:
- **Phần 1 — đúng:** "≥30% gặp thiếu / sai món trong tháng" → 23/32 (72%). Review đã làm nhóm nghi ngờ phần này ở CP2, nhưng khảo sát cho thấy review đếm thiếu.
- **Phần 2 — nhiều khả năng đúng, chưa đếm chính xác:** "≥50% người gặp mất >15 phút / không được hoàn đúng / bỏ qua" → từ biểu đồ: 20/32 kết quả không phải hoàn đúng phần thiếu, 16/32 mất trên 15 phút hoặc không có kết quả; cần `results.csv` để ghép câu 4 với câu 8, 9 theo từng người.
- **Điều đã đổi so với ban đầu:** pain không chỉ là thiếu / sai món mà cả **giao trễ** (56% gặp, và nổi bật nhất trong review) → lát cắt gồm cả hai (đã chốt CP2).
- **Điều vẫn chưa biết:** mỗi lần mất bao nhiêu tiền (câu 10 đã bỏ — impact tiền đang *(tự ước tính)*); vì sao người dùng chưa bỏ kênh hiện tại (câu 7 đã bỏ); tiếng nói phía quán ngoài 2 review (chưa phỏng vấn chủ quán).

## Lịch hẹn (dùng cho CP2 — chỉ ghi vai và giờ, không tên)

| Vai | Giờ hẹn | Đã xong? |
|---|---|---|
| | | |
