import os
import datetime
from dotenv import load_dotenv
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from utils import print_agent_response_analysis
from llm import create_siliconflow_model
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.checkpoint.memory import InMemorySaver
from operator import add
from langchain_core.messages import AnyMessage
from typing import Literal, TypedDict, Annotated
from langgraph.types import interrupt, Command
from langchain_core.messages import HumanMessage

# 创建模型实例
llm = create_siliconflow_model("Qwen/Qwen3-8B")
# model = create_siliconflow_model("deepseek-ai/DeepSeek-R1-Distill-Qwen-7B")


class State(TypedDict):
    messages: Annotated[list[AnyMessage], add]


def human_approval(state: State) -> Command[Literal["call_llm", END]]:
    is_approved = interrupt({"question": "是否同意调用大语言模型？"})

    if is_approved:
        return Command(goto="call_llm")
    else:
        return Command(goto=END)


def call_llm(state: State):
    response = llm.invoke(state["messages"])
    return {"messages": [response]}


builder = StateGraph(State)

# Add the node to the graph in an appropriate location
# and connect it to the relevant nodes.
builder.add_node("human_approval", human_approval)
builder.add_node("call_llm", call_llm)

builder.add_edge(START, "human_approval")

checkpointer = InMemorySaver()

graph = builder.compile(checkpointer=checkpointer)


# 提交任务，等待确认
thread_config = {"configurable": {"thread_id": 1}}

graph.invoke({"messages": [HumanMessage("湖南的省会在哪里？")]}, config=thread_config)

# 执行后会中断任务，等待确认

# 确认同意，继续执⾏任务
# final_result = graph.invoke(Command(resume=True), config=thread_config)
# print(final_result)
# 不同意，终⽌任务
final_result = graph.invoke(Command(resume=False), config=thread_config)
print(final_result)
