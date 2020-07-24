#!/usr/bin/env python
# encoding: utf-8
'''
@author: fanpl
@file: testclass.py
@time: 2020/7/8 20:15
@desc:
'''

#定义类
class Person():

    def __init__(self,name,age):
        self.name = name
        self.age = age

    # def set_name(self,name):
    #     self.name = name

    def eat(self):
        print(f'{self.name} 能吃')
    @classmethod
    def sleep(self):
        print('能睡')

# zs = Person('zhangsan',18)
# zs.sleep()
# print(zs.age)
# zs.name = 'pl'
# print(f'名字：{zs.name}')

Person.sleep()