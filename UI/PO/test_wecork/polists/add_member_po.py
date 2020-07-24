# -*- coding: utf-8 -*-
# @Time    : 2020/7/20 16:53
# @Author  : 饭盆里
# @File    : add_member_po.py
# @Software: PyCharm
# @desc    :
from time import sleep
from selenium.webdriver.common.by import By
from UI.PO.test_wecork.polists.base_po import BasePage

class AddMember(BasePage):
    '''
    添加成员PO
    '''

    # def __init__(self,driver:webdriver):
    #     self.driver = driver

    def add_member(self):
        """
        添加成员
        :return:
        """
        self.find(By.ID,'username').send_keys('hi1')
        self.find(By.ID,'memberAdd_acctid').send_keys('hi889')
        self.find(By.ID,'memberAdd_phone').send_keys('18800009998')
        self.find(By.CSS_SELECTOR,'.js_btn_save').click()

        sleep(5)

if __name__ == '__main__':
    AddMember().add_member()