# -*- coding: utf-8 -*-
# @Time    : 2020/7/20 10:45
# @Author  : 饭盆里
# @File    : base_po.py
# @Software: PyCharm
# @desc    : 子类在执行之前，主动调父类的构造方法
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():

    _driver = None
    _base_url = ''

    def __init__(self,driver: WebDriver = None):
        if driver is None:
            #开启调试模式
            options = Options()
            options.debugger_address = '127.0.0.1:9222'
            self._driver = webdriver.Chrome(options=options)
            # self.driver = webdriver.Chrome()

            self._driver.implicitly_wait(5)

        else:
            self._driver = driver

        if self._base_url != '':
            self._driver.get(self._base_url)

    def setup(self):
        pass

    def teardown(self):
        self.driver.quit()

    #find只返回value，直到超时；
    def find(self,by,locator):
        return self._driver.find_element(by,locator)
    #finds返回value或者[]，就是none
    def finds(self,by,locator):
        return self._driver.find_elements(by,locator)

    def wait_for_element_clickable(self, locator):
        """
        显示等待
        :param conditions: 显示等待的条件
        :return:
        """
        WebDriverWait(self._driver,10).until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_condition(self, conditions):
        """
        显示等待
        :param conditions: 显示等待的条件
        :return:
        """
        WebDriverWait(self._driver,10).until(conditions)