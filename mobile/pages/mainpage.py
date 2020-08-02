# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 16:16
# @Author  : 饭盆里
# @File    : mainpage.py
# @Software: PyCharm
# @desc    :
from mobile.pages.basepage import BasePage
from mobile.pages.contactlistpage import ContactlistPage


class MainPage(BasePage):
    """
    主页面
    """
    def goto_contactlist(self):
        """
        进入通讯录
        :return:
        """
        return ContactlistPage()