# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 16:39
# @Author  : 饭盆里
# @File    : tt.py
# @Software: PyCharm
# @desc    :
import os
import sys

import yaml


def read_file_steps(path,funcname):
    with open(path, encoding='utf-8') as f:
        steps = yaml.safe_load(f)

    for step in steps[funcname]:
        print(step)

    # for step in steps:
    #     element = self.find(step['By'], step['locator'])
    #     if "action" in step.keys():
    #         action = step['action']
    #         if "click" == action:
    #             element.click()
    #         if "send" == action:
    #             element.send_keys(step['value'])

def test():
    read_file_steps('../data/main.yaml','goto_search')
    # read_file_steps('../data/test_main_data.yaml')

def test_replace():
    a = {"stockname":'alibaba'}
    b = 'VBVVVVV"${stockname}"xCccccc'
    for key, value in a.items():
        b = b.replace('${' + key + '}', value)
    print(b)