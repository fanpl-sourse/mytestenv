# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 11:25
# @Author  : 饭盆里
# @File    : market.py
# @Software: PyCharm
# @desc    :
from appium.webdriver.common.mobileby import MobileBy
from UIautoPlatform.page.base_page import BasePage
from UIautoPlatform.page.market_search import MarketSearch


class Market(BasePage):
    """
    行情
    """
    def goto_search(self):
        self.find(MobileBy.ID,'com.xueqiu.android:id/action_search').click()
        return MarketSearch(self._driver)