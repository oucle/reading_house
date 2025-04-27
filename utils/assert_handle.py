#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/27 16:04
# @Author  : BeiGai
# @File    : assert_handle.py
# @Software: win10 Tensorflow1.13.1 python3.6.3
from utils.log_handle import logger

# 比较运算符断言字典
ASSERT_COMPARE = {
    '==': lambda a, b : a == b,
    '!=': lambda a , b : a != b,
    '>': lambda a, b : a > b,
    '<': lambda a, b : a < b,
    'in': lambda a, b : a in b
}
def change_str(a, b):
    """强制转换字符串参数"""
    return str(a),str(b)

def assert_compare(a, compare, b):
    """通过比较运算符断言"""
    a, b = change_str(a, b)
    if compare not in ASSERT_COMPARE:
        logger.warning(f"请核查用例断言条件：{a} {compare} {b}")
    else:
        try:
            assert ASSERT_COMPARE[compare](a, b),f"{a} {compare} {b}: 断言失败!!!"
            logger.info(f"{a} {compare} {b}: 断言成功!!!")
        except AssertionError as e:
            logger.error(e)

def startswith(a, b):
    """断言a以b开头"""
    a, b = change_str(a, b)
    try:
        assert a.startswith(b),f"{a} 以 {b} 开头: 断言失败!!!"
        logger.info(f"{a} 以 {b} 开头: 断言成功!!!")
    except AssertionError as e:
        logger.error(e)

def endswith(a, b):
    """断言a以b结尾"""
    a, b = change_str(a, b)
    try:
        assert a.endswith(b),f"{a} 以 {b} 结尾: 断言失败!!!"
        logger.info(f"{a} 以 {b} 结尾: 断言成功!!!")
    except AssertionError as e:
        logger.error(e)



