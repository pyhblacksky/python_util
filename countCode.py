# -*- coding: utf-8 -*-
# @Time    : 2019/1/22 10:07
# @Author  : Pyh
# @Email   : 664254320@qq.com
# @File    : countCode.py
# @Software: PyCharm Community Edition
# @Description : 用于统计github上实际代码数量


# Windows下路径使用\\分隔 linux下用/
import os
import time
basedir = 'F:\\SSM\\wenda'
filelists = []
# 指定想要统计的文件类型
whitelist = ['java']
# 遍历文件, 递归遍历文件夹中的所有
def getFile(basedir):
    global filelists
    for parent, dirnames, filenames in os.walk(basedir):
        # for dirname in dirnames:
        #    getFile(os.path.join(parent,dirname)) #递归
        for filename in filenames:
            ext = filename.split('.')[-1]
            # 只统计指定的文件类型，略过一些log和cache文件
            if ext in whitelist:
                filelists.append(os.path.join(parent, filename))
# 统计一个文件的行数
def countLine(fname):
    count = 0
    for file_line in open(fname, encoding='UTF-8').readlines():   # readlines python3的方法
        if file_line != '' and file_line != '\n':  # 过滤掉空行
            count += 1
    print(fname + '----', count)
    return count
if __name__ == '__main__':
    startTime = time.clock()
    getFile(basedir)
    totalline = 0
    for filelist in filelists:
        totalline = totalline + countLine(filelist)
    print('total lines:', totalline)
    print('Done! Cost Time: %0.2f second' % (time.clock() - startTime))
