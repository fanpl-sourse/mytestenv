# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 12:26
# @Author  : 饭盆里
# @File    : test_secret.py
# @Software: PyCharm
# @desc    :
from appium import webdriver


class TestSecret():
    def setup(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "emulator-5554",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": 'true',
            "unicodeKeyBord": 'true'
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.back()
        self.driver.quit()

    def test_touchaction_unlock(self):
        pass