#!/bin/env python3
#-*- coding:utf8 -*-
#学python3的第十一天
#核心函数和方法(正则模块)
#************re模块
# import re
# #在food开头匹配f..匹配到返回匹配对象,否则返回None
# re.match('f..','food') #match匹配开头(了解即可)
# print(re.match('f..','seafood'))
#
# #在字符串中匹配f..(重点掌握)
# re.search('f..','seafood')
# m = re.search('f..','seafood')
# #匹配到之后,用group方法返回匹配结果
# print(m.group())
# print(m)
# #返回所有查询结果
# print(re.findall('f..','seafood is food'))
# #finditer返回的是由匹配对象构成的生成器
# a = list(re.finditer('f..','seafood is food'))
# print(a) #返回列表[<re.Match object; span=(3, 6), match='foo'>, <re.Match object; span=(11, 14), match='foo'>]
# #利用for循环逐个取出
# for m in re.finditer('f..','seafood is food'):
#     print(m.group())
#
# #以.和-作为分隔符切割字符串
# r = re.split('-|\.','hello-world.tar.gz')
# print(r)
# #把x替换成tedu
# h = re.sub('x','tedu','Hello x. hi x')
# print(h)
#
# #为了提升效率,建议将正则表达式的模块优先编辑
# patt = re.compile('f..')
# m = patt.search('seafood')
# print(m.group())
# m = patt.findall('seafood is food')
# print(m)

#正则练习
#1310 行的access_log文件
#匹配ip用compile
# import re
#
# def count_patt(fname,patt):
#     result = {} #保存结果
#     cpatt = re.compile(patt) #编译模式,提升效率
#
#     with open(fname) as fobj:
#         for line in fobj:
#             m = cpatt.search(line)
#             if m: #如果配到了
#                 key = m.group()
#                 result[key] = result.get(key,0) + 1
#
#     return result
#
#
# if __name__ == '__main__':
#     fname = 'access_log'
#     ip = '^(\d+\.){3}\d+' #12345.654.1.234 10.123.45.8(不严谨 但是可用)
#     br = 'Firefox|MSIE|Chrome' #匹配火狐　微软　谷歌
#     result1 = count_patt(fname,ip)
#     result2 = count_patt(fname,br)
#     print(result1)
#     print(result2)
#
# #字典排序:字典本身没有顺序,需要将其转换成其他序列类型
#     alist = list(result1.items())
#     print(alist)
# """复杂列表排序
# 列表的sort方法　只持一名为key的参数
# key应该是一个函数
# 该函数处理列表每一项 处理结果作为排序依据
#
# """
# def get_second(seq):
#     return  seq[-1]
#
# alist.sort(key=get_second)
# print(alist)
# #上面写法可以用下一行解决
# alist.sort(key=lambda seq: seq[-1],reverse=True)
# print(alist)

# #用OOP实现
# import re
#
# class CountPatt:
#     def __init__(self, fname):
#         self.fname = fname
#
#     def count_patt(self, patt):
#         result = {}  # 保存结果
#         cpatt = re.compile(patt)  # 编译模式，提升效率
#
#         with open(self.fname) as fobj:
#             for line in fobj:
#                 m = cpatt.search(line)
#                 if m:  # 如果匹配到了
#                     key = m.group()
#                     result[key] = result.get(key, 0) + 1
#
#         return result
#
# if __name__ == '__main__':
#     fname = 'access_log'
#     ip = '^(\d+\.){3}\d+'  # 12345.6789.1.232, 10.123.45.8
#     br = 'Firefox|MSIE|Chrome'
#     cp1 = CountPatt(fname)
#     result1 = cp1.count_patt(ip)
#     result2 = cp1.count_patt(br)
#     print(result1)
#     print(result2)
#     print('*'* 30)
#
#     cp2 = CountPatt('/etc/passwd')
#     result3 = cp2.count_patt('nologin$|bash$')
#     print(result3)

#安装数据库
# """
# ## 数据库
#
# ### 安装py软件包
#
# ```shell
# # 1. 在线直接安装
# (nsd1906) [root@room8pc16 day04]# pip install pymysql
# # 直接安装，将访问python官方站点，速度慢，可以使用国内镜像站点，方法如下：
# (nsd1906) [root@room8pc16 day04]# mkdir ~/.pip/
# (nsd1906) [root@room8pc16 day04]# vim ~/.pip/pip.conf
# [global]
# index-url = http://pypi.douban.com/simple/
# [install]
# trusted-host=pypi.douban.com
#
#
# # 2. 本地安装
# # ls /linux-soft/05/zzg_pypkgs.tar.gz
# # 将该文件解压:
# [root@room8pc16 zzg_pypkgs]# ls
# ansible-cmdb_pkgs  matplotlib_pkgs  requests_pkgs
# ansible_pkg        paramiko_pkgs    sqlalchemy_pkgs
# dj_pkgs            pymysql_pkgs     wordcloud_pkgs
# jenkins            python3_pkg
# (nsd1906) [root@room8pc16 day04]# pip install pymysql_pkgs/*
# """


#pymysql模块
#创建小型数据库
# import pymysql
#
# # 创建到数据库服务器的连接
# conn = pymysql.connect(
#     host='192.168.1.50',
#     port=3306,
#     user='root',
#     passwd='123456',
#     db='nsd1906',
#     charset='utf8'
# )
#
# # 创建游标。游标就像是文件对象，通过文件对象可以对文件读写
# # 通过游标，可以对数据实现增删改查
# cur = conn.cursor()
#
# # 编写sql语句
# create_dep = """CREATE TABLE departments(
# dep_id INT, dep_name VARCHAR(20),
# PRIMARY KEY(dep_id)
# )"""
# create_emp = """CREATE TABLE employees(
# emp_id INT, emp_name VARCHAR(20), birth_date DATE,
# email VARCHAR(50), dep_id INT,
# PRIMARY KEY(emp_id),
# FOREIGN KEY(dep_id) REFERENCES departments(dep_id)
# )"""
# create_sal = """CREATE TABLE salary(
# id INT, date DATE, emp_id INT, basic INT, awards INT,
# PRIMARY KEY(id),
# FOREIGN KEY(emp_id) REFERENCES employees(emp_id)
# )"""
#
# # 执行sql语句
# cur.execute(create_dep)
# cur.execute(create_emp)
# cur.execute(create_sal)
#
# # 如果是增删改操作，需要commit
# conn.commit()
#
# # 关闭
# cur.close()
# conn.close()


# #************插入/查询/修改/删除
# import pymysql
#
# # 创建到数据库服务器的连接
# conn = pymysql.connect(
#     host='192.168.1.50',
#     port=3306,
#     user='root',
#     passwd='123456',
#     db='nsd1906',
#     charset='utf8'
# )

# # 创建游标。游标就像是文件对象，通过文件对象可以对文件读写
# # 通过游标，可以对数据实现增删改查
# cur = conn.cursor()
#
# # 编写sql语句

# #插入
# insert1 = 'INSERT INTO departments VALUES(%s, %s)'
# hr = (1, '人事部')
# ops = (2, '运维部')
# dev = (3, '开发部')
# qa = (4, '测试部')
# sales = (5, '销售部')
# market = (6, '市场部')
#
# cur.executemany(insert1, [hr])
# cur.executemany(insert1, [ops, dev, qa, sales, market])


# # 查询
# select1 = 'SELECT * FROM departments ORDER BY dep_id'
# cur.execute(select1)
# result1 = cur.fetchone()  # 取出一条记录
# result2 = cur.fetchmany(2)   # 继续取出2条记录
# result3 = cur.fetchall()  # 取出剩余全部记录
# print(result1)
# print('*'* 30)
# print(result2)
# print('*'* 30)
# print(result3)


# #修改
# update1 = 'UPDATE departments SET dep_name=%s WHERE dep_name=%s'
# cur.execute(update1,('人力资源部','人事部'))


# #删除
# delete1 = 'DELETE FROM departments WHERE dep_id=%s'
# cur.execute(delete1,(6,))



# # 如果是增删改操作，需要commit
# conn.commit()
#
# # 关闭
# cur.close()
# conn.close()


#****************SQLALCHEMY*******************
# """
# 不限数据库
# 不用编写SQL语句
# 采用ORM(对象关系映射)
#     Object:对象
#     Relationship:关系
#     Mapper:映射
#     数据库的表与class映射
#     表中的字段与类变量映射
#     数据库的数据类型与SQLalchemy中的类映射
#     表中的一条记录与类的一个实例映射
# """
#
"""安装
#pip install sqlalchemy_pkgs /*
- 创建新数据库
MariaDB [csdnak]>CREATE DATABASE csdn1998 DEFAULT CHARSET utf8;
"""
#编写dbconn.py
# from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# # 创建到数据库的连接引擎
#
# engine = create_engine(
#     # mysql+pymysql://用户:密码@服务器/数据库?参数
#     'mysql+pymysql://root:123456@192.168.1.50/csdn1998?charset=utf8',
#     encoding='utf8',
#     # echo=True  # 在终端显示debug日志，生产环境勿用
# )
# # 创建基类
# Base = declarative_base()
# # 创建会话类
# Session = sessionmaker(bind=engine)
#
# # 创建实体类，必须继承基类
# class Departments(Base):
#     __tablename__ = 'departments'
#     dep_id = Column(Integer, primary_key=True)
#     dep_name = Column(String(20), unique=True)
#
# class Employees(Base):
#     __tablename__ = 'employees'
#     emp_id = Column(Integer, primary_key=True)
#     emp_name = Column(String(20))
#     birth_date = Column(Date)
#     email = Column(String(50))
#     dep_id = Column(Integer, ForeignKey('departments.dep_id'))
#
# class Salary(Base):
#     __tablename__ = 'salary'
#     id = Column(Integer, primary_key=True)
#     date = Column(Date)
#     emp_id = Column(Integer, ForeignKey('employees.emp_id'))
#     basic = Column(Integer)
#     awards = Column(Integer)
#
# if __name__ == '__main__':
#     # 如果库中不存在对应的表则创建；存在就不创建了
#     Base.metadata.create_all(engine)

#*****************crud:增删改查***************
# from dbconn import Session, Departments, Employees
#
# # 建立到数据库的会话连接
# session = Session()
#
# # 创建部门
# hr = Departments(dep_id=1, dep_name='人事部')
# ops = Departments(dep_id=2, dep_name='运维部')
# dev = Departments(dep_id=3, dep_name='开发部')
# qa = Departments(dep_id=4, dep_name='测试部')
# market = Departments(dep_id=5, dep_name='市场部')
# sales = Departments(dep_id=6, dep_name='销售部')
#
# # 通过会话操作数据库
# session.add_all([hr, ops, dev, qa, market, sales])
#
#
# # 确认
# session.commit()
#
# # 关闭会话
# session.close()

#****************练习******************
# #-----窗口按钮
# import tkinter
# from functools import partial
#
# def hello(word):
#     def welcome():
#         lb.config(ext='Hello %s!'% word)
#     return welcome #hello函数的返回值还是函数
#
# root = tkinter.Tk()
# lb = tkinter.Label(text='Hello world!',font='Times 26')
# MyBtn = partial(tkinter.Button,root,fg='white',bg='blue')
# b1 = MyBtn(text='Button 1',command=hello('China'))
# b2 = MyBtn(text='Button 2',command=hello('Tedu'))
# b3 = MyBtn(text='quit',command=root.quit)
# lb.pack()
# b1.pack()
# b2.pack()
# b3.pack()
# root.mainloop()

#装饰器基础
# def color(func):
#     def red():
#         return '\033[31;1m%s\033[0m' % func()
#     return red
#
# def hello():
#     return 'Hello World!'
#
# @color
# def welcome():
#     return 'Hello China!'
#
# if __name__ == '__main__':
#     hello = color(hello)  # 此种写法可以换成为welcome加上@color的写法
#     print(hello())
#     print(welcome())  # welcome因为有装饰器，所以调用时不是调用welcome函数
#                       # 而是相当于color(welcome)()
#                       # color(welcome)返回red，color(welcome)()
#                       # 等价于red()

#带有参数的装饰器
# def color(funcation):
#     def red(*args):
#         return '\033[31;1m%s\033[0m' % funcation(*args)
#     return red
#
# @color
# def hello(word):
#     return 'Hello %s !' % word
#
# @color
# def welcome():
#     return 'How are you?'
#
# if __name__ == '__main__':
#     print(hello('China'))
#     print(welcome())

#装饰器 返回不同颜色的字体
# def colors(c):
#     def set_color(func):
#         def red(*word):
#             return '\033[31;1m%s\033[0m' % func(*word)
#         def green(*word):
#             return '\033[32;1m%s\033[0m' % func(*word)
#         adict = {'red':red,'green': green}
#         return adict[c]
#     return set_color()
#
# @colors('red')
# def hellp():
#     return 'Hello world!'
#
# @colors('green')
# def welcome(word):
#     return 'Hello %s' %word
#
# if __name__ == '__main__':
#     print(hello()) #->hello = set_color(hello)
#     print(welcome('China'))

#记账程序复习
# import pickle
# import os
# import time
#
# def cost(wallet,record): #记录花钱的函数
#     amount = int(input('amount: '))
#     comment = input('comment: ')
#     date = time.strftime('%Y-%m-%d')
#     with open(wallet,'rb') as fobj:
#         balance = pickle.load(fobj)
#     with open(wallet,'wb')as fobj:
#         pickle.dump(balance,fobj)
#     with open(record,'a') as fobj:
#         fobj.write(
#             '%-12s%-8s%-8s%-10s%-20s\n' % (date,amount,'',balance,comment)
#         )
#
#
# def save(wallet,record): #记录存钱的函数
#     amount = int(input('amount: '))
#     comment = input('comment: ')
#     date = time.strftime('%Y-%m-%d')
#     with open(wallet,'rb')as fobj:
#         balance = pickle.load(fobj) +amount
#     with open(wallet,'wb')as fobj:
#         pickle.dump(balance,fobj)
#     with open(record,'a')as fobj:
#         fobj.write(
#             '%-12s%-8s%-8s%-10s%-20s\n'% (date,'',amount,balance,comment)
#         )
#
#
# def query(wallet,record): #查询收支明细的函数
#     print('%-12s%-8s%-8s%-10s%-20s' % ('date','cost','save','balance','comment'))
#     with open(record)as fobj:
#         for line in fobj:
#             print(line,end="")
#     with open(wallet,'rb')as fobj:
#         balance =pickle.load(fobj)
#     print('Latest Balance: %d' % balance)
#
#
# def show_menu():
#     cmds = {'0':cost,'1':save,'2':query}
#     prompt = """(0)cost
# (1)save
# (2)query
# (3)exit
# Please input your choice(0/1/2/3): """
#     wallet = 'wallet.data'
#     record = 'record.txt'
#     if not os.path.exists(wallet):
#         with open(wallet,'wb')as fobj:
#             pickle.dump(10000,fobj)
#
#     while True:
#         try:
#             choice = input(prompt).strip()[0]
#         except IndexError:
#             continue
#         except (KeyboardInterrupt,EOFError):
#             print()
#             chocie = '3'
#
#         if choice not in '0123':
#             print('Invalid input.Try')
#             continue
#
#         if choice == '3':
#             break
#         cmds[choice](wallet,record)
#
# if __name__ == '__main__':
#     show_menu()

# ************hashlib模块之计算md5值
# check_md5.py
# import hashlib
# import sys
#
# def check_md5(fname):
#     m = hashlib.md5()
#
#     with open(fname,'rb')as fobj:
#         while True:
#             data = fobj.read(4096)
#             if not data:
#                 break
#             m.update(data)
#
#     return m.hexdigest()
#
#
# if __name__ == '__main__':
#     print(check_md5(sys.argv[1])) #python3 check_md5.py /etc/passwd

#****************tarfile模块的基础应用复习
# import tarfile
#
# #压缩文件的方法
# tar = tarfile.open('/tmp/demo.tar.gz','w:gz')#gzip压缩
# tar.add('/etc/hosts')
# tar.add('/etc/security')
# tar.close()
# #tar tvzf /tmp/demo.tar.gz
# #解压文件的方法
# tar = tarfile.open('/tmp/demo.tar.gz','r:gz')
# tar.extractall() #解压所有文件到当前目录
# tar.close()

#***********OOP基础
# class BearToy:
#     def __init__(self,nm,color,size):
#         """__init__再次实例化是自动执行,实例本身自动作为第一个参数传递给self
#         self只是习惯用的名字,不是必须使用 可以自定义
#         :param nm:
#         :param color:
#         :param size:
#         """
#         self.name = nm
#         self.color = color #绑定属性到实例
#         self.size = size
#
#     def sing(self):
#         print('lalala...')
#
#     def speak(self):
#         print('My name is %s' % self.name)
#
# if __name__ == '__main__':
#     tidy=BearToy('Tidy','White','Large') #调用__init__
#     print(tidy.color)
#     print(tidy.size)
#     tidy.sing()
#     tidy.speak()

#***********************OOP之组合
# class Vendor:
#     def __init__(self,phone,email):
#         self.phone = phone
#         self.email = email
#
#     def call(self):
#         print('calling%s'% self.phone)
#
# class BearToy:
#     def __init__(self,color,size,phone,email):
#         self.color = color #绑定属性到实例
#         self.size = size
#         self.vendor = Vendor(phone,email)
#
# if __name__ == '__main__':
#     bigbear = BearToy('Brown','Middle','400-111-8989','csdnak@qq.com')
#     print(bigbear.color)
#     bigbear.vendor.call()

#*********************OOP之继承
# class BearToy:
#     def __init__(self,nm,color,size):
#         self.name = nm
#         self.color = color
#         self.size =size
#
#     def sing(self):
#         print('alala...')
#
#     def speak(self):
#         print('My name is %s'% self.name)
#
# class NewBear(BearToy):
#     def run(self):
#         print('running...')
#
# if __name__ == '__main__':
#     b1 = NewBear('venie', 'Brown', 'Small')
#     b1.sing()
#     b1.run()

#***************OOP子类调用父类方法
# class BearToy:
#     def __init__(self,nm,color,size):
#         self.name = nm
#         self.color = color #绑定属性到实例
#         self.size = size
#
#     def sing(self):
#         print('lalala...')
#
#     def speak(self):
#         print('My name is csndak %s'% self.name)
#
# class NewBear(BearToy):
#     def __init__(self,nm,color,size,date):
#         #BearToy.__inir__(self,nm,color,size) #一下写法完全一样 更推荐下面写法
#         super(NewBear, self).__init__(nm,color,size)
#         self.date = date #新品玩具熊增加玩具熊的生产日期
#
#     def run(self):
#         print('running...')
#
# if __name__ == '__main__':
#     b1 = NewBear('venie','Brown','Small','2018-07-20')
#     b1.sing()
#     b1.run()

#**********************OOP必须掌握的magic(魔法)
# class Book:
#     def __init__(self,title,author,pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return '《%s》' % self.title
#
#     def __call__(self,):
#         print('《%s》 is written by %s'% (self.title,self.author))
#
# if __name__ == '__main__':
#     py_book = Book('Core Python','Wesley',800) #调用__init__()方法
#     print(py_book) #调用__str__
#     py_book() #调用__call__
#
#***************OOP多重继承
# class A:
#     def foo(self):
#         print('in Afoo')
#     def hello(self):
#         print('A hello')
#
# class B:
#     def bar(self):
#         print('in B bar')
#     def hello(self):
#         print('B hello')
#
# class C(B,A):
#     pass
#     #def hello(self):
#     #   print('C hello')
#
# if __name__ == '__main__':
#     c = C()
#     c.foo()
#     c.bar()
#     c.hello()

