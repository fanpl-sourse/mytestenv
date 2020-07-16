# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 23:59
# @Author  : 饭盆里
# @File    : test_page.py
# @Software: PyCharm
# @desc    :
from UI.PO.main_page import MainPage


class TestPage():
    MainPage().click_first_link().title()