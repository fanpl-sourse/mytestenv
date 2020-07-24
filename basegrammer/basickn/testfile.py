#!/usr/bin/env python
# encoding: utf-8
'''
@author: fanpl
@file: testfile.py
@time: 2020/7/8 19:30
@desc:
'''

# f = open('data.txt','r')
# print(f.readlines())
# f.close()

# with open('data.txt') as f:
#     while True:
#         line = f.readlines()
#         if line:
#           print(line,end=' ')
#         else:
#             break


##异常
# na = 's'
# print(a)

# print(1/0)

# n = 10
# print(n.upper())

# dict1 = {"key1":"hi","key2":"hello"}
# print(dict1['key3'])

# lst = [1,2,3]
# try:
#      print(lst[3])
#      print(1/0)
# except Exception as e:
#     print("越界")


# class MyException(Exception):
#     def __init__(self,msg):
#         print(f'异常：{msg}')
#
#     def set_age(self,age):
#         if age>150 or age<=0:
#             raise MyException(f'值错误,{age}')
#         else:
#             print(f"age is {age}")
#
# MyException('啥').set_age(1000)