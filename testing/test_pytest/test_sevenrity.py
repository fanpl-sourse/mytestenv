# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 19:09
# @Author  : 饭盆里
# @File    : test_sevenrity.py
# @Software: PyCharm
# @desc    :
import allure


def test_with_no_severity_label():
    print("no")

@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    print("trivial 轻微")

@allure.severity(allure.severity_level.MINOR)
def test_with_minor_severity():
    print("minor 轻微")

@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity():
    print("noraml 一般")

@allure.severity(allure.severity_level.CRITICAL)
def test_with_critical_severity():
    print("critical 功能缺失")

@allure.severity(allure.severity_level.BLOCKER)
def test_with_blocker_severity():
    print("blocker 中断")

@allure.severity(allure.severity_level.BLOCKER)
def test_with_blocker_severity2():
    print("blocker 中断2")