# -*- coding: utf-8 -*-
# 2022/03/25

# 了不起的魔术师
# 在你为完成练习8-9而编写的程序中，编写一个名为make_great() 的函数，对魔术师列表进行修改，在每个魔术师的名字中都加入字样“the Great”。
# 调用函数show_magicians() ，确认魔术师列表确实变了。

def make_great(magic_names, great_magic_names):
    while magic_names:
        great_magic_name = magic_names.pop()
        great_magic_names.append("the Great " + great_magic_name.title())


def show_magicians(great_magic_names):
    for great_magic_name in great_magic_names:
        print(great_magic_name)


magic_names = ["xiaoming", "xiaohong"]
great_magic_names = []

make_great(magic_names, great_magic_names)
show_magicians(great_magic_names)
