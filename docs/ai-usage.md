# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Claude Code | Viết khung `codebase/tools.py`, `agent.py`, `ai.py`, `eval/grade.py` theo thiết kế §4 | Đọc lại, chạy thử với model giả; kiểm lớp chặn bằng model giả "hư" (0/16 vượt hạn mức) | Nguyễn Tuấn Bách, Hoàng Hải Nam |
| Prompt / thiết kế lời gọi mô hình | Claude Code | Viết nháp `SYSTEM` trong `agent.py` | Nhóm sửa sau lượt 1 theo lỗi thấy được | Hoàng Hải Nam |
| Đào data (viết script đếm, gợi ý nhãn) | Claude Code | Cào 100 review (`scrape.py`), gắn nhãn lượt đầu theo bảng nhãn ghi trước, viết `count.py` | Kiểm tay __ dòng (stt 1–30), khớp __/30 | Phạm Thanh Tùng |
| Rà câu hỏi phỏng vấn / khảo sát | Claude Code | Soạn nháp bộ câu khảo sát + kịch bản phỏng vấn (hỏi hành vi đã xảy ra) | Nhóm đọc lại, bỏ câu dẫn dắt | Vũ Nhật Minh, Hoàng Hải Nam |
| Viết câu thử (benchmark) | Claude Code | Viết 16 câu đầu từ kịch bản §5 và 6 review thật | Mỗi câu thử có `source`; người thứ hai kiểm `expected` theo `data/policy.json` | Phạm Thanh Tùng |
| Sinh data `synthetic` (nếu có) | Claude Code | Viết `data/generate.py` | Seed 42 · kiểm tay __/16 đơn kịch bản | Nguyễn Tuấn Bách |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | | | | |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
