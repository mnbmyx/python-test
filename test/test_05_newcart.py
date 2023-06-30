# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年06月02日 16:03
"""


import pytest
import base
from page import GetOptions
from page.page import Page
from common.url_yml import url_yml


url = url_yml('../config/url.yml','58tc','url')#58同城网址
cookice = '../data/cookie.json'#登录的cookice文件
service = url_yml('../config/url.yml', 'Service', 'service')#浏览器驱动
cartname = url_yml('../config/url.yml','new_cart','cartname')#搜索的车名
info = url_yml('../config/url.yml','new_cart','info')#搜索成功返回信息
# 测试搜索新车模块
class TestNewcart():
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
    def test_new_cart(self):
        # 调用搜索新车方法
        self.cart.page_sousuo_new_cart(cartname)
        # 断言
        self.cart.base_assertion(base.sousuo_info,info)

if __name__ == '__main__':
    pytest.main(['-s','test_05_newcart.py'])