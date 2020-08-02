# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 17:31
# @Author  : 饭盆里
# @File    : test_devices_api.py
# @Software: PyCharm
# @desc    : 设备交互API 比如：打电话 发短信

from time import sleep

from appium.webdriver.extensions.android.gsm import GsmCallActions
from hamcrest import *
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiuSearch():
  def setup(self):
      desire_cap= {
        "platformName": "android",
        "deviceName": "emulator-5554",
        "appPackage": "cn.kmob.screenfingermovelock",
        "appActivity": "com.samsung.ui.MainActivity",
      }

      self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_cap)
      self.driver.implicitly_wait(20)

  def teardown(self):
    self.driver.quit()

  def test_phone_call(self):
      self.driver.make_gsm_call('5551234567', GsmCallActions.CALL)
      sleep(3)

