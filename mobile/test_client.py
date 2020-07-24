# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 14:41
# @Author  : 饭盆里
# @File    : test_client.py
# @Software: PyCharm
# @desc    :
from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.xueqiu.android'
desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
desired_caps['dontStopAppOnReset'] = 'true'

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

driver.implicitly_wait(5)
driver.find_element(By.ID,'com.xueqiu.android:id/home_search').click()
driver.find_element(By.ID,'com.xueqiu.android:id/search_input_text').send_keys('alibaba')
driver.find_element(By.ID,'com.xueqiu.android:id/name').click()

sleep(3)
driver.back()

driver.quit()


