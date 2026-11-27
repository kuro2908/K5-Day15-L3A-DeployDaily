# Đào data — cách đếm và kết quả (review công khai Google Play)

> Điền ở guide bước 1.2. Repo chỉ chứa số đã tổng hợp và trích tối đa 2 câu / review, **không chép tên người viết**, ghi link + ngày xem.
> Mục 1 viết **trước khi đọc review đầu tiên** (27/11/2026, khoảng 12:00) — không sửa cách đếm sau khi đã xem kết quả; nếu buộc phải đổi thì ghi thêm dòng "đổi gì, vì sao" ở cuối mục 1.

## 1. Cách đếm — viết TRƯỚC khi chạy

- **Data dùng:** review công khai trên **Google Play** của app **ShopeeFood** (app giao đồ ăn riêng). Nếu app không còn trang riêng trên Google Play thì ghi lại điều đó và dùng app **GrabFood / Grab** thay thế (ghi rõ đã đổi).
  - Link: https://play.google.com/store/apps/details?id=com.deliverynow&hl=vi · Ngày xem: 27/11/2026
- **Cách chọn mẫu:** sắp xếp "**Mới nhất**", lấy **100 review đầu tiên**, **mọi mức sao** (không lọc 1–3 sao), không bỏ review nào kể cả review không liên quan. Ghi ngày của review đầu và review cuối.
- **Đếm gì:** gắn **một nhãn chính** cho mỗi review theo bảng nhãn dưới.
- **Mẫu số:** N = **100** = tất cả review đã đọc, kể cả `khac` và `khen`.
- **Công cụ đếm:** mỗi review một dòng trong `evidence/reviews/shopeefood-gp-100.csv` (cột `stt, ngay, so_sao, trich (≤2 câu), nhan, co_khieu_nai_kho`) → đếm bằng `python evidence/reviews/count.py`. Người khác chạy lại phải ra cùng số. *(Thay cho Google Sheets như dự kiến ban đầu — cùng cách đếm, chỉ đổi công cụ.)*

**Bảng nhãn** (đọc thử ~30 review trước; nếu cần thêm nhãn thì thêm ở đây **trước** khi gắn nhãn cả 100):

| Nhãn | Định nghĩa (một câu) |
|---|---|
| `thieu_sai_mon` | Review kể đơn bị thiếu món, sai món, sai topping / size so với đơn đã đặt. |
| `khieu_nai_kho` | Review phàn nàn về **quá trình khiếu nại / hoàn tiền**: chờ lâu, chatbot vòng lặp, không gặp được nhân viên, chỉ được voucher, hoàn không đủ. |
| `tre` | Review phàn nàn đơn giao trễ, chờ tài xế lâu (không kèm chuyện khiếu nại). |
| `chat_luong_mon` | Đồ ăn nguội, đổ, hỏng, dị vật, không ngon. |
| `gia_phi` | Phí ship, giá, khuyến mãi, voucher không dùng được. |
| `app_loi` | Lỗi app, thanh toán, đăng nhập, không đặt được. |
| `khen` | Review khen, không có phàn nàn. |
| `khac` | Không thuộc nhãn nào ở trên. |

- Một review vừa kể thiếu món vừa kể khiếu nại khó → nhãn chính `thieu_sai_mon`, **cột phụ** `co_khieu_nai_kho = 1` để đếm thêm "trong các review thiếu / sai món, bao nhiêu kể khiếu nại khó".
- *Ghi thêm 27/11 (sau khi cào, trước khi gắn nhãn):* review chỉ có 1–2 chữ kiểu "ok", "tốt", "ngon" → `khen`; review chỉ chửi chung, không nói vấn đề gì ("app tệ", "phục vụ tệ") → `khac`; app mở chậm, lag, lỗi địa chỉ, lỗi thanh toán → `app_loi`; "lâu" / "chờ cả tiếng" / "mãi không có tài xế" → `tre`.
- **Cách lấy:** thư viện Python `google-play-scraper` (`reviews(app_id, lang="vi", country="vn", sort=Sort.NEWEST, count=100)`), chạy 27/11/2026. Không lưu tên người viết. File gốc (có toàn văn) để ngoài repo; repo chỉ có trích ≤2 câu.
- **Người gắn nhãn:** lượt đầu do trợ lý AI gắn theo bảng nhãn trên (ghi ở `docs/ai-usage.md`); **Phạm Thanh Tùng gắn lại độc lập 30 review (stt 1–30) để kiểm** — khớp __/30, ghi kết quả vào đây.

## 2. Đọc trước, đếm sau

Đã đọc cả 100 review (16/11 → 26/11/2026) trước khi gắn nhãn. Các *kiểu* phàn nàn thấy được:
- Giao lâu, đặc biệt do **ghép đơn** (một tài xế chở nhiều đơn) — đồ ăn nguội, có người chờ 1–2 tiếng.
- Lỗi app: lag, mở chậm, nhảy địa chỉ, tiền bị trừ mà đơn tự huỷ.
- Rất ít review kể chuyện **thiếu / sai món**; chỉ 1 review kể quán giao sai món và không cho huỷ đơn.
- Hoàn tiền chậm: 1 review kể đơn bị huỷ mà 2 tháng chưa được hoàn tiền.

## 3. Kết quả

| Đếm gì | x / N | % | Ghi chú |
|---|---|---|---|
| `khen` | 61/100 | 61% | không phàn nàn |
| `app_loi` | 14/100 | 14% | nhóm phàn nàn lớn nhất, nhưng không thuộc việc khiếu nại đơn |
| `tre` | **11/100** | **11%** | **10/30 review 1–2 sao là về giao trễ** |
| `khac` | 11/100 | 11% | chửi chung, không rõ vấn đề |
| `thieu_sai_mon` | 1/100 | 1% | stt 52 (cũng có `co_khieu_nai_kho = 1`) |
| `khieu_nai_kho` | 1/100 | 1% | stt 15 |
| `gia_phi` | 1/100 | 1% | |
| `thieu_sai_mon` hoặc `khieu_nai_kho` | **2/100** | **2%** | chỉ số chính D1 như đăng ký trước |

Chạy lại: `python evidence/reviews/count.py`.

## 4. ≥5 ví dụ cụ thể (trích ≤2 câu, bỏ tên, ghi ngày + số sao)

1. "đặt từ 10h37 mà 12h07 mới nhận đồ ăn. đồ nóng để trong hộp nhựa mà ngâm 1 TIẾNG RƯỠI đồng hồ…" — stt 54, 21/11/2026, 1★, `tre`
2. "ghép đơn quá nhiều dẫn đến giao lâu, đợi mòn mỏi từ mới nấu đến khi nguội chưa có ăn" — stt 70, 20/11/2026, 2★, `tre`
3. "Tệ thật sự. chờ cả tiếng đồng hồ." (kể tiếp: trả thêm tiền giao nhanh vẫn giao muộn) — stt 53, 21/11/2026, 1★, `tre`
4. "quá tệ, shop không có hàng vẫn giao loại ko đúng, ko cho hủy đơn, ép người mua nhận hàng, quá gian dối" — stt 52, 21/11/2026, 1★, `thieu_sai_mon`
5. "Đơn hàng bị hủy do ship nhưng 2 tháng trời bên shopee food ko hoàn lại tiền. Đòi t gửi sao kê giấy nhưng lại ko gửi cho t chứng từ hoàn tiền thành công." — stt 15, 24/11/2026, 1★, `khieu_nai_kho`
6. "giao không như thần gian đã dự đoán, mất cụ tiền" — stt 39, 22/11/2026, 1★, `tre`

**Ví dụ phía quán** (app *ShopeeFood – Đối Tác Nhà Hàng*, `com.sea.foody.nowmerchant`, 50 review mới nhất xem 27/11/2026 — **mẫu phụ, không đếm**, chỉ để thấy tiếng nói của bên bị khiếu nại):
- "nhân viên hỗ trợ xử lý đánh giá xấu (… khách không đưa ra được hình ảnh bằng chứng quán thiếu đồ) mà không hỗ trợ ẩn đánh giá không đúng… không công bằng giữa quán và khách hàng." — 28/07/2024, 1★
- "Tài xế không có, ép quán hủy đơn. Chính sách đền bù vô lý đến mức không thể đáp ứng." — 24/07/2025, 1★

## 5. Giới hạn của data

- Người viết review thường là người đang bực, nên % trong review **không phải** % của mọi người dùng; review không cho biết số phút mất hay số tiền mất.
- Cửa sổ chỉ 10 ngày (16–26/11/2026), một app. Review trên Google Play thường chấm **cả app** (lag, thanh toán); người gặp thiếu món có thể khiếu nại trong app chứ không viết review → review **có thể đếm thiếu** chuyện thiếu / sai món.
- **Kết luận tạm:** giả thuyết "thiếu / sai món là pain chính" **chưa được review ủng hộ** (2/100); **giao trễ** nổi bật hơn hẳn (11/100, và 10/30 review 1–2 sao). → Lát cắt mở rộng thành **khiếu nại đơn đồ ăn: thiếu / sai món hoặc giao trễ** (ghi ở `canvas.md`, dòng "Đã đổi gì so với CP1"). Khảo sát câu 4, 5 sẽ kiểm lại tỉ lệ hai loại sự cố này ở người dùng thật.
→ Kiểm lại bằng: khảo sát ≥20 người (`evidence/survey/questions.md`, câu 4, 8, 9) và phỏng vấn ≥3 người (`evidence/interviews/`).
