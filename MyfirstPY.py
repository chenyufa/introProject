#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'cyf'

print("hello py", 'I common')


sum_num = 0
for count in [100, 200, 300, 400, 1000]:
    sum_num += count
# print(sum_num)

n = 0
while n <= 100:
    if n > 10:  # 当n = 11时，条件满足，执行break语句
        break  # break语句会结束当前循环
# print(n)
    n = n + 1
print('END!'+str(2)+'!')

list_key = {1: 'a', 2: 'b', '2': 11}
# print(list_key.get('-1', 99))
