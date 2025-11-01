import os
import datetime
from dotenv import load_dotenv
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from langgraph.prebuilt.tool_node import ToolNode
from utils import print_agent_response_analysis
from llm import create_siliconflow_model


# 创建模型实例
model = create_siliconflow_model("Qwen/Qwen3-8B")
# model = create_siliconflow_model("deepseek-ai/DeepSeek-R1-Distill-Qwen-7B")


# 定义工具 - 获取当前日期
@tool
def get_current_date():
    """获取今天日期"""
    return datetime.datetime.today().strftime("%Y-%m-%d")


# 定义工具 - 除法计算（return_direct=True 表示直接返回工具的结果）
# @tool("devide_tool", return_direct=True)
@tool("devide_tool", return_direct=False)
def devide(a: int, b: int) -> float:
    """计算两个整数的除法。

    Args:
        a (int): 被除数
        b (int): 除数

    Returns:
        float: 除法结果

    Raises:
        ValueError: 当除数为1时
        ZeroDivisionError: 当除数为0时
    """
    # 自定义错误
    if b == 1:
        raise ValueError("除数不能为1")
    if b == 0:
        raise ZeroDivisionError("除数不能为0")
    return a / b


# 打印工具信息
print(f"工具名称: {devide.name}")
print(f"工具描述: {devide.description}")
print(f"工具参数: {devide.args}")
print("-" * 50)


# 定义工具调用错误处理函数
def handle_tool_error(error: Exception) -> str:
    """处理工具调用错误。

    Args:
        error (Exception): 工具调用错误

    Returns:
        str: 错误处理消息
    """
    if isinstance(error, ValueError):
        return "除数为1没有意义，请重新输入一个除数和被除数。"
    elif isinstance(error, ZeroDivisionError):
        return "除数不能为0，请重新输入一个除数和被除数。"
    return f"工具调用错误：{error}"


# 创建带有错误处理的工具节点
tool_node = ToolNode([devide], handle_tool_errors=handle_tool_error)

# 创建带有错误处理的Agent
agent_with_error_handler = create_react_agent(model=model, tools=tool_node)


# 测试Agent调用
print("\n=== 测试Agent调用 ===")
result = agent_with_error_handler.invoke(
    {"messages": [{"role": "user", "content": "10除以1等于多少？"}]}
)

# 打印结果
print("\n=== 调用结果 ===")
# print(result)

# 可选：使用格式化输出
# print("\n=== 格式化输出 ===")
# print_agent_response_analysis(result)

# 如需查看详细信息，可以使用以下参数：
print_agent_response_analysis(
    result,
    show_conversation_flow=True,  # 显示对话流程
    show_token_usage=True,  # 显示token消耗
    show_tool_results=True,  # 显示工具结果
    show_summary=True,  # 显示汇总信息
)
