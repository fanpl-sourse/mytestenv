# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 17:39
# @Author  : 饭盆里
# @File    : wework.py
# @Software: PyCharm
# @desc    :

import pytest
import requests
from interface.weworkApi.util import Util
from interface.weworkApi.baseapi import BaseApi


class Member(BaseApi):

    def __init__(self):
        self.access_token = Util().get_access_token()


    def create_member(self,userid,name,alias,mobile):
        """
        创建通讯录用户
        :return:
        """
        data = {
            "method" : "post",
            "url"    :   f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.access_token}',
            "json"   :   {
                    "userid": userid,
                    "name": name,
                    "alias": alias,
                    "mobile": mobile,
                    "department": [1]
            }
        }

        # r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.access_token}',
        #               json=jsondata)
        print(self.send(data))
        return self.send(data)