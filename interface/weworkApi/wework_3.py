# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 17:39
# @Author  : 饭盆里
# @File    : wework_1.py
# @Software: PyCharm
# @desc    : 第三次优化：数据放到数据文件yaml 中，实现数据与代码的分离
from interface.weworkApi.util import Util
from interface.weworkApi.baseapi import BaseApi

class Member(BaseApi):

    def __init__(self):
        u = Util()
        self.data = u.get_yaml_data('../data/weworkdata.yaml')
        self.params['access_token'] = u.get_access_token()

    def create_member(self,userid,name,alias,mobile):
        """
        创建通讯录用户
        :return:
        """
        self.params['userid'] = userid
        self.params['name'] = name
        self.params['alias'] = alias
        self.params['mobile'] = mobile

        data = self.data['create_member']
        response = self.send_1(data)
        print("response >>  "+str(response))
        return response

    def get_member(self,userid):
        """
        获取成员
        :return:
        """
        self.params['userid'] = userid
        data = self.data['get_member']
        response = self.send_1(data)
        print("response >>  "+str(response))
        return response

    def update_member(self,userid,name,alias):
        """
        更新成员
        :return:
        """
        self.params['userid'] = userid
        self.params['name'] = name
        self.params['alias'] = alias
        data = self.data['update_member']
        response = self.send_1(data)
        print(response)
        return response

    def delete_member(self,userid):
        """
        删除成员
        :return:
        """
        self.params['userid'] = userid
        data = self.data['delelte_member']
        response = self.send_1(data)
        print(response)
        return response
