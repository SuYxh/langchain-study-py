from langchain_redis import RedisConfig, RedisVectorStore
from embedding import create_embedding_model
import os

# 创建 embedding 模型实例
embedding_model = create_embedding_model()

# --- 配置 Redis 向量数据库 ---
redis_url = "redis://localhost:6379"
config = RedisConfig(index_name="couplet", redis_url=redis_url)

# 初始化向量存储，使用新的 embedding_model
vector_store = RedisVectorStore(embeddings=embedding_model, config=config)


# 加载数据
lines = []
# 获取当前脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(script_dir, "resource", "couplet_dataset.csv")
with open(data_file, "r", encoding="utf-8") as file:
    for line in file:
        if line.strip():  # 跳过空行
            lines.append(line.strip())

# 存入向量数据库
vector_store.add_texts(lines)
print(f"成功使用硅基流动模型加载 {len(lines)} 条对联数据到向量数据库！")


