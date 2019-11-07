#!/bin/env python3
#-*- coding:utf8 -*-
#学python3的第三天
#python打开文件
#open默认以读的方式打开,文件不存在则报错
# f = open('/tmp/mima')
# print(f)
# #将内容读取出来,赋值给data
# data = f.read()
# print(data)
# data = f.read() #继续向后读,因为全部内容已经读完所以后面呈现为空
# print(data) #如果不用print看的话就有点乱
# #关闭文件
# f.close() #关闭后再打开就又从头开始读了
# f = open('/tmp/mima') #重新打开
# print(f.read(1)) #读取1字节
# print(f.read(3)) #继续读3个字节
# print(f.readline()) #从文件指针开始,读一行
# print(f.readlines()) #将剩余部分读到列表中,每一行是列表的一项
# print(help(f.readlines())) #看帮助
# print(f.readlines(-1)) #查看全部\
#以上了解一下即可
#***重要: 文本文件一般采用的方式是for循环遍历***
# f = open('/tmp/mima')
# for line in f:
#     print(line,end='')
# f.close()
#************************************************

# f = open('/tmp/ls') #cp /bin/ls /tmp/ls
# # print(f.read(10)) #打开文本文件直接报错
# f = open('/tmp/ls','rb') #r是读,b是bytes
# print(f.read(10))
# f.close()
#
# #写入文件的两种方法.注意: 以w 方式打开文件,会将文件清空
# #1)
# f = open('/tmp/mima','w')
# print(f.write('hello world!\n')) #写入了13字节
# f.flush() #非必须操作(当没达到默认4K磁盘不会写入,先存着,这时需要刷新一下才会立刻写入)
# #2)
# f.writelines(['2nd line.','new aaa\n','3rd line.\n']) #另一种写入
# f.close()
# #打开一个不存在的文件会创建
# f = open('/tmp/aaaa','wb')
# # print(f.write('你好')) #直接写汉字会报错,就像图片里的子不能复制一样
# hi = '你好\n' #汉字赋值
# print(hi.encode()) #然后转换成二进制,在utf8一个汉字默认占3个字节(byte),\n占1个字节
# print(f.write(hi.encode())) #共写入7个字节
# f.close() #关文件好习惯!(不管一般没什么后果)
#*****************************************************************
# #with语句(防止忘了管文件)
# #通过with语句文件自动关闭,
# with open('/tmp/mima') as f:
#     f.readline() #执行完文件自动关闭
#print(f.readline()) #此时在读就报错,因为文件已经关闭
#******************************************************************************
'''
seek 可以在不关闭文件的情况下移动指针,
它有两个参数,第二个参数是相对位置,0表示开头,1表示当前指针位置
2表示结尾;第一个参数是偏移量
'''
# f = open('/tmp/mima')
# print(f.tell()) #总是显示距离开头多少字节,刚打开距离为0
# print(f.seek(6,0)) #移动6个,0是相对位置(开头是0,从0开始),6是偏移量(所在位置)
# print(f.read(5)) #在读5个
# print(f.tell()) #读到11个位置了(从0开始读的所以不是12是11)
# f.close()
#复制cp操作cp.py
#代码问题:
#不建议硬编码
#变量名应该有意义
#
# f1 = open('/bin/ls','rb')
# f2 = open('/tmp/list','wb')
#
# data = f1.read()
# f2.write(data)
#
# f1.close()
# f2.close()

#改良版本
'''
while 1和while True区别
python2中True没有做优化每次循环都会对其检查 1被优化过不会检查
python3中二者无区别
'''
# src_fname = '/bin/ls'
# dst_fname = '/tmp/list2'
#
# src_fobj = open(src_fname,'rb')
# dst_fobj = open(dst_fname,'wb')
#
# while 1:         #非文本文件用while(也能用于文本文件)
#     data = src_fobj.read(4096) #一般来说磁盘默认一块磁盘读写大小为4096
#     #if data == b'': #b表示bytes
#     #if len(data) == 0:
#     if not data: #空串为假,取反为真
#         break
#
#     dst_fobj.write(data)
#
# src_fobj.close()
# dst_fobj.close()
#*****************************************************
#函数:函数装的都是代码
'''
一组代码的集合
'''
# #格式def fuction_name(option)
# #实例
# def pstar():
#     print('*'*30)
# pstar() #使用()进行函数调用(调用的都是代码)
# a = pstar() #赋值给a函数调用完里面是个None(函数返回值)
# #函数如果需要返回值,则使用return进行返回;没用明确的语句,默认返回None
# print(a)
# #如果需要用到返回值那么就需要用return进行返回
#函数返回值
# def add():
#     a = 10+5 #函数中的变量是局部变量并不是全局变量只能在函数中使用
#     return a #返回的是结果而不是过程
# n = add()
# print(n)
#参数(变量)
# #1)形式参数(形参:在定义函数是,函数名称后面括号中的变量)
# def add(x,y):
#     return  x + y
# #2)实际参数:实参,调用函数时,传递给函数的参数
# print(add(5,5)) #传参
# #自定义9*9函数
# def f(x):
#     for i in range(1,x + 1):
#         for j in range(1,i + 1):
#             print('%sx%s=%s'% (j,i,i*j),end=' ')
#         print()
# f(int(input('请输入乘法表的范围: ')))
# #函数改良copy并用input传参
# def copy(src_fname,dst_fname):
#     src_fobj = open(src_fname,'rb')
#     dst_fobj = open(dst_fname,'wb')
#
#     while 1:         #非文本文件用while(也能用于文本文件)
#         data = src_fobj.read(4096) #一般来说磁盘默认一块磁盘读写大小为4096
#         #if data == b'': #b表示bytes
#         #if len(data) == 0:
#         if not data: #空串为假,取反为真
#             break
#
#         dst_fobj.write(data)
#
#     src_fobj.close()
#     dst_fobj.close()
#
# copy(input('sourcedir: '),input('distination: '))
# #位置参数
# #python将命令行上的位置参数,保存到了sys模块的argv列表中
# import sys
#
# print(sys.argv) #位置参数接收的全部是字符类型
# #用位置参数传参
# import  sys
#
# def copy(src_fname,dst_fname):
#     src_fobj = open(src_fname,'rb')
#     dst_fobj = open(dst_fname,'wb')
#
#     while 1:         #非文本文件用while(也能用于文本文件)
#         data = src_fobj.read(4096) #一般来说磁盘默认一块磁盘读写大小为4096
#         #if data == b'': #b表示bytes
#         #if len(data) == 0:
#         if not data: #空串为假,取反为真
#             break
#
#         dst_fobj.write(data)
#
#     src_fobj.close()
#     dst_fobj.close()
#
# if len(sys.argv) != 3:
#     print('Usage: %s [src] [dst]'% sys.argv[0])
#     exit(250) #程序遇到exit就会彻底结束,1是$?的值
# else:
#     copy(sys.argv[1],sys.argv[2])
# #函数应用:斐波那契数列
# def gen_fib(l):
#     fib = [0,1]
#
#     for i in range(l - len(fib)): #range不包括结束的数字,例如输入5则range[0,1,2]
#         fib.append(fib[-1]+fib[-2])
#
#     return  fib #返回列表,不返回变量fib
# print(gen_fib(int(input('请输入所需列表[0,1]位数: '))))
# #具有默认值的参数
# def pstar():
#     print('*'*30)
# pstar() #只能打印30个*

# def pstar(n): #传参,n的值就是*号的个数
#     print('*'*n)
# pstar(int(input('n= ')))
#a = input('请输入数字：')

# import sys
#
# def pstar(n=30): #提供默认参数
#     print('*'*n)
#
# if len(sys.argv) != 2:
#     pstar()
#     exit(1)
# pstar(int(sys.argv[1]))


# #模块导入方法
# import time #常用导入方法
# time.ctime()
#
# from random import  randint,choice #从模块中导入一部分功能:常用
# print(randint(1,100))
# print(choice('abcd'))

# #一行导入多个模块,不常用,因为可读性差
# import os,sys
# #导入模块的同时,为模块创建别名,不常用
# import getpass as gp
# p = gp.getpass()

#自定义模块
'''
#vim star.py //自定义star模块
hi = 'hello world'

def pstar(n=30):
    print('*' * n)
#vim call_star.py
import star

print('this is call_star')
star.pstar()
print(star.hi)

#python call_star.py
'''
#模块的特性:导入模块时模块中的code会先执行一遍!
#模块中的代码,希望它在作为一个脚本文件直接运行时执行;希望他被当成模块导入时,不要执行,这个时候可以使用_name_属性
'''
_name_是一个特殊的变量,它的值有两个
一个是_main_,另一个是 模块名
#cat foo.py

print(__name__)

#cat bar.py

import foo

#python foo.py //自定义的模块foo

__main__

#python bar.py //调用foo模块的文件

foo
'''
#通过_name_特殊变量可解决上述问题
'''
#vim star.py 
hi = 'hello world'

def pstar(n=30):
    print('*' * n)
    
if __name__ == '__main__': //在自定义star模块中使用_name_特殊变量做一个判断即可
    print(hi)              //因为此功能太常用 直接打main +　回车　就能瞬间打印出来
    print(40)
'''
# #生成随机八位密码
# from random import choice
#
# all_chs = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
# result = ''
#
# for i in range(8):
#     ch = choice(all_chs)
#     result += ch
#
# print(result)
#函数随机生成密码并且可自定义
import sys    #导入后以第一次为准,如果修改模块参数需要退出python3然后在进去如重新导入一次即可.
from random import choice
from string import ascii_letters,digits

def randpass(site=8):

    all_chs = ascii_letters + digits
    result = ''

    for i in range(site):
        ch = choice(all_chs)
        result += ch
    return result

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('默认随机8位:',randpass())
        exit(1)
    else:
        print('生成%s位密码:'% sys.argv[1],randpass(int(sys.argv[1])))



# #午间练习:时长两小时
# range(10) #[0,1,2,3,4,5,6,7,8,9]
# print(list(range(10)))
# range(6,11) #[6,7,8,9,10]
# range(1,10,2) #[1,3,5,7,9]
# range(10,0,-1) #[10,9,8,7,6,5,4,3,2,1]
# sum100 = 0
#
# for i in range(1,101):
#     sum100 += i
#
# print(sum100)
#
#
# fib = [0,1]
#
# for i in range(8):
#     fib.append(fib[-1]+fib[-2])
#
# print(fib)
#
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%s*%s=%s'% (j,i,i*j),end='')
#     print()
#
# #i=1 -> j:[1]
# #i=2 -> j:[1,2]
# #i=3 -> j:[1,2,3]
#
#
# n = int(input('number: '))
#
# for i in range(1,n + 1):
#     for j in range(1,i + 1):
#         print('%s*%s=%s'% (j,i,j*i),end='')
#     print()
#
# #10+5的结果放到列中
# print([10+5])
# #10+5这个表达式计算10次
# print([10 + 5 for i in range(10)])
# #10+i的i来自于循环
# print([10 + i for i in range(10) ])
# print([10+i for i in range(1,11)])
# #通过if过滤,满足if条件的才参与10+i的运算
# print([10+i for i in  range(1,11)if i % 2 == 1])
# print([10 + i for i in range(1,11)if i % 2])
# #生成ip地址列表
# ['192.168.1.%s'% i fori i in range(1,255)]
#
# #石头剪刀布三局两胜
# import  random
#
# all_choice = ['石头','剪刀','布']
# win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]
# prompt = '''(0)石头
# (1)剪刀
# (2)布
# 请选择(0/1/2): '''
# cwin = 0
# pwin = 0
#
# while cwin < 2 and pwin <2:
#     computer = random.choice(all_choice)
#     ind = int(input(prompt))
#     player = all_choice[ind]
#
#     print("Your choice: %s,Computer's choice: %s"% (player,computer))
#     if player == computer:
#         print('\033[31;1m平局\033[0m')
#     elif [player,computer] in win_list:
#         pwin  += 1
#         print('\033[31;1mYou WIN!!!\033[0m')
#     else:
#         cwin += 1
#         print('\033[31;1mYou LOSE!!!\033[0m')
# #文件操作的三个步骤:打开 读写 关闭
# #cp /etc/passwd /tmp
# f = open('/tmp/passwd') #默认以r的方式打开纯文本文件
# data = f.read() #read()把所有内容读取出来
# print(data)
# data = f.read() #随着读写的进行,文件指针向后移动.
# #因为第一个f.read()已经把文件指着移动到了结尾了,所以在读就没有数据了
# #所以data是空字符串
# f.close()
#
# f = open('/tmp/passwd')
# data = f.read(4) #读4字节
# f.readline() #督导换行符\n结束
# f.readlines() #把每一行数据读出来放到列表中
# f.close()
#
# ###########################
# f = open('/tmp/passwd')
# for line in f:
#     print(line,end='')
# f.close()
#
#
# ##############################
# f = open('图片地址','rb') #打开费文本文件要加参数b
# f.read(4096)
# f.close()
#
# ##################################
# f = open('/tmp/myfile','w') #'w'打开文件,如果文件不存在则创建
# f.write('hello world!\n')
# f.flush() #立即将缓存中的数据同步到磁盘
# f.writelines(['2nd line.\n','new line.\n'])
# f.close() #关闭文件的时候,数据保存到磁盘
#
# ############################
# with open('/tmp/passwd')
# f.tell() #查看文件指针的位置
# f.readline()
# f.tell()
# f.seek(0,0) #第一个数字是偏移量,第二位数字是数字相对位置.
#             #相对位置0表示开头,1表示当前,2表示结尾
# f.tell()
# f.close()
#
# f1 = open('/bin/ls','rb')
# f2 = open('root/ls','wb')
#
# data = f1.read()
# f2.write()
#
# f1.close()
# f2.close()
#
#
#
# src_fname = '/bin/ls'
# dst_fname = '/root/ls'
#
# src_fobj = open(src_fname,'rb')
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
# print(sys.argv ) #sys,argv是sys是模块里的argv列表
#
# #python3 position_args.py
# #python3 position_args.py 10
# #python3 position args.py 10 bob

