# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 17:41
# @Author  : 饭盆里
# @File    : wework_1.py
# @Software: PyCharm
# @desc    :
from interface.weworkApi.wework_1 import Member
class TestWework:
    def test_create_member(self):
        Member().create_member('ee1','ee1','e1','18788888889')

    def test_get_member(self):
        Member().get_member('FanPengLi')

    def test_update_member(self):
        Member().update_member('ee1','ee2','ee2')

    def test_delete_member(self):
        Member().delete_member('ee1')