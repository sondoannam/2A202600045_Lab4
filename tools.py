FLIGHTS_DB = {
    ("Hà Nội", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": 
"07:20", "price": 1_450_000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "14:00", "arrival": 
"15:20", "price": 2_800_000, "class": "business"},
        {"airline": "VietJet Air", "departure": "08:30", "arrival": "09:50", "price": 890_000,   "class": "economy"},
        {"airline": "Bamboo Airways",   "departure": "11:00", "arrival": "12:20", "price": 1_200_000, "class": "economy"},
    ],
    ("Hà Nội", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "07:00", "arrival": "09:15", "price": 2_100_000, "class": "economy"},
        {"airline": "VietJet Air",      "departure": "10:00", "arrival": "12:15", "price": 1_350_000, "class": "economy"},
        {"airline": "VietJet Air",      "departure": "16:00", "arrival": "18:15", "price": 1_100_000, "class": "economy"},
    ],
    ("Hà Nội", "Hồ Chí Minh"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "08:10", "price": 1_600_000, "class": "economy"},
        {"airline": "VietJet Air",      "departure": "07:30", "arrival": "09:40", "price": 950_000,   "class": "economy"},
        {"airline": "Bamboo Airways",   "departure": "12:00", "arrival": "14:10", "price": 1_300_000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "18:00", "arrival": "20:10", "price": 3_200_000, "class": "business"},
    ],
    ("Hồ Chí Minh", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "09:00", "arrival": "10:20", "price": 1_300_000, "class": "economy"},
        {"airline": "VietJet Air",      "departure": "13:00", "arrival": "14:20", "price": 780_000,   "class": "economy"},
    ],
    ("Hồ Chí Minh", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "08:00", "arrival": "09:00", "price": 1_100_000, "class": "economy"},
        {"airline": "VietJet Air",      "departure": "15:00", "arrival": "16:00", "price": 650_000,   "class": "economy"},
    ],
}

HOTELS_DB = {
    "Đà Nẵng": [
    {"name": "Mường Thanh Luxury",    "stars": 5, "price_per_night": 1_800_000, "area": "Mỹ Khê",       "rating": 4.5},
        {"name": "Sala Danang Beach",    "stars": 4, "price_per_night": 1_200_000, "area": "Mỹ Khê",       "rating": 4.3},
        {"name": "Fivitel Danang",       "stars": 3, "price_per_night": 650_000,   "area": "Sơn Trà",      "rating": 4.1},
        {"name": "Memory Hostel",        "stars": 2, "price_per_night": 250_000,   "area": "Hải Châu",     "rating": 4.6},
        {"name": "Christina's Homestay", "stars": 2, "price_per_night": 350_000,   "area": "An Thượng",    "rating": 4.7},
    ],
    "Phú Quốc": [
        {"name": "Vinpearl Resort",      "stars": 5, "price_per_night": 3_500_000, "area": "Bãi Dài",      "rating": 4.4},
        {"name": "Sol by Meliá",         "stars": 4, "price_per_night": 1_500_000, "area": "Bãi Trường",   "rating": 4.2},
        {"name": "Lahana Resort",        "stars": 3, "price_per_night": 800_000,   "area": "Dương Đông",   "rating": 4.0},
        {"name": "9Station Hostel",      "stars": 2, "price_per_night": 200_000,   "area": "Dương Đông",   "rating": 4.5},
    ],
    "Hồ Chí Minh": [
        {"name": "Rex Hotel",            "stars": 5, "price_per_night": 2_800_000, "area": "Quận 1",       "rating": 4.3},
        {"name": "Liberty Central",      "stars": 4, "price_per_night": 1_400_000, "area": "Quận 1",       "rating": 4.1},
        {"name": "Cochin Zen Hotel",     "stars": 3, "price_per_night": 550_000,   "area": "Quận 3",       "rating": 4.4},
        {"name": "The Common Room",      "stars": 2, "price_per_night": 180_000,   "area": "Quận 1",       "rating": 4.6},
    ],
}

from langchain_core.tools import tool

@tool
def search_flights(origin: str, destination: str) -> str:
    """Tìm kiếm các chuyến bay giữa hai thành phố.
    Tham số:
    origin: thành phố khởi hành (VD: 'Hà Nội', 'Hồ Chí Minh')
    destination: thành phố đến (VD: 'Đà Nẵng', 'Phú Quốc')
    """
    # Xử lý logic tìm chuyến bay trực tiếp hoặc tra ngược [cite: 209, 213]
    flights = FLIGHTS_DB.get((origin, destination))
    if not flights:
        flights = FLIGHTS_DB.get((destination, origin))
        
    if not flights:
        return f"Không tìm thấy chuyến bay từ {origin} đến {destination}." [cite: 214]

    result_lines = [f"Danh sách chuyến bay {origin} - {destination}:"]
    for f in flights:
        # Format giá tiền có dấu chấm [cite: 215]
        price_str = f"{f['price']:,}".replace(",", ".") + "₫"
        result_lines.append(f"- Hãng: {f['airline']}, Giờ: {f['departure']} - {f['arrival']}, Giá: {price_str}, Hạng: {f['class']}")
    
    return "\n".join(result_lines)

@tool
def search_hotels(city: str, max_price_per_night: int = 99999999) -> str:
    """Tìm kiếm khách sạn tại một thành phố, có thể lọc theo giá tối đa mỗi đêm.
    Tham số:
    city: tên thành phố
    max_price_per_night: giá tối đa mỗi đêm (VNĐ)
    """
    hotels = HOTELS_DB.get(city)
    if not hotels:
        return f"Không có dữ liệu khách sạn tại {city}."
    
    # Lọc theo giá và sắp xếp theo rating giảm dần [cite: 226, 228]
    filtered_hotels = [h for h in hotels if h['price_per_night'] <= max_price_per_night]
    filtered_hotels.sort(key=lambda x: x['rating'], reverse=True)

    if not filtered_hotels:
        return f"Không tìm thấy khách sạn tại {city} với giá dưới {max_price_per_night:,}₫/đêm. Hãy thử tăng ngân sách."

    result_lines = [f"Danh sách khách sạn tại {city} (Giá <= {max_price_per_night:,}₫):"]
    for h in filtered_hotels:
        price_str = f"{h['price_per_night']:,}".replace(",", ".") + "₫"
        result_lines.append(f"- {h['name']} ({h['stars']} sao, Khu {h['area']}) - Rating: {h['rating']} - Giá: {price_str}/đêm")
        
    return "\n".join(result_lines)

@tool
def calculate_budget(total_budget: int, expenses: str) -> str:
    """Tính toán ngân sách còn lại sau khi trừ các khoản chi phí.
    Tham số:
    total_budget: tổng ngân sách ban đầu (VNĐ)
    expenses: chuỗi mô tả các khoản chi (VD: 'vé máy bay: 890000, khách sạn: 650000')
    """
    try:
        # Parse chuỗi expenses thành dict [cite: 246]
        expense_items = {}
        items = expenses.split(',')
        for item in items:
            name, cost_str = item.split(':')
            expense_items[name.strip().capitalize()] = int(cost_str.strip())
            
        # Tính toán chi phí [cite: 247, 254]
        total_expense = sum(expense_items.values())
        remaining = total_budget - total_expense
        
        # Format bảng chi tiết [cite: 248]
        result_lines = ["Bảng chi phí:"]
        for name, cost in expense_items.items():
            cost_str = f"{cost:,}".replace(",", ".") + "₫"
            result_lines.append(f"- {name}: {cost_str}")
            
        result_lines.append("-" * 20)
        result_lines.append(f"Tổng chi: {f'{total_expense:,}'.replace(',', '.')}₫")
        result_lines.append(f"Ngân sách: {f'{total_budget:,}'.replace(',', '.')}₫")
        result_lines.append(f"Còn lại: {f'{remaining:,}'.replace(',', '.')}₫")
        
        if remaining < 0:
            result_lines.append(f"⚠️ Vượt ngân sách {f'{abs(remaining):,}'.replace(',', '.')}₫! Cần điều chỉnh.") [cite: 270]
            
        return "\n".join(result_lines)
    except Exception as e:
        # Xử lý lỗi format sai [cite: 266, 271]
        return f"Lỗi tính toán: Định dạng chi phí đầu vào sai. Hãy đảm bảo format dạng 'tên: số tiền, tên: số tiền'. Lỗi chi tiết: {str(e)}"