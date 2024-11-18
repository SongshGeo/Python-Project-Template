setup:
	make install-tests
	make install-jupyter
	make setup-pre-commit
	make setup-organizor

setup-organizor:
	poetry add hydra-core

setup-pre-commit:
	echo "安装 pre-commit 依赖"
	poetry add --group dev flake8 isort nbstripout pydocstyle pre-commit-hooks
	echo "安装 pre-commit"
	poetry run pre-commit install
	echo "pre-commit 安装完成"

install-jupyter:
	poetry add ipykernel --group dev
	poetry add jupyterlab_execute_time --group dev

install-tests:
	poetry add pytest allure-pytest --group dev
	poetry add pytest-clarity pytest-sugar --group dev

# https://timvink.github.io/mkdocs-git-authors-plugin/index.html
install-docs:
	poetry add --group docs mkdocs
	poetry add --group docs mkdocs-material
	poetry add --group docs mkdocs-git-revision-date-localized-plugin
	poetry add --group docs mkdocs-minify-plugin
	poetry add --group docs mkdocs-redirects
	poetry add --group docs mkdocs-awesome-pages-plugin
	poetry add --group docs mkdocs-git-authors-plugin
	poetry add --group docs mkdocstrings\[python\]
	poetry add --group docs mkdocs-bibtex
	poetry add --group docs mkdocs-macros-plugin
	poetry add --group docs mkdocs-jupyter
	poetry add --group docs mkdocs-callouts
	poetry add --group docs mkdocs-glightbox

# 检查必要的命令是否存在
STANDARD_VERSION := $(shell command -v standard-version 2> /dev/null)
GIT := $(shell command -v git 2> /dev/null)

.PHONY: publish test

publish:
	@echo "开始发布新版本..."

	@# 检查是否在 dev 分支
	@if [ "$$(git rev-parse --abbrev-ref HEAD)" != "dev" ]; then \
		echo "错误: 必须在 dev 分支上执行发布"; \
		exit 1; \
	fi

	@# 检查工作区是否干净
	@if [ -n "$$(git status --porcelain)" ]; then \
		echo "错误: 工作区不干净，请先提交或存储更改"; \
		exit 1; \
	fi

	@# 检查是否有未拉取的更新
	@git fetch origin
	@if [ "$$(git rev-list HEAD..origin/dev --count)" != "0" ]; then \
		echo "错误: 本地分支落后于远程，请先拉取最新代码"; \
		exit 1; \
	fi

	@echo "运行单元测试..."
	@if ! make test; then \
		echo "错误: 单元测试失败"; \
		exit 1; \
	fi

	@# 检查 standard-version 是否安装
	@if [ -z "$(STANDARD_VERSION)" ]; then \
		echo "错误: standard-version 未安装，请先安装: npm install -g standard-version"; \
		exit 1; \
	fi

	@echo "生成版本号..."
	@standard-version || { echo "错误: 版本号生成失败"; exit 1; }

	@echo "推送代码和标签..."
	@git push --follow-tags origin dev || { echo "错误: 推送失败"; exit 1; }

	@echo "✨ 发布成功!"

# 如果测试命令不存在，则跳过测试
test:
	@if [ -f "pytest" ] || [ -f "python -m pytest" ]; then \
		pytest; \
	else \
		echo "警告: 未找到测试命令，跳过测试"; \
	fi

report:
	poetry run allure serve tmp/allure_results
