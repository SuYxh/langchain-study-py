# UV 使用指南

本文档介绍如何在 Python 项目中使用 uv 进行依赖管理和环境管理。

## 项目概述

本项目是一个基于 LangChain 的 Python 项目，使用 uv 作为包管理器。项目包含以下主要依赖：

- LangChain 生态系统（langchain, langgraph 等）
- 阿里云百炼 SDK
- OpenAI SDK
- 其他工具库（selenium, pyautogui 等）

## 依赖安装

### 方法一：使用 uv sync（推荐）

```bash
uv sync
```

**特点：**
- 根据 `uv.lock` 文件安装精确版本的依赖
- 确保所有依赖版本与锁定文件完全一致
- 自动创建和管理虚拟环境
- 适合团队协作，保证环境一致性

### 方法二：使用 uv install

```bash
uv install
```

**特点：**
- 根据 `pyproject.toml` 安装依赖
- 如果 `uv.lock` 存在，会尊重锁定的版本
- 适合首次安装或更新依赖

## 环境管理

### 激活虚拟环境

```bash
# macOS/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate

# 或使用点命令（等同于 source）
. .venv/bin/activate
```

**使用场景：**
- 需要在当前终端会话中持续使用项目环境
- 进行交互式开发和调试
- 运行多个相关命令
- 使用项目中安装的命令行工具

**特点：**
- 激活后终端提示符显示环境名称（如 `(.venv)`）
- 所有 `python`、`pip` 命令使用虚拟环境
- 需要手动退出（`deactivate` 命令）

### 退出虚拟环境

```bash
deactivate
```

## 运行 Python 脚本

### 使用 uv run（推荐）

```bash
# 运行 Python 脚本
uv run python main.py

# 运行模块
uv run python -m pytest

# 传递参数
uv run python main.py --arg1 value1 --arg2 value2

# 运行其他工具
uv run pytest
uv run black .
uv run mypy src/
```

**使用场景：**
- 运行单个脚本或命令
- CI/CD 流水线中执行脚本
- 不想激活环境但需要使用项目依赖
- 快速执行一次性任务

**特点：**
- 自动使用项目虚拟环境
- 命令执行完毕后自动回到系统环境
- 不改变当前终端环境状态
- 更适合脚本化操作

## UV 常用命令

### 项目初始化

```bash
# 创建新项目
uv init my-project

# 在现有目录初始化
uv init
```

### 依赖管理

```bash
# 添加依赖
uv add package_name
uv add "package_name>=1.0.0"
uv add package_name --dev  # 开发依赖

# 移除依赖
uv remove package_name

# 更新依赖
uv lock --upgrade
uv sync --upgrade

# 查看依赖树
uv tree

# 列出已安装包
uv pip list
```

### 环境管理

```bash
# 创建虚拟环境
uv venv

# 指定 Python 版本创建环境
uv venv --python 3.12

# 删除虚拟环境
rm -rf .venv

# 查看环境信息
uv python list
```

### 运行和执行

```bash
# 运行 Python 脚本
uv run python script.py

# 指定 Python 版本运行
uv run --python 3.12 python script.py

# 显示详细输出
uv run --verbose python script.py

# 运行 pip 命令
uv pip install package_name
uv pip freeze
```

## 使用场景对比

### 场景1：快速运行脚本

**推荐：使用 uv run**
```bash
uv run python main.py
```

**优势：**
- 一条命令完成
- 不污染终端环境
- 适合自动化脚本

### 场景2：开发调试

**推荐：激活环境**
```bash
source .venv/bin/activate
python main.py
python -c "import langchain; print(langchain.__version__)"
pip list | grep langchain
deactivate
```

**优势：**
- 交互式开发友好
- 可以连续执行多个命令
- 环境状态清晰可见

### 场景3：CI/CD 流水线

**推荐：uv run**
```bash
uv sync
uv run python -m pytest
uv run python -m mypy src/
```

**优势：**
- 脚本化友好
- 环境隔离
- 执行效率高

## 最佳实践

### 1. 版本控制

- 将 `pyproject.toml` 和 `uv.lock` 都提交到版本控制
- 不要提交 `.venv/` 目录
- 使用 `.python-version` 文件指定 Python 版本

### 2. 团队协作

```bash
# 克隆项目后
git clone <repository>
cd <project>
uv sync  # 安装完全相同的依赖版本
```

### 3. 依赖更新

```bash
# 更新所有依赖到最新版本
uv lock --upgrade
uv sync

# 更新特定依赖
uv add "package_name>=2.0.0"
```

### 4. 开发工作流

```bash
# 日常开发
source .venv/bin/activate

# 添加新功能需要的依赖
uv add new_package

# 运行测试
python -m pytest

# 代码格式化
black .

# 类型检查
mypy src/

deactivate
```

## 注意事项

1. **Python 版本兼容性**
   - 项目要求 Python >= 3.10
   - `uv.lock` 显示需要 >= 3.12
   - 建议使用 Python 3.12+ 版本

2. **环境隔离**
   - uv 自动创建项目级虚拟环境
   - 每个项目都有独立的依赖环境
   - 避免全局安装项目依赖

3. **性能优化**
   - uv 比 pip 更快的依赖解析和安装
   - 使用 Rust 实现，性能优异
   - 支持并行下载和安装

4. **故障排除**
   - 如果依赖冲突，删除 `uv.lock` 重新生成
   - 清理缓存：`uv cache clean`
   - 重建环境：`rm -rf .venv && uv sync`

## 总结

uv 是一个现代化的 Python 包管理器，提供了快速、可靠的依赖管理和环境管理功能。通过合理使用 `uv sync`、`uv run` 等命令，可以大大提升 Python 项目的开发效率和环境一致性。

选择使用方式的建议：
- **快速执行**：使用 `uv run`
- **开发调试**：激活虚拟环境
- **团队协作**：使用 `uv sync` 保证环境一致
- **CI/CD**：使用 `uv run` 进行脚本化操作