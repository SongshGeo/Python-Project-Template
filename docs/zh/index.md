# Python 项目模板

[中文](index.md) | [English](https://songshgeo.github.io/project_template/en/)

一个现代化的 Python 项目模板，集成了最佳实践和完整的开发工具链。

!!! info "特性"
    - 🚀 使用 `uv`（或 `poetry`）进行包管理
    - 🧪 使用 `pytest` 进行单元测试，`tox` 进行多版本测试
    - 📊 使用 `allure` 生成美观的测试报告
    - 🔧 使用 `pre-commit` 进行代码质量检查
    - 📝 使用 `mkdocs` 生成文档网站
    - 🎯 使用 `interrogate` 确保文档覆盖率
    - 🔍 使用 `ruff`, `flake8`, `mypy` 进行代码检查

## 快速开始

### 1. 安装 uv（推荐）

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. 创建新项目

```bash
# 克隆模板
git clone https://github.com/SongshGeo/project_template.git my-project
cd my-project

# 初始化项目
make setup
```

### 3. 开始开发

```bash
# 运行测试
make test

# 查看测试报告
make report

# 运行代码检查
pre-commit run --all-files
```

!!! tip "需要帮助？"
    查看[快速开始指南](doc/quick-start.md)了解详细信息。

## 项目结构

```tree
.
├── src/                    # 源代码
├── tests/                  # 测试
├── config/                 # 配置文件
├── docs/                   # 文档
├── scripts/                # 工具脚本
├── pyproject.toml          # 项目配置
├── makefile                # 快捷命令
└── README.md               # 项目说明
```

## 主要功能

### 包管理
- **uv**（推荐）：极快的包管理器
- **poetry**（备选）：成熟的包管理器

### 代码质量
- Black：代码格式化
- Ruff：极快的代码检查
- Flake8：代码风格检查
- MyPy：类型检查
- Interrogate：文档覆盖率

### 测试框架
- Pytest：单元测试
- Tox：多版本测试（Python 3.10-3.13）
- Allure：测试报告
- Coverage：测试覆盖率

### 文档工具
- MkDocs：文档生成
- Material 主题：美观的文档网站

## 文档导航

!!! tip "文档导航"
    点击下方链接快速查看各个章节：

    - 📖 [快速开始](doc/quick-start.md) - 从零开始的详细教程
    - 🔧 [工具链说明](doc/tools.md) - 各工具的使用说明和最佳实践
    - ⚙️ [配置说明](doc/configuration.md) - 项目配置文件详解
    - 📝 [开发规范](doc/development.md) - 代码规范和最佳实践
    - 🚀 [部署指南](doc/deployment.md) - 项目部署和发布流程

## 特性清单

| 功能 | 工具 | 说明 |
|------|------|------|
| 包管理 | uv, poetry | 现代化的依赖管理 |
| 代码格式化 | Black, Ruff | 统一的代码风格 |
| 代码检查 | Ruff, Flake8, MyPy | 多层代码质量保证 |
| 测试框架 | Pytest, Tox | 全面的测试支持 |
| 测试报告 | Allure | 美观的测试报告 |
| 文档生成 | MkDocs | 专业的文档网站 |
| 文档覆盖率 | Interrogate | 确保代码有文档 |
| 代码提交 | Pre-commit | 提交前自动检查 |
| 版本管理 | Release Please | 自动化版本发布 |
| 类型检查 | MyPy | 静态类型检查 |
| 性能分析 | Snakeviz | 代码性能可视化 |

## 常用命令

```bash
# 安装依赖
make setup

# 运行测试
make test

# 查看测试报告
make report

# 配置项目
make configure-project
```

## 许可证

本项目使用 MIT 许可证。

## 贡献

欢迎贡献代码！请遵循以下步骤：

1. Fork 本仓库
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 相关链接

- 📖 [详细文档](doc/quick-start.md)
- 🔧 [GitHub 仓库](https://github.com/SongshGeo/project_template)
- 👤 [作者主页](https://cv.songshgeo.com/)
