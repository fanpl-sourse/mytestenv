# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 17:49
# @Author  : 饭盆里
# @File    : test_allure_link_issue.py
# @Software: PyCharm
# @desc    :
import allure

@allure.link('https://www.baidu.com/',name='百度链接')
def test_with_link():
    print("有链接")

TEST_CASE_LINK = 'https://www.baidu.com/'
@allure.link(TEST_CASE_LINK,name='测试用例路径')
def test_with_testcase_link():
    print("测试用例链接")

# --allure-link-pattern=issue:https://www.tapd.cn/51472312/bugtrace/bugs/view?bug_id={}
@allure.issue('1000','此处存在BUG，点击此链接')
def test_with_bug_link():
    print("缺陷链接")