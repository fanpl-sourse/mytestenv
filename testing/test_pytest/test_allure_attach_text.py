# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 19:28
# @Author  : 饭盆里
# @File    : test_allure_attach_text.py
# @Software: PyCharm
# @desc    :
import allure


def test_allure_attach_text():
    allure.attach("寸寸寸文本",attachment_type=allure.attachment_type.TEXT)


def test_allure_attach_html():
    allure.attach("<body>html</body>",name='html测试块',attachment_type=allure.attachment_type.HTML)

def test_allure_attach_picture():
    allure.attach.file('/Users/a/Pictures/20200601-0607.png',name="图片",attachment_type=allure.attachment_type.PNG)