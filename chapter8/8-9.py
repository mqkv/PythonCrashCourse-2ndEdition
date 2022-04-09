# -*- coding: utf-8 -*-
# 2022/03/25

# 魔术师
# 创建一个包含魔术师名字的列表，并将其传递给一个名为show_magicians() 的函数，这个函数打印列表中每个魔术师的名字。

def show_magicians(names):
    for name in names:
        print(name)


magic_names = ["xiaoming", "xiaohong"]
show_magicians(magic_names)
