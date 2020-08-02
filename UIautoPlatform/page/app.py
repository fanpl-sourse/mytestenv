# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 15:01
# @Author  : 饭盆里
# @File    : app.py
# @Software: PyCharm
# @desc    :
from appium import webdriver
from UIautoPlatform.page.base_page import BasePage
from UIautoPlatform.page.main import Main


class App(BasePage):
    """
    定义了是否需要启动APP
    """
    _package = 'com.xueqiu.android'
    _activity = '.view.WelcomeActivityAlias'

    def start(self):
        """
        启动雪球APP
        :return:
        """
        if self._driver is None:
            desire_cap = {
                "platformName": "android",
                "deviceName": "emulator-5554",
                "appPackage": self._package,
                "appActivity": self._activity,
                "noReset": True,
                "skipSeverInstallation": True,
                "unicodeKeyBord": 'true'
            }

            self._driver = webdriver.Remote(
                "http://127.0.0.1:4723/wd/hub",
                desire_cap)
        else:
            self._driver.start_activity(self._package,self._activity)

        self._driver.implicitly_wait(10)

        #返回自身，方便在调用启动后，可以调用APP类中的其他方法
        return self

    def main(self) -> Main:
        return Main(self._driver)