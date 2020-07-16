# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 16:18
# @Author  : 饭盆里
# @File    : test_allure.py
# @Software: PyCharm
# @desc    :

import pytest

def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')