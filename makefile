setup:
	make install-tests
	make install-jupyter
	make setup-pre-commit
	make setup-organizor

setup-organizor:
	poetry add hydra-core
	poetry add --group dev sourcery

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

test:
	poetry run pytest -vs --clean-alluredir --alluredir tmp/allure_results

report:
	poetry run allure serve tmp/allure_results

publish:
	echo "开始发布新版本"
	echo "运行单元测试"
	make test
	echo "生成版本号"
	standard-version
	echo "推送代码和标签"
	git push --follow-tags origin dev
	echo "发布成功"
