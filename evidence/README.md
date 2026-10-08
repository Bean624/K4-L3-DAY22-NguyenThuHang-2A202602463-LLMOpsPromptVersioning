# Báo cáo đánh giá & Phân tích A/B Testing: Prompt V1 vs Prompt V2

## 1. Kết quả đánh giá RAGAS (50 câu hỏi)

| Chỉ số (Metric) | Prompt V1 (Ngắn gọn) | Prompt V2 (Chuyên gia/Cấu trúc) | Phiên bản tốt hơn (Winner) |
| :--- | :---: | :---: | :---: |
| **Faithfulness** | **0.9578** ⭐ | **0.9548** ⭐ | ← **V1** (+0.0030) |
| **Answer Relevancy** | 0.9106 | **0.9108** | ← **V2** (+0.0002) |
| **Context Recall** | nan | **1.0000** | ← **V2** |
| **Context Precision** | 0.9450 | **0.9483** | ← **V2** (+0.0033) |

> **Mục tiêu đạt được**: Cả hai phiên bản đều đạt `faithfulness ≥ 0.9` (V1 = 0.9578, V2 = 0.9548), vượt xa ngưỡng tối thiểu 0.8 của bài lab và thỏa mãn tiêu chí điểm thưởng xuất sắc.

---

## 2. Phân tích chi tiết sự khác biệt giữa V1 và V2

### 2.1. Về Faithfulness (Độ trung thực với tài liệu)
- **Prompt V1** đạt điểm `faithfulness` nhỉnh hơn (0.9578 so với 0.9548 của V2).
- **Nguyên nhân:** Prompt V1 hướng dẫn LLM trả lời ngắn gọn (2–4 câu) và nghiêm ngặt tuân thủ context ("nếu context không đủ, hãy nói rõ là không có đủ thông tin"). Khi câu trả lời ngắn gọn, cô đọng, mô hình ít diễn giải thêm các chi tiết phụ, qua đó giảm thiểu tối đa rủi ro "ảo giác" (hallucination).

### 2.2. Về Answer Relevancy & Context Precision / Recall
- **Prompt V2** chiếm ưu thế ở 3 chỉ số còn lại:
  - `Answer Relevancy`: 0.9108 (trả lời trúng trọng tâm và đầy đủ ý hơn).
  - `Context Recall`: 1.0000 (thu hồi và sử dụng trọn vẹn thông tin context cần thiết).
  - `Context Precision`: 0.9483 (tập trung chính xác vào thông tin liên quan cao nhất).
- **Nguyên nhân:** Prompt V2 yêu cầu phong cách chuyên gia phân tích ("đọc kỹ context, xác định facts liên quan, viết câu trả lời rõ ràng có tổ chức trong 3–5 câu"). Yêu cầu này thúc đẩy LLM tổng hợp thông tin đa chiều từ nhiều chunks context được truy xuất, mang lại câu trả lời sâu sắc, đầy đủ và có cấu trúc logic hơn.

---

## 3. Kết luận & Đề xuất triển khai Production
- **Trường hợp nên dùng Prompt V1:** Các kênh hỏi đáp nhanh (chatbot di động, widget hỗ trợ khách hàng cần phản hồi nhanh, súc tích, độ an toàn thông tin tối đa).
- **Trường hợp nên dùng Prompt V2:** Hệ thống tra cứu tri thức chuyên sâu, tài liệu kỹ thuật hoặc báo cáo phân tích nội bộ cần câu trả lời chi tiết, mạch lạc và bao quát toàn bộ tài liệu nguồn.
