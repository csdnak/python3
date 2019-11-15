#!/bin/env python3
#-*- coding:utf8 -*-
#学Python3的第十三天
#paramiko模块
# """pip安装paramiko模块
# #pip install paramiko
# """
# import paramiko
#
#
# ssh = paramiko.SSHClient()  #创建SSHClient对象
# #自动接收服务器发来的秘钥,相当于是自懂回答yes
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('192.168.1.50', username='root', password='123')  #登录
# result = ssh.exec_command('id root; id csdnak')  #执行命令
# #分析返回的结果,result是一个长度为3的元组
# len(result)
#
# #result中的三项分别是输入 输出和错误的类文件对象.
# stdin, stdout, stderr = result
# out = stdout.read()  #读取输出信息
# err = stderr.read()  #读取错误信息
# out.decode()   #将bytes转为str
# err.decode()
#
# print(out)
# print(err)
#
# ssh.close()  #关闭链接

#将上方写成函数程序
# import paramiko
#
# def rcmd(host,user='root',passwd=None,port=22,cmd=None):
#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#     ssh.connect(host, username=user,port=port, password=passwd)
#     stdin, stdout ,stderr = ssh.exec_command(cmd)
#     out = stdout.read()
#     err = stderr.read()
#     if out:
#         print('\033[32;1m[%s] OUT:\n%s\033[0m' % (host, out.decode()))
#     if err:
#         print('\033[31;1m[%s] ERROR:\n%s\033[0m' % (host, err.decode()))
#
#     ssh.close()
#
# if __name__ == '__main__':
#     rcmd('192.168.1.50', passwd='123', cmd='id csdnak;sl')

#改良:使其能讲内容写入文件(自由发挥)
# import paramiko
# import sys
#
# def rcmd(host,user='root',passwd=None,port=22,cmd=None):
#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#     ssh.connect(host, username=user,port=port, password=passwd)
#     stdin, stdout ,stderr = ssh.exec_command(cmd)
#     out = stdout.read()
#     err = stderr.read()
#     alist = []
#     if out:
#         while True:
#             with open('/tmp/query.txt','wb') as fobj:
#                 data = out.decode()
#                 if not data:
#                     break
#                 alist.append(data)
#                 fobj.write(alist)
#     if err:
#         while True:
#             with open('/tmp/query.txt','wb') as fobj:
#                 data = err.decode()
#                 if not data:
#                     break
#                 alist.append(data)
#                 fobj.write(alist)
#     ssh.close()
#
# if __name__ == '__main__':
#     rcmd('192.168.1.50', passwd='123', cmd='id csdnak;sl')

#优化版本
# import paramiko
# import sys
# import getpass
# import threading
# import os
#
#
# def rcmd(host,user='root',passwd=None,port=22,cmd=None):
#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#     ssh.connect(host, username=user,port=port, password=passwd)
#     stdin, stdout ,stderr = ssh.exec_command(cmd)
#     out = stdout.read()
#     err = stderr.read()
#     if out:
#         print('\033[32;1m[%s] OUT:\n%s\033[0m' % (host, out.decode()))
#     if err:
#         print('\033[31;1m[%s] ERROR:\n%s\033[0m' % (host, err.decode()))
#
#     ssh.close()
#
# if __name__ == '__main__':
#     #rcmd('192.168.1.50', passwd='123', cmd='id csdnak;sl')
#     if len(sys.argv) != 3:
#         print("Usage: %s ipfile 'command" % sys.argv[0])
#         exit(1)
#
#     if not os.path.isfile(sys.argv[1]):
#         print('No such file: ',sys.argv[1])
#         exit(2)
#
#     ipfile = sys.argv[1]
#     cmd = sys.argv[2]
#     passwd = getpass.getpass()
#     with open(ipfile) as fobj:
#         for line in fobj:
#             ip = line.rstrip() #去除行末尾的\n
#             #rcmd(ip, passwd=passwd , cmd=cmd)
#             t = threading.Thread(
#                 target=rcmd, args=(ip,),
#                 kwargs={'passwd': passwd, 'cmd': cmd}
#             )
#             t.start() #rcmd(*args, **kwargs)

#*************邮件编程
# """
# 写邮件: 使用email模块
# 发邮件: 使用smtplib模块
# """
# from email.mime.text import MIMEText
# from email.header import Header
# import smtplib
#
# #准备邮件
# msg = MIMEText('这是一封Python邮件测试\n','plain','utf8') #plain普通文本邮件模式
# msg['From'] = Header('root', 'utf8')
# msg['To'] = Header('bob', 'utf8')
# msg['Subject'] = Header('py test', 'utf8')
#
# #发送邮件
# smtp = smtplib.SMTP('127.0.0.1')
# smtp.sendmail('root', ['root', 'student'], msg.as_bytes()) #bytes/string都行
# smtp.close()


#******改良:改成函数 local_mail.py
# #优化版本
# from email.mime.text import MIMEText
# from email.header import Header
# import smtplib
# import getpass
#
# def send_mail(body, sender, receivers, subject, host, passwd):
#     # 准备邮件
#     msg = MIMEText(body, 'plain', 'utf8')
#     msg['From'] = Header(sender, 'utf8')
#     msg['To'] = Header(receivers[0], 'utf8')
#     msg['Subject'] = Header(subject, 'utf8')
#
#     # 发送邮件
#     smtp = smtplib.SMTP()
#     smtp.connect(host)
#     #smtp.starttls() #如果服务器要求安全通信,打开此注释
#     smtp.login(sender, passwd)
#     smtp.sendmail(sender, receivers, msg.as_bytes())
#     smtp.close()
#
#
# if __name__ == '__main__':
#     body = '这是一封来自Python的邮件测试\n'
#     sender = 'wang614256@163.com'
#     receivers = ['wang614256@163.com']
#     subject = 'py test'
#     host = 'smtp.163.com'
#     passwd = getpass.getpass()
#     send_mail(body, sender, receivers, subject, host, passwd)



#***************进一步优化(自由发挥)
# from email.mime.text import MIMEText
# from email.header import Header
# import smtplib
# import getpass
#
#
# def send_mail(body, sender, receivers, subject, host, passwd):
#     msg = MIMEText(body, 'plain', 'utf8')
#     msg['From'] = Header(sender, 'utf8')
#     msg['To'] = Header(receivers[0], 'utf8')
#     msg['Subject'] = Header(subject, 'utf8')
#
#     smtp = smtplib.SMTP()
#     smtp.connect(host)
#     # smtp.starttls()  # 如果服务器要求安全通信，打开此注释
#     smtp.login(sender, passwd)
#     smtp.sendmail(sender, receivers, msg.as_bytes())
#     smtp.close()
#     print('\033[32;1mEmail: Send successful!\033[0m')
#
#
# if __name__ == '__main__':
#     prompt = """\033[32m(1) SendEmail
# (2) Exit
# 请选择(1/2): """
#     while True:
#         choice = input(prompt).strip()[0]
#         if choice == '1':
#             try:
#                 sender = input('\033[32mUserName: ')
#                 passwd = getpass.getpass()
#                 subject = input('\033[32mPlease input subject: ')
#                 body = input('\033[32mPlease input content: ')
#                 receivers = [input('\033[32mAddressee: ')]
#                 host = 'smtp.163.com'
#                 send_mail(body, sender, receivers, subject, host, passwd)
#             except (KeyboardInterrupt,EOFError):
#                 print('\033[32;1m\nBye-bye!\033[0m')
#                 exit(1)
#         else:
#             print('\033[32;1m\nBye-bye!\033[0m')
#             break

#*************JSON*************
# """
# JSON(JavaScript Object Notation)是一种轻量级的数据交换格式
# JSON采用完全独立于语言的文本格式,但是也使用了类似于C语言家族的习惯(包括C, C++, C#,
# Java,JavaScript, Perl, Python等)
# - python只要将数据类型转成json格式，其他语言的程序接收后，还能转成它能理解的数据类型
# """
# import json
#
# adict = {'name': 'bob', 'age': 20}
# json.dumps(adict)
# data = json.dumps(adict) #将字典转成json字符串
# print(type(data))
# print(data)
#
# rdata = json.loads(data) #将json字符串转换成字典
# print(type(rdata))
# print(rdata)

#************requests模块*******
# """
# Requests是用python语言编写的,优雅而简单的HTTP库
# Requests内部采用urillib3
# 常用的HTTP方法
#     GET:浏览器中输入网址,点击超链接,表单的默认提交方式
#     POST:表单明确声明的方法,用于提交数据
#     put /delete/options/head
# requests模块为每种方法都创建了函数
# """
# import requests
#
# url1 = 'http://www.163.com'
# r=requests.get(url1)
# r.text #r.text用于显示字符内容
#
# url2 = 'http://www.163.com'
#   #改地址是一个图片的URL
# r2 = requests.get(url2)
# with open('/tmp/bbb.jpg','wb') as fobj:
#     fobj.write(r2.content) #非字符内容用r2.content
#
# #北京的城市的代码:101010100
# url3 = 'http://www.weather.com.cn/data/sk/101010100.html'
# r3 = requests.get(url3)
# r3.encoding = 'utf8' #修改编码
# print(r3.json() #返回json数据

#*****查快递
# import requests
#
# url = 'http://www.kuaidi100.com/query'
# param = {'type': 'yuantong',"postid": '4182963481428'}
# r = requests.get(url,params=param)
# print(r.json())
# """
# #浏览器上对应的url:
# http://www.kuaidi100.com/query?type='yuantong&postid=4182963481428'
# """
#****配置钉钉机器人(用前 吧前面全部都注释了 包括""""""也注释)
# import requests
# import json
# import getpass
#
# url = getpass.getpass()
# # 头部固定的，钉钉开发者手册上明确要求的
# headers = {'Content-Type': 'application/json;charset=utf-8'}
# # data是从钉钉开发者手册上粘过来的
# # data = {
# #     "msgtype": "text",
# #     "text": {
# #         "content": "天王盖地虎。我就是我, 是不一样的烟火@156xxxx8827"
# #     },
# #     "at": {
# #         "atMobiles": [  # @哪些人
# #             "156xxxx8827",
# #             "189xxxx8325"
# #         ],
# #         "isAtAll": False  # 是否@所有人
# #     }
# # }
#
# data = {
#     "msgtype": "markdown",
#     "markdown": {
#         "title": "杭州天气",
#         "text": "#### 杭州天气 @156xxxx8827\n" +
#                 "> 9度，西北风1级，空气良89，相对温度73% 天王盖地虎\n\n" +
#                 "> ![screenshot](https://gw.alicdn.com/tfs/TB1ut3xxbsrBKNjSZFpXXcXhFXa-846-786.png)\n"  +
#                 "> ###### 10点20分发布 [天气](http://www.sogou.com/) \n"
#     },
#     "at": {
#         "atMobiles": [
#             "156xxxx8827",
#             "189xxxx8325"
#         ],
#         "isAtAll": False
#     }
# }
#
# # 钉钉开发者手册明确要求，使用post方法
# # 字典不能直接发送，必须转成json字符串
# r = requests.post(url, headers=headers, data=json.dumps(data))
# print(r.json())

#********************************部署zabbix钉钉报警*************************
# import requests
# import json
#
# url = 'http://192.168.1.50/api_jsonrpc.php'
# header = {'Content-Type': 'application/json-rpc'}

#################################
# #如果获取公共信息,可以直接发送请求,如软件版本
# data = {
#     "jsonrpc": "2.0", #zabbix采用jsonrpc协议,固定值
#     "method": "apiinfo.version", #方法
#     "params": [], #参数
#     "id": 101 #随意给一个数字表示作业号
# }
##################################
# #通过用户名和密码获取认证令牌
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1,
# }
#####################################
#获取所有的主机
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#         "filter": {           #过滤出符合条件的主机
#             # "host": [
#             #     "Zabbix server",
#             #     "Linux server"
#             # ]
#         }
#     },
#     "auth": "e42fd5b516ed9dc6d5c8db2aa990eb3c", #从上个步骤获取认证令牌
#     "id": 1
# }
#######################################
#删除主机
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.delete",
#     "params": [
#         "10254",  # 删除主机id是10254的主机
#     ],
#     "auth": "e42fd5b516ed9dc6d5c8db2aa990eb3c",
#     "id": 1
# }

#######################################
#获取Linux Server组的ID
# data = {
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "name": [
#                 "Linux servers",
#             ]
#         }
#     },
#     "auth": "e42fd5b516ed9dc6d5c8db2aa990eb3c",
#     "id": 1
# }
#######################################
#获取Template OS Linux的ID =>10001
# data = {
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux",
#             ]
#         }
#     },
#     "auth": "e42fd5b516ed9dc6d5c8db2aa990eb3c",
#     "id": 1
# }

######################################
#创建名nsd1906web1的主机,他在Linux Servers组中 应用Tempate OS Linxu末班
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.create",
#     "params": {
#         "host": "Linux server",
#         "interfaces": [  #通过什么方式监控
#             {
#                 "type": 1,
#                 "main": 1,
#                 "useip": 1,
#                 "ip": "192.168.4.100",
#                 "dns": "",
#                 "port": "10050"
#             }
#         ],
#         "groups": [
#             {
#                 "groupid": "2"
#             }
#         ],
#         "templates": [
#             {
#                 "templateid": "10001"
#             }
#         ],
#         "inventory_mode": 0,   # 主机资产记录
#         "inventory": {
#             "macaddress_a": "mei you",
#             "macaddress_b": "56768"
#         }
#     },
#     "auth": "e42fd5b516ed9dc6d5c8db2aa990eb3c",
#     "id": 1
# }




###############################
#输出内容,主要关注result即可
# r = requests.post(url, headers=header, data=json.dumps(data))
# print(r.json())
#******************************************************************************










#**************晚间练习***************
#多进程基础
# import os
#
# print('starting...')
# os.fork() #生成子进程.后续代码同时在父子进程中执行
# print('Hello World!')
# #***********根据fork返回值判断是父进程还是子进程
# import os
#
# print('starting...')
#
# pid = os.fork() #返回值十个数字,对于父进程,返回值是个子进程pid,子进程是0
# if pid:
#     print('In parent') #父进程执行的代码
# else:
#     print('In child') #子进程执行的代码
#
# print('Done') #父子进程都会执行的代码

"""
多进程编程时，要明确父子进程的工作。如：父进程只用于fork子进程；
子进程做具体的工作，如果在循环结构中，做完后要退出，否则子进程还会再产生子进程、
孙进程……子子孙孙无穷匮也，系统崩溃。
"""
# import os
#
# for i in range(5):
#     pid = os.fork() #父进程的工作是生成子进程
#     if not pid: #如果是子进程,工作完后,结束,不要进入循环
#         print('hello')
#         exit() #注视着一行执行,查看结果,分析原因
#
#
# #多进程的ping
# import subprocess
# import os
#
# def ping(host):
#     rc = subprocess.call(
#         'ping -c2 %s > /dev/null' % host,
#         shell=True
#     )
#     if rc:
#         print('%s: down' % host)
#     else:
#         print('%s: up' % host)
#
# if __name__ == '__main__':
#     ips = ('192.168.1.%s'% i for i in range(1,255))
#     for ip in ips:
#         pid = os.fork()
#         if not pid:
#             print(ip)
#             exit()

#多进程的效率
# import  time
#
# def calc():
#     result = 0
#     for i in range(1,50000001):
#         result +=i
#     print(result)
#
# if __name__ == '__main__':
#     start = time.time()
#     calc()
#     calc()
#     end = time.time()
#     print(end - start)

# import time
# import os
# def calc():
#     result = 0
#     for i in range(1,50000001):
#         result +=i
#     print(result)
#
# if __name__ == '__main__':
#     start = time.time()
#     for i in range(2):
#         pid = os.fork()
#         if not pid:
#             calc()
#             exit()
#         os.waitpid(-1,0) #挂起父进程,直到子进程结束接继续向下执行
#         os.waitpid(-1,0) #每个waitpid只能处理一个僵尸进程,两个子进程需要太偶用两次
#         end = time.time()
#         print(end - start)

# #僵尸进程
# import  os
# import time
#
# pid = os.fork()
#
# if pid:
#     print('In parent.sleeping...')
#     time.sleep(60)
#     print('parent done.')
# else:
#     print('In child.sleeping...')
#     time.sleep(10)
#     print('child done') #10秒后,子进程变成了僵尸进程
#
# #watch -n1 ps a 当子进程成为僵尸进程,显示为z
# #kill 试图杀死僵尸进程,附近进程,查看结果

#解决僵尸进程问题
# import os
# import time
#
# pid = os.fork()
#
# if pid:
#     print('In parent sleeping...')
#     print(os.waitpid(-1,1)) #无僵尸进程可以处理,返回0
#     time.sleep(20)
#     print(os.waitpid(-1,1)) #处理僵尸进程,返回子进程PIP
#     time.sleep(60)
#     print('parent done.')
# else:
#     print('In hcild.sleeping...')
#     time.sleep(10)
#     print('child done')
#
# # watch -n1 ps a  当子进程成为僵尸进程时，显示为Z
# # kill 试图杀死僵尸进程、父进进程，查看结果

#基于多进程的时间消息服务器
# import socket
# import os
# from time import strftime
#
# class TcpTimeServer:
#     def __init__(self,host='',port=12345):
#         self.addr = (host,port)
#         self.serv = socket.socket()
#         self.serv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#         self.serv.bind(self.addr)
#         self.serv.listen(1)
#
#     def chat(self,c_sock):
#         while True:
#             data = c_sock.recv(1024)
#             if data.strip() == b'quit':
#                 break
#             data = '[%s]%s'% (strftime('%H:%M:%S'),data.decode('utf8'))
#             c_sock.send(data.encode('utf8'))
#         c_sock.close()
#
#     def mainloop(self):
#         while True:
#             cli_sock,cli_addr = self.serv.accept()
#             pid = os.fork()
#             if pid:
#                 cli_sock.close()
#                 while True:
#                     result = os.waitpid(-1,1)[0] #waitpid会优先处理僵尸进程
#                     if result == 0:
#                         break
#             else:
#                 self.serv.close()
#                 self.chat(cli_sock)
#                 exit()
#
#         sel.serv.close()
#
#
# if __name__ == '__main__':
#     s = TcpTimeServer()
#     s.mainloop()

# #基于多线程的ping
# import subprocess
# import threading
#
# def ping(host):
#     rc = subprocess.call(
#         'ping -c2 %s & > /dev/null' % host,
#         shell=True
#     )
#     if rc:
#         print('%s: down'% host)
#     else:
#         print('%s: up'% host)
#
# if __name__ == '__main__':
#     ips = ['172.40.58.%s' % i for i in range(1,255)]
#     for ip in ips:
#         #创建线程,ping是上面定义的函数,args是传给ping函数的参数
#         t = threading.Thread(target=ping,args=(ip,))
#         t.start()

#多线程的效率
# import time
# import threading
#
# def calc():
#     result = 0
#     for i in range(1,50000001):
#         result += i
#     print(result)
#
# if __name__ == '__main__':
#     start = time.time()
#     t1 = threading.Thread(target=calc)
#     t1.start()
#     t2 = threading.Thread(target=calc)
#     t2.start()
#     t1.join() #挂起主进程.当t1简称执行完后才继续向下执行
#     t2.join()
#     end = time.time()
#     print(end - start)

# #基于多进程的时间消息服务器
# import socket
# import threading
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
#             t = threading.Thread(target=self.chat, args=(cli_sock,))
#             t.start()
#
#         self.serv.close()
#
# if __name__ == '__main__':
#     s = TcpTimeServer()
#     s.mainloop()

#并行批量管理远程服务器
#remote_comm.py
# import sys
# import getpass
# import paramiko
# import threading
# import os
#
# def remote_comm(host,pwd,command):
#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh.connect(hostname=host,username='root',password=pwd)
#     stdin , stdout , stderr = ssh.exec_command(command)
#     out = stdout.read()
#     err = stderr.read()
#     if out:
#         print('[%s]OUT:\n%s' % (host,out.decode('utf8')))
#     if err:
#         print('[%s]ERROR:\n%s' % (host,err.decode('utf8')))
#     ssh.close()
#
# if __name__ == '__main__':
#     if len(sys.argv) != 3:
#         print('Usage: %s ipaddr_file "command"' % sys.argv[0])
#         exit(1)
#     if not os.path.isfile(sys.argv[1]):
#         print('No such file: ',sys.argv[1])
#         exit(2)
#     fname = sys.argv[1]
#     command = sys.argv[2]
#     pwd = getpass.getpass()
#     with open(fname) as fobj:
#         ips = [line.strip() for line in fobj]
#
#     for ip in ips:
#         t = threading.Thread(target=remote_comm,args=(ip,pwd,command))
#         t.start()

#*************配置ip地址
# import sys
# import re
# from _curses import raw
#
#
# def configip(fname, ip_addr, if_ind):
#     content = """TYPE=Ethernet
# BOOTPROTO=none
# NAME=eth%s
# DEVICE=eth%s
# ONBOOT=yes
# IPADDR=%s
# PREFIX=24
# """ % (if_ind, if_ind, ip_addr)
#     with open(fname, 'w') as fobj:
#         fobj.write(content)
#
# def check_ip(ip_addr):   # 判断IP地址是不是X.X.X.X格式
#     m = re.match(r'(\d{1,3}\.){3}\d{1,3}$', ip_addr)
#     if not m:
#         return False
#     return True
#
# def show_menu():
#     prompt = """Configure IP Address:
# (0) eth0
# (1) eth1
# (2) eth2
# (3) eth3
# Your choice(0/1/2/3): """
#     try:
#         if_ind = raw_input(prompt).strip()[0]
#     except:
#         print ('Invalid input.')
#         sys.exit(1)
#
#     if if_ind not in '0123':
#         print ('Wrong Selection. Use 0/1/2/3')
#         sys.exit(2)
#
#     fname = '/etc/sysconfig/network-scripts/ifcfg-eth%s' % if_ind
#     ip_addr = raw_input('ip address: ').strip()
#     result = check_ip(ip_addr)
#     if not result:
#         print ('Invalid ip address')
#         sys.exit(3)
#     configip(fname, ip_addr, if_ind)
#     print('\033[32;1mConfigure ip address done. Please execute "systemctl restart NetworkManager"\033[0m')
#
# if __name__ == '__main__':
#     show_menu()
#********************************
#模拟字符串lstrip用法
# whitesps = '\r\n\v\f\t'
#
# def rmlsps(astr):
#     for i in range(len(astr)):
#         if astr[i] not in whitesps:
#             return astr[i:]
#     else: #所有字符均为空,循环正常结束,返回空串
#         return ''
#
# if __name__ == '__main__':
#     print(rmlsps('\thello'))
# whitesps = '\r\n\v\f\t'
#
# def rmrsps(astr):
#     for i in range(-1,-len(astr),-1): #自右向左 下标为负
#         if astr[i] not in whitesps:
#             return astr[:i + 1]  #结束下表对应的字符不包含,所以加1
#         else:
#             return ''
#
# if __name__ == '__main__':
#     print(rmrsps(''))
#     print(rmrsps('\thello'))

# whitesps = ' \r\n\v\f\t'
#
# def rmrsps(astr):
#     for i in range(len(astr) - 1, -1, -1):
#         if astr[i] not in whitesps:
#             return astr[:i + 1]  # 结束下标对应的字符不包含，所以加1
#     else:
#         return ''
#
# if __name__ == '__main__':
#     print(rmrsps(''))
#     print(rmrsps('  \thello  '))
"""
我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
思路：
1、答案不只一个
2、如果全是公鸡i，最多100/5只
3、如果全是母鸡j，最多100/3只
4、如果全是小鸡k，100块钱，可以买300只；但，所有的鸡最多是100只
5、鸡的数目i+j+k==100
6、鸡的价钱i * 5 + j * 3 + k / 3 == 100

作者：凯茜的老爸
链接：https://www.jianshu.com/p/a915980dadd0
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
# for i in range(100//5+1): #//表示只留商 不要小数 舍弃余数
#     for j in range(100//3+1):
#         for k in range(100 + 1):
#             if i + j + k == 100 and i * 5+j*3+k/3 == 100:
#                 print('公鸡:%s,母鸡:%s,小鸡:%s'% (i,j,k))

#fork子进程解析
# import os
#
# for i in range(3):
#     pid = os.fork()
#     if not pid:
#         print('hello')
#

#可变与不可变对象的效率
# from random import choice
# import string
#
# all_chs = string.ascii_letters + string.digits #大小写字母加数字
#
# def gen_pass(n = 8):
#     result = []
#
#     for i in range(n):
#         ch =choice(all_chs)
#         result.append(ch)
#
#     return ''.join(result)
#
# if __name__ == '__main__':
#     print(gen_pass())
#     print(gen_pass(4))
#     print(gen_pass(10))

#************比较文件的差异
# import difflib
# import webbrowser
# import sys
# import string
# import os
# from random import choice
#
# def rand_chs(n=8): #默认生成8个随机字符
#     all_chs = string.ascii_letters + string.digits
#     result = [choice(all_chs)for i in range(n)]
#     return ''.join(result)
#
# #函数接受连个相似的文件名,返回HTML形式的字符串
# def make_diff(lfile,rfile):
#     d = difflib.HtmlDiff()
#
#     #将两个文件分别读到列表中
#     with open(lfile) as fobj:
#         ldata = fobj.readlines()
#
#     with open(rfile) as fobj:
#         rdata = fobj.readlines()
#
#     return  d.make_file(ldata,rdata)
#
# if __name__ == '__main__':
#     try:
#         lfile = sys.argv[1]
#         rfile = sys.argv[2]
#     except IndexError:
#         print('Usage: %s file1 file2'% sys.argv[0])
#         sys.exit(1)
#     if not os.path.isfile(lfile):
#         print('No such file: ', lfile)
#         sys.exit(2)
#     if not os.path.isfile(rfile):
#         print('No such file: ', rfile)
#         sys.exit(3)
#     data  = make_diff(lfile,rfile)
#     #以下只是为说明内容增加中文显示,非必须项
#     data = data.replace(';Added', ';Added（增加）')
#     data = data.replace('>Changed', '>Changed（改变）')
#     data = data.replace('>Deleted', '>Deleted（被删除）')
#     data = data.replace('(f)irst change', '(f)irst change【第一处变更】')
#     data = data.replace('(n)ext change', '(n)ext change【下一处变更】')
#     data = data.replace('(t)op', '(t)op【回到顶部】')
#     html_file = '/tmp/%s.html' % rand_chs()  # 用随机字符生成文件名
#     with open(html_file, 'w') as fobj:
#         fobj.write(data)
#     webbrowser.open_new_tab('file:///%s' % html_file)  # 使用浏览器打开文件
#****************************

#进度条
"""
[root@room8pc16 ~]# vim /tmp/process_bar.py
from tqdm import tqdm
import time

for i in tqdm(range(10)):
    time.sleep(1)

[root@room8pc16 ~]# python3 /tmp/process_bar.py
30%|█████████████▏                              | 3/10 [00:03<00:07,  1.00s/it]
"""
#带进度条的拷贝文件
# import  os
# import sys
# import tqdm import tqdm
#
# def copy(src_fname,dst_fname,length=4096):
#     size = os.stat(src_fname).st_size
#     times,extra = divmod(size,length)
#     if extra:
#         times += 1
#
#     with open(src_fname,'rb') as src_fobj:
#         with open(dst_fname,'wb') as dst_fobj:
#             for i in tqdm(range(times)):
#                 data = src_fobj.read(length)
#                 dst_fobj.write(data)
#
# if __name__ == '__main__':
#     copy(sys.argv[1],sys.argv[2])

#取出指定时间段的文本
# import time
#
# fname  = 'myfile.txt'
# t1 = time.strptime('2019-5-15 09:00:00', '%Y-%m-%d %H:%M:%S')
# t2 = time.strptime('2019-5-15 12:00:00', '%Y-%m-%d %H:%M:%S')
#
# with open(fname) as fobj:
#     for line in fobj:
#         t = time.strptime(line[:19],'%Y-%m-%d %H:%M:%S')
#         if t1 < t < t2:
#             print(line,end='')



