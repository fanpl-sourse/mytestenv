# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 15:34
# @Author  : 饭盆里
# @File    : test_screenfinger.py
# @Software: PyCharm
# @desc    :
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestScrenFinger():
    def setup(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "emulator-5554",
            "appPackage": "cn.kmob.screenfingermovelock",
            "appActivity": "com.samsung.ui.MainActivity",
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_unlock(self):
        TouchAction(self.driver).press(x=120,y=182).wait(100).move_to(x=360,y=186).wait(100)\
        .move_to(x=600,y=184).wait(100).move_to(x=600,y=246).wait(100).move_to(x=600,y=667).wait(100).release().perform()