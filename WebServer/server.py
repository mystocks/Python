# -*- coding: utf-8 -*-

# ����wsgiref�е�make_serverģ��
from wsgiref.simple_server import make_server

# �����Լ���д��applicationģ��
from helloclient import application

# ����һ����������ip��ַΪ�գ��˿�Ϊ8000��������ʱapplication
httpd = make_server('', 8000, application)

print "Serving HTTP on port 8000..."

# ��ʼ����http����
httpd.serve_forever()