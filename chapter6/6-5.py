# -*- coding:utf-8 -*-
# 2022/03/31

# 河流
# 创建一个字典，在其中存储三条大河流及其流经的国家。其中一个键—值对可能是'nile': 'egypt' 
# 使用循环为每条河流打印一条消息，如“The Nileruns throughEgypt.”
# 使用循环将该字典中每条河流的名字都打印出来
# 使用循环将该字典包含的每个国家的名字都打印出来


dicts = {'huanghe': 'zhongguo', 'changjiang': 'zhongguo', 'nile': 'egypt'}


for key, value in dicts.items():
    print("The " + key.title() + " runs through " + value.title() + ".")


for key in dicts.keys():
    print(key)
   # print("The " + key.title() + " runs through " + dicts[key].title() + ".")


for value in dicts.values():
    print(value)

