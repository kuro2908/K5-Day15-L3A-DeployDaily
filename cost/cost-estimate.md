# Chi phí khi dùng thật

> Guide bước 4.2, nộp CP4 14:30 Thứ Bảy 28/11. Chấm ở rubric R6. Số lấy từ `cost/simulate-1-summary.md` (không điền tay).
> Lúc build dùng tài khoản của nhóm, vẫn tính theo **giá gói trả phí Standard** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): 3 kiểu theo khảo sát câu 2 (29 người có đặt đơn) — **đặt ít** 1–8 đơn / tháng (42%) · **đặt vừa** 9–15 đơn (41%) · **đặt nhiều** trên 15 đơn (17%). Số phiên khiếu nại / người / tháng: 1 · 3 · 5; lượt hỏi / phiên: 1 · 2 · 2 *(tự ước tính từ khảo sát câu 4–5)*. Nhóm đặt nhiều có cả câu `tu_choi` (doạ, đòi vượt chính sách).
- **Số người dùng thật** (người dùng app giao đồ ăn ở Việt Nam): thấp **16,1 triệu** (Statista 2023 — chưa mở được trang gốc) · cơ sở **17,8 triệu** (dự báo 2025, [Vietnam News 31/05/2025](https://vietnamnews.vn/economy/1718645/food-apps-invest-strategically-or-be-swept-away-by-price-wars.html)) · cao **21,2 triệu** *(tự ước tính: 17,8 triệu × 1,19 theo mức tăng 19% của thị trường 2025, [VnExpress](https://e.vnexpress.net/news/business/data-speaks/vietnamese-spend-2-1b-on-food-delivery-in-2025-5011109.html))*.
- **Giá** (USD / 1 triệu token, Standard):
  - `gpt-5.4-nano` 0,20 / 1,25 — model đang dùng, [trang model OpenAI](https://developers.openai.com/api/docs/models/gpt-5.4-nano), xem 27/11/2026 *(không có trong bảng giá BTC; trang ghi model "Deprecated")*
  - `gpt-5-nano` 0,05 / 0,40 — mức rẻ hơn, bảng giá BTC (`further-reading/model-prices.md`, [OpenAI pricing](https://developers.openai.com/api/docs/pricing)), xem 25/11/2026
  - `gpt-5.4-mini` 0,75 / 4,50 — mức mạnh hơn, bảng giá BTC, xem 25/11/2026
- **Tỉ lệ đạt dùng để tính:** 30/30 (100%) — lượt `run-3@20261127-233759`, **cùng code và cùng model** với lượt mô phỏng (bản AI gọi 2 lần). Lượt 2 (30/30) chạy bản AI gọi 1 lần nên không dùng cho chi phí của bản hiện tại.
- **Đo token trên model `gpt-5.4-nano`, tính giá cả 3 model** — model khác bộ tách token thì số token thật có thể lệch.
- **Tỷ giá:** 1 USD = 26.000 ₫ *(tự ước tính, chưa kiểm với ngân hàng)*.

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-1.csv` · run ID `simulate-1@20261127-233949` · **60 phiên** · seed 42 · phiên lỗi 0/60 · trace `traces/simulate-1.jsonl`

| Persona | Số phiên | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dat_it | 29 | 1 | 2259 | 208 | 2.0 | 8.4 |
| dat_vua | 25 | 2 | 4502 | 421 | 4.0 | 16.7 |
| dat_nhieu | 6 | 2 | 4644 | 442 | 4.0 | 17.7 |

| Model | Chi phí / phiên | Chi phí / task thành công | / tháng — thấp | / tháng — cơ sở | / tháng — cao | / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|
| **gpt-5.4-nano** (đang dùng) | $0.0011 (≈ 28 ₫) | $0.0011 (≈ 28 ₫) | $53.336 (≈ 1,39 tỷ ₫) | **$58.967 (≈ 1,53 tỷ ₫)** | $70.231 (≈ 1,83 tỷ ₫) | **$0.0033 (≈ 86 ₫)** |
| gpt-5-nano (rẻ hơn) | $0.00030 (≈ 8 ₫) | $0.00030 (≈ 8 ₫) | $14.716 (≈ 0,38 tỷ ₫) | $16.270 (≈ 0,42 tỷ ₫) | $19.377 (≈ 0,50 tỷ ₫) | $0.00091 (≈ 24 ₫) |
| gpt-5.4-mini (mạnh hơn) | $0.0040 (≈ 104 ₫) | $0.0040 (≈ 104 ₫) | $197.048 (≈ 5,12 tỷ ₫) | $217.854 (≈ 5,66 tỷ ₫) | $259.467 (≈ 6,75 tỷ ₫) | $0.0122 (≈ 318 ₫) |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt.

**Lưu ý về tỉ lệ đạt 100%:** bộ câu thử do nhóm tự viết và nhóm đã nhìn khi sửa (chưa có phần giữ riêng), nên tỉ lệ đạt khi dùng thật sẽ thấp hơn. Nếu tỉ lệ thật chỉ bằng ngưỡng chuẩn "đạt" **75%**, chi phí / task thành công với `gpt-5.4-nano` là $0.0011 ÷ 0,75 ≈ **$0.0015 (≈ 38 ₫)** và / người / tháng ≈ **115 ₫** — vẫn cùng kết luận ở mục 3.

## 3. So với impact

- **Impact / người / tháng** (`spec.md` §2, cơ sở): ≈ **19 phút** chờ xử lý khiếu nại + ≈ **8.750 ₫** tiền không được bồi thường đủ *(tiền: tự ước tính)*.
- **Chi phí / người / tháng** (cơ sở, `gpt-5.4-nano`): ≈ **86 ₫** — khoảng **1%** riêng phần tiền của impact, chưa tính 19 phút.
- **So với nhân viên** *(tự ước tính)*: lương CSKH ≈ 8 triệu ₫ / tháng ÷ (26 ngày × 8 giờ × 60 phút) ≈ 640 ₫ / phút; ≈ 5 phút / ca → ≈ **3.200 ₫ / ca**, so với ≈ **28 ₫ / phiên** của AI. Các ca nhạy cảm (an toàn thực phẩm, vượt hạn mức, khách khiếu nại nhiều) vẫn chuyển nhân viên — chi phí đó không mất đi.
- **Kết luận một dòng — đáng làm không:** **Đáng làm (go)** — kể cả khi tỉ lệ đạt thật chỉ 75% và dùng model mạnh hơn (`gpt-5.4-mini`, ≈ 318 ₫ / người / tháng), chi phí vẫn nhỏ hơn nhiều so với ≈ 8.750 ₫ + 19 phút mỗi người mất mỗi tháng; điều cần làm trước khi dùng thật là đo lại tỉ lệ đạt trên bộ câu thử giữ riêng.

## 4. *(Muốn sâu hơn, không bắt buộc)*

- **Model:** chuyển `gpt-5-nano` giảm chi phí ≈ 3,6 lần (86 → 24 ₫ / người / tháng) — phải chạy lại bộ câu thử trên model đó trước khi đổi.
- **Ngữ cảnh:** mỗi lượt gửi ≈ 2.250 token vào, phần lớn là dữ liệu đơn + chính sách lặp lại → cache phần chính sách (giá cache `gpt-5.4-nano` $0.02 / 1M) có thể giảm đáng kể token vào.
- **Chưa tính:** hosting, lưu trữ, giờ công nhân viên ở các ca chuyển người.
