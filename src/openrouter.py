import os
from dotenv import load_dotenv
from openai import OpenAI

# 加载 .env 文件中的环境变量
load_dotenv()

# 从环境变量中获取 API 密钥
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("请在 .env 文件中设置 OPENROUTER_API_KEY")


def main():
    """OpenRouter API 测试主函数"""
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": os.getenv(
                "SITE_URL", "https://your-site.com"
            ),  # 从环境变量获取，有默认值
            "X-Title": os.getenv(
                "SITE_NAME", "Your Site Name"
            ),  # 从环境变量获取，有默认值
        },
        extra_body={},
        model="openai/gpt-oss-20b:free",
        messages=[{"role": "user", "content": "你是谁？"}],
    )
    print(completion.choices[0].message.content)


if __name__ == "__main__":
    main()
