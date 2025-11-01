from langchain_core.messages import AnyMessage, AIMessage
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from typing import Annotated, TypedDict
from operator import add


# TypedDict 基类
# - State 继承自 TypedDict ，这是 Python 的类型提示工具
# - 提供了字典的结构化类型定义，确保状态字段的类型安全
# - 在运行时仍然是普通字典，但在开发时提供类型检查


# Annotated 类型注解
# Annotated[类型, 合并函数] 是 LangGraph 的核心机制：
# 作用 ：定义字段类型和状态合并策略
class State(TypedDict):
    # 消息列表
    # - 类型 ： list[AnyMessage] - 消息列表
    # - 合并策略 ： add_messages - LangGraph 内置的消息合并函数
    # - 行为 ：新消息会追加到现有消息列表末尾
    # - 用途 ：存储对话历史，是 LangGraph 中最常用的字段
    messages: Annotated[list[AnyMessage], add_messages]
    # 整数列表
    # - 类型 ： list[int] - 整数列表
    # - 合并策略 ： add - Python 内置的加法操作符
    # - 行为 ：新列表会与现有列表合并（相当于 list1 + list2 ）
    # - 用途 ：演示自定义列表字段的合并
    list_field: Annotated[list[int], add]
    # - 类型 ： int - 整数
    # - 合并策略 ：无（默认覆盖）
    # - 行为 ：新值直接覆盖旧值
    # - 用途 ：存储简单的状态值
    extra_field: int


def node1(state: State):
    new_message = AIMessage("Hello!")
    return {"messages": [new_message], "list_field": [10], "extra_field": 10}


def node2(state: State):
    new_message = AIMessage("LangGraph!")
    return {"messages": [new_message], "list_field": [20], "extra_field": 20}


graph = (
    StateGraph(State)
    .add_node("node1", node1)
    .add_node("node2", node2)
    .set_entry_point("node1")
    .add_edge("node1", "node2")
    .compile()
)
input_message = {"role": "user", "content": "Hi"}
result = graph.invoke({"messages": [input_message], "list_field": [1, 2, 3]})

print(result)
