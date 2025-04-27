#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/27 11:12
# @Author  : BeiGai
# @File    : run.py
# @Software: win10 Tensorflow1.13.1 python3.6.3
import time
import pytest
import os

if __name__ == '__main__':
    pytest.main()
    time.sleep(3)
    os.system('allure generate ./allure-results -o ./allure-report --clean')
    os.system('allure open ./allure-report')