# Đào data — cách đếm và kết quả (review công khai Google Play)

> Điền ở guide bước 1.2. Repo chỉ chứa số đã tổng hợp và trích tối đa 2 câu / review, **không chép tên người viết**, ghi link + ngày xem.
> Mục 1 viết **trước khi đọc review đầu tiên** (27/11/2026, khoảng 12:00) — không sửa cách đếm sau khi đã xem kết quả; nếu buộc phải đổi thì ghi thêm dòng "đổi gì, vì sao" ở cuối mục 1.

## 1. Cách đếm — viết TRƯỚC khi chạy

- **Data dùng:** review công khai trên **Google Play** của app **ShopeeFood** (app giao đồ ăn riêng). Nếu app không còn trang riêng trên Google Play thì ghi lại điều đó và dùng app **GrabFood / Grab** thay thế (ghi rõ đã đổi).
  - Link: __ · Ngày xem: __
- **Cách chọn mẫu:** sắp xếp "**Mới nhất**", lấy **100 review đầu tiên**, **mọi mức sao** (không lọc 1–3 sao), không bỏ review nào kể cả review không liên quan. Ghi ngày của review đầu và review cuối.
- **Đếm gì:** gắn **một nhãn chính** cho mỗi review theo bảng nhãn dưới.
- **Mẫu số:** N = **100** = tất cả review đã đọc, kể cả `khac` và `khen`.
- **Công cụ đếm:** Google Sheets, mỗi review một dòng → xuất `evidence/reviews.csv` với cột `stt, ngay, so_sao, trich (≤2 câu), nhan`. Đếm bằng `=COUNTIF(E:E, "thieu_sai_mon")` (tương tự cho từng nhãn). Người khác mở file đếm lại phải ra cùng số.

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

## 2. Đọc trước, đếm sau

Đã đọc __ review đầu. Các *kiểu* phàn nàn thấy được (trước khi chốt nhãn):
- __
- __

## 3. Kết quả

| Đếm gì | x / N | % | Ghi chú |
|---|---|---|---|
| `thieu_sai_mon` | __/100 | | |
| `khieu_nai_kho` | __/100 | | |
| `thieu_sai_mon` hoặc `khieu_nai_kho` | __/100 | | chỉ số chính cho D1 |
| `tre` | __/100 | | so sánh hướng D1b |

## 4. ≥5 ví dụ cụ thể (trích ≤2 câu, bỏ tên, ghi ngày + số sao)

1.
2.
3.
4.
5.

## 5. Giới hạn của data

Người viết review thường là người đang bực, nên % trong review **không phải** % của mọi người dùng; review không cho biết số phút mất hay số tiền mất.
→ Kiểm lại bằng: khảo sát ≥20 người (`evidence/survey/questions.md`, câu 4, 8, 9) và phỏng vấn ≥3 người (`evidence/interviews/`).
