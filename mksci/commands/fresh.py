#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Created date: 2022/3/1
# @Author  : Shuang Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Research Gate: https://www.researchgate.net/profile/Song_Shuang9

import os
import re

import yaml
from new import ROOT, TEMPLATES


def show_files(path, all_files=None, full_path=False, suffix=None):
    """
    All files under the folder.
    :param path: A folder.
    :param all_files: initial list, where files will be saved.
    :param full_path: Save full path or just file name? Default False, i.e., just file name.
    :param suffix: Filter by suffix.
    :return: all_files, a updated list where new files under the path-folder saved, besides of the original input.
    """
    # 首先遍历当前目录所有文件及文件夹
    if not os.path.isdir(path):
        raise FileNotFoundError(f"{path} is not a folder.")
    if all_files is None:
        all_files = []
    if not suffix:
        suffix = []

    file_list = os.listdir(path)
    # 准备循环判断每个元素是否是文件夹还是文件，是文件的话，把名称传入list，是文件夹的话，递归
    for file in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)
        if isinstance(suffix, str):
            judge = not cur_path.endswith(suffix)
        else:
            judge = all([not cur_path.endswith(suf) for suf in suffix])
        if judge:
            continue
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            show_files(cur_path, all_files, full_path)
        else:
            if full_path:
                all_files.append(cur_path)
            else:
                all_files.append(file)
    return all_files


def check_yaml(path):
    """
    If path is a string where YAML file located at,
    return a dictionary by reading that file.
    """
    if isinstance(path, str):
        full_path = os.path.join(ROOT, path)
        if not os.path.isfile(full_path) or not full_path.endswith(".yaml"):
            return path
        else:
            with open(full_path, "r", encoding="utf-8") as file:
                params = yaml.load(file.read(), Loader=yaml.FullLoader)
                file.close()
            return params
    else:
        return path


# Loading CONFIG parameters
CONFIG = check_yaml(os.path.join(ROOT, "config.yaml"))


def find_value(dictionary, keys):
    key = keys.pop(0)
    value = dictionary.get(key)
    value = check_yaml(value)
    if isinstance(value, dict):
        value = find_value(value, keys)
    return value


def fill_out_text(text):
    pattern = r"\{%\s+.*?\s+%\}"
    pattern2 = r"\{%\s+(?P<value>.*?)\s+%\}"

    templates = re.findall(pattern, text)
    for temp in templates:
        keys = re.search(pattern2, temp).group("value").split(":")
        value = find_value(CONFIG, keys)
        text = text.replace(temp, str(value))
    return text


def generate_project_markdown():
    template = os.path.join(TEMPLATES, "docs/repo_readme.md")
    with open(template, "r", encoding="utf-8") as f:
        text = f.read()
        filled_text = fill_out_text(text)
    output_path = os.path.join(ROOT, "README.md")
    with open(output_path, "w") as md:
        md.write(filled_text)


def refresh_links(suffix=None):
    files = show_files(ROOT, suffix=suffix, full_path=True)
    links = CONFIG["links"]
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            text = f.read()
            f.close()
        with open(file, "w", encoding="utf-8") as f:
            for key in links:
                text = text.replace(key, links[key])
            f.write(text)


if __name__ == "__main__":
    generate_project_markdown()
    refresh_links(suffix=".md")
