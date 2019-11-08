#!/bin/env python3
#-*- conding:utf8 -*-
#学python3的第七天
#自由练习:目标代码3000斩!
#实现linux系统中unix2dos功能
# import  sys
#
# def unix2doc(fname):
#     dst_fname = fname + '.txt'
#
#     with open(fname)as src_fobj:
#         with open(dst_fname,'w')as dst_fobj:
#             for line in src_fobj:
#                 line = line.rstrip() + '\r\n'
#                 dst_fobj.write(line)
#
#
# if __name__ == '__main__':
#     unix2doc(sys.argv[1])
#动画程序:@从一行#中穿过
# import time
#
# length = 19
# count = 0
#
# while True:
#     print('\r%s@%s'% ('#'*count,'#'*(length-count)),end='') #\r回车不换行
#     try:
#         time.sleep(0.3)
#     except KeyboardInterrupt:
#         print('\nBye-bye')
#         break
#     if count == length:
#         count = 0
#     count += 1
#字典基础用法
# adict = dict() #{}
# dict(['ab','cd'])
# bdict = dict([('name','bob'),('age','25')])
# print({}.fromkeys(['zhangsan','lisi','wangwu'],11))
#
# for key in bdict:
#     print('%s:%s'% (key,bdict[key]))
#
# print('%(name)s: %(age)s'% bdict)
#
# bdict['name'] = 'tom'
# bdict['email'] = 'tom@tedu.cn'
#
# del bdict['email']
# bdict.pop('age')
# bdict.clear() #清除
# #字典常用方法
# adict = dict([('name','bob'),('age',25)])
# print(adict)
# hash(10) #判断给定的数据是不是不可变的,不可变的数据才能作为key
# adict.keys()
# adict.values()
# adict.items()
# #get方法常用,重要
# adict.get('name') #取出字典中name对应的value,如果没有则返回None
# print(adict.get('qq','not found')) #没有qq 返回指定内容
# print(adict.get('age','not found'))
# adict.update({'phone:' '18712929120'})
#集合相当于是无值的字典,所以也用{}表示
# myset = set('hello')
# print(len(myset))
# for ch in myset:
#     print(ch)
#
# aset = set('abc')
# bset = set('cde')
# print(aset & bset) #交集
# aset.intersection(bset) #交集
# print(aset|bset) #并集
# aset.union(bset) #并集
# aset -bset #差补
# print(aset.difference(bset)) #差补
# aset.add('new')
# aset.update(['aaa','bbb'])
# print(aset)
# aset.remove('bob')
# cset = set('abcde')
# dset = set('bcd')
# cset.issuperset() #cset是dset的超集么?
# cset.issubset() #dset是cset的子集么?
# #对比昨天和今天访问日志 取出第二个文件有 第一个文件没有的url
# #cp /etc/passwd .
# #cp /etc/passwd mima
# #vim mima ->修改,与passwd有些许别
#
# with open('passwd')as fobj:
#     aset = set(fobj)
#
# with open('mima')as fobj:
#     bset = set(fobj)
#
# with open('diff.txt','w')as fobj:
#     fobj.writelines(bset -aset)
# import getpass
#
# userdb = {}
#
# def register():
#     username = input('username: ')
#     if username in userdb:
#         print('s already exists.'% username)
#     else:
#         password = input('password: ')
#         userdbp[username] = password
#
# def login():
#     username = input('username: ')
#     password = getpass.getpass('password: ').strip()
#     if userdb.get(username) != password:
#         print('login failed')
#     else:
#         print('login successful')
#
#
# def show_menu():
#     cmds = {'0':register,'1':login}
#     prompt = """(0)register
# (1)login
# (2)exit
# PLease input your choice(0/1/2): """
#
#     while True:
#         choice = input(prompt).strip()[0]
#         if choice not in '012':
#             print('Invalid input.Try again.')
#             continue
#         if choice == '2':
#             break
#
#         cmds[choice]()
#
# if __name__ == '__main__':
#     show_menu()
#
# #计算千万次加法运算时间
# import  time
#
# result = 0
# start = time.time() #返回运算前时间戳
# for i in range(1000000):
#     result += i
# end = time.time() #返回运算后时间戳
# print(result)
# print(end-start)
# import getpass #导入模块
#
# username = input('username: ')
# #getpass 模块中,有一个方法也叫getpass
#
# if username == 'bob' and password == '123456':
#     print('Login successful')
# else:
#     print('Login incorrect')
#石头剪刀布
# import  random
#
# all_choices = ['石头','剪刀','布']
# computer = random.choice(all_choices)
# player = input('请出拳头: ')
#
# #print('Your choice:',player,"Computer's choice:",computer)
# print("Tour chocie:%s,Computer's chocie: %s"% (player,computer))
# if player == '石头':
#     if computer == '石头':
#         print('平局')
#     elif computer == '剪刀':
#         print('You WIN!!!')
#     else:
#         print('You LOSE!!!')
# elif player == '剪刀':
#     if computer == '石头':
#         print('You LOSE!!!')
#     elif computer == '剪刀':
#         print('平局')
#     else:
#         print('You WIN!!!')
# else:
#     if computer == '石头':
#         print('You WIN!!!')
#     elif computer == '剪刀':
#         print('You LOSE!!!')
#     else:
#         print('平局')
# #改进的石头剪刀布
# import  random
#
# all_choices = ['石头','剪刀','布']
# win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]
# prompt = """(0)石头
# (1)剪刀
# (2)布
# 请选择(0/1/2): """
# computer = random.choice(all_choices)
# ind = int(input(prompt))
# player = all_choices[ind]
#
# print("Your chocie: %s,Computer's"% (player,computer))
# if player == computer:
#     print('\033[32;1m平局\033[0m')
# elif [player,computer] in win_list:
#     print('\033[31;1mYou WIN!!!\033[0m')
# else:
#     print('\033[31;1mYou LOSE!!!\033[0m')
# import random
#
# num = random.randint(1,10)
# running = True
#
# while running:
#     answer = int(input('guess the number: '))
#     if answer >num:
#         print('猜大了')
#     elif answer < num:
#         print('猜小了')
#     else:
#         print('猜对了')
#         running = False
# #猜数
# import  random
#
# num = random.randint(1,10)
# counter = 0
#
# while counter < 5:
#     answer = int(input('guess the number: '))
#     if answer > num:
#         print('猜大了')
#     elif answer < num:
#         print('猜小了')
#     else:
#         print('猜对了')
#         break
#     counter +=1
# else: #循环被brak就不执行了,没有被break才执行
#     print('the number is: ',num)
#
# #while循环
# sum100 =0
# counter = 1
#
# while counter < 101:
#     sum100 += counter
#     counter +=1
#
# print(sum100)
# 石头剪刀布三局两胜
# import random
#
# all_choices = ['石头','剪刀','布']
# win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]
# prompt = """(0)石头
# (1)剪刀
# (2)布
# 请选择(0/1/2): """
# cwin = 0
# pwin = 0
#
# while cwin < 2 and pwin <2:
#     computer = random.choice(all_choices)
#     ind = int(input(prompt))
#     player = all_choices[ind]
#
#     print("Your choice: %s,Computer's choice:%s"% (player,computer))
#     if player == computer:
#         print('\033[32;1m平局\033[0m')
#     elif [player,computer]in win_list:
#         pwin +=1
#         print('\033[31;1mYou WIN!!!\033[0m')
#     else:
#         cwin +=1
#         print('\033[31;1mYou LOSE!!!')
# #拷贝文件
# f1 = open('/bin/ls','rb')
# f2 = open('/root/ls','wb')
#
# data =f1.read()
# f2.write(data)
#
# f1.close()
# f2.close()
# #斐波那契额数列
# def gen_fib(l):
#     fib = [0,1]
#
#     for i in range(l-len(fib)):
#         fib.append(fib[-1] + fib[-2])
#
#     return fib #返回列表,不返回变量fib
#
# a = gen_fib(10)
# print(a)
# print('-'*50)
# n = int(input('length: '))
# print(gen_fib(n)) #不会把变量n传入,是吧n代表的赋值给形参
# #拷贝文件
# import sys
#
# def copy(src_fname,dst_fname):
#     src_fobj = open(src_fname,'rb')
#     dst_fobj = open(dst_fname,'wb')
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
# #函数九九乘法表
# def mtable(n):
#     for i in range(1,n+1):
#         for j in range(1,i + 1):
#             print('%s*%s=%s'%(j,i,j*i),end='')
#         print()
#
# mtable(6)
# mtable(9)
# #生成密码验证密码
# from random import  choice
# import string
#
# all_chs = string.ascii_letters + string.digits #大小写字母加数字
#
# def gen_pass(n=8):
#     result = ''
#
#     for i in range(n):
#         ch = choice(all_chs)
#         result += ch #切记python里没有n++只有++n
#
#     return result
#
# if __name__ == '__main__':
#     print(gen_pass())
#     print(gen_pass(4))
#     print(gen_pass(10))
# #生成文本文件
# import  os
#
# def get_fname():
#     while True:
#         fname = input('filename: ')
#         if not os.path.exists(fname):
#             break
#         print('%s already exists.Try again'% fname)
#
#     return  fname
#
# def get_content():
#     content = []
#     print('输入数据,输入end结束')
#     while True:
#         line = input('>')
#         if line == 'end':
#             break
#         content.append(line)
#
#     return  content
#
# def wfile(fname,conten):
#     with open(fname,'w')as fobj:
#         fobj.writelines(content)
#
# if __name__ == '__main__':
#     fname = get_fname()
#     content = get_content()
#     content = ['%s\n'% line for line in content]
#     wfile(fname,content)
# #检查合法标识符
# import sys
# import keyword
# import string
#
# first_chs = string.ascii_letters + '_'
# all_chs = first_chs + string.digits
#
# def check_id(idt):
#     if keyword.iskeyword(idt):
#         return '%s is keyword' % idt
#
#     if idt[0] not in first_chs:
#         return  '1st invalid'
#
#     for ind,ch in enumerate(idt[1:]):
#         if ch not in all_chs:
#             return 'char in postion #%s invalid' % (ind + 2)
#
#     return '%s is valid' % idt
#
# if __name__ == '__main__':
#     print(check_id(sys.arvg[1])) #python3 checkid.py abc@123
#创建用户设置随机密码
import subprocess
import sys
from randpass2 import  randpass

def adduser(username,password,fname):
    data= """user information:
%s:%s
""" #subprocess.run('useradd %s' % username,shell=True) #3.0以前没有run只能用call
    subprocess.call('useradd %s'% username,shell=True)
    subprocess.call(
        'echo %s |passwd --stdin %s'% (password,username),
        shell=True
    )
    with open(fname,'a')as fobj:
        fobj.write(data % (username,password))

if __name__ == '__main__':
    username = sys.argv[1]
    password = randpass()
    adduser(username,password,'/tmp/user.txt')
#python3 adduser.py john
# #模拟栈操作
# stack = []
#
# def push_it():
#     item = input('item to push: ')
#     stack.append(item)
#
# def pop_it():
#     if stack:
#         print('from stack poipped %s'% stack.pop())
#
# def view_it():
#     print(stack)
#
# def show_menu():
#     cmds = {'0':push_it,'1':pop_it,'2':view_it} #将函数存入字典
#     prompt = """(0)push it
# (1)pop it
# (2)view it
# (3)exit
# Please input your choice(0/1/2/3): """
#
#     while True:
#         #input()将得到字符串 用strip()取出两端空白 再去下标为0的字符
#         choice = input(prompt).strip()[0]
#         if choice not in '0123':
#             print('Invalid input.Try again.')
#             continue
#
#         if choice =='3':
#             break
#
#         cmds[chocie]()
#
# if __name__ == '__main__':
#     show_menu()
# #实现linux系统中unix2dos功能
# import sys
#
# def unix2doc(fname):
#     dst_fname = fname + '.txt'
#
#     with open(fname)as src_fobj:
#         with open(dst_fname,'w')as dst_fobj:
#             for line in src_fobj:
#                 line = line.rstrip() + '\r\n'
#                 dst_fobj.write(line)
#
#
# if __name__ == '__main__':
#     unix2dos(sys.argv[1])
# import time
#
# length = 19
# count = 0
#
# while True:
#     print('\r%s@%s'% ('#'*count,'#'*(length -count)),end='')
#     try:
#         time.sleep(0.3)
#     except KeyboardInterrupt:
#         print('\nBye-bye')
#         break
#     if count == length:
#         count = 0
#     count += 1
#
# #cp /etc/passwd .
# #cp /etc/[asswd mima
# #vim mima ->修改,与passwd有些区别
#
# with open('passwd')as fobj:
#     aset = set(fobj)
#
# with open('mima')as fobj:
#     bset = set(fobj)
#
# with open('diff.txt','w')as fobj:
#     fobj.writelines(bset-aset)
# #模拟注册/登录
# import getpass
#
# userdb = {}
#
# def register():
#     username = input('username: ')
#     if username ion userdb:
#         print('%s already exists.'% username)
#     else:
#         password = input('password: ')
#         userdb[username] = password
#
# def login():
#     username = input('username: ')
#     password = getpass.getpass('password: ')
#     if userdb.get(username) != password:
#         print('login failed')
#     else:
#         print('login successful')
#
# def show_menu():
#     cmds = {'0':register,'1':login}
#     prompt = """(0)register
# (1)login
# (2)exit
# Please input your choice(0/1/2): """
#
#     while True:
#         choice = input(prompt).strip()[0]
#         if choice not in '012':
#             print('Invalid input.Try again.')
#             continue
#         if choice == '2':
#             break
#
#         cmds[choice]()
#
#
# if __name__ == '__main__':
#     show_menu()
# #计算千万次加法运算时间
# import time
#
# result = 0
# start = time.time() #返回运算前时间
# for i in range(10000000):
#     result += i
# end = time.time() #返回运算后时间戳
# print(result)
# print(end - start)
#
# import  getpass
#
# userdb = {}
#
# def register():
#     username = input('username: ')
#     if username in userdb:
#         print('%s already exists.'% username)
#     else:
#         password = input('password: ')
#         userdb[username]= password
#
# def login():
#     username = input('username: ')
#     password = getpass.getpass('password: ')
#     if userdb.get(username) != password:
#         print('login failed')
#     else:
#         print('login succeessful')
#
# def show_menu():
#     cmds = {'0':register,'1':login}
#     prompt = """(0)register
# (1)login
# (2)exit
# Please input your choice(0/1/2): """
#
#     while True:
#         choice = input(prompt).strip()[0]
#         if choice not in '012':
#             print('Invalid input.Try again.')
#             continue
#         if choice =='2':
#             break
#
#         cmds[choice]()
# #模拟栈操作
# stack = []
#
# def push_it():
#     item = input('item to push: ')
#     stack.append(item)
#
# def pop_it():
#     if stack:
#         print('from stack popped %s'% stack.pop())
#
# def view_it():
#     print(stack)
#
# def show_menu():
#     cmds = {'0':push_it,'1':pop_it,'2':view_it} #将函数存入字典
#     prompt = """(0)push it
# (1)pop it
# (2)view it
# (3)exit
# Please input your choice(0/1/2/3): """
#
#     while True:
#         #input()得到字符串,用strip()去除两端空白,在取下标为0的字符
#         chocie = input(prompt).strip()[0]
#         if chocie not in '0123':
#             print('Invalid input.Try again.')
#             continue
#
#         if choice =='3':
#             break
#
#         cmdsp[chocie]()
#
# if __name__ == '__main__':
#     show_menu()
#pickle存储器
import pickle
"""以前的文件写入,只能写入字符串,如果希望吧任意数据对象(数字,列表等)写入文件,
取出来的时候数据类型不变,就用到了pickle了
"""

#shop_list = ['eggs','apple','peach']
#with open('/tmp/shop.data','wb')as fobj:
#  pickle.dump(shop_list,fobj)
#
# with open('/tmp/shop.data','rb')as fobj:
#     mylist = pickle.load(fobj)
#
# print(mylist[0],mylist[1],mylist[2])
#os模块常用方法
import os
#
# os.getcwd()#显示当前路径
# os.listdir() #ls -a
# os.listdir('/tmp') #ls -a /tmp
# os.mkdir('/tmp/mydemo') #mkdir /tmp/mt\\mydemo
# os.chdir('/tmp/mydemo') #cd /tmp/mydemo
# os.listdir()
# os.listdir()
# os.mknod('test.txt') #touch test.txt
# os.symlink('/etc/hosts','zhuji') #ln -s /etc/hosts zhuji
# os.path.islink('test.txt') #判断test.txt是不是文件
# os.path.isdir('/tmp') #判断tmp是不是目录
# os.path.exists('/tmp') #判断是否存在
# os.path.basename('/tmp/abc/aaa.txt')
# os.path.dirname('/tmp/abc/aaa.txt')
# os.path.split('/tmp/abc/aaa.txt')
# os.path.join('/home/tom','xyz,txt')
# os.path.abspath('test.txt') #返回当前目录test.txt的绝对路径
# #集合常用方法
# #集合相当于是无值的字典,所以也用{}表示
# myset =set('hello')
# print(len(myset))
# for ch in myset:
#     print(ch)
#
# aset =set('abc')
# bset = set('cde')
# aset & bset #交集
# aset.intersection(bset) #交集
# aset | bset #并集
# aset.union(bset) #并集
# aset - bset #差补
# aset.difference(bset) #差补
# aset.add('new')
# aset.update(['aaa','bbb'])
# aset.remove('bob')
# cset =set('abcde')
# dset =set('bcd')
# cset.issuperset(dset) #cset是dset的超集么?
# cset.issubset(dset) #cset 是dset的子集么?
# adict = dict() #{}
# dict(['ab','cd'])
# bdict = dict([('name','bob'),('age',25)])
# print({}.fromkeys(['zhangsan','lisi','wangwu']),11)
#
# for key in bdict:
#     print('%s:%s'% (key,bdict[key]))
#
# print('%(name)s:%(age)s' %bdict)
#
# bdict['name']='tom'
# bdict['email']='tom@tedu.cn'
#
# del bdict['email']
# bdict.pop('age')
# bdict.clear()
# import sys
# import keyword
# import string
#
# first_chs = string.ascii_letters + '_'
# all_chs = first_chs + string.digits
#
# def check_id(idt):
#     if keyword.iskeyword(idt):
#         return "%s is keyword" % idt
#
#     if idt[0] not in first_chs:
#         return "1st invalid"
#
#     for ind,ch in enumerate(idt[1:]):
#         if ch not in all_chs:
#             return "char in postion #%s invalid" % (ind +2)
#
#     return  '%s is valid'% idt
#
# if __name__ == '__main__':
#     print(check_id(sys.argv[1])) #python3 checkid.py abc@123
#
# import os
#
# def get_fname():
#     while True:
#         fname =input('filename: ')
#         if not os.path.exists(fname):
#             break
#         print('%s already exists.Try again'% fname)
#
#     return fname
#
# def get_content():
#     content = []
#     print('输入数据,输入end结束')
#     while True:
#         line = input('>')
#         if line == 'end: '
#             break
#         content.append(line)
#
#     return content
#
# def wfile(fname,content):
#     with open(fname,'w')as fobj:
#         fobj.writelines(content)
#
# if __name__ == '__main__':
#     fname = get_fname()
#     content = get_content()
#     content = ['%s\n'% line for line in content]
#     wfile(fname,content)
#
# from random import  choice
# import string
#
# all_chs = string.ascii_letters + string.digits
#
# def gen_pass(n=8):
#     result = ''
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
#----
# def mtable(n):
#     for i in range(1,n+1):
#         for j in range(1,i + 1):
#             print('%s*%s=%s'%(j,i,j*i),end="")
#         print()
#
# mtable(6)
# mtable(9)
# def gen_fib(l):
#     fib = [0,1]
#
#     for i in range(l - len(fib)):
#         fib.append(fib[-1]+fib[-2])
#
#     return  fib #返回列表,不反悔变量fib
#
# a = gen_fib(10)
# print(a)
# print('-'*50)
# n = int(input('length:'))
# print((gen_fib(n))) #不会把变量n传入,是把n代表的赋值给形参
# import  sys
#
# def copy(src_fname,dst_fname)
#     src_fobj = open(src_fname,'rb')
#     dst_fobj = open(dst_fname,'wb')
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
# import random
#
# all_choices = ['石头', '剪刀', '布']
# win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
# prompt = """(0) 石头
# (1) 剪刀
# (2) 布
# 请选择(0/1/2): """
# cwin = 0
# pwin = 0
#
# while cwin < 2 and pwin < 2:
#     computer = random.choice(all_choices)
#     ind = int(input(prompt))
#     player = all_choices[ind]
#
#     print("Your choice: %s, Computer's choice: %s" % (player, computer))
#     if player == computer:
#         print('\033[32;1m平局\033[0m')
#     elif [player, computer] in win_list:
#         pwin += 1
#         print('\033[31;1mYou WIN!!!\033[0m')
#     else:
#         cwin += 1
#         print('\033[31;1mYou LOSE!!!\033[0m')
# fib = [0,1]
#
# for i in range(8):
#     fib.append(fib[-1]+fib[-2])
#
# print(fib)
#
# while True:
#     yn = input('Continue(y/n)')
#     if yn in ['n','N']:
#         break
#     print('running...')
# sum100 = 0
# counter = 0
#
# while counter < 100:
#     counter += 1
#     #if counter %2:
#     if counter %2 == 1:
#         continue
#     sum100 += counter
#
# print(sum100)


