# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 15:24
# @Author  : 饭盆里
# @File    : test_main.py
# @Software: PyCharm
# @desc    :
from UIautoPlatform.page.app import App


class TestMain:
    def test_main(self):
        App().start().main().goto_search()