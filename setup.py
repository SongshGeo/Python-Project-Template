#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Created date: 2022/3/1
# @Author  : Shuang Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Research Gate: https://www.researchgate.net/profile/Song_Shuang9

from setuptools import find_packages, setup

from mksci import __version__, description

setup(
    name="mkpro-sci",
    version=__version__,
    keywords=("mksci"),
    description="Scientific Python Project automatic manager",
    long_description=description,
    license="MIT Licence",
    url="https://github.com/SongshGeo",
    author="SongshGeo",
    author_email="songshgeo@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    platforms="any",
    install_requires=["requests"],
    scripts=[],
    entry_points={"console_scripts": ["mksci = mksci.__main__:cli"]},
)
