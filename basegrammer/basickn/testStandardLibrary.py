#!/usr/bin/env python
# encoding: utf-8
'''
@author: fanpl
@file: testStandardLibrary.py
@time: 2020/7/8 20:36
@desc:
'''
# import os
# # os.mkdir("testdir")
# # os.removedirs('testdir')
# # print(os.listdir("./"))
# #
# # print(os.getcwd())
#
# if not os.path.exists('testdir'):
#     os.mkdir('testdir')
# if not os.path.exists('testdir/testdata.txt'):
#     with open('testdir/testdata.txt','a+') as f:
#         f.write('he,你好吗？')


# import time
# print(time.time())
# print(time.asctime())
# time.sleep(1)
# print(time.localtime())
# print(time.strftime("%Y-%m-%d"))
#
# #获取两天前的时间
# now = time.time()
# two_day_before = now - 60*60*24*2
# time_tuple = time.localtime(two_day_before)
# print(time.strftime("%Y-%m-%d-%H-%M-%S",time_tuple))

#
# import urllib.request
# response = urllib.request.urlopen('https://www.baidu.com/')
# print(response.status)

import math

print(math.ceil(5.4))
print(math.floor(5.9))
print(math.sqrt(16))