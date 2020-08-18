# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 17:30
# @Author  : 饭盆里
# @File    : util.py
# @Software: PyCharm
# @desc    :
import requests

class Util():
    def get_access_token(self):
        param = {
            "corpid": "ww9141708bbda1c588",
            "corpsecret": "F_AGdOLLFROJupVo2-H6WGjg8SErlDPb4OBVTsUlOp4"
        }
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=param)
        return r.json()['access_token']


