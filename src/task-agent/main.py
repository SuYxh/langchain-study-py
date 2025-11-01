from operator import add
from typing import TypedDict, Annotated
from langchain_core.messages import AnyMessage, HumanMessage
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.config import get_stream_writer
from langchain_community.chat_models import ChatTongyi
from config.Load_key import Load_key

# 定义状态
class State(TypedDict):
    messages: Annotated[list[AnyMessage], add]
    type: str

# 初始化大模型
llm = ChatTongyi(
    model="qwen-plus",
    api_key=Load_key("QWEN_API_KEY")
)

# 路由函数
def routing_func(state: State):
    if state["type"] == "travel":
        return "travel_node"
    elif state["type"] == "joke":
        return "joke_node"
    elif state["type"] == "couplet":
        return "couplet_node"
    elif state["type"] == "other":
        return "other_node"
    elif state["type"] == END:
        return END
    else:
        return "other_node"

# Supervisor节点
def supervisor_node(state: State):
    writer = get_stream_writer()
    writer({"node": ">>>> supervisor_node"})
    
    if "type" in state:
        writer({"supervisor_step": f"已获得{state['type']} 智能体处理结果"})
        return {"type": END}
    else:
        prompt = """你是一个专业的客服助手，负责对用户的问题进行分类，并将任务分给其他Agent执行。
        如果用户的问题是和旅游路线规划相关的，那就返回 travel。
        如果用户的问题是希望讲一个笑话，那就返回 joke。
        如果用户的问题是希望对一个对联，那就返回 couplet。
        如果是其他的问题，返回 other。
        除了这几个选项外，不要返回任何其他的内容。"""
        
        prompts = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": state["messages"][0].content}
        ]
        
        response = llm.invoke(prompts)
        type_res = response.content
        writer({"supervisor_step": f"问题分类结果: {type_res}"})
        
        if type_res in ["travel", "joke", "couplet", "other"]:
            return {"type": type_res}
        else:
            raise ValueError("type is not in (travel, joke, other, couplet)")

# 其他节点（示例）
def other_node(state: State):
    writer = get_stream_writer()
    writer({"node": ">>>> other_node"})
    return {"messages": [HumanMessage(content="我暂时无法回答这个问题")], "type": "other"}

# 构建图
builder = StateGraph(State)
builder.add_node("supervisor_node", supervisor_node)
builder.add_node("travel_node", travel_node)
builder.add_node("joke_node", joke_node)
builder.add_node("couplet_node", couplet_node)
builder.add_node("other_node", other_node)

# 添加边
builder.add_edge(START, "supervisor_node")
builder.add_conditional_edges("supervisor_node", routing_func, path_map=["travel_node", "joke_node", "couplet_node", "other_node", END])
builder.add_edge("travel_node", "supervisor_node")
builder.add_edge("joke_node", "supervisor_node")
builder.add_edge("couplet_node", "supervisor_node")
builder.add_edge("other_node", "supervisor_node")

# 编译图
checkpointer = InMemorySaver()
graph = builder.compile(checkpointer=checkpointer)

# 测试
config = {"configurable": {"thread_id": "1"}}
for chunk in graph.stream({"messages": ["请给我讲一个郭德纲的笑话"]}, config, stream_mode="custom"):
    print(chunk)
