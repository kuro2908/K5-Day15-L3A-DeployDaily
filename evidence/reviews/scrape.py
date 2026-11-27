"""Cào review Google Play — chạy: pip install google-play-scraper && python evidence/reviews/scrape.py OUT.json
Lấy 100 review mới nhất (mọi mức sao) của ShopeeFood và 50 của app đối tác nhà hàng. File OUT có toàn văn:
ĐỂ NGOÀI REPO. Repo chỉ giữ bản đã bỏ tên, trích ≤ 2 câu (shopeefood-gp-100.csv). Ngày chạy bản dùng: 27/11/2026."""
import json
import sys

from google_play_scraper import Sort, reviews

out = {}
for app_id, n in [("com.deliverynow", 100), ("com.sea.foody.nowmerchant", 50)]:
    rs, _ = reviews(app_id, lang="vi", country="vn", sort=Sort.NEWEST, count=n)
    out[app_id] = [{"date": r["at"].strftime("%Y-%m-%d"), "score": r["score"], "text": r["content"]} for r in rs]
    print(app_id, len(rs))
json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=0)
