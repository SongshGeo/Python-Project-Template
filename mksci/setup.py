#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Created date: 2022/3/1
# @Author  : Shuang Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Research Gate: https://www.researchgate.net/profile/Song_Shuang9

from setuptools import find_packages, setup

setup(
    name="mkpro-sci",
    version="0.1",
    keywords=("mksci"),
    description="eds sdk",
    long_description="Testing",
    license="MIT Licence",
    url="https://github.com/SongshGeo",
    author="SongshGeo",
    author_email="songshgeo@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[],
    scripts=[],
    entry_points={"console_scripts": ["test = test.help:main"]},
)
