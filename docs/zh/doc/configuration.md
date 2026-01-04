# 配置说明

[中文](configuration.md) | [English](https://songshgeo.github.io/project_template/en/doc/configuration/)

本模板包含多种配置文件，用于管理项目的各个方面。本章节详细说明各个配置文件的作用和配置方法。

## 主要配置文件

### pyproject.toml

**作用：** Python 项目的核心配置文件，定义项目元数据、依赖、工具配置等。

**主要配置段：**

#### [project]（uv 使用）

```toml
[project]
name = "project-name"
version = "1.0.0"
description = "Project description"
requires-python = ">=3.10,<3.14"
dependencies = [
    "package1>=1.0.0",
    "package2>=2.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=23.0.0",
]
docs = [
    "mkdocs>=1.4.0",
]
```

#### [tool.poetry]（poetry 兼容）

```toml
[tool.poetry]
name = "project-name"
version = "1.0.0"
description = "Project description"

[tool.poetry.dependencies]
python = ">=3.10,<3.14"
package1 = ">=1.0.0"

[tool.poetry.group.dev.dependencies]
pytest = ">=7.0.0"
```

#### 工具配置

```toml
# Black 配置
[tool.black]
line-length = 88
target-version = ['py310', 'py311', 'py312', 'py313']

# Ruff 配置
[tool.ruff]
line-length = 88
target-version = "py310"
select = ["E", "F", "I", "N", "W", "B", "C4", "UP"]

# MyPy 配置
[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true

# Interrogate 配置
[tool.interrogate]
fail-under = 80
ignore-init-module = true

# Flake8 配置
[tool.flake8]
max-line-length = 88
max-complexity = 10
```

### tox.ini

**作用：** 配置多版本 Python 测试环境。

**配置示例：**

```ini
[tox]
# 指定要测试的 Python 版本
envlist = py310, py311, py312, py313

# 隔离构建
isolated_build = true

[testenv]
# 外部命令白名单
whitelist_externals = uv

# 安装依赖命令
commands_pre = uv sync --dev

# 运行测试命令
commands = uv run pytest

# 覆盖率报告
commands =
    uv run pytest --cov=src --cov-report=html
    uv run pytest --cov=src --cov-report=term

[testenv:docs]
commands = uv run mkdocs build
```

### .pre-commit-config.yaml

**作用：** 配置 Git pre-commit hooks，在提交前自动运行代码检查。

**主要 hooks：**

```yaml
repos:
  # Black - 代码格式化
  - repo: https://github.com/psf/black
    rev: '24.1.0'
    hooks:
      - id: black
      - id: black-jupyter  # Jupyter notebooks

  # Ruff - 代码检查
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.0
    hooks:
      - id: ruff
      - id: ruff-format

  # nbstripout - Notebook 管理
  - repo: https://github.com/kynan/nbstripout
    rev: 0.8.1
    hooks:
      - id: nbstripout
        args: ['--keep-output']  # 保留输出

  # Interrogate - 文档覆盖率
  - repo: https://github.com/econchick/interrogate
    rev: 1.7.0
    hooks:
      - id: interrogate
        args: [--verbose, --fail-under=80]
```

### makefile

**作用：** 定义常用命令的快捷方式。

**当前命令：**

```makefile
# 安装依赖并初始化
setup:
    @uv sync --all-extras
    @make configure-project

# 运行测试
test:
    uv run pytest

# 生成测试报告
report:
    uv run allure serve tmp/allure_results

# 配置项目
configure-project:
    @uv run python scripts/configure_project.py
```

**添加自定义命令：**

```makefile
# 格式化代码
format:
	@black src/ tests/
	@isort src/ tests/

# 类型检查
typecheck:
	@mypy src/

# 清理临时文件
clean:
	@rm -rf build/ dist/ *.egg-info
	@find . -type d -name __pycache__ -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete

# 构建文档
docs:
	@uv run mkdocs build
```

### .github/workflows/

**作用：** GitHub Actions 工作流配置。

#### release-please.yml

**作用：** 自动化版本发布流程。

主要步骤：
1. 创建 release PR
2. 发布到 PyPI
3. 创建 GitHub release

**配置 PyPI token：**

1. 创建 PyPI API token
2. 添加到 GitHub Secrets：`PYPI_TOKEN`
3. 工作流会自动使用它

## 项目特定配置

### config/config.yaml

**作用：** 应用程序配置文件（如果使用 Hydra 等配置管理工具）。

**示例配置：**

```yaml
# 数据库配置
database:
  host: localhost
  port: 5432
  name: myapp

# API 配置
api:
  host: 0.0.0.0
  port: 8000
  debug: false

# 日志配置
logging:
  level: INFO
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
```

### config/ds/

存储数据集特定的配置文件：

- `mac.yaml` - macOS 特定配置
- `win.yaml` - Windows 特定配置

## 环境变量

**推荐使用：** `.env` 文件（不要提交到版本控制）

```bash
# .env
DATABASE_URL=postgresql://user:pass@localhost/db
API_KEY=your-api-key
DEBUG=True
```

**加载环境变量：**

```python
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
```

## IDE 配置

### VS Code

**.vscode/settings.json（可选创建）：**

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.linting.mypyEnabled": true,
  "python.testing.pytestEnabled": true,
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  }
}
```

### PyCharm

1. 设置 Python 解释器为虚拟环境
2. 启用 Black 格式化
3. 配置 pytest 为测试框架
4. 启用 flake8 和 mypy 检查

## 配置优先级

1. 命令行参数
2. 环境变量
3. `.env` 文件
4. 配置文件（如 `config.yaml`）
5. 默认值

## 自定义配置

### 修改代码风格

编辑 `pyproject.toml`：

```toml
[tool.black]
line-length = 100  # 更改行长度

[tool.ruff]
line-length = 100
```

### 修改 Python 版本

编辑 `pyproject.toml`：

```toml
[project]
requires-python = ">=3.11,<3.14"  # 更新版本要求

[tool.poetry.dependencies]
python = ">=3.11,<3.14"  # 同步更新
```

### 修改测试覆盖率要求

编辑 `pyproject.toml`：

```toml
[tool.interrogate]
fail-under = 90  # 提高到 90%
```

### 添加新工具配置

在 `pyproject.toml` 中添加新配置段：

```toml
[tool.your-tool]
setting1 = "value1"
setting2 = "value2"
```

## 配置管理最佳实践

1. **版本控制：** 提交所有配置文件到版本控制
2. **敏感信息：** 使用环境变量或 secrets
3. **文档化：** 更新本文档以反映配置更改
4. **一致性：** 保持团队配置统一
5. **验证：** 使用 lint 工具验证配置

## 常见配置问题

### Q: 如何修改依赖版本？

A: 编辑 `pyproject.toml`，然后运行：

```bash
uv lock  # uv
poetry lock  # poetry
```

### Q: 如何忽略某些文件/目录？

A: 在各工具的配置段添加 exclude 选项：

```toml
[tool.black]
exclude = '''
/(
    \.git
    | \.venv
    | build
    | dist
)/
'''
```

### Q: 如何使用不同的 Python 版本？

A: 使用 `pyenv` 或其他 Python 版本管理工具：

```bash
pyenv install 3.12.0
pyenv local 3.12.0
```

## 下一步

- 查看 [快速开始指南](quick-start.md)
- 阅读 [工具链说明](tools.md)
- 学习 [开发规范](development.md)
