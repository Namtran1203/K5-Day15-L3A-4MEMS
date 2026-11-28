"""Tra dữ liệu giả lập và kiểm tra ràng buộc lịch trình."""
import json
from datetime import datetime, timedelta
from pathlib import Path
from tracing import tool


REQUEST_FIELDS = {
    "people": "số người",
    "budget_per_person": "ngân sách/người",
    "start": "giờ bắt đầu (HH:MM)",
    "end": "giờ kết thúc (HH:MM)",
    "interests": "sở thích",
    "avoid_intense": "giới hạn cảm giác mạnh",
    "weather": "thời tiết (khô, mưa hoặc không rõ)",
}


def parse_time(value):
    try:
        return datetime.strptime(value, "%H:%M")
    except (ValueError, TypeError):
        return None


@tool
def read_park():
    """Tra khu giả lập; input: không; output: dữ liệu khu; không tác động ra ngoài."""
    with (Path(__file__).resolve().parent.parent / "data" / "park.json").open(encoding="utf-8") as f:
        return json.load(f)


@tool
def make_schedule(request, park):
    """Xếp lịch; input: yêu cầu và dữ liệu khu; output: lịch hoặc lý do; không tác động ra ngoài."""
    people, budget = request.get("people"), request.get("budget_per_person")
    interests = request.get("interests")
    weather = request.get("weather")
    start, end = parse_time(request.get("start")), parse_time(request.get("end"))
    valid = {
        "people": type(people) is int and people > 0,
        "budget_per_person": type(budget) is int and budget >= 0,
        "start": start is not None,
        "end": end is not None,
        "interests": isinstance(interests, list) and all(isinstance(item, str) for item in interests),
        "avoid_intense": type(request.get("avoid_intense")) is bool,
        "weather": weather in ("khô", "mưa", "không rõ"),
    }
    if start is not None and end is not None:
        if start >= end or start < parse_time(park["open"]) or end > parse_time(park["close"]):
            return "Khung giờ nằm ngoài giờ mở cửa {}–{} hoặc không hợp lệ. Hãy điều chỉnh khung giờ.".format(park["open"], park["close"])
    if valid["budget_per_person"] and budget < park["ticket"]:
        return "Không đủ ngân sách: vé vào cổng {:,} đồng/người. Hãy tăng ngân sách.".format(park["ticket"])
    needs_clarification = [label for field, label in REQUEST_FIELDS.items() if not valid[field]]
    if needs_clarification:
        return "Vui lòng bổ sung: " + ", ".join(needs_clarification) + "."
    order = request.get("activity_order", [])
    if not isinstance(order, list) or any(not isinstance(name, str) for name in order):
        return "Thứ tự hoạt động phải là danh sách chuỗi."
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
        begin = max(earliest, parse_time(activity["open"]))
        if activity.get("fixed_start"):
            begin = parse_time(activity["fixed_start"])
            if begin < earliest:
                continue
        finish = begin + timedelta(minutes=activity["duration"])
        if finish > min(end, parse_time(activity["close"])) or total + activity["price"] > budget:
            continue
        lines.append("{}–{}: {} ({:,} đồng/người; {})".format(begin.strftime("%H:%M"), finish.strftime("%H:%M"), activity["name"], activity["price"], ", ".join(activity["tags"])))
        total += activity["price"]
        cursor = finish
    if not lines:
        return "Chưa xếp được hoạt động; hãy nới thời gian, ngân sách hoặc giới hạn."
    return "Lịch gợi ý từ dữ liệu giả lập (v{}):\n".format(park["version"]) + "\n".join(lines) + "\nTổng: {:,} đồng/người; {:,} đồng/{} người, gồm vé. Di chuyển: {} phút giữa các điểm. Thời tiết do người dùng cung cấp: {}.".format(total, total * people, people, park["travel_minutes"], weather)
