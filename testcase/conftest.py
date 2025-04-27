#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/27 16:36
# @Author  : BeiGai
# @File    : conftest.py
# @Software: win10 Tensorflow1.13.1 python3.6.3
import time
import allure
import pytest

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from typing import Optional
from selenium import webdriver
from utils.path_handle import WEB_DRIVER, URL, FAILURES, MODULE_DIR
from utils.log_handle import logger
import os

def create_driver()-> Optional[WebDriver]:
    """创建浏览器驱动对象"""
    # 谷歌浏览器驱动地址
    driver_path = WEB_DRIVER['chromedriver.exe']
    options = Options()
    options.add_experimental_option('detach', True)  # 设置浏览器不自动关闭
    # 隐藏自动化测试提示
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    service = Service(driver_path)
    try:
        driver = webdriver.Chrome(options=options, service=service)
        logger.info(f"实例化浏览器驱动对象：{driver}")
        return driver
    except Exception as e:
        logger.error(f"实例化浏览器驱动对象失败，详情：{e}")
        return None

def open_url(driver)-> bool:
    """打开目标网址"""
    try:
        driver.get(URL)
        logger.info(f"打开目标网址：{URL}")
    except Exception as e:
        logger.error(f'打开目标网址失败，详情：{e}')
        return True
    else:
        driver.fullscreen_window() # 窗口全屏显示
        return False

def write_failure_info(item, rep):
    """写入测试用例失败信息"""
    try:
        with open(FAILURES, mode='a', encoding='utf-8')as f:
            if 'tmpdir' in item.fixturenames:
                extra = '%s()' % item.funcargs['tmpdir']
            else:
                extra = ''
            f.write(rep.nodeid + extra + '\n')
            logger.info(f"测试用例断言失败，详细信息写入成功，地址：{FAILURES}")
    except Exception as e:
        logger.error(f"测试用例断言失败，详细信息写入失败文件失败，详情：{e}")

def save_screenshot(driver):
    """保存用例断言失败截图"""
    img_path = os.path.join(MODULE_DIR['img'],'{}.png'.format(str(round(time.time()*1000))))
    try:
        driver.save_screenshot(img_path)
        logger.info(f"保存截图成功，地址：{img_path}")
        return img_path
    except Exception as e:
        logger.error(f"保存截图失败，详情：{e}")
        return None

def add_screenshot_to_allure(driver):
    """将测试用例失败截图添加到Allure报告"""
    if hasattr(driver, ''):
        try:
            with allure.step("添加用例断言失败截图"):
                allure.attach(driver.get_screenshort_as_png,"添加失败截图",allure.attachment_type.PNG)
                logger.info("allure测试报告添加错误截图成功")
        except Exception as e:
            logger.error(f"allure测试报告添加错误截图失败，详情：{e}")

@pytest.fixture(scope='session')
def driver1(request):
    driver = create_driver()
    if driver:
        if open_url(driver):
            def end():
                driver.quit() # 关闭浏览器，
                time.sleep(1)
                request.addfinalizer(end)
            return driver
    return None

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    # 以下为实现异常截图的代码：
    # rep.when可选参数有call、setup、teardown，
    # call表示为用例执行环节、setup、teardown为环境初始化和清理环节
    # 这里只针对用例执行且失败的用例进行异常截图
    if rep.when == 'call' and rep.failed:
        write_failure_info(item, rep)
        if 'driver1' in item.funcargs:
            driver = item.funcargs['driver1']
            save_screenshot(driver)
            add_screenshot_to_allure(driver)
