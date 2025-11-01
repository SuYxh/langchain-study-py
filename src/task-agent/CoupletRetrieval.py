from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import RedisVectorStore
from langchain_redis import RedisConfig
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatTongyi

# 初始化
redis_url = "redis://localhost:6379"
config = RedisConfig(index_name="couplet", redis_url=redis_url)
vector_store = RedisVectorStore(embedding_model=DashScopeEmbeddings(), config=config)
llm = ChatTongyi(model="qwen-plus", api_key="YOUR_API_KEY")

# 检索测试
query = "帮我对个对联，上联是: 瑞雪兆丰年"
samples = []
scored_results = vector_store.similarity_search_with_score(query, k=10)
for doc, score in scored_results:
    samples.append(doc.page_content)

# 生成下联
prompt_template = ChatPromptTemplate.from_messages([
    ("system", """你是一个专业的对联大师，参考以下对联设计下联：
    参考对联: {samples}
    请用中文回答"""),
    ("user", "{text}")
])

prompt = prompt_template.invoke({"samples": samples, "text": query})
response = llm.invoke(prompt)
print(response.content)
