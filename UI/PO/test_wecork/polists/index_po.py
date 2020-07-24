# -*- coding: utf-8 -*-
# @Time    : 2020/7/20 10:31
# @Author  : 饭盆里
# @File    : index_po.py
# @Software: PyCharm
# @desc    : 企业微信首页
from selenium.webdriver.common.by import By
from UI.PO.test_wecork.polists.base_po import BasePage
from UI.PO.test_wecork.polists.login_po import Login
from UI.PO.test_wecork.polists.registe_po import Registe

class Index(BasePage):
    """
    首页PO
    """
    _base_url = 'https://work.weixin.qq.com/'

    def goto_register(self):
        """
        点击立即注册
        进入立即注册PO
        :return: 注册页面实例
        """
        self.find(By.XPATH,'//*[@class="index_head_info_pCDownloadBtn"]').click()
        return Registe()

    def goto_login(self):
        """
        点击企业登陆
        进入企业登陆PO
        :return: 登陆页面实例
        """
        self.find(By.CSS_SELECTOR,'.index_top_operation_loginBtn').click()
        return Login(self._driver)

if __name__ == '__main__':
        # Index().goto_register()
        Index().goto_login()
