# Development Guide

[English](development.md) | [中文](https://songshgeo.github.io/project_template/zh/doc/development/)

Coding standards, workflow, and best practices for this template.

## Code Style

### Python style
- Follow [PEP 8]; auto-format with Black (88 cols)
- Meaningful names; add type hints
- Google-style docstrings

Example:

```python
def calculate_total(items: list[dict[str, float]], tax_rate: float = 0.1) -> float:
    """
    Calculate the total price including tax.

    Args:
        items: List of items with 'price'
        tax_rate: Tax rate as decimal

    Returns:
        Total price including tax

    Raises:
        ValueError: If any item is negative
    """
    if not items:
        return 0.0
    subtotal = sum(item["price"] for item in items)
    if subtotal < 0:
        raise ValueError("Total cannot be negative")
    return subtotal * (1 + tax_rate)
```

### Naming
- Files/dirs: lowercase, underscores (`my_module.py`); tests `test_module.py`
- Vars/functions: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE`
- Private: `_internal`, `__for_mangling`

## Docstrings

Use Google style for functions and classes (see examples above and below).

## Type Hints

Basic types and containers:

```python
name: str = "John"
age: int = 30
items: list[str] = ["apple", "banana"]
```

Optional and unions:

```python
from typing import Optional, Union

def find_user(user_id: str) -> Optional[dict]:
    """Find user by ID."""
    ...

def process_value(value: Union[int, str]) -> str:
    """Process integer or string value."""
    return str(value)
```

Generics:

```python
from typing import TypeVar, List

T = TypeVar("T")

def reverse(items: List[T]) -> List[T]:
    """Reverse a list."""
    return items[::-1]
```

## Git Workflow

### Branch naming

```
feature/add-user-authentication
bugfix/fix-login-error
hotfix/critical-security-patch
refactor/improve-api-structure
docs/update-readme
test/add-integration-tests
```

### Conventional Commits

Format:

```
<type>(<scope>): <subject>
```

Types: feat, fix, docs, style, refactor, test, chore.

Example:

```bash
git commit -m "feat: add user authentication"
git commit -m "feat(auth): add OAuth2 login support

- Implement OAuth2 flow
- Add token refresh
- Update session management

Closes #123"
```

### Pre-commit checks

Automatically run before commit:
1. black
2. ruff
3. flake8
4. mypy
5. interrogate
6. isort

Skip (not recommended):

```bash
git commit --no-verify -m "emergency fix"
```

## Testing Standards

### Layout

```
tests/
├── __init__.py
├── conftest.py
├── test_core.py
├── test_api.py
└── integration/
    └── test_integration.py
```

### Writing tests

```python
import pytest
from src.core.example import Example


class TestExample:
    """Test suite for Example."""

    def test_init(self):
        example = Example(42)
        assert example.value == 42

    def test_method_with_valid_input(self):
        example = Example(10)
        assert example.calculate(2) == 20

    def test_method_with_invalid_input(self):
        example = Example(10)
        with pytest.raises(ValueError):
            example.calculate(-1)

    @pytest.mark.parametrize("input_value,expected", [(0, 0), (5, 25), (10, 100)])
    def test_calculate_multiple(self, input_value, expected):
        example = Example(input_value)
        assert example.calculate(input_value) == expected
```

### Coverage targets
- Minimum: 80%
- Core logic: 100%
- Check doc coverage with `interrogate`

## Code Review Checklist

- Functionality: meets requirements; no regressions; error handling present
- Quality: follows style; lint passes; formatted; no type errors
- Tests: unit tests added; passing; coverage ok; integration tests as needed
- Docs: docstrings added; README/CHANGELOG updated if needed
- Other: no secrets; no temp files; CI green

## Performance

- Prefer generators; cache results; choose right data structures; async I/O when helpful

```python
def process_large_dataset(data):
    """Use generator for large data."""
    for item in data:
        yield process_item(item)
```

Profile with `snakeviz`:

```python
import cProfile

def profile_code(func):
    """Profile a function."""
    profiler = cProfile.Profile()
    profiler.enable()
    result = func()
    profiler.disable()
    profiler.dump_stats("profile.stats")
    return result
```

## Best Practices

### Error handling

```python
import logging

logger = logging.getLogger(__name__)

def process_user_data(user_id: str) -> dict:
    """Process user data with proper error handling."""
    try:
        user = get_user(user_id)
        return process(user)
    except UserNotFoundError:
        logger.error("User %s not found", user_id)
        raise
    except Exception as exc:
        logger.error("Unexpected error processing user %s: %s", user_id, exc)
        raise ProcessingError(f"Failed to process user: {exc}") from exc
```

### Logging

```python
import logging

logger = logging.getLogger(__name__)

def important_operation(value: str) -> None:
    """Perform important operation with logging."""
    logger.info("Starting important operation with value: %s", value)
    try:
        result = do_something(value)
        logger.info("Operation completed successfully")
    except Exception as exc:
        logger.error("Operation failed: %s", exc, exc_info=True)
        raise
```

### Resource management

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
```

## Next Steps
- Read [Quick Start](quick-start.md)
- See [Tooling](tools.md)
- Check [Configuration](configuration.md)
