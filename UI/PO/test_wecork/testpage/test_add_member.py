# -*- coding: utf-8 -*-
# @Time    : 2020/7/20 19:20
# @Author  : 饭盆里
# @File    : test_add_member.py
# @Software: PyCharm
# @desc    :
from UI.PO.test_wecork.polists.firstpage_po import FirstPage


class TestAddMember:
    def setup(self):
        self.firstpage = FirstPage()

    def test_add_member(self):
        self.firstpage.goto_add_member().add_member()