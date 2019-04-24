#encoding : utf-8

import os
import sys

def string_practice():
    #1.将字符串的每个单词首字母大写
    name = ' this is my first "python" '
    print(name.title())
    #2.将字符串转换成大写
    print(name.upper())
    #3.将字符串全部转换成小写
    print(name.lower())
    #4.制表符\t
    print("\tpython2.0\tpython3.0")
    #5.删除字符串首末的空格
    print(name.lstrip())
    print(name.rstrip())

if __name__ == "__main__":
    string_practice()
