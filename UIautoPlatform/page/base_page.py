# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 14:57
# @Author  : 饭盆里
# @File    : base_page.py
# @Software: PyCharm
# @desc    :
from time import sleep

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    _driver : WebDriver
    #黑名单列表
    _black_list = [
        (MobileBy.ID,'iv_close')
    ]
    #最大出错次数，避免出现死循环
    _max_error_times = 3
    #出错次数
    _error_times = 0

    def __init__(self,driver:WebDriver=None):
        self._driver = driver

    # def find(self,locator,value):
    #     try:
    #         element =  self._driver.find_element(locator,value)
    #         return element
    #     except:
    #         for black in self._black_list:
    #             elements = self._driver.find_elements(*black)
    #             if len(elements) > 0:
    #                 elements[0].click()
    #                 break
    #         # 关闭掉弹框后，继续查找要找的元素
    #         return self.find(locator,value)

    def find(self,by,locator=None):
        try:
            #如果元素找到，就清空error计数
            # 如果locator是None，则说明传进来的是元祖/list，需要进行解析
            if locator is None:
                element = self._driver.find_element(*by)
            else:
                #否则，说明传进来的是两个数据，可以一个萝卜一个坑，不需要解析
                element = self._driver.find_element(by,locator)
            self._error_times = 0
            return element

        except Exception as e:
            #如果没有找到，就进行黑名单处理
            #错误次数超过最大次数，则直接报错，避免死循环
            if self._error_times >= self._max_error_times:
                self._error_times = 0
                raise e

            self._error_times += 1

            for black in self._black_list:
                elements = self.finds(*black)
                #长度大于0，说明名中了黑名单中的一个定位元素，则将黑名单点击即可(关闭弹框或者广告)
                if len(elements) > 0:
                    elements[0].click()
                    # 关闭掉弹框后，继续查找要找的元素
                    return self.find(by,locator)

            raise ValueError('元素不在黑名单中')


    def finds(self,by,locator=None):
        if locator is None:
            return self._driver.find_elements(*by)
        else:
            return self._driver.find_elements(by,locator)

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

