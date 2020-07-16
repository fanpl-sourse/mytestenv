# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 12:01
# @Author  : 饭盆里
# @File    : test_calcute.py
# @Software: PyCharm
# @desc    :
import pytest
from pythoncode.calcute import Calculator


def setup_module(self):
    print('模块setup')

def teardown_module(self):
    print('模块teardown')

# 类外叫函数，类里面的叫方法
def setup_function(self):
    print('函数setup')

def teardown_function(self):
    print('函数teardown')

class TestCalcute:
    #类级别的：类前后运行
    @classmethod
    def setup_class(cls):
        cls.cal = Calculator()
        print('类setup')
    @classmethod
    def teardown_class(cls):
        print('类teardown')

    #每个函数前后都执行
    def setup(self):
        print('方法setup')

    def teardown(self):
        print('方法teardown')

    @pytest.mark.myadd
    @pytest.mark.parametrize("a,b,s",[
        (2,1,3)
    ])
    def test_myadd(self,a,b,s):
        assert self.cal.myadd(a,b) == s
        print('myadd')

    @pytest.mark.mydiv
    @pytest.mark.parametrize("a,b,result",[
        (3,2,1.5)
    ])
    def test_mydiv(self,a,b,result):
        assert self.cal.mydiv(a,b) == result
        print('mydiv')


