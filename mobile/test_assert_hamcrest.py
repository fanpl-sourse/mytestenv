# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 23:29
# @Author  : 饭盆里
# @File    : test_assert_hamcrest.py
# @Software: PyCharm
# @desc    :
from hamcrest import *
class TestAssertHamcrest:
    def test_Assert(self):
        assert 'h' in 'hello'

    def test_hamcrest(self):
        assert_that(1,equal_to(1))
        assert_that(110,close_to(100,10))
        assert_that('i am fanpl',contains_string('fanpl'))