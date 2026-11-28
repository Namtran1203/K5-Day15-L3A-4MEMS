# Reflection — Bùi Hữu Phúc

> Lớp `L3A` · Nhóm `4MEMS` · Mã học viên: `2A202603573` · Vai trò: Thành viên · Track C (Hướng C1)

1. **Vai trò + phần mình làm (trỏ tới file / commit):**
   - Phụ trách **xây dựng bản chạy thử, dữ liệu khu vui chơi giả lập và kết nối model thật** trong `codebase/` và `data/`.
   - **CP2:** Thiết kế và dựng dữ liệu giả lập `data/park.json` (v2.0 — Công viên Sắc Màu, 5 hoạt động gồm 2 show cố định giờ, vé cổng 200.000đ, 15 phút di chuyển), viết `data/DATA_CARD.md`, cài đặt hai công cụ chỉ đọc `read_park()` và `make_schedule()` trong `codebase/tools.py` cùng luồng khung trong `codebase/agent.py` (commit `e0f36c7`, PR #3 & #4).
   - **CP3–CP4:** Tích hợp API OpenRouter (`upstage/solar-mini-4-5`) vào `codebase/ai.py`, cập nhật `.env.example` và hướng dẫn `docs/connect-model.md`, chạy xác nhận nối model có token thật (`eval/openrouter-try-cp3.csv`, `traces/openrouter-try-cp3.jsonl`) và chạy đánh giá Lượt 1 (`eval/run-1.csv`, `traces/run-1.jsonl` — commit `fe8ec99`, PR #8); phụ trách vận hành demo trực tiếp bằng `python run.py`.

2. **AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):**
   - **Công cụ & việc hỗ trợ:** Dùng trợ lý coding AI để gợi ý cấu trúc `park.json`, viết nháp hàm `make_schedule()` kiểm tra ràng buộc thời gian/ngân sách và đoạn gọi HTTP POST tới OpenRouter trong `codebase/ai.py` chỉ bằng thư viện chuẩn `urllib`.
   - **Chỗ tự kiểm và sửa lại:** Khi đồng bộ với canvas nhóm bạn trẻ (`e0f36c7`), mình phải chỉnh lại cấu trúc trường JSON đầu vào (từ thông tin gia đình sang nhóm bạn trẻ có `avoid_intense` và `weather`), tự kiểm lại logic cộng đúng `15` phút di chuyển giữa hai hoạt động, xử lý mốc giờ show cố định (`fixed_start`), và bẫy lỗi `json.loads()` khi model trả văn bản không đúng định dạng JSON trước khi bàn giao cho Hùng và Hà Anh chạy hàng loạt.

3. **Một câu thử trượt của nhóm và mình học được gì từ nó:**
   - **Câu thử trượt tiêu biểu: `C05` và `C16`** (người dùng yêu cầu xếp các điểm không tồn tại trong `park.json` như *Tàu Lượn Siêu Tốc X*, *Khu Trượt Băng Y*, *Khu Trượt Tuyết*, *Nhà Ma 3D*).
   - Mặc dù trong `codebase/tools.py` mình đã viết bước kiểm tra `any(x not in lookup for x in order)` để chặn mã điểm lạ, nhưng khi chạy model thật ở cả Lượt 1 và Lượt 2, model chỉ đưa các trò có sẵn trong `park.json` vào `activity_order` và **im lặng bỏ qua** các điểm người dùng yêu cầu. Kết quả là code Python thấy `order` hoàn toàn hợp lệ nên xuất lịch bình thường mà không hề báo cho người dùng biết các điểm kia không có trong dữ liệu.
   - **Bài học rút ra:** Lớp chặn nguồn sự thật không thể chỉ kiểm tra danh sách đầu ra do LLM sinh ra, vì LLM có xu hướng tự lọc bỏ thầm lặng những thứ không có trong context. Cần thêm bước đối chiếu trực tiếp các tên điểm người dùng nêu trong câu hỏi gốc (hoặc yêu cầu model xuất thêm trường `unavailable_requested`) để thông báo minh bạch khi điểm chơi không tồn tại hoặc đang bảo trì.
