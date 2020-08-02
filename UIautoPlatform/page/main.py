# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 15:13
# @Author  : 饭盆里
# @File    : main.py
# @Software: PyCharm
# @desc    :
from appium.webdriver.common.mobileby import MobileBy
from UIautoPlatform.page.base_page import BasePage


class Main(BasePage):
    def goto_search(self):
        self.find(MobileBy.ID,'com.xueqiu.android:id/tv_search').click()

    def get_steps(self,path = '../data/main.yaml'):
        self.read_file_steps(path)