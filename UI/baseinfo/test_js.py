# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 20:02
# @Author  : 饭盆里
# @File    : test_js.py
# @Software: PyCharm
# @desc    :
from time import sleep
import pytest
from UI.baseinfo.SetupTeardown import setupTeardown

class TestJs(setupTeardown):
    @pytest.mark.skip
    def test_js(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element_by_name('wd').send_keys('selenium官网')
        click_element = self.driver.execute_script("return document.getElementById('su')")
        click_element.click()
        sleep(2)
        self.driver.execute_script('return document.documentElement.scrollTop=10000')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@class="page-inner"]//a[last()]').click()
        sleep(5)

        for i in [
            'return document.title',
            #性能参数
            'return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(i))


    def test_js_time(self):
        self.driver.get('https://www.12306.cn/index/')
        # self.driver.execute_script('a = document.getElementById("train_date");a.removeAttribute("readonly")')
        # print(self.driver.execute_script('return document.getElementById("train_date").value="2020-06-12"'))

        element = self.driver.execute_script('return document.getElementById("train_date")')
        remove_js = r'arguments[0].removeAttribute("readonly")'
        set_time_js = r'arguments[0].value="2020-06-12"'
        self.driver.execute_script(remove_js,element)
        print(self.driver.execute_script(set_time_js,element))

        sleep(2)