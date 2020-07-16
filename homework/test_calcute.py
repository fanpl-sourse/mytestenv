# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 12:01
# @Author  : 饭盆里
# @File    : test_calcute.py
# @Software: PyCharm
# @desc    :
#    1、补全计算器（加减乘除）的测试用例
#    2、使用数据驱动完成测试用例的自动生成
#    3、conftest.py中创建fixture 完成setup和teardown
#    4、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
import sys
import pytest
import yaml
sys.path.append('..')
from pythoncode.calcute import Calculator

datafilepath = '../data/calculate_data.yaml'

def readyaml(file_path):
    with open(file_path,encoding='utf-8') as f:
        data = yaml.safe_load(f)
    print(f"加载yaml文件:{file_path}文件的数据为：{data}")
    return data

class TestCalcute:
    #类级别的：类前后运行
    @classmethod
    def setup_class(cls):
        cls.cal = Calculator()
        print('类setup')

    @classmethod
    def teardown_class(cls):
        print('类teardown')


    @pytest.mark.myadd
    @pytest.mark.parametrize("a,b,result",
                             readyaml(datafilepath)['int'],
                             ids=['int1','int2','fushu','float1','bigdata','float2'])
    def test_myadd(self,a,b,result):
        assert result == self.cal.myadd(a,b)

    @pytest.mark.mydiv
    @pytest.mark.parametrize("a,b,result",[
        (3,2,1.5)
    ])
    def test_mydiv(self,a,b,result):
        assert self.cal.mydiv(a,b) == result


