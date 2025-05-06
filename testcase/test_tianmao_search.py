#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/27 17:36
# @Author  : BeiGai
# @File    : test_tianmao_search.py
# @Software: win10 Tensorflow1.13.1 python3.6.3
from page.tianmao_homepage import TianMaoHomePage
from utils.assert_handle import assert_compare

class TestTianMaoSearch:
    def test_search(self, driver1):
        page = TianMaoHomePage(driver1)
        page.find_element(page.search_input).send_keys("1+13")
