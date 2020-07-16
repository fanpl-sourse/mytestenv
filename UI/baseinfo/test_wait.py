# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 23:45
# @Author  : 饭盆里
# @File    : test_wait.py
# @Software: PyCharm
# @desc    :
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://ceshiren.com/')
        self.driver.maximize_window()
        ##隐式等待
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.close()

    def test_wait(self):
        ##直接等待
        # self.driver.find_element(By.LINK_TEXT,'所有分类').click()
        # sleep(5)
        # self.driver.find_element_by_xpath('//*[@class="latest-topic-list ember-view"]/div[1]').click()
        # sleep(2)

        ##隐式等待
        # self.driver.find_element(By.LINK_TEXT, '所有分类').click()
        # self.driver.find_element_by_xpath('//*[@class="latest-topic-list ember-view"]/div[1]').click()

        ##显示等待
        # self.driver.find_element(By.LINK_TEXT, '所有分类').click()
        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH,('//*[@class="latest-topic-list ember-view"]/div[1]')))>=1
        # WebDriverWait(self.driver,10).until(wait)

        ##显示等待
        self.driver.find_element(By.LINK_TEXT, '所有分类').click()
        WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,'//*[@class="latest-topic-list ember-view"]/div[1]')))

