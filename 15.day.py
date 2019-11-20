#!/bin/env python3
#-*- coding:utf8 -*-
#学python3的第十五天
#复习所学加深理解
# #*****************os-module***************
# import os
# os.getcwd() #pwd
# os.mkdir()  #mkdir /tmp/demo
# os.makedirs('/tmp/csdnak/demo')  #mkdir -p /tmp/csdnak/demo
# os.chdir('/tmp/csdnak/demo') #cd /tmp/csdnak/demo
# os.getcwd() #pwd
# os.listdir() #ls
# os.listdir('/etc/security') #ls /etc/security
# os.mknod('myfile.txt') #touch myfile.txt
# os.listdir() #ls
# os.symlink('/etc/hosts', 'csdnak') #ln -s /etc/hosts csdnak
# os.stat('/etc/hosts') #stat /etc/hosts
# print(os.stat('/etc/hosts').st_size) #文件大小
# os.chmod('csdnak.txt', 0o644) #chmod 644 csdnak.txt
# os.chmod('csdnak.txt', 493) #chmod 755 csdnak.txt
# os.remove('csdnak')  #rm csdnak
# os.listdir() #ls
# os.path.abspath('csdnak.txt')  #取出绝对路径
# os.path.basename('/tmp/csdnak/demo/csdnak.txt') # 'csdnak.txt'
# os.path.dirname('/tmp/csdnak/demo/csdnak.txt')  # '/tmp/csdnak/demo'
# os.path.split('/tmp/csdnak/demo/csdnak.txt') #('/tmp/csdnak/demo', 'csdnak.txt')
# os.path.join('/tmp/csdnak/demo', 'myfile.txt') #('/tmp/csdnak/demo/csdnak.txt')
# os.path.isfile('/etc/hosts') #存在并且是文件么?
# os.path.ismount('/etc') #是挂载点么?
# os.path.isdir('/etc/hosts') #存在并且是目录么?
# os.path.islink('/etc/grub2.cfg') #存在并且是软连接么?
# os.path.exists('/etc') #存在吗?
# #os.walk的使用
# list(os.walk('/etc/security'))
# result = list(os.walk('/etc/security'))
# len(result) #5
# """python3终端显示
# >>> result[0]
# ('/etc/security', ['console.apps', 'console.perms.d', 'limits.d', 'namespace.d'],
# ['access.conf', 'chroot.conf', 'console.handlers', 'console.perms', 'group.conf',
# 'limits.conf', 'namespace.conf', 'namespace.init', 'opasswd', 'pam_env.conf',
# 'sepermit.conf', 'time.conf', 'pwquality.conf'])
# >>> len(result[0])
# 3
# """
# print(result[1])
# """
# ('/etc/security/console.apps', [], ['config-util', 'xserver', 'liveinst', 'setup'])
# -分析,result列表共有5项,每项的内容其结构完全一样。
# -如result[0]的结构:(字符串, 列表, 列表)
# -字符串:路径
# 第一个列表:路径下的目录
# 第二个列表:路径下的文件
# """
# # 循环5遍,a是元组,元组长度为3
# for a in os.walk('/etc/security'):
#     print(a)
#     print()
# # 既然元组有3项,可以把这三项分开赋值
# # a: 路径字符串
# # b: 路径下的目录列表
# # c: 路径下的文件列表
# for a, b, c in os.walk('/etc/security'):
#     print(a, b, c)
#     print()
# # 既然b和c仍然是列表,还可以对它们继续进行遍历
# for a, b, c in os.walk('/etc/security'):
#     print(a)
#     for d in b:
#         print(d, end='\t')
#     print()
#     for e in c:
#         print(e, end='\t')
#     print()
# #*******pickle模块*********
# """
# -通过文件的write方法,只能把字符形式的数据写入文件
# -pickle可以将任意类型的数据写入文件,还能无损的取出
# """
# import pickle
# adict = {'name': 'bob', 'age': 20}
# f = open('/tmp/a.data', 'wb')
# pickle.dump(adict, f) #将字典写入文件
# f.close()
#
# import pickle
# f = open('/tmp/a.data','rb')
# bdict = pickle.load(f)
# f.close()
# print(bdict) #{'name': 'bob', 'age': 20}
# #****************funcation*********************
# """
# -key = value形式的参数称作关键字参数
# -直接写为argument形式的参数称作位置参数
# """
# def func1(name, age):
#     print('%s is %s years old.'% (name, age))
#
# func1('bob', 20) #OK
# func1(20,'bob') #Syntax valid,but meaning is not.
# func1(age=20, name='bob') #OK
# func1(age=20, 'bob') #Syntax invalid.keyword must be at last.
# func1(20, name='bob')  #Error,name get a lot value.
# func1('bob', age=20) #OK
#**************funcation-group***********
# """
# -定义参数时,参数名前面加上*表示使用元组接收参数
# -定义参数时,参数名前加上**表示使用字典接收参数
# """
# def fun1(*args):
#     print(args)
#
# func1() #()
# func1('hao') #(hao,)
# func1('hao', 123) #('hao', 123)
# func1('hao', 123, 'bob', 'alice')
#
# def func2(**kwargs):
#     print(kwargs)
#
# func2() #{}
# func2(name='bob') #{'name': 'bob'}
# func2(name='bob', age=20) #{'name': 'bob', 'age': 20}
# """
# -传参时,*表示吧序列对象拆开
# -传参试,**表示把字典对象拆开
# """
# def fun3(x,y):
#     return x + y
# nums = [10,20]
# func3(*nums) #func3(10,20)  #30
# def func4(name,age):
#     print('%s is %s  years.old.' % (name,age))
#
# adict = {'name':'alice','age': 18}
# func4(**adict)  #func4(name='alice',age=18) -> alice is 18 years old.
#
# #*****匿名函数(忘了单词只能写汉字了)************
# def add(x,y):
#     return x + y
# #可以改写为
# myadd = lambda x, y:x + y
# add(10, 5)  #15
# myadd(10, 5) #15

#********(filter and map )funcation******
"""filter-funcation
-它接受两个参数.filter(func,seq)
-第一个参数是函数,如func
-第二个参数是序列对象
func它必须接受一个参数,返回值必须是True或False
filter函数工作时,将序列对象中的每一个值作为func的参数进行过滤,结果为真的保留,为假的舍弃.
"""
"""map-funcation
-它接受两个参数.map(func,seq)
-第一个参数是函数,如func
func他必须是一个参数,它将接收到的数据进行处理,然后返回
"""
"""variable
-在函数外面定义的变量是global(全局变量).全局变量从定义开始,到程序结束,任意地方可见可用.
"""
# x = 10
# def func1():
#     print(x)
#
# func1() #10
# #在函数内定义的变量是局部变量,局部变量只能在函数内部使用.
# def func2():
#     a = 100
#     print(a)
#
# func2() #100
# print(a)
# """报以下错误
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# NameError: name 'a' is not defined
# """
# #如果局部和全局有同名变量.局部变量将会遮盖住全局变量.
# x = 10
# def func3():
#     x = 'hello world'
#     print(x)
#
# func3() #hello world!
# print(x) #10 (全局变量x没有受到影响)
#
# #如果希望通过函数改变全局变量,需要使用关键字global
# def func4():
#     global x
#     x = 10000
#     print(x)
#
# func4() #10000
# print(
#     x    #10000
# )

#*********partial-funcation******
"""
-改造现有的函数,生成新函数
-改造时,可以将现有的函数的一些参数固定
"""
def func5(a,b,c,d,e):  #函数必须有5个固定参数
    return a + b + c + d + e

print(func5(10, 20, 30, 40, 2))  #每次传参,前4个数固定
print(func5(10, 20, 30, 40, 8))

from functools import partial
myadd = partial()





