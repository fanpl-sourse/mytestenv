# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 16:22
# @Author  : 饭盆里
# @File    : test_contact.py
# @Software: PyCharm
# @desc    :
from mobile.pages.app import App


class  TestContact:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def test_addcontact(self):
        """
        添加联系人
        :return:
        """
        self.main.goto_contactlist().add_contact().add_menual()