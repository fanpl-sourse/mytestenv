# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 14:41
# @Author  : 饭盆里
# @File    : test_ordering.py
# @Software: PyCharm
# @desc    :
import pytest

@pytest.mark.run(order=2)
def test_order_01():
    print('prder01')

@pytest.mark.run(order=-1)
def test_order_02():
    print('prder02')

@pytest.mark.run(order=3)
def test_order_03():
    print('prder03')

@pytest.mark.first
def test_order_04():
    print('prder04')

# import pytest
#
# @pytest.mark.run(order=2)
# def test_foo():
#     assert True
#
# @pytest.mark.run(order=1)
# def test_bar():
#     assert True