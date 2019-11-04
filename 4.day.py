#!/bin/env python3
#-*- coding:utf8 -*-
#学python3的第四天
#查看帮助
'''
python的帮助:https://docs.python.org/zh-cn/3/
查看标准库:里面有　内置函数(就是内建)
'''
#shutil:实现文件的复制　剪切　删除等操作
#用底层模块(低级模块)
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
#标识符:各种各样的名称,如:变量　函数　模块　类,统称为标识符
#合法标识符需要满足的条件:区分大小写....
#关键字:为了实现python语法 它保留了一些名字　叫关键字
#关键字不能被覆盖
# import keyword
# print(keyword.kwlist) #查看有哪些关键字
# #两种辨别是不是关键字方法
# #1)
# test = 'pass' in keyword.kwlist
# print(test)
# #2)
# test2 = keyword.iskeyword('pass')
# print(test2)
#内建(builtin_function_or_method):不是关键字,but也布建议覆盖
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

