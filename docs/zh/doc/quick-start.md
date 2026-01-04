# 快速开始指南

[中文](quick-start.md) | [English](https://songshgeo.github.io/project_template/en/doc/quick-start/)

这是一个详细的快速开始指南，帮助您从零开始使用这个 Python 项目模板。

## 前提条件

在开始之前，请确保您的系统已安装：

- **Python 3.10-3.13**（推荐使用 3.11）
- **Git**
- **uv**（推荐）或 **poetry**

## 步骤 1：安装包管理器

### 选项 A：使用 uv（推荐）

uv 是一个极快的 Python 包管理器，由 Rust 编写。

```bash
# 安装 uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 验证安装
uv --version
```

### 选项 B：使用 poetry

```bash
# 安装 poetry
pip install poetry

# 验证安装
poetry --version
```

## 步骤 2：创建新项目

```bash
# 克隆模板仓库
git clone https://github.com/SongshGeo/project_template.git my-project
cd my-project

# 删除旧的 git 历史（可选）
rm -rf .git
git init
```

## 步骤 3：配置项目

运行配置脚本来自定义项目信息：

```bash
make configure-project
```

或者手动运行：

```bash
python scripts/configure_project.py
```

脚本会提示您输入：
- **项目名称**：将在包名和配置中使用（例如：`my-awesome-project`）
- **项目描述**：项目的简要描述（例如：`An awesome Python project`）

**配置脚本会自动执行以下操作：**

1. **更新 `pyproject.toml`**
   - 更新 `[project]` 段的 `name` 和 `description`
   - 更新 `[tool.poetry]` 段的 `name` 和 `description`

2. **更新 GitHub Workflow**
   - 更新 `.github/workflows/release-please.yml` 中的项目名称

3. **创建 README.md**
   - 使用项目名称和描述创建新的 README.md

4. **清空 CHANGELOG.md**
   - 为您的项目准备一个新的变更日志

**示例输出：**

```
$ make configure-project
项目名称: my-awesome-project
项目描述: An awesome Python project
✓ 已更新 pyproject.toml
✓ 已更新 .github/workflows/release-please.yml

✨ 项目配置已完成!
```

## 步骤 4：安装依赖

### 使用 uv

```bash
# 安装所有依赖（包括开发依赖和文档依赖）
uv sync --all-extras

# 或只安装开发依赖
uv sync --dev
```

### 使用 poetry

```bash
# 安装所有依赖
poetry install
```

安装完成后，依赖会被安装到虚拟环境中。

## 步骤 5：设置 Git hooks

```bash
# 安装 pre-commit hooks
pre-commit install

# 首次运行所有检查
pre-commit run --all-files
```

## 步骤 6：验证安装

运行测试以确保一切正常：

```bash
# 使用 Makefile
make test

# 或直接运行
uv run pytest
# 或
poetry run pytest
```

查看测试报告：

```bash
make report
```

## 步骤 7：开始开发

### 项目结构

```
src/
├── core/          # 核心业务逻辑
└── api/           # API 接口
├── conftest.py             # pytest 配置
├── test_configure_project.py  # 配置脚本测试
└── test_*.py               # 其他测试文件
```

### 当前测试

项目模板已包含基础测试：
- `tests/test_configure_project.py` - 测试项目配置脚本

运行测试：
```bash
make test
# 或
uv run pytest
```

### 添加新功能

1. 在 `src/` 目录下添加您的代码
2. 在 `tests/` 目录下添加对应的测试文件
3. 运行测试确保功能正常

**测试示例：**

```python
# tests/test_my_module.py
def test_my_function():
    """Test my function."""
    from src.my_module import my_function
    assert my_function() == expected_value
```

### 添加新依赖

使用 uv：

```bash
# 添加运行时依赖
uv add numpy pandas

# 添加开发依赖
uv add --dev pytest-cov

# 添加文档依赖
uv add --dev mkdocs
```

使用 poetry：

```bash
# 添加运行时依赖
poetry add numpy pandas

# 添加开发依赖
poetry add --group dev pytest-cov
```

### 运行代码

```bash
# 使用 uv
uv run python src/your_script.py

# 使用 poetry
poetry run python src/your_script.py

# 或激活虚拟环境
uv shell  # uv
poetry shell  # poetry
```

## 步骤 8：代码质量检查

### 运行多版本测试

使用 tox 测试代码在不同 Python 版本的兼容性：

```bash
# 测试所有版本（3.10-3.13）
make tox

# 测试特定版本
make tox-e pyversion=py311

# 查看可用环境
make tox-list
```

### 自动检查（推荐）

每次提交时会自动运行检查。如果需要手动运行：

```bash
# 运行所有检查
pre-commit run --all-files

# 运行特定检查
pre-commit run black --all-files
pre-commit run flake8 --all-files
pre-commit run interrogate --all-files
```

### 手动运行工具

```bash
# 代码格式化
black .
ruff format .

# 代码检查
flake8 src/
mypy src/

# 文档覆盖率
interrogate src/
```

## 下一步

- 阅读 [工具链说明](tools.md) 了解各工具的详细用法
- 查看 [配置说明](configuration.md) 了解如何配置项目
- 阅读 [开发规范](development.md) 了解代码规范
- 查看 [部署指南](deployment.md) 了解如何部署项目

## 常见问题

### Q: 如何选择 uv 还是 poetry？

A: uv 更快，是 Rust 编写。poetry 更成熟，社区支持更多。如果追求性能，选择 uv；如果追求稳定性，选择 poetry。本模板同时支持两者。

### Q: 虚拟环境在哪里？

A:
- uv 默认使用 `.venv` 目录
- poetry 默认使用独立的环境目录

查看虚拟环境位置：

```bash
uv info  # uv
poetry env info  # poetry
```

### Q: 如何添加 Python 版本测试？

A: 编辑 `tox.ini`，修改 `envlist` 行：

```ini
envlist = py310, py311, py312, py313
```

### Q: 如何生成文档？

A:

```bash
# 启动文档服务器
uv run mkdocs serve

# 构建静态文档
uv run mkdocs build
```

文档将生成在 `site/` 目录。

### Q: 如何发布到 PyPI？

A: 参考 [部署指南](deployment.md) 中的 PyPI 发布章节。
