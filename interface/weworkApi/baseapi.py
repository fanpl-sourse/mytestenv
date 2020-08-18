# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 17:39
# @Author  : 饭盆里
# @File    : baseapi.py
# @Software: PyCharm
# @desc    :

import requests

class BaseApi():
    def send(self,**data):
        return requests.request(**data).json()