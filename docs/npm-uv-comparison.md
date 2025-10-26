# 前端工程师的 Python 包管理指南：npm vs uv

作为前端工程师，你已经熟悉了 npm 和 package.json 的工作方式。本文档将帮助你快速理解 Python 生态中的 uv 包管理器，通过对比 npm 和 uv 的相似概念和命令，让你能够快速上手 Python 项目开发。

## 📋 概念对比

| 概念 | npm (Node.js) | uv (Python) | 说明 |
|------|---------------|-------------|------|
| 包管理器 | npm / yarn / pnpm | uv / pip | 用于安装和管理依赖 |
| 配置文件 | package.json | pyproject.toml | 项目配置和依赖声明 |
| 锁定文件 | package-lock.json / yarn.lock | uv.lock | 锁定具体版本，确保一致性 |
| 依赖目录 | node_modules/ | .venv/ | 存放项目依赖 |
| 全局安装 | npm install -g | uv tool install | 全局安装工具 |
| 脚本执行 | npm run script | uv run python script.py | 执行项目脚本 |
| 开发依赖 | devDependencies | dev-dependencies | 仅开发时需要的依赖 |

## 📁 文件结构对比

### Node.js 项目结构
```
my-node-project/
├── package.json          # 项目配置和依赖
├── package-lock.json     # 锁定文件
├── node_modules/         # 依赖目录
├── src/
│   └── index.js
└── README.md
```

### Python 项目结构
```
my-python-project/
├── pyproject.toml        # 项目配置和依赖
├── uv.lock              # 锁定文件
├── .venv/               # 虚拟环境（类似 node_modules）
├── src/
│   └── main.py
└── README.md
```

## 📄 配置文件对比

### package.json vs pyproject.toml

**package.json 示例：**
```json
{
  "name": "my-app",
  "version": "1.0.0",
  "description": "My awesome app",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js",
    "build": "webpack --mode production",
    "test": "jest"
  },
  "dependencies": {
    "express": "^4.18.0",
    "lodash": "^4.17.21"
  },
  "devDependencies": {
    "nodemon": "^2.0.20",
    "jest": "^29.0.0"
  }
}
```

**pyproject.toml 示例：**
```toml
[project]
name = "my-app"
version = "1.0.0"
description = "My awesome app"
requires-python = ">=3.10"
dependencies = [
    "fastapi>=0.100.0",
    "requests>=2.31.0"
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=23.0.0"
]

[tool.uv]
dev-dependencies = [
    "pytest>=7.0.0",
    "black>=23.0.0"
]
```

## 🚀 常用命令对比

### 项目初始化

| 操作 | npm | uv |
|------|-----|----|
| 创建新项目 | `npm init` | `uv init` |
| 使用模板创建 | `npm create vite@latest` | `uv init --template` |
| 初始化现有目录 | `npm init -y` | `uv init` |

### 依赖管理

| 操作 | npm | uv |
|------|-----|----|
| 安装所有依赖 | `npm install` | `uv sync` |
| 安装生产依赖 | `npm ci` | `uv sync --frozen` |
| 添加依赖 | `npm install express` | `uv add express` |
| 添加开发依赖 | `npm install -D jest` | `uv add --dev pytest` |
| 添加特定版本 | `npm install lodash@4.17.21` | `uv add "lodash==4.17.21"` |
| 移除依赖 | `npm uninstall express` | `uv remove express` |
| 更新依赖 | `npm update` | `uv lock --upgrade` |
| 查看依赖树 | `npm ls` | `uv tree` |
| 查看过期依赖 | `npm outdated` | `uv lock --upgrade --dry-run` |

### 脚本执行

| 操作 | npm | uv |
|------|-----|----|
| 运行脚本 | `npm run start` | `uv run python main.py` |
| 运行开发服务器 | `npm run dev` | `uv run python -m uvicorn main:app --reload` |
| 运行测试 | `npm test` | `uv run pytest` |
| 执行任意命令 | `npx command` | `uv run command` |

### 环境管理

| 操作 | npm | uv |
|------|-----|----|
| 清理缓存 | `npm cache clean --force` | `uv cache clean` |
| 查看配置 | `npm config list` | `uv --version` |
| 查看安装位置 | `npm root` | `uv python list` |

## 🔄 工作流对比

### Node.js 典型工作流
```bash
# 1. 克隆项目
git clone <repo>
cd <project>

# 2. 安装依赖
npm install

# 3. 开发
npm run dev

# 4. 添加新依赖
npm install new-package

# 5. 运行测试
npm test

# 6. 构建
npm run build
```

### Python (uv) 典型工作流
```bash
# 1. 克隆项目
git clone <repo>
cd <project>

# 2. 安装依赖
uv sync

# 3. 开发
uv run python main.py

# 4. 添加新依赖
uv add new-package

# 5. 运行测试
uv run pytest

# 6. 构建/打包
uv build
```

## 🎯 实际示例对比

### 创建 Web 应用

**Node.js + Express:**
```bash
# 初始化项目
npm init -y
npm install express

# 创建 app.js
echo 'const express = require("express");
const app = express();
app.get("/", (req, res) => res.send("Hello World!"));
app.listen(3000);' > app.js

# 运行
node app.js
```

**Python + FastAPI:**
```bash
# 初始化项目
uv init
uv add fastapi uvicorn

# 创建 main.py
echo 'from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}' > main.py

# 运行
uv run uvicorn main:app --reload
```

### 添加测试

**Node.js + Jest:**
```bash
npm install -D jest
# 在 package.json 中添加 "test": "jest"
npm test
```

**Python + pytest:**
```bash
uv add --dev pytest
uv run pytest
```

## 🔧 高级功能对比

### 工作区/Monorepo

| 功能 | npm | uv |
|------|-----|----|
| 工作区支持 | `npm workspaces` | `uv workspace` |
| 链接本地包 | `npm link` | `uv add --editable ./local-package` |
| 运行所有包脚本 | `npm run --workspaces test` | `uv run --all-packages pytest` |

### 版本管理

| 功能 | npm | uv |
|------|-----|----|
| 查看版本 | `npm version` | 在 `pyproject.toml` 中手动管理 |
| 发布包 | `npm publish` | `uv publish` |
| 语义化版本 | `npm version patch/minor/major` | 手动更新或使用工具 |

## 💡 最佳实践对比

### Node.js 最佳实践
```bash
# 使用 .nvmrc 锁定 Node 版本
echo "18.17.0" > .nvmrc

# 使用 package-lock.json
npm ci  # 在 CI 中使用

# 区分生产和开发依赖
npm install --production
```

### Python (uv) 最佳实践
```bash
# 使用 .python-version 锁定 Python 版本
echo "3.11" > .python-version

# 使用 uv.lock
uv sync --frozen  # 在 CI 中使用

# 区分生产和开发依赖
uv sync --no-dev  # 仅安装生产依赖
```

## 🚨 常见陷阱和解决方案

### Node.js 常见问题 → Python 解决方案

| Node.js 问题 | Python (uv) 解决方案 |
|-------------|----------------------|
| `node_modules` 太大 | `.venv` 更轻量，且可以删除重建 |
| 版本冲突 | uv 的依赖解析更智能 |
| 全局污染 | 虚拟环境天然隔离 |
| 安装速度慢 | uv 使用 Rust 实现，速度更快 |

### 迁移检查清单

- [ ] 将 `package.json` 依赖转换为 `pyproject.toml`
- [ ] 将 npm scripts 转换为 uv run 命令
- [ ] 设置 `.python-version` 文件
- [ ] 配置 `.gitignore` 忽略 `.venv/`
- [ ] 更新 CI/CD 脚本使用 uv 命令

## 🎓 学习路径建议

### 第一周：基础概念
1. 理解虚拟环境概念（类比 node_modules）
2. 学习 `uv sync` 和 `uv add` 基本命令
3. 熟悉 `pyproject.toml` 文件结构

### 第二周：开发工作流
1. 掌握 `uv run` 执行脚本
2. 学习开发依赖管理
3. 了解测试和代码质量工具

### 第三周：高级功能
1. 探索 uv 的高级配置
2. 学习 Python 特有的包管理概念
3. 集成到现有开发流程

## 📚 相关资源

- [uv 官方文档](https://docs.astral.sh/uv/)
- [Python 包管理指南](https://packaging.python.org/)
- [pyproject.toml 规范](https://peps.python.org/pep-0621/)

## 🤝 总结

作为前端工程师，你会发现 uv 和 npm 有很多相似之处：

- **依赖管理**：都有配置文件和锁定文件
- **脚本执行**：都可以运行项目脚本
- **环境隔离**：都提供项目级别的依赖隔离
- **包生态**：都有丰富的第三方包生态

主要区别在于：
- Python 使用虚拟环境而不是 node_modules
- uv 更注重依赖解析的准确性和速度
- Python 生态更注重代码质量和类型安全

通过这个对比指南，你应该能够快速上手 Python 项目开发，并充分利用你在前端开发中积累的包管理经验！