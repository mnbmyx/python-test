# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年06月01日 20:02
"""

import pytest
import base
from page import GetDriver
from page.page import Page
from common.url_yml import url_yml
from common.data_csv import data_csv

url = url_yml('../config/url.yml','58tc','url')#58同城网址
information = data_csv('../data/data.csv')#登录测试的账号、密码和提示信息
@pytest.mark.parametrize(('username','password','info'),information)
# 登录测试模块
class TestLogin():
    @classmethod
    def setup_class(cls):
        # 打开58同城页面
        cls.driver = GetDriver.get_driver(url)
        cls.tc = Page(cls.driver)
        # 点击登录链接
        cls.tc.base_click(base.dl_login_link)

    @classmethod
    def teardown_class(cls):
        # 关闭浏览器
        GetDriver.quit_driver()

    @pytest.mark.L1
    def test_login(self,username,password,info):
        # 调用登录方法
        self.tc.page_login(username,password)
        # 断言
        if info == information[-1][2]:
            print('登录成功')
            assert self.tc.base_info(base.dl_username).text == info
        else:
            print('检查用户名或密码是否正确')


if __name__ == '__main__':
    pytest.main(['-s','test_01_login.py'])