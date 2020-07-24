# -*- coding: utf-8 -*-
# @Time    : 2020/7/20 10:31
# @Author  : 饭盆里
# @File    : login_po.py
# @Software: PyCharm
# @desc    :
from selenium.webdriver.common.by import By
from UI.PO.test_wecork.polists.base_po import BasePage
from UI.PO.test_wecork.polists.registe_po import Registe


class Login(BasePage):
    """
    登陆页面PO
    """
    _base_url = 'https://work.weixin.qq.com/wework_admin/loginpage_wx'

    def sacn_login(self):
        """
        扫描二维码登陆
        :return:
        """

    def goto_register(self):
        """
        点击企业注册按钮
        进入企业注册PO
        :return:
        """
        self.find(By.CSS_SELECTOR,'.login_registerBar_link').click()
        return Registe()

if __name__ == '__main__':
    Login().goto_register()