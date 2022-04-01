# -*- coding:utf-8 -*-
# 2022/03/29

# 比萨配料
# 编写一个循环，提示用户输入一系列的比萨配料，并在用户输入'quit' 时结束循环。每当用户输入一种配料后，都打印一条消息，说我们会在比萨
# 中添加这种配料。

is_active = True
while is_active:
    msg = input("请输入您需要的比萨配料(输入'quit'后会退出程序)：")

    if msg == 'quit':
        is_active = False
    else:
        print("您选择的比萨配料是：" + msg + "。")
