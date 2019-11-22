#!/bin/env python3
#-*- coding:utf8 -*-
# print('hello world')
# print('hao',123)
# print('hao',123,sep='***') #分隔符定义为***
# print('hao',123)
# print('hao' + '123')
# user = input('username: ')
# print(user)
# divmod(5,3) #5除以3 返回商和余数(1, 2)
# a,b  = divmod(5,3) #将商和余数赋值给a和b
# 10 > 5 > 1 # python支持连续比较
# 20 > 10 < 30 #相当于20 > 10 and 10 < 30
# (not 10 > 50) or 2 < 5 #设计到可读性差的代码 应该加()
# print( type(1.3))
# True + 1 = 2
# False * 5 = 0
# #python默认使用10进制数表示数字
# hex(20) #10进制转16
# oct(10) #转8进制
# bin(10) #十进制转2进制
#
# py_str[2:6] # 切片,不会出现下标越界的错误
#
# import  getpass #倒入模块
# username= input('username: ')
# password = getpass.getpass('password: ')
#
# if username == 'bob' and password == '123456':
#     print('Login successful')
# else:
#     print('Login incorrect')
#
# import random
#
# num = random.randint(1,10) #随机生成1-10之间的数字
# answer = int(input('guess a number: '))
# if answer > num:
#     print('猜大了')
# elif answer < num :
#     print('猜小了')
# else:
#     print('猜对了')
#
# print('the number: ',num)
#
# score = int(input('分数: '))
#
# if score  >= 90:
#     print('优秀')
# elif score >= 80:
#     print('好')
# elif score >=70:
#     print('良')
# elif score >=60:
#     print('及格')
# else:
#     print('你要努力了')
#
# score = int(input('分数：　'))
#
# if score >= 60 and score <=70:
#     print('几个')
# elif 70 <= score < 80:
#     print('良')
# elif 80 <= score <90:
#     print('好')
# elif score >=90 and score <=100:
#     print('优秀')
# else:
#     print('你要努力了')
#
# import  random
#
# all_choices = ['石头','剪刀','布']
# computer = random.choice(all_choices)
# player = input('请出拳头：　')
#
# #print('Your choice:',player,:Computer's choice:",computer ')
# print("Your choice: %s,Computer's choice: %s"% (player,computer))
# if player =='石头':
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
#         print("You WIN!!!")
# else:
#     if computer == '石头':
#         print('You WIN!!!')
#     elif computer == '剪刀':
#         print('You LOSE!!!')
#     else:
#         print('平局')
#
# import  random
#
# all_choices = ['石头','剪刀','布']
# win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]
# prompt ="""(0)石头
# (1)剪刀
# (2)布
# 请选择(0/1/2): """
# computer = random.choice(all_choices)
# ind = int(input(prompt))
# player  = all_choices[ind]
#
# print("Your choice:%s,Computer's chocie:%s"% (player,computer))
# if player == computer:
#     print('\033[32;1m平局\033[0m')
# elif [player,computer] in win_list:
#     print('\033[31;1mYou WIN!!!\033[0m')
# else:
#     print('\033[31;1mYou LOSE!!!\033[0m')
#
# import random
#
# num = random.randint(1,10)
# running =True
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
#
# import random
#
# num = random.random.randint(1,10)
# counter = 0
#
# while counter < 5:
#     answer = int(input('guess the number: '))
#     if answer > num:
#         print('猜大了')
#     elif answer < num:
#         print("猜小了")
#     else:
#         print('猜对了')
#         break
#     counter +=1
# else: #循环被break就不执行了,没有被break 才执行
#     print('the number is: ',num)
#
# sum100 = 0
# counter = 1
#
# while counter < 101:
#     sum100 +=counter
#     counter += 1
#
# print(sum100)
#
# while True:
#     yn =input('Continue(y/n)')
#     if yn in ['n','N']:
#         break
#     print('running...')
# sum100 = 0
# counter =0
#
# while counter < 100:
#     counter +=1
#     #if counter %2:
#     if counter %2 ==1:
#         continue
#     sum100 += counter
#
# print(sum100)
#
# fib = [0,1]
#
# for i in range(8):
#     fib.append(fib[-1]+fb[-2])
#
# print(fib)
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%s*%s=%s'% (j,i,i*j),end='')
#     print()
#
# #10+5的结果放到列表中
# [10+5]
# #10+5这个表达式计算10次
# [10+5 for i in range(10)]
# #10+i的i来自与循环
# [10+ i for i in range(10)]
# [10+i for i in range(1,11)]
# #通过if过滤,满足if条件的才参与10+i的运算
# [10+i for i in range(1,11)if i %2 ==1]
# [10 +i for i in range(1,11)if i % 2]
# #生成ＩＰ地址列表
# ['192.168.1.%s'% i for i in range(1,255)]
#
# import  random
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
# while cwin <2 and pwin <2:
#     computer = random.choice(all_chocies)
#     ind = int(input(prompt))
#     player = all_choices[ind]
#
#     print("Your chocie:%s,Computer's choice:%s"% (player,computer))
#     if player == computer:
#         print("\033[32;1m平局\033[0m")
#     elif [player,computer]in win_list:
#         pwin +=1
#         print('\033[31;1mYou WIN!!!\033[0m')
#     else:
#         cwin +=1
#         print("\033[31;1mYou LOSE!!!\033[0m")
#
# import  getpass
#
# userdb = {}
#
# def register():
#     uname = input('username: ').strip()[0]
#     if uname and (uname not in userdb):
#         upass = input('password: ')
#         userdb[uname]= upass
#     else:
#         print('用户名为空或已存在')
#
# def login():
#         uname = input('username: ')
#         upass = getpass.getpass('password: ')
#         #if (uname in userdb) and (userdb[uname]==upass):
#         if userdb.get(uname) == upass:
#             print('\033[32;1m登陆成功\033[0m')
#         else:
#             print('\033[31;1m登录失败\033[0m')
#
# def show_menu():
#     cmds = {'0':register,'1':login}
#     prompt = """(0)注册
# (1)登录
# (2)退出
# 请选择(0/1/2): """
#
#     while True:
#         choice = input(prompt).strip()[0]
#         if choice not in ['0','1','2']:
#             print('无效的输入,请重试')
#             continue
#
#         if choice == '2':
#             print('\nBye-bye')
#             break
#
#         cmds[choice]()
#
# if __name__ == '__main__':
#     show_menu()
#
# stack = []
#
# def push_it():
#     #读取用户输入非空内容追加到列表否则打印提示
#     data = input('数据: ').strip()[0]
#     if data:
#         stack.append(data)
#     else:
#         print('输入内容为空.')
#
# def pop_it():
#     if stack:
#         print('从栈中,弹出: %s'% stack.pop())
#     else:
#         print('空栈')
#
# def view_if():
#     print(stack)
#
# def show_menu():
#     cmds = {'0':push_it,'1':pop_it,'2':view_if}
#     prompt ="""(0)压栈
# (1)出栈
# (2)查询
# (3)退出
# 请选择(0/1/2/3): """
#
#     while 1:
#         choice = input(prompt).strip()
#         if choice not in ['0','1','2','3']:
#             print('无效的输入,请重试')
#             continue
#
#         if choice == '3':
#             print('\nBye-bye')
#             break
#
#         cmds[choice]()
#
# if __name__ == '__main__':
#     show_menu()
#
# import sys
# import  subprocess
# import randpass2
#
# def adduser(uname,passwd,fname):
#     result = subprocess.run(
#         'id %s &> /dev/null' % uname,shell=True
#     )
#     if result.returncode ==0:
#         print('用户已存在')
#         return
#
#     subprocess.run('useradd %s'% uname,shell=True)
#     subprocess.run(
#         'echo %s |passwd --stdin %s'% (passwd,uname),
#         shell=True
#     )
#
#     info = """用户名: %s
# 密码：　%s
# """% (uname,passwd)
#     with open(fname,'a')as fobj:
#         fobj.write(info)
#
# if __name__ == '__main__':
#     uname = sys.argv[1]
#     fname = sys.argv[2]
#     passwd = randpass2.randpass()
#     adduser(uname,passwd,fname)
#     #python adduser.py zs /tmp/users.txt
#
# import os
#
# def get_fname():
#     while 1:
#         fname = input('文件名：')
#         if not os.path.exists(fname):
#             break
#
#         print('文件已存在.请重试.')
#
#     return  fname
#
# def get_content():
#     content = []
#
#     print('请输入文件内容,单独输入end表示结束.')
#     while 1:
#         line = input('(end to quit)> ')
#         if line == 'end':
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
#     fname =get_fname()
#     content = get_content()
#     content = ['%s\n'% line for line in content]
#     wfile(fname,content)
#
# from random import choice
# from string import ascii_letters,digits
#
# all_chs = ascii_letters + digits
#
# def randpass(n=8):
#     result = ''
#
#     for i in range(n):
#         ch = choice(all_chs)
#         result +=ch
#
#     return  result
#
# if __name__ == '__main__':
#     a = randpass()
#     print(a)
#
# import sys
#
# def copy(src_fname,dst_name):
#     src_fobj = open(src_fname,'rb')
#     dst_fobj = open(dst_fname,'wb')
#
#     while 1:
#         data = src_fobj.read(4096)
#         if not data:
#             break
#
#         dst_fobj.write(data)
#
#     src_fobj.close()
#     dst_fobj.close()
#
# if len(sys.argv) != 3:
#     print('Usage: %s src dst' % sys.argv[0])
#     exit(10)
#
# copy(sys.argv[1],sys.argv[2])
#
# #python cp4.pu /etc/hosts /tmp/zj
#
# from random import choice
# from string import ascii_letters,digits
#
# def randpass(n=8):
#     result = ''
#
#     for i in range(n):
#         ch = choice(all_chs)
#         result += ch
#
#     return result
#
# if __name__ == '__main__':
#     a = randpass()
#     print(a)
#
# import  sys
# import subprocess
# import randpass2
#
# def adduser(uname,passwd,fname):
#     result = subprocess.run(
#         'id %s &> /dev/null' % uname,shell=True
#     )
#     if result.returncode == 0:
#         print('用户已存在')
#         return
#     subprocess.run('useradd %s'% uname,shell=True)
#     subprocess.run(
#         'echo %s | passwd --stdin %s'% (passwd,uname),
#         shell=True
#     )
#
#     info ="""用户名:%s
# 密码:%s
# """% (uname,passwd)
#     with open(fname,'a')as fobj:
#         fobj.write(info)
#
# if __name__ == '__main__':
#     uname = sys.argv[1]
#     fname = sys.argv[2]
#     passwd = randpass2.randpass()
#     adduser(uname,passwd,fname)
#     #python adduser.py zs /tmp/users.txt
