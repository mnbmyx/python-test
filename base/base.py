# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年06月01日 19:28
"""
import json
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from common.get_log import GetLogger

# 初始化日志对象
log = GetLogger.get_logger(fliename='../log/test_tc.log')

"""
页面元素操作层
"""
class Base(object):
    # 初始化
    def __init__(self, driver):
        log.info(f'初始化driver：{driver}')
        self.driver = driver

    # 查找元素方法
    def base_get_element(self, loc, time=30, poll=0.5):
        """
        :param loc: 元素的配置信息，格式为元组
        :param time: 默认超时时间为30秒
        :param poll: 访问频率，默认0.5秒查找一次元素
        :return:返回查找到的元素
        """
        log.info(f'正在查找元素{loc}')
        try:
            element = WebDriverWait(self.driver,
                                    timeout=time,
                                    poll_frequency=poll).until(lambda x: x.find_element(*loc))
            return element
        except Exception as e:
            raise e

     # 截图（使用时间戳命名）方法
    def base_get_img(self):
        log.info('正在截图')
        time.sleep(1)
        self.driver.get_screenshot_as_file(f'../img/{time.strftime("%Y_%m_%d %H_%M_%S")}.png')
        time.sleep(1)

    # 点击方法
    def base_click(self,loc):
        time.sleep(1)
        self.base_get_element(loc).click()
        log.info(f'正在点击元素：{loc}')

    # 输入方法
    def base_input(self,loc,key):
        time.sleep(1)
        # 定位元素
        ele = self.base_get_element(loc)
        # 进行清空操作
        ele.clear()
        log.info(f'正在给元素：{loc}进行清空')
        # 进行输入内容
        ele.send_keys(key)
        log.info(f'正在给元素{loc}输入内容：{key}')

    # 获取定位内容
    def base_info(self,loc):
        log.info(f'正在定位元素{loc}')
        return self.base_get_element(loc)

    # 切换窗口方法
    def base_switch_windows(self,index):
        handles = self.driver.window_handles
        log.info('正在切换窗口')
        self.driver.switch_to.window(handles[index])

    # 断言封装
    def base_assertion(self,loc,info):
        if info == self.base_info(loc).text:
            print('ok!')
        else:
            print('error!')

# cookice登录方法
class BaseCookie:
    def __init__(self,path):
        self.path = path

    def base_cookice(self):
        """
        Cookies读取方法
        :param encoding: 文件编码,默认utf-8
        """
        log.info('正在使用cookice登录...')
        if os.path.isfile(self.path):
            with open(self.path, "r", encoding='utf-8') as f:
                cookice = json.load(f)
            return cookice