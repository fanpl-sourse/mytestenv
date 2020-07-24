# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 13:52
# @Author  : 饭盆里
# @File    : test_rerunfailures.py
# @Software: PyCharm
# @desc    : 测试插件pytest-rerunfailures
import pytest


@pytest.mark.flaky(reruns=5)
def test_example():
    import random
    assert random.choice([True, False])