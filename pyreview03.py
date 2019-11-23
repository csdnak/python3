#!/bin/env python3
#-*- coding:utf8 -*-
#复习python3的第三天
#*********while循环
while 条件:
    如果条件为真则反复执行的语句
#列表解析:生成列表的一种方式
[5] #[5]
[5 + 2] #[7] (将表达式到列表)
[5 + 2 for i in range(1,11)] #循环决定表达式计算的次数[7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
[5 +i for i in range(1,11)]  #在表达式中使用循环的变量[6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
[5 + i for i in range(1,11) if i %2 == 1] #判断条件作为过滤条件
['192.168.1.%s' % i for i in range(1,255)]

#************file**************
#文件对象
"""操作文件的步骤
-打开:在磁盘中找到文件的存储位置
-读写:不管是文字还是声音还是图像,最终自爱磁盘上都是以2进制的0、1表示,读写是读写0、1的组合
-关闭
"""
#打开本文件
"""
(nsd1906) [root@room8pc16 day03]# cp /etc/passwd /tmp/mima
"""
#open默认以读的方式打开,文件不存在则报错
f = open('/tmp/mina.txt')
f = open('/tmp/mima')
#将全部内容读取出来,赋值给data
data = f.read()
print(data)
data = f.read() #继续向后读,因为全部内容已读完,所以剩下的是空
print(data) #''

f.close() #关闭文件(好习惯)
f = open('/tmp/mima') #重新打开
f.read(1)  #读取1个字节 ('r')
f.read(3)  #继续读取三3个字节
f.readline()  #从文件指针开始,读1行
':x:0:0:root:/root:/bin/bash\n'
f.readlines() #将剩余部分读到列表中,每一行是列表的一项
f.close()
#******important:text file 一般采用的方式是for循环遍历*******
f = open('/tmp/mima')
for line in f:
    print(line,end='')
f.close()
#*******read not text file
"""
(nsd1906) [root@room8pc16 day03]# cp /bin/ls /tmp/ls
"""
f = open('/tmp/ls','rb') #r是读,b是bytes
f.read(10)  #b'\x7fELF\x02\x01\x01\x00\x00\x00'
f.close()

#***********write text file
# 注意:以w方式打开文件,会将文件清空
f = open('/tmp/mima','w')
f.write('hello world!\n')  #写入了13字节(13)
f.flush() #立即将内存数据同步至磁盘
f.writelines(['2nd line.','new aaa\n','3rd line.\n'])
f.close()

#**********write not text file
f = open('/tmp/aaaa','wb')
hi = '你好\n'
hi.encode()  #b'\xe4\xbd\xa0\xe5\xa5\xbd\n'
#共写入七个字节,在utf8编码中一个汉字占3个字节,\n占1字节
f.write(hi.encode())  #7
f.close()
#************with sentence
#通过with语句打开文件,当with语句结束时,文件自动关闭
with open('/tmp/mima') as f:
    f.readline()

'hello world!\n'
f.readline()   #报错,因为文件已经关闭了

#***************seek :move file pointer
"""
seek 可以在不关闭文件的情况下,移动指针,他有两个参数,第二个参数是相对位置,0表示开头,
1表示当前指针位置,2表示结尾:第一个参数是偏移量.
"""
f = open('/tmp/mima')
f.tell() #总是显示文件指针距离开头多少字节 (0)
f.seek(6,0)  #从开头向右移动6字节 (6)
f.read(5) #world
f.close()

#*********function
"""
-函数就是一组代码的集合
-函数定义的时候,它里面的代码不会执行
-函数使用一对()进行调用,调用时,它里面的代码执行一遍
-函数定义的语法
"""
def function_name(argument):
    code_group
#example:
def pstar():
    print('*'*30)

pstar() #调用函数(**********************)
a = pstar() #******************************
print(a)  #None
#函数返回值
#函数如果需要有返回值,则使用return进行返回;没有明确的return语句,默认返回None
def add():
    a = 10 + 5
    return a
a = add()
print(a)  #15
#**********argument
"""
-形参:形式参数.在定义函数时,函数名称后面括号中的变量
-实参:实际参数.调用函数时,传递给函数的参数
"""
def add(x,y):
    return x + y

add(5,5)  #10

#poistion argument(位置参数)
#python将命令行上的未知参数,保存到了sys模块的argv列表中.
#注意,未知参数接受的全部是字符串类型
#vim position.py
import sys

print(sys.argv)

"""
(nsd1906) [root@room8pc16 day03]# python position.py
['position.py']
(nsd1906) [root@room8pc16 day03]# python position.py hao 123
['position.py', 'hao', '123']
"""
#*******default argument***********
#具有默认值的参数
def pstar():
    print('*'*30)

pstar()  #函数只能打印30个*
'********************'
def pstar(n): #传参,n的值就是*号的个数
    print('*'*n)

pstar(40)
'******************************'

def pstar(n=30):  #提供默认参数
    print('*' * n)

pstar()  #不传参,n使用默认的30
'***********************'
pstar(15)  #传参,n使用传递进来的15
'*************'

#**********module
"""
-当代码量增加时,可以考虑把代码放到不同的文件里
-每个以.py作为结尾的文件被称作模块文件
-文件是代码的物理组织形式
-模块是代码的逻辑组织形式.模块文件,将扩展名.py去掉就是模块名
"""
#模块导入方法
import time #直接导入;常用
time.time()
'Sat Nov 2 15:45:46 2019'

#从模块中导入一部分功能,常用
from random import randint, choice
randint(1,100) #9
choice('abcde') #'e'
#一行到入多个模块,不常用,因为可读性差
import os, sys

#导入模块的同时,为模块创建别名,不常用
import getpass as gp
p = gp.getpass
'Password:'
#自定义模块
#vim star.py
hi = 'hello world!'

def pstar(n=30):
    print('*'*n)

#vim call_star.py
import star

print('this is call_star')
star.pstar()
print(star.hi)

#python call_star.py
"""模块的特性
-导入模块时,模块内的代码将会执行一遍.
-模块中的代码,有时希望它在作为一个脚本文件直接运行时执行;希望它被当成模块导入时,不要执行,这个
时候可以使用__name__属性
-__name__是一个特殊的变量,它的值有两个
    1.当程序文件直接运行时,值是__main__
    2.当程序文件作为模块导入时,值是模块名
"""
#练习:生成随机字符串
"""
1.决定从哪些字符中随机选取
2.个不要求选n次
3.把这n个字符拼接起来
"""
#day04
"""
-查看python的帮助:https://docs.python.org/zh-cn/3/ -> 标准库参考
在标准库参考页面中,'内置函数'就是内键.还可以按ctrl+f搜索模块
"""
#****************************常用喜用模块
#********shutil:实现文件的复制 剪切 删除等操作
import shutil
# 通过文件对象拷贝文件
f1 = open('/etc/shadow','rb')
f2 = open('/tmp/sd','wb')
shutil.copyfileobj(f1,f2)
f1.close()
f2.close()

#直接拷贝文件
shutil.copy('/etc/hosts', '/tmp')
'/tmp/hosts'

#拷贝目录
shutil.copytree('/etc/security','/tmp/anquan')

#移动
shutil.move('/tmp/anquan','/var/tmp/anquan')

#删除目录
shutil.rmtree('/var/tmp/anquan')

#改变文件的属组属主
shutil.chown('/tmp/sd',user='bob',group='bob')
help(shutil.chown)

#*************subprocess module
#subprocess模块:可以调用任何的系统命令
import subprocess

subprocess.run('ls -a ~bob', shell=True)
#执行系统命令,将输出保存到stdout变量中,错误信息保存到stderr变量中
result = subprocess.run('ls -a ~bob',shell=True,stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
print(result.stdout)
print(result.stderr) #b''
print(result.returncode) #即$?
'0'

result1 = subprocess.run('id natasaha',shell=True,stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
print(result1.stderr) #b'id: natasha: no such user\n'
#************Python其他语法风格
#链式多重赋值
a = b = 10
print(a) #10
print(b) #10
b = 20
print(b) #20
print(a) #10
alist = blist = [1,2]
print(alist) #[1,2]
print(blist) #[1,2]
blist[0] = 10
print(blist) #[10,2]
print(alist) #[10,2]
#多元赋值(必须前后对号)
a, b = 'xy'
c, d = (10, 20)
e, f = ['hello','world']
g, h = 100,200
print(a) #x
print(b) #y
print(c) #10
print(d)  #20
print(e) #hello
print(f) #world
print(g) #100
print(h) #200
#交换两个变量的值
a, b = 1, 100
print(a) #1
print(b) #100
t = a #其他语法写法
a = b
b = t
print(a) #100
print(b) #1
a, b = b, a #Python写法
print(a) #1
print(b) #100
"""标识符
-各种各样的名称,如变量 函数 模块 类 统称为标识符
-和发表师傅需要满足的条件:
    1.首字符必须是字母或下划线
    2.其他字符是字母,下划线或数字
    3.区分大小写
"""
"""关键字
-为了实现python语法,python保留了一些名字,叫关键字
-关键字不能被覆盖
"""
import keyword #关键字模块
print(keyword.kwlist)
"""
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def',
'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in',
'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with',
'yield']
"""
print('pass' in keyword.kwlist) #True
print(keyword.iskeyword('pass')) #True
#***********内建
"""
-内建不是关键字
-但是内建也不建议覆盖
"""
type(len)
'<class 'builtin_function_or_method'>'
len('abcd') #4
len = 10 #将len定义为变量,赋值10
len('abcd') #报错,因为len已不再是函数,等价于下面的10('abcd')
"""Error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callabl
"""
10('abcd')
"""Error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callabl
"""
#*********module file 布局
#!/usr/env python3 #解释器
"""模块说明文档

用于help帮助时显示
"""

import os #模块导入
import time

debug =True
