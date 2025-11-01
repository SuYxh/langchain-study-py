from langchain_core.runnables import RunnableConfig
from langgraph.constants import START, END
from langgraph.graph import StateGraph
from operator import add
from typing import TypedDict, Annotated
from langgraph.types import Send


# 配置状态
class State(TypedDict):
    messages: Annotated[list[str], add]


class PrivateState(TypedDict):
    msg: str


def node_1(state: PrivateState) -> State:
    res = state["msg"] + "!"
    return {"messages": [res]}


builder = StateGraph(State)
# Node缓存5秒
builder.add_node("node1", node_1)


def routing_func(state: State):
    result = []
    for message in state["messages"]:
        result.append(Send("node1", {"msg": message}))
    return result


# 通过路由函数，将消息中每个字符串分别传入node1处理。
# 第三个参数 ["node1"] 是可能的目标节点列表，用于：
# 1. 类型检查：确保路由函数返回的Send对象中的目标节点在此列表中
# 2. 图构建优化：LangGraph可以预先知道哪些节点可能被动态调用
# 3. 验证安全：防止路由到未声明的节点，避免运行时错误
builder.add_conditional_edges(START, routing_func, ["node1"])
builder.add_edge("node1", END)

graph = builder.compile()

print(graph.invoke({"messages": ["hello", "world", "hello", "graph"]}))
