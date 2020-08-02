# -*- coding: utf-8 -*-
# @Time    : 2020/7/24 15:29
# @Author  : 饭盆里
# @File    : tt.py
# @Software: PyCharm
# @desc    :
# import re
# r = '共66人，5人未加入'
# member_num = int(re.match(r'共(\d+)人',r).group(1))
# s = re.match(r'共(\d+)人',r).group(1)
# print(type(member_num))

name = 'f'
print(f"//*[@text='联系人']/../..//*[@text={name}]")