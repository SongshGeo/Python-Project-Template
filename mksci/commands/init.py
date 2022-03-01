#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Created date: 2022/3/1
# @Author  : Shuang Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Research Gate: https://www.researchgate.net/profile/Song_Shuang9

import os

import click
from fresh import CONFIG, ROOT, TEMPLATES, check_yaml


def make_dirs(path=None, structure=None):
    # TODO docs
    if not structure:
        structure = check_yaml(CONFIG["structure"])
    if not path:
        path = ROOT
    for folder in structure:
        expect_path = os.path.join(path, folder)
        if os.path.exists(expect_path) and os.path.isdir(expect_path):
            print(f"{expect_path} made")  # TODO log
            pass
        else:
            os.mkdir(expect_path)
            print(f"{expect_path} made.")  # TODO log
        if isinstance(structure[folder], dict):
            make_dirs(path=expect_path, structure=structure[folder])


def initiate():
    os.system(
        f"cp -R {os.path.join(TEMPLATES, 'init/.')} {os.path.join(ROOT, '.')}"
    )


def playground():
    # TODO find path of notebook
    os.system(
        f"cp {os.path.join(TEMPLATES, 'scripts/playground.ipynb')} {os.path.join(ROOT, 'notebooks/.')}"
    )


@click.command(name="init")
@click.option("-g", default="", help="input your")
def init():
    """
    Initiate the repo.
    --all:
    :return:
    """
    click.echo("Init repo.")
    pass


if __name__ == "__main__":
    initiate()
    make_dirs()
    playground()
