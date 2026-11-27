# Data card — khu vui chơi giả lập

| Mục | Nội dung |
|---|---|
| Dataset | `park.json`, phiên bản 2.0; cập nhật theo canvas Track C1. |
| Mục đích | Thử lập lịch cho nhóm bạn trẻ một ngày, không đặt vé. |
| Nguồn | Dữ liệu synthetic do AI tạo cho bản thử, không phản ánh địa điểm thực tế; không dùng seed. |
| Quy mô | Một khu, 5 hoạt động gồm 2 sự kiện giờ cố định, giá và thời gian di chuyển giả định. |
| Kiểm tra | Chưa được thành viên nhóm xác nhận; số bản ghi đã kiểm tra thủ công: 0. |
| Giới hạn | Không có thời tiết thực tế, thông tin chiều cao hay thời gian chờ; không phải bằng chứng nhu cầu và không dùng để lên kế hoạch thực tế. |

Mọi giá là đồng/người; thời gian di chuyển giữa các điểm là 15 phút. Thời tiết do người dùng cung cấp, không phải dự báo. Hoạt động mạnh được xem là không phù hợp khi nhóm khai có giới hạn cảm giác mạnh; lịch dành cho cả nhóm, không tách nhóm.

Ví dụ đầu vào JSON một dòng ở chế độ giả: `{"people":4,"budget_per_person":600000,"start":"09:00","end":"18:00","interests":["show"],"avoid_intense":false,"weather":"khô"}`. Mưa dùng `"weather":"mưa"`; khi chưa biết ghi `"weather":"không rõ"`, hệ thống chỉ chọn điểm trong nhà. Model thật cần cấu hình theo `docs/connect-model.md`.
