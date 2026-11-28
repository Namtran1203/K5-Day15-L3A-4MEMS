# Tóm tắt mô phỏng simulate-1@20261128-102148

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 26 | 1 | 860 | 96 | 1.0 | 2.0 |
| dung_vua | 17 | 3 | 2569 | 307 | 3.0 | 6.0 |
| dung_nhieu | 7 | 5 | 4252 | 505 | 5.0 | 10.0 |

Tỉ lệ đạt dùng để tính: 9/20 (45%) — lượt run-2@20261128-095652

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (3.000 người) | Chi phí / tháng — cơ sở (10.000 người) | Chi phí / tháng — cao (30.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-4o-mini (vào 0.15 · ra 0.6 $/1M) | $0.00042 (≈ 11 ₫) | $0.00094 (≈ 24 ₫) | $0.00042 (≈ 11 ₫) | $1.30 (≈ 33.060 ₫) | $4.34 (≈ 110.200 ₫) | $13.02 (≈ 330.599 ₫) | $0.00043 (≈ 11 ₫) |
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.00082 (≈ 21 ₫) | $0.0018 (≈ 46 ₫) | $0.00081 (≈ 21 ₫) | $2.52 (≈ 63.915 ₫) | $8.39 (≈ 213.051 ₫) | $25.16 (≈ 639.152 ₫) | $0.00084 (≈ 21 ₫) |
| gemini-4-hydrogen (vào 1.5 · ra 7.5 $/1M) | $0.0046 (≈ 116 ₫) | $0.0101 (≈ 258 ₫) | $0.0045 (≈ 115 ₫) | $14.06 (≈ 357.045 ₫) | $46.86 (≈ 1.190.151 ₫) | $140.57 (≈ 3.570.454 ₫) | $0.0047 (≈ 119 ₫) |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (2.2) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: upstage/solar-mini-4-5. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
- Tỷ giá: 1 USD = 25.400 ₫ (Tỷ giá tham khảo USD/VND ~25.400đ · xem 27/11/2026 (tự ước tính làm tròn)).
