# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 23:06
# @Author  : 饭盆里
# @File    : test_UI_hg.py
# @Software: PyCharm
# @desc    :

from selenium import webdriver
from time import sleep

class TestUIHg():
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://ceshiren.com/')
        cls.driver.implicitly_wait(5)

    @classmethod
    def teardown_class(cls):
        sleep(2)
        cls.driver.close()

    # def setup(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('https://ceshiren.com/')
    #     self.driver.implicitly_wait(5)
    #
    # def teardown(self):
    #     self.driver.quit()

    def test_ui_hg(self):
        self.driver.find_element_by_link_text('精华帖').click()
        self.driver.find_element_by_partial_link_text('面试题').click()
