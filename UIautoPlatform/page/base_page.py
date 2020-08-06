# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 14:57
# @Author  : 饭盆里
# @File    : base_page.py
# @Software: PyCharm
# @desc    :
import json
from time import sleep

import yaml
from appium.webdriver.webdriver import WebDriver
from UIautoPlatform.page.handle_black import handle_black

class BasePage:
    _driver : WebDriver
    # 最大出错次数，避免出现死循环
    _max_error_times = 3
    # 出错次数
    _error_times = 0
    # 参数
    _params = {}

    def __init__(self,driver:WebDriver=None):
        self._driver = driver

    @handle_black
    def find(self,by,locator=None):
            #如果元素找到，就清空error计数
            # 如果locator是None，则说明传进来的是元祖/list，需要进行解析
            if locator is None:
                element = self._driver.find_element(*by)
            else:
                #否则，说明传进来的是两个数据，可以一个萝卜一个坑，不需要解析
                element = self._driver.find_element(by,locator)
            return element

    def finds(self,by,locator=None):
        if locator is None:
            return self._driver.find_elements(*by)
        else:
            return self._driver.find_elements(by,locator)

    def read_file_steps(self,path,funcname):
        with open(path,encoding='utf-8') as f:
            steps = yaml.safe_load(f)[funcname]

        # 将变量解析 替换 然后又还原格式
        raw = json.dumps(steps)
        for key,value in self._params.items():
            raw = raw.replace('${'+key+'}',value)
        steps = json.loads(raw)

        for step in steps:
            if "action" in step.keys():
                action = step['action']
                if "click" == action:
                    self.find(step['by'],step['locator']).click()
                if "send" == action:
                    self.find(step['by'],step['locator']).send_keys(step['value'])
                if "sleep" == action:
                    sleep(1)
                if "len > 0" == action:
                    eles = self.finds(step['by'], step['locator'])
                    return len(eles) > 0


    def save_screen_short(self,screenpath):
        return self._driver.save_screenshot(screenpath)

    def set_implicitly_wait(self,sec):
        self._driver.implicitly_wait(sec)

