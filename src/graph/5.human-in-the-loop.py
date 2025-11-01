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

# from langgraph.types import Command

# 创建模型实例
model = create_siliconflow_model("Qwen/Qwen3-8B")
# model = create_siliconflow_model("deepseek-ai/DeepSeek-R1-Distill-Qwen-7B")


# An example of a sensitive tool that requires human review / approval
@tool(return_direct=True)
def book_hotel(hotel_name: str):
    """预定宾馆"""
    response = interrupt(
        f"正准备执⾏'book_hotel'⼯具预定宾馆，相关参数名： {{'hotel_name': {hotel_name}}}. "
        "请选择OK，表示同意，或者选择edit，提出补充意⻅."
    )
    if response["type"] == "OK":
        return f"成功在 {hotel_name} 预定了⼀个房间."
    elif response["type"] == "edit":
        hotel_name = response["args"]["hotel_name"]
    else:
        raise ValueError(f"Unknown response type: {response['type']}")
    return f"成功在 {hotel_name} 预定了⼀个房间."


checkpointer = InMemorySaver()

agent = create_react_agent(
    model=model,
    tools=[book_hotel],
    checkpointer=checkpointer,
)

config = {"configurable": {"thread_id": "1"}}


for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "帮我在图灵宾馆预定⼀个房间"}]}, config
):
    print(chunk)
    print("\n")

for chunk in agent.stream(
    # Command(resume={"type": "OK"}),
    Command(resume={"type": "edit", "args": {"hotel_name": "三号宾馆"}}),
    config,
):
    print(chunk)
    print(chunk["tools"]["messages"][-1].content)
    print("\n")
