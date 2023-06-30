# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年06月01日 19:33
"""

import csv

'''
返回嵌套列表，类似：[['admin', 'error', '0'], ['admin', 'rootroot', '1']]
'''
def data_csv(file):
    mylist = []
    with open(file, 'r', encoding='utf8') as f:
        data = csv.reader(f)
        for i in data:
            mylist.append(i)
        del mylist[0] # 删除标题那行数据
        return mylist


if __name__ == '__main__':
    data = data_csv('../data/data.csv')
    print(data)