#!/usr/bin/env python
import pytest

# 被测试方法
def test_search1(login):
    print("test_search1")

@pytest.mark.parametrize('a,b',[(1,2),(4,3)])
def test_search2(a,b):
    print("test_search2")