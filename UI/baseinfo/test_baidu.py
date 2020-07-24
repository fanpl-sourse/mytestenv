# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 21:54
# @Author  : 饭盆里
# @File    : test_baidu.py
# @Software: PyCharm
# @desc    :
from time import sleep
from selenium  import webdriver
from selenium.webdriver.common.by import By


class TestBaidu:
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://www.baidu.com/')
        cls.driver.maximize_window()
    def teardown_class(cls):
        cls.driver.close()

    def test_baidu(self):
        # self.driver.find_element(By.ID,'kw').send_keys('selenium')
        # self.driver.find_element_by_name('wd').send_keys('selenium')
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')
        sleep(3)
        self.driver.find_element(By.XPATH,'//*[@class="bg s_btn"]').click()
        sleep(3)