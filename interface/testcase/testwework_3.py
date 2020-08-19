# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 17:41
# @Author  : 饭盆里
# @File    : wework_1.py
# @Software: PyCharm
# @desc    :
import requests

from interface.weworkApi.wework_3 import Member
from interface.weworkApi.util import Util
class TestWework:
    def test_access_token(self):
        print(Util().get_access_token())

    def test_create_member(self):
        Member().create_member('ee2','ee2','e2','18788888890')

    def test_get_member(self):
        Member().get_member('ee2')

    def test_update_member(self):
        Member().update_member('ee2','ee2','ee2')

    def test_delete_member(self):
        Member().delete_member('ee2')

    def test_session(self):
        s = requests.session()
        s.params = {"access_token":Util().get_access_token()}
        res = s.get('https://qyapi.weixin.qq.com/cgi-bin/user/get?userid=ee2')
        print(res.json())
