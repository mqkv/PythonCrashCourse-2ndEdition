# -*- coding: utf-8 -*-
# 2022/03/29

# 10的整数倍
# 让用户输入一个数字，并指出这个数字是否是10的整数倍。

num = int(input("请输入正整数："))

if num % 10 == 0:
    print("%d是10的整数倍！" % num)
else:
    print("%d不是10的整数倍！" % num)
