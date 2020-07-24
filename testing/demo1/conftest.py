# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 10:42
# @Author  : 饭盆里
# @File    : conftest.py
# @Software: PyCharm
# @desc    :
# scope: 模块级别
import pytest


@pytest.fixture(scope="module")
def login():
    print('这是登录')
    #yield 生成器，激活teardown
    yield
    print('最末执行')