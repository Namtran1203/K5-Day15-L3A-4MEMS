# Dàn slide 4 trang → lấy số từ file nào

> Làm ở guide bước 5.1 (rút gọn 4 trang theo yêu cầu demo Zone). Luật: **không có bằng chứng thì không có slide** — mỗi trang ≥1 con số / trích dẫn có nguồn / kết quả đo.
> Bản thiết kế nguồn: `slides/demo-slides.html` → xuất PDF thành **`demo-slides.pdf`** ở thư mục gốc repo, nộp tại CP4 14:30 Thứ Bảy 28/11.

| # | Trang | Có gì | Số lấy từ | Xong |
|---|---|---|---|---|
| 1 | **Pain & Impact: Vì sao chọn C1?** | Vai trưởng nhóm bạn trẻ · Pain không chữ AI · Đào data `26,5%` / `38,2%` + trích dẫn có `Review_ID` · Impact `7.500 giờ/tháng ≈ 225tr ₫/tháng` (`22.500 ₫/nhóm/tháng`) + lý do loại C2, C3 | `evidence/summary.md` · `spec.md` §2 | ☑ |
| 2 | **Giải pháp AI & Demo Live** | Lát cắt 1 câu · Sơ đồ `docs/diagram.drawio.png` · Workflow cố định + AI gợi ý, người quyết + chặn rủi ro Python + HAX G10 · Demo ca thường (320k/người), ca mưa (290k/người), ca thiếu thông tin + video dự phòng (`docs/demoVid.mp4`) | `spec.md` §4 · `eval/benchmark.csv` · `docs/demoVid.mp4` | ☑ |
| 3 | **Đánh giá thế nào?** | `park.json` v2.0 · 20 câu thử (`9/20 = 45%` `data_that`) · 4 metric · Hiệu chuẩn `5/5` · Chuẩn "đạt" CP2 (`≥80%` + 4/4 metric) · Lượt 1 `8/20 (40%)` → 1 cải tiến → Lượt 2 `9/20 (45%)` kèm run ID · Lỗi chính còn lại | `eval/README.md` · `eval/report.md` · `spec.md` §7 | ☑ |
| 4 | **Chi phí dùng thật & Kết luận** | Mô phỏng 50 phiên (`simulate-1@20261128-102148`, `0/50` lỗi, tỉ lệ Lượt 2 `45%`) · Chi phí / task thành công (`24–258 ₫`) & 3 kịch bản (`$4.34–$46.86`/tháng cơ sở) · So với Impact (`< 1,2%`) · Kết luận **ITERATE** + 3 việc nếu có thêm 1 tuần | `cost/cost-estimate.md` · `cost/simulate-1-summary.md` · `spec.md` §8 | ☑ |

**Trước khi lên:** tải repo về máy demo, chạy theo mục "Chạy trong 3 phút" của `README.md` · `.env` có trên máy demo, đã gọi thử 1 câu trong vòng 1 giờ trước giờ demo · video dự phòng mở được bằng cửa sổ ẩn danh · sẵn sàng trả lời **1 câu thử lạ** của giám khảo.

## Phân công trình bày (cả 4 thành viên đều nói ≥1 phần)

| Trang | Người nói | Thời lượng dự kiến |
|---|---|---|
| Trang 1 — Pain & Impact | **Nguyễn Hà Anh** | ~45 giây |
| Trang 2 — Giải pháp AI & Demo Live | **Trần Thành Nam** (kiến trúc) + **Bùi Hữu Phúc** (demo live) | ~90–120 giây |
| Trang 3 — Đánh giá thế nào | **Nguyễn Xuân Hùng** | ~45 giây |
| Trang 4 — Chi phí dùng thật & Kết luận | **Nguyễn Hà Anh** (chi phí) + **Trần Thành Nam** (kết luận) | ~45 giây |
