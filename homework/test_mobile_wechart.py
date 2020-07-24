# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 21:05
# @Author  : 饭盆里
# @File    : test_wechart.py
# @Software: PyCharm
# @desc    :
import random
import re

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWechat:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps['skipServerInstallation'] = 'true'  # 跳过 uiautomator2 server的安装
        caps['skipDeviceInitialization'] = 'true'  # 跳过设备初始化
        caps['settings[waitForIdleTimeout]'] = 0  #等待Idle为0

        # 与sever 建立连接，初始化一个driver，创建session
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_punch_the_clock(self):

        #d点击工作台
        self.driver.find_element(MobileBy.XPATH,'//*[@text="工作台"]').click()

        # 滚动查找 "打卡" 元素
        self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
                                          '(new UiSelector().'
                                          'scrollable(true).'
                                          'instance(0)).'
                                          'scrollIntoView('
                                          'new UiSelector().'
                                          'text("打卡").instance(0));').click()

        #切换到外出打卡tab页
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/gw8').click()

        #点击打卡按钮
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/ao_').click()

        #打卡成功校验
        result = self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/n7').text
        assert '打卡成功' in result


    def test_wechart_addmember(self):
        name = '饭饭'+str(random.randint(0,1000))
        tel = random.randint(13100000000,13199999999)

        #点击通讯录
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()

        # 滚动查找获取当前列表页的人数
        member_text = self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
                                          '(new UiSelector().'
                                          'scrollable(true).'
                                          'instance(0)).'
                                          'scrollIntoView('
                                          'new UiSelector().'
                                          'textContains("共").instance(0));').text
        member_num = int(re.match(r'共(\d+)人',member_text).group(1))


        #滚动查找并点击添加成员按钮
        self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
                                          '(new UiSelector().'
                                          'scrollable(true).'
                                          'instance(0)).'
                                          'scrollIntoView('
                                          'new UiSelector().'
                                          'text("添加成员").instance(0));').click()

        #点击手动输入添加
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/hgx').click()
        #输入姓名
        self.driver.find_element(MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.EditText').send_keys(name)

        #选择性别
        self.driver.find_element(MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout').click()
        self.driver.find_element(MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout').click()

        #输入手机号
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/f1e').send_keys(tel)

        #点击按钮
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/h9w').click()

        #返回
        back_element = WebDriverWait(self.driver,10,0.5).until(\
            expected_conditions.element_to_be_clickable((MobileBy.ID,'com.tencent.wework:id/h9e')))
        back_element.click()

        # 滚动获取当前列表页的人数
        member_text_new  = self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
                                          '(new UiSelector().'
                                          'scrollable(true).'
                                          'instance(0)).'
                                          'scrollIntoView('
                                          'new UiSelector().'
                                          'textContains("共").instance(0));').text

        member_num_new = int(re.match(r'共(\d+)人', member_text_new).group(1))

        assert member_num == member_num_new -1


    def test_wechart_delete_member(self):
        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()

        # 滚动查找获取当前列表页的人数
        member_text = self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
                                          '(new UiSelector().'
                                          'scrollable(true).'
                                          'instance(0)).'
                                          'scrollIntoView('
                                          'new UiSelector().'
                                          'textContains("共").instance(0));').text
        member_num = int(re.match(r'共(\d+)人', member_text).group(1))

        # 点击对员工操作按钮
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/h9u').click()
        # 点击要删除员工后面的操作按钮
        self.driver.find_element(MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[3]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView').click()

        # 滚动查找 "删除成员" 元素
        self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
                                          '(new UiSelector().'
                                          'scrollable(true).'
                                          'instance(0)).'
                                          'scrollIntoView('
                                          'new UiSelector().'
                                          'text("删除成员").instance(0));').click()
        # 确定删除
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/bci').click()

        # 获取当前列表页的人数
        member_text_new = self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
                                          '(new UiSelector().'
                                          'scrollable(true).'
                                          'instance(0)).'
                                          'scrollIntoView('
                                          'new UiSelector().'
                                          'textContains("共").instance(0));').text
        member_num_new = int(re.match(r'共(\d+)人', member_text_new).group(1))

        assert member_num == member_num_new + 1




