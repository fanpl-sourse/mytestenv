# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 09:07
# @Author  : 饭盆里
# @File    : test_base.py
# @Software: PyCharm
# @desc    :
from UIautoPlatform.page.app import App


class TestBase:
    app = None

    def setup(self):
        self.app = App()