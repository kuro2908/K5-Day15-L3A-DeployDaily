# Tóm tắt mô phỏng simulate-1@20261127-233949

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dat_it | 29 | 1 | 2259 | 208 | 2.0 | 8.4 |
| dat_vua | 25 | 2 | 4502 | 421 | 4.0 | 16.7 |
| dat_nhieu | 6 | 2 | 4644 | 442 | 4.0 | 17.7 |

Tỉ lệ đạt dùng để tính: 30/30 (100%) — lượt run-3@20261127-233759

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-3.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (16.100.000 người) | Chi phí / tháng — cơ sở (17.800.000 người) | Chi phí / tháng — cao (21.200.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-5.4-nano (vào 0.2 · ra 1.25 $/1M) | $0.0011 (≈ 28 ₫) | $0.0011 (≈ 28 ₫) | $0.00072 (≈ 19 ₫) | $53,335.67 (≈ 1.386.727.414 ₫) | $58,967.39 (≈ 1.533.152.048 ₫) | $70,230.82 (≈ 1.826.001.316 ₫) | $0.0033 (≈ 86 ₫) |
| gpt-5-nano (vào 0.05 · ra 0.4 $/1M) | $0.00030 (≈ 8 ₫) | $0.00030 (≈ 8 ₫) | $0.00020 (≈ 5 ₫) | $14,715.73 (≈ 382.608.859 ₫) | $16,269.56 (≈ 423.008.552 ₫) | $19,377.23 (≈ 503.807.939 ₫) | $0.00091 (≈ 24 ₫) |
| gpt-5.4-mini (vào 0.75 · ra 4.5 $/1M) | $0.0040 (≈ 104 ₫) | $0.0040 (≈ 104 ₫) | $0.0026 (≈ 69 ₫) | $197,047.74 (≈ 5.123.241.363 ₫) | $217,854.03 (≈ 5.664.204.736 ₫) | $259,466.60 (≈ 6.746.131.484 ₫) | $0.0122 (≈ 318 ₫) |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.5) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gpt-5.4-nano. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/60.
- Tỷ giá: 1 USD = 26.000 ₫ ((tự ước tính) xấp xỉ tỉ giá USD/VND cuối 11/2026 — chưa kiểm với ngân hàng).
