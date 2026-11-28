# Reflection — Nguyễn Hà Anh

> Lớp `L3A` · Nhóm `4MEMS` · Mã học viên: `2A202603605` · Track C (Hướng C1 — Lập lịch 1 ngày tại khu vui chơi)

1. **Vai trò + phần mình làm (trỏ tới file / commit):**
   - Phụ trách mảng **sản phẩm, bằng chứng người dùng, Impact, mô phỏng chi phí và slide trình bày** của nhóm `4MEMS`.
   - **CP1:** Soạn và hoàn thiện 7 dòng `canvas.md` theo vai trưởng nhóm bạn trẻ / sinh viên đi khu vui chơi 1 ngày.
   - **CP2–CP3:** Thực hiện đối chiếu chấm độc lập 5 đầu ra mock cùng Hùng (khớp `5/5`, ghi trong `eval/README.md`); chạy xác minh `evidence/count.py` (`seed = 42`) trên 42.656 review `DisneylandReviews.csv`, hoàn thiện `evidence/hypothesis.md`, `evidence/data-mining.md`, `evidence/summary.md` (7 trích dẫn có `Review_ID`), bàn giao 4 `Review_ID` mới cho Hùng mở rộng bộ 20 câu thử; cập nhật `spec.md` §1 và tính bảng Impact/tháng ở §2; cấu hình `cost/personas.yaml` và chạy thử `python run.py simulate --try` (10/10 phiên, `0` lỗi) — commit `30dba65`.
   - **CP4:** Chạy mô phỏng chi phí chính thức **50 phiên** (`python run.py simulate --rate-from eval/run-2.csv`, run ID `simulate-1@20261128-102148`, `0/50` lỗi) theo tỉ lệ đạt thật Lượt 2 (`9/20 = 45%`), hoàn thiện `cost/cost-estimate.md`, `spec.md` §8 & changelog §10 (`cost/simulate-1.csv`, `cost/simulate-1-summary.md`, `traces/simulate-1.jsonl` — commit `5d38009`); hoàn thiện `slides/outline.md`, `slides/demo-slides.html` và xuất `demo-slides.pdf` 4 trang ở thư mục gốc repo (commit `9ab32c4`).

2. **AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):**
   - **Công cụ & việc hỗ trợ:** Dùng trợ lý AI (Antigravity / Gemini) để rà soát yêu cầu từng checkpoint/rubric, soạn khung nháp `canvas.md`, chuẩn hóa bảng số liệu từ kết quả `evidence/count.py` và `cost/simulate-1-summary.md`, tra cứu số liệu lượng khách công khai (TEA/AECOM 2024 cho Hong Kong Disneyland), dựng bố cục HTML xuất `demo-slides.pdf` và rút gọn kịch bản thuyết trình.
   - **Những chỗ mình trực tiếp kiểm và sửa lại output AI:**
     - Ở CP1, AI ban đầu viết `canvas.md` theo vai *phụ huynh có con nhỏ (4–10 tuổi)*; mình chủ động chỉnh lại sang vai *trưởng nhóm bạn trẻ / sinh viên* để đúng đối tượng nhóm hướng tới và sát bối cảnh thực tế hơn.
     - Ở CP3–CP4, mình tự chạy lệnh xác minh lại toàn bộ số đếm trên `DisneylandReviews.csv` (`26,5%` toàn tập, `38,2%` tập 1–3★) và chạy thật `simulate` trên API OpenRouter (`upstage/solar-mini-4-5`), rà kỹ để tách bạch rõ số có nguồn công khai với các thừa số phải ghi *(tự ước tính)* trong `spec.md` §2 và `cost/personas.yaml`.
     - Khi xuất `demo-slides.pdf`, bản đầu bị tràn chiều cao sơ đồ ở Trang 2 làm mất chân trang và dòng cuối thẻ Demo; phải kiểm tra trực tiếp từng trang PDF và chỉnh lại tỉ lệ sơ đồ/cỡ chữ để đủ 4 trang 16:9 sạch đẹp.

3. **Một câu thử trượt của nhóm và mình học được gì từ nó:**
   - **Câu thử trượt ấn tượng nhất: `C08`** (*"Nhóm 4 người đang chơi theo lịch buổi chiều thì 14h00 trời đổ mưa to kéo dài đến 16h30, cần xếp lại lịch phần chiều trong mức 600.000đ/người"*).
   - Ở Lượt 1 (`run-1@20261128-054303`, `8/20 = 40%`), `C08` đạt nhưng nhóm có 6 ca trượt vì model tự đoán thông tin thiếu (như `C06`, `C18`). Khi nhóm cải tiến bằng cách yêu cầu model trả `null` và thêm hàm `supported_request()` ở Lượt 2 (`run-2@20261128-095652`, `9/20 = 45%`), `C06` và `C18` chuyển sang đạt nhưng **`C08` lại tụt từ đạt xuống trượt** vì model trả `people: null` và regex chưa nhận cụm *"cần xếp lại lịch"*, làm hệ thống dừng hỏi lại thay vì xếp lịch điểm trong nhà.
   - **Bài học rút ra:**
     - Thứ nhất, khi sửa prompt hoặc rule để vá một nhóm lỗi, rất dễ gây hồi quy (regression) ở các câu vốn đang chạy đúng — nên bắt buộc phải chạy lại **trọn bộ 20 câu thử** sau mỗi lần sửa thay vì chỉ kiểm tra cục bộ.
     - Thứ hai, tỷ lệ đạt gắn chặt với **bài toán chi phí**: vì Lượt 2 mới đạt `45%` (`< 80%`), `chi phí / task thành công` bị nhân lên hơn **2,2 lần** so với chi phí mỗi phiên (`$0.00042 → $0.00094` ở `gpt-4o-mini`; `$0.0046 → $0.0101` ở `gemini-4-hydrogen`). Nhờ đo lường trung thực cả chất lượng lẫn chi phí, nhóm có cơ sở định lượng rõ ràng để kết luận **ITERATE** (cải tiến và cân nhắc nâng model tầng Lớn vì chi phí vẫn chỉ `< 1,2%` Impact) thay vì vội vàng Go-Live.
