# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 16:28
# @Author  : 饭盆里
# @File    : test.py
# @Software: PyCharm
# @desc    :

from appium import webdriver
desire_cap= {
  "platformName": "android",
  "deviceName": "emulator-5554",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".view.WelcomeActivityAlias",
    "noReset":True
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_cap)
driver.implicitly_wait(10)
el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el2.send_keys("阿里巴巴")
el4 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el4.click()
el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
el5.click()
driver.quit()

