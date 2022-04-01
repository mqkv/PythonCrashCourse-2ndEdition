# -*- coding:utf-8 -*-
# 2022/03/30

# 梦想的度假胜地
# 编写一个程序，调查用户梦想的度假胜地。
# 使用类似于“If you could visit one place in the world, where would you go?”的提示，并编写一个打印调查结果的代码块。

info = {}
is_active = True

while is_active:
    name = input("what is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")
    info[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        is_active = False

print("\n--- Poll Results ---")
for name, response in info.items():
    print(name + " would like to climb " + response + ".")
