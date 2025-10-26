# 快速命令指南

## 📋 概述

本项目提供了类似 `npm scripts` 的快速命令功能，让你可以轻松运行项目中的各种脚本。

## 🚀 可用命令

### 使用 Makefile (推荐)

```bash
# 显示所有可用命令
make help

# 运行主程序
make dev
make main

# 运行 OpenRouter 测试
make openrouter
make test-openrouter

# 安装依赖
make install

# 清理缓存
make clean
```

### 直接使用 uv run

```bash
# 运行主程序
uv run src/main.py

# 运行 OpenRouter 测试
uv run src/openrouter.py
```

## 📊 命令对比表

| 功能 | npm 命令 | 本项目命令 | 直接命令 |
|------|----------|------------|----------|
| 启动开发 | `npm run dev` | `make dev` | `uv run src/main.py` |
| 运行主程序 | `npm start` | `make main` | `uv run src/main.py` |
| 运行测试 | `npm run test` | `make openrouter` | `uv run src/openrouter.py` |
| 安装依赖 | `npm install` | `make install` | `uv sync` |
| 清理缓存 | `npm run clean` | `make clean` | `uv cache clean` |

## 🔧 自定义命令

### 添加新的 Makefile 命令

在 `Makefile` 中添加新的目标：

```makefile
# 添加新命令
new-script:
	uv run src/your-new-script.py

# 带参数的命令
test-with-args:
	uv run src/test.py --verbose

# 组合命令
full-test:
	uv sync
	uv run src/test.py
	echo "测试完成！"
```

### 使用环境变量

```makefile
# 设置环境变量
dev-with-debug:
	DEBUG=1 uv run src/main.py

production:
	ENV=production uv run src/main.py
```

## 💡 使用技巧

### 1. 查看帮助信息

```bash
# 显示所有可用命令
make help
# 或者直接运行 make（默认显示帮助）
make
```

### 2. 命令自动补全

在 zsh 中，你可以使用 Tab 键自动补全 make 命令：

```bash
make <Tab>  # 显示所有可用的目标
```

### 3. 并行执行

```bash
# 并行运行多个命令（如果支持）
make -j2 install test
```

### 4. 静默模式

```bash
# 静默运行，不显示命令本身
make -s dev
```

## 🔍 故障排除

### 常见问题

**问题**: `make: command not found`

**解决方案**: 
- macOS: `brew install make`
- 或者直接使用 `uv run` 命令

**问题**: `make: *** No rule to make target 'xxx'`

**解决方案**: 
- 检查命令名称是否正确
- 运行 `make help` 查看可用命令

**问题**: 权限错误

**解决方案**: 
```bash
# 确保 Makefile 有执行权限
chmod +x Makefile
```

## 📚 扩展阅读

- [GNU Make 官方文档](https://www.gnu.org/software/make/manual/)
- [uv 官方文档](https://docs.astral.sh/uv/)
- [Python 项目结构最佳实践](https://docs.python-guide.org/writing/structure/)

## 🎯 最佳实践

1. **保持命令简短**: 使用简短、易记的命令名
2. **添加帮助信息**: 为每个命令添加描述
3. **使用有意义的名称**: 命令名应该清楚地表达其功能
4. **组织相关命令**: 将相关的命令分组
5. **提供多种方式**: 既提供 make 命令，也提供直接的 uv run 方式