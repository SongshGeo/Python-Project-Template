# 检查必要的命令是否存在
GIT := $(shell command -v git 2> /dev/null)
UV := $(shell command -v uv 2> /dev/null)
POETRY := $(shell command -v poetry 2> /dev/null)

# 检查是否安装了包管理器
check-package-manager:
	@if [ -z "$(UV)" ] && [ -z "$(POETRY)" ]; then \
		echo "错误: 未找到 uv 或 poetry，请先安装其中一个："; \
		echo "  - uv:   curl -LsSf https://astral.sh/uv/install.sh | sh"; \
		echo "  - poetry: pip install poetry"; \
		exit 1; \
	fi
	@if [ -n "$(UV)" ]; then \
		echo "使用 uv 作为包管理器"; \
	elif [ -n "$(POETRY)" ]; then \
		echo "使用 poetry 作为包管理器"; \
	fi

# 自动让当前项目适配新的名字
setup: check-package-manager
	@echo "安装依赖..."
	@if [ -n "$(UV)" ]; then \
		uv sync --all-extras; \
	elif [ -n "$(POETRY)" ]; then \
		poetry install; \
	fi
	@echo "初始化项目..."
	@make configure-project

.PHONY: setup test report configure-project check-package-manager

# 如果测试命令不存在，则跳过测试
test: check-package-manager
	@echo "运行测试..."
	@if [ -n "$(UV)" ]; then \
		uv run pytest; \
	elif [ -n "$(POETRY)" ]; then \
		poetry run pytest; \
	fi

report:
	@if [ -n "$(UV)" ]; then \
		uv run allure serve tmp/allure_results; \
	elif [ -n "$(POETRY)" ]; then \
		poetry run allure serve tmp/allure_results; \
	fi

configure-project: check-package-manager
	@if [ -n "$(UV)" ]; then \
		uv run python scripts/configure_project.py; \
	elif [ -n "$(POETRY)" ]; then \
		poetry run python scripts/configure_project.py; \
	fi

docs:
	@if [ -n "$(UV)" ]; then \
		uv run mkdocs serve; \
	elif [ -n "$(POETRY)" ]; then \
		poetry run mkdocs serve; \
	fi

docs-build:
	@if [ -n "$(UV)" ]; then \
		uv run mkdocs build; \
	elif [ -n "$(POETRY)" ]; then \
		poetry run mkdocs build; \
	fi

.PHONY: setup test report configure-project check-package-manager docs docs-build
