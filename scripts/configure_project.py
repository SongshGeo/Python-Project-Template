#!/usr/bin/env python 3.11.0
# -*-coding:utf-8 -*-
"""
Project configuration script.

This script helps initialize a new Python project by configuring various
files including pyproject.toml, GitHub workflows, README.md, and CHANGELOG.md.

It prompts the user for:
- Project name: Used in package name and configuration files
- Project description: Brief description of the project

Usage:
    python scripts/configure_project.py

Examples:
    Interactive mode:
    $ python scripts/configure_project.py
    项目名称: my-awesome-project
    项目描述: An awesome Python project
    
    Using via Makefile:
    $ make configure-project
"""
# @Author  : Shuang (Twist) Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Website: https://cv.songshgeo.com/

import re
from pathlib import Path

import questionary

README_TEMPLATE = """
# {title}

{description}
"""


def configure_files(project_name: str, project_description: str) -> None:
    """
    Configure project information in configuration files.
    
    This function updates the project name and description in various
    configuration files including pyproject.toml (both [project] and
    [tool.poetry] sections) and GitHub workflow files.
    
    Args:
        project_name: The name of the project to set
        project_description: The description of the project to set
    
    Example:
        >>> configure_files("my-awesome-project", "An awesome Python project")
        ✓ 已更新 pyproject.toml
        ✓ 已更新 .github/workflows/release-please.yml
    """
    # 配置文件路径
    files_to_update = {
        "pyproject.toml": [
            ('name = "songshgeo"', 'name = "' + project_name + '"'),
            ('description = "Template"', 'description = "' + project_description + '"'),
        ],
        ".github/workflows/release-please.yml": [
            ("${project_name}", project_name),
        ],
    }

    # 处理 pyproject.toml 的特殊配置
    pyproject_path = Path("pyproject.toml")
    if pyproject_path.exists():
        content = pyproject_path.read_text(encoding="utf-8")

        # 更新 [project] 段的 name 和 description
        content = content.replace('name = "songshgeo"', 'name = "' + project_name + '"')
        content = content.replace(
            'description = "Template"', 'description = "' + project_description + '"'
        )

        # 更新 [tool.poetry] 段的 name 和 description
        content = re.sub(
            r'(name = "songshgeo")',
            'name = "' + project_name + '"',
            content,
            flags=re.MULTILINE,
        )
        content = re.sub(
            r'(description = "Template")',
            'description = "' + project_description + '"',
            content,
            flags=re.MULTILINE,
        )

        pyproject_path.write_text(content, encoding="utf-8")
        print("✓ 已更新 pyproject.toml")

    # 跳过 pyproject.toml，因为它已经在上面特殊处理了
    for file_path, replacements in files_to_update.items():
        if file_path == "pyproject.toml":
            continue
        path = Path(file_path)
        if path.exists():
            content = path.read_text(encoding="utf-8")
            for old, new in replacements:
                content = content.replace(old, new)
            path.write_text(content, encoding="utf-8")
            print(f"✓ 已更新 {file_path}")
        else:
            print(f"! 警告: 未找到文件 {file_path}")


def setup_description_files(title: str, description: str) -> None:
    """
    Setup project description files.
    
    This function clears the CHANGELOG.md file and creates a new
    README.md with the provided title and description.
    
    Args:
        title: The project title
        description: The project description
    
    Example:
        >>> setup_description_files("My Project", "A great project")
        # Creates README.md with template and clears CHANGELOG.md
    """
    Path("CHANGELOG.md").write_text("", encoding="utf-8")
    Path("README.md").write_text(
        README_TEMPLATE.format(title=title, description=description),
        encoding="utf-8",
    )


def main() -> None:
    """
    Main entry point for the project configuration script.
    
    This function prompts the user for project name and description,
    then configures all project files accordingly.
    
    The script will:
    1. Prompt for project name and description
    2. Update pyproject.toml in both [project] and [tool.poetry] sections
    3. Update GitHub workflow files
    4. Create/update README.md
    5. Clear CHANGELOG.md
    
    Example:
        $ python scripts/configure_project.py
        开始配置项目信息...
        项目名称: my-project
        项目描述: A sample project
        ✓ 已更新 pyproject.toml
        ✓ 已更新 .github/workflows/release-please.yml
        ✨ 项目配置已完成!
    """
    print("开始配置项目信息...")

    # 使用 questionary 获取用户输入
    project_name = questionary.text(
        "项目名称:", validate=lambda text: len(text) > 0
    ).ask()

    project_description = questionary.text(
        "项目描述:", validate=lambda text: len(text) > 0
    ).ask()

    configure_files(project_name, project_description)
    setup_description_files(project_name, project_description)
    print("\n✨ 项目配置已完成!")


if __name__ == "__main__":
    main()
