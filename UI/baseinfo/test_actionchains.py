# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 22:32
# @Author  : 饭盆里
# @File    : test_actionchains.py
# @Software: PyCharm
# @desc    :
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.close()

    @pytest.mark.skip
    def test_actionchains(self):
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        myclick = self.driver.find_element_by_xpath('//input[@value="click me"]')
        mydubboclick = self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        myrightclich = self.driver.find_element_by_xpath('//input[@value="right click me"]')

        action = ActionChains(self.driver)
        action.click(myclick)
        action.double_click(mydubboclick)
        action.context_click(myrightclich)
        sleep(3)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_moveto_action(self):
        self.driver.get('https://www.baidu.com/')
        mts = self.driver.find_element(By.ID,'s-usersetting-top')
        ActionChains(self.driver).move_to_element(mts).perform()
        sleep(3)

    @pytest.mark.skip
    def test_drag_drop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        # drag_element = self.driver.find_element_by_id('dragger')
        # drag_element = self.driver.find_element_by_xpath('//*[@class="drag"]')
        drag_element = self.driver.find_element_by_css_selector('.drag')
        drop_element = self.driver.find_element_by_xpath('/html/body/div[2]')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_element,drop_element)
        action.perform()
        sleep(5)

    def test_keys(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        self.driver.find_element_by_xpath('/html/body/label[1]/input').click()

        action = ActionChains(self.driver)
        action.send_keys('hi ~').pause(1)
        action.send_keys(Keys.BACKSPACE).pause(1)
        action.send_keys('你好吗？').pause(1)
        action.send_keys(Keys.CLEAR).pause(1)
        action.perform()
        sleep(2)



