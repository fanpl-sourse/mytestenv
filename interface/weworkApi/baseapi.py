# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 17:39
# @Author  : 饭盆里
# @File    : baseapi.py
# @Software: PyCharm
# @desc    :
import json
import requests

class BaseApi():
    params = {}
    def send(self,data):
        """
        基础版的：引用requests底层的逻辑
        :param data:
        :return:
        """
        return requests.request(**data).json()


    def send_1(self,data):
        """
        优化一： 将${}参数替换为输入的变量值
        :param filepath:  {'create_member': {'method': 'post', 'url': 'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=${self.access_token}', 'json': {'userid': '${userid}', 'name': '${name}', 'alias': '${alias}', 'mobile': '${mobile}', 'department': [1]}}}
        :return:
        """
        raw_data = json.dumps(data)
        for key,value in self.params.items():
            raw_data = raw_data.replace("${"+key+"}",value)
        data = json.loads(raw_data)
        print("request >>  "+str(data))
        return requests.request(**data).json()
