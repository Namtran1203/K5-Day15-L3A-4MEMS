"""Tra dữ liệu giả lập và kiểm tra ràng buộc lịch trình."""
import json
from datetime import datetime, timedelta
from pathlib import Path
from tracing import tool


@tool
def read_park():
    """Tra khu giả lập; input: không; output: dữ liệu khu; không tác động ra ngoài."""
    with (Path(__file__).resolve().parent.parent / "data" / "park.json").open(encoding="utf-8") as f:
        return json.load(f)


@tool
def make_schedule(request, park):
    """Xếp lịch; input: yêu cầu và dữ liệu khu; output: lịch hoặc lý do; không tác động ra ngoài."""
    fields = {"people":"số người", "budget_per_person":"ngân sách/người", "start":"giờ bắt đầu", "end":"giờ kết thúc", "interests":"sở thích", "avoid_intense":"giới hạn cảm giác mạnh", "weather":"thời tiết"}
    missing = [label for key, label in fields.items() if key not in request or request[key] is None]
    if missing:
        return "Vui lòng bổ sung: " + ", ".join(missing) + "."
    people, budget = request["people"], request["budget_per_person"]
    if type(people) is not int or people < 1 or type(budget) is not int or budget < 0 or type(request["avoid_intense"]) is not bool:
        return "Số người, ngân sách hoặc giới hạn cảm giác mạnh không hợp lệ."
    interests, order = request["interests"], request.get("activity_order", [])
    if not isinstance(interests, list) or any(not isinstance(x, str) for x in interests) or not isinstance(order, list) or any(not isinstance(x, str) for x in order):
        return "Sở thích và thứ tự hoạt động phải là danh sách chuỗi."
    weather = request["weather"]
    if weather not in ("khô", "mưa", "không rõ"):
        return "Vui lòng cho biết thời tiết là khô, mưa hoặc không rõ."
    try:
        parse = lambda value: datetime.strptime(value, "%H:%M")
        start, end = parse(request["start"]), parse(request["end"])
    except (ValueError, TypeError):
        return "Giờ không hợp lệ; hãy nhập HH:MM."
    if start >= end or start < parse(park["open"]) or end > parse(park["close"]):
        return "Khung giờ nằm ngoài giờ mở cửa {}–{} hoặc không hợp lệ. Hãy điều chỉnh khung giờ.".format(park["open"], park["close"])
    if budget < park["ticket"]:
        return "Không đủ ngân sách: vé vào cổng {:,} đồng/người. Hãy tăng ngân sách.".format(park["ticket"])
    lookup = {a["name"]: a for a in park["activities"]}
    if len(set(order)) != len(order) or any(x not in lookup for x in order):
        return "Có hoạt động không tồn tại hoặc bị lặp trong dữ liệu giả lập; hãy chọn lại."
    activities = [lookup[x] for x in order] if order else list(park["activities"])
    if not order:
        activities.sort(key=lambda a: -sum(t.casefold() in (a["name"] + " " + " ".join(a["tags"])).casefold() for t in interests))
    cursor, total, lines = start, park["ticket"], []
    for activity in activities:
        if request["avoid_intense"] and activity["intense"] or weather != "khô" and not activity["indoor"]:
            continue
        earliest = cursor + (timedelta(minutes=park["travel_minutes"]) if lines else timedelta())
        begin = max(earliest, parse(activity["open"]))
        if activity.get("fixed_start"):
            begin = parse(activity["fixed_start"])
            if begin < earliest:
                continue
        finish = begin + timedelta(minutes=activity["duration"])
        if finish > min(end, parse(activity["close"])) or total + activity["price"] > budget:
            continue
        lines.append("{}–{}: {} ({:,} đồng/người; {})".format(begin.strftime("%H:%M"), finish.strftime("%H:%M"), activity["name"], activity["price"], ", ".join(activity["tags"])))
        total += activity["price"]
        cursor = finish
    if not lines:
        return "Chưa xếp được hoạt động; hãy nới thời gian, ngân sách hoặc giới hạn."
    return "Lịch gợi ý từ dữ liệu giả lập (v{}):\n".format(park["version"]) + "\n".join(lines) + "\nTổng: {:,} đồng/người; {:,} đồng/{} người, gồm vé. Di chuyển: {} phút giữa các điểm. Thời tiết do người dùng cung cấp: {}.".format(total, total * people, people, park["travel_minutes"], weather)
