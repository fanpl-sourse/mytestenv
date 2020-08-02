# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 15:24
# @Author  : 饭盆里
# @File    : test_main.py
# @Software: PyCharm
# @desc    :
import pytest
import yaml

from UIautoPlatform.page.app import App


class TestMain:
    def test_main(self):
        App().start().main().goto_search()

    @pytest.mark.parametrize('a,b',yaml.safe_load(open('../data/test_main_data.yaml')))
    def test_para(self,a,b):
        print(a)
        print(b)