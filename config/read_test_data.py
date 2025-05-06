#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/27 20:31
# @Author  : BeiGai
# @File    : read_test_data.py
# @Software: win10 Tensorflow1.13.1 python3.6.3
import pandas as pd
from utils.path_handle import PARAMETRIZE
from utils.log_handle import logger
import yaml
import mysql.connector

def read_xlsx_data(filepath,sheet_name):
    """读取xlsx文件测试数据"""
    try:
        df = pd.read_excel(filepath,sheet_name=sheet_name)
        logger.info(f"读取xlsx文件：{filepath}的sheet页：{sheet_name}成功！！")
    except Exception as e:
        logger.error(f"读取xlsx文件：{filepath}的sheet页：{sheet_name}失败，详情：{e}")
    else:
        result = df.to_dict(orient='records')
        return result

def read_yaml_data(filepath):
    """读取yaml文件测试数据"""
    result = []
    try:
        with open(filepath)as f:
            data = yaml.load(f.read(),Loader=yaml.SafeLoader)
        logger.info(f"读取yaml文件：{filepath}测试数据成功！！")
    except Exception as e:
        logger.error(f"读取yaml文件：{filepath}测试数据失败，详情：{e}")
    else:
        test = data['tests']
        return test

def read_mysql_data(localhost, use, pas, db, table):
    """读取MySQL数据库数据表测试数据"""
    try:
        conn = mysql.connector.connect(
            host = localhost,
            user = use,
            password = pas,
            database = db
        )
        logger.info("连接数据库成功！！")
    except ConnectionError as e:
        logger.error(f"连接数据库失败，详情：{e}")
    else:
        my_cur = conn.cursor()
        sql = 'SELECT * FROM {}'.format(table)
        try:
            my_cur.execute(sql)
            logger.info("执行sql语句成功！！")
        except Exception as e:
            logger.error(f"执行sql语句发生错误，详情：{e}")
        else:
            result = my_cur.fetchall()
            return result

if __name__ == '__main__':
    local = '127.0.0.1'
    result1 = read_mysql_data(local,'root','admin','test_db', 'students')
    print(result1)
