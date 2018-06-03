# -*- coding:utf-8 -*-
# @TIME     : 20180603 19:30
# @Author   : KyleWang
# @File     : advance01.py


# 列表
myList = ['physics', 'chemistry', 1997, 2000]
print(myList[0])

print(myList)
del myList[0]
print(myList)

print(len([1, 2, 3]))
print([1, 2, 3] + [4, 5, 6])
print(['Hi!' * 4])
print(3 in [1, 2, 3])
for x in [1, 2, 3]:
    print(x)

L = ['hello', 'Hello', 'HELLO!']
print(L[2])
print(L[-2])
print(L[1:])

# 元组
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = ()
tup3 = (50,)

print(tup1[0])

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
# 修改元组非法,可连接创建新元组
tup3 = tup1 + tup2
print(tup3)
# 元组不允许删除,可del删除整个元组
tup1 = ('physics', 'chemistry', 1997, 2000)
print(tup1)
del tup1
