# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年06月02日 9:19
"""

import pytest
import base
from page import GetOptions
from page.page import Page
from common.url_yml import url_yml

url = url_yml('../config/url.yml','58tc','url')#58同城网址
cookice = '../data/cookie.json'#登录的cookice文件
service = url_yml('../config/url.yml', 'Service', 'service')#浏览器驱动
name = url_yml('../config/url.yml','jianli','name')#简历姓名
# 测试登记简历模块
class TestJianli():
    # 初始化浏览器
    @classmethod
    def setup_class(cls):
        cls.driver = GetOptions.get_driver(url,cookice,service)
        cls.jianli = Page(cls.driver)

    # 关闭浏览器
    @classmethod
    def teardown_class(cls):
        GetOptions.quit_driver()

    @pytest.mark.L1
    def test_jianli(self):
        # 调用登记简历方法
        self.jianli.page_jianli(name)
        # 断言
        self.jianli.base_assertion(base.jianli_name_info,name)


if __name__ == '__main__':
    pytest.main(['-s','test_02_jianli.py'])