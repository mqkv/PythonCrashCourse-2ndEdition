# -*- coding:utf-8 -*-
# 2022/03/30

# 五香烟熏牛肉(pastrami)卖完了
# 使用为完成练习7-8而创建的列表sandwich_orders ，并确保'pastrami' 在其中至少出现了三次。
# 在程序开头附近添加这样的代码：打印一条消息，指出熟食店的五香烟熏牛肉卖完了；
# 再使用一个while 循环将列表sandwich_orders 中的'pastrami' 都删除。确认最终的列表finished_sandwiches 中不包含'pastrami'

sandwich_orders = ['tuna', 'Ham and Cheese', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print("熟食店的五香烟熏牛肉卖完啦!")

while sandwich_orders:
    make_sandwiches = sandwich_orders.pop()
    if make_sandwiches == "pastrami":
        continue
    else:
        print("I made your " + make_sandwiches + ' sandwich.')
        finished_sandwiches.append(make_sandwiches)

print("\nAll sandwiches are made:")
for sandwich in finished_sandwiches:
    print(sandwich.title() + " Sandwich.")
