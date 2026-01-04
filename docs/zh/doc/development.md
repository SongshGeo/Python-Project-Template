# 开发规范

[中文](development.md) | [English](https://songshgeo.github.io/project_template/en/doc/development/)

本文档说明项目的代码规范、开发流程和最佳实践。

## 代码风格

### Python 代码风格

遵循 [PEP 8](https://pep8.org/) 代码风格指南，使用 Black 自动格式化。

**主要规则：**

- 使用 4 个空格缩进（不使用制表符）
- 行长度限制 88 字符（Black 默认）
- 使用有意义的变量名
- 添加类型注解
- 遵循 Google 风格的文档字符串

**示例：**

```python
def calculate_total(items: list[dict[str, float]], tax_rate: float = 0.1) -> float:
    """
    Calculate the total price including tax.

    Args:
        items: List of items with 'price' key
        tax_rate: Tax rate as a decimal (default 0.1)

    Returns:
        Total price including tax

    Raises:
        ValueError: If any item has negative price
    """
    if not items:
        return 0.0

    subtotal = sum(item['price'] for item in items)
    if subtotal < 0:
        raise ValueError("Total cannot be negative")

    return subtotal * (1 + tax_rate)
```

### 命名规范

**文件和目录：**
- 使用小写字母
- 多个单词用下划线分隔：`my_module.py`
- 测试文件：`test_module_name.py`

**变量和函数：**
- 使用 snake_case：`user_name`, `calculate_total()`

**类：**
- 使用 PascalCase：`UserProfile`, `DatabaseConnection`

**常量：**
- 使用大写和下划线：`MAX_RETRIES = 3`

**私有成员：**
- 使用单下划线前缀：`_internal_method()`
- 使用双下划线前缀避免命名冲突：`__class_attribute`

## 文档字符串

### Google 风格文档字符串

```python
def process_data(input_data: dict[str, Any], validate: bool = True) -> dict[str, Any]:
    """
    Process input data according to specified rules.

    This function takes a dictionary of input data and processes it according
    to the rules defined in the configuration.

    Args:
        input_data: Dictionary containing the input data to process.
                    Must contain 'id' and 'value' keys.
        validate: Whether to validate the input data before processing.
                 Defaults to True.

    Returns:
        Dictionary containing the processed data with the following structure:
        - 'id': Original ID
        - 'processed_value': Processed value
        - 'timestamp': Processing timestamp

    Raises:
        ValueError: If input_data is empty or missing required keys.
        TypeError: If input_data is not a dictionary.

    Example:
        >>> data = {'id': '123', 'value': 'test'}
        >>> result = process_data(data)
        >>> print(result['id'])
        '123'

    Note:
        This function modifies the input dictionary in place if validate=False.
    """
    if not isinstance(input_data, dict):
        raise TypeError("input_data must be a dictionary")

    if not input_data:
        raise ValueError("input_data cannot be empty")

    # Implementation here
    return processed_result
```

### 类文档字符串

```python
class UserManager:
    """
    Manages user accounts and authentication.

    This class provides methods for creating, updating, and deleting user
    accounts, as well as handling authentication and authorization.

    Attributes:
        db_connection: Database connection instance
        cache: Cache instance for storing user sessions

    Example:
        >>> manager = UserManager(db_connection)
        >>> user = manager.create_user('john@example.com', 'password123')
        >>> print(user.id)
        'user_123'
    """

    def __init__(self, db_connection: Database, cache: Cache) -> None:
        """
        Initialize UserManager.

        Args:
            db_connection: Database connection instance
            cache: Cache instance for storing user sessions
        """
        self.db_connection = db_connection
        self.cache = cache
```

## 类型注解

### 基本类型

```python
# 基本类型
name: str = "John"
age: int = 30
price: float = 19.99
is_active: bool = True

# 容器类型（Python 3.9+）
items: list[str] = ["apple", "banana"]
counts: dict[str, int] = {"apple": 5, "banana": 3}

# 容器类型（Python 3.8 及更早）
from typing import List, Dict
items: List[str] = ["apple", "banana"]
counts: Dict[str, int] = {"apple": 5}
```

### 可选类型

```python
from typing import Optional

def find_user(user_id: str) -> Optional[dict]:
    """
    Find user by ID.

    Args:
        user_id: User identifier

    Returns:
        User dictionary if found, None otherwise
    """
    # Implementation
    pass
```

### 多种类型

```python
from typing import Union

def process_value(value: Union[int, str]) -> str:
    """Process integer or string value."""
    return str(value)
```

### 泛型函数

```python
from typing import TypeVar, List

T = TypeVar('T')

def reverse(items: List[T]) -> List[T]:
    """Reverse a list of items."""
    return items[::-1]
```

## Git 工作流

### 分支命名规范

```
feature/add-user-authentication
bugfix/fix-login-error
hotfix/critical-security-patch
refactor/improve-api-structure
docs/update-readme
test/add-integration-tests
```

### 提交消息规范

遵循 [Conventional Commits](https://www.conventionalcommits.org/)：

**格式：**

```
<type>(<scope>): <subject>

<body>

<footer>
```

**类型：**

- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更改
- `style`: 代码格式（不影响代码运行）
- `refactor`: 重构
- `test`: 添加或修改测试
- `chore`: 构建过程或辅助工具的变动

**示例：**

```bash
# 简单提交
git commit -m "feat: add user authentication"

# 详细提交
git commit -m "feat(auth): add OAuth2 login support

- Implement OAuth2 authentication flow
- Add token refresh mechanism
- Update user session management

Closes #123"
```

### Pre-commit 检查

提交前会自动运行以下检查：

1. **black** - 代码格式化
2. **ruff** - 代码检查
3. **flake8** - 代码风格
4. **mypy** - 类型检查
5. **interrogate** - 文档覆盖率
6. **isort** - Import 排序

**跳过检查（不推荐）：**

```bash
git commit --no-verify -m "emergency fix"
```

## 测试规范

### 测试文件组织

```
tests/
├── __init__.py
├── conftest.py           # Pytest 配置
├── test_core.py          # 核心功能测试
├── test_api.py           # API 测试
└── integration/          # 集成测试
    └── test_integration.py
```

### 编写测试

```python
import pytest
from src.core.example import Example


class TestExample:
    """Test suite for Example class."""

    def test_init(self):
        """Test Example initialization."""
        example = Example(42)
        assert example.value == 42

    def test_method_with_valid_input(self):
        """Test method with valid input."""
        example = Example(10)
        result = example.calculate(2)
        assert result == 20

    def test_method_with_invalid_input(self):
        """Test method with invalid input raises error."""
        example = Example(10)
        with pytest.raises(ValueError):
            example.calculate(-1)

    @pytest.mark.parametrize("input_value,expected", [
        (0, 0),
        (5, 25),
        (10, 100),
    ])
    def test_calculate_multiple(self, input_value, expected):
        """Test calculate with multiple inputs."""
        example = Example(input_value)
        assert example.calculate(input_value) == expected
```

### 测试覆盖率要求

- 最低覆盖率：80%
- 核心功能：100%
- 使用 `interrogate` 检查文档覆盖率

## 代码审查

### Pull Request 检查清单

**功能：**
- [ ] 代码实现符合需求
- [ ] 没有破坏现有功能
- [ ] 添加了适当的错误处理

**代码质量：**
- [ ] 代码符合风格指南
- [ ] 通过了所有 lint 检查
- [ ] 代码已格式化
- [ ] 没有类型错误

**测试：**
- [ ] 添加了单元测试
- [ ] 测试通过
- [ ] 覆盖率满足要求
- [ ] 集成测试通过（如适用）

**文档：**
- [ ] 添加了文档字符串
- [ ] 更新了 README（如需要）
- [ ] 更新了 CHANGELOG（如需要）

**其他：**
- [ ] 没有提交敏感信息
- [ ] 没有提交临时文件
- [ ] CI 检查通过

## 性能优化

### 代码性能

1. **使用生成器** 节省内存
2. **缓存计算结果** 避免重复计算
3. **使用适当的数据结构** 提高查找速度
4. **异步 I/O** 提高并发性能

```python
# 好的实践
def process_large_dataset(data):
    """Process large dataset using generator."""
    for item in data:
        yield process_item(item)

# 避免
def process_large_dataset(data):
    """Process large dataset."""
    results = []
    for item in data:
        results.append(process_item(item))
    return results
```

### 性能分析

使用 `snakeviz` 进行性能分析：

```python
import cProfile
import pstats

def profile_code(func):
    """Profile a function."""
    profiler = cProfile.Profile()
    profiler.enable()
    result = func()
    profiler.disable()
    profiler.dump_stats('profile.stats')
    return result
```

## 最佳实践

### 错误处理

```python
import logging

logger = logging.getLogger(__name__)

def process_user_data(user_id: str) -> dict:
    """Process user data with proper error handling."""
    try:
        user = get_user(user_id)
        return process(user)
    except UserNotFoundError:
        logger.error(f"User {user_id} not found")
        raise
    except Exception as e:
        logger.error(f"Unexpected error processing user {user_id}: {e}")
        raise ProcessingError(f"Failed to process user: {e}") from e
```

### 日志记录

```python
import logging

logger = logging.getLogger(__name__)

def important_operation(value: str) -> None:
    """Perform important operation with logging."""
    logger.info(f"Starting important operation with value: {value}")

    try:
        result = do_something(value)
        logger.info(f"Operation completed successfully")
    except Exception as e:
        logger.error(f"Operation failed: {e}", exc_info=True)
        raise
```

### 资源管理

```python
from contextlib import contextmanager

@contextmanager
def managed_resource(resource):
    """Context manager for resource management."""
    try:
        resource.open()
        yield resource
    finally:
        resource.close()

# 使用
with managed_resource(resource):
    # 使用资源
    pass
```

## 下一步

- 查看 [快速开始指南](quick-start.md)
- 阅读 [工具链说明](tools.md)
- 学习 [配置说明](configuration.md)
