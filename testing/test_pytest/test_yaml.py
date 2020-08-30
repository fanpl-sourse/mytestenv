# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 15:51
# @Author  : 饭盆里
# @File    : test_yaml.py
# @Software: PyCharm
# @desc    :
import pytest
import yaml

class TestYaml:
    @pytest.mark.parametrize("env", yaml.safe_load(open("data/yaml.yaml")))
    def test_yaml(self,env):
        if "selenium_ui_jenkins" in env:
            print('这是测试环境')
            print(f'{env["selenium_ui_jenkins"]}')
        elif "dev" in env:
            print("这是开发环境")
            print(f'开发环境IP：{env["dev"]}')