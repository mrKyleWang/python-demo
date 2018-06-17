# -*- coding:utf-8 -*-
# @TIME     : 20180605 12:11
# @Author   : KyleWang
# @File     : advance02.py

import time
import datetime

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

# 日期和时间
localtime = time.localtime(time.time())
print("local current time:", localtime)

print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'))
print(str(datetime.datetime.now())[:19])

expire_time = "2018-06-17 15:37:36"
d = datetime.datetime.strptime(expire_time, '%Y-%m-%d %H:%M:%S')
print(d)

oneday = datetime.timedelta(days=1)
today = datetime.date.today()
yesterday = datetime.date.today() - oneday
tomorrow = datetime.date.today() + oneday
print(oneday, today, yesterday, tomorrow)

time_sec_float = time.mktime(d.timetuple())
print(time_sec_float)

time_sec_float = time.mktime(today.timetuple())
print(time_sec_float)

print(time.time())
