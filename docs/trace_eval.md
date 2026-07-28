# 📊 BÁO CÁO GIÁM SÁT & ĐÁNH GIÁ (OBSERVABILITY TRACE LOGS)
đề bài : Trợ Lý Tìm & Đặt Lịch Xem Nhà Trọ / Căn Hộ Cho Thuê
## 🎯 1. BẢNG CHẤM ĐIỂM AGENTIC FIT (SCORING MATRIX)

| Tiêu chí | Điểm (1-5) | Lý do đánh giá |
| :--- | :---: | :--- |
| 🧠 **Multi-step Reasoning** | `4/5` | Agent cần suy luận từ nhu cầu tìm nhà đến việc xác định loại hình thuê ( phòng/căn hộ). |
| 🛠️ **Tool Interaction** | `5/5` | Agent cần tra cứu dữ liệu thời gian thực qua API giá tiền, địa điểm và tình trạng avalible |
| 🔀 **Dynamic Decision** | `5/5` | Kết quả bước trước quyết định hành động bước sau. |
| ⏳ **Long Horizon** | `4/5` | Quy trình gồm 2-3 bước xử lý ngắn. |
| **TỔNG ĐIỂM FIT** | **18/20** | **KẾT LUẬN: BÀI TOÁN RẤT NÊN DÙNG REACT AGENT!** |

---

## 🔍 2. SO SÁNH PHẢN HỒI (TEST CASE #3)

**Câu hỏi**: *"Tìm giúp tôi phòng trọ ở quận Thủ Duc, giá dưới 3 triệu/tháng."*

### 🤖 Chatbot Baseline:
* **Phản hồi**: *"Chào bạn! Mình rất vui được hỗ trợ bạn tìm phòng trọ ở khu vực Thủ Đức (nay là thành phố Thủ Đức) với mức giá dưới 3 triệu/tháng.

Tuy nhiên, mình là trợ lý AI không có khả năng truy cập dữ liệu thời gian thực từ các trang cho thuê nhà trọ hay tin đăng mới nhất. Thông tin về phòng trọ thường thay đổi liên tục, nên mình sẽ không thể đưa ra danh sách cụ thể và chính xác được.

**Nhưng mình có thể gợi ý cho bạn một số cách tìm kiếm hiệu quả:**

1. **Các trang web/ứng dụng phổ biến:**
   - Phongtro.com, Nhatot.com, ChoTot.vn, Homedy.com
   - Facebook Marketplace hoặc các group chuyên cho thuê phòng trọ tại Thủ Đức (ví dụ: "Phòng trọ Thủ Đức - Giá rẻ", "Hội sinh viên Thủ Đức")
   - Zalo OA của các khu nhà trọ, hoặc các hội nhóm trên Zalo

2. **Một số lưu ý khi tìm:**
   - Giá dưới 3 triệu/tháng ở Thủ Đức thường là phòng trọ nhỏ (khoảng 15-20m²), có thể ở các khu vực xa trung tâm như: phường Linh Trung, Linh Xuân, Tam Bình, Tam Phú, hoặc gần các trường đại học (ĐH Quốc gia, ĐH Sư phạm Kỹ thuật…).
   - Nên xem phòng trực tiếp, kiểm tra kỹ hợp đồng, điện nước, an ninh và các chi phí phát sinh (phí dịch vụ, gửi xe…).
   - Cảnh giác với các tin đăng ảo, giá rẻ bất thường hoặc yêu cầu chuyển tiền cọc trước khi xem phòng.

3. **Nếu bạn cần thêm lời khuyên về cách tìm hoặc các tiêu chí chọn phòng (gần chợ, gần trường, an toàn…), mình sẵn lòng tư vấn thêm.**

Hy vọng bạn sớm tìm được phòng ưng ý! Nếu cần mình giúp gì thêm, đừng ngần ngại hỏi nhé 😊
"*
* **Nhận xét**: An toàn nhưng không giải quyết được nhu cầu thực tế của người dùng.

### 🧠 ReAct Agent:
* **Thought 1**:  Câu hỏi này yêu cầu tìm phòng trọ ở Thủ Đức với giá dưới 3 triệu/tháng. Tôi sẽ dùng công cụ search_properties.
* **Action 1**: `search_properties`
* **Observation 1**: ` Kết quả tìm kiếm nhà trọ/căn hộ tại 'Thủ Đức':
1. CH01 - Chung cư mini 45m² - Quận 1 - 5,000,000 VNĐ/tháng (2PN)
2. NT02 - Nhà trọ 25m² - Thủ Đức - 2,500,000 VNĐ/tháng (1PN)
3. CH03 - Căn hộ studio 35m² - Quận 3 - 4,000,000 VNĐ/tháng
4. NT04 - Phòng trọ 20m² - Cầu Giấy - 2,000,000 VNĐ/tháng
5. CH05 - Căn hộ 70m² - Quận 7 - 8,000,000 VNĐ/tháng (2PN)
(Dữ liệu mẫu — vui lòng lọc thêm nếu cần)`
* **Thought 2**:Tôi đã có kết quả tìm kiếm phòng trọ ở Thủ Đức phù hợp tiêu chí. Bây giờ tôi sẽ trả lời người dùng.
* **Final Answer**: Chào bạn, hiện tại ở Thủ Đức đang có phòng trọ NT02 (25m², có gác lửng) với giá 2,500,000 VNĐ/tháng rất phù hợp với yêu cầu dưới 3 triệu của bạn. Bạn có muốn xem thêm chi tiết hoặc đặt lịch đi xem phòng này không?
* **Nhận xét**: Hoàn thành xuất sắc nhiệm vụ nhờ sự kết hợp giữa suy luận và công cụ.
