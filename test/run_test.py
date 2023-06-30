# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年06月02日 16:43
"""
# 导包
import pytest
# 运行测试文件并生成测试报告
pytest.main(['-s','test_01_login.py','--alluredir','../report/'])
pytest.main(['-s','test_02_jianli.py','--alluredir','../report/'])
pytest.main(['-s','test_03_shopping.py','--alluredir','../report/'])
pytest.main(['-s','test_04_pinggu.py','--alluredir','../report/'])
pytest.main(['-s','test_05_newcart.py','--alluredir','../report/'])
