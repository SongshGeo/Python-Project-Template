# Python 项目模板

一个现代化的 Python 项目模板，集成了最佳实践和完整的开发工具链。

## 快速开始

### 1. 安装 uv（推荐）或 poetry

```bash
# 安装 uv（推荐，更快）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 或安装 poetry
pip install poetry
```

### 2. 创建新项目

```bash
# 克隆此模板
git clone https://github.com/SongshGeo/project_template.git my-project
cd my-project

# 初始化项目（配置项目名称和描述）
make setup

# 手动配置项目（可选，如果 make setup 没有运行）
# 使用 Makefile（推荐，会自动选择包管理器）
make configure-project

# 或直接运行（需要先安装依赖）
python scripts/configure_project.py
```

**配置脚本功能：**
- 更新 `pyproject.toml` 中的 `[project]` 和 `[tool.poetry]` 段
- 更新 GitHub workflow 配置
- 创建/更新 `README.md`
- 清空 `CHANGELOG.md`

**脚本会提示您输入：**
- **项目名称**：将在包名和配置中使用
- **项目描述**：项目的简要描述

### 手动安装依赖（可选）

如果只想安装依赖而不配置项目：

```bash
uv sync --all-extras  # 使用 uv
# 或
poetry install        # 使用 poetry
```

### 3. 开发

```bash
# 运行测试
make test

# 查看测试报告
make report

# 运行 pre-commit 检查
pre-commit run --all-files
```

## 项目结构

```shell
.
├── src/                    # 源代码目录
│   ├── api/                # API 相关
│   ├── core/               # 核心功能
│   └── __init__.py
├── tests/                  # 测试目录
│   ├── conftest.py        # pytest 配置
│   └── helper.py          # 测试辅助函数
├── config/                 # 配置文件目录
│   └── config.yaml        # 主配置文件
├── data/                   # 数据目录
├── docs/                   # 文档目录
├── examples/               # 示例代码
├── scripts/                # 工具脚本
│   └── configure_project.py
├── pyproject.toml          # 项目配置（uv/poetry/pyproject）
├── tox.ini                 # 多版本 Python 测试配置
├── makefile                # Make 命令快捷方式
└── README.md               # 本文件
```

## 特性

1. 使用 `Makefile` 进行批量操作
2. 使用 `Hydra` 管理模型参数与配置
3. 使用 `pytest` 进行单元测试
4. 使用 `allure` 生成测试报告
5. 使用 `nbstripout` 管理 Jupyter Notebook 输出（保留 notebook 输出）
6. 使用 `pre-commit` 进行代码检查
7. 使用 `mkdocs` 生成文档
8. 使用 `uv` 进行包管理（兼容 `poetry`）
9. 使用 `interrogate` 检查文档覆盖率
10. 使用 `jupyter` 进行数据分析
11. 使用 `snakeviz` 进行性能分析
12. 使用 `isort` 进行代码格式化
13. 使用 `flake8` 进行代码检查
14. 使用 `ruff` 进行文档检查
15. 使用 `black` 进行代码格式化
16. 使用 `mypy` 进行类型检查
17. 使用 `coverage` 进行测试覆盖率分析
18. 使用 `tox` 进行多 Python 版本（3.10-3.13）兼容性测试
19. 使用 `release-please` 进行版本管理
20. 使用 `mkdocs-material` 生成美观的文档

## 常见命令

### 开发工作流

```bash
# 安装所有依赖（自动检测并使用 uv 或 poetry）
make setup

# 运行测试（自动适配包管理器）
make test

# 生成测试报告
make report

# 配置项目（修改项目名称、描述等）
make configure-project
```

**注意：** Makefile 会自动检测系统中安装的包管理器（uv 或 poetry），优先使用 uv。如果两者都未安装，会提示错误并告知安装方法。

### 使用 uv（推荐）

```bash
# 安装依赖
uv sync --all-extras

# 运行测试
uv run pytest

# 运行任意 Python 命令
uv run python your_script.py

# 添加新依赖
uv add package-name

# 添加开发依赖
uv add --dev package-name
```

### 使用 poetry（备选）

```bash
# 安装依赖
poetry install

# 运行测试
poetry run pytest

# 添加新依赖
poetry add package-name
```

### 代码质量

```bash
# 安装 pre-commit hooks
pre-commit install

# 手动运行所有检查
pre-commit run --all-files

# 运行特定检查
pre-commit run flake8 --all-files
pre-commit run black --all-files
pre-commit run interrogate --all-files  # 检查文档覆盖率
```

### 多 Python 版本测试

```bash
# 使用 tox 测试多个 Python 版本（3.10-3.13）
tox

# 测试特定版本
tox -e py311

# 查看可用环境
tox list
```

## 文档

!!! info "在线文档"
    访问 [在线文档网站](https://songshgeo.github.io/project_template/) 查看完整的文档和教程。

### 本地查看文档

```bash
# 启动文档服务器（开发模式，支持热重载）
make docs

# 或手动运行
uv run mkdocs serve
poetry run mkdocs serve  # 使用 poetry
```

访问 `http://127.0.0.1:8000` 查看文档。

### 构建文档

```bash
# 构建静态文档站点
make docs-build

# 或手动运行
uv run mkdocs build
```

### 部署文档到 GitHub Pages

文档通过 GitHub Actions 自动部署：

1. 推送代码到 `main` 分支
2. GitHub Actions 自动触发构建
3. 文档部署到 GitHub Pages

**访问地址：** `https://songshgeo.github.io/project_template/`

### 文档章节

- 📖 [快速开始指南](docs/doc/quick-start.md) - 从零开始的详细教程
- 🔧 [工具链说明](docs/doc/tools.md) - 各工具的使用说明和最佳实践
- ⚙️ [配置说明](docs/doc/configuration.md) - 项目配置文件详解
- 📝 [开发规范](docs/doc/development.md) - 代码规范和最佳实践
- 🚀 [部署指南](docs/doc/deployment.md) - 项目部署和发布流程

## 常见问题

### Q: 如何选择 uv 还是 poetry？

**A:** uv 更快、更现代，推荐使用。Poetry 更成熟，可根据项目需求选择。

### Q: 如何开始一个新项目？

**A:** 运行 `make setup` 即可完成配置和依赖安装。

### Q: 如何添加新依赖？

**A:**
```bash
uv add package-name          # 运行时依赖
uv add --dev package-name    # 开发依赖
```

### Q: 如何运行测试？

**A:**
```bash
make test        # 使用 Make
uv run pytest    # 直接运行
```

## 贡献指南

欢迎贡献代码！请遵循以下步骤：

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'feat: Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

请确保：
- 代码通过所有 linter 检查
- 添加适当的测试
- 更新相关文档
- 遵循代码规范

## 许可证

本项目使用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 作者

- **SongshGeo** - [GitHub](https://github.com/SongshGeo) - [Website](https://cv.songshgeo.com/)
