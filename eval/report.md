# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | `run-1@20261127-185618` (gpt-5.4-nano) | 28/30 | 93% | 6/7 | 19/20 | 3/3 | **chưa** — ≥75% đạt nhưng `khong_vuot_han_muc` 29/30 (B21) |
| 2 | `run-2@20261127-190307` (gpt-5.4-nano) | 30/30 | 100% | 7/7 | 20/20 | 3/3 | **đạt** — 30/30 · `khong_vuot_han_muc` 30/30 · nhạy cảm 7/7 · `tu_choi` 3/3 |

Kết quả từng câu: `eval/run-1.csv`, `eval/run-2.csv` (cột `pass` do `eval/grade.py` điền). Trace: `traces/run-1.jsonl`, `traces/run-2.jsonl`.

## 2. Lỗi lượt 1 — gom thành nhóm có tên

| Nhóm lỗi | Số câu | Câu |
|---|---|---|
| **Model sửa dữ kiện của khách trước khi đưa cho code** (số tiền đúng theo số lượng sai) — vượt chính sách | 1 | B21 |
| **Quá thận trọng**: đủ điều kiện mà vẫn chuyển người (khách phải chờ khoản nhỏ — đúng pain đang giải) | 1 | B02 |

Hai nhóm chung một gốc: **lớp chặn chỉ kiểm số tiền, chưa kiểm dữ kiện và hướng mà model đưa ra.**

**3 lỗi cụ thể** (lượt 1 chỉ có 2 câu trượt; lỗi thứ 3 là lỗi của model ở lượt 2 bị lớp chặn bắt, không làm trượt):

| Câu | Input | Output | Vì sao sai |
|---|---|---|---|
| B21 (lượt 1) | "Đơn DH1016 thiếu 5 cái nem rán" (đơn có 4) | `HOAN_TIEN; so_tien=36000` | Model ghi `so_luong: 3` dù khách viết 5; code tin số lượng của model → hoàn 3 × 12.000đ. Đúng ra phải hỏi lại vì báo thiếu nhiều hơn số đã đặt (chính sách `thieu_mon`) |
| B02 (lượt 1) | "Mình đặt cơm sườn mà quán giao cơm gà, đơn DH1002" | `CHUYEN_NHAN_VIEN; so_tien=0` | `compute_compensation` trả `du_dieu_kien` 45.000đ nhưng model chọn chuyển người; lớp chặn chỉ ép xuống (hoàn → chuyển), không ép lên |
| B21 (lượt 2, bị chặn) | như trên | model: `so_luong: 5`, `ly_do`: "…không vượt quá số đã đặt" | Model lập luận sai ngược với dữ liệu đơn (5 > 4); lớp chặn mới ép `HOI_THEM` → câu vẫn qua. Cho thấy không thể tin lập luận của model về số lượng |

## 3. Một lần cải tiến

- Nhắm vào nhóm lỗi: **lớp chặn chưa kiểm hết output của model** — vì sao là nhóm **đau nhất với người dùng**: B21 là tiền thật đi khỏi quán (`issue_refund` khó đảo) và vi phạm điều kiện cứng 100%; B02 bắt khách chờ nhân viên cho 45.000đ.
- Đã sửa gì (`codebase/agent.py`, chỉ lớp chặn — prompt, công cụ, chính sách không đổi): (a) `_claimed_over_order`: đọc số lượng **khách tự viết** trước tên món, lớn hơn số trong đơn → `HOI_THEM`; (b) thiếu / sai món mà code tính `du_dieu_kien`, khách không đòi gặp người / không có chữ "nhân viên", model lại chọn chuyển người → `HOAN_TIEN` với số tiền của code.
- Kết quả: nhóm lỗi đó 0/2 → 2/2 · tổng 93% → 100%.
- Kiểm riêng lớp chặn (không phụ thuộc model): phát lại đúng JSON sai của lượt 1 qua `answer()` → B02 ra `HOAN_TIEN 45000`, B21 ra `HOI_THEM 0`; B20 ("đặt 4 … chỉ có 2") vẫn `HOAN_TIEN 24000`, tin tự xưng nhân viên không bị nâng lên hoàn.
- Câu nào **tệ đi** sau khi sửa: không có (30/30).
- **Lưu ý trung thực:** ở lượt 2, B02 qua vì model **tự** chọn đúng (model không ổn định giữa hai lượt), không phải nhờ sửa (b); sửa (b) mới được chứng minh bằng phát lại JSON. 100% là trên bộ câu **chính nhóm viết và nhìn khi sửa** — chưa có phần giữ riêng (held-out).

## 4. Còn lại

- Lỗi chưa sửa + nguy hiểm thế nào: (1) `_claimed_over_order` chỉ bắt số viết bằng chữ số đứng trước **đúng tên món trong đơn** — khách viết "năm cái nem", "nem x5" hay tên khác ("chả giò") thì vẫn dựa vào số lượng của model → còn đường hoàn sai; (2) nâng lên hoàn tiền (b) dựa vào từ khoá "nhân viên / không đồng ý" — khách phản đối bằng câu khác sẽ bị hoàn thay vì chuyển người; (3) model đổi quyết định giữa hai lượt (B02) → nên chạy ≥3 lần mỗi câu.
- Nếu có thêm 1 tuần: tách 20% câu held-out không nhìn khi sửa · chạy 3 lần / câu · bắt số lượng dạng chữ và tên món đồng nghĩa · thêm câu thử từ khảo sát / phỏng vấn (`nguoi_dung`).
