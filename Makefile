# 类似 npm scripts 的快速命令
# 使用方法: make dev, make openrouter, make main

.PHONY: dev openrouter main test-openrouter utils help

# 默认显示帮助信息
help:
	@echo "可用的命令:"
	@echo "  make main         - 运行主程序 (src/main.py)"
	@echo "  make openrouter   - 运行 OpenRouter 测试 (src/openrouter.py)"
	@echo "  make utils        - 运行工具函数演示 (src/utils.py)"
	@echo "  make test-openrouter - 运行 OpenRouter 测试 (src/openrouter.py)"
	@echo ""
	@echo "或者直接使用 uv run:"
	@echo "  uv run src/main.py"
	@echo "  uv run src/openrouter.py"
	@echo "  uv run src/utils.py"

# 运行主程序
main:
	uv run src/main.py

# 运行 OpenRouter 测试
openrouter:
	uv run src/openrouter.py

# 运行工具函数演示
utils:
	uv run src/utils.py

# 安装依赖
install:
	uv sync

# 清理缓存
clean:
	uv cache clean