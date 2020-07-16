# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 17:14
# @Author  : 饭盆里
# @File    : test_feature_story.py
# @Software: PyCharm
# @desc    :
import allure

@allure.feature("登录模块")
class TestLogin:
    @allure.story("登录成功")
    def test_login_success(self):
        print("测试登录成功")

    @allure.story("登录失败")
    def test_login_success_a(self):
        print("测试登录失败")

    @allure.story("用户名缺失")
    def test_login_success_b(self):
        print("测试登录时未输入登录名")

    @allure.story("密码缺失")
    def test_login_success_c(self):
        print("测试登录未输入密码")
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("请输入密码")
        print("点击登录")
        with allure.step("点击登录后登录失败"):
            print("登录失败")

