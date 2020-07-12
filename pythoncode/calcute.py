# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 11:55
# @Author  : 饭盆里
# @File    : calcute.py
# @Software: PyCharm
# @desc    :

class Calculator:
    def myadd(self,a,b):
        return a+b
    def mysub(self,a,b):
        return a-b
    def mymult(self,a,b):
         return a*b
    def mydiv(self,a,b):
        return a/b

if __name__ == '__main__':
    ca = Calculator()
    print(ca.myadd(1,2))
    print(ca.mysub(2,1))
    print(ca.mymult(2, 2))
    print(ca.mydiv(2, 2))