# AI SPEC — Khiếu nại đơn đồ ăn thiếu / sai món trong hạn mức · Nhóm DeployDaily · Phòng [XXX] · Zone [X]

> Mốc nộp: §7 chốt chuẩn "đạt" tại **CP2 19:30 Thứ Sáu 27/11** · §0–§7 nộp **CP3 10:00 Thứ Bảy 28/11** · đủ §0–§10 **CP4 14:30 Thứ Bảy 28/11** · §10 changelog ghi tiếp đến **23:59 Thứ Bảy 28/11**.
> Đầu mỗi mục ghi bước guide (`02-guide.md` trong repo đề) chỉ cách điền. Mỗi mục ngắn, có số và nguồn; chi tiết để ở file được trỏ tới. Xoá dòng hướng dẫn trong ngoặc vuông khi điền xong.

Track: [ ] A · [ ] B · [ ] C · [x] D · [ ] E — bài toán: D1 · Xử lý khiếu nại đơn giao đồ ăn (hướng gợi ý trong `tracks/track-d-ecommerce.md`), thu hẹp vào đơn **thiếu / sai món**
Data BTC cấp đã dùng (nếu có — không commit nguyên file): không (track D không có data BTC cấp)

## §0. Hiện tại việc này diễn ra thế nào *(guide 1.1)*
- Luồng hiện tại của việc này, trong khoá hoặc trên app thật (3–5 bước; ảnh chụp từ tài khoản của mình, đã che thông tin): *(chưa kiểm — cần chụp màn hình luồng khiếu nại trên app của thành viên, che mã đơn / địa chỉ / SĐT, lưu `evidence/screenshots/`)*. Luồng dự kiến, theo trải nghiệm của nhóm, **chưa kiểm**:
  1. Nhận đơn, phát hiện thiếu / sai món.
  2. Vào đơn trong app → mục trợ giúp / "Trò chuyện" → chọn sự cố theo menu có sẵn.
  3. Chọn món bị thiếu, có khi phải gửi ảnh.
  4. Chờ hệ thống / nhân viên trả lời; nhận hoàn tiền, voucher, hoặc bị từ chối.
  5. Không thoả đáng → nhắn tiếp, gọi quán / shipper, đánh giá 1 sao, hoặc bỏ qua.
- Công cụ / AI đang được dùng cho việc này (nếu có) + nguồn. Không kiểm được thì ghi "chưa kiểm": theo `tracks/track-d-ecommerce.md` (BTC kiểm 11/11/2026), trợ lý "Trò chuyện với Shopee" chủ yếu chạy theo menu có sẵn. Trợ lý trong app giao đồ ăn: **chưa kiểm**.

## §1. Người dùng & bằng chứng *(guide 1.1, 1.2)*
- Người dùng chính (một vai cụ thể): sinh viên / người đi làm đặt đồ ăn qua app (ShopeeFood, GrabFood, BeFood…) vài lần mỗi tuần, vừa nhận một đơn bị thiếu hoặc sai món. *(Vai phụ để kiểm lại: chủ quán / người bán — bên bị khiếu nại.)*
- Việc họ cố làm xong (`động từ + đối tượng + bối cảnh`, không có chữ AI): **đòi lại đúng phần tiền của món bị thiếu / sai, ngay sau khi nhận đơn, mà không mất nhiều thời gian.**
- Hôm nay họ giải bằng gì, hỏng ở đâu, vì sao chưa bỏ: *(giả thuyết, chờ khảo sát + phỏng vấn kiểm)* khiếu nại qua menu trong app, gọi / nhắn quán hoặc shipper, hoặc bỏ qua. Hỏng ở chỗ: nhiều bước, chờ nhân viên, kết quả hay là voucher thay vì hoàn đúng phần thiếu. Chưa bỏ vì đó là kênh duy nhất để được hoàn tiền, và số tiền mỗi lần nhỏ nên không đáng làm to.
- Pain (KHÔNG chữ AI): người đặt đồ ăn vừa nhận đơn thiếu / sai món → phải khiếu nại qua nhiều bước, chờ trả lời → mất thời gian giữa bữa ăn, thường không được hoàn đúng phần thiếu, nhiều người bỏ qua và chịu mất tiền; phía quán có lúc bị trừ tiền dù giao đúng.
- Bằng chứng — số chính + kết luận (chi tiết: `evidence/summary.md`): *chưa có — giả thuyết ở `evidence/hypothesis.md`; đang làm khảo sát ≥20 (nguồn chính), phỏng vấn ≥3 + 1 chủ quán, đếm 100 review Google Play (kiểm lại).*

## §2. Impact & quyết định chọn *(guide 1.3)*

| Hướng | Bao nhiêu người gặp | Bao nhiêu lần / tháng | Mỗi lần tốn gì | Impact / tháng | Làm kịp không | Chọn? |
|---|---|---|---|---|---|---|
| **D1a · Đơn thiếu / sai món** | chờ khảo sát câu 2, 4 | chờ khảo sát câu 4 | phút (câu 8) + tiền không được hoàn (câu 9, 10) | __ | Kịp: tra đơn + chính sách + kiểm hạn mức bằng code | **Dự kiến chọn** |
| D1b · Giao trễ, đền voucher | chờ khảo sát câu 5 | chờ khảo sát câu 5 | phút chờ, bữa ăn nguội | __ | Kịp, nhưng thiệt hại khó tính ra tiền | |
| D2 · Đặt đơn nhóm có người ăn chay / dị ứng | chờ khảo sát câu 5a | chờ khảo sát câu 5a | phút chọn món, rủi ro dị ứng | __ | Kịp | |
| D3 · Trả hàng / hoàn tiền trên sàn | chờ khảo sát câu 5b | chờ khảo sát câu 5b | tiền hàng, thời gian trả hàng | __ | Khó: phải dựng mô tả lúc đặt và hiện tại, bằng chứng hai bên | |

- **Impact / tháng** của hướng chọn = __ người × __ lần × __ phút = __ — nguồn từng thừa số: __ (không có nguồn thì ghi rõ *(tự ước tính)*)
- **Công thức dự kiến (D1a):** impact / tháng = số người dùng app × % gặp thiếu / sai món mỗi tháng (khảo sát câu 4) × số lần / tháng (câu 4) × [phút mất (câu 8) + tiền không được hoàn (câu 9, 10)]. Phía nền tảng: số khiếu nại / tháng × phút nhân viên xử lý một ca × chi phí nhân viên / phút *(tự ước tính, hoặc hỏi người làm CSKH)*. Số người dùng app: nguồn công khai có link, không có thì *(tự ước tính)*.
- Hướng ĐÃ LOẠI + vì sao (giữ lại, đừng xoá):
- Số lần / tháng của từng kiểu người dùng (dùng cho persona ở §8):

## §3. Giải pháp tương tự *(guide 2.1)*
- [sản phẩm / tính năng gần giống]: một điều đáng học · một điều đáng né · mình khác gì

## §4. Thiết kế *(guide 2.2, 3.2)*
- **Lát cắt MỘT CÂU** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả): *(dự kiến ở CP1, chốt ở CP2)* Một người đặt đồ ăn · nhắn khiếu nại đơn vừa nhận bị thiếu một món · AI quyết định hoàn đúng phần thiếu trong hạn mức, hỏi thêm thông tin, hay chuyển nhân viên · khách nhận lời xin lỗi kèm số tiền hoàn đúng theo chính sách, hoặc biết rõ đã được chuyển người.
- Không làm (≥3 điều): *(dự kiến)* không xử lý trả hàng trên sàn TMĐT · không thực hiện hoàn tiền thật (chỉ ra lệnh hoàn nháp trên dữ liệu giả) · không phân xử tranh chấp với shipper · không tự xử lý ca dị vật / nghi ngộ độc / phản ứng dị ứng (chuyển người ngay) · không phạt hay khoá quán.
- **Sơ đồ** (ảnh / Mermaid / draw.io): [chèn ở đây]
- **Hình dạng:** [ ] workflow cố định · [ ] một agent · [ ] nhiều agent — 2 dòng lý do, và vì sao **không** chọn hình dạng phức tạp hơn:
- **AI dựa vào đâu** — mỗi công cụ (khớp `codebase/tools.py`):

  | Công cụ | Input | Output | Tác động ra ngoài? |
  |---|---|---|---|
  |  |  |  |  |

- **Mức tự động:** [ ] AI gợi ý, người quyết · [ ] AI tự làm khi chắc, chuyển người khi không · [ ] AI tự làm — lý do (sai thì ai chịu gì, sửa đắt hay rẻ):
- **Chỗ chặn rủi ro** (rủi ro lớn nhất của lát cắt bị chặn ở đâu, bằng gì):
- **Chỗ người duyệt** (việc AI không được tự làm):
- **Nguyên tắc thiết kế** (≥3, bắt buộc G10):

  | Nguyên tắc | Chỗ cụ thể trên sơ đồ / trong bản chạy thử |
  |---|---|
  | G10 — thu hẹp phạm vi khi không chắc |  |
  |  |  |
  |  |  |

- Phần nào còn giả (công cụ trả dữ liệu giả, model chế độ giả…) — ghi rõ, không giả làm thật:

## §5. Chỗ khó — 4 lớp + ≥6 kịch bản + 2 tấn công *(guide 2.3)*

| Kịch bản | Lớp (1–4) | Hành vi mong muốn (nói gì, hiện gì, cho làm gì tiếp) | Câu thử |
|---|---|---|---|
|  |  |  |  |
| *(tấn công)* |  |  |  |
| *(tấn công)* |  |  |  |

(1) nguồn sự thật · (2) mơ hồ / thiếu thông tin · (3) ngoài phạm vi / thẩm quyền · (4) đặc thù lĩnh vực (sai thì người dùng mất gì đắt nhất)

## §6. Bốn đường đi của trải nghiệm
- Mọi thứ suôn sẻ: · Không chắc (lớp 2): · Không có căn cứ (lớp 1): · Người dùng sửa:
- Bị đòi ngoài phạm vi (lớp 3): · Trường hợp đặc thù lĩnh vực (lớp 4):

## §7. Đánh giá & chuẩn "đạt" *(guide 2.4, 4.1)*
- Data card: `data/DATA_CARD.md` · bộ câu thử: `eval/benchmark.csv` — __ câu (thuong __ · kho __ · tu_choi __) · metric: `eval/metric_spec.yaml` (__ metric)
- **Chuẩn "đạt"** (chốt **trước 19:30 Thứ Sáu 27/11**, giữ nguyên đến 23:59 Thứ Bảy 28/11): "Đạt khi ≥ __% câu qua, và __"
- Kết quả: lượt 1 __/__ (__%) · lượt 2 __/__ (__%) — run ID: __ / __ → chi tiết `eval/report.md`, hồ sơ `eval/README.md`

## §8. Chi phí khi dùng thật *(guide 4.2)*
- Persona + giá: `cost/personas.yaml` · lượt mô phỏng: `cost/simulate-__.csv` (__ phiên)
- Chi phí / task thành công: __ (model __) · __ (model __)
- Chi phí / tháng ở quy mô thật: thấp __ · cơ sở __ · cao __ → chi tiết `cost/cost-estimate.md`
- So với impact / người / tháng (§2): đáng làm không, vì sao:

## §9. Rủi ro & an toàn
- Dữ liệu: đã ẩn danh gì, không thu gì, không đưa gì vào model gói miễn phí:
- AI **không được** làm gì kể cả khi người dùng yêu cầu:
- Ai có thể bị hại nếu AI sai, và nhóm chặn thế nào:

## §10. Phân công & changelog
- Phân công có tên (theo chặng, chia cặp — guide "Cách chia việc"): __
- Dùng AI vào việc gì (2–3 dòng; chi tiết `docs/ai-usage.md`):
- Nhật ký thay đổi — **mọi thay đổi sau CP2 19:30 Thứ Sáu 27/11 phải có dòng ở đây**:

**CP2 → CP4** (vd thu hẹp lát cắt, hỏi thêm người dùng, lần cải tiến trước lượt 2)

| Thời điểm | Đổi gì | Vì sao (trỏ về câu thử / lỗi / bằng chứng nào) |
|---|---|---|
|  |  |  |

**Sau CP4 (đến 23:59 Thứ Bảy 28/11)** (sửa theo góp ý — không sửa chuẩn "đạt", câu thử, số bằng chứng, kết quả các lượt đã chạy)

| Thời điểm | Đổi gì | Vì sao |
|---|---|---|
|  |  |  |
