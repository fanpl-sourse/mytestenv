# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 12:34
# @Author  : 饭盆里
# @File    : test_market_search.py
# @Software: PyCharm
# @desc    :
import pytest

from UIautoPlatform.test_case.test_base import TestBase


class TestMarketSearch(TestBase):
    @pytest.mark.parametrize('stock_name',[
        "阿里巴巴-SW",
        "京东"
    ])
    def test_market_search(self,stock_name):
        search = self.app.start().goto_main().goto_market().goto_search()
        search.send_search_key(stock_name)
        assert search.is_choose(stock_name)
