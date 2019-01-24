# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 8:31
# @Author  : Pyh
# @Email   : 664254320@qq.com
# @File    : test1.py
# @Software: PyCharm Community Edition
# @Description : 简单测试基本语法
from operator import add, sub

import requests
from bs4 import BeautifulSoup

# 简单爬取糗事百科的文字内容
def qiushibaike():
    content = requests.get('https://www.qiushibaike.com/text/').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div', {'class': 'content'}):
        print(div.text.strip())

def demo_string():
    str1 = '\n\r hell \r\n'
    print(str1.lstrip().rstrip())
    print('-'.join({'a','b','c'}))

def demo_list():
    # 注意list是 []  而{}是set
    lista = [1,2,3]
    print(lista)
    print(dir(lista))
    listb = [7,3,1,4]

    print(listb)
    lista = lista + listb
    lista.sort()
    print(lista * 2)

    # 元组是 (), 不可变的 list
    t = (1,3,4,8)
    print(t)

def demo_dict():
    # 字典，{}表示
    dic = {1:2, 'a':'b'}
    print(dic)
    for key, value in dic.items():
        print(key,  value)

    # 用于判断key是否在dic中,py3中使用，
    if 1 in dic:
        print(dic.get(1))

    dica = {'+':add, '-':sub}   # 字典中可存放函数对象
    print(dica['+'](5,7))
    print(dica.get('-')(11,80))
    print(dica)


def demo_set():
    # 集合演示
    seta = set([1,2,3])
    setb = set([2,3,4])
    print(seta)
    print(setb)
    print(seta & setb)
    print(seta | setb)
    print(seta-setb)
    print(setb-seta)

# 类
class User:
    # 构造函数
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    # 返回代理对象的表示形式
    def __repr__(self):
        return 'Im ' + self.name + ' ' + str(self.uid)

def demo_obj():
    user1 = User('qq', 1)
    print(user1)

if __name__ == '__main__':
    # qiushibaike()
    #demo_string()
    #demo_list()
    #demo_dict()
    #demo_set()
    demo_obj()
