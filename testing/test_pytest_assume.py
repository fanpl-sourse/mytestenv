# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 14:00
# @Author  : 饭盆里
# @File    : test_pytest_assume.py
# @Software: PyCharm
# @desc    :
import pytest


@pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)])
def test_simple_assume(x, y):
    with pytest.assume:
        assert x == y
        assert True
        assert False
    # assert x==y
