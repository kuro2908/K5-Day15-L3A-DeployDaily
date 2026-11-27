"""Công cụ của bài toán — khiếu nại đơn đồ ăn (thiếu / sai món, giao trễ). Thiết kế: spec.md §4.

Dữ liệu đọc: data/orders.json · data/policy.json · data/complaint_history.json (synthetic, sinh bằng data/generate.py, seed 42).

Ba nhóm công cụ:
- CHỈ ĐỌC:           get_order · get_policy · get_complaint_history
- TÍNH BẰNG CODE:    compute_compensation (thay cho check_limit) — model KHÔNG BAO GIỜ tự tính tiền
- TÁC ĐỘNG RA NGOÀI: issue_refund · issue_voucher · escalate_to_human — trong bản chạy thử CHỈ TẠO BẢN NHÁP
                     (không có hệ thống thật phía sau). Chỉ agent.py gọi, SAU khi đã qua lớp chặn rủi ro.
"""
import datetime
import json
import os

from tracing import tool, TOOLS  # noqa: F401

DATA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")


def _load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return json.load(f)


_ORDERS = _load("orders.json")
_POLICY = _load("policy.json")
_HISTORY = _load("complaint_history.json")
NOW = datetime.datetime.fromisoformat(_ORDERS["_now"])


def _norm(s):
    return " ".join((s or "").lower().split())


# ------------------------------------------------------------------ chỉ đọc
@tool
def get_order(order_id: str):
    """Tra đơn. Input: mã đơn (str, vd "DH1001"). Output: dict đơn (món, đơn giá, số lượng, giờ hẹn, giờ giao,
    trạng thái, mã khách) hoặc None nếu không có. Không tác động ra ngoài."""
    return _ORDERS["orders"].get((order_id or "").strip().upper())


@tool
def get_policy(issue_type: str = ""):
    """Tra chính sách. Input: loại sự cố (thieu_mon | sai_mon | giao_tre | an_toan) hoặc rỗng = quy định chung.
    Output: dict điều kiện + mức bồi thường + quy định chung. Không tác động ra ngoài."""
    out = {"chung": _POLICY["chung"]}
    if issue_type in _POLICY:
        p = dict(_POLICY[issue_type])
        p.pop("bac", None)
        out[issue_type] = p
    return out


@tool
def get_complaint_history(user_id: str):
    """Tra lịch sử khiếu nại 30 ngày qua của khách. Input: mã khách. Output: {"so_lan_30_ngay": int, "chi_tiet": [...]}.
    Không tác động ra ngoài."""
    h = _HISTORY["history"].get(user_id, [])
    return {"so_lan_30_ngay": len(h), "chi_tiet": h}


# ------------------------------------------------------------------ tính bằng code
@tool
def compute_compensation(order_id: str, issue_type: str, items: list = None):
    """Tính bồi thường theo chính sách — CODE, không phải AI.
    Input: mã đơn · loại sự cố (thieu_mon | sai_mon | giao_tre | an_toan | khac) · danh sách món khách báo
    [{"ten_mon", "so_luong"}] (cho thieu_mon / sai_mon).
    Output: {"ket_luan": "du_dieu_kien" | "khong_du_dieu_kien" | "can_hoi_them" | "chuyen_nhan_vien",
             "hinh_thuc": "hoan_tien" | "voucher" | None, "so_tien": int, "ly_do": str, "chi_tiet": [...]}
    Không tác động ra ngoài."""
    o = _ORDERS["orders"].get((order_id or "").strip().upper())
    if not o:
        return {"ket_luan": "can_hoi_them", "hinh_thuc": None, "so_tien": 0, "ly_do": "không tìm thấy mã đơn", "chi_tiet": []}
    if o["trang_thai"] != "da_giao":
        return _human("đơn ở trạng thái '%s' (đã huỷ / hoàn thanh toán) — ngoài phạm vi tự xử lý" % o["trang_thai"])
    if issue_type == "an_toan":
        return _human("sự cố an toàn thực phẩm (dị vật / nghi ngộ độc / dị ứng) — chuyển nhân viên ngay")
    if issue_type not in ("thieu_mon", "sai_mon", "giao_tre"):
        return _human("loại sự cố ngoài phạm vi tự xử lý")
    hours = (NOW - datetime.datetime.fromisoformat(o["gio_giao"])).total_seconds() / 3600
    if hours > _POLICY["bao_trong_gio"]:
        return _human("báo sau %d giờ kể từ lúc giao (quá %d giờ)" % (hours, _POLICY["bao_trong_gio"]))
    n_hist = len(_HISTORY["history"].get(o["user_id"], []))
    if n_hist > _POLICY["lich_su_toi_da_30_ngay"]:
        return _human("khách đã khiếu nại %d lần trong 30 ngày (quá %d)" % (n_hist, _POLICY["lich_su_toi_da_30_ngay"]))

    if issue_type == "giao_tre":
        late = (datetime.datetime.fromisoformat(o["gio_giao"]) - datetime.datetime.fromisoformat(o["gio_hen"])).total_seconds() / 60
        amount = 0
        for threshold, value in _POLICY["giao_tre"]["bac"]:
            if late > threshold:
                amount = value
        if amount == 0:
            return {"ket_luan": "khong_du_dieu_kien", "hinh_thuc": None, "so_tien": 0, "chi_tiet": [],
                    "ly_do": "đơn giao trễ %d phút so với giờ hẹn, chưa quá 30 phút nên chưa thuộc diện bồi thường" % max(late, 0)}
        return {"ket_luan": "du_dieu_kien", "hinh_thuc": "voucher", "so_tien": amount, "chi_tiet": [],
                "ly_do": "đơn giao trễ %d phút so với giờ hẹn → voucher %s" % (late, _vnd(amount))}

    # thieu_mon / sai_mon
    if not items:
        return {"ket_luan": "can_hoi_them", "hinh_thuc": None, "so_tien": 0, "chi_tiet": [],
                "ly_do": "chưa rõ món nào bị thiếu / sai"}
    by_name = {_norm(i["ten_mon"]): i for i in o["mon"]}
    total, detail, missing = 0, [], []
    for it in items:
        name = _norm(it.get("ten_mon"))
        line = by_name.get(name) or next((v for k, v in by_name.items() if name and (name in k or k in name)), None)
        if not line:
            missing.append(it.get("ten_mon"))
            continue
        qty = int(it.get("so_luong") or 1)
        if qty > line["so_luong"]:
            missing.append("%s × %d (đơn chỉ có %d)" % (line["ten_mon"], qty, line["so_luong"]))
            continue
        total += line["don_gia"] * qty
        detail.append({"ten_mon": line["ten_mon"], "so_luong": qty, "don_gia": line["don_gia"], "thanh_tien": line["don_gia"] * qty})
    if missing:
        return {"ket_luan": "can_hoi_them", "hinh_thuc": None, "so_tien": 0, "chi_tiet": detail,
                "ly_do": "món khách báo không khớp với đơn: %s" % ", ".join(str(x) for x in missing)}
    if total > _POLICY["tu_dong_toi_da_moi_don"]:
        r = _human("tổng bồi thường %s vượt hạn mức tự động %s / đơn" % (_vnd(total), _vnd(_POLICY["tu_dong_toi_da_moi_don"])))
        r["chi_tiet"] = detail
        return r
    names = ", ".join("%s × %d" % (d["ten_mon"], d["so_luong"]) for d in detail)
    return {"ket_luan": "du_dieu_kien", "hinh_thuc": "hoan_tien", "so_tien": total, "chi_tiet": detail,
            "ly_do": "%s: %s → hoàn %s" % ("thiếu món" if issue_type == "thieu_mon" else "giao sai món", names, _vnd(total))}


def _human(reason):
    return {"ket_luan": "chuyen_nhan_vien", "hinh_thuc": None, "so_tien": 0, "ly_do": reason, "chi_tiet": []}


def _vnd(x):
    return "{:,}đ".format(int(x)).replace(",", ".")


# ------------------------------------------------------------------ tác động ra ngoài (bản nháp)
@tool
def issue_refund(order_id: str, amount: int):
    """Hoàn tiền cho khách — KHÓ ĐẢO (tiền đi khỏi quán). Input: mã đơn, số tiền (int, lấy từ compute_compensation).
    Output: lệnh hoàn NHÁP {"loai": "hoan_tien", "trang_thai": "nhap"}. Bản chạy thử không trừ tiền thật."""
    return {"loai": "hoan_tien", "order_id": order_id, "so_tien": int(amount), "trang_thai": "nhap"}


@tool
def issue_voucher(order_id: str, amount: int):
    """Tặng voucher cho khách — khó đảo (voucher đã gửi). Input: mã đơn, giá trị (int, lấy từ compute_compensation).
    Output: voucher NHÁP. Bản chạy thử không gửi voucher thật."""
    return {"loai": "voucher", "order_id": order_id, "so_tien": int(amount), "trang_thai": "nhap"}


@tool
def escalate_to_human(order_id: str, reason: str, priority: str = "thuong"):
    """Chuyển nhân viên — ĐẢO ĐƯỢC. Input: mã đơn (có thể rỗng), lý do, mức ưu tiên (thuong | cao).
    Output: phiếu chuyển NHÁP."""
    return {"loai": "chuyen_nhan_vien", "order_id": order_id or "", "ly_do": reason, "uu_tien": priority, "trang_thai": "nhap"}
