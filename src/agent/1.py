from langchain_core.tools import StructuredTool
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
import os
import dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

dotenv.load_dotenv()

# 读取配置文件的信息
os.environ['TAVILY_API_KEY'] = os.getenv("TAVILY_API_KEY")


# 获取Tavily搜索工具的实例
search = TavilySearchResults(max_results=3)

# 获取一个搜索的工具
# 方式1：
# search_tool = StructuredTool.from_function(
#     func=search.run,
#     name="Search",
#     description="用于检索互联网上的信息",
# )

# 方式2：使用Tool
search_tool = Tool(
    func=search.run,
    name="Search",
    description="用于检索互联网上的信息",
)


# 获取大语言模型
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")

llm = ChatOpenAI(model_name='gpt-4o-mini', temperature=0)
# llm = ChatOpenAI(model_name='openai/gpt-oss-20b:free', temperature=0)
# llm = ChatOpenAI(model_name='qwen/qwen3-235b-a22b:free', temperature=0)


# 获取Agent的实例
agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION

# 获取AgentExecutor的实例
agent_executor = initialize_agent(
    tools = [search_tool],
    llm = llm,
    agent = agent,
    verbose = True, # 显示详细的日志信息
)


# 通过AgentExecutor 调用invoke(),并得到响应
result = agent_executor.invoke("langchain 目前最新版本是多少？ ")


# 处理响应数据
print(result)