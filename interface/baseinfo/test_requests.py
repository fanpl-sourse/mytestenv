# -*- coding: utf-8 -*-
# @Time    : 2020/8/13 19:56
# @Author  : 饭盆里
# @File    : test_requests.py
# @Software: PyCharm
# @desc    :
import pytest
import requests
import pystache
from jsonpath import jsonpath
from hamcrest import *

class TestRequests():
    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get')
        print(r.status_code)
        print(r.text)
        print(r.headers)
        assert r.status_code==200
        # r = requests.get('https://www.baidu.com/')
        # r = requests.put('https://httpbin.org/put',data={'key':'walue'})
        # r = requests.delete('https://httpbin.org/delete')
        # r = requests.head('https://httpbin.org/get')
        # r = requests.options('https://httpbin.org/put')

    def test_get_query(self):
        payload = {
            "a":"1",
            "b":"2"
        }
        r = requests.get('https://httpbin.org/get',params=payload)
        print(r.text)

    def test_post_form(self):
        formdata = {
            "a":"1",
            "b":"2"
        }
        r = requests.post('https://httpbin.org/post',data=formdata)
        print(r.text)

    def test_get_headers(self):
        headers = {"name":"fanpl","Cookie":"Cookie=fanplcookie"}
        # cookie = {"cookies_are":"123"}
        # cookie = dict(cookies_are="123")
        r = requests.get('https://httpbin.org/get',headers=headers)
        print(r.text)
        assert r.status_code==200
        assert r.json()['headers']['Name'] == 'fanpl'

    def test_post_data(self):
        json = {
            "a":1,
            "b":"hi"
        }
        r = requests.post(url='https://httpbin.org/post',json=json)
        print(r.text)
        print(r.status_code)

    @pytest.mark.parametrize('name',[
        ('cc'),
        ('jj'),
        ('ll')
    ])
    def test_pystache(self,name):
        # print(pystache.render('Hi {{person}}', {'person': name}))

        c2 = {
            "header": "Colors2222",
            "items": [
                {"name": name, "first": True}
            ],
            "empty": False
        }

        t = open("ttt.mustache", "r")  # 用文件作为模板
        filecontent = pystache.render(t.read(), c2)
        print(filecontent)

    def test_response_assert_json(self):
        r = requests.get('https://ceshiren.com/categories_and_latest')
        print(r.text)
        #json形式
        assert r.json()['category_list']['categories'][0]['name'] == '社区治理'
        #json path形式
        assert jsonpath(r.json(),'$..name')[0] == '社区治理'

    def test_hamcrest(self):
        r = requests.get('https://ceshiren.com/categories_and_latest')
        assert_that(r.json()['category_list']['categories'][0]['name'],equal_to('社区治理'))


    def test_oauth(self):
        r = requests.get('http://httpbin.testing-studio.com/basic-auth/test/123',
                         auth = ("selenium_ui_jenkins","123"))
        print(r.text)



