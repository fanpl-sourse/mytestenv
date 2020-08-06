# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 20:03
# @Author  : 饭盆里
# @File    : handle_black.py
# @Software: PyCharm
# @desc    : 黑名单处理逻辑
import logging

import allure
from appium.webdriver.common.mobileby import MobileBy

def handle_black(func):
    logging.basicConfig(level=logging.INFO)
    def wrapper(*args,**kwargs):

        # 黑名单列表
        _black_list = [
            (MobileBy.ID, 'iv_close')
        ]

        # 第一个元素：self 实例化本身  (局部引入，防止循环导入引发的异常)
        from UIautoPlatform.page.base_page import BasePage
        instance: BasePage = args[0]

        try:
            logging.info("run "+func.__name__ +'\n args: \n' + repr(args[1:])+'\n'+repr(kwargs))
            element = func(*args,**kwargs)
            return element
        except Exception as e:

            #如果出现错误，就进行截图
            instance.save_screen_short('../../result/tmp.png')
            allure.attach.file('../../result/tmp.png',
                               name='黑名单截图',
                               attachment_type=allure.attachment_type.PNG)
            logging.error('元素没有找到，进行黑名单处理')
            instance.set_implicitly_wait(1)

            # 如果没有找到，就进行黑名单处理
            # 错误次数超过最大次数，则直接报错，避免死循环
            if instance._error_times >= instance._max_error_times:
                instance._error_times = 0
                raise e

            instance._error_times += 1

            for black in _black_list:
                elements = instance.finds(*black)
                # 长度大于0，说明名中了黑名单中的一个定位元素，则将黑名单点击即可(关闭弹框或者广告)
                if len(elements) > 0:
                    elements[0].click()
                    # 关闭掉弹框后，继续查找要找的元素
                    return wrapper(*args,**kwargs)

            raise ValueError('元素不在黑名单中')

    return wrapper