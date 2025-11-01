import os
import datetime
import asyncio
from dotenv import load_dotenv
from langchain_core.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import create_react_agent
from utils import print_agent_response_analysis
from llm import create_siliconflow_model
from langchain_core.runnables import RunnableConfig
from langgraph.config import get_store
from langgraph.store.memory import InMemoryStore
from langgraph.types import interrupt, Command
from langchain_mcp_adapters.client import MultiServerMCPClient


async def main():
    """主异步函数"""
    # 加载环境变量
    load_dotenv()

    # 创建支持异步的模型实例（解决SSL证书问题）
    import ssl
    import httpx
    from langchain.chat_models import init_chat_model

    # 解决SSL证书验证问题
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    # 创建异步HTTP客户端
    async_client = httpx.AsyncClient(verify=False, timeout=30.0)

    # 获取API密钥
    api_key = os.environ.get("SILICONFLOW_API_KEY")
    map_api_key = os.environ.get("AMAP_MAPS_API_KEY")

    if not api_key:
        raise ValueError("SILICONFLOW_API_KEY not found in environment variables.")

    # 创建模型
    model = init_chat_model(
        "Qwen/Qwen3-8B",
        model_provider="openai",
        base_url="https://api.siliconflow.cn/v1",
        api_key=api_key,
        http_async_client=async_client,  # 使用异步客户端
    )

    # 创建MCP客户端
    client = MultiServerMCPClient(
        {
            # 这个会有问题
            # "amap-amap-sse": {
            #     "url": f"https://mcp.amap.com/sse?key={map_api_key}",
            #     "transport": "streamable_http",
            # },
            "amap-maps": {
                "command": "npx",
                "args": ["-y", "@amap/amap-maps-mcp-server"],
                "env": {"AMAP_MAPS_API_KEY": map_api_key},
                "transport": "stdio",
            }
        }
    )

    # 获取工具
    tools = await client.get_tools()
    print(f"获取到 {len(tools)} 个工具")

    # 创建agent
    agent = create_react_agent(model=model, tools=tools)

    # 执行查询
    response = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "帮我规划一条从杭州富力中心到西湖的自驾路线",
                }
            ]
        }
    )

    # 打印响应分析
    print_agent_response_analysis(response)

    # 关闭客户端连接
    try:
        await client.close()
    except AttributeError:
        # MultiServerMCPClient 可能没有 close 方法
        pass
    await async_client.aclose()  # 关闭异步HTTP客户端


if __name__ == "__main__":
    # 运行异步主函数
    asyncio.run(main())
