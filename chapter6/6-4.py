# -*- coding:utf-8 -*-
# 2022/03/31

# 词汇表2
# 既然你知道了如何遍历字典，现在请整理你为完成练习6-3而编写的代码，将其中的一系列print 语句替换为一个遍历字典中的键和值的循环。
# 确定该循环正确无误后，再在词汇表中添加5个Python术语。当你再次运行这个程序时，这些新术语及其含义将自动包含在输出中。

dicts = {
    'int': '整数',
    'str': '字符串',
    'list': '列表',
    'tuple': '元组',
    'dict': '字典',
    'boolean': '布尔',
    'byte': '字节',
    'float': '浮点数',
    'slice': '切片',
    }


for key, value in dicts.items():
    print('key: ' + key + ' --- ' + 'value: ' + value)

