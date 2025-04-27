#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/27 15:09
# @Author  : BeiGai
# @File    : path_handle.py
# @Software: win10 Tensorflow1.13.1 python3.6.3
import os.path

# 项目跟目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 模块目录
MODULE_DIR = {
    'base': os.path.join(BASE_DIR, 'base'), # selenium基本配件目录
    'config': os.path.join(BASE_DIR, 'config'), # 项目配置文件目录
    'download': os.path.join(BASE_DIR, 'download'), # 附件下载目录
    'driver': os.path.join(BASE_DIR, 'driver'), # 浏览器驱动目录
    'img': os.path.join(BASE_DIR, 'img'), # 页面截图目录
    'log': os.path.join(BASE_DIR, 'log'), # 日志目录
    'page': os.path.join(BASE_DIR, 'page'), # WEB页面目录
    'testcase': os.path.join(BASE_DIR, 'testcase'), # 测试用例目录
    'utils': os.path.join(BASE_DIR, 'utils') # 工具目录
}

# 测试参数配置文件
PARAMETRIZE = {
    'data.yaml': os.path.join(MODULE_DIR['config'],'data.yaml'), # yaml参数化测试文件
    'data.xlsx': os.path.join(MODULE_DIR['config'],'data.xlsx') # Excel参数化测试文件
}
# 浏览器驱动
WEB_DRIVER = {
    'chromedriver.exe': os.path.join(MODULE_DIR['driver'],'chromedriver.exe') # 谷歌浏览器驱动
}

if __name__ == '__main__':
    print(BASE_DIR)
    print(MODULE_DIR['page'])
    print(PARAMETRIZE['data.xlsx'])
    print(WEB_DRIVER['chromedriver.exe'])