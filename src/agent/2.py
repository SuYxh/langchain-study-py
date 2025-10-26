from langchain.agents import create_react_agent
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
# 获取Tavily搜索的实例
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType, create_tool_calling_agent, AgentExecutor
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
# 使用Tool
search_tool = Tool(
    func=search.run,
    name="Search",
    description="用于检索互联网上的信息",
)


# 获取大语言模型
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
)
# 提供提示词模板（以PromptTemplate为例）
template = """
Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}"""
prompt_template = PromptTemplate.from_template(
    template=template,
)

# 获取Agent的实例：create_react_agent()
agent = create_react_agent(
    llm=llm,
    prompt=prompt_template,
    tools=[search_tool]
)

# 获取AgentExecutor的实例
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool],
    verbose=True,
)


# 通过AgentExecutor的实例调用invoke(),得到响应
result = agent_executor.invoke({"input":"langchain 目前最新版本是多少？"})

# 处理响应
print(result)
