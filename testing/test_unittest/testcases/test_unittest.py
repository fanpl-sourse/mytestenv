# -*- coding: utf-8 -*-
# @Time    : 2020/7/10 22:00
# @Author  : 饭盆里
# @File    : test_unittest.py
# @Software: PyCharm
# @desc    :

import unittest

class TestStringMethods(unittest.TestCase):

    # setup teardown 在每条测试用例前后分别调用的方法
    #-> None  :默认返回值为None
    def setUp(self) -> None:
        print("setup")
    def tearDown(self) -> None:
        print("teardown")

    # setupclass teardownclass 整个类的前后调用的方法
    # 类级别的方法，需要加上装饰器
    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")
    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

    def test_h(self):
        print("hi")

    def test_upper(self):
        print("upper")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("isupper")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print("split")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()