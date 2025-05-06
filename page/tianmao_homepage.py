#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/5/6 15:44
# @Author  : BeiGai
# @File    : tianmao_homepage.py
# @Software: win10 Tensorflow1.13.1 python3.6.3
import sys
from utils.path_handle import MODULE_DIR
base_path = MODULE_DIR['base']
sys.path.append(base_path)
print(sys.path)
from base.base_page import BasePage
from selenium.webdriver.common.by import By

class TianMaoHomePage(BasePage):
    search_input = (By.XPATH, '//input[@id="q" and @name="q"]')