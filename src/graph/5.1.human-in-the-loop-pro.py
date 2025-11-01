import os
import datetime
from dotenv import load_dotenv
from langchain_core.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import create_react_agent
from utils import print_agent_response_analysis
from llm import create_siliconflow_model
from langchain_core.runnables import RunnableConfig
from langgraph.config import get_store
from langgraph.store.memory import InMemoryStore
from langgraph.types import interrupt, Command

# 创建模型实例
model = create_siliconflow_model("Qwen/Qwen3-8B")


# An example of a sensitive tool that requires human review / approval
@tool(return_direct=True)
def book_hotel(hotel_name: str):
    """预定宾馆"""
    response = interrupt(
        f"正准备执行'book_hotel'工具预定宾馆，相关参数名： {{'hotel_name': {hotel_name}}}. "
        "请选择OK，表示同意，或者选择edit，提出补充意见."
    )
    if response["type"] == "OK":
        return f"成功在 {hotel_name} 预定了一个房间."
    elif response["type"] == "edit":
        hotel_name = response["args"]["hotel_name"]
        return f"成功在 {hotel_name} 预定了一个房间."
    else:
        raise ValueError(f"Unknown response type: {response['type']}")


checkpointer = InMemorySaver()

agent = create_react_agent(
    model=model,
    tools=[book_hotel],
    checkpointer=checkpointer,
)

config = {"configurable": {"thread_id": "1"}}

print("=== 第一次调用：触发人工干预 ===")
for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "帮我在图灵宾馆预定一个房间"}]}, config
):
    print(f"节点: {list(chunk.keys())}")
    for node_name, node_data in chunk.items():
        if "messages" in node_data:
            last_message = node_data["messages"][-1]
            if hasattr(last_message, "content") and last_message.content:
                print(f"{node_name} 输出: {last_message.content}")
    print("-" * 50)

print("\n=== 第二次调用：人工干预响应 ===")
try:
    for chunk in agent.stream(
        # 选择一个响应类型
        # Command(resume={"type": "OK"}),  # 同意原始请求
        Command(
            resume={"type": "edit", "args": {"hotel_name": "三号宾馆"}}
        ),  # 修改酒店名称
        config,
    ):
        print(f"节点: {list(chunk.keys())}")
        for node_name, node_data in chunk.items():
            if "messages" in node_data:
                last_message = node_data["messages"][-1]
                if hasattr(last_message, "content") and last_message.content:
                    print(f"{node_name} 输出: {last_message.content}")
        print("-" * 50)
except Exception as e:
    print(f"执行出错: {e}")

print("\n=== 检查最终状态 ===")
# 获取最终的对话状态
final_state = agent.get_state(config)
if final_state.values.get("messages"):
    final_message = final_state.values["messages"][-1]
    print(f"最终结果: {final_message.content}")
