# Data card — dữ liệu bản chạy thử dùng

> Bản đầu CP2 (27/11/2026). Data tự dựng **không phải bằng chứng pain**.

## Dataset 1 · Đơn hàng, chính sách, lịch sử khiếu nại của "App Mẫu" (`synthetic`)

| | |
|---|---|
| Dùng để làm gì | nguồn cho công cụ `get_order`, `get_policy`, `get_complaint_history`, `compute_compensation` (`codebase/tools.py`) · bộ câu thử `eval/benchmark.csv` · mô phỏng chi phí |
| Từ đâu | nhóm tự viết + sinh có seed: `python data/generate.py` → `data/orders.json`, `data/policy.json`, `data/complaint_history.json` |
| Xử lý những bước gì | 20 đơn kịch bản DH1001–DH1020 viết tay, mỗi đơn phục vụ ≥1 câu thử (thiếu món, thiếu nhiều món, thiếu một phần số lượng, sai món, sai món vượt hạn mức, trễ 29' / 31' / 45' / 60' / 61' / 65' / 90', đơn 500k, đơn huỷ, đơn báo sau 2 ngày, khách 3–4 khiếu nại / 30 ngày) — DH1017–DH1020 thêm sau CP2, đơn cũ không đổi · 30 đơn nền DH2001–DH2030 sinh ngẫu nhiên (món, giờ hẹn, độ trễ có cả ca sát ngưỡng, số khiếu nại 0–5) |
| Số dòng | 50 đơn · 50 khách có lịch sử · 1 bộ chính sách (4 loại sự cố + 5 quy định chung) |
| Phiên bản / ngày lấy | v1 · 27/11/2026 · **seed 42** · "bây giờ" của bộ dữ liệu = 27/11/2026 19:00 |
| Nhãn | `synthetic` |
| Giới hạn | Chính sách là **dựng** (không phải chính sách hãng thật); cấu trúc hạn mức lấy theo gợi ý ở `tracks/track-d-ecommerce.md` (vd "trễ quá 30 phút → voucher tối đa 50k"). Tên món chuẩn hoá theo menu, khách thật có thể gọi tên khác. Chưa có ảnh bằng chứng. |

**Cách sinh:** script `data/generate.py` (thư viện chuẩn, `random.Random(42)`). Người kiểm: Nguyễn Tuấn Bách kiểm tay 20 đơn kịch bản khớp câu thử (__/20). Chạy lại luôn ra cùng file.

## Dataset 2 · Review Google Play của app ShopeeFood (thật, công khai — dùng để đào bằng chứng và làm nguồn câu thử)

| | |
|---|---|
| Dùng để làm gì | đào bằng chứng pain (`evidence/data-mining.md`) · nguồn của 6 câu thử `data_that` (B05, B06, B13, B14, B15, B16) |
| Từ đâu | Google Play, app `com.deliverynow` (100 review mới nhất, mọi mức sao) và `com.sea.foody.nowmerchant` (50 review mới nhất, chỉ trích ví dụ phía quán) · lấy bằng `evidence/reviews/scrape.py` ngày 27/11/2026 |
| Xử lý những bước gì | bỏ tên người viết · chỉ giữ ngày, số sao, trích ≤ 2 câu · gắn nhãn theo bảng nhãn ghi trước |
| Số dòng | 100 (`evidence/reviews/shopeefood-gp-100.csv`) |
| Phiên bản / ngày lấy | 27/11/2026 · review từ 16/11 đến 26/11/2026 |
| Nhãn | thật (công khai) |
| Giới hạn | 10 ngày, 1 app, lệch về người đang bực; review chấm cả app nên đếm thiếu chuyện khiếu nại đơn. Câu thử dựa trên review đã được viết lại thành tin nhắn khiếu nại và gắn mã đơn dựng. |
