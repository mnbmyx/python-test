# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年06月01日 19:17
"""

"""
页面元素对象层
"""

from selenium.webdriver.common.by import By

"""
登录页面元素配置信息
"""
# 登录按钮链接
dl_login_link = By.XPATH,'//*[@id="commonTopbar_login"]/a[1]'
# 账户名输入框
dl_username_input = By.ID,'mask_body_item_username'
# 密码输入框
dl_password_input = By.ID,'mask_body_item_newpassword'
# 登录按钮
dl_login_btn = By.ID,'mask_body_item_login'
# 登录成功后的用户名
dl_username = By.XPATH,'//*[@id="commonTopbar_login"]/span'

"""
登记简历页面元素配置信息
"""
# 招聘链接
jianli_zhaoping_link = By.XPATH,'//*[@id="zpNav"]/a'
# 登记简历按钮
jianli_dengji_btn = By.XPATH,'/html/body/div[2]/div/div[2]/a[2]'
# # 职业类别按钮
jianli_zhiye_btn = By.XPATH,'//*[@id="job"]/div[2]'
# # 计算机类别按钮
jianli_jisuanji_btn = By.XPATH,'/html/body/div[2]/form/div[1]/div[2]/ul/li[1]/div[2]/div[2]/ul/li[6]/ul/li[1]'
# 测试工程师
jianli_test_work = By.XPATH,'/html/body/div[2]/form/div[1]/div[2]/ul/li[1]/div[2]/div[2]/ul/li[6]/ul/li[1]/ul/li[9]/i'
# 关闭职业类别选择
jianli_cloes_btn = By.XPATH,'//*[@id="search-close"]'
# # 工作地点按钮
jianli_work_btn = By.XPATH,'//*[@id="address-first-text"]'
# 省份按钮
jianli_sheng_btn = By.XPATH,'//*[@id="address"]/div[4]/div[2]/div/ul/li[2]/a'
# 城市按钮
jianli_chengshi_btn = By.XPATH,'//*[@id="address"]/div[4]/div/ul/li[4]/a'
# 区按钮
jianli_qu_btn = By.XPATH,'//*[@id="address"]/div[4]/div/ul/li[4]/a'
# 期望薪资按钮
jianli_money_btn = By.XPATH,'/html/body/div[2]/form/div[1]/div[2]/ul/li[3]/div/div[1]'
# 工资
jianli_money = By.XPATH,'/html/body/div[2]/form/div[1]/div[2]/ul/li[3]/div/div[3]/ul/li[6]/a'
# 姓名
jianli_name = By.ID,'txtUserName'
# 年份按钮
jianli_year_btn = By.XPATH,'/html/body/div[2]/form/div[2]/div[2]/ul/li[3]/div/div[1]'
# 出生年份
jianli_year = By.XPATH,'//*[@id="yearList"]/ul/li[6]/a'
# 工作年限按钮
jianli_work_years_btn = By.XPATH,'/html/body/div[2]/form/div[2]/div[2]/ul/li[4]/div/div[1]'
# 工作年限
jianli_work_years = By.XPATH,'/html/body/div[2]/form/div[2]/div[2]/ul/li[4]/div/div[3]/ul/li[2]/a'
# 最高学历按钮
jianli_hight_level_btn = By.XPATH,'/html/body/div[2]/form/div[2]/div[2]/ul/li[5]/div/div[1]'
# 最高学历
jianli_hight_level = By.XPATH,'/html/body/div[2]/form/div[2]/div[2]/ul/li[5]/div/div[3]/ul/li[5]/a'
# 保存简历
jianli_save_jianli = By.XPATH,'//*[@id="submit"]'
# 保存简历后的主页姓名信息
jianli_name_info = By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/h2'


"""
生活会员服务推广币加入购物车页面元素配置信息
"""
# 二手市场链接
shopping_market_link = By.XPATH,'//*[@id="esNav"]/a'
# 商家入驻链接
shopping_business_link = By.XPATH,'//*[@id="header"]/div/a[2]/img'
# 我要推广链接
shopping_tuiguang_link = By.XPATH,'/html/body/div[4]/a'
# 加入购物车链接
shopping_cart_link = By.XPATH,'//*[@id="popularizeMoneyBuy"]/div[2]'
# 选择1000 规格
shopping_thousand_btn = By.XPATH,'//*[@id="popularizeListMask"]/div/div[3]/label[1]/div/span[2]'
# 加号按钮
shopping_add_btn = By.XPATH,'//*[@id="popularizeListMask"]/div/div[3]/label[2]/div/span[2]'
# 加入购物车按钮
shopping_cart_btn = By.XPATH,'//*[@id="popularizeMaskBuy"]/button[1]'
# 加入购物车后的黄页推广币
shopping_tuiguangbi_info = By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[1]/ul/li/div/p[1]'


"""
车辆评估页面元素配置信息
"""
# 二手车链接
cartpg_duble_cart_link = By.XPATH,'//*[@id="escNav"]/a'
# 品牌输入框
cartpg_pinpai_btn = By.XPATH,'//*[@id="pinpai"]'
# 柯尼塞格按钮
cartpg_kenisaige_btn = By.XPATH,'//*[@id="pinPaiUl"]/li[188]'
# 柯尼塞格CCX按钮
cartpg_kenisaige_ccx_btn = By.XPATH,'//*[@id="cheXiUl"]/li[4]'
# 柯尼塞格CCX标准型
cartpg_kenisaige_ccx_bzx_btn = By.XPATH,'//*[@id="cheXingUl"]/li[3]/span'
# 上牌时间
cartpg_shangpai_time = By.XPATH,'//*[@id="list"]/ul/li[4]/div/div/ul/li/div/p[2]'
# 2023年
cartpg_2023_year = By.XPATH,'//*[@id="yearList"]/li[1]'
# 3 月份
cartpg_3_month = By.XPATH,'//*[@id="monthList"]/li[4]'
# 行驶里程
cartpg_load_km = By.XPATH,'//*[@id="xslicheng"]'
# 所在地区
cartpg_home_btn = By.XPATH,'//*[@id="area"]'
# 上海
cartpg_shanghai_btn = By.XPATH,'//*[@id="provinceList"]/li[2]'
# 手机号码
cartpg_phone_input = By.XPATH,'//*[@id="phone"]'
# 马上评估按钮
cartpg_pinggu_btn = By.XPATH,'//*[@id="operate"]'
# 评估返回信息
cartpg_cart_info = By.XPATH,'/html/body/div[4]/div[5]/div/div[3]/a[1]'

"""
搜索新车页面元素配置信息
"""
# 新车链接
sousuo_new_cart_link = By.XPATH,'//*[@id="nav"]/li[6]/a'
# 搜索输入框
sousuo_input = By.XPATH,'//*[@id="search_keyword"]'
# 搜索第二个
sousuo_btn = By.XPATH,'//*[@id="searcbtn"]'
# 搜索成功提示信息
sousuo_info = By.XPATH,'/html/body/div[5]/div[1]/div[1]/div/a'