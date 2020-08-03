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
        #输入检索内容
        self.find(MobileBy.ID,'search_input_text').send_keys("阿里巴巴")
        #在查询弹出中选中阿里巴巴-SW
        self.find(MobileBy.XPATH,f'//*[@text="{stockname}"]').click()
        #获取查询结果中的阿里巴巴-SW并添加自选
        self.find(MobileBy.XPATH,f'//*[contains(@resource-id,"ll_stock_item_container")]//*[@text="{stockname}"]/../..//*[@text="加自选"]').click()

    def is_choose(self,stockname):
        eles = self.finds(MobileBy.XPATH,
                  f'//*[contains(@resource-id,"ll_stock_item_container")]//*[@text="{stockname}"]/../..//*[@text="已添加"]')

        return len(eles) > 0
