# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 14:57
# @Author  : 饭盆里
# @File    : base_page.py
# @Software: PyCharm
# @desc    :
import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    _driver : WebDriver
    _black_list = [(By.ID,'iv_close')]
    def __init__(self,driver:WebDriver=None):
        self._driver = driver

    def find(self,locator,value):
        try:
            element =  self._driver.find_element(locator,value)
            return element
        except:
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                break
            # 关闭掉弹框后，继续查找要找的元素
            return self.find(locator,value)

    def read_file_steps(self,path):
        with open(path) as f:
            steps = yaml.safe_load(f)

            for step in steps:
                if "By" in step:
                    element = self.find(step['By'],step['locator'])
                if "action" in step:
                    action = step['action']
                    if "click" == action:
                        element.click()

