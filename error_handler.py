# -*- coding: utf-8 -*-
# @Time    : 2020/9/28 11:01
# @Author  : Enmo Ren
# @FileName: error_handler.py
# @Software: PyCharm
import sys


def error_exit(message):
    sys.stderr.write(message)
    sys.exit(1)