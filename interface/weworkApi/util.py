# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 17:30
# @Author  : 饭盆里
# @File    : util.py
# @Software: PyCharm
# @desc    :
import requests
import yaml
from interface.weworkApi.baseapi import BaseApi
class Util():
    def get_access_token(self):
        # param = {
        #     "corpid": "ww9141708bbda1c588",
        #     "corpsecret": "F_AGdOLLFROJupVo2-H6WGjg8SErlDPb4OBVTsUlOp4"
        # }
        # r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=param)
        # print(r.json()['access_token'])
        # return r.json()['access_token']

        data = self.get_yaml_data('../data/access_token.yaml')
        return BaseApi().send_1(data['access_token'])['access_token']



    def get_yaml_data(self,file):
        with open(file,encoding='utf-8') as f:
            data = yaml.safe_load(f)
            return data


