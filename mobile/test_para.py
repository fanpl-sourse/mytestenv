# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 19:18
# @Author  : 饭盆里
# @File    : test_para.py
# @Software: PyCharm
# @desc    :
from time import sleep

import pytest
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
        "appPackage": "com.xueqiu.android",
        "appActivity": ".view.WelcomeActivityAlias",
        "noReset":True,
        "skipSeverInstallation":True,
        "unicodeKeyBord":'true'
      }

      self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_cap)
      self.driver.implicitly_wait(20)

  def teardown(self):
      pass
      self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/action_close').click()
    # self.driver.back()
    # self.driver.quit()

  @pytest.mark.parametrize('search_name,code,expect_price',[
      ('alibaba','BABA',250),
      ('小米','BK0611',1300)
  ])
  def test_search(self,search_name,code,expect_price):
      """
          1.打开雪球APP
          2.点击搜索输入框
          3.在搜索框输入"阿里巴巴"
          4.在搜索结果中选择 "阿里巴巴"，然后点击
          5.获取阿里巴巴股价，并判断价格
          6.重新搜索"小米"，进行同样的动作
          :return:
      """
      self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/tv_search').click()
      self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/search_input_text').send_keys(search_name).click()
      self.driver.find_element(MobileBy.XPATH,f'//*[@text="{code}"]').click()
      current_price = self.driver.find_element(MobileBy.XPATH,f'//*[@text="{code}"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text
      print(current_price)
      assert_that(float(current_price),close_to(expect_price,expect_price*0.2))


