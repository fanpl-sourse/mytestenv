# -*- coding: utf-8 -*-
# @Time    : 2020/7/10 23:22
# @Author  : 饭盆里
# @File    : runtest.py
# @Software: PyCharm
# @desc    :
import unittest

from testing.test_unittest.beautyReport.HTMLTestRunner_PY3.HTMLTestRunner import HTMLTestRunner

report_title = 'Example用例执行报告'
desc = '用于展示修改样式后的HTMLTestRunner'
report_file = 'ExampleReport.html'

test_dir = 'testcases/'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
# unittest.TextTestRunner().run(discover)

with open(report_file, 'wb') as report:
    runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
    runner.run(discover)