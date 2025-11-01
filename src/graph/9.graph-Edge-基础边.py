"""LangGraph 基础边案例

这个案例展示了如何在 LangGraph 中使用基础边来连接节点，
创建一个简单的线性工作流。
"""

from typing import TypedDict
from langchain_core.runnables import RunnableConfig
from langgraph.constants import START, END
from langgraph.graph import StateGraph


# 定义状态结构
class State(TypedDict):
    message: str
    count: int
    processed: bool


# 节点1：初始化处理
def initialize_node(state: State, config: RunnableConfig) -> State:
    """初始化节点 - 设置初始状态"""
    print(f"🚀 初始化节点: 接收到消息 '{state['message']}'")
    return {"message": f"处理中: {state['message']}", "count": 1, "processed": False}


# 节点2：数据处理
def process_node(state: State, config: RunnableConfig) -> State:
    """处理节点 - 执行主要逻辑"""
    print(f"⚙️ 处理节点: 当前计数 {state['count']}")
    return {
        "message": state["message"].replace("处理中", "已处理"),
        "count": state["count"] + 1,
        "processed": True,
    }


# 节点3：最终化处理
def finalize_node(state: State, config: RunnableConfig) -> State:
    """最终化节点 - 完成处理"""
    print(f"✅ 最终化节点: 完成处理，最终计数 {state['count']}")
    return {
        "message": f"完成: {state['message']}",
        "count": state["count"] + 1,
        "processed": True,
    }


# 创建状态图
builder = StateGraph(State)

# 添加节点
builder.add_node("initialize", initialize_node)
builder.add_node("process", process_node)
builder.add_node("finalize", finalize_node)

# 添加基础边 - 创建线性工作流
# START -> initialize -> process -> finalize -> END
builder.add_edge(START, "initialize")  # 从开始点到初始化节点
builder.add_edge("initialize", "process")  # 从初始化到处理节点
builder.add_edge("process", "finalize")  # 从处理到最终化节点
builder.add_edge("finalize", END)  # 从最终化节点到结束点

# 编译图
graph = builder.compile()


def main():
    """主函数 - 演示基础边的使用"""
    print("=== LangGraph 基础边案例演示 ===")
    print("\n📋 工作流程: START -> initialize -> process -> finalize -> END\n")

    # 初始输入
    initial_state = {"message": "Hello LangGraph", "count": 0, "processed": False}

    print(f"📥 输入状态: {initial_state}\n")

    # 执行图
    result = graph.invoke(initial_state)

    print(f"\n📤 最终结果: {result}")
    print("\n=== 基础边案例完成 ===")


if __name__ == "__main__":
    main()
