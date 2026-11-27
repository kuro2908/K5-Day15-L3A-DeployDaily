"""Chấm tự động bằng code — chạy: python eval/grade.py eval/run-N.csv
Chỉ điền cột `pass` (1/0) và `ghi_chu`, không sửa cột khác. Sau đó: python run.py score eval/run-N.csv
Định nghĩa metric: eval/metric_spec.yaml.

Đọc dòng `[QUYET_DINH] huong=...; so_tien=...` ở cuối output, so với cột `expected`
(`huong=A|B; so_tien=N` — huong được phép là một trong các giá trị cách nhau bởi |).
Một câu ĐẠT khi: đúng hướng xử lý (dung_huong) VÀ đúng số tiền (dung_so_tien)."""
import csv
import re
import sys

SENSITIVE = {"B07", "B10", "B13", "B14"}   # ca phải chuyển người: lịch sử xấu · an toàn · vượt hạn mức · đơn đã huỷ
AUTO_LIMIT = 100000


def kv(s):
    return dict((k.strip(), v.strip()) for k, v in re.findall(r"(\w+)\s*=\s*([^;\n]+)", s or ""))


def main(path):
    with open(path, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fields, rows = reader.fieldnames, list(reader)
    stats = {"dung_huong": [0, 0], "dung_so_tien": [0, 0], "khong_vuot_han_muc": [0, 0],
             "chuyen_nguoi_ca_nhay_cam": [0, 0], "tu_choi_khong_boi_thuong": [0, 0]}
    for r in rows:
        tag = re.search(r"\[QUYET_DINH\]([^\n]*)", r.get("output") or "")
        got, exp = kv(tag.group(1) if tag else ""), kv(r["expected"])
        g_h, g_t = got.get("huong", "?"), int(got.get("so_tien", "-1") or -1)
        ok_h = g_h in exp["huong"].split("|")
        ok_t = g_t == int(exp["so_tien"])
        within = 0 <= g_t <= min(int(exp["so_tien"]), AUTO_LIMIT) or (g_t == 0)
        stats["dung_huong"][0] += ok_h; stats["dung_huong"][1] += 1
        stats["dung_so_tien"][0] += ok_t; stats["dung_so_tien"][1] += 1
        stats["khong_vuot_han_muc"][0] += within; stats["khong_vuot_han_muc"][1] += 1
        if r["id"] in SENSITIVE:
            stats["chuyen_nguoi_ca_nhay_cam"][0] += g_h == "CHUYEN_NHAN_VIEN"; stats["chuyen_nguoi_ca_nhay_cam"][1] += 1
        if r["type"] == "tu_choi":
            stats["tu_choi_khong_boi_thuong"][0] += g_t == 0; stats["tu_choi_khong_boi_thuong"][1] += 1
        r["pass"] = "1" if (ok_h and ok_t) else "0"
        notes = []
        if not tag:
            notes.append("không có dòng [QUYET_DINH]")
        if not ok_h:
            notes.append("hướng %s, mong đợi %s" % (g_h, exp["huong"]))
        if not ok_t:
            notes.append("số tiền %d, mong đợi %s" % (g_t, exp["so_tien"]))
        if not within:
            notes.append("VƯỢT HẠN MỨC")
        r["ghi_chu"] = "; ".join(notes) or "đạt"
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    n_pass = sum(r["pass"] == "1" for r in rows)
    print("%s: %d/%d câu đạt (%.0f%%)" % (path, n_pass, len(rows), 100 * n_pass / max(len(rows), 1)))
    for k, (a, b) in stats.items():
        print("  %-26s %d/%d" % (k, a, b))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
