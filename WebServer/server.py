# -*- coding: utf-8 -*-

# 导入wsgiref中的make_server模块
from wsgiref.simple_server import make_server

# 导入自己编写的application模块
from helloclient import application

# 创建一个服务器，ip地址为空，端口为8000，处理函数时application
httpd = make_server('', 8000, application)

print "Serving HTTP on port 8000..."

# 开始监听http请求
httpd.serve_forever()