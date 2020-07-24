#!/usr/bin/env python
# encoding: utf-8
'''
@author: fanpl
@file: base.py
@time: 2020/7/7 19:15
@desc:
'''

# import sys
# print(sys.path)
# a =1
# print(a)
# print(id(a))

#####################
# 数据类型练习
#####################
# str_a = 'hhh'
# int_a = 1
# float_a = 0.2
# str_b = '12345'
# print(type(float_a))
# print(str_b[1])
# print(str_b[1:4:2])


#####################
# if 分支练习
# 分段函数求值
# 3x-5(x>1)
# x+2(-1<=x<=1)
# 5x+3(x<-1)
#####################
# todu:
#     print("确保输入的是数字")
# print("请输入：")
#
# num = int(input())
#
# if num < -1:
#     y = num * 5 + 3
# elif num <= 1:
#     y = num + 2
# else:
#     y = num * 3 -5
#
# print(y)


#####################
#for循环
#1. 计算1……100求和
#2. 1~100偶数求和
#####################
# sumint = 0
# for i in range(101):
#     sumint += i
# print(sumint)
#
# sumou = 0
# for i in range(0,101,2):
#     sumou += i
# print(sumou)


#####################
#while循环
# 猜数字：计算机给出随机数，人给出答案后，计算机提示大了/小了/猜对了提示
#####################
# import random
# rand = random.randint(0,100)
# print(rand)
# guestdata = 0
# while rand != guestdata:
#     print("请输入0-100的正整数：")
#     guestdata = int(input())
#     if rand > guestdata:
#         print('谜底大了')
#     elif rand < guestdata:
#         print('谜底小了')
#     else:
#         print('猜对了')
#         break

#####################
# 函数
#####################
# import random
# def game1(a):
#     """
#     猜数字：计算机给出随机数，人给出答案后，计算机提示大了/小了/猜对了提示
#     :param a:
#     :return:
#     """
#     rand = random.randint(0, 100)
#     print(rand)
#     guestdata = 0
#     while rand != guestdata:
#         print("请输入0-100的正整数：")
#         guestdata = int(input())
#         if rand > guestdata:
#             print('谜底大了')
#             print('谜底大了')
#             print('谜底大了')
#         elif rand < guestdata:
#             print('谜底小了')
#         else:
#             print('猜对了')
#             break
# game1(1)


#####################
# lambda
#####################
# mi = lambda x:x*x
# print(mi(3))

#####################
#list 常用函数
#####################
# lst = [5,3,7,92,3]
# print(lst)
# lst.append(12)
# print(lst)
# lst.insert(2,88)
# print(lst)
# d = lst.pop()
# print(lst)
# print(d)
# lst.sort()
# print(lst)
# lst.sort(reverse=True)
# print(lst)
# lst.reverse()
# print(lst)

#####################
#list 推导式
#####################
# lst = [i**2*j for i in range(1,5) for j in range(1,3)]
# print(lst)

#####################
# 元祖
#####################
# a = [3,2]
# tp = (4,3,5,7,a)
# print(tp)
# print(type(tp))
#
# tp[4][1] = 'h'
# print(tp)
# #3出现了多少次
# print(tp.count(3))
# #根据值，查找下标，不存在会报错
# print(tp.index(7))
# # 元祖转list
# print(list(tp))


#####################
# 集合
#####################
# set1 = {1,2,3}
# set2 = set()
# set2 = {1,4,5}
# print(set1)
# print(type(set1))
# print(set2)
# print(type(set2))
# print(set1.union(set2))
# print(set1.difference(set2))
# print(set1.intersection(set2))

#####################
# 字典
#####################
# dict1 = {"a1":1,"b1":3}
# dict2 = dict(a2=1,b2=2)
#
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
# #删除一个字典key值，并返回values值
# print(dict1.pop("a1"))
# print(dict1)
# #随机删除
# print(dict2.popitem())
# print(dict2)
# # 生成key值
# a ={}
# b = a.fromkeys(("a","b","c"),1)
# print(b)
# # 字典推导式
# print({i:i*i for i in range(1,3)})


na = 'f'
print('i am %s'  %na)

print('i am {}'.format(na))

namelist = ['h','hh','hhh']
print('we are {} ,{}, {}'.format(*namelist))

na = 'f'
age = 18
print(f'i am {na},and {age}')
print(f'i am {na.upper()}')
print(f'result is {(lambda x:x+1)(2)}')

