import sqlite3
# -*- coding: utf-8 -*-
#连接目标数据库，此数据库就是在本地的一个文件，如果没有会自动创建一个
conn = sqlite3.connect('test.db')

#创建游标cursor，获取后即可对它执行SQL语句
cursor = conn.cursor()	

#执行一条SQL语句，创建user表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

#继续执行SQL语句，插入一条记录
cursor.execute('insert into user (id, name) values(\'1\', \'firstName\')')
cursor.execute('insert into user (id, name) values(\'2\', \'secondName\')')
#通过rowcount获取插入的行号
cursor.rowcount

#关闭cursor
cursor.close()

#提交事务
conn.commit()

#关闭Connection
conn.close()