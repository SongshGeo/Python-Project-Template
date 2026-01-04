# 部署指南

[中文](deployment.md) | [English](https://songshgeo.github.io/project_template/en/doc/deployment/)

本文档说明如何构建、测试和部署 Python 项目。

## 本地构建

### 安装依赖

```bash
# 使用 uv
uv sync --all-extras

# 使用 poetry
poetry install
```

### 运行测试

```bash
# 使用 Make
make test

# 直接运行
uv run pytest

# 生成测试报告
make report
```

### 代码质量检查

```bash
# 运行所有检查
pre-commit run --all-files

# 格式化代码
black src/ tests/
ruff format src/ tests/

# 运行 linter
ruff check src/
flake8 src/

# 类型检查
mypy src/

# 文档覆盖率
interrogate src/
```

## 构建包

### 使用 uv 构建

```bash
# 构建 Wheel 和 Source Distribution
uv build

# 输出目录
ls dist/
```

### 使用 poetry 构建

```bash
# 构建包
poetry build

# 输出目录
ls dist/
```

### 验证构建

```bash
# 检查包内容
tar -tzf dist/*.tar.gz

# 安装并测试
pip install dist/*.whl
python -c "import your_package"
```

## 版本管理

### 自动版本管理（推荐）

项目使用 [release-please](https://github.com/googleapis/release-please) 自动管理版本：

1. 提交代码到 `main` 分支
2. Release Please 自动创建版本 PR
3. 合并 PR 后自动创建 GitHub release

**配置：** `release-please-config.json`

### 手动版本管理

```bash
# 更新版本号（pyproject.toml）
# [project]
# version = "1.2.0"

# 更新 CHANGELOG.md
# 提交更改
git add pyproject.toml CHANGELOG.md
git commit -m "chore: bump version to 1.2.0"

# 创建 tag
git tag -a v1.2.0 -m "Release version 1.2.0"
git push origin main --tags
```

## 发布到 PyPI

### 配置 PyPI Token

1. 登录 [PyPI](https://pypi.org/)
2. 访问 [Account settings](https://pypi.org/manage/account/)
3. 创建 API token
4. 添加到 GitHub Secrets：`PYPI_TOKEN`

### 自动发布（推荐）

GitHub Actions 会自动在以下情况发布到 PyPI：

1. Release Please 创建新版本
2. 合并 version PR
3. 触发 `.github/workflows/release-please.yml`

### 手动发布

#### 使用 uv

```bash
# 构建
uv build

# 发布到 PyPI
uv publish --token YOUR_PYPI_TOKEN

# 发布到 TestPyPI（测试）
uv publish --publish-url https://test.pypi.org/legacy/
```

#### 使用 poetry

```bash
# 配置 PyPI token
poetry config pypi-token.pypi YOUR_PYPI_TOKEN

# 发布
poetry publish

# 发布到 TestPyPI
poetry publish --repository testpypi
```

#### 使用 twine

```bash
# 安装 twine
pip install twine

# 上传到 PyPI
twine upload dist/*

# 上传到 TestPyPI
twine upload --repository testpypi dist/*
```

## 版本兼容性测试

### 使用 tox

```bash
# 测试所有 Python 版本（3.10-3.13）
tox

# 测试特定版本
tox -e py311

# 并行运行
tox -p

# 跳过环境安装
tox --notest
```

### CI 中运行

GitHub Actions 配置：

```yaml
name: Test

on: [push, pull_request]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        python-version: ['3.10', '3.11', '3.12', '3.13']
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install uv
        run: curl -LsSf https://astral.sh/uv/install.sh | sh
      - name: Install dependencies
        run: uv sync --all-extras
      - name: Run tests
        run: uv run pytest
      - name: Run checks
        run: pre-commit run --all-files
```

## 容器化部署

### Dockerfile 示例

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# 安装 uv
RUN pip install uv

# 复制依赖文件
COPY pyproject.toml uv.lock ./

# 安装依赖
RUN uv sync --frozen

# 复制源代码
COPY src/ ./src/

# 运行应用
CMD ["uv", "run", "python", "-m", "src.main"]
```

### 构建镜像

```bash
# 构建
docker build -t myapp:latest .

# 运行
docker run -p 8000:8000 myapp:latest
```

## 持续集成/持续部署

### GitHub Actions 配置

#### 测试工作流

**.github/workflows/test.yml：**

```yaml
name: Test

on:
  push:
    branches: [main, dev]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12', '3.13']

    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install uv
        run: curl -LsSf https://astral.sh/uv/install.sh | sh

      - name: Install dependencies
        run: uv sync --all-extras

      - name: Run tests
        run: uv run pytest

      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage.xml
```

#### 发布工作流

已经配置在 `.github/workflows/release-please.yml`

## 文档部署

### MkDocs

```bash
# 本地预览
uv run mkdocs serve

# 构建静态站点
uv run mkdocs build

# 部署到 GitHub Pages
uv run mike deploy 3.10 -p
```

### GitHub Pages

1. 设置 GitHub Pages 源为 `gh-pages` 分支
2. 使用 GitHub Actions 自动部署

**示例工作流：**

```yaml
name: Deploy Docs

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Install uv
        run: curl -LsSf https://astral.sh/uv/install.sh | sh
      - name: Install dependencies
        run: uv sync --extras docs
      - name: Build docs
        run: uv run mkdocs build
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site
```

## 环境配置

### 生产环境检查清单

- [ ] 使用生产级 WSGI 服务器（如 Gunicorn）
- [ ] 启用 HTTPS
- [ ] 配置日志记录
- [ ] 设置环境变量
- [ ] 配置监控和告警
- [ ] 备份数据库
- [ ] 配置防火墙

### 环境变量

```bash
# .env.production
DATABASE_URL=postgresql://user:pass@host:5432/dbname
SECRET_KEY=your-secret-key
DEBUG=False
LOG_LEVEL=INFO
```

## 监控和日志

### 日志配置

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
```

### 健康检查

```python
from flask import Flask

app = Flask(__name__)

@app.route('/health')
def health_check():
    """Health check endpoint."""
    return {'status': 'healthy'}, 200
```

## 故障排除

### 常见问题

**Q: 构建失败怎么办？**

A: 检查以下几点：
1. Python 版本是否符合要求
2. 依赖版本是否兼容
3. 运行 `uv sync --all-extras` 更新依赖
4. 检查错误日志

**Q: 测试覆盖率不够怎么办？**

A:
```bash
# 查看覆盖率报告
pytest --cov=src --cov-report=html
open htmlcov/index.html
```

**Q: PyPI 发布失败怎么办？**

A:
1. 检查 API token 是否正确
2. 确保包名称唯一
3. 运行 `uv build` 检查构建文件

**Q: 如何回滚版本？**

A:
```bash
# 创建回滚 tag
git tag -a v1.0.0-rollback -m "Rollback to 1.0.0"

# 重新发布旧版本
# 需要从 Git 历史中恢复旧版本
```

## 下一步

- 查看 [快速开始指南](quick-start.md)
- 阅读 [工具链说明](tools.md)
- 学习 [开发规范](development.md)
