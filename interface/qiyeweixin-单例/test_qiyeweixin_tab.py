# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 19:46
# @Author  : 饭盆里
# @File    : test_qiyeweixin_tab.py
# @Software: PyCharm
# @desc    :
import pytest
import requests


class TestTab():
    @pytest.fixture(scope='module')
    def get_access_token(self):
        param = {
            "corpid": "ww9141708bbda1c588",
            "corpsecret": "F_AGdOLLFROJupVo2-H6WGjg8SErlDPb4OBVTsUlOp4"
        }
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=param)
        return r.json()['access_token']

    def test_create_tab(self,get_access_token):
        print(get_access_token)
        json = {"tagname": "UI"}
        r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={get_access_token}',json=json)
        print(r.json())
