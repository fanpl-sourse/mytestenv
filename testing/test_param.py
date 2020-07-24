# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 14:22
# @Author  : 饭盆里
# @File    : test_param.py
# @Software: PyCharm
# @desc    :

# datas = [[1,2,3],[0.1,0.4,0.5]]
# myids = ['整数','浮点']
import yaml

with open("../data/calculate_data_testing.yaml") as f:
    alldata = yaml.safe_load(f)
    #myids,mydatas 应该与 conftest.py 中hook函数 pytest_generate_tests 的 metafunc.module.mydatas,ids=metafunc.module.myids一致
    myids = alldata.keys()
    mydatas = alldata.values()

#param 要与conftest.py 中hook函数 pytest_generate_tests 的param保持一致
def test_param(param):
    print(f"param: {param}")