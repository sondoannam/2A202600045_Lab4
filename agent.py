from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage
from tools import search_flights, search_hotels, calculate_budget
from dotenv import load_dotenv

load_dotenv()

# 1. Đọc System Prompt
with open("system_prompt.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

# 2. Khai báo State
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

# 3. Khởi tạo LLM và Tools
def get_llm_model(provider: str = "gemini"):
    if provider == "openai":
        # Khởi tạo mô hình của OpenAI
        return init_chat_model(
            model="gpt-4o-mini", 
            model_provider="openai"
        )
    elif provider == "gemini":
        # Khởi tạo mô hình Gemini 3 Flash Preview
        return init_chat_model(
            model="gemini-3-flash-preview", 
            model_provider="google_genai"
        )
    else:
        raise ValueError(f"Cảnh báo: Provider {provider} chưa được hỗ trợ!")

tools_list = [search_flights, search_hotels, calculate_budget]
llm = get_llm_model(provider="gemini")
llm_with_tools = llm.bind_tools(tools_list)

# 4. Agent Node
def agent_node(state: AgentState):
    messages = state["messages"]
    if not isinstance(messages[0], SystemMessage):
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + messages
    
    response = llm_with_tools.invoke(messages)

    # === LOGGING ===
    if response.tool_calls:
        for tc in response.tool_calls:
            print(f"  [Log] Gọi tool: {tc['name']}({tc['args']})")
    else:
        print(f"  [Log] Trả lời trực tiếp")
        
    return {"messages": [response]}

# 5. Xây dựng Graph
builder = StateGraph(AgentState)

builder.add_node("agent", agent_node)
tool_node = ToolNode(tools_list)
builder.add_node("tools", tool_node)

# Đã giải quyết TODO khai báo edges
builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", tools_condition)
builder.add_edge("tools", "agent")

graph = builder.compile()

# 6. Chat loop
if __name__ == "__main__":
    print("=" * 60)
    print("TravelBuddy - Trợ lý Du lịch Thông minh")
    print(" Gõ 'quit' để thoát")
    print("=" * 60)

    while True:
        user_input = input("\nBạn: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            break
            
        print("\nLemme think...")
        result = graph.invoke({"messages": [("human", user_input)]})
        
        final = result["messages"][-1]
        print(f"\nTravelBuddy: {final.content}")