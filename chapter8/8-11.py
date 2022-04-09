# -*- coding: utf-8 -*-
# 2022/03/25

# 不变的魔术师
# 修改你为完成练习8-10而编写的程序，在调用函数make_great() 时，向它传递魔术师列表的副本。
# 由于不想修改原始列表，请返回修改后的列表，并将其存储到另一个列表中。
# 分别使用这两个列表来调用show_magicians() ，确认一个列表包含的是原来的魔术师名字，而另一个列表包含的是添加了字样“the Great”的魔术师名字。

def make_great(magic_names, great_magic_names):
    while magic_names:
        great_magic_name = magic_names.pop()
        great_magic_names.append("the Great " + great_magic_name.title())


def show_magicians(names):
    for name in names:
        print(name)


magic_names = ["xiaoming", "xiaohong"]
great_magic_names = []

# 传递 magic_name 副本
make_great(magic_names[:], great_magic_names)

# 打印原始魔术师列表
show_magicians(magic_names)
# 打印修改后的魔术师列表
show_magicians(great_magic_names)
