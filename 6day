#!/bin/env python3
#-*- coding:utf8 -*-
#学python3的第六天
#练习一天~
# adict = dict([('name','bob'),('age',25)])
# print(len(adict))
# print(adict)
# a = hash(100) #判断给定的数据是不是不可变的,不可变数据才能作为key
# print(a)
# a = adict.keys() #取出所有字典的key
# print(a)
# a = adict.values() #取出字典所有的value
# print(a)
# a = adict.items() #取出key:value对
# print(a)
# #get方法常用很重要
# print(adict.get('name')) #取出字典中name对应的value,如果没有则返回None
# print(adict.get('qq')) #None
# print(adict.get('qq','not found')) #没有qq,返回指定内容:not found
# print(adict.get('age','not found'))
# a = adict.update({'phone': '123456'}) #返回值为None
# print(a)
# b = adict['phone'] = '123456' #存在则更新 不存在就添加 并且可赋值
# print(b)
# #集合相当于是无值(value)的字典,所以也用{}表示
# myset = set('hello')
# print(len(myset))
# for ch in myset:
#     print(ch)
#
# aset = set('abc')
# bset = set('cde')
# aset & bset #交集
# aset.intersection(bset) #交集
# aset | bset #并集
# aset.union(bset) #并集
# aset - bset #差补
# aset.difference(bset) #差补
# aset.add('new')
# print(aset)
# aset.update(['aaa','bbb'])
# print(aset)
# aset.remove('bbb')
# cset = set('abcde')
# dset = set('bcd')
# cset.issuperset(dset) #cset是dset的超集么?
# dset.issubset(cset) #dset是cset的子集么?

# #cp /etc/passwd .
# #cp /etc/passwd mima
# #vim mima -> 修改,与passwd有些区别
#
# with open('passwd')as fobj:
#     aset = set(fobj)
#
# with open('mima') as fobj:
#     bset = set(fobj)
#
# with open('diff.txt','w')as fobj:
#     fobj.writelines(bset - aset)
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
#         userdb[username]=password
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
# Please input your choice(0/1/2): """
#
#
#     while True:
#         choice = input(prompt).strip()[0]
#         if choice not in '012':
#             print('Invalid input,Try again.')
#             continue
#
#         if choice == '2':
#             break
#
#
#         cmds[choice]()
#
# if __name__ == '__main__':
#     show_menu()
#
# import time
#
# result = 0
# start = time.time() #返回运算前时间戳
# for i in range(100000000):
#     result +=i
# end = time.time() #返回运算后时间戳
# print(result)
# print(end-start)
# print('hello world!')
#
# if 3 > 0:
#     print('ok')
#     print('yes')
#
# x = 3; y = 4 #不推荐 可读性差
# print(x+y)
#
# print('hello world!')
# print('hello','world!') #逗号自动添加默认的分隔符:空格
# print('hello' + 'world') #+表示字符拼接
# print('hello','world',sep='***') #sep指定分隔符
# print('#' * 50) #*表示重复*50遍
# print('how are you?',end='') #取消print的默认打空格机构
# print(5/2)
# print(5//2)
# print(5%2)
# print(5**3)
# print(5>3)
# print(3>5)
# print(20>10>5)
# print(20>10 and 10 > 5)
# print(not 20 > 10)
#
# number = input('请输入数字; ') #input用于获取键盘输入
# print(number)
# print(type(number)) #input获得的数据是字符型
#
# print(number + 10) #报错 不能把字符和数字做运算
# print(int(number) + 10) #int可将字符串10转换成数字10
# print(number + str(10)) #str将10转换为字符串后实现字符串拼接
#
# username = input('username: ')
# print('welcome',username) #print各项间默认以空格作为分隔符
# print('welcome'+username) #助意引号内最后的空格
#
# sentence = 'tom\'s pet is a cat'
# sentence2 = "tom's pet is a act"
# sentence3 = 'tom said:\"hello world!\"'
# sentence4 = 'tom said"hello world"'
# #三个连续的单引号或双引号,可以保存输入格式,允许输入多行字符串
# words = """
# hello
# world
# abcd"""
# print(words)
#
# py_str = 'python'
# len(py_str) #取长度
# py_str[0] #取第一个字符串
# 'python'[0]
# py_str[-1] #最后一个字符
# #py_str[6] #错误,下表超出范围
# py_str[2:4] #切片 起始下标包含,结束下标不包含
# py_str[2:] #从下标为2的字符取到结尾
# py_str[:2] #从开头取到下标是2之前的字符
# py_str[:] #取全部
# #步长值为2,默认是1
# py_str[::2]
# py_str[1::2] #去除yhn
# py_str[::-1] #步长为负,表示自右向左取
#
# py_str + 'is good' #简单的拼接到一起
# py_str * 3 #把字符串重复三遍
# print('t' in py_str) #True
# print('th' in py_str)
# print('to' in py_str)
# print('to' not in py_str)
#
# alist = [10,20,30,'bob','alice',[1,2,3]]
# print(len(alist))
# alist[-1] #取出最后一项
# alist[-1][-1] #因为最后一项是列表,列表还可以继续取吓标
# [1,2,3][-1] #[1,2,3]是列表,[-1]表示列表最后一项
# alist[-2][2] #列表倒数第二项是字符串,在取出来字符下标为2的字符
# alist[3:5] #['bob','alice']
# print(10 in alist)
# print('o' in list)
# print(100 not in alist)
# alist[-1] = 100 #修改最后一项的值
# alist.append(200) #向列表中追加一项

# atuple = (10,20,30,'bob','alice',[1,2,3])
# print(len(atuple))
# print(10 in atuple)
# print(atuple[2])
# print(atuple[3:5])
# #atuple[-1]=100 #错误 元组是个不可改变的
# #字典是key-value键值对形式的,没有顺序,通过键取出值
# adict = {'name':'bob','age': 21}
# print(len(adict))
# print('bob' in adict)
# print('name' in adict)
# a = adict['email']= 'bob@tedu.cn'
# print(a)
# adict['age']=25 #字典中已有key,修改对应的value
#
# if 3 > 0:
#     print('yes')
#     print('ok')
#
# if 10 in [10,20,30]:
#     print('ok')
#
# if -0.0:
#     print('yes') #任何值为0的数字都是
#
# if [1,2];
#     print('yes') #非空对象都是True
#
# if '':
#     print('yes') #空格字符也是字符,条件为True
#
# a = 10
# b = 20
#
# if a<b:
#     smaller=a
# else:
#     smaller=b
#
# print(smaller)
#
# s = a if a < b else b #和上面的if-else语句等价
#
# print(s)
#
#
# import  getpass
#
# username = input('username: ')
# #getpass模块中,有一个方法也叫getpass
# password = getpass.getpass('password: ')
#
# if username == 'bob' and password == '123456':
#     print('Login successful')
# else:
#     print('Login incorrect')
#
# import random
#
# num = _random.randint(1,10) #随机生成1-10\之间的数字
# answer = int(input('guess a number: ')) #将用户输入的数字符转乘整数
# if answer > num:
#     print('猜大了')
# elif answer > num:
#     print('猜小了')
# else:
#     print('猜对了')
#
# print('the number: ',num)
#
# score = int(input('分数: '))
#
# if score >=90:
#     print('优秀')
# elif score >= 80:
#     print('好')
# elif score >= 70:
#     print('良好')
# elif score >= 60:
#     print('及格')
# else:
#     print('你要努力了')
# score = int(input('得分: '))
#
# if score >= 60 and score <70:
#     print('及格')
# elif 7 <= score<80:
#     print('良好')
# elif 80 <= score <90:
#     print('好')
# elif score >= 90:
#     print('优秀')
# else:
#     print('你要努力了')
# import  randdom
#
# all_choice = ['石头','剪刀','布']
# computer = randdom.chocie(all_choice)
# player = input('请出拳头: ')
#
# #print('Your choice:',player,"Computer's choice",computer)
# print("'Your choice: %s,Computer's choice: %s"% (player,computer))
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
# import random
#
# all_choices = ['石头','剪刀','布']
# win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]
# prompt = """(0)石头
# (1)剪刀
# (2)布
# 请选择(0/1/2: """
# computer = random.choice(all_choice)
# ind = int(input(prompt))
# player = all_choices[ind]
#
# print("'Your choice: %s,Computer's chocie:%s"% (player,computer))
# if player == computer:
#     print('\033[31;1m平局\033[0m')
# elif [player,computer]in win_list:
#     print('\033[31;1mYou WIN!!!\033[0m')
# else:
#     print('\033[31;1mYou LOSE!!!\033[0m')
# import  random
#
# num = random.randint(1,10)
# couter = 0
#
# while couter <5:
#     answer = int(input('guess the number:'))
#     if answer > num:
#         print('猜大了')
#     elif answer < num:
#         print('猜笑了')
#     else:
#         print('猜对了')
#         break
#     couter +=1
# else: #循环被break就不执行了,没有被break才执行
#     print('the number is : ',num)
# sum100 = 0
# counter = 1
#
# while counter < 101:
#     sum100 += counter
#     counter +=1
#
# print(sum100)
# while True:
#     yn = input('Continue(y/n): ')
#     if yn in ['n','N']:
#         break
#     print('running...')
#
# sum100 = 0
# counter = 0
#
# while counter < 100:
#     counter +=1
#     #if conuter %2:
#     if counter %2 ==1:
#         continue
#     sum100 += counter
#
# print(sum100)
#
# astr = 'hello'
# alist = [10,20,30]
# atuple = ('bob','tom','alice')
# adict = {'name': 'john','age':23}
#
# for ch in astr:
#     print(ch)
#
# for i in alist:
#     print(i)
#
# for name in atuple:
#     print(name)
#
# for key in adict:
#     print('%s:%s'% (key,adict[key]))
#
#range(10) #[0,1,2,3,4,5,6,7,8,9]
#>>>list(range(10))
#range(6,11) #[6,7,8,9,10]
#range(1 ,10, 2) #随机的基数列表1 3 5 7 9
#range(10 ,0 ,-1) #倒着随机10 9 8 7 6 5 4 3 2 1 由于0为最后一项不打印
# sum100 = 0
#
# for i in range(1,101):
#     sum100 += i
#
# print(sum100)
# fib = [0,1]
#
# for i in range(8):
#     fib.append(fib[-1] + fib[-2])
#
# print(fib)
#
# for i in range(1,10):
#     for i in range(1,i + 1):
#         print('%s*%s=%s'% (j,i,j*i),end='')
#     print()
#
# #i =1 ->j:[1]
# #i =2 ->j:[1,2]
# #i =3 ->j:[1,2,3]
#
# n = int(input('number: '))
#
# for i in range(1,n + 1):
#     for j in range(1, i + 1):
#         print('%s*%s=%s'% (j,i.i*j),end="")
#     print()
# #10+5的结果放到列表中
# [10+5]
# #10+5这个表达式计算10次
# print([10+5for i in range(10)])
# #10+i的i来自循环
# print([10+i for i in range(10)])
# print([10 + i for i in range(1,11)])
# #通过if过滤,满足if条件的才参与10+i的运算
# print([10+i for i in range(1,11)if i % 2 == 1])
# print([10+i for i in range(1,11)if i %2])
# #生成ip地址列表
#print(['192.168.1.%s'% i for i in range(1,255)])
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
# while cwin < 2 and pwin <2 :
#     computer = random.choice(all_choice)
#     ind = int(input(prompt))
#     player = all_choices[ind]
#
#     print("Your choice: %s,Computer's choice: %s"% (player,computer))
#     if player == computer:
#         print('\033;1m平局\033[0m')
#     elif [player,computer] in win_list:
#         pwin += 1
#         print('\033[31;1m You WIN!!!\033[0m')
#     else:
#         cwin += 1
#         print('\033[31;1mYou LOSE!!!\033[0m')
# #文件操作的三个步骤:打开 读写 关闭
# #cp /etc/passwd /tmp
# f = open('/tmp/passwd') #默认以r的方式打开纯文本文件
# data = f.read() #read()把所有内容读取出来
# print(data)
# data =f.read() #随着读写的进行,文件指针向后移动.
# #因为第一个f.read()已经把文件指针移动到结尾了,所以再读就没有数据了
# #所以data时空字符串
# f.close()
#
# f= open('/tmp/passwd')
# data=f.read(4) #读4字节
# print(f.readline()) #读到换行符\n结束
# f.readlines() #把每一行数据读出来放到列表中
# f.close()
# #########################################
# f = open('/tmp/passwd')
# for line in f:
#     print(line,end='')
# f.close()
#
# ###############################################
# f =open('图片地址','rb') #打开非文本文件要加参数b
# f.read(4096)
# f.close()
#
# #########################################
# f = open('/tmp/myfile','w') #'w'打开文件,如果文件不存在则创建
# f.write('hello world!\n')
# f.flush() #立即将缓存中的数据同步到磁盘
# f.writelines(['2nd line.\n','new line.]n'])
# f.close() #关闭文件的时候将数据保存到磁盘
#
# ###############################
# with open('/tmp/passwd')as f:
#     print(f.readline())
#
# ##########################
# f = open('/tmp/passwd')
# f.tell() #查看文件指针的位置
# f.readline()
# f.tell()
# f.seek(0,0) #第一个数字是偏移量,第二个数字是相对位置
#              #相对位置0表示开头 1表示当前 2表示结尾
#
# f.tell() #查看当前的位置
# f.close()
# file1 = open('/bin/ls','rb')
# file2 = open('/root/ls','wb')
#
# data = file1.read()
# file2.write(data)
#
# file1.close()
# file2.close()
# src_fname='/bin/ls'
# dst_fname='/root/ls'
#
# src_fobj=open(src_fname,'rb')
# dst_fobj = open(dst_fname,'wb')
#
# while True:
#     data = src_fobj.read(4096)
#     if not data:
#         break
#     dst_fobj.write(data)
#
# src_fobj.close()
# dst_fobj.close()
#
# import sys
#
# print(sys.argv) #sys.argv是sys模块里的argv列表
#
#python3 position_args.py
#python3 positon_args.py
#python3 position_args.py
# def gen_fib(l):
#     fib = [0,1]
#
#     for i in range(l -len(fib)):
#         fib.append(fib[-1] + fib[-2])
#
#     return fib #返回列表,不返回变量fib
#
# a = gen_fib(10)
# print(a)
# print('-'*50)
# n = int(input("length: "))
# print(gen_fib(n))
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
# def mtable(n):
#     for i in range(1,n+1):
#         for j in range(1,i + 1):
#             print('%s*%s=%s'% (j,i,i*j),end='')
#         print()
#
# mtable(6)
# mtable(9)
# hi ='hello world!'
#
# def pstar(n=50):
#     print('*'*n)
#
# if __name__ == '__main__':
#     pstar()
#     pstar(30)
#
# print(pstar())
# print(hi)
#
# from random import choice
# import string
#
# all_chs = string.ascii_letters + string.digits
#
# def gen_pass(n=8):
#     result = ''
#
#     for i in range(n):
#         ch = choice(all_chs)
#         result +=ch
#
#     return result
#
# if __name__ == '__main__':
#     print(gen_pass())
#     print(gen_pass(4))
#     print(gen_pass(10))
# alist = [10,'john']
# #list(enumerate(alist)) #[(0,10),(1,'john)] #取出key和value以列表方式
# #a,b = 0,10 #a->0  ->10
# print(len(alist))
# for ind in range(len(alist)):
#     print('%s:%s'% (ind,alist[ind]))
#
# for item in enumerate(alist):
#     print('%s: %s'% (item[0],item[1]))
#
# for ind,val in enumerate(alist):
#     print('%s: %s'% (ind,val))

# atuple = (96,97,40,75,58,34,69,26,66,90)
# print(sorted(atuple)) #分类
# print(sorted('hello'))
# for i in reversed(atuple):
#     print(i,end='')
# py_str = 'hello world!'
# print(py_str)
# py_str.capitalize() #行首字母大写
# print(py_str.capitalize())
# print(py_str.title()) #每个单词首字母大写
# print(py_str.center(50)) #居中50格子默认用空格补齐
# print(py_str.center(50,'#')) #居中50并且用#补全
# print(py_str.ljust(50)) #左对齐右边默认空格补全
# print(py_str.rjust(50,'*')) #右对齐并以*补全左边50
# print(py_str.count('l')) #统计i出现的次数
# print(py_str.count('lo'))
# print(py_str.endswith('!')) #以!结尾么?
# print(py_str.endswith('d!'))
# print(py_str.startswith('a')) #是以a开头么?
# print(py_str.islower()) #字母都是小写的?其他字符不考虑
# print(py_str.isupper()) #字母都是大写的?其他字符不考虑
# print('  \thello\t '.strip()) #默认去除两端空白字符,常用
# print('hello\t  '.lstrip()) #去除左边
# print('how are you ?'.split()) #默认分离 以空格为分割标志
# print('hello.tar.gz'.split('.')) #分离 以·为分割标志
# print('.'.join(['hello','tar','gz'])) #合并 是split和join是相反的
# print('%s is %s years old'% ('bob',23)) #常用
# print('%s is %d years old'% ('bob',23))
# print('%s is %d years old'% ('bob',23.5)) #%d只能整数 但是不会报错
# print('%s is %f years old'% ('bob',23.5)) #小数显示
# print('%s is %.2f years old'% ('bob',23.5))
# print('%s is %5.2f years old'% ('bob',23.5))
# print('%s is %5.f years old'% ('bob',23.5)) #宽五保留两位小数
# print('97 is %c '% 97) #ascii码中小写字母a编号为97
# print('11 is %#o'% 11) #表示有前缀的八进制(11 is 0o13)
# print('11 is %#x'% 11) #表示有前缀的十六进制(11 is 0xb)
# print('%10s%5s'% ('name','age')) #%10s表示总宽度为10,走对其
# print('%-10s%-5s'% ('name','age')) #左对齐
# print('%10d'% 123)
# print('%010d'% 123) #右靠其并且总长度为10不足的用0补全

# print('{} is {} years old'.format('bob',25))
# print('{1} is {0} years old'.format(25,'bob'))
# print("{:<10}{:<8}".format('name', 'age')) #向左对其
# print("{:>10}{:>8}".format('name', 'age')) #向右对其
# import shutil
#
# with open('/etc/passwd','rb')as sfobj:
#     with open('/tmp/mima.txt','wb')as dfobj:
#         shutil.copyfileobj(sfobj,dfobj) #拷贝文件对象
#
# shutil.copyfile('/etc/passwd','/tmp/mima2.txt')
# shutil.copy('/etc/shadow','/tmp/') #cp /etc/shadow /tmp/
# shutil.copy2('/etc/shadow','/tmp/') #cp -p /etc/shadow /tmp/
# shutil.move('/tmp/mima.txt','/var/tmp') #mv /tmp/mima.txt /var/tmp
# shutil.copytree('/etc/security','/tmp/anquan') #cp -r /etc/security /tmp/anquan
# shutil.rmtree('/tmp/anquan') #rm -rf /tmp/anquan
# #将mima2的权限在设置成与/etc/shadow一样
# shutil.copymode('/etc/shadow','/tmp/mima2.txt')
# #将mima2.txt的\元数据设置成与/etc/shadow一样
# #元数据使用stat /etc/shadow查看
# shutil.copystat('/etc/shadow','/tmp/mima2.txt')
# shutil.chown('/tmp/mima2.txt',user='zhangsan',group='zhangsan')
#
# import os
#
# def get_fname():
#     while True:
#         fname = input('filename: ')
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
#         if line == 'end':
#             break
#         content.append(line)
#
#     return  content
#
# def wfile(name,content):
#     with open(fname,'w')as fobj:
#         fobj.writelines(content)
#
# if __name__ == '__main__':
#     fname = get_fname()
#     content = get_content()
#     content = ['%s\n'% line for line in content]
#     wfile(fname,content)
alist = [1,2,3,'bob','alice']
# alist[0] = 10
# alist[1:3] = [20,30]
# print(alist)
# alist[2:2] = [22,24,26,28]
# print(alist)
# print(alist.append(100))
# alist.remove(24) #删除第一个24
# alist.index('bob') #返回下标
# blist = alist.copy() #相当于blist = alist[:]
# alist.insert(1,15) #向下标为1的位置插入数字15
# alist.pop() #默认弹出最后一项
# alist.pop(2) #弹出下标为2的项目
# alist.pop(alist.index('bob'))
# alist = [1,2,3,4,5,6]
# alist.sort(reverse=True) #倒叙排序
# print(alist)
# alist.reverse()
# alist.count(20) #统计20出现次数
# alist.clear()
# #alist.append('new')
# alist.extend('new') #['n', 'e', 'w']
# alist.extend(['hello','world','hehe'])
# print(alist)
#
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
#             return "char in postion #%s invalid" % (ind + 2)
#
#     return '%s is valid' % idt
#
# if __name__ == '__main__':
#     print(check_id(sys.argv[1]))

#
# import subprocess
# import sys
# from randpass2 import randpass
#
# def adduser(username,password,fname):
#     data= '''user information:
# %s:%s
# '''
#
#     subprocess.call('useradd %s'% username,shell=True)
#     subprocess.call(
#         'echo %s |passwd --stdin %s'% (password,username),
#         shell=True
#     )
#     with open(fname,'a')as fobj:
#         fobj.write(data % (username,password))
#
# if __name__ == '__main__':
#     username = sys.argv[1]
#     password = randpass()
#     adduser(username,password,'/tmp/user.txt')
# #python3 adduser.py.john
#
# stack = []
#
# def push_it():
#     item = input('item to push: ')
#     stack.append(item)
#
# def pop_it():
#     if stack:
#         print("from stack popped %s"% stack.pop())
#
# def view_it():
#     print(stack)
#
# import sys
#
# def unix2dos(fname):
#     dst_fname = fname + '.txt'
#
#     with open(fname)as src_fobj:
#         with open(dst_fname,'w')as dst_fobj:
#             for line in src_fobj:
#                 line = line.rstrip() +'\r\n'
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
#     print('\r%s@%s'% ('#'* count,'#'*(length-count)),end="")
#     try:
#         time.sleep(0.3)
#     except KeyboardInterrupt:
#         print('\nBye-bye')
#         break
#     if count ==length:
#         count = 0
#     count += 1
#
# adict = dict() #{}
# dict(['ab','cd'])
# bdict = dict([('name','bob'),('age',25)])
# print({}.fromkeys(['zhangsan','lisi','wangwu'],11))
#
# for key in bdict:
#     print('%s:%s'% (key,bdict[key]))
#
# print('%(name)s:%(age)s'% bdict)
#
# bdict['name'] = 'tom'
# bdict['email'] = 'tom@tedu.cn'
#
# del bdict['email']
# print(bdict)
# bdict.pop('age')
# bdict.clear()
stack = []

def push_it():
    data = input('数据: ').strip()
    if data:
        stack.append(data)
    else:
        print('输入内容为空.')

def pop_it():
    if stack:
        print('从栈中,弹出:%s'% stack.pop())
    else:
        print('空栈')

def view_it():
    print(stack)

def show_menu():
    cmds = {'0': push_it,'1': pop_it,'2': view_it}
    prompt ="""(0)压栈
(1)出栈
(2)查询
(3)退出
请选择(0/1/2/3): """

    while True:
        choice = input(prompt).strip()
        if choice not in ['0','1','2','3']:
            print('input is invalid,Try again,')
            continue

        if choice =='3':
            print('\nBye-bye')
            break

        cmds[choice]()

if __name__ == '__main__':
    show_menu()






