# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 11:30
# @Author  : 饭盆里
# @File    : test_qiyeweixin.py
# @Software: PyCharm
# @desc    :
import re
import pytest
import requests

def test_data():
    """
    生成测试数据：用户ID 用户名 用户别名 手机号
    :return:
    """
    # [('rr', '人人', '人人', '18788778877')]
    data = [('ff'     + str(i),
             'fanfan' + str(i),
             'fanfan',
             '13811%06d' % i) for i in range(20)]
    print(data)
    return data


class TestMember():
    @pytest.fixture(scope='module')
    def get_access_token(self):
        param = {
            "corpid": "ww9141708bbda1c588",
            "corpsecret": "F_AGdOLLFROJupVo2-H6WGjg8SErlDPb4OBVTsUlOp4"
        }
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=param)
        return r.json()['access_token']

    @pytest.mark.parametrize('userid,name,alias,mobile',[
        ('rr','人人','人人','18788778877')
    ])
    def test_create_member(self,get_access_token,userid,name,alias,mobile):
        """
        创建通讯录用户
        :return:
        """
        jsondata={
                "userid": userid,
                "name": name,
                "alias": alias,
                "mobile": mobile,
                "department": [1]
        }

        r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_access_token}',
                      json=jsondata)
        print(r.json())
        return r.json()

    @pytest.mark.parametrize('userid',[('rr')])
    def test_get_member(self,get_access_token,userid):
        """
        获取成员
        :return:
        """
        # access_token = self.get_access_token()
        print(get_access_token)
        r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_access_token}&userid={userid}')
        print(r.json())
        return r.json()

    @pytest.mark.parametrize('userid,name,alias',[
        ('rr','人人','人人')
    ])
    def test_update_member(self,get_access_token,userid,name,alias):
        """
        更新成员
        :return:
        """
        # access_token = self.get_access_token()
        jsondata={
            "userid": userid,
            "name": name,
            "alias": alias,
        }
        r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_access_token}',json=jsondata)
        print(r.json())
        return r.json()

    @pytest.mark.parametrize('userid',[('rr')])
    def test_delete_member(self,get_access_token,userid):
        """
        删除成员
        :return:
        """
        # access_token = self.get_access_token()
        r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_access_token}&userid={userid}')
        print(r.json())
        return r.json()

    # @pytest.mark.parametrize('userId,name,alias,mobile',[('rr','人人','人人','18788778877')])
    @pytest.mark.parametrize('userId,name,alias,mobile', test_data())
    def test_wework_series(self,get_access_token,userId,name,alias,mobile):
        """
        企业微信系列动作:集成测试
        :return:
        """
        try:
            assert 'created' == self.test_create_member(get_access_token,userId,name,alias,mobile)['errmsg']
        except AssertionError as e:
            if "mobile existed" in e.__str__():
                userId = re.findall(':(.*)\'',e.__str__())[0]
                self.test_delete_member(get_access_token,userId)
                assert 'created' == self.test_create_member(get_access_token, userId,name,alias,mobile)['errmsg']

        assert 'fanfan' in self.test_get_member(get_access_token,userId)['name']
        assert 'updated' == self.test_update_member(get_access_token,userId,'人人-改','人人-改')['errmsg']
        assert 'deleted' == self.test_delete_member(get_access_token,userId)['errmsg']
