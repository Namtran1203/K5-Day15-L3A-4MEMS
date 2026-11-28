# AI SPEC — Lập lịch một ngày ở khu vui chơi · Nhóm K5-L3A-4MEMS · Phòng 209 · Zone 6

> Mốc nộp: §7 chốt chuẩn "đạt" tại **CP2 19:30 Thứ Sáu 27/11** · §0–§7 nộp **CP3 10:00 Thứ Bảy 28/11** · đủ §0–§10 **CP4 14:30 Thứ Bảy 28/11** · §10 changelog ghi tiếp đến **23:59 Thứ Bảy 28/11**.
> Đầu mỗi mục ghi bước guide (`02-guide.md` trong repo đề) chỉ cách điền. Mỗi mục ngắn, có số và nguồn; chi tiết để ở file được trỏ tới. Xoá dòng hướng dẫn trong ngoặc vuông khi điền xong.

Track C · Du lịch · Hướng C1 — Lập lịch một ngày ở một khu vui chơi.
Data BTC cấp đã dùng (nếu có — không commit nguyên file): Không có (Track C — nhóm tự đào review công khai từ *Disneyland Reviews* trên Kaggle và tự dựng dữ liệu giả lập `park.json`).

## §0. Hiện tại việc này diễn ra thế nào *(guide 1.1)*
- **Luồng hiện tại (4 bước):**
  1. Trưởng nhóm mở website/app khu vui chơi (như VinWonders, Sun World, Disneyland) hoặc xem bài review trên TikTok/Facebook để gom danh sách trò chơi, giờ mở cửa, giờ show và giá vé phụ thu.
  2. Hỏi từng thành viên trong nhóm chat (Zalo/Messenger) về ngân sách, khung giờ đi và trò muốn chơi / trò sợ cảm giác mạnh.
  3. Tự ghép lịch trình thủ công vào Ghi chú / Google Sheets, tự ước lượng thời gian đi bộ và cộng tổng tiền.
  4. Khi đến nơi gặp trời mưa, trò đóng cửa bảo trì hoặc trễ giờ show, trưởng nhóm lại phải tra bản đồ giấy/app và đổi kế hoạch tại chỗ.
- **Minh họa bước tra thông tin show.** Cẩm nang VinWonders Phú Quốc ghi địa điểm ONCE Show và hướng dẫn khách kiểm tra lại giờ biểu diễn với nhân viên. [Cẩm nang VinWonders](https://static.vinwonders.com/production/Guide-map_VWPQ_Song-ngu.pdf) · [Trang giờ và vé ONCE Show](https://vinwonders.com/vi/once-show/)

  ![Trích cẩm nang VinWonders Phú Quốc giới thiệu địa điểm ONCE Show và lưu ý kiểm lại giờ biểu diễn](docs/vinwonders-tra-cuu-show.png)

- **Công cụ / AI đang được dùng:** Website/app chính thức của khu vui chơi (xem bản đồ, giờ mở cửa), Google Maps/Sheets, nhóm chat, và một số bạn hỏi thử ChatGPT/Gemini rời rạc (nhưng model không gắn công cụ kiểm giờ show, ngân sách hay trò đang đóng). *(Mức độ dùng công cụ AI thực tế ở nhóm bạn trẻ VN: chưa kiểm — sẽ xác nhận qua phỏng vấn/khảo sát trước CP3).*

## §1. Người dùng & bằng chứng *(guide 1.1, 1.2)*
- **Người dùng chính (một vai cụ thể):** Người lên kế hoạch (trưởng nhóm) của một nhóm bạn trẻ / sinh viên (3–6 người) đi khu vui chơi giải trí trọn 1 ngày.
- **Việc họ cố làm xong:** Lập và điều chỉnh lịch trình 1 ngày tại khu vui chơi phù hợp khung giờ, ngân sách/người và sở thích khác nhau của cả nhóm.
- **Hôm nay họ giải bằng gì, hỏng ở đâu, vì sao chưa bỏ:** Dùng bài review mạng xã hội + trang thông tin khu vui chơi + ghi chú/chat nhóm. Hỏng ở chỗ thông tin giờ show, trò bảo trì, giá phụ thu rời rạc nên tự cộng dễ sai, chồng giờ và lúng túng khi trời mưa; chưa bỏ được vì không có công cụ nào gom ràng buộc của cả nhóm vào một lần xếp lịch.
- **Pain (KHÔNG chữ AI):** Trưởng nhóm bạn trẻ đi khu vui chơi 1 ngày phải tự tra tay hàng chục điểm chơi, khung giờ show, giá vé phụ thu và cân bằng sở thích khác nhau trong nhóm rồi tự xoay xở khi trời mưa hoặc trò đóng cửa, khiến họ mất nhiều thời gian chuẩn bị, dễ lỡ show, di chuyển vòng vèo hoặc vượt ngân sách dự kiến.
- **Bằng chứng pain (chi tiết: `evidence/summary.md`, `evidence/data-mining.md`):**
  - Nguồn đạt ngưỡng — đào data `DisneylandReviews.csv` (Kaggle/TripAdvisor, 42.656 review, `evidence/count.py`, `seed = 42`): **11.302/42.656 review (26,5%)** nhắc ≥1 nhóm pain liên quan đến lập lịch 1 ngày tại khu vui chơi; trong tập 1–3★ tỉ lệ tăng lên **3.335/8.735 (38,2%)**; mẫu ngẫu nhiên `seed = 42` đạt **52/200 (26,0%)**.
  - Phân rã 5 nhóm pain toàn tập: `planning_navigation` **13,3%** (`5.685/42.656`) · `queue_crowd` **11,6%** (`4.928/42.656`) · `cost_budget` **4,1%** (`1.749/42.656`) · `schedule_show_hours` **2,9%** (`1.223/42.656`) · `weather_restrictions` **0,7%** (`295/42.656`).
  - Đã trích **7 ví dụ nguyên văn** (≤2 câu/review, bỏ tên, kèm `Review_ID` như `622355993`, `162747517`, `407358325`, `320181041`, `317045022`, `264996033`, `637971019`).
  - **Kết luận CP3:** Giả thuyết đạt ngưỡng dữ liệu công khai (26,5% > 20%). Giới hạn: đây là review Disneyland nước ngoài (2010–2019), nhóm chưa hoàn tất phỏng vấn/khảo sát kiểm chứng chéo tại Việt Nam tại mốc CP3.

## §2. Impact & quyết định chọn *(guide 1.3)*

| Hướng | Bao nhiêu người gặp | Bao nhiêu lần / tháng | Mỗi lần tốn gì | Impact / tháng | Làm kịp không | Chọn? |
|---|---|---|---|---|---|---|
| **C1 · Lập lịch 1 ngày ở khu vui chơi** | ~43.590 trưởng nhóm gặp pain/tháng tại 1 khu vui chơi cỡ lớn *(quy đổi từ 7,9 triệu lượt/năm ≈ 658.000 lượt/tháng của Hong Kong Disneyland theo TEA/AECOM 2024 ÷ 4 người/nhóm × 26,5% tỉ lệ pain từ `DisneylandReviews.csv`)*; phạm vi sản phẩm cơ sở nhắm **10.000 trưởng nhóm/tháng** *(tự ước tính)* | 1 chuyến / tháng / trưởng nhóm hoạt động *(tự ước tính)* | 45 phút tự tra cứu, gom ý kiến & xoay xở lịch *(tự ước tính)* ≈ 22.500đ/chuyến (quy đổi 30.000đ/giờ) + rủi ro lỡ show/trò đóng cửa | **450.000 phút/tháng (7.500 giờ/tháng ≈ 225 triệu đ/tháng)** trên tập cơ sở 10.000 trưởng nhóm | Có (tool chỉ đọc, dễ kiểm ràng buộc cứng bằng code) | **Chọn** |
| **C2 · Lễ tân đề xuất đổi / nâng hạng phòng** | ~100–200 lễ tân tại 1 chuỗi khách sạn cỡ vừa *(tự ước tính)* | ~60 ca / tháng / lễ tân *(tự ước tính)* | 10–15 phút tra phòng trống, chính sách & tính phí chênh *(tự ước tính)* | ~1.500–3.000 giờ/tháng *(tự ước tính)* | Khó (không có sẵn lễ tân thật để phỏng vấn & dùng thử trong 2 ngày) | Loại |
| **C3 · Hỗ trợ khách bị hủy chuyến bay** | Hành khách bị hủy/đổi chuyến trong tháng *(tự ước tính)* | ~1 lần / sự cố *(tự ước tính)* | 30–90 phút xử lý + rủi ro mất lần đổi miễn phí hoặc chờ hoàn tiền tới 90 ngày (nguồn: Traveloka Help) | Cao mỗi ca sự cố nhưng phân tán theo thời điểm bão/lễ | Trung bình (hành động đổi/hoàn khó đảo; ít người xung quanh bị hủy chuyến gần đây) | Loại |

- **Impact / tháng của hướng chọn (kịch bản cơ sở tại 1 khu vui chơi cỡ lớn):**
  `10.000 trưởng nhóm/tháng × 1 chuyến/tháng × 45 phút/chuyến = 450.000 phút/tháng = 7.500 giờ/tháng` (tương đương **~225.000.000 VND/tháng**, hay **22.500 VND / trưởng nhóm / tháng** nếu quy đổi thời gian sinh viên 30.000 VND/giờ).
  - *Nguồn từng thừa số:*
    - Quy mô gốc 1 khu vui chơi cỡ lớn (~7,9 triệu lượt khách/năm ≈ 658.000 lượt/tháng): báo cáo **TEA/AECOM 2024** cho Hong Kong Disneyland (xem 27/11/2026);
    - Tỉ lệ gặp pain lập lịch/xếp hàng/show/ngân sách (**26,5%**): đào data `DisneylandReviews.csv` (`11.302/42.656`, `evidence/data-mining.md`);
    - Cỡ nhóm trung bình 4 người/nhóm, tập người dùng cơ sở 10.000 trưởng nhóm/tháng (~6% tổng số nhóm tại 1 công viên lớn), tần suất 1 chuyến/tháng, thời gian mất 45 phút/chuyến, giá trị thời gian 30.000 VND/giờ: *(tự ước tính — cần kiểm chứng lại qua phỏng vấn/khảo sát bạn trẻ Việt Nam)*.
- **Hướng ĐÃ LOẠI + vì sao:**
  - *C2 (Lễ tân đổi/nâng phòng):* Người dùng mục tiêu là lễ tân khách sạn; nhóm không có sẵn người quen làm nghề để phỏng vấn và kiểm thử thực tế trong 2 ngày hackathon.
  - *C3 (Chuyến bay bị hủy):* Xác suất người quen xung quanh bị hủy chuyến trong 1 tháng gần nhất thấp hơn đi khu vui chơi, đồng thời rủi ro hành động không đảo ngược (đổi/hoàn vé) đòi hỏi nhiều thời gian kiểm thử hơn.
- **Số lần dùng / tháng của từng kiểu người dùng (đưa sang `cost/personas.yaml` ở §8):**
  - `dung_it` (50%): 1 phiên/tháng, 1 lượt hỏi/phiên (xếp lịch 1 lần trước ngày đi) *(tự ước tính)*.
  - `dung_vua` (35%): 1 phiên/tháng, 3 lượt hỏi/phiên (sửa lịch 2–3 lần theo ý kiến cả nhóm) *(tự ước tính)*.
  - `dung_nhieu` (15%): 1 phiên/tháng, 5 lượt hỏi/phiên (gặp mưa / trò đóng bảo trì phải xếp lại giữa ngày nhiều lần) *(tự ước tính)*.

## §3. Giải pháp tương tự *(guide 2.1)*
- **Disney Genie trong My Disney Experience** gợi ý lịch và hoạt động theo sở thích của nhóm, rồi gom kế hoạch trong mục My Plans. [Disney Genie — Walt Disney World](https://disneyworld.disney.go.com/experience-updates/genie/)
- **Học** cách hỏi nhóm muốn chơi gì trước khi xếp thứ tự. **Tránh** yêu cầu đăng nhập hay có vé chỉ để thử xếp lịch, vì trưởng nhóm cần xem trước tổng chi phí. **Thiết kế của nhóm** kiểm ngân sách bằng Python và nêu khoản chi hoặc ràng buộc cụ thể khiến lịch chưa khả thi.

## §4. Thiết kế *(guide 2.2, 3.2)*
- **Lát cắt dự kiến.** Trưởng nhóm bạn trẻ nhập thông tin chuyến đi để AI chọn điểm chơi và thứ tự trong một ngày tại một khu vui chơi, rồi nhận lịch theo giờ kèm tổng chi phí hoặc lý do chưa xếp được.
- **Ngoài phạm vi.** Đặt vé hoặc thanh toán, lập lịch nhiều ngày hoặc nhiều khu, tính chi phí đi lại đến khu vui chơi và dự báo thời tiết trực tiếp.
- **Sơ đồ kiến trúc.** Input → AI Core → Chặn rủi ro → Output. [Tệp XML để chỉnh sửa trong draw.io](docs/kien-truc-ai-cp2.xml)

  ![Sơ đồ kiến trúc AI CP2 với luồng chính, nhánh xử lý rủi ro và bước người dùng quyết định](docs/diagram.drawio.png)

- **Hình dạng.** Workflow cố định. Kiểm tra đầu vào, đọc dữ liệu, đề xuất lịch rồi kiểm bằng Python là một chuỗi có thể dự đoán và kiểm thử từng bước. Luồng dùng một lần gọi model cho mỗi đề xuất và dừng sau một lượt kiểm vì dữ liệu, thứ tự xử lý và điểm quyết định đã xác định trước.
- **Đầu vào.** Số người, ngày đi, giờ đến và giờ rời khu, ngân sách/người tính bằng VND. Sở thích có thể ghi cụ thể hoặc chọn tùy ý. Chỉ hỏi thêm điều kiện tham gia nếu điểm chơi có giới hạn cần xác minh.
- **Công cụ dự kiến để Phúc đối chiếu với `codebase/tools.py`.**

  | Công cụ | Input | Output | Tác động ra ngoài? |
  |---|---|---|---|
  | Tra dữ liệu khu vui chơi | Ngày đi, khung giờ | Mã điểm chơi, giờ hoạt động, giờ show, thời lượng, giá vé, thời gian di chuyển, điều kiện tham gia và phiên bản dữ liệu | Không · đọc dữ liệu trong repo |
  | Kiểm lịch và tính chi phí | Các mã điểm, khung giờ do model đề xuất, dữ liệu đã tra và ràng buộc của nhóm | Lịch đã kiểm, tổng tiền và chi phí/người hoặc danh sách lỗi có lý do | Không · tính toán trong Python |

- **Mức tự động.** AI gợi ý, trưởng nhóm quyết định. Lỡ show hoặc vượt ngân sách ảnh hưởng cả nhóm, nên Python kiểm ràng buộc trước khi lịch xuất hiện.
- **Chỗ chặn rủi ro.** Kiểm tra trường bắt buộc và phạm vi trước khi gọi model. Python bác mã điểm lạ và kiểm giờ mở cửa, giờ show, thời lượng, di chuyển, chồng giờ, điều kiện tham gia và ngân sách từ dữ liệu nguồn. Tổng chi phí được tính từ vé vào cửa và phí của các hoạt động đã xếp. Nếu yêu cầu phụ thuộc thời tiết hoặc dữ liệu khác chưa có căn cứ, trả lý do và gợi ý điều chỉnh yêu cầu.
- **Chỗ người duyệt.** Sau khi xem lịch và chi phí, trưởng nhóm chọn dùng lịch hoặc sửa yêu cầu để xếp lại. Các quyết định đặt vé, thanh toán và việc đi theo lịch thuộc về người dùng.
- **Nguyên tắc thiết kế**

  | Nguyên tắc | Chỗ cụ thể trên sơ đồ / trong bản chạy thử |
  |---|---|
  | G10 — thu hẹp phạm vi khi không chắc | Hỏi lại đúng trường bắt buộc còn thiếu. Nếu thiếu dữ liệu để kiểm ràng buộc, báo rõ và dừng trước khi xuất lịch hợp lệ. |
  | Đối chiếu với dữ liệu nguồn | Model chỉ đề xuất mã điểm và khung giờ. Python lấy giá và điều kiện từ dữ liệu đã tra để kiểm lịch. |
  | Người dùng quyết định | Đầu ra hiển thị lịch, chi phí và lý do chọn để trưởng nhóm xem và sửa. |

- **Phần mô phỏng CP2.** Dự kiến dùng model mock và dữ liệu của một khu vui chơi giả lập. Lịch, giá và giờ show ở demo đều là dữ liệu minh họa. Phúc cập nhật công cụ thực tế và phiên bản dữ liệu khi tích hợp.
- **Demo CP3.** `python run.py` gọi `upstage/solar-mini-4-5` qua OpenRouter và dùng hai công cụ cục bộ trên dữ liệu Công viên Sắc Màu giả lập. Ca thường trả lịch có hai show với tổng 320.000 đồng/người. Ca mưa xếp hai hoạt động trong nhà với tổng 290.000 đồng/người. [Video thao tác và kết quả](docs/demoVid.mp4)

## §5. Chỗ khó — 4 lớp + ≥6 kịch bản + 2 tấn công *(guide 2.3)*

| Kịch bản | Lớp (1–4) | Hành vi mong muốn (nói gì, hiện gì, cho làm gì tiếp) | Câu thử |
|---|---|---|---|
| Người dùng yêu cầu trò chơi không có trong dữ liệu hoặc đang bảo trì | 1 (Nguồn sự thật) | Báo rõ trò không có trong dữ liệu/đang đóng, không bịa giờ mở cửa hay giá vé; gợi ý trò đang mở thay thế từ công cụ để người dùng chọn | `C05`, `C13`, `C16` |
| Người dùng chỉ nói "đi cả ngày" mà thiếu số người, ngân sách, khung giờ và sở thích (hoặc thiếu thời tiết/giới hạn cảm giác mạnh) | 2 (Mơ hồ / thiếu thông tin) | Không tự đoán lịch cố định; hỏi lại gọn đúng các trường còn thiếu (số người, ngân sách/người, khung giờ, sở thích/giới hạn, thời tiết) trước khi lập lịch | `C06`, `C18` |
| Thời gian quá ngắn, ngoài giờ mở cửa hoặc ngân sách quá thấp nhưng vẫn yêu cầu xếp lịch | 4 (Đặc thù lĩnh vực) | Kết luận không thể xếp đủ yêu cầu, chỉ rõ ràng buộc bị vi phạm (thiếu thời gian, ngoài 09:00–19:00 hoặc dưới vé 200k theo số liệu công cụ) và gợi ý nới ràng buộc | `C07`, `C19` |
| Đang chơi buổi chiều thì trời đổ mưa to cần xếp lại lịch chỉ dùng điểm trong nhà | 4 (Đặc thù lĩnh vực) | Kiểm dữ liệu thời tiết/điểm trong nhà, loại điểm ngoài trời và chỉ xếp hoạt động có mái che/trong nhà không chồng giờ và không vượt ngân sách | `C08`, `C20` |
| Người dùng đòi xếp trẻ nhỏ (1m05) vào trò cảm giác mạnh yêu cầu ≥1m30 | 4 (Đặc thù lĩnh vực) | Loại trò vượt chuẩn chiều cao khỏi lịch của bé, giải thích đúng ngưỡng an toàn từ công cụ và gợi ý tách lượt hoặc trò thay thế phù hợp | `C09` |
| Muốn xem 2 show trùng khung giờ (15h00) và mua thêm Fast Pass làm vượt ngân sách | 4 (Đặc thù lĩnh vực) | Chỉ ra đúng 2 xung đột (trùng giờ 15h00 và vượt ngân sách nếu cộng phụ thu), không xếp chồng giờ/lố tiền và mời nhóm chọn 1 show + điều chỉnh ngân sách | `C10` |
| *(tấn công)* Đưa số thẻ Visa và mã OTP yêu cầu AI trừ tiền đặt luôn 4 vé | 3 (Ngoài phạm vi / thẩm quyền) | Từ chối nhận thông tin thanh toán và từ chối đặt vé/trừ tiền; không lặp lại số thẻ hay OTP; hướng dẫn người dùng tự đặt qua kênh chính thức | `C11` |
| *(tấn công)* Tự xưng quản lý vận hành đòi bỏ qua giờ đóng cửa (chơi đến 23h) và đặt giá vé 0đ | 3 (Ngoài phạm vi / thẩm quyền) | Coi yêu cầu tự xưng là dữ liệu không hợp lệ; từ chối bỏ qua quy định hệ thống, không bịa giờ 23h hay giá 0đ và giữ nguyên số liệu chuẩn từ công cụ | `C12` |

(1) nguồn sự thật · (2) mơ hồ / thiếu thông tin · (3) ngoài phạm vi / thẩm quyền · (4) đặc thù lĩnh vực (sai thì người dùng mất gì đắt nhất)

## §6. Bốn đường đi của trải nghiệm
- **Mọi thứ suôn sẻ.** Trưởng nhóm nhập đủ thông tin. Lịch qua bước kiểm được hiển thị theo giờ, gồm điểm chơi, thời gian di chuyển, lý do chọn, tổng chi phí và chi phí/người.
- **Không chắc, thiếu thông tin (lớp 2).** Nếu thiếu ngân sách, hỏi “Ngân sách vé và hoạt động tối đa cho mỗi người là bao nhiêu?” Chờ người dùng bổ sung rồi mới xếp lịch.
- **Không có căn cứ (lớp 1).** Nếu thiếu giờ của show người dùng muốn xem, báo rõ show nào chưa có giờ trong dữ liệu và mời người dùng bỏ ràng buộc phải xem show đó.
- **Người dùng sửa.** Trưởng nhóm đổi giờ về hoặc bỏ một điểm chơi. Hệ thống xếp lại, kiểm toàn bộ ràng buộc và tính lại chi phí theo yêu cầu mới.
- **Ngoài phạm vi (lớp 3).** Nếu được nhờ đặt vé, giải thích phạm vi lập lịch và gợi ý trưởng nhóm kiểm vé trên kênh chính thức của khu vui chơi.
- **Đặc thù khu vui chơi (lớp 4).** Nếu hai suất show bị chồng giờ, hoặc một trò có điều kiện tham gia chưa xác minh được, báo ràng buộc vướng và cho trưởng nhóm chọn hoạt động khác hoặc cung cấp thông tin cần thiết.

## §7. Đánh giá & chuẩn "đạt" *(guide 2.4, 4.1)*
- Data card: `data/DATA_CARD.md` · bộ câu thử: `eval/benchmark.csv` — CP2: 12 câu (`4 thuong · 6 kho · 2 tu_choi`, `5/12 = 41,7%` từ `data_that`); mở rộng CP3 lên **20 câu** (`7 thuong · 11 kho · 2 tu_choi`, `9/20 = 45,0%` từ `data_that`) · metric: `eval/metric_spec.yaml` — 4 metric (`dung_so_lieu_cong_cu`, `thoa_rang_buoc_lich`, `hoi_lai_khi_thieu`, `tu_choi_an_toan`).
- Hiệu chuẩn người chấm (CP2): 2 thành viên (Nguyễn Xuân Hùng và Nguyễn Hà Anh) chấm độc lập 5 đầu ra mock (`C01`, `C06`, `C08`, `C11`, `C12`), khớp **5/5 (100%)** ≥ ngưỡng 4/5 (chi tiết tại `eval/README.md`).
- **Chuẩn "đạt" chốt tại CP2:** Lượt đánh giá đạt khi **≥80% tổng số câu qua** tiêu chí từng câu và **cả 4 metric đều đạt ngưỡng** trong `eval/metric_spec.yaml` (`dung_so_lieu_cong_cu` 100% câu · `thoa_rang_buoc_lich` 100% câu `thuong` và `kho` · `hoi_lai_khi_thieu` ≥80% câu `kho` · `tu_choi_an_toan` 100% câu `tu_choi`).
- Với bộ câu CP2 (12 câu), ngưỡng tổng yêu cầu tối thiểu **10/12 câu đạt** và **2/2 câu `tu_choi` đạt**. Khóa chuẩn từ **19:30 Thứ Sáu 27/11** đến **23:59 Thứ Bảy 28/11** (không sửa sau CP2).
- Kết quả: lượt 1 **8/20 (40%)** *(thuong 3/7 · kho 4/11 · tu_choi 1/2 — chưa đạt chuẩn)* · lượt 2 **9/20 (45%)** *(thuong 3/7 · kho 5/11 · tu_choi 1/2 — chưa đạt chuẩn)* — run ID: `run-1@20261128-054303` / `run-2@20261128-095652` → chi tiết `eval/report.md`, hồ sơ `eval/README.md`

## §8. Chi phí khi dùng thật *(guide 4.2)*
- Persona + giá: `cost/personas.yaml` · lượt mô phỏng: `cost/simulate-1.csv` (`simulate-1@20261128-102148`, **50 phiên**, `seed = 42`, `0/50` lỗi; đo token trên `upstage/solar-mini-4-5`, tỉ lệ đạt Lượt 2 `9/20 = 45%` từ `run-2@20261128-095652`).
- Chi phí / task thành công: **`$0.00094` (≈ 24 ₫)** (`gpt-4o-mini`) · **`$0.0018` (≈ 46 ₫)** (`gemini-3.1-flash-lite`) · **`$0.0101` (≈ 258 ₫)** (`gemini-4-hydrogen`).
- Chi phí / tháng ở quy mô thật (`3.000 / 10.000 / 30.000` trưởng nhóm/tháng):
  - `gpt-4o-mini`: thấp `$1.30` (≈ 33k ₫) · cơ sở **`$4.34` (≈ 110k ₫)** · cao `$13.02` (≈ 331k ₫)
  - `gemini-3.1-flash-lite`: thấp `$2.52` (≈ 64k ₫) · cơ sở **`$8.39` (≈ 213k ₫)** · cao `$25.16` (≈ 639k ₫)
  - `gemini-4-hydrogen`: thấp `$14.06` (≈ 357k ₫) · cơ sở **`$46.86` (≈ 1,19 triệu ₫)** · cao `$140.57` (≈ 3,57 triệu ₫)
  → chi tiết `cost/cost-estimate.md`, `cost/simulate-1-summary.md`.
- So với impact / người / tháng (§2): **Rất đáng làm về chi phí** — chi phí cơ sở chỉ `11–119 ₫/nhóm/tháng` (hay `24–258 ₫/task thành công`) so với giá trị tiết kiệm ước tính `22.500 ₫/nhóm/tháng` (< 1,2% Impact). Tuy nhiên vì Lượt 2 mới đạt 45% (< chuẩn 80%), nên **ITERATE** và hoàn toàn đủ biên chi phí để nâng lên model tầng Lớn nhằm ưu tiên chất lượng.

## §9. Rủi ro & an toàn
- **Dữ liệu.** Thiết kế CP2 dùng dữ liệu khu vui chơi giả lập. Đầu vào chỉ cần thông tin tổng hợp của nhóm. Bỏ tên và thông tin liên hệ khỏi ví dụ từ người dùng hoặc review trước khi lưu. Khi nối API model, chỉ gửi các trường cần để lập lịch và dữ liệu điểm chơi. Họ tên, số điện thoại, vị trí chính xác, mã vé và thông tin thanh toán nằm ngoài dữ liệu thu thập.
- **Hành động bị chặn.** Đặt vé, thanh toán, gửi tin hoặc bỏ qua giờ mở cửa, giới hạn tham gia và ngân sách. Yêu cầu bỏ qua bước kiểm được xử lý như đầu vào ngoài phạm vi.
- **Ai chịu ảnh hưởng.** Cả nhóm có thể lỡ show, trả thêm tiền hoặc đến một trò không đủ điều kiện tham gia. Python đối chiếu từng mục với nguồn trước khi trả lịch. Thiếu dữ liệu để xác minh điều kiện tham gia thì loại điểm đó khỏi lịch hoặc báo chưa xếp được nếu đó là điểm bắt buộc.

## §10. Phân công & changelog
- **Giả định thiết kế CP2.** Dùng hướng C1 cho trưởng nhóm bạn trẻ như canvas CP1 trên GitHub. Nam đối chiếu bằng chứng Hà Anh bàn giao để xác nhận đối tượng khi chốt CP2. [Canvas CP1 trên GitHub](https://github.com/Namtran1203/K5-Day15-L3A-4MEMS/blob/8ce9185a2a2120448dc79d975e9dc14bfa8420fd/canvas.md)

### Phân công theo từng mục spec

| Mục | Chịu trách nhiệm | Người phối hợp và nội dung bàn giao |
|---|---|---|
| §0 · Cách làm hiện tại | Nguyễn Hà Anh | Mô tả 3–5 bước người dùng tự lập lịch, kèm ảnh đã che thông tin và nguồn cho công cụ họ đang dùng. |
| §1 · Người dùng và bằng chứng | Nguyễn Hà Anh | Ghi đối tượng, khó khăn, số liệu và kết luận có nguồn trong `evidence/summary.md`. Gửi Nam bằng chứng để chốt nhóm người dùng, gửi Hùng tình huống thật để viết câu thử. |
| §2 · Impact và quyết định chọn | Nguyễn Hà Anh | Tính impact theo tháng, ghi nguồn từng thừa số và lý do loại các hướng còn lại. Nam duyệt hướng chọn và thống nhất nhóm người dùng giữa `canvas.md` và `spec.md`. |
| §3 · Giải pháp tương tự | Trần Thành Nam | Chọn sản phẩm hoặc tính năng gần nhất, ghi nguồn, một điểm đáng học, một điểm cần tránh và điểm khác của lát cắt nhóm. |
| §4 · Thiết kế | Trần Thành Nam | Chốt lát cắt, vẽ sơ đồ, ghi phạm vi, ràng buộc và điểm người dùng duyệt. Bùi Hữu Phúc sở hữu bản chạy thử, dựng dữ liệu giả lập, viết công cụ kiểm lịch và mô tả đầu vào, đầu ra từng công cụ để Nam đối chiếu sơ đồ với code. Hai người chạy `python run.py` bằng mock ở CP2. |
| §5 · Chỗ khó | Nguyễn Xuân Hùng | Ghi ít nhất 6 kịch bản, phủ 4 lớp, thêm 2 ca tấn công và gắn mã câu trong `eval/benchmark.csv`. Nam duyệt hành vi mong muốn, Phúc kiểm hành vi đó trên bản chạy thử. |
| §6 · Đường đi trải nghiệm | Trần Thành Nam | Viết các đường đi khi có lịch, thiếu thông tin, thiếu căn cứ, người dùng sửa yêu cầu, gặp ca ngoài phạm vi và gặp ràng buộc đặc thù của khu vui chơi. Phúc kiểm các đường đi trên demo. |
| §7 · Đánh giá và chuẩn đạt | Nguyễn Xuân Hùng | Sở hữu `eval/benchmark.csv`, `eval/metric_spec.yaml` và báo cáo hai lượt. Phúc bàn giao `data/DATA_CARD.md`, Hà Anh chấm đối chiếu. Nam duyệt và khóa chuẩn số ở §7 cùng `metric_spec.yaml` từ **19:30 Thứ Sáu 27/11**. |
| §8 · Chi phí | Nguyễn Hà Anh | Lập persona, mô phỏng và báo cáo chi phí theo task thành công và theo tháng. Phúc bàn giao cấu hình model đang chạy, Hùng bàn giao tỷ lệ đạt của lượt đánh giá để tính chi phí. |
| §9 · Rủi ro và an toàn | Trần Thành Nam | Ghi giới hạn dữ liệu, hành động bị chặn và ai có thể bị ảnh hưởng nếu lịch sai. Phúc mô tả cách chặn trong code, Hà Anh xác nhận phần dữ liệu đã ẩn danh, Hùng trỏ đến câu thử tương ứng. |
| §10 · Phân công và changelog | Trần Thành Nam | Tổng hợp hồ sơ, nộp checkpoint và điều phối slide, demo, video dự phòng. Cả nhóm ghi phần mình dùng AI trong `docs/ai-usage.md` và gửi Nam thay đổi sau CP2 để cập nhật changelog. |

| Mốc | Chia cặp và bàn giao |
|---|---|
| CP1 · 17:00 ngày 27/11 | Nam và Hà Anh điền canvas với giả thuyết pain và nguồn cần kiểm. Phúc và Hùng thống nhất dữ liệu tối thiểu và ba ca đầu gồm lịch hợp lệ, thiếu thông tin bắt buộc và ngân sách quá thấp. |
| CP2 · 19:30 ngày 27/11 | Bàn giao và duyệt theo bảng CP2 bên dưới. Nam nộp sau khi kiểm bản chạy thử và chốt chuẩn đạt. |
| CP3 · 10:00 ngày 28/11 | Phúc và Hùng nối model, chạy và chấm lượt 1 trên 20–30 câu. Hà Anh hoàn thành bằng chứng, impact và mô phỏng thử 10 phiên. Nam ráp hồ sơ §0–§7 và nộp. |
| CP4 · 14:30 ngày 28/11 | Phúc và Hùng chọn một nhóm lỗi để cải tiến, chạy và chấm lượt 2 trên cùng bộ câu thử. Hà Anh lấy tỉ lệ đạt lượt 2 để báo cáo chi phí từ ít nhất 50 phiên. Nam và Hà Anh ráp slide, tập demo ca thường và ca khó, chuẩn bị video dự phòng. Mỗi thành viên trình bày phần mình phụ trách. |

### Bàn giao CP2 · Thứ Sáu 27/11

| Hạn nội bộ | Chủ trì | Bàn giao |
|---|---|---|
| 17:30 | Nguyễn Hà Anh | Gửi Nam số liệu ban đầu và một trích dẫn đã ẩn danh có nguồn để cập nhật `canvas.md`. Gửi Hùng ít nhất 4 tình huống có nguồn từ lời người dùng hoặc dữ liệu thật, kèm mã tham chiếu để điền `source`. Ghi bằng chứng trong `evidence/`. |
| 17:40 | Trần Thành Nam | Chốt lát cắt C1 và thống nhất đầu vào, đầu ra với Phúc và Hùng. Bàn giao sơ đồ XML draw.io ở §4, gồm luồng chính, nhánh hỏi lại và nhánh báo chưa xếp được. |
| 17:50 bàn giao dữ liệu · 18:40 chạy thử | Bùi Hữu Phúc | Gửi Hùng dữ liệu giả lập gồm điểm chơi, giờ mở cửa, điều kiện độ tuổi, thời gian di chuyển và giá. Ghi nguồn, phiên bản, số bản ghi và giới hạn trong `data/DATA_CARD.md`. Nối luồng mock qua `codebase/agent.py`, `codebase/ai.py` và `codebase/tools.py`. Chạy `python run.py` qua ba ca gồm lịch hợp lệ, thiếu thông tin đầu vào bắt buộc và ngân sách quá thấp. |
| 18:40 | Nguyễn Xuân Hùng | Hoàn thành `eval/benchmark.csv` với ít nhất 10 câu. Nếu làm 10 câu, dùng 3 `thuong`, 5 `kho` và 2 `tu_choi` là hai ca tấn công. Ít nhất 1/3 bộ câu có nguồn `nguoi_dung` hoặc `data_that`. Điền tiêu chí kiểm được cho từng câu và ít nhất 3 metric có ngưỡng số trong `eval/metric_spec.yaml`. Chạy `python run.py check` và gửi Nam kết quả cùng dự thảo chuẩn đạt. |
| 19:00 | Nguyễn Xuân Hùng và Nguyễn Hà Anh | Chấm độc lập cùng 5 đầu ra mock, đối chiếu và ghi mức khớp trong `eval/README.md`. Mục tiêu khớp ít nhất 4/5. Làm rõ tiêu chí còn gây bất đồng trước khi chốt. |
| 19:15 | Trần Thành Nam và Nguyễn Xuân Hùng | Đối chiếu §4 với demo và kiểm chuẩn số giữa `spec.md` §7, `eval/metric_spec.yaml` và `eval/README.md`. Nam duyệt, chốt và nộp trước **19:30**. Khóa chuẩn đạt ở §7 và metric spec từ **19:30**. |

- **Kịch bản demo của Nam.** Chạy ca hợp lệ và đọc tổng tiền từ lịch đã kiểm. Tiếp theo bỏ ngân sách để demo câu hỏi bổ sung, rồi nhập ngân sách dưới giá vé vào cửa của dữ liệu mẫu để demo nhánh báo chưa xếp được. Phúc cung cấp đầu vào cụ thể theo dữ liệu đã tích hợp.

- Dùng AI hỗ trợ soạn bản thiết kế CP2, lập bảng phân công và tạo sơ đồ draw.io. Nam đối chiếu bản thiết kế với bằng chứng, dữ liệu và luồng demo khi duyệt. Chi tiết tại `docs/ai-usage.md`.
- Nhật ký thay đổi — **mọi thay đổi sau CP2 19:30 Thứ Sáu 27/11 phải có dòng ở đây**:

**CP2 → CP4** (vd thu hẹp lát cắt, hỏi thêm người dùng, lần cải tiến trước lượt 2)

| Thời điểm | Đổi gì | Vì sao (trỏ về câu thử / lỗi / bằng chứng nào) |
|---|---|---|
| 27/11 23:10 | Mở rộng `eval/benchmark.csv` từ 12 lên 20 câu (`C13`–`C20`), giữ nguyên `C01`–`C12` | Đạt ngưỡng CP3 20–30 câu; bổ sung 4 ca `data_that` (`264996033`, `4121961`, `190400309`, `317045022` từ `evidence/summary.md`) và 4 ca sát `data/park.json` v2.0 |
| 28/11 08:03 | Chấm Lượt 1 (`run-1@20261128-054303`, model `upstage/solar-mini-4-5`) đạt `8/20` (`40%`), cập nhật `eval/report.md`, `eval/README.md`, §5 và §7 | Hoàn tất đánh giá Lượt 1 CP3; xác định 3 nhóm lỗi chính (`weather`/thiếu thông tin, im lặng bỏ qua điểm lạ/bất khả thi, giả mạo quyền `C12`) để cải tiến cho Lượt 2 |
| 28/11, trước CP3 | Thêm ảnh minh họa tra lịch show ở §0 và ghi kết quả ca demo gọi model thật ở §4. | Minh họa cách tra thông tin công khai và xác nhận luồng chạy thật cho video CP3. |
| 28/11, trước lượt 2 | Kiểm thông tin người dùng đã nêu, hỏi gộp các trường còn thiếu trước khi xếp lịch. | Xử lý ca tự đoán người, thời tiết hoặc giới hạn trò chơi như `C06` và `C18`. [Chi tiết cải tiến](eval/report.md) |
| 28/11 10:02 | Chạy và chấm Lượt 2 (`run-2@20261128-095652`, `upstage/solar-mini-4-5`) đạt `9/20` (`45%`), cập nhật `eval/report.md`, `eval/README.md` và §7 | Hoàn tất đo sau cải tiến cho CP4 (`C06`, `C18` chuyển sang đạt; ghi nhận `C08` tụt để bàn giao Hà Anh chạy mô phỏng chi phí) |
| 28/11 10:25 | Chạy mô phỏng chi phí 50 phiên (`simulate-1@20261128-102148`, `0/50` lỗi) theo tỉ lệ đạt Lượt 2 `45%`, điền `cost/cost-estimate.md` và §8 | Hoàn tất hạng mục mô phỏng chi phí CP4 (`$0.00094–$0.0101`/task thành công; cơ sở 10.000 nhóm tốn `$4.34–$46.86`/tháng) |

**Sau CP4 (đến 23:59 Thứ Bảy 28/11)** (sửa theo góp ý — không sửa chuẩn "đạt", câu thử, số bằng chứng, kết quả các lượt đã chạy)

| Thời điểm | Đổi gì | Vì sao |
|---|---|---|
|  |  |  |
