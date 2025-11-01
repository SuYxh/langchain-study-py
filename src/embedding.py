from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

def create_embedding_model():
    """创建并返回 embedding 模型实例"""
    # 获取硅基流动的 API Key
    api_key = os.environ.get("SILICONFLOW_API_KEY")
    
    # 创建 OpenAI Embeddings 实例，使用硅基流动的配置
    embedding_model = OpenAIEmbeddings(
        model="Qwen/Qwen3-Embedding-8B",  # 指定模型名称
        api_key=api_key,                  # 你的 API Key
        base_url="https://api.siliconflow.cn/v1" # 硅基流动的 API 基础地址
    )
    
    return embedding_model