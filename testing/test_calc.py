#!/usr/bin/env python
import pytest
import sys
import yaml
print(sys.path.append('..'))

from pythoncode.calc import Calculator

# with open('../data/calculate_data_testing.yaml') as f:
#     datas = yaml.safe_load(f)
#     myids = datas.keys()
#     mydatas = datas.values()


def get_values(opt):
    """
    根据操作的入参，获取对应的数据
    :param opt: 操作，比如：add div 等
    :return:    操作对应等别名 和 数据
    """
    with open('../data/calculate_data.yaml') as f:
        datas = yaml.safe_load(f)
        for operate in datas.keys():
            if operate == opt:
                myids = datas[opt].keys()
                mydatas = datas[opt].values()

    return mydatas,myids

class TestCal:

    def setup_class(self):
        print("类")
    def teardown_class(self):
        print("类 teardown")

    # @pytest.mark.add
    # @pytest.mark.parametrize('a,b,result',[
    #     (1,1,2),
    #     (2,3,5),
    #     (6,5,11)
    # ],ids=['int1','int2','int3'])
    mydatas ,myids= get_values('add')
    @pytest.mark.parametrize('a,b,result',mydatas,ids=myids)
    def test_add(self,a,b,result):
         cal = Calculator()
         assert result== cal.myadd(a,b)

    # @pytest.mark.div
    mydatas,myids = get_values('div')
    @pytest.mark.parametrize('a,b,result',mydatas,ids=myids)
    def test_div(self,a,b,result):
            cal = Calculator()
            try:
                assert result== cal.mydiv(a,b)
            except ZeroDivisionError as es:
                print('被除数为0')
