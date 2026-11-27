# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, hoàn thiện nguồn đạt ngưỡng trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1.
> Ba nguồn ngang nhau — tối thiểu **≥1 nguồn đạt ngưỡng**. Hiện nhóm đã đạt ngưỡng nguồn **Đào data**; nguồn kiểm chứng chéo (phỏng vấn / khảo sát bạn trẻ Việt Nam) sẽ bổ sung thêm khi thu đủ phản hồi.

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☑ | `evidence/data-mining.md` · `evidence/count.py` |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | ☐ *(chưa hoàn tất tại CP3)* | `evidence/interviews/` |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | ☐ *(chưa triển khai tại CP3)* | `evidence/survey/` |

## 2. Số chính

- **Đào data (`DisneylandReviews.csv` — Kaggle/TripAdvisor, `evidence/count.py`, `seed = 42`):**
  - Toàn bộ tập (mọi mức sao): **11.302/42.656 (26,5%)** review nhắc đến ≥1 nhóm pain liên quan đến lập lịch 1 ngày tại khu vui chơi — gồm:
    - `planning_navigation` (phải tự lên kế hoạch / rối thông tin / Fast Pass / bản đồ): **5.685/42.656 (13,3%)**
    - `queue_crowd` (xếp hàng quá lâu / quá đông không chơi kịp): **4.928/42.656 (11,6%)**
    - `cost_budget` (chi phí vượt kỳ vọng / không xứng ngân sách): **1.749/42.656 (4,1%)**
    - `schedule_show_hours` (không đủ giờ / lỡ show / trò đóng bảo trì): **1.223/42.656 (2,9%)**
    - `weather_restrictions` (thời tiết mưa/nắng nóng / giới hạn chiều cao): **295/42.656 (0,7%)**
  - Tập review 1–3★ (nghiêng về phàn nàn): **3.335/8.735 (38,2%)** khớp ≥1 nhóm pain.
  - Mẫu ngẫu nhiên `seed = 42` (mọi mức sao): **52/200 (26,0%)** khớp ≥1 nhóm pain (khớp sát toàn tập 26,5%).
- **Phỏng vấn:** Chưa có dữ liệu tại thời điểm CP3 (`0/3` người hoàn tất).
- **Khảo sát:** Chưa triển khai tại thời điểm CP3 (`n = 0`).

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

1. *"they should better change their name to long queue land. everywhere its long queue ,some even goes to 120.min of waiting time."* — `DisneylandReviews.csv`, `Review_ID 622355993` (1★ · Disneyland_Paris · 2018-10 · `queue_crowd`)
2. *"The lines are ridiculous, the Fast Pass process at CarsLand is useless, and when we did the Fast Pass for the Tower, we still were in line to wait for 45 minutes so we just left. I can't believe people spend so much time at this park and wait in the lines."* — `DisneylandReviews.csv`, `Review_ID 162747517` (2★ · Disneyland_California · 2013-5 · `planning_navigation`)
3. *"This was are 3rd visit not good so much is closed this puts pressure on the other rides,all this at peak season,waiting times for most rides 45 60'we tried differant times of day early start or syayed late they really need to plan better and invest in more big rides..."* — `DisneylandReviews.csv`, `Review_ID 407358325` (2★ · Disneyland_Paris · 2016-8 · `planning_navigation, cost_budget`)
4. *"It was very hot and humid when we were there and it was just too hot standing in the sun in long, crowded lines. We tried to watch the fireworks one night and people crowded themselves in very early to the front of the park."* — `DisneylandReviews.csv`, `Review_ID 320181041` (2★ · Disneyland_California · 2015-10 · `weather_restrictions`)
5. *"Quite a few of the other attractions in Fantasyland were shut down during our visit."* — `DisneylandReviews.csv`, `Review_ID 317045022` (Disneyland · `schedule_show_hours`)
6. *"We visited in late March when there seemed to quite a bit of refurbishment going on... there were a few rides out including the main roller coaster. We were four friends around 24 25 years old and while we went to Disney for a bit of nostalgia, we did kind of crave a bit more of the thrill seeking part."* — `DisneylandReviews.csv`, `Review_ID 264996033` (3★ · Disneyland_HongKong · 2015-3 · nhóm 4 bạn trẻ gặp trò bảo trì)
7. *"With kids yes but it is overpriced and a little boring to be honest."* — `DisneylandReviews.csv`, `Review_ID 637971019` (3★ · Disneyland_HongKong · 2018-1 · `cost_budget`)

## 4. Các nguồn có khớp nhau không

- Hiện tại CP3 nhóm **mới hoàn tất 1 nguồn đạt ngưỡng (Đào data)**, chưa có nguồn thứ 2 (phỏng vấn / khảo sát tại Việt Nam) để kiểm chứng chéo.
- Trong nội bộ tập đào data, mẫu ngẫu nhiên `seed = 42` (**26,0%**, `52/200`) khớp rất sát với toàn bộ tập (**26,5%**, `11.302/42.656`), và tỉ lệ pain tăng rõ rệt từ 26,5% lên **38,2%** (`3.335/8.735`) khi lọc nhóm đánh giá thấp 1–3★.

## 5. Kết luận

- Giả thuyết ở `evidence/hypothesis.md`: **đúng một phần (đạt ngưỡng dữ liệu công khai, cần kiểm chứng thêm tại Việt Nam)** — vì **26,5%** toàn bộ 42.656 review (vượt ngưỡng giả thuyết ≥20%) và **38,2%** review 1–3★ ghi nhận trực tiếp các pain về lập kế hoạch (`13,3%`), xếp hàng/không chơi kịp (`11,6%`), chi phí (`4,1%`), giờ show/trò đóng bảo trì (`2,9%`) và thời tiết/giới hạn (`0,7%`).
- **Điều vẫn chưa biết:** (1) Thời gian cụ thể (tính bằng phút) mà trưởng nhóm bạn trẻ Việt Nam mất để tự lập lịch trước chuyến đi; (2) Mức độ sẵn sàng dùng công cụ gợi ý lịch trình thực tế tại các khu vui chơi trong nước (VinWonders, Sun World…). Các thông số này hiện được đánh dấu rõ *(tự ước tính)* trong `spec.md` §2 và `cost/personas.yaml` cho đến khi có nguồn phỏng vấn/khảo sát bổ sung.
