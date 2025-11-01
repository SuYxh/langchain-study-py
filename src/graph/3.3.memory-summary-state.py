import os
import datetime
from dotenv import load_dotenv
from langchain_core.tools import tool
from langmem.short_term import SummarizationNode
from langchain_core.messages.utils import trim_messages, count_tokens_approximately
from langgraph.checkpoint.memory import InMemorySaver

from langgraph.prebuilt.chat_agent_executor import AgentState

from utils import print_agent_response_analysis
from llm import create_siliconflow_model

from typing import Annotated
from langgraph.prebuilt import InjectedState, create_react_agent


class CustomState(AgentState):
    user_id: str


@tool(return_direct=False)
def get_user_info(state: Annotated[CustomState, InjectedState]) -> str:
    """查询⽤户信息."""
    user_id = state["user_id"]
    return "user_123⽤户的姓名： dahuang。" if user_id == "user_123" else "未知⽤户"


# 创建模型实例
model = create_siliconflow_model("Qwen/Qwen3-8B")
# model = create_siliconflow_model("deepseek-ai/DeepSeek-R1-Distill-Qwen-7B")


checkpointer = InMemorySaver()


agent = create_react_agent(
    model=model,
    tools=[get_user_info],
    state_schema=CustomState,
)

# Run the agent
response = agent.invoke({"messages": "查询⽤户信息", "user_id": "user_123"})

print_agent_response_analysis(
    response,
    show_conversation_flow=True,  # 显示对话流程
    show_token_usage=True,  # 显示token消耗
    show_tool_results=True,  # 显示工具结果
    show_summary=True,
)  # 显示汇总信息
