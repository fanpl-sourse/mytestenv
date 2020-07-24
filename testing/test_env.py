# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 13:37
# @Author  : 饭盆里
# @File    : test_env.py
# @Software: PyCharm
# @desc    :

#测试用例通过传入fixture 方法，获取测试/开发数据
def test_case(cmdoption):
    print("测试环境验证")
    myenv,mydatas = cmdoption
    print(myenv)
    ip = mydatas['env']['ip']
    port = mydatas['env']['port']
    print("https://"+str(ip)+':'+str(port))
