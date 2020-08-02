# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 22:47
# @Author  : 饭盆里
# @File    : test_getattribute.py
# @Software: PyCharm
# @desc    :
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestGetAttribute():
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
        self.driver.implicitly_wait(20)

    def teardown(self):
        self.driver.quit()

    def test_getattribute(self):
        # element = self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/tv_search')
        element = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tv_search")')
        sleep(2)
        print(element.get_attribute("text"))
        print(element.get_attribute("class"))
        print(element.get_attribute("enabled"))
        print(element.get_attribute("bounds"))

        assert '军工' in element.get_attribute("text")