from langchain_redis import RedisConfig, RedisVectorStore
from langchain_core.prompts import ChatPromptTemplate
from llm import create_siliconflow_model
from embedding import create_embedding_model


llm = create_siliconflow_model()
# 创建 embedding 模型实例
embedding_model = create_embedding_model()


# 初始化
# --- 配置 Redis 向量数据库 ---
redis_url = "redis://localhost:6379"
config = RedisConfig(index_name="couplet", redis_url=redis_url)

# 初始化向量存储，使用新的 embedding_model
vector_store = RedisVectorStore(embeddings=embedding_model, config=config)


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
