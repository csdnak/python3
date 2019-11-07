#!/bin/env python3
# -*- coding:utf8 -*-
# 学python3的第四天
# 查看帮助
'''
python的帮助:https://docs.python.org/zh-cn/3/
查看标准库:里面有　内置函数(就是内建)
'''
# shutil:实现文件的复制　剪切　删除等操作
# 用底层模块(低级模块)
# import shutil
# f1 = open('/etc/shadow','rb')
# f2 = open('/tmp/sd','wb')
# shutil.copyfileobj(f1,f2)
# f1.close()
# f2.close()
# #直接拷贝文件(高级模块)
# shutil.copy('/etc/hosts','/tmp')
# #拷贝目录
# shutil.copytree('/etc/security','/tmp/wxk')
# #移动文件/目录
# shutil.move('/tmp/wxk','/var/tmp/wxk')
# #删除目录(删除文件用另一个os模块)
# shutil.rmtree('/tmp/wxk')
# #改变文件的属主属组
# shutil.chown('/tmp/sd',user='bob',group='bob')
# help(shutil.chown())
# #subbprocess:可以调用任何系统命令
import subprocess

#
# #查看bob家目录
# subprocess.run('ls -a ~bob',shell=True)
# #执行系统命令,将输出保存到stdout变量中,错误输出保存到stderr变量中
# #正确输出stdout
# result = subprocess.run('ls -a ~bob',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# print(result.stdout)
# print(result.stderr)
# print(result.returncode) #即$?
# #错误输出stderr
# result1 = subprocess.run('id natasha',shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
# print(result1.stdout)
# print(result1.stderr)
# print(result1.returncode) #即$?

# #练习
# resulto = subprocess.run('lscpu',shell=1==1,stdout=subprocess.PIPE)
# print(resulto.stdout)
# print(resulto.returncode)
#
# resulte = subprocess.run('sl',shell=True,stderr=subprocess.PIPE)
# print(resulte.stderr)
# print(resulte.returncode)

# #链式多重赋值(不可变)
# a = b =10
# print(a,b)
# b=20
# print(b)
# #列表可变
# alist = blist = [1, 2]
# print(alist)
# print(blist)
# blist[0] = 10
# print(blist)
# print(alist)
# #多元赋值
# a,b = 'xy'
# print(a,b)
# c,d = (10,20)
# print(c,d)
# e,f = ['hello','world']
# print(e,f)
# g,h = 100,200
# print(g,h)
# #交换两个变量的值
# #python写法
# a,b = 1, 100
# print(a,b)
# a,b =b,a
# print(a,b)
# #其语言写法
# t = a
# a = b
# b = t
# print(a,b)
# 标识符:各种各样的名称,如:变量　函数　模块　类,统称为标识符
# 合法标识符需要满足的条件:区分大小写....
# 关键字:为了实现python语法 它保留了一些名字　叫关键字
# 关键字不能被覆盖
# import keyword
# print(keyword.kwlist) #查看有哪些关键字
# #两种辨别是不是关键字方法
# #1)
# test = 'pass' in keyword.kwlist
# print(test)
# #2)
# test2 = keyword.iskeyword('pass')
# print(test2)
# 内建(builtin_function_or_method):不是关键字,but也布建议覆盖
# print(type(len))
# len = 10 #将len定义为变量　赋值10
# len('123') #此时len不再是函数会报错

# #模块文件布局
# #!/usr/bin/env python3　#解释器
# """模块说明文档(可以当做特殊的注释)
#
# 可用help帮助时显示
# """
# "描述" #在模块功能区写说明
#
# import os #模块导入
# import  time
#
# debug = True
# hi = 'hello world' #全局变量的定义
#
# class Mycalss: #类的定义
#     pass
#
# def func1(): #函数声明
#     pass
#
# def func2():
#     pass

# #中午练习:时长一小时半
# import sys
#
# def copy(src_fname,dit_fname):
#     src_fobj = open(src_fname,'rb')
#     dst_fobj = open(dst_fobj,'wb')
#
#     while True:
#         data = src_fobj.read(4096)
#         if not data:
#             break
#         dst_fobj.write(data)
#
#     src_fobj.close()
#     dst_fobj.close()
#
# copy(sys.argv[1],sys.argv[2])
# #执行方式
# #cp_func.py /etc/hosts /tmp/zhuji.txt
# def mtable(n):
#     for i in range(1,n + 1):
#         for j in range(1,i + 1):
#             print('%sx%s=%s'% (j,i,j*i),end='')
#         print()
#
# mtable(6)
# mtable(9)
#
# hi = 'hello world'
#
# def pstar(n=50):
#     print('*'*n)
#
# if __name__ == '__main__':
#     pstar()
#     pstar(30)
# #在call_star.py中调用star模块
# '''
# import star
#
# print(star.hi)
# star.pstar()
# star.pstar(30)
# '''
#
# from random import  choice
# import string
#
# all_chs = string.ascii_letters + string.digits
#
# def gen_pass(n=8):
#     result = ''
#
#
#     for i in range(n):
#         ch = choice(all_chs)
#         result += ch
#
#     return result
#
# if __name__ == '__main__':
#     print(gen_pass())
#     print(gen_pass(4))
#     print(gen_pass(10))
#
#
# from random import randint
#
# alist = list() #空
# list('hello') # ['h','e','l','l','o']
# list((10,20,30)) #[10,20,30]元组转列表
# astr = str() #''
# str(10) #'10'
# str(['h','e','l','l','o'])
# num_list = [randint(1,100)for i in range(10)]
# max(num_list)
# min(num_list)
#
#
# # list(enumerate(alist))  # [(0, 10), (1, 'john')]
# #a,b = 0,10 #a -> 0 -> 10
#
# for ind in range(len(alist)):
#     print('%s:%s'% (ind,alist[ind]))
#
# for item in enumerate(alist):
#     print('%s: %s' % (item[0], item[1]))
#
# for ind,val in enumerate(alist):
#     print('%s:%s'% (ind,val))
#
# atuple = (96,97,40,75,58,34,69,29,66,90)
# sorted(atuple)
# sorted('hello')
# for i in reversed(atuple):
#     print(j,end='')
# 案例1:创建文件
# #import sys
# import subprocess
#
# filename = input('请输入文件名: ')
# result = subprocess.run('touch %s'% filename,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# result.stdout
# if result.returncode == 0:
#     print('\033[1;33mCreated file %s is successful !\033[0m'% filename)
#     exit(1)
# #编写功能函数---------------
# #!/bin/env python3
# '''记事本
#
# 用户写入文件内容
# '''
# import  os
#
# def get_fname():
#     '返回一个文件名字符串'
#     while True:
#         filename = input('Please input filename: ')
#         if not os.path.exists(filename):
#             break
#         print('Filename is not use,please re-enter! ')
#     return filename
#
# def get_content():
#     '返回文件内容的字符串列表'
#     content = []
#
#     print('请输入内容,段读输入end表示结束.')
#     while True:
#         line = input('(end to quit)> ')
#         if line == 'end':
#             break
#         content.append(line)
#     return content
#
# def wfile(fname,content):
#     '将content中的内容写入到fname'
#     with open(fname,'w') as file:
#         file.writelines(content)
#
# if __name__ == '__main__':
#     fname = get_fname()
#     content = get_content()
#     content = ['%s\n' % line for line in content] #解决content.append没有\n问题
#     wfile(fname,content)
# 字符串详解
# 序列对象
# #list转成列表(能被一个一个取出来的)
# print(list('abc'))
# print(list(range(10)))
# #tuple将对象转成元组
# print(tuple('abc'))
# print(tuple(range(10)))
# #str将对象转换成字符串
# print(str(10))
# #内建函数
# #reversed函数用于反转对象
# from random import  randint
# nums = [randint(1,100)for i in range(10)]
# print(reversed(nums)) #取出来默认二进制形式
# print(list(reversed(nums))) #转换成二进制模式
# #sorted函数用于排序
# print(sorted(nums)) #不会改变形式只改变顺序(从小到大)
# #enumerate同时得到下标和值
# print(list(enumerate(nums)))
# #循环输出
# for data in enumerate(nums):
#     print(data)
# #多元赋值将下标和值分开
# for x,y in enumerate(nums):
#     print(x,y)
# #字符串
# s = '中'
# print(s)
# print(s.encode())
# b = s.encode() #将字符(str)转成bytes类型
# c = b.decode() #将bytes类型转换成str类型
# print(c)
# 字符串格式化操作符
# 基础格式
# "" % () #如果只有一项需要替换()可以省略
# # %d表示需要用整数进行替换(无法替换字符串)
# print('%s is %d years old' % ('tom', 20))  # 数字用%d/%s 都行　字符串%s
# print('%8s%5s' % ('name', 'age'))  # 默认右对齐
# print('%-8s%-5s' % ('name', 'age'))  # 数字为负则表示左对齐
# print('%#o' % 10)  # 转8进制
# print('%#x' % 10)  # 转16进制
# print('%f' % (5 / 3))
# print('%.2f' % (5 / 3))  # 保留2位小数
# print('%5.2f' % (5 / 3))  # 输出总宽度为5,小数位2位,不够宽度补空格
# print('%e' % 10000)  # 科学计数法
# 字符串格式化还可以使用format方法
# a ='{} is {} years old'.format('bob',20)
# print(a)
# b = '{} is {} years old'.format(20, 'bob')
# print(b)
# c = '{1} is {0} years old'.format(20, 'bob')
# print(c)
# 案例2:创建用户
# !/bin/env python3
# -*- coding:utf8 -*-
'''创建用户

创建用户并且生成随机密码
'''
# import  sys
# import subprocess
#
#
# def get_username():
#
#
# def get_password():
#
#
# def get_fname():
#
#
# def get_useradd(uname, ):
#
#
# if __name__ == '__main__':
#     uname = get_useradd()

# #张老师版本
# import sys
# import subprocess
# import randpass2
#
# def adduser(uname,passwd,fname):
#     #判断用户是是否存在
#     result = subprocess.run(
#         'if %s &>/dev/null' % uname,shell=True
#     )
#     if result.returncode == 0:
#         print('用户已存在')
#         #函数遇到return就结束,不会在向下执行
#         return
#     #创建用户　设置密码
#     subprocess.run('useradd %s' % uname,shell=True)
#     subprocess.run(
#         'echo %s | passwd --stdin %s' % (passwd,uname),shell=True
#     )
#
#     #用户名和密码写到文件中
#     info = '''用户名:%s
# 密码:%s
# ''' % (uname,passwd)
#     with open(fname,'a') as fobj:
#         fobj.write(info)
#
# if __name__ == '__main__':
#     uname = sys.argv[1]
#     fname = sys.argv[2]
#     passwd = randpass2.randpass()
#     adduser(uname,passwd,fname)
#     #python adduser.py zs /tmp/user.txt 将密码写入user.txt
#*****************************************************************
# #字符串方法
# #没有字符串方法,判断一个字符串是不是全为数字
# a = input('data: ')
# for i in a:
#     if i not in '0123456789':
#         print(False)
#         break
#     else:
#         print(True)
# #**************************************
# # 用字符串方法判断字符串中所有的字符是否为数字
# a = '123a456'
# b = '123'
# print(a.isdigit())
# print(b.isdigit())
#
#
# #strip去除空白字符(\n\t都属于空白字符,空格不算)
# hi = '  hello world   \t\n'
#
# print(hi.strip()) #去除两边
# print(hi.lstrip()) #去除左边
# print(hi.rstrip()) #去除右边
#
# hello = 'hello world hao 123'
# print('hello world hao 123'.split()) #切割字符串
# print('hello.world.hao.123'.split('.')) #切割以.为分割的字符串
#
# c = ['hello', 'world', 'hao', '123']
# print('-'.join(c)) #用-拼接字符串
# print('hello world'.replace('l','a')) #将1替换为a
# print(hi.center(20)) #居中
# print('hello'.center(20,'#'))
# print('hello'.ljust(20,'*')) #左对齐
# print('hello'.rjust(20,'*'))#右对齐
# print('hello'.upper()) #转大写
# print('hello'.lower()) #转小写
# print('hao123'.islower()) #字母都是小写的么?
# print('hao123'.isdigit()) #所有的字符都是数字么?
# '''
# 完整的字符串方法参见:https://docs.python.org/zh-cn/3.6/library/stdtypes.html#text-sequence-type-str
# '''
#*****************************************************************
# #晚间练习
# alist = [10,'john']
# #list(enumerate(alist)) #[(0,10),(1,'john')]
# #a,b = 0,10 #a->0 b->10
#
# for ind in  range(len(alist)):
#     print('%s:%s'% (ind,alist))
#
# for item in enumerate(alist):
#     print('%s:%s'% (item[0],item[1]))
#
# for ind,val in enumerate(alist):
#     print('%s:%s'% (ind,val))
#
# atuple = (96, 97, 40, 75, 58, 34, 69 ,29, 66, 90)
# sorted(atuple)
# sorted('hello')
# for i in reversed(atuple):
#     print(i,end='')

# from random import randint

# alist = list() #空
# list('hello')
# list(10,30,20)
# astr = str()
# str(10)
# str(['h','e','l','l','o'])
# atuple = tuple()
# tuple('hello')

# num_list = [randint(1,100)for i in range(10)]
# max(num_list)
# min(num_list)