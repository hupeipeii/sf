#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 09:49:04 2017

@author: hupeipei8090
"""

def is_leaf_years(year):    
    if year%400==0 or  year%4==0 and year%100!=0:
        True
    else:
        False
        
def get_num_of_days_in_month(year,month):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif is_leaf_years(year):
        return 29
    else:
        return 28
    
def get_total_num_of_days(year,month):
    days=0
    for year in range(1800,year):
        if is_leaf_years(year):
            days+=366
        else:
            days+=365
    for month in range(1,month):
        days+=get_num_of_days_in_month(year,month)
    return days

def get_start_day(year,month):
    return 3+get_total_num_of_days(year,month)%7

month_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',  
              7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
def get_month_name(month):
        print month_dict[month]#字典调用
        
def print_month_title(year,month):
    print"    %s    %s"%(year,get_month_name(month))
    print"-"*35
    print"  Sun  Mon  Tue  Wed  Thu  Fri  Sat  "
    
def print_month_body(year,month):
        #''''' 
    #打印日历正文 
    #格式说明：空两个空格，每天的长度为5 
    #需要注意的是print加逗号会多一个空格 
    #'''  
    i = get_start_day(year, month)  
    if i != 7:  
        print ' ', # 打印行首的两个空格  
        print '    ' * i,   # 从星期几开始则空i几个空格  
    for j in range(1, get_num_of_days_in_month(year, month)+1):  
        print '%4d' %j, # 宽度控制，4+1=5,j这个数占4个字符。
        i += 1 
        if i % 7 == 0:  # i用于计数和换行  
            print ' '   # 每换行一次行首继续空格 
            
if __name__=='__main__':
    year = int(raw_input('Please input target year:') )
    month = int(raw_input('Please input target month:') )
    print_month_title(year, month)  
    print_month_body(year, month)
    

