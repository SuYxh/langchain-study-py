from typing import TypedDict
from langgraph.config import get_stream_writer
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    query: str
    answer: str


def node(state: State):
    writer = get_stream_writer()
    writer({"自定义key": "在节点内返回自定义信息"})
    return {"answer": "some data"}


def node2(state: State):
    writer = get_stream_writer()
    writer({"自定义key": "在节点内返回自定义信息2"})
    return {"answer": "some data"}


graph = (
    StateGraph(State)
    .add_node(node)
    .add_node(node2)
    .add_edge(START, "node")
    .add_edge("node", "node2")
    .add_edge("node2", END)
    .compile()
)

inputs = {"query": "example"}

# Usage
for chunk in graph.stream(inputs, stream_mode="custom"):
    print(chunk)
