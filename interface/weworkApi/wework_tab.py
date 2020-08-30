# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 19:57
# @Author  : 饭盆里
# @File    : wework_tab.py
# @Software: PyCharm
# @desc    :
from interface.weworkApi.baseapi import BaseApi
from interface.weworkApi.util import Util

class Tab(BaseApi):
    def __init__(self):
        self.data = Util().get_yaml_data('../data/weworkapidata.yaml')
        self.params['access_token'] = Util().get_access_token()

    def create_tag(self,tagname):
        """
        创建tab
        :return:
        """
        self.params['tagname'] = tagname
        response = self.send_1(self.data['create_tag'])
        print('response >> ' + str(response))
        return response

    def update_tagname(self,tagid,tagname):
        """
        更新标签名字
        :param tagid:
        :param tagname:
        :return:
        """
        self.params['tagid'] = tagid
        self.params['tagname'] = tagname
        response = self.send_1(self.data['update_tagname'])
        print('response >> ' + str(response))
        return response

    def delete_tag(self,tagid):
        """
        根据标签ID删除标签
        :return:
        """
        self.params['tagid'] = tagid
        response = self.send_1(self.data['delete_tag'])
        print(response)
        return response