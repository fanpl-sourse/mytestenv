# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 12:34
# @Author  : 饭盆里
# @File    : test_market_search.py
# @Software: PyCharm
# @desc    :
from UIautoPlatform.test_case.test_base import TestBase


class TestMarketSearch(TestBase):
    def test_market_search(self):
        search = self.app.start().goto_main().goto_market().goto_search()
        search.send_search_key("阿里巴巴-SW")
        assert search.is_choose("阿里巴巴-SW")
