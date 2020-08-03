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

    def goto_windows(self):
        #点击推荐
        self.find(MobileBy.XPATH,'//*[@text="推荐" and contains(@resource-id,"title_text")]').click()
        #点击笔
        self.find(MobileBy.ID,'post_status').click()
        #点击检索(上面需要将弹窗捕获并关闭)
        self.find(MobileBy.ID, 'tv_search').click()

    def get_steps(self,path = '../data/main.yaml'):
        self.read_file_steps(path)