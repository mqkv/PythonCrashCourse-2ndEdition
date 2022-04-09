# -*- coding: utf-8 -*-
# 2022/03/28

# 打印模型
# 将示例print_models.py中的函数放在另一个名为printing_functions.py的文件中；
# 在print_models.py的开头编写一条import 语句，并修改这个文件以使用导入的函数。

import printing_functions as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)
