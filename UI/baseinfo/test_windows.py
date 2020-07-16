# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 14:44
# @Author  : 饭盆里
# @File    : test_windows.py
# @Software: PyCharm
# @desc    :
import sys
sys.path.append('..')
from time import sleep
from UI.baseinfo.SetupTeardown import setupTeardown


class TestWindows(setupTeardown):
    def test_windows(self):
        self.driver.get('https://www.baidu.com/')
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)
        self.driver.find_element_by_xpath('//*[@id="u1"]/a[2]').click()
        self.driver.find_element_by_link_text('立即注册').click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        sleep(1)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        self.driver.find_element_by_xpath('//*[@name="userName"]').send_keys('hi')
        sleep(1)
        self.driver.switch_to.window(windows[0])
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        self.driver.find_element_by_name('userName').send_keys('hi')
        sleep(1)



