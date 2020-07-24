# -*- coding: utf-8 -*-
# @Time    : 2020/7/20 13:56
# @Author  : 饭盆里
# @File    : firstpage_po.py
# @Software: PyCharm
# @desc    :
from time import sleep
from selenium.webdriver.common.by import By
from UI.PO.test_wecork.polists.add_member_po import AddMember
from UI.PO.test_wecork.polists.base_po import BasePage


class FirstPage(BasePage):
    """
    登陆后首页
    """
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'
    def goto_add_member(self):
        """
        添加成员
        :return:
        """
        self.find(By.CSS_SELECTOR,'.index_service_cnt_item_title').click()
        return AddMember()

    def goto_add_member_tab(self):
        """
        通过顶部的tab进入到添加成员页面
        :return:
        """
        #tab点击
        self.find(By.XPATH,'//*[@id="menu_contacts"]').click()
        sleep(3)
        #显示等待的条件
        def add_member_condition(x):
            element_lens = len(self.finds(By.ID,'username'))
            if element_lens <= 0:
                self.find(By.XPATH, '//*[@class="ww_operationBar"]/a[1]').click()
            return element_lens > 0

        self.wait_for_condition(add_member_condition)
        return AddMember()


    def import_address(self):
        """
        导入通讯录
        :return:
        """
        pass

    def member_join(self):
        """
        成员加入
        :return:
        """
        pass

if __name__ == '__main__':
    FirstPage().goto_add_member_tab().add_member()
