# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 16:51
# @Author  : 饭盆里
# @File    : basepage.py
# @Software: PyCharm
# @desc    :
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    """
    用于存放一些基本方法，比如： 初始化，driver，find
    """

    def __init__(self,driver:WebDriver=None):
        self.driver = driver

    def find(self,locator):
        return self.driver.find_element(*locator)

    def find_and_click(self,locator):
        self.find(locator).click()

    def find_and_sendkeys(self,locator,text):
        self.find(locator).send_keys(text)

    def find_by_scroll(self,text):
        return self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR, f'new UiScrollable'
                                          '(new UiSelector().'
                                          'scrollable(true).'
                                          'instance(0)).'
                                          'scrollIntoView('
                                          'new UiSelector().'
                                          f'text({text}).instance(0));').text

    def webdriver_wait(self,locator):
        return WebDriverWait(self.driver, 10, 0.5).until( \
            expected_conditions.element_to_be_clickable((MobileBy.ID, locator)))
