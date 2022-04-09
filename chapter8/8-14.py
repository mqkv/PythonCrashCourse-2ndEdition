# -*- coding: utf-8 -*-
# 2022/03/25

# 汽车
# 编写一个函数，将一辆汽车的信息存储在一个字典中。
# 这个函数总是接受制造商和型号，还接受任意数量的关键字实参。
# 这样调用这个函数：提供必不可少的信息，以及两个名称—值对，如颜色和选装配件。

def make_car(mfrs, model, **other_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    car_info = {}
    car_info['mfrs'] = mfrs
    car_info['model'] = model
    for key, value in other_info.items():
        car_info[key] = value
    return car_info


car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)
