# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1.
> Ba nguồn ngang nhau — tối thiểu **≥1 nguồn đạt ngưỡng**. Mạnh nhất: đào data ra insight → hỏi người dùng để kiểm lại (hoặc ngược lại).

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☑ (100 review, 6 ví dụ) | `evidence/data-mining.md` · `evidence/reviews/` |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | ☐ | `evidence/interviews/P1.md`… |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | ☐ | `evidence/survey/` |

## 2. Số chính

- Đào data: 100 review Google Play ShopeeFood mới nhất (16–26/11/2026) — **giao trễ 11/100 (11%)**, 10/30 review 1–2 sao · thiếu / sai món hoặc khiếu nại khó **2/100 (2%)** · lỗi app 14/100 · khen 61/100
- Phỏng vấn: __/3 người gặp *(n nhỏ không ghi %)* · số lần / tháng: P1 __, P2 __, P3 __ · mỗi lần mất __–__ phút
- Khảo sát: n = __ · __/__ (__%) …

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

*(Phỏng vấn / khảo sát: thêm trích dẫn `P_` / phiếu __ khi có.)*

## 4. Các nguồn có khớp nhau không

**Hiện mới có một nguồn đạt ngưỡng (đào review).** Data nói: trong 100 review mới nhất, phàn nàn **giao trễ** (11/100) nhiều hơn hẳn **thiếu / sai món** (1/100) và **khiếu nại khó** (1/100); 10/30 review 1–2 sao là về giao trễ. Người dùng nói: *chờ khảo sát (câu 4 thiếu / sai món, câu 5 giao trễ) và phỏng vấn P1–P3* — đây là nguồn thứ hai để kiểm lại.
Giới hạn cần nhớ khi so: người viết review là người đang bực, và review hiếm khi kể quá trình khiếu nại, nên 2/100 có thể **đếm thiếu** ca thiếu món (khách được hoàn thì ít khi viết review). Mẫu phụ phía quán (app đối tác nhà hàng, không đếm) cho thấy chiều ngược lại: quán thấy bị xử thua khi khách không có bằng chứng.

## 5. Kết luận

Giả thuyết ở `evidence/hypothesis.md`: **phải đổi** — vì review không ủng hộ "thiếu / sai món là pain chính" (2/100), còn giao trễ xuất hiện 11/100 và chiếm 1/3 review 1–2 sao. Nhóm đã mở rộng lát cắt thêm **giao trễ** tại CP2 (canvas, `spec.md` §4). Điều vẫn chưa biết: (1) bao nhiêu % người dùng thật gặp thiếu / sai món và giao trễ mỗi tháng (khảo sát câu 4, 5); (2) mỗi lần mất bao nhiêu phút / tiền và họ có bỏ qua không (câu 6–10, phỏng vấn); (3) review có đếm thiếu ca thiếu món không.

## Lịch hẹn (dùng cho CP2 — chỉ ghi vai và giờ, không tên)

| Vai | Giờ hẹn | Đã xong? |
|---|---|---|
| | | |
