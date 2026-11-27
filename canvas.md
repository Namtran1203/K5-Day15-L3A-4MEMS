# Canvas — 4MEMS · Track C

> Điền ở guide bước 1.4. CP1 17:00 Thứ Sáu 27/11: nộp bản đầu, đủ 7 dòng (dòng 4 được ghi giả thuyết + nguồn sẽ kiểm).
> CP2 19:30 Thứ Sáu 27/11: cập nhật (số bằng chứng đầu, lát cắt đã chốt) và điền dòng "Đã đổi gì so với CP1".
> Track F: chép thêm thẻ đề của nhóm (khung trong file track F) xuống dưới bảng này.

| # | Dòng | Nhóm điền |
|---|---|---|
| 1 | Track + lát cắt dự kiến | **Track C (Du lịch — hướng C1):** Lập và tự kiểm lịch trình 1 ngày tại khu vui chơi cho nhóm bạn trẻ theo ràng buộc ngân sách, khung giờ, sở thích/giới hạn của nhóm, giờ show và thời tiết. |
| 2 | Người dùng chính (một vai cụ thể — không phải "học viên nói chung") | Người lên kế hoạch (trưởng nhóm) của một nhóm bạn trẻ / sinh viên (3–6 người) đi khu vui chơi giải trí trọn 1 ngày (như VinWonders, Sun World, Đầm Sen, Suối Tiên, Disneyland). |
| 3 | Pain một câu: ai — đang làm gì — vướng đâu — hậu quả | Người lên lịch cho nhóm bạn trẻ đi khu vui chơi 1 ngày phải tự tra tay hàng chục điểm chơi, giờ mở cửa/giờ show, giá vé phụ thu và cân bằng sở thích khác nhau trong nhóm (vd: người thích cảm giác mạnh, người không), rồi tự xoay xở khi trời mưa hoặc trễ giờ — khiến họ tốn nhiều thời gian chuẩn bị, dễ lỡ show, di chuyển vòng vèo hoặc vượt ngân sách dự kiến. |
| 4 | Bằng chứng đầu — CP1: giả thuyết + nguồn sẽ kiểm · CP2: số đầu tiên + 1 trích dẫn | **CP2:** 1.223/42.656 review (2,9%) khớp từ khóa về giờ hoạt động, lỡ show hoặc trò đóng cửa. Trong mẫu ngẫu nhiên 200 review (seed 42), con số là 9/200 (4,5%). “Quite a few of the other attractions in Fantasyland were shut down during our visit.” — Review ID `317045022`. Đây là số đếm từ review Disneyland, cần kiểm chứng với nhóm bạn trẻ tại Việt Nam. [Nguồn và cách đếm](evidence/data-mining.md#bằng-chứng-ban-đầu-cp2) |
| 5 | **Lát cắt MỘT CÂU** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả) | Trưởng nhóm bạn trẻ nhập thông tin chuyến đi để AI đề xuất thứ tự các điểm chơi trong một ngày tại một khu vui chơi, rồi nhận lịch đã kiểm theo giờ kèm tổng chi phí hoặc lý do chưa xếp được. |
| 6 | AI tự làm đến đâu + 1 dòng lý do: sai thì ai chịu gì | **AI gợi ý lịch trình (có code tự kiểm ràng buộc), người dùng quyết định chọn/sửa.** Lý do: công cụ chỉ đọc (không tự đặt vé/trừ tiền), nhưng nếu AI báo sai giờ mở cửa/giờ show, xếp chồng giờ hoặc vượt ngân sách sinh viên thì cả nhóm mất thời gian, lỡ show và hỏng chuyến đi — nên mọi con số và ràng buộc cứng phải do code kiểm, AI chỉ đề xuất để nhóm chốt. |
| 7 | Phân công có tên | Trần Thành Nam — thiết kế, checkpoint và demo<br>Bùi Hữu Phúc — bản chạy thử và dữ liệu giả lập<br>Nguyễn Hà Anh — bằng chứng, impact và chi phí<br>Nguyễn Xuân Hùng — câu thử, metric và đánh giá |
| — | *(CP2)* Đã đổi gì so với CP1 | Thu hẹp bản thử xuống một khu vui chơi giả lập. Bản mock nhận một dòng JSON và dùng thời tiết do người dùng cung cấp. Python kiểm giờ mở cửa, giờ show, di chuyển, giới hạn trò mạnh và ngân sách. Đầu ra là lịch theo giờ kèm chi phí hoặc lý do chưa xếp được. [Thiết kế CP2](spec.md) |
