import os
import ssl
import httpx
import datetime
from dotenv import load_dotenv
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model
from utils import print_agent_response_analysis

# 在项目根目录自动查找并加载 .env 文件, load_dotenv() 会把 .env 文件中的变量加载到 os.environ 中
load_dotenv()

# 直接从环境变量中获取 API_KEY
api_key = os.environ.get("SILICONFLOW_API_KEY")

if not api_key:
    print("api_key", api_key)
    raise ValueError(
        "SILICONFLOW_API_KEY not found in .env file or environment variables."
    )


# 解决SSL证书验证问题
# 创建一个不验证SSL证书的httpx客户端
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

custom_client = httpx.Client(verify=False, timeout=30.0)  # 禁用SSL验证

# 创建访问硅基流动的 Model
model = init_chat_model(
    "Qwen/Qwen3-8B",
    # "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B",
    model_provider="openai",
    base_url="https://api.siliconflow.cn/v1",
    api_key=api_key,
    http_client=custom_client,  # 使用自定义的httpx客户端
)

# 调用模型并打印结果
# response = model.invoke("你是谁？能帮我解决什么问题？")
# print("模型回复:")
# print(response.content)


# 定义⼯具 注意要添加注释
@tool
def get_current_date():
    """获取今天⽇期"""
    return datetime.datetime.today().strftime("%Y-%m-%d")


agent = create_react_agent(
    model=model,
    tools=[get_current_date],
    prompt="You are a helpful assistant",
)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "今天是⼏⽉⼏号"}]}
)

print("模型回复:")
# 默认配置：只显示AI最终回复
print_agent_response_analysis(response)

# 如需查看详细信息，可以使用以下参数：
# print_agent_response_analysis(response, 
#                             show_conversation_flow=True,  # 显示对话流程
#                             show_token_usage=True,        # 显示token消耗
#                             show_tool_results=True,       # 显示工具结果
#                             show_summary=True)            # 显示汇总信息
