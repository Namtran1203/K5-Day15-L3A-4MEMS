"""Công cụ tra cứu và lập lịch với dữ liệu giả lập."""
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
    required = ("adults", "children_ages", "start", "end", "budget")
    missing = [key for key in required if key not in request]
    if missing:
        return "Thiếu thông tin: " + ", ".join(missing) + ". Cần số người lớn, tuổi từng trẻ, giờ và ngân sách."
    adults, ages, budget = request["adults"], request["children_ages"], request["budget"]
    if type(adults) is not int or adults < 1 or not isinstance(ages, list) or not ages or any(type(age) is not int or age < 0 or age > 17 for age in ages) or type(budget) is not int or budget < 0:
        return "Thông tin không hợp lệ: cần ít nhất một người lớn, tuổi trẻ 0–17 và ngân sách không âm."
    try:
        parse = lambda value: datetime.strptime(value, "%H:%M")
        start, end = parse(request["start"]), parse(request["end"])
    except (ValueError, TypeError):
        return "Giờ không hợp lệ; hãy nhập theo dạng HH:MM."
    if start >= end or start < parse(park["open"]) or end > parse(park["close"]):
        return "Khung giờ không hợp lệ hoặc nằm ngoài giờ mở cửa 09:00–17:00."
    total = adults * park["adult_ticket"] + len(ages) * park["child_ticket"]
    if total > budget:
        return "Ngân sách không đủ: vé vào cổng {:,} đồng, ngân sách {:,} đồng.".format(total, budget)
    interests = request.get("interests", [])
    order = request.get("activity_order", [])
    if not isinstance(interests, list) or any(not isinstance(x, str) for x in interests) or not isinstance(order, list) or any(not isinstance(x, str) for x in order):
        return "Sở thích và thứ tự hoạt động phải là danh sách chuỗi."
    names = {activity["name"] for activity in park["activities"]}
    if any(name not in names for name in order) or len(set(order)) != len(order):
        return "Đề xuất có hoạt động không tồn tại hoặc bị lặp; vui lòng thử lại."
    activities = list(park["activities"])
    if order:
        activities = [next(a for a in activities if a["name"] == name) for name in order]
    elif interests:
        activities.sort(key=lambda a: -sum(term.casefold() in (a["name"] + " " + " ".join(a.get("tags", []))).casefold() for term in interests))
    cursor, lines = start, []
    for activity in activities:
        if any(age < activity["min_age"] for age in ages):
            continue
        begin = max(cursor + (timedelta(minutes=park["travel_minutes"]) if lines else timedelta()), parse(activity["open"]))
        finish = begin + timedelta(minutes=activity["duration"])
        cost = activity["price"] * (adults + len(ages))
        if finish > min(end, parse(activity["close"])) or total + cost > budget:
            continue
        lines.append("{}–{}: {} ({:,} đồng)".format(begin.strftime("%H:%M"), finish.strftime("%H:%M"), activity["name"], cost))
        total += cost
        cursor = finish
    if not lines:
        return "Chưa xếp được hoạt động phù hợp trong khung giờ và ngân sách sau khi tính vé vào cổng."
    return "Lịch tham khảo cho khu giả lập:\n" + "\n".join(lines) + "\nTổng gồm vé vào cổng: {:,} đồng. Di chuyển giữa các điểm: {} phút.".format(total, park["travel_minutes"])
