# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Coding AI (Codex / ChatGPT) | Gợi ý khung `codebase/agent.py`, `codebase/tools.py` (`make_schedule`), kết nối HTTP OpenRouter trong `codebase/ai.py` | Kiểm lại logic cộng 15 phút di chuyển, giờ show cố định `fixed_start`, bẫy lỗi JSON và chạy thật `python run.py` + `eval --try` có token > 0 | Bùi Hữu Phúc |
| Prompt / thiết kế lời gọi mô hình | ChatGPT / Codex | Soạn nháp `SYSTEM` prompt trả JSON có `null` khi thiếu dữ liệu và biểu thức regex cho `supported_request()` ở cải tiến Lượt 2 | Đối chiếu kết quả trên ca `C06`, `C18` và kiểm chạy thật qua OpenRouter (`upstage/solar-mini-4-5`) | Trần Thành Nam · Bùi Hữu Phúc |
| Đào data (viết script đếm, gợi ý nhãn) | Antigravity / Gemini | Gợi ý nhóm từ khóa regex trong `evidence/count.py`, chuẩn hóa bảng tóm tắt `evidence/data-mining.md` & `evidence/summary.md`, tra cứu số liệu khách TEA/AECOM 2024 | Chạy lại trực tiếp `python evidence/count.py --seed 42` trên 42.656 dòng `DisneylandReviews.csv`, đọc kiểm tay 35 dòng mẫu đầu trong `raw-sample-200.csv`, tự tách rõ nguồn công khai và số *(tự ước tính)* | Nguyễn Hà Anh |
| Rà câu hỏi phỏng vấn / khảo sát | Không sử dụng *(chưa triển khai phỏng vấn/khảo sát tại CP4)* | — | — | Nguyễn Hà Anh |
| Viết câu thử (benchmark) | Coding AI | Rà độ phủ lưới đầu vào 4 lớp chỗ khó, chuẩn hóa định dạng `eval/benchmark.csv`, `eval/report.md`, `eval/README.md` | Tự thiết kế `pass_criterion` đo được bằng số, gắn nguồn `data_that` cho 9/20 câu (`Review_ID` thật), không sửa `expected` sau khi chạy | Nguyễn Xuân Hùng |
| Sinh data `synthetic` (`data/park.json`) | Coding AI | Tạo bộ dữ liệu khu vui chơi giả lập Công viên Sắc Màu v2.0 (5 hoạt động, 2 show cố định) | Không dùng script random nên không có seed (đã ghi rõ trong `data/DATA_CARD.md`); kiểm khớp giá vé, giờ mở cửa và điều kiện indoor/intense với `codebase/tools.py` | Bùi Hữu Phúc |
| Chấm cột `pass` bằng LLM | Không sử dụng *(chấm tay 100%)* | — | Hùng đọc trực tiếp từng output & trace (`run-1.jsonl`, `run-2.jsonl`) để chấm tay 20/20 câu cả 2 lượt; đối chiếu độc lập 5 đầu ra mock với Hà Anh khớp 5/5 | Nguyễn Xuân Hùng · Nguyễn Hà Anh |
| Spec, phân công và sơ đồ XML CP2 | ChatGPT | Soạn §3, §4, §6, §9, cập nhật §10, đề xuất ngưỡng §7 và tạo sơ đồ draw.io | Nam đối chiếu nguồn tham khảo, thu hẹp phạm vi còn 1 khu vui chơi 1 ngày, kiểm khớp sơ đồ với code và quay video demo thật | Trần Thành Nam |
| Canvas, mô phỏng chi phí, slide & kịch bản | Antigravity / Gemini | Soạn nháp `canvas.md`, cấu hình `cost/personas.yaml`, chuẩn hóa `cost/cost-estimate.md`, dựng HTML xuất `demo-slides.pdf` 4 trang và rút gọn kịch bản thuyết trình | Tự đổi vai người dùng sang nhóm bạn trẻ/sinh viên ở CP1; chạy thật `python run.py simulate --rate-from eval/run-2.csv` (50/50 phiên, `0` lỗi); mở kiểm trực tiếp 4 trang PDF và chỉnh lại chiều cao sơ đồ Trang 2 | Nguyễn Hà Anh |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
