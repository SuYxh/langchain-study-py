from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import RedisVectorStore
from langchain_redis import RedisConfig
import os

# 配置
redis_url = "redis://localhost:6379"
config = RedisConfig(index_name="couplet", redis_url=redis_url)
vector_store = RedisVectorStore(embedding_model=DashScopeEmbeddings(), config=config)

# 加载数据
lines = []
with open("./resource/couplet_dataset.csv", "r", encoding="utf-8") as file:
    for line in file:
        lines.append(line.strip())

# 存入向量数据库
vector_store.add_texts(lines)
print("对联数据加载完成！")
