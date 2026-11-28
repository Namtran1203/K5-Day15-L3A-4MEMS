# Reflection — Nguyễn Xuân Hùng

> Lớp `L3A` · Nhóm `4MEMS` · Mã học viên: `2A202603599` · Vai trò: Thành viên · Track C (Hướng C1)

1. **Vai trò + phần mình làm (trỏ tới file / commit):**
   - Phụ trách toàn bộ mảng **định nghĩa "tốt", bộ câu thử, metric, chấm điểm và báo cáo đánh giá 2 lượt** trong `eval/` và `spec.md` §5, §7.
   - **CP2:** Thiết kế 12 câu thử đầu tiên (`C01`–`C12`, 41,7% nguồn `data_that`), viết 4 metric kiểm chứng được trong `eval/metric_spec.yaml`, đối chiếu chấm độc lập 5 đầu ra mock với Hà Anh (khớp `5/5`) và phối hợp khóa chuẩn "đạt" (`≥80%` câu qua + đạt cả 4 metric).
   - **CP3:** Mở rộng `eval/benchmark.csv` từ 12 lên **20 câu** (`7 thuong · 11 kho · 2 tu_choi`, trong đó **9/20 = 45%** từ `data_that` gắn `Review_ID` từ Hà Anh — commit `2f114af`); chấm tay toàn bộ **Lượt 1** (`eval/run-1.csv`, run ID `run-1@20261128-054303`, đạt `8/20 = 40%`), phân loại 12 ca trượt thành 3 nhóm lỗi và cập nhật `eval/report.md`, `eval/README.md`, `spec.md` §5/§7/§10 (commit `763e8ca`).
   - **CP4:** Chạy và chấm tay **Lượt 2** trên cùng bộ 20 câu (`eval/run-2.csv`, run ID `run-2@20261128-095652`, đạt `9/20 = 45%`), ghi nhận trung thực cả 2 câu cải thiện (`C06`, `C18`) lẫn 1 câu tụt (`C08`), hoàn thiện `eval/report.md` & `eval/README.md` và bàn giao tỉ lệ 45% cho Hà Anh mô phỏng chi phí (commit `8acba9a`, PR #9).

2. **AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):**
   - **Công cụ & việc hỗ trợ:** Dùng trợ lý AI để rà độ phủ lưới đầu vào theo 4 lớp chỗ khó, gợi ý cách diễn đạt bảng báo cáo trong `eval/report.md` và `eval/README.md`, và kiểm tra cú pháp CSV/YAML trước khi chạy `python run.py check`.
   - **Chỗ tự kiểm và sửa lại:** Mình không dùng LLM để chấm tự động cột `pass` mà trực tiếp đọc từng đầu ra và trace (`traces/run-1.jsonl`, `traces/run-2.jsonl`) để chấm tay theo đúng `pass_criterion` đã khóa từ CP2. Khi viết thêm 8 câu thử (`C13`–`C20`), mình sửa lại các tiêu chí chung chung AI gợi ý thành điều kiện kiểm chứng được bằng số (giờ show `14:00–14:30`, khoảng cách di chuyển `≥15 phút`, tổng tiền `≤320.000đ/người`) và giữ nguyên không sửa `expected` dù Lượt 1 và Lượt 2 có tỉ lệ đạt thấp.

3. **Một câu thử trượt của nhóm và mình học được gì từ nó:**
   - **Câu thử trượt tiêu biểu: `C07`** (*"Nhóm 4 bạn đi chơi chỉ có 3 tiếng từ 14h00 đến 17h00, ngân sách 250.000đ/người, nhưng bắt buộc phải đi đủ 7 trò lớn, 2 show và ăn tối trong khu"*).
   - Ở cả Lượt 1 và Lượt 2, hệ thống vẫn trả về một lịch gồm 1 hoạt động (`14:00–14:30: Show Sắc Màu`, tổng `240.000đ/người`) — về mặt kỹ thuật không chồng giờ và không vượt 250k, nhưng hoàn toàn **không báo cho người dùng biết yêu cầu gốc là bất khả thi** và không gợi ý nới khung giờ hay ngân sách, nên bị chấm trượt theo `pass_criterion`.
   - **Bài học rút ra:** Một đầu ra thỏa điều kiện toán học ở hàm kiểm lịch chưa chắc đã là câu trả lời tốt cho người dùng. Nhờ viết `pass_criterion` cụ thể và chốt chuẩn "đạt" sớm từ CP2 (trước khi nhìn output thật), nhóm tránh được bẫy chấm nới tay và nhìn ra rõ khoảng cách giữa "code chạy không lỗi" với "sản phẩm giải quyết đúng kỳ vọng người dùng".
