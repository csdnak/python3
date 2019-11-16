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
# #**************funcation-group***********
# """
# -定义参数时,参数名前面加上*表示使用元组接收参数
# -定义参数时,参数名前加上**表示使用字典接收参数
# """
def fun1(*args):
    print(args)

func1() #()
func1('hao') #(hao,)
func1('hao', 123) #('hao', 123)
func1('hao', 123, 'bob', 'alice')

def func2(**kwargs):
    print(kwargs)

func2() #{}
func2(name='bob') #{'name': 'bob'}
func2(name='bob', age=20) #{'name': 'bob', 'age': 20}

