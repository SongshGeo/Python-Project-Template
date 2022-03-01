#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Created date: 2022/3/1
# @Author  : Shuang Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Research Gate: https://www.researchgate.net/profile/Song_Shuang9

import logging
import os
import sys

ROOT = os.getcwd()
log = logging.getLogger(__name__)
# package path
path_mksci = os.path.abspath(os.path.join(sys.argv[0], "../.."))
TEMPLATES = os.path.join(path_mksci, "templates")

with open(
    os.path.join(TEMPLATES, "config_temp.yaml"), "r", encoding="utf-8"
) as file:
    config_yaml = file.read()
    file.close()

config_py = f"""
import logging
import os

ROOT = "{ROOT}"
"""


def new(output_dir):
    config_path = os.path.join(output_dir, "config.py")
    yaml_path = os.path.join(output_dir, "config.yaml")
    if os.path.exists(config_path):
        log.info("Project already exists.")
        return

    log.info(f"Writing config file: {config_path}")
    with open(config_path, "w", encoding="utf-8") as f:
        f.write(config_py)

    log.info(f"Writing initial config yaml: {yaml_path}")
    with open(yaml_path, "w", encoding="utf-8") as f:
        f.write(config_yaml)


if __name__ == "__main__":
    new(ROOT)
