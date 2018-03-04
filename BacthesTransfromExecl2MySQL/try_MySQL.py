# -*- coding:utf-8 -*-
'''
author: Barnett
'''
import pandas as pd
import openpyxl
import os
import re

curdir = os.listdir(r'C:\Users\h\Desktop\Python\Selenium_test\Xinlang_stock_spider')
print('log.txt' in curdir)

os.chdir(r'C:\Users\h\Desktop\Python\Selenium_test\Xinlang_stock_spider')

filter_condition = open('log.txt', 'r').readlines()
print(filter_condition)

for each in curdir:
    print((each+'\n') in filter_condition, end=' ')

