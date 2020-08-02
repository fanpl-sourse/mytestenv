# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 14:57
# @Author  : 饭盆里
# @File    : base_page.py
# @Software: PyCharm
# @desc    :
import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _driver : WebDriver
    def __init__(self,driver:WebDriver=None):
        self._driver = driver

    def find(self,locator,value):
        return self._driver.find_element(locator,value)

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

