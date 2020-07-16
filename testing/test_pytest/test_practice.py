# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 14:17
# @Author  : 饭盆里
# @File    : test_practice.py
# @Software: PyCharm
# @desc    :
import pytest
import yaml


def func(x):
    return x + 1

@pytest.mark.parametrize(('a','b'),[
    (1,2),
    (3,4),
    (10,22)
])
def test_answer(a,b):
    assert func(a) == b

@pytest.mark.parametrize('a,b', yaml.safe_load(open('data/data.yaml')))
def test_answer1(a,b):
    assert func(a) == b

@pytest.fixture()
def login():
    print('登录操作')
    username= 'hi'
    return username
class TestDemo:
    def test_a(self,login):
        print(f"a login {login}")

    def test_b(self):
        print('B')

    def test_c(self,login):
        print(f'c login {login}')

# if __name__ == '__main__':
#     pytest.main(['test_practice.py'])