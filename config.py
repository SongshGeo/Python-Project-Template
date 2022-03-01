#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Created date: 2022/2/22
# @Author  : Shuang Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Research Gate: https://www.researchgate.net/profile/Song_Shuang9

import logging
import os

ROOT = "/Users/songshgeo/Documents/Pycharm/PPTemplate_PMT_2022"

# BASIC testing settings.
LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(filename)s %(message)s "
DATE_FORMAT = "%Y-%m-%d  %H:%M:%S %a "

# log file paths
TEST_LOG_PATH = os.path.join(ROOT, "docs/logs/test_logs/tests.log")
ANALYSIS_LOG_PATH = os.path.join(ROOT, "docs/logs/analysis_logs/analysis.log")

# log levels
FILE_LEVEL = logging.DEBUG
CMD_LEVEL = logging.WARNING

log = logging.getLogger(__name__)


def set_logger(reset=False):
    if reset:
        for path in [TEST_LOG_PATH, ANALYSIS_LOG_PATH]:
            if not os.path.exists(path):
                raise FileNotFoundError(f"Test log file not found in {path}.")
            else:
                os.remove(path)
    test_logger = logging.getLogger("TEST")
    analysis_logger = logging.getLogger("ANALYSIS")

    # 建立一个 FileHandler 来把日志记录在文件里
    test_fh = logging.FileHandler(TEST_LOG_PATH)
    analysis_fh = logging.FileHandler(ANALYSIS_LOG_PATH)
    for fh in [test_fh, analysis_fh]:
        fh.setLevel(FILE_LEVEL)
        fh.setFormatter(logging.Formatter(LOG_FORMAT))
    test_logger.addHandler(test_fh)
    analysis_logger.addHandler(analysis_fh)

    # 建立一个 StreamHandler 来把日志打在CMD窗口上
    ch = logging.StreamHandler()
    ch.setLevel(CMD_LEVEL)
    ch.setFormatter(logging.Formatter(LOG_FORMAT))
    for logger in [test_logger, analysis_logger]:
        logger.setLevel(FILE_LEVEL)
        logger.addHandler(ch)
        logger.info(f"Log file set, level {FILE_LEVEL}, cmd level {CMD_LEVEL}")
    # 返回两个日志器
    return test_logger, analysis_logger


LOG_T, LOG_A = set_logger()
