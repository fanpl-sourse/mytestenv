# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 08:51
# @Author  : 饭盆里
# @File    : conftest.py
# @Software: PyCharm
# @desc    :
import pytest


@pytest.fixture()
def instantiateCal():
    print('hi fixture')