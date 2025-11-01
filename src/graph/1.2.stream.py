import os
import ssl
import httpx
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model

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


agent = create_react_agent(
    model=model,
    tools=[],
    prompt="You are a helpful assistant",
)

# agent.invoke(
#     {"messages": [{"role": "user", "content": "你是谁？能帮我解决什么问题？"}]}
# )

print("=== LangGraph流式输出说明 ===")
print("LangGraph的stream()方法有几种不同的模式：")
print("1. 默认模式：返回每个节点的完整状态更新")
print("2. messages模式：返回消息级别的更新")
print("3. updates模式：返回增量更新")
print("\n注意：真正的逐字符流式输出需要模型本身支持streaming")
print("\n" + "=" * 60)

print("\n=== 默认模式（节点状态更新）===")
for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "请用一句话介绍你自己"}]}
):
    node_name = list(chunk.keys())[0]
    print(f"\n节点 '{node_name}' 完成处理")
    if "messages" in chunk[node_name]:
        last_message = chunk[node_name]["messages"][-1]
        if hasattr(last_message, "content"):
            print(f"回复: {last_message.content[:100]}...")

print("\n" + "=" * 60)
print("\n=== Messages模式（消息级别更新）===")
print("AI回复: ", end="", flush=True)

for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "请简单说说你能做什么"}]},
    stream_mode="messages",
):
    message, metadata = chunk
    if hasattr(message, "content") and message.content:
        # 这里仍然是完整消息，不是逐字符流式
        # 真正的逐字符流式需要模型API支持
        print(message.content)
        break  # 只显示第一个AI消息

print("\n" + "=" * 60)
print("\n=== 为什么看起来不是'流式'？===")
print("1. LangGraph的stream主要用于多步骤工作流的状态跟踪")
print("2. 每个chunk是一个完整的状态更新，不是逐字符生成")
print("3. 要实现逐字符流式，需要：")
print("   - 模型API支持streaming=True")
print("   - 使用model.stream()而不是agent.stream()")
print("   - 或者自定义Agent实现")

print("\n=== 真正的流式输出示例（直接调用模型）===")
print("AI回复: ", end="", flush=True)

# 直接使用模型的流式功能
try:
    for chunk in model.stream("请用一句话介绍你自己"):
        if hasattr(chunk, "content") and chunk.content:
            print(chunk.content, end="", flush=True)
except Exception as e:
    print(f"\n模型流式输出失败: {e}")
    print("\n使用普通调用:")
    response = model.invoke("请用一句话介绍你自己")
    print(response.content)

print("\n\n" + "=" * 60)
print("总结：LangGraph的stream()主要用于工作流状态跟踪，")
print("而不是逐字符的文本生成流式输出。")
