# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 19:47
# @Author  : 饭盆里
# @File    : test_baidudemo.py
# @Software: PyCharm
# @desc    : UI：打开百度、输入检索词、截图、关闭网页
from time import sleep

import allure
import pytest
from selenium import webdriver

@allure.feature('百度检索')
@pytest.mark.parametrize('value',['hi','selenium'])
def test_baidudemo(value):
    with allure.step('打开浏览器'):
        driver = webdriver.Chrome()
        driver.get('https:www.baidu.com')
        driver.maximize_window()
    with allure.step(f'输入检索词：{value}'):
        driver.find_element_by_id('kw').send_keys(value)
        sleep(2)
        driver.find_element_by_id('su').click()
        sleep(2)
    with allure.step('截图'):
        driver.save_screenshot('./result/1.png')
        allure.attach.file('./result/1.png',name='检索截图',attachment_type=allure.attachment_type.PNG)
    with allure.step('关闭浏览器'):
        driver.close()