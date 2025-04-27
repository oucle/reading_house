#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/27 15:33
# @Author  : BeiGai
# @File    : log_handle.py
# @Software: win10 Tensorflow1.13.1 python3.6.3
import logging
import os
import time

from utils.path_handle import MODULE_DIR

# 日志文件夹
LOG_PATH = MODULE_DIR['log']
# 如果日志文件目录不存在则自动创建日志目录
try:
    if not os.path.exists(LOG_PATH):
        os.makedirs(LOG_PATH)
except Exception as e:
    print(f"创建：{LOG_PATH}目录失败，详情：{e}")


class MyLogger:
    def __init__(self):
        filename = os.path.join(LOG_PATH,'{}.log'.format(time.strftime('%Y%m%d_%H%M%S')))
        formatter = logging.Formatter('[%(asctime)s]-[%(filename)s _%(lineno)d]-[%(levelname)s]- %(message)s')
        self.logger = logging.getLogger('Auto_Test')
        self.logger.setLevel(logging.DEBUG)
        try:
            file_handle = logging.FileHandler(filename, encoding='utf-8')
            console_handle = logging.StreamHandler()
        except Exception as e:
            print(f"创建文件/控制台，日志记录器失败,详情：{e}")
        else:
            file_handle.setLevel(logging.DEBUG)
            console_handle.setLevel(logging.DEBUG)
            try:
                file_handle.setFormatter(formatter)
                console_handle.setFormatter(formatter)
            except Exception as e:
                print(f"设置文件/控制台,日志记录器格式失败，详情：{e}")
            self.logger.addHandler(file_handle)
            self.logger.addHandler(console_handle)

    def get_handle(self):
        return self.logger

logger = MyLogger().get_handle()

if __name__ == '__main__':
    logger.debug("日志调试测试")
