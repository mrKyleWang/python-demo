# -*- coding:utf-8 -*-
# @TIME     : 20180520 14:21
# @Author   : KyleWang
# @File     : test1.py

# 单行注释
'''
多行注释
'''

"""
多行注释
"""

# 定义和使用变量
score = 100
high = 180

applePrice = 3.5
weight = 7.5

money = applePrice + weight
money = money - 10

# 输入输出(注意python2和python3输入的区别)

name = input("请输入你的名字:")
print("姓名是" + name)
age = 18
print("age变量里的值是%d" % age)  # %d:整数占位符
gender = "男"
print("gender变量里的值是%s" % gender)  # %s:字符串占位符
