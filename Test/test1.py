# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 8:31
# @Author  : Pyh
# @Email   : 664254320@qq.com
# @File    : test1.py
# @Software: PyCharm Community Edition
# @Description : 简单测试基本语法
from operator import add, sub

import re
import random
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
    a = 3
    b = 2
    print(str(a) + '*' + str(b) + '=' + str(a * b))

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

def demo_random():
    for i in range(0,10):
        print(random.randint(0, 100))
    print((int)(random.random()*100))
    print(random.choice(range(0, 1000, 9)))  # 从某个范围内抽
    print(random.sample(range(0, 1000, 8), 5))  # 抽取多少个样本
    lista = [1,2,3,4,5]
    random.shuffle(lista)  # 随机打乱
    print(lista)

# 正则表达式
def demo_regex():
    str = 'abc123def12gh15'
    p1 = re.compile('[\d]+')  # 一个及以上数字匹配
    p2 = re.compile('[\d]')   # 单个数字
    print(p1.findall(str))
    print(p2.findall(str))

    str1 = 'a@163.com, b@google.com, c@qq.com, d@qq.com, e@163.com, 45465123,213sazxas, @daszxc.sdq, 123@qq.com'
    p3 = re.compile('[\w]+@[163|qq|google]+\.com')
    print(p3.findall(str1))

    str2 = '<html><h>title</h><body>content</body></html>'
    p4 = re.compile('<h>[^<]+</h>')
    print(p4.findall(str2))
    p5 = re.compile('<h>[^<]+</h><body>[^<]+</body>')
    print(p5.findall(str2))

if __name__ == '__main__':
    # qiushibaike()
    # demo_string()
    # demo_list()
    # demo_dict()
    # demo_set()
    # demo_obj()
    # demo_random()
    demo_regex()

