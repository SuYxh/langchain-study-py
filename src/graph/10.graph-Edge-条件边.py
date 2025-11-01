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

# 如果不想在路由函数中写⼊过多具体的节点名称，也可以在函数中返回⼀个⾃定义的结果，然后将这个结果解析到某⼀个具体的Node上。例如
# def routing_func(state: State) -> bool:
#     if state["number"] > 5:
#         return True
#     else:
#         return False

# builder.add_conditional_edges(START, routing_func, {True: "node_a", False: "node_b"})


builder.add_conditional_edges(START, routing_func)
builder.add_edge("node1", END)

graph = builder.compile()
print(graph.invoke({"number": 7}))



