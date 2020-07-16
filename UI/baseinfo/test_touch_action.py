
# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 10:15
# @Author  : 饭盆里
# @File    : test_touch_action.py
# @Software: PyCharm
# @desc    :
from time import sleep
from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.get('https://www.baidu.com/')
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touch_action(self):
        search_element = self.driver.find_element_by_id('kw')
        click_element = self.driver.find_element_by_xpath('//*[@value="百度一下"]')

        search_element.send_keys('selenium')
        action = TouchActions(self.driver)
        action.tap(click_element)
        action.perform()
        sleep(3)

        action.scroll_from_element(search_element,0,10000).perform()
        sleep(3)