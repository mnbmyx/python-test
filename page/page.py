# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年06月01日 19:28
"""
from time import sleep

from base.base import Base
import base

"""
页面业务场景层
"""
class Page(Base):

    # 登录模块
    def page_login(self,username,password):
        # 输入用户名
        self.base_input(base.dl_username_input,username)
        # 输入密码
        self.base_input(base.dl_password_input,password)
        # 点击登录按钮
        self.base_click(base.dl_login_btn)
        sleep(1)
        # 截屏
        self.base_get_img()

    # 登记简历模块
    def page_jianli(self,name):
        # 点击招聘链接
        self.base_click(base.jianli_zhaoping_link)
        # 切换窗口
        self.base_switch_windows(-1)
        # 点击登记简历按钮
        self.base_click(base.jianli_dengji_btn)
        # 切换窗口
        self.base_switch_windows(-1)
        # 选择职业类别
        self.base_click(base.jianli_zhiye_btn)
        self.base_click(base.jianli_jisuanji_btn)
        self.base_click(base.jianli_test_work)
        self.base_click(base.jianli_cloes_btn)
        # 选择工作地点
        self.base_click(base.jianli_work_btn)
        self.base_click(base.jianli_sheng_btn)
        self.base_click(base.jianli_chengshi_btn)
        self.base_click(base.jianli_qu_btn)
        # 选择工资
        self.base_click(base.jianli_money_btn)
        self.base_click(base.jianli_money)
        # 输入姓名
        self.base_input(base.jianli_name,name)
        # 选择出生年份
        self.base_click(base.jianli_year_btn)
        self.base_click(base.jianli_year)
        # 选择工作年限
        self.base_click(base.jianli_work_years_btn)
        self.base_click(base.jianli_work_years)
        # 选择最高学历
        self.base_click(base.jianli_hight_level_btn)
        self.base_click(base.jianli_hight_level)
        # 截屏
        self.base_get_img()
        # 点击保存简历按钮
        self.base_click(base.jianli_save_jianli)
        sleep(1)
        # 截屏
        self.base_get_img()

    # 生活会员服务推广币加入购物车模块
    def page_shopping_cart(self):
        # 点击二手市场链接
        self.base_click(base.shopping_market_link)
        # 切换窗口
        self.base_switch_windows(-1)
        # 点击商家入驻链接
        self.base_click(base.shopping_business_link)
        # 切换窗口
        self.base_switch_windows(-1)
        # 点击我要推广链接
        self.base_click(base.shopping_tuiguang_link)
        # 切换窗口
        self.base_switch_windows(-1)
        # 点击加入购物车链接
        self.base_click(base.shopping_cart_link)
        # 选择1000 规格
        self.base_click(base.shopping_thousand_btn)
        # 点击加号添加数量
        self.base_click(base.shopping_add_btn)
        sleep(1)
        # 截屏
        self.base_get_img()
        # 点击加入购物车按钮
        self.base_click(base.shopping_cart_btn)

    # 车辆评估模块
    def page_cart_pinggu(self,load,phone):
        # 点击二手车链接
        self.base_click(base.cartpg_duble_cart_link)
        # 切换窗口
        self.base_switch_windows(-1)
        # 点击品牌框
        self.base_click(base.cartpg_pinpai_btn)
        # 点击柯尼塞格
        self.base_click(base.cartpg_kenisaige_btn)
        # 点击柯尼塞格CCX
        self.base_click(base.cartpg_kenisaige_ccx_btn)
        # 点击CCX标准型
        self.base_click(base.cartpg_kenisaige_ccx_bzx_btn)
        # 点击上牌时间
        self.base_click(base.cartpg_shangpai_time)
        # 点击2023年
        self.base_click(base.cartpg_2023_year)
        # 点击3 月份
        self.base_click(base.cartpg_3_month)
        # 输入行驶里程
        self.base_input(base.cartpg_load_km,load)
        # 点击所在地区
        self.base_click(base.cartpg_home_btn)
        # 点击上海
        self.base_click(base.cartpg_shanghai_btn)
        # 输入电话号码
        self.base_input(base.cartpg_phone_input,phone)
        # 截屏
        self.base_get_img()
        # 点击评估按钮
        self.base_click(base.cartpg_pinggu_btn)
        sleep(1)
        # 切换窗口
        self.base_switch_windows(-1)
        sleep(1)
        # 截屏
        self.base_get_img()

    # 搜索新车模块
    def page_sousuo_new_cart(self,cartname):
        # 点击新车链接
        self.base_click(base.sousuo_new_cart_link)
        # 切换窗口
        self.base_switch_windows(-1)
        # 搜索框输入车辆
        self.base_input(base.sousuo_input,cartname)
        sleep(1)
        # 截屏
        self.base_get_img()
        # 点击搜索按钮
        self.base_click(base.sousuo_btn)
        sleep(1)
        # 切换窗口
        self.base_switch_windows(-1)
        sleep(1)
        # 截屏
        self.base_get_img()