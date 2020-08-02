# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 16:12
# @Author  : 饭盆里
# @File    : app.py
# @Software: PyCharm
# @desc    :
from appium import webdriver

from mobile.pages.basepage import BasePage
from mobile.pages.mainpage import MainPage


class App(BasePage):
    """
    存放APP常用的方法：启动、重启、关闭、进入首页
    """
    def start(self):
        """
        启动
        :return:
        """

        if self.driver == None:

            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "emulator-5554"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"
            caps['skipServerInstallation'] = 'true'  # 跳过 uiautomator2 server的安装
            caps['skipDeviceInitialization'] = 'true'  # 跳过设备初始化
            caps['settings[waitForIdleTimeout]'] = 0  # 等待Idle为0

            # 与sever 建立连接，初始化一个driver，创建session
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        else:
              #无需参数，自动启动desireCapa里面定义的activity
            self.driver.launch_app()


        self.driver.implicitly_wait(5)

        return self

    def restart(self):
        """
        重启
        :return:
        """
        self.driver.close()
        self.driver.launch_app()
        return self

    def stop(self):
        """
        关闭APP
        :return:
        """
        self.driver.close()

    def goto_main(self):
        """
        进入首页
        :return: 首页
        """
        return MainPage()