import sqlite3
# -*- coding: utf-8 -*-
conn = sqlite3.connect('test.db')

cursor = conn.cursor()

#÷¥––≤È—Ø”Ôæ‰
cursor.execute('select * from user where id=?', '2')
#cursor.execute('select * from user')

value = cursor.fetchall()

print value
cursor.close()
conn.close()
