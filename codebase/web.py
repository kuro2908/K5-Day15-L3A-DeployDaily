"""Giao diện web cho bản chạy thử — chạy: python run.py web  (mở http://127.0.0.1:8000)

Chỉ dùng thư viện chuẩn. Gọi ĐÚNG hàm answer() trong agent.py như `run.py eval`, nên kết quả trên giao diện
khớp với cách chấm. Mỗi lượt hỏi được bọc bằng tracing.begin()/end() để hiện "đường đi" của quyết định
(công cụ đã gọi, model chọn gì, code tính gì, lớp chặn có can thiệp không).

Không ghi trace ra file, không đổi eval/ hay traces/. Chỉ nghe ở 127.0.0.1 (máy của mình).
"""
import ast
import json
import os
import re
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import tracing  # noqa: E402

tracing.PREVIEW = 6000  # chỉ trong tiến trình web: giữ đủ output công cụ để hiện lý do (không đổi file tracing.py)

import ai  # noqa: E402
import agent  # noqa: E402
import tools  # noqa: E402

PAGE = os.path.join(HERE, "web", "index.html")
TAG_RE = re.compile(r"\[QUYET_DINH\]\s*([^\n]*)")
SCENARIO_IDS = ["DH%d" % n for n in range(1001, 1021)]
_LOCK = __import__("threading").Lock()  # tracing dùng trạng thái chung → mỗi lúc một lượt


def _lit(text):
    try:
        return ast.literal_eval(text)
    except Exception:
        return None


def _model_json(text):
    m = re.search(r"\{.*\}", text or "", re.DOTALL)
    try:
        return json.loads(m.group(0)) if m else None
    except json.JSONDecodeError:
        return None


def _order_card(order_id):
    o = tools._ORDERS["orders"].get(order_id) if order_id else None
    if not o:
        return None
    return {"order_id": o["order_id"], "quan": o["quan"], "mon": o["mon"], "phi_ship": o["phi_ship"],
            "tong_tien": o["tong_tien"], "gio_hen": o["gio_hen"], "gio_giao": o["gio_giao"], "trang_thai": o["trang_thai"]}


def handle_message(text):
    with _LOCK:
        tracing.begin("web")
        error = ""
        try:
            out = agent.answer(text)["output"]
        except Exception as e:  # lỗi model / mạng: báo rõ, không giả câu trả lời
            out, error = "", "%s: %s" % (type(e).__name__, e)
        summary, events = tracing.end()

    tag = TAG_RE.search(out or "")
    decision = dict(re.findall(r"(\w+)\s*=\s*([^;\n]+)", tag.group(1))) if tag else {}
    decision = {k: v.strip() for k, v in decision.items()}
    reply = TAG_RE.sub("", out or "").strip()

    steps, order_id = [], decision.get("ma_don", "-")
    for e in events:
        if e["kind"] == "tool" and e["name"] == "get_order":
            o = _lit(e.get("output", ""))
            steps.append({"key": "order", "ok": bool(o),
                          "text": ("Tìm thấy đơn %s" % o["order_id"]) if o else "Không có mã đơn hợp lệ trong tin nhắn"})
        elif e["kind"] == "tool" and e["name"] == "get_complaint_history":
            h = _lit(e.get("output", "")) or {}
            n = h.get("so_lan_30_ngay", 0)
            steps.append({"key": "history", "ok": n <= 2, "text": "Khách có %d khiếu nại trong 30 ngày" % n})
        elif e["kind"] == "model":
            j = _model_json(e.get("output", "")) or {}
            mon = ", ".join("%s × %s" % (m.get("ten_mon"), m.get("so_luong")) for m in j.get("mon") or [])
            steps.append({"key": "model", "ok": bool(j), "model": e.get("model", ""),
                          "text": ("AI hiểu: %s%s, đề xuất %s" % (j.get("loai_su_co", "?"), (" (%s)" % mon) if mon else "",
                                                                 j.get("huong", "?"))) if j else "AI trả lời không đọc được — chuyển nhân viên"})
        elif e["kind"] == "tool" and e["name"] == "compute_compensation":
            c = _lit(e.get("output", "")) or {}
            steps.append({"key": "code", "ok": c.get("ket_luan") == "du_dieu_kien",
                          "text": "Code tính theo chính sách: %s" % (c.get("ly_do") or c.get("ket_luan", "?"))})
        elif e["kind"] == "note" and str(e.get("text", "")).startswith("chặn"):
            steps.append({"key": "guard", "ok": False, "text": "Lớp chặn can thiệp — " + e["text"][len("chặn: "):]})
        elif e["kind"] == "tool" and e["name"] in ("issue_refund", "issue_voucher", "escalate_to_human"):
            label = {"issue_refund": "Tạo lệnh hoàn tiền (bản nháp)", "issue_voucher": "Tạo voucher (bản nháp)",
                     "escalate_to_human": "Tạo phiếu chuyển nhân viên (bản nháp)"}[e["name"]]
            steps.append({"key": "action", "ok": True, "text": label})
    if not any(s["key"] == "guard" for s in steps) and any(s["key"] == "model" for s in steps):
        idx = next(i for i, s in enumerate(steps) if s["key"] == "model") + 1
        while idx < len(steps) and steps[idx]["key"] == "code":
            idx += 1
        steps.insert(idx, {"key": "guard", "ok": True, "text": "Lớp chặn không cần can thiệp"})

    return {"reply": reply, "decision": decision, "steps": steps, "error": error,
            "order": _order_card(order_id if order_id != "-" else ""),
            "meta": {"model": ", ".join(summary["models"]) or ai.MODEL_PROVIDER, "model_calls": summary["model_calls"],
                     "tool_calls": summary["tool_calls"], "tokens_in": summary["tokens_in"], "tokens_out": summary["tokens_out"]}}


def orders_list():
    out = []
    for oid in SCENARIO_IDS:
        card = _order_card(oid)
        if card:
            out.append(card)
    return {"orders": out, "mode": ai.MODEL_PROVIDER}


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        data = body if isinstance(body, bytes) else json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        path = urlsplit(self.path).path
        if path in ("/", "/index.html"):
            with open(PAGE, "rb") as f:
                return self._send(200, f.read(), "text/html; charset=utf-8")
        if path == "/api/orders":
            return self._send(200, orders_list())
        return self._send(404, {"error": "không có trang này"})

    def do_POST(self):
        if self.path != "/api/message":
            return self._send(404, {"error": "không có API này"})
        try:
            n = int(self.headers.get("Content-Length") or 0)
            text = (json.loads(self.rfile.read(n) or b"{}").get("text") or "").strip()
        except (ValueError, json.JSONDecodeError):
            return self._send(400, {"error": "Dữ liệu gửi lên không đúng dạng JSON"})
        if not text:
            return self._send(400, {"error": "Tin nhắn đang trống"})
        if len(text) > 1000:
            return self._send(400, {"error": "Tin nhắn dài quá 1000 ký tự"})
        return self._send(200, handle_message(text))

    def log_message(self, fmt, *args):
        sys.stderr.write("[web] " + fmt % args + "\n")


def main(port=8000):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print("Giao diện bản chạy thử: http://127.0.0.1:%d  (model: %s) — dừng: Ctrl+C" % (port, ai.MODEL_PROVIDER))
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nĐã dừng.")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 8000)
