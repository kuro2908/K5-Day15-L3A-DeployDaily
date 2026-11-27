"""MẪU PHỤ — KHÔNG dùng để đếm %. Lọc review có chữ "thiếu" trong 2.000 review mới nhất của ShopeeFood trên Google Play,
chỉ để lấy ví dụ nguyên văn / nguồn câu thử (source = data_that). Mẫu đếm chính: shopeefood-gp-100.csv (scrape.py, count.py).

Chạy: pip install google-play-scraper && python evidence/reviews/scrape_tukhoa.py
Ra:   evidence/reviews/shopeefood-gp-tukhoa-thieu.csv (stt, ngay, so_sao, trich ≤ 2 câu) — không lưu tên người viết.
Bản đang dùng: chạy 27/11/2026 17:16, 13/2000 review khớp (review từ 07/07/2026 đến 26/11/2026).
Chạy lại sẽ ra mẫu mới hơn → stt đổi; câu thử trỏ về bản đã commit.
"""
import csv
import re
import sys
from pathlib import Path

from google_play_scraper import Sort, reviews

APP_ID = "com.deliverynow"  # ShopeeFood - Ứng dụng giao món
POOL = 2000
KEYWORDS = re.compile(r"\bthiếu\b|\bthieu\b", re.IGNORECASE)
OUT = Path(__file__).resolve().parent / "shopeefood-gp-tukhoa-thieu.csv"


def two_sentences(text):
    parts = re.split(r"(?<=[.!?])\s+", " ".join((text or "").split()))
    return " ".join(parts[:2])


def main():
    pool, token = [], None
    while len(pool) < POOL:
        batch, token = reviews(APP_ID, lang="vi", country="vn", sort=Sort.NEWEST,
                               count=min(200, POOL - len(pool)), continuation_token=token)
        if not batch:
            break
        pool.extend(batch)
        if token is None:
            break
    hits = [r for r in pool if KEYWORDS.search(r["content"] or "")]
    with OUT.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["stt", "ngay", "so_sao", "trich", "ghi_chu"])
        for i, r in enumerate(hits, 1):
            w.writerow([i, r["at"].strftime("%Y-%m-%d"), r["score"], two_sentences(r["content"]), ""])
    print("%d/%d review có chữ 'thiếu' → %s" % (len(hits), len(pool), OUT))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
