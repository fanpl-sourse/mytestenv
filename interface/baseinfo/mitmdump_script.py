# -*- coding: utf-8 -*-
# @Time    : 2020/8/13 14:59
# @Author  : 饭盆里
# @File    : mitmdump_script.py
# @Software: PyCharm
# @desc    :
import json

from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url == "https://www.baidu.com/":
        with open('xueqiu.json',encoding="utf-8") as f:
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                # b"Hello World",  # (optional) content
                # {"Content-Type": "text/html"}  # (optional) headers
                f.read(),
                {"Content-Type": "application/json"}
            )

def response(flow: http.HTTPFlow):
    if 'quote.json' in flow.request.pretty_url:
        data = json.loads(flow.response.content)
        data['data']['items'][0]['quote']['name'] = 'fanpl'
        flow.response.text = json.dumps(data)