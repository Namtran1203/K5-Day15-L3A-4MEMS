# Data card — khu vui chơi giả lập

| Mục | Nội dung |
|---|---|
| Dataset | `park.json`, phiên bản 1.1, tạo ngày 27/11/2026; bổ sung nhãn sở thích. |
| Mục đích | Dữ liệu cho bản thử xếp lịch một ngày của gia đình. |
| Nguồn và cách tạo | Dữ liệu synthetic do AI tạo thủ công, không lấy từ khu vui chơi có thật; không sử dụng seed. |
| Quy mô | 3 hoạt động, 1 bảng giá vé và thời gian di chuyển giả định. |
| Xử lý | Viết trực tiếp dữ liệu có cấu trúc; không thu thập dữ liệu cá nhân. |
| Kiểm tra | Chưa có người trong nhóm xác nhận; số bản ghi được thành viên kiểm tra thủ công: 0. |
| Giới hạn | Giờ, giá, tuổi và thời gian di chuyển đều giả định; không dùng để lập lịch thực tế hay làm bằng chứng về nhu cầu người dùng. |

Giá tính bằng đồng Việt Nam, giá hoạt động tính cho mỗi người; thời gian di chuyển tính giữa các hoạt động.

Chế độ giả nhận JSON một dòng, ví dụ `{"adults":2,"children_ages":[5],"start":"09:00","end":"16:00","budget":500000,"interests":["động vật"]}`. Để nhận câu tự nhiên và đề xuất thứ tự bằng AI, cấu hình `MODEL_PROVIDER=openai`, `MODEL_NAME` và `API_KEY` trong `.env`; xem hướng dẫn trong `docs/connect-model.md`. Không đưa khoá vào repo. Chế độ giả chọn theo nhãn sở thích, không gọi AI và không dùng làm kết quả đánh giá model thật.
