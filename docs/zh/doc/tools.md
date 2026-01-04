# 工具链说明

[中文](tools.md) | [English](https://songshgeo.github.io/project_template/en/doc/tools/)

本模板集成了众多优秀的开发工具，以提高代码质量、开发效率和项目管理。本章节详细说明各个工具的作用和使用方法。

## 包管理

### uv（推荐）

**为什么选择 uv？**
- 极快的安装速度（比 pip 快 10-100 倍）
- 统一的工具（管理虚拟环境、依赖和包）
- 由 astral-sh 开发，Rust 编写
- 兼容 pip 和 PyPI

**常用命令：**

```bash
# 安装依赖
uv sync --all-extras

# 添加依赖
uv add package-name
uv add --dev package-name

# 移除依赖
uv remove package-name

# 运行命令
uv run python script.py
uv run pytest

# 查看依赖树
uv tree

# 导出 requirements.txt
uv pip compile pyproject.toml
```

### poetry（备选）

**为什么保留 poetry？**
- 成熟的工具，社区支持广泛
- 更好的版本控制
- 丰富的插件生态

**常用命令：**

```bash
# 安装依赖
poetry install

# 添加依赖
poetry add package-name
poetry add --group dev package-name

# 移除依赖
poetry remove package-name

# 更新依赖
poetry update

# 运行命令
poetry run python script.py
poetry run pytest
```

## 代码质量

### Black（代码格式化）

**作用：** 自动格式化 Python 代码，确保一致的代码风格。

**配置位置：** `.pre-commit-config.yaml`

**使用：**

```bash
# 自动格式化
black src/ tests/

# 检查是否需要格式化（CI 中使用）
black --check src/

# 格式化 Jupyter notebooks
black --include \.ipynb$ notebooks/
```

**配置选项：** `pyproject.toml` 中的 `[tool.black]` 段

### Ruff（代码检查 + 格式化）

**作用：** 极快的 Python linter 和 formatter（Rust 编写）。

**优势：**
- 速度极快（比 flake8 快 100 倍）
- 集成多个工具（flake8, isort, pyupgrade 等）
- 内置代码格式化功能

**使用：**

```bash
# 检查代码
ruff check src/

# 自动修复
ruff check --fix src/

# 格式化代码
ruff format src/

# 检查所有文件
pre-commit run ruff --all-files
pre-commit run ruff-format --all-files
```

**配置选项：** `pyproject.toml` 中的 `[tool.ruff]` 段

### Flake8（代码检查）

**作用：** 检查 Python 代码风格和错误。

**配置位置：** `pyproject.toml` 中的 `[tool.flake8]` 段

**使用：**

```bash
# 检查代码
flake8 src/ tests/

# 检查单个文件
flake8 src/core/exp.py
```

### isort（导入排序）

**作用：** 自动排序 Python import 语句。

**配置：** 使用 Black 配置文件，确保与 Black 兼容。

**使用：**

```bash
# 自动排序 import
isort src/ tests/

# 检查是否需要排序
isort --check src/
```

### MyPy（类型检查）

**作用：** 静态类型检查，提高代码质量和可维护性。

**使用：**

```bash
# 类型检查
mypy src/

# 忽略缺失的导入（常见于第三方库）
mypy --ignore-missing-imports src/
```

**添加类型注解示例：**

```python
def greet(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"
```

### Interrogate（文档覆盖率）

**作用：** 检查代码的文档覆盖率。

**配置位置：** `pyproject.toml` 中的 `[tool.interrogate]` 段

**使用：**

```bash
# 检查文档覆盖率
interrogate src/

# 指定最低覆盖率
interrogate --fail-under=80 src/

# 查看详细报告
interrogate --verbose src/
```

**提高文档覆盖率：**

```python
class Example:
    """Example class for demonstration."""

    def __init__(self, value: int) -> None:
        """
        Initialize the example.

        Args:
            value: Initial value
        """
        self.value = value

    def get_value(self) -> int:
        """Get the current value."""
        return self.value
```

## 测试

### Pytest

**作用：** Python 测试框架。

**配置文件：** `tests/conftest.py`

**使用：**

```bash
# 运行所有测试
pytest

# 运行特定文件
pytest tests/test_core.py

# 运行特定测试
pytest tests/test_core.py::test_example

# 详细输出
pytest -v

# 显示覆盖率
pytest --cov=src --cov-report=html

# 运行失败的测试
pytest --lf

# 并行运行
pytest -n auto
```

**编写测试示例：**

```python
import pytest
from src.core.example import Example


def test_example():
    """Test example functionality."""
    example = Example(42)
    assert example.get_value() == 42
```

### Tox（多版本测试）

**作用：** 测试多个 Python 版本的兼容性。

**配置文件：** `tox.ini`

**使用：**

```bash
# 运行所有环境
tox

# 测试特定版本
tox -e py311

# 并行运行
tox -p

# 查看可用环境
tox list
```

### Allure（测试报告）

**作用：** 生成美观的测试报告。

**使用：**

```bash
# 运行测试并生成报告
pytest --alluredir=tmp/allure_results

# 查看报告
make report
# 或
allure serve tmp/allure_results
```

## 文档

### MkDocs

**作用：** 生成项目文档网站。

**配置文件：** `mkdocs.yml`（如存在）

**使用：**

```bash
# 启动开发服务器
uv run mkdocs serve

# 构建静态网站
uv run mkdocs build

# 部署到 GitHub Pages
uv run mike deploy 3.10
```

### Jupyter Notebook

**作用：** 交互式数据分析和实验。

**使用：**

```bash
# 启动 Jupyter Lab
uv run jupyter lab

# 启动 Jupyter Notebook
uv run jupyter notebook

# 管理 notebook 输出
nbstripout --keep-output
```

## Pre-commit（Git Hooks）

**作用：** 在提交前自动运行代码检查。

**配置文件：** `.pre-commit-config.yaml`

**使用：**

```bash
# 安装 hooks
pre-commit install

# 手动运行所有检查
pre-commit run --all-files

# 运行特定 hook
pre-commit run black --all-files

# 跳过 hooks（不推荐）
git commit --no-verify
```

## 性能分析

### Snakeviz

**作用：** 可视化 Python 代码的运行时性能。

**使用：**

```python
import cProfile
import pstats
from snakeviz.cli import main

# 分析代码
profiler = cProfile.Profile()
profiler.enable()

# 运行你的代码
your_function()

profiler.disable()
profiler.dump_stats('tmp/profile.stats')

# 启动可视化
main(['tmp/profile.stats'])
```

## 版本管理

### Release Please

**作用：** 自动化版本管理和发布流程。

**配置文件：** `release-please-config.json`

**工作流程：**
1. 推送代码到 main 分支
2. Release Please 自动创建版本 PR
3. 合并 PR 后自动创建 release 和 tag
4. GitHub Actions 自动构建和发布

## 配置最佳实践

### 开发环境

1. 安装 pre-commit hooks
2. 配置 IDE 集成（如 VS Code 的 Python 扩展）
3. 启用自动保存时格式化

### CI/CD

确保 CI 中运行：

```yaml
- pre-commit run --all-files
- pytest
- interrogate --fail-under=80
- tox
```

### 团队协作

- 统一使用相同的工具版本
- 共享 `pyproject.toml` 配置
- 定期更新依赖版本

## 故障排除

### 工具冲突

如果多个工具有冲突（如 isort 和 ruff），建议：
1. 统一使用 ruff（更快）
2. 或配置它们使用相同的设置

### 性能优化

- 使用 ruff 替代 flake8（更快）
- 使用 uv 替代 pip（更快）
- 使用 pytest-xdist 并行运行测试

### 常见错误

**错误：** `command not found: uv`
**解决：** 确保安装了 uv 或在正确版本的 Python 环境中

**错误：** `ModuleNotFoundError`
**解决：** 确保激活了虚拟环境并安装了依赖
