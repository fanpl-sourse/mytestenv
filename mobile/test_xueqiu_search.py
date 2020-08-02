# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 16:28
# @Author  : 饭盆里
# @File    : test_xueqiu_search.py
# @Software: PyCharm
# @desc    :
from time import sleep
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
    self.driver.back()
    self.driver.quit()

  def test_search(self):
    """
    1.打开雪球APP
    2.点击搜索输入框
    3.在搜索框输入"阿里巴巴"
    4.在搜索结果中选择 "阿里巴巴"，然后点击
    5.获取阿里巴巴股价，并判断价格>200
    :return: 
    """
    self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
    self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
    self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").click()
    self.driver.find_element(MobileBy.XPATH,'//*[@text="09988"]').click()
    current_price = float(self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/current_price").text)

    assert current_price>200

  def test_attr(self):
    """
    1. 打开【雪球】首页
    2. 定位首页搜索框
    3. 判断搜索框是否可用，并查看搜索框name属性值
    4. 打印搜索这个元素的坐标和宽高
    5. 在搜索框输入：阿里巴巴
    6. 判断阿里巴巴是否可见
    7. 如果可见，打印“搜索成功”，如果不可见，打印“搜索失败”
    :return:
    """
    element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
    if element.is_enabled() == True:
      print(element.text)
      print(element.location)
      # print(element.tag_name)
      print(element.size)
      element.click()
      self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
      element = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
      if element.is_displayed() == True:
        print("搜索成功")
      else:
        print("搜索失败")

  def test_touch(self):
    """
    文本信息
    :return:
    """
    sleep(10)
    action = TouchAction(self.driver)
    #获取窗口尺寸
    window_rect = self.driver.get_window_rect()
    x = int(window_rect['width']/2)
    y1 = int(window_rect['height']*0.2)
    y2 = int(window_rect['height']*0.8)
    action.press(x=x,y=y2).wait(2000).move_to(x=x,y=y1).release().perform()
    sleep(3)

  def test_myinfo(self):
    """
    1. 点击我的，进入个人信息页
    2. 点击登录，进入登录页面
    3. 输入用户名，输入密码
    4. 点击登录
    :return:
    """
    sleep(6)
    self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")').click()
    self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("密码登录")').click()
    sleep(2)
    self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.EditText").textContains("输入")').send_keys('122')
    # self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/login_account').send_keys('122')
    self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("123222")
    # self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/login_password').send_keys('222')

    self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()
    # self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/button_next').click()
    text = self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/md_content').text
    assert '错误' in text

  def test_alibaba_hkprice(self):

    self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/tv_search').click()
    self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/search_input_text').send_keys('alibaba')
    self.driver.find_element(MobileBy.XPATH,'//*[@text="BABA"]').click()
    self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/ti_tab_indicator").childSelector(text("股票"))').click()

    LOCATED = (MobileBy.XPATH,'//*[@text="09988"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]')
    #方案一
    # current_price = self.driver.find_element(*LOCATED).text
    #方案二
    # WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(LOCATED))
    # current_price = self.driver.find_element(*LOCATED).text
    #方案三
    WebDriverWait(self.driver,10).until(lambda x:x.find_element(*LOCATED))
    current_price = float(self.driver.find_element(*LOCATED).text)
    expect_price = 200.0
    # assert float(current_price) > expect_price
    print(current_price)
    assert_that(current_price,close_to(expect_price,expect_price*0.5))

  def test_scroll_find_element(self):
    self.driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
    self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
                                                    'scrollIntoView(new UiSelector().text("青春的泥沼").instance(0))').click()
    sleep(3)












