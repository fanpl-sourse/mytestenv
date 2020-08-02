# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 16:17
# @Author  : 饭盆里
# @File    : contactlistpage.py
# @Software: PyCharm
# @desc    :
from mobile.pages.addmemberpage import AddMemberPage
from mobile.pages.basepage import BasePage


class ContactlistPage(BasePage):
    """
    通讯录列表页
    """

    def add_contact(self):
        """
        添加成员
        :return:
        """
        return AddMemberPage()

    def search_contact(self):
        """
        搜索联系人
        :return:
        """