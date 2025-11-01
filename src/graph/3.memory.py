import os
import datetime
from dotenv import load_dotenv
from langchain_core.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import create_react_agent
from utils import print_agent_response_analysis
from llm import create_siliconflow_model

# 创建模型实例
model = create_siliconflow_model("Qwen/Qwen3-8B")
# model = create_siliconflow_model("deepseek-ai/DeepSeek-R1-Distill-Qwen-7B")

checkpointer = InMemorySaver()


def get_weather(city: str) -> str:
    """获取某个城市的天⽓"""
    return f"城市：{city}，天⽓⼀直都是晴天！"


# 定义⼯具 注意要添加注释
@tool
def get_current_date():
    """获取今天⽇期"""
    return datetime.datetime.today().strftime("%Y-%m-%d")


agent = create_react_agent(
    model=model,
    tools=[get_current_date, get_weather],
    checkpointer=checkpointer,
)

# Run the agent
config = {"configurable": {"thread_id": "1"}}
cs_response = agent.invoke(
    {"messages": [{"role": "user", "content": "⻓沙天⽓怎么样？"}]}, config
)

print_agent_response_analysis(cs_response)

# Continue the conversation using the same thread_id
bj_response = agent.invoke(
    {"messages": [{"role": "user", "content": "我之前的问题是什么"}]}, config
)

print_agent_response_analysis(bj_response)
