# Đào data — cách đếm và kết quả

> Điền ở guide bước 1.2. Ôn lại: ngày 2, ngày 6 · lab ngày 2, lab ngày 6.
> Script đếm nằm ngay trong repo ([evidence/count.py](count.py)), chạy lại trên `DisneylandReviews.csv` cho ra đúng cùng bộ số liệu. Repo không commit file dữ liệu gốc (32 MB, đã ignore trong `.gitignore`).

## Bằng chứng ban đầu CP2

Chạy `evidence/count.py` trên `DisneylandReviews.csv` (42.656 review TripAdvisor tại ba chi nhánh Disneyland). Đếm mỗi review một lần trong nhóm `schedule_show_hours` nếu văn bản khớp từ khóa về giờ hoạt động, lỡ show hoặc trò đóng cửa. Mẫu ngẫu nhiên 200 review lấy từ toàn bộ tập với seed 42. [Disneyland Reviews trên Kaggle](https://www.kaggle.com/datasets/arushchillar/disneyland-reviews) · [Script đếm](count.py)

| Tập review | Khớp nhóm từ khóa `schedule_show_hours` | Tỷ lệ |
|---|---|---|
| Toàn bộ | 1.223/42.656 | 2,9% |
| Mẫu seed 42 | 9/200 | 4,5% |

> “Quite a few of the other attractions in Fantasyland were shut down during our visit.” — Review ID `317045022`

---

## 1. Cách đếm — viết TRƯỚC khi chạy

- **Data dùng:** `DisneylandReviews.csv` từ [Kaggle — Disneyland Reviews (TripAdvisor)](https://www.kaggle.com/datasets/arushchillar/disneyland-reviews) (xem ngày 27/11/2026). Tổng **42.656** review, khoảng thời gian `Year_Month`: `2010-10` → `2019-5`, gồm 3 chi nhánh: `Disneyland_California` (19.406), `Disneyland_Paris` (13.630), `Disneyland_HongKong` (9.620). Phân bố sao: 1★ = 1.499 · 2★ = 2.127 · 3★ = 5.109 · 4★ = 10.775 · 5★ = 23.146.
- **Đếm gì:** Đếm số review khớp ít nhất 1 cụm từ khóa regex (không phân biệt hoa thường) thuộc 5 nhóm pain gắn với lập lịch 1 ngày tại khu vui chơi:
  1. `queue_crowd`: xếp hàng quá lâu / quá đông không chơi kịp.
  2. `planning_navigation`: phải tự lập kế hoạch kỹ / rối thông tin / Fast Pass / app hoặc bản đồ khó dùng.
  3. `cost_budget`: chi phí quá đắt / không xứng đáng ngân sách.
  4. `schedule_show_hours`: không đủ thời gian / lỡ show / trò chơi đóng bảo trì / giờ mở–đóng cửa.
  5. `weather_restrictions`: ảnh hưởng thời tiết (mưa/nắng nóng) hoặc giới hạn chiều cao trẻ nhỏ.
- **Trên tập nào & lọc gì:**
  - Chạy trên **toàn bộ 42.656 review** (mọi mức sao) để tránh thiên lệch chỉ nhìn đánh giá thấp.
  - Chạy lát cắt **tập review 1–3★** (`N = 8.735`) để quan sát riêng nhóm khách có trải nghiệm chưa trọn vẹn *(ghi rõ tập này nghiêng về phàn nàn)*.
  - Rút **mẫu ngẫu nhiên 200 review** từ toàn bộ tập với **`seed = 42`** để đọc đối chiếu thủ công (`evidence/raw-sample-200.csv`, đã ẩn trong `.gitignore`).
- **Mẫu số là gì:** Tổng số dòng review trong từng tập (`N = 42.656` cho toàn bộ, `N = 8.735` cho tập 1–3★, `N = 200` cho mẫu `seed = 42`), **bao gồm cả review không nhắc pain**. Một review có thể khớp nhiều nhóm pain nên tổng các hàng lẻ lớn hơn số review khớp ≥1 nhóm.
- **Script / lệnh tái lập:**
  ```powershell
  python evidence/count.py --input "<duong-dan>/DisneylandReviews.csv" --sample-size 200 --seed 42
  ```

## 2. Đọc trước, đếm sau

Đã mở và đọc 35 dòng đầu trong mẫu ngẫu nhiên `evidence/raw-sample-200.csv` (và từ điển 6 cột: `Review_ID, Rating, Year_Month, Reviewer_Location, Review_Text, Branch`). Các *kiểu* hành vi lặp lại quan sát được trước khi chốt tổng hợp:
- Khách (kể cả nhóm bạn trẻ 4 người ~24–25 tuổi như `Review_ID 264996033`) gặp trò chính đóng bảo trì bất ngờ làm hụt trải nghiệm so với giá vé bỏ ra.
- Nhiều khách đi 1 ngày cho biết nếu không canh giờ trước (Fast Pass, giờ mở cổng, giờ diễu hành/show phải đứng chờ trước 30–45 phút như `Review_ID 4121961`) thì gần như chỉ chơi được vài trò (`Review_ID 190400309`, `201621036`).
- Khách phàn nàn chi phí ăn uống và vé phụ thu cao hơn dự tính, đặc biệt khi chờ quá lâu hoặc nhiều trò đóng cửa.
- Một số review 4–5★ vẫn khớp từ khóa (vd: khuyên người đến sau phải *"plan ahead"* hoặc *"use Fast Pass"* để tránh kẹt giờ) — chứng tỏ nhu cầu lập lịch tồn tại ở cả khách hài lòng, không chỉ khách chấm 1–2★.

## 3. Kết quả

| Nhóm pain | Mô tả | Toàn bộ (`N = 42.656`) | Tập 1–3★ (`N = 8.735`) | Mẫu `seed = 42` (`N = 200`) | Ghi chú |
|---|---|---|---|---|---|
| **Ít nhất 1 pain từ khóa** | Tổng review khớp ≥1 nhóm | **11.302/42.656 (26,5%)** | **3.335/8.735 (38,2%)** | **52/200 (26,0%)** | Tỉ lệ mẫu `seed=42` bám sát toàn bộ tập |
| `planning_navigation` | Lập kế hoạch / rối thông tin / Fast Pass / bản đồ | 5.685/42.656 (13,3%) | 1.244/8.735 (14,2%) | 32/200 (16,0%) | Nhóm xuất hiện nhiều nhất toàn tập |
| `queue_crowd` | Xếp hàng quá lâu / quá đông không chơi kịp | 4.928/42.656 (11,6%) | 1.581/8.735 (18,1%) | 19/200 (9,5%) | Tăng mạnh ở nhóm 1–3★ |
| `cost_budget` | Chi phí quá đắt / không xứng đáng ngân sách | 1.749/42.656 (4,1%) | 1.012/8.735 (11,6%) | 6/200 (3,0%) | Tăng gần 3× ở nhóm 1–3★ |
| `schedule_show_hours` | Không đủ giờ / lỡ show / trò đóng bảo trì | 1.223/42.656 (2,9%) | 415/8.735 (4,8%) | 9/200 (4,5%) | Trực tiếp gắn với ràng buộc giờ/bảo trì |
| `weather_restrictions` | Thời tiết (mưa/nắng nóng) / giới hạn chiều cao | 295/42.656 (0,7%) | 61/8.735 (0,7%) | 2/200 (1,0%) | Tần suất thấp hơn nhưng sai rất đắt |

## 4. ≥5 ví dụ cụ thể (trích tối đa 2 câu/review, đã bỏ tên)

1. `Review_ID 622355993` (1★ · `Disneyland_Paris` · `2018-10` · `queue_crowd`): *"they should better change their name to long queue land. everywhere its long queue ,some even goes to 120.min of waiting time."*
2. `Review_ID 162747517` (2★ · `Disneyland_California` · `2013-5` · `planning_navigation`): *"The lines are ridiculous, the Fast Pass process at CarsLand is useless, and when we did the Fast Pass for the Tower, we still were in line to wait for 45 minutes so we just left. I can't believe people spend so much time at this park and wait in the lines."*
3. `Review_ID 407358325` (2★ · `Disneyland_Paris` · `2016-8` · `planning_navigation, cost_budget`): *"This was are 3rd visit not good so much is closed this puts pressure on the other rides,all this at peak season,waiting times for most rides 45 60'we tried differant times of day early start or syayed late they really need to plan better and invest in more big rides..."*
4. `Review_ID 320181041` (2★ · `Disneyland_California` · `2015-10` · `weather_restrictions`): *"It was very hot and humid when we were there and it was just too hot standing in the sun in long, crowded lines. We tried to watch the fireworks one night and people crowded themselves in very early to the front of the park."*
5. `Review_ID 317045022` (`Disneyland` · `schedule_show_hours`): *"Quite a few of the other attractions in Fantasyland were shut down during our visit."*
6. `Review_ID 264996033` (3★ · `Disneyland_HongKong` · `2015-3` · nhóm 4 bạn trẻ 24–25 tuổi, trò đóng bảo trì): *"We visited in late March when there seemed to quite a bit of refurbishment going on... there were a few rides out including the main roller coaster. We were four friends around 24 25 years old and while we went to Disney for a bit of nostalgia, we did kind of crave a bit more of the thrill seeking part."*
7. `Review_ID 637971019` (3★ · `Disneyland_HongKong` · `2018-1` · `cost_budget`): *"With kids yes but it is overpriced and a little boring to be honest."*

## 5. Giới hạn của data

- **Khác biệt địa lý & thời gian:** Dữ liệu là review tiếng Anh tại 3 chi nhánh Disneyland nước ngoài giai đoạn `2010-10` → `2019-5`, không phản ánh trực tiếp bảng giá và cách vận hành hiện tại của các khu vui chơi tại Việt Nam (như VinWonders, Sun World).
- **Thiên lệch chọn mẫu & từ khóa:** Người có trải nghiệm bức xúc có xu hướng viết review nhiều hơn; mặt khác, đếm regex có thể bắt cả review 4–5★ nhắc mẹo *plan ahead* hoặc bỏ sót các phàn nàn viết cách khác (ví dụ `Review_ID 264996033` nhắc *refurbishment* và *rides out* không khớp đúng regex cứng).
- **Chưa cho biết "vì sao" và thời gian chuẩn bị:** Review công khai cho biết khách gặp sự cố gì tại công viên nhưng không đo được trưởng nhóm mất bao nhiêu phút lập kế hoạch trước chuyến đi.
- **Hướng kiểm chứng lại:** Cần bổ sung nguồn thứ 2 (phỏng vấn ≥3 bạn trẻ/sinh viên ngoài nhóm hoặc khảo sát ≥20 người tại Việt Nam) để xác nhận thời gian lập lịch thực tế, tần suất đi khu vui chơi và kiểm chứng chéo độ khớp với bối cảnh VN trước CP4.
