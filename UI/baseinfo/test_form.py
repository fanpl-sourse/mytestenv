# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 12:31
# @Author  : 饭盆里
# @File    : test_form.py
# @Software: PyCharm
# @desc    :
from time import sleep

from selenium import webdriver


class TestForm:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://testerhome.com/account/sign_in')
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.close()

    def test_form(self):
        self.driver.find_element_by_name('user[login]').send_keys('134')
        self.driver.find_element_by_id('user_password').send_keys('pswd')
        self.driver.find_element_by_id('user_remember_me').click()
        self.driver.find_element_by_name('commit').click()
        sleep(5)
