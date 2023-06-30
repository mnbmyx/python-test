# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年06月02日 11:07
"""

import pytest

import base
from page import GetOptions
from page.page import Page
from common.url_yml import url_yml

url = url_yml('../config/url.yml','58tc','url')#58同城网址
cookice = '../data/cookie.json'#登录的cookice文件
service = url_yml('../config/url.yml', 'Service', 'service')#浏览器驱动
load = url_yml('../config/url.yml','cart_pinggu','load')#行驶里程
phone = url_yml('../config/url.yml','cart_pinggu','phone')#电话号码
info = url_yml('../config/url.yml','cart_pinggu','info')#断言信息
# 测试车辆评估模块
class TestPinggu():
    # 初始化浏览器
    @classmethod
    def setup_class(cls):
        cls.driver = GetOptions.get_driver(url,cookice,service)
        cls.cart = Page(cls.driver)

    # 关闭浏览器
    @classmethod
    def teardown_class(cls):
        GetOptions.quit_driver()

    @pytest.mark.L2
    def test_pinggu(self):
        # 调用车辆评估方法
        self.cart.page_cart_pinggu(load,phone)
        # 断言
        self.cart.base_assertion(base.cartpg_cart_info,info)


if __name__ == '__main__':
    pytest.main(['-s','test_04_pinggu.py'])