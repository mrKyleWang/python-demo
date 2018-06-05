# -*- coding:utf-8 -*-
# @TIME     : 20180605 12:11
# @Author   : KyleWang
# @File     : advance02.py

# 字典
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

dict1 = {'abc': 456}
dict2 = {'abc': 123, 5: 37}

dict = {'name': 'Zara', 'age': 7, 'class': 'First'}
print("dict['name']", dict['name'])
print("dict['age']", dict['age'])
print(dict)
dict['class'] = "Second"
print(dict)

del dict['name']
dict.clear()
del dict


