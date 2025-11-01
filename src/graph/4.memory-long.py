import os
import datetime
from dotenv import load_dotenv
from langchain_core.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import create_react_agent
from utils import print_agent_response_analysis
from llm import create_siliconflow_model
from langchain_core.runnables import RunnableConfig
from langgraph.config import get_store
from langgraph.store.memory import InMemoryStore


# 定义⻓期存储, 是不是可以存在数据库中
store = InMemoryStore()
# 添加⼀些测试数据。 users是命名空间，user_123是key，后⾯的JSON数据是value
store.put(
    ("users",),
    "user_123",
    {
        "name": "dahuang",
        "age": "18",
    },
)


# 定义⼯具
@tool(return_direct=False)
def get_user_info(config: RunnableConfig) -> str:
    """查找⽤户信息"""
    # 获取⻓期存储。获取到了后，这个存储组件可读也可写
    store = get_store()

    # 获取配置中的⽤户ID
    user_id = config["configurable"].get("user_id")
    user_info = store.get(("users",), user_id)
    return str(user_info.value) if user_info else "Unknown user"


# 创建模型实例
model = create_siliconflow_model("Qwen/Qwen3-8B")
# model = create_siliconflow_model("deepseek-ai/DeepSeek-R1-Distill-Qwen-7B")

checkpointer = InMemorySaver()


agent = create_react_agent(model=model, tools=[get_user_info], store=store)

# Run the agent
response = agent.invoke(
    {"messages": [{"role": "user", "content": "查找⽤户信息"}]},
    config={"configurable": {"user_id": "user_123"}},
)

print_agent_response_analysis(response)
