# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 17:41
# @Author  : 饭盆里
# @File    : testwework.py
# @Software: PyCharm
# @desc    :
from interface.weworkApi.wework import Member
class TestWework:
    def test_create_member(self):
        Member().create_member('ee1','ee1','e1','18788888889')

