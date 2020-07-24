# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 22:26
# @Author  : 饭盆里
# @File    : test_fileup.py
# @Software: PyCharm
# @desc    :
from time import sleep
from UI import setupTeardown


class TestFile(setupTeardown):
    def test_file(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element_by_xpath('//*[@class="soutu-btn"]').click()
        self.driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/div[2]/input').send_keys('/Users/a/Pictures/WechatIMG175.jpeg')
        sleep(3)