# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 17:39
# @Author  : 饭盆里
# @File    : wework_1.py
# @Software: PyCharm
# @desc    : 第一次优化： 将token方法提取出去

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
        json = {
                "userid": userid,
                "name": name,
                "alias": alias,
                "mobile": mobile,
                "department": [1]
        }
        r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.access_token}',
                      json=json)
        print(r.json())
        return r.json()

    def get_member(self,userid):
        """
        获取成员
        :return:
        """
        r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.access_token}&userid={userid}')
        print(r.json())
        return r.json()

    def update_member(self,userid,name,alias):
        """
        更新成员
        :return:
        """
        jsondata={
            "userid": userid,
            "name": name,
            "alias": alias,
        }
        r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.access_token}',json=jsondata)
        print(r.json())
        return r.json()

    def delete_member(self,userid):
        """
        删除成员
        :return:
        """
        # access_token = self.get_access_token()
        r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.access_token}&userid={userid}')
        print(r.json())
        return r.json()
