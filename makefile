# 检查必要的命令是否存在
GIT := $(shell command -v git 2> /dev/null)
POETRY := $(shell command -v poetry 2> /dev/null)

# 自动让当前项目适配新的名字
setup:
	@echo "安装依赖..."
	@poetry install
	@echo "初始化项目..."
	@make configure-project

.PHONY: publish test

# 如果测试命令不存在，则跳过测试
test:
	@if [ -f "pytest" ] || [ -f "python -m pytest" ]; then \
		pytest; \
	else \
		echo "警告: 未找到测试命令，跳过测试"; \
	fi

report:
	poetry run allure serve tmp/allure_results

configure-project:
	@poetry run python scripts/configure_project.py
