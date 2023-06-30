# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年06月02日 9:54
"""

import pytest

import base
from page import GetOptions
from page.page import Page
from common.url_yml import url_yml

url = url_yml('../config/url.yml','58tc','url')#58同城网址
cookice = '../data/cookie.json'#登录的cookice文件
service = url_yml('../config/url.yml', 'Service', 'service')#浏览器驱动
info = url_yml('../config/url.yml','shopping','info')#断言信息
# 测试生活会员服务推广币加入购物车模块
class TestShopping():
    # 初始化浏览器
    @classmethod
    def setup_class(cls):
        cls.driver = GetOptions.get_driver(url,cookice,service)
        cls.shopping = Page(cls.driver)

    # 关闭浏览器
    @classmethod
    def teardown_class(cls):
        GetOptions.quit_driver()

    @pytest.mark.L2
    def test_shopping(self):
        # 调用生活会员服务推广币加入购物车方法
        self.shopping.page_shopping_cart()
        # 断言
        self.shopping.base_assertion(base.shopping_tuiguangbi_info,info)


if __name__ == '__main__':
    pytest.main(['-s','test_03_shopping.py'])