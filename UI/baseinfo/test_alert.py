# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 22:56
# @Author  : 饭盆里
# @File    : test_alert.py
# @Software: PyCharm
# @desc    :
from time import sleep
from selenium.webdriver import ActionChains
from UI import setupTeardown


class TestAlert(setupTeardown):
    def test_alert(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

        self.driver.switch_to.frame('iframeResult')

        drag = self.driver.find_element_by_xpath('//*[@class="ui-draggable"]')
        drop = self.driver.find_element_by_xpath('//*[@class="ui-droppable"]')

        action = ActionChains(self.driver)
        action.drag_and_drop(drag,drop).perform()

        sleep(2)
        self.driver.switch_to.alert.accept()
        sleep(2)
        #回到默认frame
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id('submitBTN').click()

        sleep(2)


