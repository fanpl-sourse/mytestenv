#!/usr/bin/env python
# encoding: utf-8
'''
@author: fanpl
@file: test_baidu.py
@time: 2020/7/9 17:50
@desc:
'''
import pytest
import selenium
import requests

class TestData:
    @pytest.mark.parametrize("a,b",[(1,2),(3,5),(6,7)])
    def test_data(self,a,b):
        print(a+b)

