# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 15:00
# @Author  : 饭盆里
# @File    : SetupTeardown.py
# @Software: PyCharm
# @desc    :
import os
import sys
sys.path.append('..')
from selenium import webdriver


class setupTeardown:
    def setup(self):
        #运行命令：browser=Chrome pytest 脚本文件名
        # browser= os.getenv("browser")
        # if browser.lower() == 'ie':
        #     self.driver = webdriver.Ie()
        # elif browser.lower() == 'firefox':
        #     self.driver = webdriver.firefox()
        # else:
        #     self.driver = webdriver.Chrome()

        self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()