# 引入依赖包
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
import os
import dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")

# 初始化语言模型
# chat_model = ChatOpenAI(model="gpt-4o-mini")
chat_model = ChatOpenAI(model="openai/gpt-oss-20b:free")

joke_query = "告诉我一个笑话。"

# 定义Json解析器
parser = JsonOutputParser()

# 以PromptTemplate为例
prompt_template = PromptTemplate.from_template(
    template="回答用户的查询\n 满足的格式为{format_instructions}\n 问题为{question}\n",
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

prompt = prompt_template.invoke(input={"question": joke_query})
response = chat_model.invoke(prompt)
print(response)

json_result = parser.invoke(response)
print(json_result)
