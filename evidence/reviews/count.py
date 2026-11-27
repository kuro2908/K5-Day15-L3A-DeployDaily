"""Đếm nhãn review — chạy: python evidence/reviews/count.py
Đọc evidence/reviews/shopeefood-gp-100.csv (cách chọn mẫu + bảng nhãn: evidence/data-mining.md mục 1).
Mẫu số N = mọi review đã đọc, kể cả khen / khac."""
import collections, csv, os, sys

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "shopeefood-gp-100.csv")
rows = list(csv.DictReader(open(path, encoding="utf-8")))
N = len(rows)
c = collections.Counter(r["nhan"] for r in rows)
complaints = N - c["khen"]
print("N = %d review (ngày %s → %s)" % (N, min(r["ngay"] for r in rows), max(r["ngay"] for r in rows)))
for k, v in c.most_common():
    print("  %-15s %3d/%d  (%4.1f%%)  ·  trong %d review có phàn nàn: %4.1f%%" % (k, v, N, 100 * v / N, complaints, 100 * v / complaints if k != "khen" else 0))
d1 = sum(1 for r in rows if r["nhan"] in ("thieu_sai_mon", "khieu_nai_kho") or r["co_khieu_nai_kho"] == "1")
d1b = c["tre"]
print("Chỉ số D1 (thieu_sai_mon hoặc khieu_nai_kho): %d/%d (%.1f%%)" % (d1, N, 100 * d1 / N))
print("Chỉ số giao trễ (tre):                        %d/%d (%.1f%%)" % (d1b, N, 100 * d1b / N))
print("1–2 sao: %d/%d · trong đó tre: %d" % (sum(1 for r in rows if int(r["so_sao"]) <= 2), N,
      sum(1 for r in rows if int(r["so_sao"]) <= 2 and r["nhan"] == "tre")))
