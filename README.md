# LangChain Study Python 项目

一个基于 LangChain 的 Python 学习项目，包含链式调用、智能代理、聊天机器人等多种 AI 应用示例。

## 📋 项目概述

本项目是一个 LangChain 学习和实践项目，展示了如何使用 LangChain 框架构建各种 AI 应用。项目使用现代 Python 工具链，包括 `uv` 作为包管理器，`Makefile` 提供便捷的命令接口。

## ✨ 功能特性

### 🔗 核心功能模块

- **链式调用 (Chains)**: 演示 LangChain 的基本链式调用和 JSON 输出解析
- **智能代理 (Agents)**: 集成搜索工具的智能代理，支持实时信息检索
- **聊天机器人 (Chat Bot)**: 具备记忆功能的对话机器人，支持文档检索
- **工具函数库**: 提供数学计算等实用工具函数
- **OpenRouter 集成**: 支持多种开源大语言模型

### 🛠 技术栈

- **核心框架**: LangChain, LangGraph
- **大语言模型**: OpenAI API, OpenRouter
- **搜索工具**: Tavily Search API
- **向量数据库**: FAISS
- **文档处理**: 网页加载器、文本分割器
- **包管理**: UV (现代 Python 包管理器)
- **任务运行**: Makefile (类似 npm scripts)

## 📁 项目结构

```
langchain-study-py2/
├── src/                    # 源代码目录
│   ├── main.py            # 主程序入口
│   ├── openrouter.py      # OpenRouter API 测试
│   ├── utils.py           # 工具函数库
│   ├── chains/            # 链式调用示例
│   │   ├── 1.lecl.py      # LECL 链式调用
│   │   └── 2.memory.py    # 记忆功能
│   ├── agent/             # 智能代理示例
│   │   ├── 1.py           # 基础代理
│   │   └── 2.py           # 高级代理
│   └── chat-bot/          # 聊天机器人
│       └── main.py        # 聊天机器人主程序
├── docs/                  # 文档目录
│   ├── env-setup.md       # 环境配置指南
│   ├── quick-commands.md  # 快速命令指南
│   ├── uv-use.md         # UV 使用指南
│   └── ...               # 其他文档
├── .env-example          # 环境变量示例文件
├── pyproject.toml        # 项目配置文件
├── uv.lock              # 依赖锁定文件
├── Makefile             # 任务运行配置
└── README.md            # 项目说明文档
```

## 🚀 快速开始

### 1. 环境要求

- Python >= 3.12
- UV 包管理器

### 2. 安装 UV

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# 或使用 pip
pip install uv
```

### 3. 克隆项目

```bash
git clone <repository-url>
cd langchain-study-py2
```

### 4. 安装依赖

```bash
# 使用 Makefile (推荐)
make install

# 或直接使用 uv
uv sync
```

### 5. 配置环境变量

```bash
# 复制环境变量示例文件
cp .env-example .env

# 编辑 .env 文件，填入你的 API 密钥
# 需要配置的密钥：
# - OPENROUTER_API_KEY: OpenRouter API 密钥
# - TAVILY_API_KEY: Tavily 搜索 API 密钥
```

## 🎯 使用方法

### 快速命令 (推荐)

```bash
# 查看所有可用命令
make help

# 运行主程序
make main

# 测试 OpenRouter API
make openrouter

# 运行工具函数演示
make utils

# 清理缓存
make clean
```

### 直接运行

```bash
# 运行主程序
uv run src/main.py

# 测试 OpenRouter
uv run src/openrouter.py

# 运行工具函数
uv run src/utils.py

# 运行链式调用示例
uv run src/chains/1.lecl.py

# 运行智能代理
uv run src/agent/1.py

# 运行聊天机器人
uv run src/chat-bot/main.py
```

## 📚 功能模块详解

### 🔗 链式调用 (Chains)

**文件**: `src/chains/1.lecl.py`

演示如何使用 LangChain 的基本链式调用功能：
- PromptTemplate 使用
- JsonOutputParser 输出解析
- 与大语言模型的交互

### 🤖 智能代理 (Agents)

**文件**: `src/agent/1.py`

展示智能代理的构建和使用：
- 集成 Tavily 搜索工具
- ZERO_SHOT_REACT_DESCRIPTION 代理类型
- 实时信息检索和处理

### 💬 聊天机器人 (Chat Bot)

**文件**: `src/chat-bot/main.py`

功能完整的聊天机器人：
- 文档加载和向量化
- FAISS 向量数据库
- 对话历史记忆
- 多工具集成（搜索 + 文档检索）

### 🛠 工具函数库

**文件**: `src/utils.py`

提供各种实用工具函数：
- 数学计算函数
- 类型提示支持
- 完整的文档字符串

## 🔧 配置说明

### 环境变量

项目需要以下环境变量：

```bash
# OpenRouter API 配置
OPENAI_API_KEY=sk-or-v1-your-api-key
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_API_KEY=sk-or-your-api-key

# 可选：网站信息（用于 OpenRouter 排名）
SITE_URL=https://your-site.com
SITE_NAME=Your Site Name

# Tavily 搜索 API
TAVILY_API_KEY=tvly-your-api-key
```

### 支持的模型

项目支持多种大语言模型：
- `openai/gpt-oss-20b:free` (免费)
- `gpt-4o-mini`
- `qwen/qwen3-235b-a22b:free` (免费)

## 📖 文档

项目包含详细的文档，位于 `docs/` 目录：

- [环境配置指南](docs/env-setup.md)
- [快速命令指南](docs/quick-commands.md)
- [UV 使用指南](docs/uv-use.md)
- [Makefile 指南](docs/makefile-guide.md)
- [NPM vs UV 对比](docs/npm-uv-comparison.md)

## 🤝 贡献指南

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- [LangChain](https://github.com/langchain-ai/langchain) - 强大的 LLM 应用框架
- [UV](https://github.com/astral-sh/uv) - 现代 Python 包管理器
- [OpenRouter](https://openrouter.ai/) - 多模型 API 服务
- [Tavily](https://tavily.com/) - 搜索 API 服务

## 📞 联系方式

如有问题或建议，请通过以下方式联系：

- 提交 Issue
- 发起 Discussion
- 邮件联系

---

⭐ 如果这个项目对你有帮助，请给它一个星标！