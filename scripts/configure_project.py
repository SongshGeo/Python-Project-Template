#!/usr/bin/env python 3.11.0
# -*-coding:utf-8 -*-
# @Author  : Shuang (Twist) Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Website: https://cv.songshgeo.com/

from pathlib import Path

import questionary


def configure_files(project_name: str, project_description: str):
    """
    配置项目信息
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

    for file_path, replacements in files_to_update.items():
        path = Path(file_path)
        if path.exists():
            content = path.read_text(encoding="utf-8")
            for old, new in replacements:
                content = content.replace(old, new)
            path.write_text(content, encoding="utf-8")
            print(f"✓ 已更新 {file_path}")
        else:
            print(f"! 警告: 未找到文件 {file_path}")


def remove_ignore_files():
    """
    删除 .gitignore 文件中的 'CHANGELOG.md'
    """
    ignore_file = Path(".gitignore")
    if ignore_file.exists():
        content = ignore_file.read_text(encoding="utf-8")
        content = content.replace("CHANGELOG.md\n", "")
        ignore_file.write_text(content, encoding="utf-8")


def main():
    """
    主函数
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
    remove_ignore_files()
    print("\n✨ 项目配置已完成!")


if __name__ == "__main__":
    main()
