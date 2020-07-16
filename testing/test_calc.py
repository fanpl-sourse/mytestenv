#!/usr/bin/env python
import pytest
import sys
print(sys.path.append('..'))

from pythoncode.calc import Calculator


class TestCal:

    def setup_class(self):
        print("类")
    def teardown_class(self):
        print("类 teardown")

    @pytest.mark.add
    @pytest.mark.parametrize('a,b,result',[
        (1,1,2),
        (2,3,5),
        (6,5,11)
    ])
    def test_add(self,a,b,result):
         cal = Calculator()
         assert result== cal.myadd(a,b)

    # @pytest.mark.div
    # def test_div(self,a,b):
    #         cal = Calculator()
    #         assert 2== cal.mydiv(2,1)
