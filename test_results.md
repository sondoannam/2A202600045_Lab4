# Báo Cáo Kiểm thử TravelBuddy (Lab 4)

## Test 1: Direct Answer (Không cần tool)
**Người dùng:** Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.

**Quá trình suy nghĩ & Trả lời:**

**TravelBuddy:**
Chào bạn! Thú vị quá! Bạn có thể cho mình biết một vài thông tin để giúp bạn dễ dàng hơn trong việc chọn địa điểm du lịch nhé? 

- Bạn muốn khám phá thành phố nào hay thiên nhiên, biển đảo?
- Có thời gian cụ thể nào không?
- Ngân sách của bạn khoảng bao nhiêu cho chuyến đi này?

Càng cụ thể mình càng dễ dàng giúp bạn lên kế hoạch tốt hơn!

---

## Test 2: Single Tool Call
**Người dùng:** Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng

**Quá trình suy nghĩ & Trả lời:**
- *[Log] Kích hoạt tool:* `search_flights({"origin": "Hà Nội", "destination": "Đà Nẵng"})`

**TravelBuddy:**
Dưới đây là danh sách các chuyến bay từ Hà Nội đi Đà Nẵng:

1. **Vietnam Airlines**
   - Giờ: 06:00 - 07:20
   - Giá: 1.450.000₫
   - Hạng: Economy

2. **Vietnam Airlines**
   - Giờ: 14:00 - 15:20
   - Giá: 2.800.000₫
   - Hạng: Business

3. **VietJet Air**
   - Giờ: 08:30 - 09:50
   - Giá: 890.000₫
   - Hạng: Economy

4. **Bamboo Airways**
   - Giờ: 11:00 - 12:20
   - Giá: 1.200.000₫
   - Hạng: Economy

Bạn muốn đặt chuyến bay nào không?

---

## Test 3: Multi-Step Tool Chaining
**Người dùng:** Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!

**Quá trình suy nghĩ & Trả lời:**
- *[Log] Kích hoạt tool:* `search_flights({"origin": "Hà Nội", "destination": "Phú Quốc"})`
- *[Log] Kích hoạt tool:* `search_hotels({"city": "Phú Quốc", "max_price_per_night": 2500000})`
- *[Log] Kích hoạt tool:* `calculate_budget({"total_budget": 5000000, "expenses": "vé máy bay: 1350000, khách sạn: 1600000"})`

**TravelBuddy:**
Dưới đây là tư vấn cho chuyến đi của bạn từ Hà Nội đến Phú Quốc trong 2 đêm:

**Chuyến bay:**
- Hãng: VietJet Air, Giờ: 10:00 - 12:15, Giá: 1.350.000₫, Hạng: economy

**Khách sạn:**
- **Sol by Meliá** (4 sao, Khu Bãi Trường) - Rating: 4.2 - Giá: 1.500.000₫/đêm (Tổng 2 đêm: 3.000.000₫)

**Tổng chi phí ước tính:**
- Vé máy bay: 1.350.000₫
- Khách sạn: 3.000.000₫
--------------------
Tổng chi: 4.350.000₫  
Ngân sách: 5.000.000₫  
Còn lại: 650.000₫  

**Gợi ý thêm:**
- Thời tiết ở Phú Quốc thường khá ấm và có nhiều nắng, bạn nhớ mang theo kem chống nắng và đồ bơi nhé.
- Ở Phú Quốc có nhiều món hải sản tươi ngon, đừng quên thưởng thức những món ăn đặc sản tại đây nhé!

---

## Test 4: Missing Info / Clarification
**Người dùng:** Tôi muốn đặt khách sạn

**Quá trình suy nghĩ & Trả lời:**

**TravelBuddy:**
Bạn có thể cho mình biết bạn muốn đặt khách sạn ở thành phố nào và ngân sách tối đa cho mỗi đêm là bao nhiêu không?

---

## Test 5: Guardrail / Refusal
**Người dùng:** Giải giúp tôi bài tập lập trình Python về linked list

**Quá trình suy nghĩ & Trả lời:**

**TravelBuddy:**
Ta là Trợ lý Du lịch, chỉ hỗ trợ bôn ba bốn bể, không can dự chuyện giang hồ này.

---

