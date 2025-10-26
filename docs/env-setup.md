# 环境变量配置指南

## 📋 概述

本项目使用 `.env` 文件来管理敏感信息（如 API 密钥），确保安全性和配置的灵活性。

## 🔧 设置步骤

### 1. 环境变量文件

项目根目录下的 `.env` 文件包含以下配置：

```bash
# OpenRouter API Key
OPENROUTER_API_KEY=your-api-key-here

# Optional: Site information for OpenRouter rankings
SITE_URL=https://your-site.com
SITE_NAME=Your Site Name
```

### 2. 修改 API 密钥

将 `.env` 文件中的 `OPENROUTER_API_KEY` 值替换为你的实际 API 密钥：

```bash
OPENROUTER_API_KEY=sk-or-v1-your-actual-api-key
```

### 3. 安装依赖

确保已安装 `python-dotenv` 依赖：

```bash
uv sync
```

## 🚀 使用方法

### 在代码中加载环境变量

```python
import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# 获取环境变量
api_key = os.getenv("OPENROUTER_API_KEY")
site_url = os.getenv("SITE_URL", "默认值")
```

### 运行项目

```bash
# 使用 uv 运行
uv run openrouter.py

# 或者激活虚拟环境后运行
source .venv/bin/activate
python openrouter.py
```

## 🔒 安全注意事项

### ✅ 已配置的安全措施

- ✅ `.env` 文件已添加到 `.gitignore`，不会被提交到版本控制
- ✅ 代码中移除了硬编码的 API 密钥
- ✅ 添加了环境变量验证，缺少必要配置时会报错

### 🚨 重要提醒

1. **永远不要**将 `.env` 文件提交到 Git 仓库
2. **永远不要**在代码中硬编码 API 密钥
3. **定期轮换** API 密钥以提高安全性
4. **限制访问权限**，只有需要的人员才能访问 `.env` 文件

## 🛠️ 故障排除

### 常见问题

**问题**: `ValueError: 请在 .env 文件中设置 OPENROUTER_API_KEY`

**解决方案**:
1. 检查 `.env` 文件是否存在于项目根目录
2. 确认 `OPENROUTER_API_KEY` 变量名拼写正确
3. 确保 API 密钥值不为空

**问题**: `ModuleNotFoundError: No module named 'dotenv'`

**解决方案**:
```bash
uv sync  # 重新同步依赖
```

## 📚 相关文档

- [python-dotenv 官方文档](https://python-dotenv.readthedocs.io/)
- [OpenRouter API 文档](https://openrouter.ai/docs)
- [uv 使用指南](./uv-use.md)