# Detect required commands
GIT := $(shell command -v git 2> /dev/null)
UV := $(shell command -v uv 2> /dev/null)
POETRY := $(shell command -v poetry 2> /dev/null)
# Control optional dependency groups (1 to enable, 0 to skip)
DEV ?= 1
DOCS ?= 0

# Language selection: prompt user first; default from system locale; fallback en
ifeq ($(LANG),)
LANG := $(shell \
	detected=$$(locale 2>/dev/null | awk -F= '/^LANG=/{print $$2}' | cut -d_ -f1 | cut -d. -f1); \
	default=$${detected:-en}; \
	printf "Select language (en/zh) [%s]: " $$default 1>&2; \
	read choice; \
	lang=$${choice:-$$default}; \
	case $$lang in zh|en) ;; *) lang=en ;; esac; \
	echo $$lang \
)
endif
LANG_CODE := $(LANG)

ifeq ($(LANG_CODE),zh)
  MSG_PKG_MGR_NOT_FOUND = 错误: 未找到 uv 或 poetry，请先安装其中一个：
  MSG_INSTALL_UV =   - uv:   curl -LsSf https://astral.sh/uv/install.sh | sh
  MSG_INSTALL_POETRY =   - poetry: pip install poetry
  MSG_USING_UV = 使用 uv 作为包管理器
  MSG_USING_POETRY = 使用 poetry 作为包管理器
  MSG_INSTALL_DEPS = 安装依赖...
  MSG_INIT_PROJECT = 初始化项目...
  MSG_RUN_TESTS = 运行测试...
  MSG_TOX_ALL = 运行 tox 测试所有 Python 版本（3.10-3.13）...
  MSG_TOX_LIST = 查看可用环境...
  MSG_TOX_E = 运行特定版本的测试（用法: make tox-e pyversion=py311）...
  MSG_TOX_E_MISSING = 错误: 请指定版本，例如: make tox-e pyversion=py311
else
  MSG_PKG_MGR_NOT_FOUND = Error: uv or poetry not found. Please install one:
  MSG_INSTALL_UV =   - uv:   curl -LsSf https://astral.sh/uv/install.sh | sh
  MSG_INSTALL_POETRY =   - poetry: pip install poetry
  MSG_USING_UV = Using uv as package manager
  MSG_USING_POETRY = Using poetry as package manager
  MSG_INSTALL_DEPS = Installing dependencies...
  MSG_INIT_PROJECT = Initializing project...
  MSG_RUN_TESTS = Running tests...
  MSG_TOX_ALL = Running tox for Python 3.10-3.13...
  MSG_TOX_LIST = Listing available environments...
  MSG_TOX_E = Running tests for specified version (usage: make tox-e pyversion=py311)...
  MSG_TOX_E_MISSING = Error: please specify a version, e.g., make tox-e pyversion=py311
endif

# Check for package manager
check-package-manager:
	@if [ -z "$(UV)" ] && [ -z "$(POETRY)" ]; then \
		echo "$(MSG_PKG_MGR_NOT_FOUND)"; \
		echo "$(MSG_INSTALL_UV)"; \
		echo "$(MSG_INSTALL_POETRY)"; \
		exit 1; \
	fi
	@if [ -n "$(UV)" ]; then \
		echo "$(MSG_USING_UV)"; \
	elif [ -n "$(POETRY)" ]; then \
		echo "$(MSG_USING_POETRY)"; \
	fi

# Install dependencies and configure project
setup: check-package-manager
	@echo "$(MSG_INSTALL_DEPS)"
	@if [ -n "$(UV)" ]; then \
		env -u VIRTUAL_ENV uv sync --no-install-project \
		$(if $(DEV),--extra dev,) \
		$(if $(DOCS),--extra docs,); \
	elif [ -n "$(POETRY)" ]; then \
		env -u VIRTUAL_ENV poetry install --no-root \
		$(if $(DEV),--with dev,) \
		$(if $(DOCS),--with docs,); \
	fi
	@echo "$(MSG_INIT_PROJECT)"
	@make configure-project

.PHONY: setup test report configure-project check-package-manager

# 如果测试命令不存在，则跳过测试
test: check-package-manager
	@echo "$(MSG_RUN_TESTS)"
	@if [ -n "$(UV)" ]; then \
		env -u VIRTUAL_ENV uv run pytest; \
	elif [ -n "$(POETRY)" ]; then \
		env -u VIRTUAL_ENV poetry run pytest; \
	fi

report:
	@if [ -n "$(UV)" ]; then \
		env -u VIRTUAL_ENV uv run allure serve tmp/allure_results; \
	elif [ -n "$(POETRY)" ]; then \
		env -u VIRTUAL_ENV poetry run allure serve tmp/allure_results; \
	fi

configure-project: check-package-manager
	@if [ -n "$(UV)" ]; then \
		env -u VIRTUAL_ENV uv run python scripts/configure_project.py; \
	elif [ -n "$(POETRY)" ]; then \
		env -u VIRTUAL_ENV poetry run python scripts/configure_project.py; \
	fi

docs:
	@if [ -n "$(UV)" ]; then \
		env -u VIRTUAL_ENV uv run mkdocs serve; \
	elif [ -n "$(POETRY)" ]; then \
		env -u VIRTUAL_ENV poetry run mkdocs serve; \
	fi

docs-build:
	@if [ -n "$(UV)" ]; then \
		env -u VIRTUAL_ENV uv run mkdocs build; \
	elif [ -n "$(POETRY)" ]; then \
		env -u VIRTUAL_ENV poetry run mkdocs build; \
	fi

tox:
	@echo "$(MSG_TOX_ALL)"
	@if [ -n "$(UV)" ]; then \
		env -u VIRTUAL_ENV uv run tox; \
	elif [ -n "$(POETRY)" ]; then \
		env -u VIRTUAL_ENV poetry run tox; \
	fi

tox-list:
	@echo "$(MSG_TOX_LIST)"
	@if [ -n "$(UV)" ]; then \
		env -u VIRTUAL_ENV uv run tox list; \
	elif [ -n "$(POETRY)" ]; then \
		env -u VIRTUAL_ENV poetry run tox list; \
	fi

tox-e:
	@echo "$(MSG_TOX_E)"
	@if [ -z "$(pyversion)" ]; then \
		echo "$(MSG_TOX_E_MISSING)"; \
		exit 1; \
	fi
	@if [ -n "$(UV)" ]; then \
		env -u VIRTUAL_ENV uv run tox -e $(pyversion); \
	elif [ -n "$(POETRY)" ]; then \
		env -u VIRTUAL_ENV poetry run tox -e $(pyversion); \
	fi

.PHONY: setup test report configure-project check-package-manager docs docs-build tox tox-list tox-e
