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
    def test_create_tab(self,tagname):
        Tab().create_tab(tagname)

    @pytest.mark.parametrize('tagid,tagname',[
        ('4','lili-gai')
    ])
    def test_update_tagname(self,tagid,tagname):
        Tab().update_tagname(tagid,tagname)

    @pytest.mark.parametrize('tagid',[('4')])
    def test_delete_tag(self,tagid):
        Tab().delete_tag(tagid)