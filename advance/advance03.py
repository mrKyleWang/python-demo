# -*- coding:utf-8 -*-
# @TIME     : 20180617 16:34
# @Author   : KyleWang
# @File     : advance03.py

from functools import reduce

lst = [1, 2, 1, 1, 2, 3, 4, 2, 1, 2, 5, 6, 1, 2]


def statistics(lst):
    dic = {}
    for k in lst:
        if not k in dic:
            dic[k] = 1
        else:
            dic[k] += 1
    return dic


print(statistics(lst))


def statistics2(lst):
    m = set(lst)
    dic = {}
    for x in m:
        dic[x] = lst.count(x)
    return dic


print(statistics2(lst))


def statistics3(dic, k):
    if not k in dic:
        dic[k] = 1
    else:
        dic[k] += 1
    return dic
