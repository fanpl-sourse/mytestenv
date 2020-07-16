# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 22:33
# @Author  : 饭盆里
# @File    : test_fixture1.py
# @Software: PyCharm
# @desc    :
import pytest

##模式一
# @pytest.fixture()

##模式二
# @pytest.fixture(scope="module")
# def login():
#     print('这是登录')

##模式三
# @pytest.fixture(scope="module")
# def login():
#     print('这是登录')
#     #yield 生成器，激活teardown
#     yield
#     print('最末执行')

##模式四 conftest.py

class TestFixture1:
    @pytest.mark.parametrize("login",[
        ("username","passwd")
    ], indirect=True)
    @pytest.mark.parametrize('a,b',[
        (1,2),
        (3,4)
    ])
    def test_case1(self,login,a,b):
        print(f'这是测试用例,a = {a},b = {b}')

    def test_case2(self):
        print('这是测试用例2')

    def test_case3(self,login):
        print('这是测试用例3')

# class TestFixture2:
#     def test_case4(self,login):
#         print('这是测试用例4')
#
#     def test_case5(self):
#         print('这是测试用例5')
#
#     def test_case6(self,login):
#         print('这是测试用例6')