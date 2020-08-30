# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 20:04
# @Author  : 饭盆里
# @File    : testwework_tab.py
# @Software: PyCharm
# @desc    :
import pytest

from interface.weworkApi.wework_tab import Tab
class TestWeworkTab():

    @pytest.mark.parametrize('tagname',[('fanfan')])
    def test_create_tag(self,tagname):
        result= Tab().create_tag(tagname)
        print(result['tagid'])
        print(type(result))

    @pytest.mark.parametrize('tagid,tagname',[
        ('4','lili-gai')
    ])
    def test_update_tagname(self,tagid,tagname):
        Tab().update_tagname(tagid,tagname)

    @pytest.mark.parametrize('tagid',[('4')])
    def test_delete_tag(self,tagid):
        Tab().delete_tag(tagid)

    @pytest.mark.parametrize('tagname',[('hu')])
    def test_tag_serious(self,tagname):
        create_tag = Tab().create_tag(tagname)
        assert 'created' == create_tag['errmsg']
        tagid =  create_tag['tagid']

        assert 'updated' == Tab().update_tagname(str(tagid), tagname)['errmsg']
        assert 'deleted' == Tab().delete_tag(str(tagid))['errmsg']
