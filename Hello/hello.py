# -*- coding: utf-8 -*-
import HelloModule
import sys
import socket
print'hello python','Second python test'
print '100+200=',100+200
#name = raw_input('please input your name:')
#print 'Hello',name
a = 1.2e-2
print a
print "I'm adu"
print 'I\'m \"adu\"'
print '\\\t\\'
print r'\\\t\\'
print r'''line1
line2
line3'''
print 10/3
print 10.0/3
print ord('B')
print u'中文'
print len(u'我是中文字符串')
print unicode('100')
def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)
print fact(100)
HelloModule.test()
print sys.path
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print s
s.connect(('www.baidu.com', 80))
print "after s.connect"
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
print "After s.send"
buffer = []
while(True):
	b = s.recv(1024)
	if b:
		buffer.append(b)
	else:
		break
data = ''.join(buffer)
s.close
header, html = data.split('\r\n\r\n', 1)
print header
with open('sina.html', 'wb') as f:
	f.write(html)