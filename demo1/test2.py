# -*- coding:utf-8 -*-
# @TIME     : 20180520 14:37
# @Author   : KyleWang
# @File     : test2.py

# 变量类型及转换
age = 10
name = "kyle"
price = 15.3
print("age变量的类型是%s" % type(age))
print("name变量的类型是%s" % type(name))
print("price变量的类型是%s" % type(price))
score = "98"
print("score变量的类型是%s" % type(score))
print("score变量类型转换后的类型是%s" % type(int(score)))

# 条件判断语句if else
age = int(input("请输入你的年龄:"))
if age > 18:
    print("已成年")
else:
    print("未成年")
print("判断结束")
