# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 16:19
# @Author  : 饭盆里
# @File    : addmemberpage.py
# @Software: PyCharm
# @desc    :
from mobile.pages.basepage import BasePage
from mobile.pages.contactaddpage import ContactAddPage


class AddMemberPage(BasePage):
    def add_menual(self):

        return ContactAddPage()