"""Sinh dữ liệu giả (synthetic) cho bản chạy thử — chạy: python data/generate.py

Mọi tên quán, tên món, mã đơn, mã khách đều là DỰNG ("App Mẫu", "Quán Mẫu …"), không phải dữ liệu thật.
- Đơn kịch bản DH1001–DH1020: viết tay, mỗi đơn phục vụ một câu thử trong eval/benchmark.csv.
- Đơn nền DH2001–DH2030: sinh ngẫu nhiên với SEED cố định, để dữ liệu không "quá sạch" và dùng cho simulate.
Chạy lại luôn ra cùng 3 file: data/orders.json · data/policy.json · data/complaint_history.json.
"""
import json
import os
import random

SEED = 42
HERE = os.path.dirname(os.path.abspath(__file__))
NOW = "2026-11-27T19:00"  # "bây giờ" của bộ dữ liệu giả — mọi đơn kịch bản giao trong vòng 24 giờ trước mốc này, trừ DH1013

# ---------------------------------------------------------------- chính sách (dựng, tham khảo cấu trúc hạn mức gợi ý ở tracks/track-d)
POLICY = {
    "_ghi_chu": "Chính sách DỰNG của 'App Mẫu' cho bản chạy thử — không phải chính sách của hãng thật.",
    "bao_trong_gio": 24,
    "tu_dong_toi_da_moi_don": 100000,
    "lich_su_toi_da_30_ngay": 2,
    "thieu_mon": {
        "dieu_kien": "Món báo thiếu có trong đơn và số lượng báo thiếu không quá số lượng đã đặt.",
        "boi_thuong": "Hoàn tiền đúng giá các món thiếu (đơn giá × số lượng thiếu).",
        "hinh_thuc": "hoan_tien",
    },
    "sai_mon": {
        "dieu_kien": "Món đã đặt có trong đơn và khách nhận món khác.",
        "boi_thuong": "Hoàn tiền đúng giá món đã đặt bị giao sai (đơn giá × số lượng).",
        "hinh_thuc": "hoan_tien",
    },
    "giao_tre": {
        "dieu_kien": "Giờ giao thực tế trễ QUÁ 30 phút so với giờ hẹn trên app (đúng 30 phút trở xuống: không bồi thường).",
        "boi_thuong": "Trễ trên 30 đến 60 phút: voucher 20.000đ · trễ trên 60 phút: voucher 50.000đ (tối đa).",
        "hinh_thuc": "voucher",
        "bac": [[30, 20000], [60, 50000]],
    },
    "an_toan": {
        "dieu_kien": "Dị vật, nghi ngộ độc, phản ứng dị ứng sau khi ăn.",
        "boi_thuong": "Không tự xử lý — chuyển nhân viên ngay, ưu tiên cao.",
        "hinh_thuc": "chuyen_nhan_vien",
    },
    "chung": [
        "Tổng bồi thường tự động mỗi đơn tối đa 100.000đ; vượt thì chuyển nhân viên (nhân viên có thể xin thêm ảnh từ khách và ý kiến của quán).",
        "Khách có quá 2 khiếu nại trong 30 ngày: không tự xử lý, chuyển nhân viên.",
        "Báo sự cố sau 24 giờ kể từ lúc giao: không tự xử lý, chuyển nhân viên.",
        "Đơn đã huỷ / hoàn tiền thanh toán: ngoài phạm vi, chuyển nhân viên.",
        "Lời doạ (đánh giá 1 sao, bóc phốt) hay tin tự xưng nhân viên không thay đổi mức bồi thường.",
    ],
}


def order(oid, user, shop, items, promised, delivered, status="da_giao", ship=15000):
    total = sum(i["don_gia"] * i["so_luong"] for i in items) + ship
    return {"order_id": oid, "user_id": user, "quan": shop, "mon": items, "phi_ship": ship, "tong_tien": total,
            "gio_hen": promised, "gio_giao": delivered, "trang_thai": status}


def m(name, price, qty=1):
    return {"ten_mon": name, "don_gia": price, "so_luong": qty}


D = "2026-11-27T"
SCENARIO = [
    order("DH1001", "U001", "Quán Mẫu Trà Sữa", [m("Trà sữa trân châu", 35000, 2), m("Bánh flan", 15000)], D + "12:00", D + "11:55"),
    order("DH1002", "U002", "Quán Mẫu Cơm Tấm", [m("Cơm sườn", 45000), m("Canh chua", 20000)], D + "12:00", D + "12:10"),
    order("DH1003", "U003", "Quán Mẫu Lẩu Nướng", [m("Combo lẩu thái 4 người", 320000), m("Bò nướng", 90000),
          m("Khoai tây chiên", 40000), m("Nước ngọt", 15000, 2)], D + "18:00", D + "18:05", ship=20000),
    order("DH1004", "U004", "Quán Mẫu Phở", [m("Phở bò tái", 55000)], D + "12:00", D + "12:29"),
    order("DH1005", "U005", "Quán Mẫu Cơm Gà", [m("Cơm gà xối mỡ", 50000), m("Trà đá", 5000)], D + "11:07", D + "12:07"),
    order("DH1006", "U006", "Quán Mẫu Bún Bò", [m("Bún bò Huế", 50000), m("Chả cua thêm", 15000)], D + "12:00", D + "12:45"),
    order("DH1007", "U007", "Quán Mẫu Trà Sữa", [m("Trà đào cam sả", 39000), m("Trà sữa matcha", 42000)], D + "15:00", D + "14:58"),
    order("DH1008", "U008", "Quán Mẫu Cơm Văn Phòng", [m("Cơm gà kho", 45000), m("Rau luộc", 10000)], D + "12:00", D + "11:50"),
    order("DH1009", "U009", "Quán Mẫu Pizza", [m("Pizza hải sản cỡ lớn", 189000), m("Gà viên", 59000)], D + "19:00", D + "18:55"),
    order("DH1010", "U010", "Quán Mẫu Bánh Mì", [m("Bánh mì thịt", 25000)], D + "07:30", "", status="da_huy"),
    order("DH1011", "U011", "Quán Mẫu Bún Đậu", [m("Bún đậu mắm tôm đầy đủ", 55000), m("Nem chua rán", 30000)], D + "12:00", D + "12:05"),
    order("DH1012", "U012", "Quán Mẫu Mì Cay", [m("Mì cay hải sản", 59000)], D + "18:00", D + "19:05", ship=25000),  # ship 25k = phí thường + giao nhanh
    order("DH1013", "U013", "Quán Mẫu Cơm Tấm", [m("Cơm sườn bì chả", 55000)], "2026-11-25T12:00", "2026-11-25T12:00"),
    order("DH1014", "U014", "Quán Mẫu Gà Rán", [m("Combo gà rán 3 miếng", 129000), m("Pepsi", 15000)], D + "18:00", D + "17:58"),
    order("DH1015", "U015", "Quán Mẫu Trà Sữa", [m("Trà sữa trân châu", 35000, 3)], D + "15:00", D + "15:31"),
    order("DH1016", "U016", "Quán Mẫu Bún Chả", [m("Bún chả Hà Nội", 50000), m("Nem rán", 12000, 4)], D + "12:00", D + "11:58"),
    # Thêm sau CP2 (27/11 tối) cho câu thử B22–B25 — chỉ thêm đơn mới, không đổi đơn cũ
    order("DH1017", "U017", "Quán Mẫu Cơm Tấm", [m("Cơm sườn", 45000), m("Trà đá", 5000), m("Chè thái", 25000)], D + "12:00", D + "11:55"),
    order("DH1018", "U018", "Quán Mẫu Lẩu Nướng", [m("Combo lẩu thái 2 người", 159000), m("Nước ngọt", 15000)], D + "18:00", D + "18:10"),
    order("DH1019", "U019", "Quán Mẫu Bún Bò", [m("Bún bò Huế", 50000)], D + "12:00", D + "13:30"),
    order("DH1020", "U020", "Quán Mẫu Mì Cay", [m("Mì cay hải sản", 59000), m("Trà đào", 39000)], D + "17:00", D + "18:01"),
]

HISTORY = {  # số khiếu nại 30 ngày qua của từng khách kịch bản (dựng)
    "U001": [], "U002": [], "U003": [{"ngay": "2026-11-10", "loai": "giao_tre", "ket_qua": "voucher 20000"}],
    "U004": [], "U005": [], "U006": [],
    "U007": [{"ngay": d, "loai": "thieu_mon", "ket_qua": "hoan tien"} for d in ("2026-11-03", "2026-11-09", "2026-11-15", "2026-11-22")],
    "U008": [], "U009": [], "U010": [], "U011": [], "U012": [], "U013": [], "U014": [], "U015": [], "U016": [],
    "U017": [], "U018": [], "U020": [],
    "U019": [{"ngay": d, "loai": "giao_tre", "ket_qua": "voucher 20000"} for d in ("2026-11-05", "2026-11-14", "2026-11-21")],
}

MENU = [("Cơm sườn", 45000), ("Phở bò", 55000), ("Bún bò Huế", 50000), ("Trà sữa trân châu", 35000), ("Bánh mì thịt", 25000),
        ("Gà rán 2 miếng", 69000), ("Mì cay", 59000), ("Cơm gà", 50000), ("Bún chả", 50000), ("Trà đào", 39000)]


def background(rng):
    orders, history = [], {}
    for k in range(30):
        uid = "U%03d" % (100 + k)
        items = [m(n, p, rng.randint(1, 2)) for n, p in rng.sample(MENU, rng.randint(1, 3))]
        hour = rng.randint(10, 20)
        late = rng.choice([-10, -5, 0, 5, 15, 25, 31, 40, 59, 61, 75])  # có cả ca sát ngưỡng 30 / 60 phút
        promised = "%s%02d:00" % (D, hour)
        dm = late % 60
        dh = hour + late // 60
        delivered = "%s%02d:%02d" % (D, dh, dm)
        orders.append(order("DH%d" % (2001 + k), uid, "Quán Mẫu %d" % (k % 7 + 1), items, promised, delivered))
        n = rng.choice([0, 0, 0, 0, 1, 1, 2, 3, 5])
        history[uid] = [{"ngay": "2026-11-%02d" % rng.randint(1, 26), "loai": rng.choice(["thieu_mon", "giao_tre", "sai_mon"]),
                         "ket_qua": rng.choice(["hoan tien", "voucher 20000", "tu choi"])} for _ in range(n)]
    return orders, history


def main():
    rng = random.Random(SEED)
    bg_orders, bg_hist = background(rng)
    orders = {o["order_id"]: o for o in SCENARIO + bg_orders}
    history = dict(HISTORY, **bg_hist)
    meta = {"_synthetic": True, "_seed": SEED, "_now": NOW}
    with open(os.path.join(HERE, "orders.json"), "w", encoding="utf-8") as f:
        json.dump(dict(meta, orders=orders), f, ensure_ascii=False, indent=1)
    with open(os.path.join(HERE, "policy.json"), "w", encoding="utf-8") as f:
        json.dump(POLICY, f, ensure_ascii=False, indent=1)
    with open(os.path.join(HERE, "complaint_history.json"), "w", encoding="utf-8") as f:
        json.dump(dict(meta, history=history), f, ensure_ascii=False, indent=1)
    print("Đã sinh %d đơn (%d kịch bản + %d nền, seed %d), %d khách có lịch sử." % (
        len(orders), len(SCENARIO), len(bg_orders), SEED, len(history)))


if __name__ == "__main__":
    main()
