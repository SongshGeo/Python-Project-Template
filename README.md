# Shuang's Python 项目模板

## 项目结构

```shell
.
├── pyproject.toml
├── README.md
├── src
│   ├── __init__.py
│   └── model
│       ├── __init__.py
│       └── exp.py
└── tests
    ├── __init__.py
    └── test_exp.py
```

## 特性

1. 使用 `Makefile` 进行批量操作
2. 使用 `Hydra` 管理模型参数与配置
3. 使用 `pytest` 进行单元测试
4. 使用 `allure` 生成测试报告
5. 使用 `nbstripout` 管理 Jupyter Notebook 输出
6. 使用 `pre-commit` 进行代码检查
7. 使用 `mkdocs` 生成文档
8. 使用 `poetry` 进行包管理
9. 使用 `jupyter` 进行数据分析
10. 使用 `snakeviz` 进行性能分析
11. 使用 `isort` 进行代码格式化
12. 使用 `flake8` 进行代码检查
13. 使用 `ruff` 进行文档检查
14. 使用 `black` 进行代码格式化
15. 使用 `mypy` 进行类型检查
16. 使用 `coverage` 进行测试覆盖率分析
17. 使用 `release-please` 进行版本管理
18. 使用 `mkdocs-material` 生成美观的文档

## 使用方法

1. 在 GitHub 上创建一个新仓库，使用本模板进行初始化。
2. 克隆仓库到本地。
3. 在本地运行 `make setup` 安装依赖。
4. 开发代码。
5. 在本地运行 `make test` 运行单元测试。
6. 在本地运行 `make report` 生成测试报告。
