import os
import datetime
from dotenv import load_dotenv
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from utils import print_agent_response_analysis
from llm import create_siliconflow_model

# 创建模型实例
model = create_siliconflow_model("Qwen/Qwen3-8B")
# model = create_siliconflow_model("deepseek-ai/DeepSeek-R1-Distill-Qwen-7B")


# 定义⼯具 注意要添加注释
@tool
def get_current_date():
    """获取今天⽇期"""
    return datetime.datetime.today().strftime("%Y-%m-%d")


agent = create_react_agent(
    model=model,
    tools=[get_current_date],
    prompt="You are a helpful assistant",
)

response = agent.invoke({"messages": [{"role": "user", "content": "今天是⼏⽉⼏号"}]})

print("模型回复:")
# 默认配置：只显示AI最终回复
# print_agent_response_analysis(response)

# 如需查看详细信息，可以使用以下参数：
print_agent_response_analysis(
    response,
    show_conversation_flow=True,  # 显示对话流程
    show_token_usage=True,  # 显示token消耗
    show_tool_results=True,  # 显示工具结果
    show_summary=True,
)  # 显示汇总信息
