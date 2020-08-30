# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 16:18
# @Author  : 饭盆里
# @File    : test_allure.py
# @Software: PyCharm
# @desc    :

import pytest

def test_success():
    """this selenium_ui_jenkins succeeds"""
    assert True


def test_failure():
    """this selenium_ui_jenkins fails"""
    assert False


def test_skip():
    """this selenium_ui_jenkins is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')