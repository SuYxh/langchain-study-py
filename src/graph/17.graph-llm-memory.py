import os
import datetime
from dotenv import load_dotenv
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from utils import print_agent_response_analysis
from llm import create_siliconflow_model
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.checkpoint.memory import InMemorySaver

# 创建模型实例
model = create_siliconflow_model("Qwen/Qwen3-8B")
# model = create_siliconflow_model("deepseek-ai/DeepSeek-R1-Distill-Qwen-7B")


def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": response}


builder = StateGraph(MessagesState)

builder.add_node(call_model)

builder.add_edge(START, "call_model")

checkpointer = InMemorySaver()
graph = builder.compile(checkpointer=checkpointer)

config = {"configurable": {"thread_id": "1"}}

for chunk in graph.stream(
    {"messages": [{"role": "user", "content": "湖南的省会是哪里？"}]},
    config,
    stream_mode="values",
):
    chunk["messages"][-1].pretty_print()

for chunk in graph.stream(
    {"messages": [{"role": "user", "content": "湖北呢？"}]},
    config,
    stream_mode="values",
):
    chunk["messages"][-1].pretty_print()
