# -*- coding: utf-8 -*-
# 2022/03/25

# 用户的专辑
# 在为完成练习8-7编写的程序中，编写一个while 循环，让用户输入一个专辑的歌手和名称。
# 获取这些信息后，使用它们来调用函数make_album() ，并将创建的字典打印出来。在这个while 循环中，务必要提供退出途径。

def make_album(name, album):
    person = {"name": name, "album": album}
    return person


while True:
    print("(Enter 'q' or 'Q' at any time to quit)")
    name = input("Your favorite singer is: ")
    if name == 'q' or name == 'Q':
        break
    album = input("Please enter one of his/her albums: ")
    if album == 'q' or album == 'Q':
        break

    info = make_album(name, album)
    print(info)
