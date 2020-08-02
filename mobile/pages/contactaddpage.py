# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 16:20
# @Author  : 饭盆里
# @File    : contactaddpage.py
# @Software: PyCharm
# @desc    :
from mobile.pages.addmemberpage import AddMemberPage
from mobile.pages.basepage import BasePage


class ContactAddPage(BasePage):

    def set_name(self,name):
        return self

    def set_gender(self):
        return self

    def set_phone(self,phonenum):
        return self

    def click_save(self):
        return AddMemberPage()