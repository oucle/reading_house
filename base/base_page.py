#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/5/6 14:38
# @Author  : BeiGai
# @File    : base_page.py
# @Software: win10 Tensorflow1.13.1 python3.6.3
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from utils.log_handle import logger
import time


class BasePage:
    def __init__(self,driver):
        self.driver =  driver
        self.driver.implicitly_wait(30) # 设置全局隐式等待15s
        self.wait = WebDriverWait(driver, 15) # 设置初始化显示等待15s
        self.actions =  ActionChains(driver)

    def find_element(self, locator, condition='presence', retry=1, retry_delay=1):
        """
        定位页面元素（支持重试和多种等待条件）

        :param locator: 元素定位器，如 (By.XPATH, "//button")
        :param condition: 等待条件（presence/visibility/clickable/invisibility）
        :param retry: 重试次数（默认1次）
        :param retry_delay: 重试间隔秒数（默认1秒）
        :return: WebElement对象
        :raises: Exception: 元素定位失败时抛出异常
        """
        error_info = None
        ele = None  # 初始化返回值

        # 条件映射表（扩展性强）
        condition_map = {
            'invisibility': EC.invisibility_of_element_located,
            'visibility': EC.visibility_of_element_located,
            'clickable': EC.element_to_be_clickable,
            'presence': EC.presence_of_element_located
        }

        for attempt in range(retry + 1):
            try:
                # 通过映射表获取对应的等待条件
                ec_method = condition_map.get(condition, EC.presence_of_element_located)
                ele = self.wait.until(ec_method(locator))

                logger.info(f"元素定位成功 | 条件: {condition} | 定位器: {locator}")
                return ele  # 直接返回避免break和else的歧义

            except Exception as e:
                error_info = e
                if attempt < retry:
                    logger.warning(f"元素重试中... [{attempt + 1}/{retry}] | 定位器: {locator} | 错误: {str(e)}")
                    time.sleep(retry_delay)

        # 所有重试失败后的处理
        logger.error(f"元素定位失败 | 条件: {condition} | 定位器: {locator}")
        raise Exception(
            f"元素定位失败（条件: {condition}）\n"
            f"定位器: {locator}\n"
            f"最终错误: {str(error_info)}"
        )



