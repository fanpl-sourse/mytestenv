# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 15:13
# @Author  : 饭盆里
# @File    : main.py
# @Software: PyCharm
# @desc    :
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from UIautoPlatform.page.base_page import BasePage
from UIautoPlatform.page.market import Market


class Main(BasePage):
    def goto_search(self):
        self.read_file_steps('../data/main.yaml','goto_search')

    def goto_windows(self):
        self.read_file_steps('../data/main.yaml','goto_windows')
        # #点击推荐
        # self.find(MobileBy.XPATH,'//*[@text="推荐" and contains(@resource-id,"title_text")]').click()
        # #点击笔
        # self.find(MobileBy.ID,'post_status').click()
        # sleep(1)
        # #点击检索(上面需要将弹窗捕获并关闭)
        # self.find(MobileBy.ID, 'com.xueqiu.android:id/tv_search').click()

    def goto_market(self):
        """
        进入行情
        :return:
        """
        self.read_file_steps('../data/main.yaml','goto_market')
        return Market(self._driver)