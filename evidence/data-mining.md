# Đào data — cách đếm và kết quả

> Điền ở guide bước 1.2. Ôn lại: ngày 2, ngày 6 · lab ngày 2, lab ngày 6.
> Không đào data thì xoá file này. Script / công thức đếm để trong repo (vd `evidence/count.py` hoặc ghi công thức Sheets ngay dưới), người khác chạy lại phải ra cùng số.
> Repo chỉ chứa số đã tổng hợp và vài dòng ví dụ — không chép lại nguyên file data.

## Bằng chứng ban đầu CP2

Chạy `evidence/count.py` trên `DisneylandReviews.csv` (42.656 review TripAdvisor tại ba chi nhánh Disneyland). Đếm mỗi review một lần trong nhóm `schedule_show_hours` nếu văn bản khớp từ khóa về giờ hoạt động, lỡ show hoặc trò đóng cửa. Mẫu ngẫu nhiên 200 review lấy từ toàn bộ tập với seed 42. [Disneyland Reviews trên Kaggle](https://www.kaggle.com/datasets/arushchillar/disneyland-reviews) · [Script đếm](count.py)

| Tập review | Khớp nhóm từ khóa | Tỷ lệ |
|---|---|---|
| Toàn bộ | 1.223/42.656 | 2,9% |
| Mẫu seed 42 | 9/200 | 4,5% |

> “Quite a few of the other attractions in Fantasyland were shut down during our visit.” — Review ID `317045022`

Tỷ lệ mô tả số review khớp từ khóa. Một số review chỉ nhắc giờ mở cửa hoặc show. Cần kiểm chứng khó khăn với trưởng nhóm bạn trẻ tại Việt Nam.

## 1. Cách đếm — viết TRƯỚC khi chạy

- Data dùng: __ (file nào, từ ngày nào đến ngày nào)
- Đếm gì: __ · trên tập nào: __ · lọc gì: __
- **Mẫu số là gì:** __ *(lỗi hay gặp nhất là mẫu số sai)*
- Script / công thức: __

## 2. Đọc trước, đếm sau

Đã đọc __ dòng đầu và từ điển cột. Các *kiểu* hành vi thấy được (trước khi định nghĩa thứ cần đếm):
- __
- __

## 3. Kết quả

| Đếm gì | x / N | % | Ghi chú |
|---|---|---|---|
| | | | |
| | | | |

Ghi dạng "x/N (y%)". "Nhiều bạn…" không phải số.

## 4. ≥5 ví dụ cụ thể (mã dòng / mã đã ẩn danh, không đoán ai là ai)

1.
2.
3.
4.
5.

## 5. Giới hạn của data

Data cho biết người ta **làm gì**, không cho biết **vì sao**. Thiếu gì, lệch về phía nào: __
→ Kiểm lại bằng phỏng vấn / khảo sát nào: __
