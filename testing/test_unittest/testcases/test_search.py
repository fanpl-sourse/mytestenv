# -*- coding: utf-8 -*-
# @Time    : 2020/7/10 22:22
# @Author  : 饭盆里
# @File    : test_search.py
# @Software: PyCharm
# @desc    :

#被测方法
import unittest

class Search:
    def search(self):
        print("search")
        return True

#单元测试类
class TestSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.search = Search()
        print("setUpclass")
    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

    def setUp(self) -> None:
        print("每个方法前执行setup")
    def tearDown(self) -> None:
        print("每个方法后执行teardown")

    def test_search1(self):
        print("search1")

        assert True == self.search.search()

    def test_search2(self):
        print("search2")
        assert True == self.search.search()

class TestAssert(unittest.TestCase):
    def test_equal(self):
        print('断言相等')
        self.assertEqual(1,1,'相等')
    def test_notequal(self):
        print('不等')
        self.assertNotEqual(1,2)
    def test_true(self):
        print("真")
        self.assertTrue(1==1)


if __name__ == '__main__':
    ##方法一： 执行当前文件所有用例
    # unittest.main()
    ##方法二：执行指定的用例
    # suite = unittest.TestSuite()
    # suite.addTest(TestSearch("test_notequal"))
    # suite.addTest(TestSearch("test_true"))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    ##方法三：执行指定类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestAssert)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
    suite = unittest.TestSuite([suite1,suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)