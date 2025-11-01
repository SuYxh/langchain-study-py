import asyncio
from mcp import MultiServerMCPClient

def travel_node(state: State):
    writer = get_stream_writer()
    writer({"node": ">>>> travel_node"})
    
    system_prompt = "你是一个专业的旅行规划助手，根据用户的问题，生成一个旅游路线规划。请用中文回答，并返回一个不超过100字的规划结果。"
    prompts = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": state["messages"][0].content}
    ]
    
    # MCP客户端配置
    client = MultiServerMCPClient(
        {
            "amap-maps": {
                "command": "npx",
                "args": ["@amap/amap-maps-mcp-server"],
                "env": {"AMAP_MAPS_API_KEY": "your_api_key"}
            }
        }
    )
    
    tools = asyncio.run(client.get_tools())
    agent = create_react_agent(llm, tools)
    response = agent.invoke({"messages": prompts})
    writer({"travel_result": response["messages"][-1].content})
    return {"messages": [HumanMessage(content=response["messages"][-1].content)], "type": "travel"}
