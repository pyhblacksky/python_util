# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 20:30
# @Author  : Pyh
# @Email   : 664254320@qq.com
# @File    : test2.py
# @Software: PyCharm Community Edition
# @Description : 测试爬虫

'''
爬虫
第一步：解析网页，定位到想要的信息
第二步：

'''

from pyquery import PyQuery

if __name__ == '__main__':
    q = PyQuery(open('v2ex.html', encoding='utf8').read())
    print(q('title').html())  # 找到标签为title的元素


    # CSS选择器
    # > 表示下一层一定要是所写的   ' '空格表示 只要下面有一层包含即可
    # > 该符号表示子元素是a     下面表达式表示：inner下的元素a，两层
    for each in q('div.inner>a').items():
        if each.attr.href.find('tab') > 0:
            print(each.attr.href)

    #   #id   表示<p id=“id”>   即#Tabs表示寻找id为Tabs的项
    for each in q('#Tabs>a').items():
        print(2, each.attr.href)

    # class为cell的，下标签为a，a的开头为go开头的元素
    for each in q('.cell>a[href^="/go/"]').items():
        print(3, each.attr.href)

    # 使用空格
    for each in q('.cell a[href^="/go/"]').items():
        print(4, each.attr.href)

    # 爬取标题    下列表达式的含义：<span class="item_title"><a   下列的项
    for each in q('span.item_title>a').items():
        print(5, each.html())