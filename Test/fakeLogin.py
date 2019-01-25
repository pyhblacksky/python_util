# -*- coding: utf-8 -*-
# @Time    : 2019/1/25 9:04
# @Author  : Pyh
# @Email   : 664254320@qq.com
# @File    : fakeLogin.py
# @Software: PyCharm Community Edition
# @Description : 模拟登陆，以自己的网站为例子

import requests

if __name__ == '__main__':
    payload = {'username': 'xx', 'password': 'xx'}
    s = requests.session()
    s.get('http://127.0.0.1:8080/user/14')
    #r = s.post('http://127.0.0.1:8080/reglogin', data=payload)   # 模拟请求登录的方式
    print(s.get('http://127.0.0.1:8080/user/14', cookies={"ticket": "332cd24f246c40a6aaf2b6e9adc2bdd5"}).content)  # 使用cookie