# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 15:06
# @Author  : 饭盆里
# @File    : test_cookie.py
# @Software: PyCharm
# @desc    :
import shelve
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class  Test():
    def setup(self):
        options = Options()
        # 和浏览器打开的调试端口进行通信
        # 浏览器要使用 --remote-debugging-port=9222 开启调试，
        # 由于我环境变量设置了变量，alias driver_debugging='/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222'
        # 所以可以直接：driver_debugging
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=options)
        # self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown(self):

        self.driver.quit()

    @pytest.mark.skip
    def test_baidu(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element(By.ID,'kw').send_keys('hi')
        self.driver.find_element(By.XPATH,'//*[@id="su"]').click()
        sleep(5)

    def test_wework(self):
        self.driver.get("https://work.weixin.qq.com/")
        # 获取 cookies
        # print(self.driver.get_cookies())
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850531850742'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'PI81GkMu8osptnJ46fIu-UWJvR3o8_ViBwX5USscimOQRrHRyNdnruNfbjNLbSU2p3AvksJoKJc6tACT8EJXxe89v6xc0h_5FZUIikMzapf27LnrSjJkfUxRoHkefiaUAoTRgR0a_QBWoj8mEOELID9xl2Etr5gBTKAqCPdJzz3aBZC5b7iKufwcWtgb54qvKyXIK4J5zMnAy8DBzvrRb2pUE_hYYbkptzwyfk5rR7xiK01F3fqXjJwA2QIuI5R_e35ZDA10FFYBxpMtVyvbJA'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850531850742'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325138147142'}, {'domain': '.work.weixin.qq.com', 'expiry': 1626742501, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1594975399,1594979354,1594979612,1595206501'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '8752271993'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a3834163'}, {'domain': 'work.weixin.qq.com', 'expiry': 1595238009, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': 'oj731e'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1595206501'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '26225621643276726'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'lvWc6ImOzsx44Nw-2SegyMqIl7_H2EiVGhYcto58RPhmIx18vxT56MuBeZCy7aHo'}, {'domain': '.work.weixin.qq.com', 'expiry': 1595238009, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1658051906, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1583622381.1594901080'}, {'domain': '.work.weixin.qq.com', 'expiry': 1597798500, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}]

        # # 创建或者打开一个数据库
        db = shelve.open("cookies")
        # # 将数据存储到 shelve 中
        db["cookies"] = cookies
        #
        # # 取出数据
        cookies = db["cookies"]

        #把cookie 中的时间戳去除"expiry",然后加入到浏览器的cookies中
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            # 把字典加入到 driver 的 cookie 中
            self.driver.add_cookie(cookie)

        sleep(2)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        # sleep(4)
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        # db.close()

