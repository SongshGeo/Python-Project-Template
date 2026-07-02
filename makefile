# Detect required commands
GIT := $(shell command -v git 2> /dev/null)
UV := $(shell command -v uv 2> /dev/null)
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
  MSG_UV_NOT_FOUND = 错误: 未找到 uv，请先安装：
  MSG_INSTALL_UV =   - uv:   curl -LsSf https://astral.sh/uv/install.sh | sh
  MSG_USING_UV = 使用 uv 作为包管理器
  MSG_INSTALL_DEPS = 安装依赖...
  MSG_INIT_PROJECT = 初始化项目...
  MSG_RUN_TESTS = 运行测试...
  MSG_TOX_ALL = 运行 tox 测试所有 Python 版本（3.10-3.13）...
  MSG_TOX_LIST = 查看可用环境...
  MSG_TOX_E = 运行特定版本的测试（用法: make tox-e pyversion=py311）...
  MSG_TOX_E_MISSING = 错误: 请指定版本，例如: make tox-e pyversion=py311
else
  MSG_UV_NOT_FOUND = Error: uv not found. Please install it:
  MSG_INSTALL_UV =   - uv:   curl -LsSf https://astral.sh/uv/install.sh | sh
  MSG_USING_UV = Using uv as package manager
  MSG_INSTALL_DEPS = Installing dependencies...
  MSG_INIT_PROJECT = Initializing project...
  MSG_RUN_TESTS = Running tests...
  MSG_TOX_ALL = Running tox for Python 3.10-3.13...
  MSG_TOX_LIST = Listing available environments...
  MSG_TOX_E = Running tests for specified version (usage: make tox-e pyversion=py311)...
  MSG_TOX_E_MISSING = Error: please specify a version, e.g., make tox-e pyversion=py311
endif

# Check that uv is available
check-package-manager:
	@if [ -z "$(UV)" ]; then \
		echo "$(MSG_UV_NOT_FOUND)"; \
		echo "$(MSG_INSTALL_UV)"; \
		exit 1; \
	fi
	@echo "$(MSG_USING_UV)"

# Install dependencies and configure project
setup: check-package-manager
	@echo "$(MSG_INSTALL_DEPS)"
	@env -u VIRTUAL_ENV uv sync --no-install-project \
		$(if $(DEV),--extra dev,) \
		$(if $(DOCS),--extra docs,)
	@echo "$(MSG_INIT_PROJECT)"
	@make configure-project

test: check-package-manager
	@echo "$(MSG_RUN_TESTS)"
	@env -u VIRTUAL_ENV uv run pytest

report:
	@env -u VIRTUAL_ENV uv run allure serve tmp/allure_results

configure-project: check-package-manager
	@env -u VIRTUAL_ENV uv run python scripts/configure_project.py

docs:
	@env -u VIRTUAL_ENV uv run mkdocs serve

docs-build:
	@env -u VIRTUAL_ENV uv run mkdocs build

tox:
	@echo "$(MSG_TOX_ALL)"
	@env -u VIRTUAL_ENV uv run tox

tox-list:
	@echo "$(MSG_TOX_LIST)"
	@env -u VIRTUAL_ENV uv run tox list

tox-e:
	@echo "$(MSG_TOX_E)"
	@if [ -z "$(pyversion)" ]; then \
		echo "$(MSG_TOX_E_MISSING)"; \
		exit 1; \
	fi
	@env -u VIRTUAL_ENV uv run tox -e $(pyversion)

.PHONY: setup test report configure-project check-package-manager docs docs-build tox tox-list tox-e
