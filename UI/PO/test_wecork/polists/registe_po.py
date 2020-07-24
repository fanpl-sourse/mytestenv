# -*- coding: utf-8 -*-
# @Time    : 2020/7/20 10:39
# @Author  : 饭盆里
# @File    : registe_po.py
# @Software: PyCharm
# @desc    :
from selenium.webdriver.common.by import By
from UI.PO.test_wecork.polists.base_po import BasePage

class Registe(BasePage):
    """
    企业注册PO
    """
    _base_url = 'https://work.weixin.qq.com/wework_admin/register_wx?from=myhome'

    def registe(self):
        """
        输入内容
        选择下拉框
        :return:
        """
        self.find(By.ID,'corp_name').send_keys('我的企业微信')
        self.find(By.ID,'manager_name').send_keys('小企鹅')
        self.find(By.NAME,'registerTel').send_keys('18800009999')


if __name__ == '__main__':
    Registe().registe()
