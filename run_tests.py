import json
from agent import graph
from langchain_core.messages import AIMessage

# Danh sách 5 kịch bản thử thách Khí linh
test_cases = [
    ("Test 1: Direct Answer (Không cần tool)", "Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu."),
    ("Test 2: Single Tool Call", "Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng"),
    ("Test 3: Multi-Step Tool Chaining", "Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!"),
    ("Test 4: Missing Info / Clarification", "Tôi muốn đặt khách sạn"),
    ("Test 5: Guardrail / Refusal", "Giải giúp tôi bài tập lập trình Python về linked list")
]

def run_all_tests():
    print("Khởi động kiểm thử tự động...")
    
    with open("test_results.md", "w", encoding="utf-8") as f:
        f.write("# Báo Cáo Kiểm thử TravelBuddy (Lab 4)\n\n")
        
        for name, prompt in test_cases:
            print(f"Đang chạy {name}...")
            f.write(f"## {name}\n")
            f.write(f"**Người dùng:** {prompt}\n\n")
            
            # Kích hoạt đồ thị với từng câu hỏi (truyền vào state mới hoàn toàn)
            result = graph.invoke({"messages": [("human", prompt)]})
            
            f.write("**Quá trình suy nghĩ & Trả lời:**\n")
            
            # Duyệt qua các luồng messages để ghi log
            for msg in result["messages"]:
                if isinstance(msg, AIMessage):
                    # Nếu model gọi tool, ghi lại tool đó
                    if msg.tool_calls:
                        for tc in msg.tool_calls:
                            args_str = json.dumps(tc['args'], ensure_ascii=False)
                            f.write(f"- *[Log] Kích hoạt tool:* `{tc['name']}({args_str})`\n")
                    
                    # Nội dung trả lời cho người dùng
                    if msg.content:
                        # Kiểm tra xem content có phải là chuỗi không
                        if isinstance(msg.content, str):
                            f.write(f"\n**TravelBuddy:**\n{msg.content}\n\n")
                        # Trường hợp content là một list
                        elif isinstance(msg.content, list):
                            for item in msg.content:
                                if isinstance(item, dict) and item.get('type') == 'text':
                                    f.write(f"\n**TravelBuddy:**\n{item['text']}\n\n")
            
            f.write("---\n\n")
            
    print("\nKiểm thử hoàn tất! Đã lưu kết quả vào: test_results.md.")

if __name__ == "__main__":
    run_all_tests()