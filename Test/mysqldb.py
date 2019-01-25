# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 21:26
# @Author  : Pyh
# @Email   : 664254320@qq.com
# @File    : mysqldb.py
# @Software: PyCharm Community Edition
# @Description : mysqlDB：和mysql数据库连接测试  读取数据库

import MySQLdb

'''
步骤：
    1. 取链接
    2. 取数据库游标
    3. 指定sql语句
    4. db.commit()
'''

if __name__ == '__main__':
    # 连接数据库。字段分别为 : 地址、用户名、密码、数据库名、
    db = MySQLdb.connect('localhost', 'root', 'PYHmysql000000001', 'wenda', charset='utf8')

    try:
        cursor = db.cursor()  # 游标
        '''
        # 插入sql语句
        sql = 'insert into question(title, content, user_id, created_date, comment_count) ' \
              'values("xxx","xxx",1,now(),0)'
        cursor.execute(sql)  # 游标执行
        qid = cursor.lastrowid  # 返回id
        db.commit()   # 数据提交
        print(qid)
        '''

        # 读取数据
        sql = 'select * from question order by id desc limit 2'
        cursor.execute(sql)
        # 调用fetch函数取出数据
        for each in cursor.fetchall():
            for row in each:
                print(row)
            #print(each)

        db.commit()
    except Exception as e:
        print(e)
        db.rollback()  # 数据库出错，回滚
    finally:
        db.close()
