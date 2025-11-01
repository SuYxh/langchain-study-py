from langchain_community.embeddings import DashScopeEmbeddings
from langchain_redis import RedisConfig, RedisVectorStore
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

# 方法二（临时测试）：直接在代码中写入（注意安全风险）
# api_key = "你的硅基流动API密钥" # <--- 替换成你自己的 Key
api_key = os.environ.get("SILICONFLOW_API_KEY")

# 初始化 embedding 模型
embedding_model = OpenAIEmbeddings(
    model="Qwen/Qwen3-Embedding-8B",  # 指定模型名称
    api_key=api_key,                  # 你的 API Key
    base_url="https://api.siliconflow.cn/v1" # 硅基流动的 API 基础地址
)

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


