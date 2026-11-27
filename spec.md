# AI SPEC — [Tên lát cắt] · Nhóm [tên nhóm] · Phòng [XXX] · Zone [X]

> Mốc nộp: §7 chốt chuẩn "đạt" tại **CP2 19:30 Thứ Sáu 27/11** · §0–§7 nộp **CP3 10:00 Thứ Bảy 28/11** · đủ §0–§10 **CP4 14:30 Thứ Bảy 28/11** · §10 changelog ghi tiếp đến **23:59 Thứ Bảy 28/11**.
> Đầu mỗi mục ghi bước guide (`02-guide.md` trong repo đề) chỉ cách điền. Mỗi mục ngắn, có số và nguồn; chi tiết để ở file được trỏ tới. Xoá dòng hướng dẫn trong ngoặc vuông khi điền xong.

Track: [ ] A · [ ] B · [ ] C · [ ] D · [ ] E — bài toán: [đề gợi ý trong file track, hoặc bài toán nhóm tự mở rộng] __
Data BTC cấp đã dùng (nếu có — không commit nguyên file): __

## §0. Hiện tại việc này diễn ra thế nào *(guide 1.1)*
- Luồng hiện tại của việc này, trong khoá hoặc trên app thật (3–5 bước; ảnh chụp từ tài khoản của mình, đã che thông tin):
- Công cụ / AI đang được dùng cho việc này (nếu có) + nguồn. Không kiểm được thì ghi "chưa kiểm":

## §1. Người dùng & bằng chứng *(guide 1.1, 1.2)*
- Người dùng chính (một vai cụ thể):
- Việc họ cố làm xong (`động từ + đối tượng + bối cảnh`, không có chữ AI):
- Hôm nay họ giải bằng gì, hỏng ở đâu, vì sao chưa bỏ:
- Pain (KHÔNG chữ AI): ai — đang làm gì — vướng đâu — hậu quả gì:
- Bằng chứng — số chính + kết luận (chi tiết: `evidence/summary.md`): __

## §2. Impact & quyết định chọn *(guide 1.3)*

| Hướng | Bao nhiêu người gặp | Bao nhiêu lần / tháng | Mỗi lần tốn gì | Impact / tháng | Làm kịp không | Chọn? |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

- **Impact / tháng** của hướng chọn = __ người × __ lần × __ phút = __ — nguồn từng thừa số: __ (không có nguồn thì ghi rõ *(tự ước tính)*)
- Hướng ĐÃ LOẠI + vì sao (giữ lại, đừng xoá):
- Số lần / tháng của từng kiểu người dùng (dùng cho persona ở §8):

## §3. Giải pháp tương tự *(guide 2.1)*
- [sản phẩm / tính năng gần giống]: một điều đáng học · một điều đáng né · mình khác gì

## §4. Thiết kế *(guide 2.2, 3.2)*
- **Lát cắt MỘT CÂU** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả):
- Không làm (≥3 điều):
- **Sơ đồ** (ảnh / Mermaid / draw.io): [chèn ở đây]
- **Hình dạng:** [ ] workflow cố định · [ ] một agent · [ ] nhiều agent — 2 dòng lý do, và vì sao **không** chọn hình dạng phức tạp hơn:
- **AI dựa vào đâu** — mỗi công cụ (khớp `codebase/tools.py`):

  | Công cụ | Input | Output | Tác động ra ngoài? |
  |---|---|---|---|
  |  |  |  |  |

- **Mức tự động:** [ ] AI gợi ý, người quyết · [ ] AI tự làm khi chắc, chuyển người khi không · [ ] AI tự làm — lý do (sai thì ai chịu gì, sửa đắt hay rẻ):
- **Chỗ chặn rủi ro** (rủi ro lớn nhất của lát cắt bị chặn ở đâu, bằng gì):
- **Chỗ người duyệt** (việc AI không được tự làm):
- **Nguyên tắc thiết kế** (≥3, bắt buộc G10):

  | Nguyên tắc | Chỗ cụ thể trên sơ đồ / trong bản chạy thử |
  |---|---|
  | G10 — thu hẹp phạm vi khi không chắc |  |
  |  |  |
  |  |  |

- Phần nào còn giả (công cụ trả dữ liệu giả, model chế độ giả…) — ghi rõ, không giả làm thật:

## §5. Chỗ khó — 4 lớp + ≥6 kịch bản + 2 tấn công *(guide 2.3)*

| Kịch bản | Lớp (1–4) | Hành vi mong muốn (nói gì, hiện gì, cho làm gì tiếp) | Câu thử |
|---|---|---|---|
|  |  |  |  |
| *(tấn công)* |  |  |  |
| *(tấn công)* |  |  |  |

(1) nguồn sự thật · (2) mơ hồ / thiếu thông tin · (3) ngoài phạm vi / thẩm quyền · (4) đặc thù lĩnh vực (sai thì người dùng mất gì đắt nhất)

## §6. Bốn đường đi của trải nghiệm
- Mọi thứ suôn sẻ: · Không chắc (lớp 2): · Không có căn cứ (lớp 1): · Người dùng sửa:
- Bị đòi ngoài phạm vi (lớp 3): · Trường hợp đặc thù lĩnh vực (lớp 4):

## §7. Đánh giá & chuẩn "đạt" *(guide 2.4, 4.1)*
- Data card: `data/DATA_CARD.md` · bộ câu thử: `eval/benchmark.csv` — __ câu (thuong __ · kho __ · tu_choi __) · metric: `eval/metric_spec.yaml` (__ metric)
- **Chuẩn "đạt"** (chốt **trước 19:30 Thứ Sáu 27/11**, giữ nguyên đến 23:59 Thứ Bảy 28/11): "Đạt khi ≥ __% câu qua, và __"
- Kết quả: lượt 1 __/__ (__%) · lượt 2 __/__ (__%) — run ID: __ / __ → chi tiết `eval/report.md`, hồ sơ `eval/README.md`

## §8. Chi phí khi dùng thật *(guide 4.2)*
- Persona + giá: `cost/personas.yaml` · lượt mô phỏng: `cost/simulate-__.csv` (__ phiên)
- Chi phí / task thành công: __ (model __) · __ (model __)
- Chi phí / tháng ở quy mô thật: thấp __ · cơ sở __ · cao __ → chi tiết `cost/cost-estimate.md`
- So với impact / người / tháng (§2): đáng làm không, vì sao:

## §9. Rủi ro & an toàn
- Dữ liệu: đã ẩn danh gì, không thu gì, không đưa gì vào model gói miễn phí:
- AI **không được** làm gì kể cả khi người dùng yêu cầu:
- Ai có thể bị hại nếu AI sai, và nhóm chặn thế nào:

## §10. Phân công & changelog
- **Hướng dự kiến** — C1, xếp lịch một ngày tại một khu vui chơi cho gia đình có trẻ nhỏ. AI chọn điểm và thứ tự theo độ tuổi, sở thích, khung giờ và ngân sách. Python kiểm giờ mở cửa, thời gian di chuyển, chồng giờ và tổng tiền. Đầu ra là lịch theo giờ kèm tổng tiền hoặc lý do chưa xếp được. Nhóm dùng bằng chứng người dùng để chốt hướng ở CP2.

| Người phụ trách | Đầu việc và nơi bàn giao |
|---|---|
| Trần Thành Nam | Chốt lát cắt, thiết kế luồng và hành vi khi thiếu dữ liệu trong `spec.md` §3–§6 và §9. Tổng hợp hồ sơ, nộp checkpoint, điều phối slide, demo và video dự phòng. |
| Bùi Hữu Phúc | Dựng dữ liệu của một khu vui chơi giả lập, ghi nguồn và phiên bản trong `data/DATA_CARD.md`. Xây công cụ tra điểm, lịch, giá và kiểm ràng buộc bằng Python. Tích hợp luồng trong `codebase/agent.py` và nối model cho CP3. |
| Nguyễn Hà Anh | Tìm review công khai và hỏi người từng đi khu vui chơi cùng trẻ nhỏ. Ghi bằng chứng và nguồn trong `evidence/`, hoàn thiện `spec.md` §0–§2. Từ bằng chứng, lập persona, chạy mô phỏng và báo cáo chi phí so với impact trong `cost/` và `spec.md` §8. |
| Nguyễn Xuân Hùng | Viết câu thử và metric trong `eval/`, đề xuất chuẩn đạt với Nam trước CP2. Chạy và chấm hai lượt, phân tích lỗi và tổng hợp kết quả trong `eval/report.md` và `spec.md` §7. |

| Mốc | Chia cặp và bàn giao |
|---|---|
| CP1 · 17:00 ngày 27/11 | Nam và Hà Anh điền canvas với giả thuyết pain và nguồn cần kiểm. Phúc và Hùng thống nhất dữ liệu tối thiểu và ba ca đầu: lịch hợp lệ, thiếu cơ cấu người lớn/trẻ em, ngân sách quá thấp. |
| CP2 · 19:30 ngày 27/11 | Nam và Phúc chốt phạm vi C1 theo bằng chứng và chạy demo với dữ liệu giả lập. Hà Anh đưa tình huống thực tế cho Hùng để hoàn thành ít nhất 10 câu thử và 3 metric. Nam và Hùng chốt chuẩn đạt trước giờ nộp. |
| CP3 · 10:00 ngày 28/11 | Phúc và Hùng nối model, chạy và chấm lượt 1 trên 20–30 câu. Hà Anh hoàn thành bằng chứng, impact và mô phỏng thử 10 phiên. Nam ráp hồ sơ §0–§7 và nộp. |
| CP4 · 14:30 ngày 28/11 | Phúc và Hùng chọn một nhóm lỗi để cải tiến, chạy và chấm lượt 2 trên cùng bộ câu thử. Hà Anh lấy tỉ lệ đạt lượt 2 để báo cáo chi phí từ ít nhất 50 phiên. Nam và Hà Anh ráp slide, tập demo ca thường và ca khó, chuẩn bị video dự phòng. Mỗi thành viên trình bày phần mình phụ trách. |

- Dùng AI vào việc gì (2–3 dòng; chi tiết `docs/ai-usage.md`):
- Nhật ký thay đổi — **mọi thay đổi sau CP2 19:30 Thứ Sáu 27/11 phải có dòng ở đây**:

**CP2 → CP4** (vd thu hẹp lát cắt, hỏi thêm người dùng, lần cải tiến trước lượt 2)

| Thời điểm | Đổi gì | Vì sao (trỏ về câu thử / lỗi / bằng chứng nào) |
|---|---|---|
|  |  |  |

**Sau CP4 (đến 23:59 Thứ Bảy 28/11)** (sửa theo góp ý — không sửa chuẩn "đạt", câu thử, số bằng chứng, kết quả các lượt đã chạy)

| Thời điểm | Đổi gì | Vì sao |
|---|---|---|
|  |  |  |
