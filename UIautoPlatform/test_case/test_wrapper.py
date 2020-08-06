# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 17:35
# @Author  : 饭盆里
# @File    : test_wrapper.py
# @Software: PyCharm
# @desc    : 装饰器
def wrapper(func):
    print('hi')
    func()
    print('bye')

def wrapper1(func):
    #允许所有类型的入参
    def hello(*args,**kwargs):
        print(args)
        func()
        print(kwargs)

    return hello

@wrapper1
def temp1():
    print("temp1")

def temp2():
    print("temp2")

def tmp():
    print('tmp')


def test():
    #直接调用函数
    # tmp()
    #想要给函数前后增加内容时，可以用一个函数封装另一个函数，实现集中调用
    # wrapper(tmp)
    # wrapper(temp1)
    #入参：函数名，返回：函数名
    # wrapper1(tmp)(1,2,a=3)
    #上述写法 加装饰器可简写为：
    temp1(1,2,a=3)
