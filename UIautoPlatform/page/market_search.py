# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 11:37
# @Author  : 饭盆里
# @File    : market_search.py
# @Software: PyCharm
# @desc    :
from appium.webdriver.common.mobileby import MobileBy

from UIautoPlatform.page.base_page import BasePage

class MarketSearch(BasePage):
    """
    行情页面的检索页面
    """
    def send_search_key(self,stockname):
        self._params['stockname'] = stockname
        self.read_file_steps('../data/search.yaml','send_search_key')

    def is_choose(self,stockname):
        eles = self.finds(MobileBy.XPATH,
                  f'//*[contains(@resource-id,"ll_stock_item_container")]//*[@text="{stockname}"]/../..//*[@text="已添加"]')

        return len(eles) > 0
        # self._params['stockname'] = stockname
        # self.read_file_steps('../data/search.yaml','is_choose')
