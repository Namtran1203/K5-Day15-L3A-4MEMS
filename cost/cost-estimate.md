# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Toàn bộ con số trong bảng kết quả lấy trực tiếp từ `cost/simulate-1-summary.md` (sinh bởi `python run.py simulate --rate-from eval/run-2.csv`), tính theo **giá gói trả phí** cho bối cảnh vận hành thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml` — tổng `share = 1.0`, `seed = 42`, các giả định tần suất *(tự ước tính)* khớp `spec.md` §2):
  - `dung_it`: tỉ lệ `50%` · `1` phiên/tháng · `1` lượt hỏi/phiên (`types: [thuong]`) — lập lịch 1 lần trước khi đi.
  - `dung_vua`: tỉ lệ `35%` · `1` phiên/tháng · `3` lượt hỏi/phiên (`types: [thuong, kho]`) — chỉnh sửa 2–3 lần theo ý cả nhóm.
  - `dung_nhieu`: tỉ lệ `15%` · `1` phiên/tháng · `5` lượt hỏi/phiên (`types: [kho]`) — gặp mưa / trò đóng cửa phải xếp lại nhiều lần trong ngày.
- **Số người dùng thật** (đơn vị: trưởng nhóm dùng công cụ/tháng tại 1 khu vui chơi cỡ lớn — 3 kịch bản):
  - Thấp: **3.000** · Cơ sở: **10.000** · Cao: **30.000** trưởng nhóm/tháng.
  - Nguồn: Quy đổi từ ~7,9 triệu lượt khách/năm (~658.000 lượt/tháng) của Hong Kong Disneyland theo báo cáo **TEA/AECOM 2024** (xem 27/11/2026) ÷ 4 người/nhóm (~164.500 nhóm/tháng) × tỉ lệ pain 26,5% (`evidence/data-mining.md`); tỉ lệ adoption 3 kịch bản (`3.000 / 10.000 / 30.000`): *(tự ước tính)*.
- **Giá ≥2 mức model** (từ bảng giá chung K5 `further-reading/model-prices.md`, kiểm 25/11/2026 — USD / 1 triệu token):
  - `gpt-4o-mini` (tầng Nhỏ): vào `$0.15` · ra `$0.60` — https://developers.openai.com/api/docs/pricing (xem 25/11/2026).
  - `gemini-3.1-flash-lite` (tầng Nhỏ): vào `$0.25` · ra `$1.50` — https://ai.google.dev/gemini-api/docs/pricing (xem 25/11/2026).
  - `gemini-4-hydrogen` (tầng Lớn): vào `$1.50` · ra `$7.50` — https://ai.google.dev/gemini-api/docs/pricing (xem 25/11/2026).
- **Tỷ giá quy đổi tham khảo:** `1 USD = 25.400 ₫` *(xem 27/11/2026, tự ước tính làm tròn)*.
- **Tỉ lệ đạt dùng để tính:** **9/20 (45%)** — lượt `run-2@20261128-095652` (`eval/run-2.csv`, Lượt 2).
- **Lưu ý đo token:** Đo token thật trên model **`upstage/solar-mini-4-5`** (qua OpenRouter, 0/50 phiên lỗi), tính giá trên 3 model **`gpt-4o-mini`**, **`gemini-3.1-flash-lite`** và **`gemini-4-hydrogen`** *(mỗi hãng dùng bộ tách token khác nhau nên số token thực tế khi đổi hãng có thể chênh nhẹ)*.

## 2. Kết quả mô phỏng

- Lượt mô phỏng: `cost/simulate-1.csv` · tóm tắt `cost/simulate-1-summary.md` · trace `traces/simulate-1.jsonl` · **run ID `simulate-1@20261128-102148`** · **50 phiên** (`0/50` phiên lỗi) · `seed = 42`.

**Thống kê token đo thật theo persona (50 phiên):**

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| `dung_it` | 26 | 1 | 860 | 96 | 1.0 | 2.0 |
| `dung_vua` | 17 | 3 | 2.569 | 307 | 3.0 | 6.0 |
| `dung_nhieu` | 7 | 5 | 4.252 | 505 | 5.0 | 10.0 |

**Bảng chi phí 3 kịch bản (dán nguyên số từ `cost/simulate-1-summary.md`):**

| Model (giá $/1M token) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | / tháng — thấp (3.000 người) | / tháng — cơ sở (10.000 người) | / tháng — cao (30.000 người) | / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| `gpt-4o-mini` (vào 0.15 · ra 0.60) | $0.00042 (≈ 11 ₫) | **$0.00094 (≈ 24 ₫)** | $0.00042 (≈ 11 ₫) | $1.30 (≈ 33.060 ₫) | **$4.34 (≈ 110.200 ₫)** | $13.02 (≈ 330.599 ₫) | $0.00043 (≈ 11 ₫) |
| `gemini-3.1-flash-lite` (vào 0.25 · ra 1.50) | $0.00082 (≈ 21 ₫) | **$0.0018 (≈ 46 ₫)** | $0.00081 (≈ 21 ₫) | $2.52 (≈ 63.915 ₫) | **$8.39 (≈ 213.051 ₫)** | $25.16 (≈ 639.152 ₫) | $0.00084 (≈ 21 ₫) |
| `gemini-4-hydrogen` (vào 1.50 · ra 7.50) | $0.0046 (≈ 116 ₫) | **$0.0101 (≈ 258 ₫)** | $0.0045 (≈ 115 ₫) | $14.06 (≈ 357.045 ₫) | **$46.86 (≈ 1.190.151 ₫)** | $140.57 (≈ 3.570.454 ₫) | $0.0047 (≈ 119 ₫) |

*Công thức:* `Chi phí / task thành công = Chi phí / phiên ÷ tỉ lệ đạt (0,45)` — không coi như đạt 100%. `Chi phí / câu hỏi đạt = Chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (2,2) ÷ 0,45`.

## 3. So với impact

- **Impact / người / tháng (`spec.md` §2):** **22.500 ₫ / trưởng nhóm / tháng** (~45 phút tự tra cứu & xoay xở lịch quy đổi 30.000 ₫/giờ *(tự ước tính)*, tổng ~225 triệu ₫/tháng cho 10.000 trưởng nhóm).
- **Chi phí AI / người / tháng (kịch bản cơ sở 10.000 người):** **11 ₫** (`gpt-4o-mini`) · **21 ₫** (`gemini-3.1-flash-lite`) · **119 ₫** (`gemini-4-hydrogen`). Kể cả tính trên **task thành công** với tỉ lệ đạt Lượt 2 mới 45% (`24 ₫` – `258 ₫`), chi phí AI chỉ chiếm **0,1% – 1,1%** giá trị thời gian tiết kiệm.
- **Kết luận một dòng — đáng làm không:** **Rất đáng làm về chi phí (rẻ hơn Impact gần 100–1.000 lần), nhưng cần ITERATE để kéo tỉ lệ đạt từ 45% vượt chuẩn 80% trước khi triển khai; biên chi phí rộng cho phép nâng hẳn lên model tầng Lớn (`gemini-4-hydrogen`, chỉ $46.86/tháng ở mức 10.000 nhóm) để ưu tiên độ chính xác.**

## 4. Phân tích thêm về độ nhạy & chi phí ngoài model

- **Độ nhạy theo tỉ lệ đạt (pass rate):** Nếu sau khi cải tiến tỉ lệ đạt tăng từ `45%` lên chuẩn `80%`, **chi phí / task thành công giảm gần một nửa** (từ `$0.00094 → ~$0.00053` với `gpt-4o-mini`, và từ `$0.0101 → ~$0.0058` với `gemini-4-hydrogen`).
- **Độ nhạy theo ngữ cảnh & cache:** Mỗi lượt hiện tiêu trung bình `~855` token vào (`SYSTEM` prompt + JSON `park.json`). Khi mở rộng `park.json` lên 30–50 trò chơi, cần bật prompt caching cho phần dữ liệu khu vui chơi tĩnh hoặc lọc trò theo sở thích bằng Python trước khi gửi vào model để giữ `tokens_in` ổn định.
- **Chi phí ngoài model:** Hosting backend/web nhẹ (~$10–$30/tháng) + công cập nhật bảng giá/giờ mở cửa khu vui chơi định kỳ (vì công cụ hoàn toàn chỉ đọc, không cần nhân sự duyệt từng giao dịch).
