# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 16:00
# @Author  : 饭盆里
# @File    : test_pytest_dependency.py
# @Software: PyCharm
# @desc    :
import pytest

@pytest.mark.dependency(name='a')
def test_demo1():
    print('demo1')
    assert False

@pytest.mark.dependency(name='b')
def test_demo2():
    print('demo2')
"""
如果a执行通过，则test_demo3会被执行
如果a执行失败，则跳过依赖a的用例
depends=[] 列表中加入依赖的测试用例
被依赖的测试用例需要加上装饰器：@pytest.mark.dependency()
"""
@pytest.mark.dependency(name='c',depends=["b","test_demo1"])
def test_demo3():
    print('demo3')

@pytest.mark.dependency(depends=['a'])
def test_demo4():
    print('demo4')