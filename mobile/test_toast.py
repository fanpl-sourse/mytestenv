# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 22:00
# @Author  : 饭盆里
# @File    : test_toast.py
# @Software: PyCharm
# @desc    :
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestToast():
    def setup(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "emulator-5554",
            "appPackage": "io.appium.android.apis",
            "appActivity": "io.appium.android.apis.view.PopupMenu1"
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(20)

    def teardown(self):
        self.driver.quit()

    def test_toast(self):
        self.driver.find_element_by_accessibility_id('Make a Popup!').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="Search"]').click()
        #获取当前页面的dom
        # print(self.driver.page_source)
        #获取toast 内容的方案一
        # text = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        # print(text)
        #获取toast 内容的方案二
        text= self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"Clicked popup")]').text
        print(text)
        assert 'Search' in text