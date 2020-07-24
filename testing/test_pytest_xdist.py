# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 16:21
# @Author  : 饭盆里
# @File    : test_pytest_xdist.py
# @Software: PyCharm
# @desc    :
from datetime import time
from time import sleep

import time
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
print(now)

def test_demo1():
    print("demo1")
    sleep(5)

def test_demo2():
    print("demo2")
    sleep(5)

def test_demo3():
    print("demo3")
    sleep(5)

now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
print(now)