import sqlite3
# -*- coding: utf-8 -*-
#����Ŀ�����ݿ⣬�����ݿ�����ڱ��ص�һ���ļ������û�л��Զ�����һ��
conn = sqlite3.connect('test.db')

#�����α�cursor����ȡ�󼴿ɶ���ִ��SQL���
cursor = conn.cursor()	

#ִ��һ��SQL��䣬����user��
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

#����ִ��SQL��䣬����һ����¼
cursor.execute('insert into user (id, name) values(\'1\', \'firstName\')')
cursor.execute('insert into user (id, name) values(\'2\', \'secondName\')')
#ͨ��rowcount��ȡ������к�
cursor.rowcount

#�ر�cursor
cursor.close()

#�ύ����
conn.commit()

#�ر�Connection
conn.close()