from typing import TypedDict
from langchain_core.runnables import RunnableConfig
from langgraph.constants import START, END
from langgraph.graph import StateGraph


# 配置状态
class State(TypedDict):
    number: int


def node_1(state: State, config: RunnableConfig):
    return {"number": state["number"] + 1}


builder = StateGraph(State)
# Node缓存5秒
builder.add_node("node1", node_1)


def routing_func(state: State) -> str:
    if state["number"] > 5:
        return "node1"
    else:
        return END


builder.add_conditional_edges(START, routing_func)
builder.add_edge("node1", END)

graph = builder.compile()
print(graph.invoke({"number": 7}))