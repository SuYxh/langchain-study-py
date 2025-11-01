import os
import datetime
import uuid
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
from typing_extensions import NotRequired



# 创建模型实例
llm = create_siliconflow_model("Qwen/Qwen3-8B")
# model = create_siliconflow_model("deepseek-ai/DeepSeek-R1-Distill-Qwen-7B")

class State(TypedDict):
    author: NotRequired[str]
    joke: NotRequired[str]

def author_node(state: State) -> dict:
    prompt = "帮我推荐一位受人们欢迎的作家。只需要给出作家的名字即可。"
    author = llm.invoke(prompt)
    return {"author": author}

def joke_node(state: State) -> dict:
    prompt = f"用作家：{state['author']} 的风格，写一个100字以内的笑话"
    joke = llm.invoke(prompt)
    return {"joke": joke}

builder = StateGraph(State)

builder.add_node("author_node", author_node)
builder.add_node("joke_node", joke_node)

builder.add_edge(START, "author_node")
builder.add_edge("author_node", "joke_node")
builder.add_edge("joke_node", END)

checkpointer = InMemorySaver()

graph = builder.compile(checkpointer=checkpointer)


config = {
    "configurable": {
        "thread_id": uuid.uuid4(),
    }
}

state = graph.invoke({}, config)

print(state["author"])

print()

print(state["joke"])


# 查看所有checkpoint检查点
states = list(graph.get_state_history(config))

for state in states:
    print(state.next)
    print(state.config["configurable"]["checkpoint_id"])
    print()

# 查看所有checkpoint检查点
# ()
# 1f0b70db-8264-62d2-8002-89ac323c93cf

# ('joke_node',)
# 1f0b70db-12a5-67d4-8001-3a0f48dc53af

# ('author_node',)
# 1f0b70da-b8da-6dda-8000-4744a94545fb

# ('__start__',)
# 1f0b70da-b8d8-6ee0-bfff-0f62eae934a3    


# 选定某⼀个检查点。这⾥选择author_node，让⼤模型重新推荐作家
selected_state = states[1]
print(selected_state.next)
print(selected_state.values)


# 为了后⾯的重演，更新state。可选步骤：
new_config = graph.update_state(selected_state.config, values={"author": "郭德纲"})
print(new_config)


# 接下来，指定thread_id和checkpoint_id，进⾏重演
res = graph.invoke(None,new_config)
print(res)