# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 15:24
# @Author  : 饭盆里
# @File    : test_main.py
# @Software: PyCharm
# @desc    :
import pytest
import yaml

from UIautoPlatform.test_case.test_base import TestBase


class TestMain(TestBase):
    def test_main(self):
        self.app.start().goto_main().goto_search()

    def test_windows(self):
        self.app.start().goto_main().goto_windows()

    @pytest.mark.parametrize('a,b',yaml.safe_load(open('../data/test_main_data.yaml')))
    def test_para(self,a,b):
        print(a)
        print(b)