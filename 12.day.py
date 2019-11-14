#!/bin/env python3
#-*- coding:utf8 -*-
#学Python3的第十二天
#crud:增删改查,create/retrieve/update/delete
# from dbconn import Session, Departments, Employees
#
# #建立数据库的会连接
# session = Session()
#
# # #创建部门
# # hr = Departments(dep_id=1, dep_name='人事部')
# # ops = Departments(dep_id=2, dep_name='运维部')
# # dev = Departments(dep_id=3, dep_name='开发部')
# # qa = Departments(dep_id=4, dep_name=' 测试部')
# # market = Departments(dep_id=5, dep_name='市场部')
# # sales = Departments(dep_id=6, dep_name='销售部')
# #通过会话操作数据库
# #session.add_all([hr,ops,dev,qa,market,sales])
#
# #创建员工
# lb = Employees(
#     emp_id=1, emp_name='刘备',
#     birth_date='1970-1-10',
#     email='lb@csdnak.cn',
#     dep_id=1
# )
# gy = Employees(
#     emp_id=2,
#     emp_name='关羽',
#     birth_date='1971-2-8',
#     email='gy@csdnak.cn',
#     dep_id=2
# )
# zf =Employees(
#     emp_id=3,
#     emp_name='张飞',
#     birth_date='1973-4-20',
#     email='zf@qq.com',
#     dep_id=2
# )
# zy = Employees(
#     emp_id=4,
#     emp_name='赵云',
#     birth_date='1980-10-3',
#     email='zy@163.com',
#     dep_id=3
# )
# # session.add_all([lb, gy, zf, zy])
# ##################################
# # #查询时,直接查询类 返回的是类的所有实例
# # qset1 = session.query(Departments)
# # print(qset1) #qset1只是查询语句,取值时,才会真正连接数据库
# # #从qset1中取值,方法一,使用all方法返回列表
# # #result1=qset1.all()
# # #print(result1)
# # #从qset1中取值,方法二,直接遍历
# # for dep in qset1:
# #     print(dep.dep_id, dep.dep_name)
#
# # ######################################
# # #查询时 查询的是类属性 返回的是元组
# # qset2 = session.query(Employees.emp_name,Employees.email)
# # for data in qset2:
# #     print(data)
# #
# # for name,email in qset2:
# #     print(name, email)
# #
# # ######################################
# # #排序(常用)
# # qset3 = session.query(Departments).order_by(
# #     Departments.dep_id
# # )
# # for dep in qset3:
# #     print(dep.dep_id, dep.dep_name)
# #
# #######################################
# # #切片(不常用)
# # qset4 = session.query(Departments).order_by(
# #     Departments.dep_id
# # )[1:3]
# # for dep in qset4:
# #     print(dep.dep_id, dep.dep_name)
# #######################################
# # #过滤(常用)
# # qset5 = session.query(Departments).filter(
# #     Departments.dep_id < 3
# # )
# # for dep in qset5:
# #     print(dep.dep_id, dep.dep_name)
# ########################################
# # #过滤,in / not in操作符
# # qset6 = session.query(Departments).filter(
# #     Departments.dep_id.in_([3,5])
# # )
# # for dep in qset6:
# #     print(dep.dep_id, dep.dep_name)
# #
# # print('*'*30)
# #
# # qset7 = session.query(Departments).filter(
# #     ~Departments.dep_id.in_([3,5])
# # )
# # for dep in qset7:
# #     print(dep.dep_id, dep.dep_name)
# #######################################
# # #字段为空null 、不为空
# # qset8 = session.query(Departments).first(Departments.dep_name.is_(None))
# # qset9 = session.query(Departments).first(Departments.dep_name.isnot(None))
#
# #####################################
# # #在查询结果中取值,all返回所有结果的列表
# # qset10 = session.query(Employees.emp_name, Employees.email)
# # print(qset10.all())
# #######################################
# #在查询结果中取值,first返回第一项的值
# # qset11 = session.query(Employees.emp_name, Employees.email)
# # print(qset11.first())
# #####################################
# # #多表查询 query中先写Employees ,join就要填Departments
# #        query中先写join就要填Departments,join就要填Employees
# # qset12 = session.query(Employees.emp_name, Departments.dep_name).join(Departments)
# # qset13 = session.query(Departments.dep_name, Employees.emp_name).join(Employees)
# # print(qset12.all())
# # print(qset13.all())
# ####################################
# # #修改 就是重新赋值
# # qset14 = session.query(Departments).filter(
# #     Departments.dep_name == '人事部'
# # )
# # hr = qset14.first()
# # hr.dep_name = '人力资源部'
# ###################################
# # #删除
# # qset15 = session.query(Departments).filter(
# #     Departments.dep_id == 6
# # )
# # sales = qset15.first()
# # session.delete(sales)
#
#
#
# #确认
# session.commit()
#
# #关闭回话
# session.close()


# #ping.py
# import time
# import subprocess
#
# def ping(host):
#     result = subprocess.run(
#         'ping -c2  %s &> /dev/null' % host,
#         shell=True
#     )
#     if result.returncode == 0:
#         print('%s:up' % host)
#     else:
#         print('%s down' % host)
#
#
# if __name__ == '__main__':
#     ips = ('172.40.84.%s' % i for i in range(1, 255))
#     start = time.time()
#     for ip in ips:
#         ping(ip)
#     end = time.time()
#     print('耗时: ', start - end, 's')

#*********************多进程
#forking创建子进程
# import os
#
# print('starting...')
# retval = os.fork() #实现forking功能 子进程返回PID0
# if retval: #如果是1就执行
#     print('hello from parent')  #父进程干
# else:
#     print('hello from child')  #子进程
#
# print('hello from both')

#myfork.py
# import os
#
# print('starting...')
# for i in range(3):
#     retval = os.fork()
#     if not retval: #子进程打印
#         print('Hello World')
#         exit() #进程遇到exit就彻底结束 否则就会打印7遍(子进程还能产生子进程)
#
# print('Done') #只有父进程能打印

#多进程ping(节省大量时间取消三次握手)
"""
windows 不支持多进程支持多线程
各操作系统均支持多线程
"""
# #ping2.py
# import os
# import time
# import subprocess
#
# def ping(host):
#     result = subprocess.run(
#         'ping -c2  %s &> /dev/null' % host,
#         shell=True
#     )
#     if result.returncode == 0:
#         print('%s:up' % host)
#     else:
#         print('%s down' % host)
#
#
# if __name__ == '__main__':
#     ips = ('172.40.84.%s' % i for i in range(1, 255))
#     start = time.time()
#
#     for ip in ips:
#         retval = os.fork()
#         if not retval:
#             ping(ip)
#             exit()
#     end = time.time()
#
#     print('耗时:', start - end, 's')

# #制造僵尸进程
# import os
# import time
#
# retval = os.fork()
# if retval:
#     print('parent')
#     time.sleep(45)
#     print('parent done')
# else:
#     print('child')
#     time.sleep(15)
#     print('child done')
"""
终端输入watch -n1 ps a实时监测后台进程 Z+的就是僵尸老弟
kill 和kill -9是都解决不掉的
"""
#****************以下内容解决僵尸进程一般不会用到*******************
#********************毕竟写服务器的人寥寥无几**********************
#os.waitpid挂起子进程完美解决Z+僵尸进程
# import os
# import time
#
# retval = os.fork()
# if retval:
#     print('parent')
#     #挂起父进程 处理完变成僵尸进程的子进程后才继续
#     result = os.waitpid(-1,0)
#     print(result) #result是(子进程PID,0)
#     time.sleep(10)
#     print('parent done')
# else:
#     print('child')
#     time.sleep(15)
#     print('child done')
#
# #os.waitpid也可不挂起 制造僵尸进程Z+
# import os
# import time
#
# retval = os.fork()
# if retval:
#     print('parent')
#     #挂起父进程 处理完变成僵尸进程的子进程后才继续
#     result = os.waitpid(-1, 1)  #不挂起父进程
#     time.sleep(10)
#     print('parent done')
# else:
#     print('child')
#     time.sleep(15)
#     print('child done')

#多线程
"""
当程序运行时,就会出现进程,可以说,进程就是加载内存中的一系列的指令,
每个进程都拥有自己独立的运行空间.
进程还可以拥有多个线程.同意进货高层内的所有线程,共享进程的运行空间.
多线程没有僵尸进程问题
多线程的编程思路:
    主线程(类似)
"""
#mtpin.py
# import subprocess
# import threading
#
# def ping(host):
#     result = subprocess.run(
#         'ping -c2  %s &> /dev/null' % host,
#         shell=True
#     )
#     if result.returncode == 0:
#         print('%s:up' % host)
#     else:
#         print('%s down' % host)
#
#
# if __name__ == '__main__':
#     ips = ('172.40.84.%s' % i for i in range(1, 255))
#     for ip in ips:
#         #创建工作线程
#         t = threading.Thread(target=ping, args=(ip,))
#         #启动工作线程,就是调用相应的函数,函数结束,工作线程也就结束了
#         t.start() #调用target(*args)

# #调用类(用__call__)
# import subprocess
# import threading
#
# class Ping:
#     def __call__(self,host):
#         result = subprocess.run(
#             'ping -c2  %s &> /dev/null' % host,
#             shell=True
#         )
#         if result.returncode == 0:
#             print('%s:up' % host)
#         else:
#             print('%s down' % host)
#
#
# if __name__ == '__main__':
#     ips = ('172.40.84.%s' % i for i in range(1, 255))
#     for ip in ips:
#         #target是Ping的实例
#         t = threading.Thread(target=Ping(), args=(ip,))
#         t.start()

#使用__init__
# import subprocess
# import threading
#
# class Ping:
#     def __init__(self,host):
#         self.host = host
#
#     def __call__(self):
#         result = subprocess.run(
#             'ping -c2 %s &> /dev/null' % self.host,shell=True
#         )
#         if result.returncode == 0:
#             print('%s:up' % self.host)
#         else:
#             print('%sdown' % self.host)
#
#
# if __name__ == '__main__':
#     ips = ('172.40.84.%s' % i for i in range(1, 255))
#     for ip in ips:
#         #创建工作线程
#         t = threading.Thread(target=Ping(ip))
#         t.start()

#*****************urllib模块
"""
实现http客户端功能
包括4个子模块
    request:最常用的模块
    error:定义错误,实现异常
    parse:用来解析和处理URL
    robotparse:解析页面的robots.txt文件
"""
# from urllib import request
#
# url = 'http://www.baidu.com'
# html = request.urlopen(url)
# html.readline()
# html.read(10)
# html.readlines()

# #简单爬去网页图片
# from urllib import request
# import sys
#
# def download(url, fname):
#     html = request.urlopen(url)
#
#     with open(fname, 'wb') as fobj:
#         while 1:
#             data = html.read(4096)
#             if not data:
#                 break
#             fobj.write(data)
#
# if __name__ == '__main__':
#     url = sys.argv[1]
#     fname = sys.argv[2]
#     download(url, fname)

# #修改请求头(绕过防御)
# from urllib import request
#
# url = 'http://www.jianshu.com'
# html = request.urlopen(url) #403:Forbidden

# #简书他会做基本检查,发现请求不是正常的人为行为,将会拒绝
# #改变头部信息,骗过简述服务器,客户端浏览器改为火狐
# from urllib import request
#
# url = 'http://www.jianshu.com'
# heads = {'User-Agent': 'Mozilla/5.0 (x11; Linux x86_64; rv:52.0)'
#                        'Gecko/20100101 Firefox/52.0'}
# r = request.Request(url, headers=heads)
# html = request.urlopen(r)
# print(html.read())

#url编码
"""
url只允许一部分ascii字符,其他字符需要编码
"""
# from urllib import request
#
# # url = 'https://www.sogou.com/web?query=元旦'
# # html = request.urlopen(url) #会报错 因为只支持一部分ascii字符
#
# url = 'https://www.sogou.com/web?query=' + request.quote('性感荷官在线吃饭')
# print(url)

# #使用wget模块
# import wget
#
# url = 'https://gss2.bdstatic.com/9fo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike150%2C5%2C5%2C150%2C50/sign=e95e57acd20735fa85fd46ebff3864d6/f703738da9773912f15d70d6fe198618367ae20a.jpg'
# wget.download(url,'/tmp/fbb.jpg')

#下载所有网易图片
"""
找到所有图片url
下载图片
"""
# import wget
# import os
# import re
#
# def get_url(fname,patt,encoding=None):
#     result = []
#     cpatt = re.compile(patt)
#
#     with open(fname,encoding=encoding) as fobj:
#         for line in fobj:
#             m = cpatt.search(line)
#             if m:
#                 result.append(m.group())
#
#     return result
#
#
# if __name__ == '__main__':
#     img_dir = '/tmp/163'
#     fname163 = '/tmp/163/163.html'
#     url163 = 'http://www.163.com'
#     #如果不存在保存图片的目录,则创建
#     if not os.path.exists(img_dir):
#         os.mkdir(img_dir)
#
#     #如果网易首页文件不存在, 则下载
#     if not os.path.exists(fname163):
#         wget.download(url163,fname163)
#
#     #取出网易首页中所有的图片地址
#     img_patt = '(http|https)://[-\w/.]+\.(jpg|png|jpeg|gif)'
#     img_list = get_url(fname163,img_patt,'gbk')
#     #下载图片
#     for url in img_list:
#         wget.download(url,img_dir)

#*************************午间/晚间练习****************************
# class Date:
#     def __init__(self,year,month,date):
#         self.year = year
#         self.month = month
#         self.date = date
#
#     @classmethod #类方法,不用创建实例即可调用
#     def create(cls,dstr):
#         y,m,d = map(int,dstr.split('-')) ##map(int,['2000','5','4'])
#         dt = cls(y,m,d) #即Date(y,m,d)
#         return dt
#
#     @staticmethod #静态方法 写在类的外面,可以独立成为一个函数,'愣'把它放到类中了
#     def is_date_valid(dstr):
#         y,m,d = map(int,dstr.split('-'))
#         return 1 <= d <= 31 and 1 <= m <= 12 and y < 4000
#
# if __name__ == '__main__':
#     bith_date = Date(1995,12,3)
#     print(Date.is_date_valid('2000-5-4'))
#     day = Date.create('2000-5-4')
#     print(day)

#OPP练习
# import os
#
# class Convert:
#     def __init__(self,fname):
#         self.fname = fname
#
#     def to_linux(self):
#         dst_fname = os.path.splitext(self.fname)[0]+ '.linux'
#         with open(self.fname,'r')as src_fobj:
#             with open(dst_fname,'w')as dst_fobj:
#                 for line in src_fobj:
#                     line = line.rstrip() + '\n'
#                     dst_fobj.writelines(line)
#
#     def to_windows(self):
#         dst_fname= os.path.splitext(self.fname)[0]+ ',windows'
#         with open(self.fname,'r')as src_fobj:
#             with open(dst_fname,'w')as dst_fobj:
#                 for line in src_fobj:
#                     line = line.rstrip() + '\r\n'
#                     dst_fobj.write(line)
#
# if __name__ == '__main__':
#     c = Convert('/tmp/passwd') #cp /etc/passwd /tmp
#     c.to_linux()
#     c.to_windows()

#***************re模块基础
# import re
#
# m = re.match('f', 'food') #匹配到返回对象
# print(re.match('f..', 'seafood')) #匹配不到返回None
# m.group() #返回匹配的值
# m = re.search('f..', 'seafood') #全文搜索匹配
# m.group()
# re.findall('f', 'seafood is food') #返回所有匹配项组成的列表
#
# result = re.finditer('f..','seafood is food') #返回匹配对象组成的迭代器
# for m in result: #从迭代器中逐个取出匹配对象
#     print(m.group())
#
# re.sub('f..', 'abc', 'fish is food')
# re.split('\.|-',' hello-world.tar.gz') #用.和-做切割符号
#
# patt = re.compile('f..') #先把要匹配的模式编译,提升效率
# m = patt.search('seafood') #指定在那个字符串中匹配
# m.group()

# #re练习:匹配文件中制定模式
# import re
#
# def count_patt(fname,patt):
#     cpatt = re.compile(patt)
#     result = {}
#
#     with open(fname)as fobj:
#         for line in fobj:
#             m = cpatt.search(line) #如果匹配不到 返回None
#             if m:
#                 key = m.group()
#                 result[key] = result.get(key, 0)+1
#
#     return result
#
#
# if __name__ == '__main__':
#     fname = 'access_log'#apache日志文件
#     ip = '^(\d+\.){3}\d+' #日志开头的ip地址
#     print(count_patt(fname,ip))
#     br = 'Firefox|MSIE|Chrome' #日志中客户端浏览器
#     print(count_patt(fname,br))

#re练习;模式匹配进阶写法
# import re
# from collections import Counter  # Counter对象是有序的，字典无序
#
# class CountPatt:
#     def __init__(self, fname):
#         self.fname = fname
#
#     def count_patt(self, patt):
#         cpatt = re.compile(patt)
#         result = Counter()
#
#         with open(self.fname) as fobj:
#             for line in fobj:
#                 m = cpatt.search(line)  # 如果匹配不到，返回None
#                 if m:
#                     result.update([m.group()])
#
#         return result
#
#
# if __name__ == '__main__':
#     c = CountPatt('access_log')
#     ip = '^(\d+\.){3}\d+'
#     br = 'Firefox|MSIE|Chrome'
#     a = c.count_patt(ip)
#     print(a)
#     print(a.most_common(3))  # 访问量最大的前三名
#     print(c.count_patt(br))

#*********socket基础
# import socket
#
# host = ''#表示本机所有地址0.0.0.0
# port =123456 #应该大于1024
# addr = (host, port)
# s = socket.socket() #默认值就是基于tcp的网络套接字
# #设置选项,程序结束之后可以立即在运行,否则需要等60秒
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# s.bind(addr)  #绑定地址到套接字
# s.listen(1) #启动监听进程
# cli_sock,cli_addr = s.accept()  #等带客户端链接
# print('Client connect from: ',cli_addr)
# print(cli_sock.recv(1024))  #一次最多读1024字节数据
# cli_sock.send(b'I4CPU\r\n')  #发送的数据要求是bytes类型
# cli_sock.close()
# s.close()

#可重用的TCP服务器
# import socket
#
# host = ''
# port = 12345
# addr = (host, port)
# s = socket.socket()
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# s.bind(addr)
# s.listen(1)
# while True:
#     cli_sock, cli_addr = s.accept()
#     print('Client connect from:', cli_addr)
#     while True:
#         data = cli_sock.recv(1024)
#         if data.strip() == b'end':
#             break
#         print(data.decode('utf8'))  # bytes类型转为string类型
#         data = input('> ') + '\r\n'  # 获得的是string类型
#         cli_sock.send(data.encode('utf8'))  # 转成bytes类型发送
#     cli_sock.close()
# s.close()

# #简单完整的TCP服务器
# import socket
# from time import strftime
#
# class TcpTimeServer:
#     def __init__(self, host='', port=12345):
#         self.addr = (host, port)
#         self.serv = socket.socket()
#         self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         self.serv.bind(self.addr)
#         self.serv.listen(1)
#
#     def chat(self, c_sock):
#         while True:
#             data = c_sock.recv(1024)
#             if data.strip() == b'quit':
#                 break
#             data = '[%s] %s' % (strftime('%H:%M:%S'), data.decode('utf8'))
#             c_sock.send(data.encode('utf8'))
#         c_sock.close()
#
#     def mainloop(self):
#         while True:
#             cli_sock, cli_addr = self.serv.accept()
#             self.chat(cli_sock)
#
#         self.serv.close()
#
# if __name__ == '__main__':
#     s = TcpTimeServer()
#     s.mainloop()

#简单的TCP客户端
# import socket
#
# host = '192.168.4.254' #服务器IP地址
# port = 123456 #服务器端口
# addr = (host,port)
#
# c = socket.socket()
# c.connetc(addr)
# while True:
#     data = input('>')+ '\r\n'
#     c.send(data.encode('utf8')) #服务器收到end结束,所以要先发送在判断
#     if data.strip() == 'end':
#         break
#     data = c.recv(1024)
#     print(data.decode('utf8'))
#
# c.close()

# #简单的udp服务器流程
# import socket
# from time import strftime
#
# host = ''
# port = 12345
# addr =(host,port)
# s = socket.socket(type=socket.SOCK_DGRAM)
# s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# s.bind(addr)
#
# while True:
#     data.cli_addr = s.recvfrom(1024)
#     clock = strftime('%H:%M:%S')
#     data = data.decode('utf8')
#     data = '[%s]%s' %(clock,data)
#     s.sendto(data.encode('utf8'),cli_addr)
#
# s.close()

#简单的udp客户端的流程
# import socket
#
# host = '192.168.4.254'
# port = 12345
# addr = (host,port)
#
# c = socket.socket(type=socket.SOCK_DGRAM)
#
# while True:
#     data = input('>')
#     if data.strip() == 'quit':
#         break
#     c.sendto(data.encode('utf8'),addr)
#     print(c.recvfrom(1024)[0].decode('utf8'))
#     #print(c.recvfrom(1024))
#
# c.close()

#