#!/bin/env python3
#-*- coding:utf8 -*-
#复习python第四天
#!/usr/bin/python3
# 解释器
"""模块说明文档
用于help帮助时显示
"""
import os
# 模块导入
import time
debug = True
hi = 'Hello World' #全局变量的定义

class MyClass: #类的定义
    pass

def func1(): #函数声明
    pass

if __name__ == '__main__':
    mc = MyClass()

#**********编程思路***************
#1.发呆.思考程序的运行方式:交互?费交互?
#python mkfile.py
"""
文件名: /etc/hosts
文件已存在,请重试。
文件名: /etc
文件已存在,请重试。
文件名: /tmp/abc.txt
请输入文件内容,单独输入end表示结束。
(end to quit)> Hello World!
(end to quit)> How are you?
(end to quit)> the end
(end to quit)> end
# ls /tmp/abc.txt
abc.txt
# cat /tmp/abc.txt
Hello World!
How are you?
the end
"""
#2.思考程序由哪些功能构成,将这些功能变成函数.
def get_fanme():
    pass

def get_content():
    pass

def wfile(fname, content):
    pass

#3.编写主程序,按一定的规则调用函数
def get_fname():
    '返回一个文件名字符串'

def get_content():
    '返回我呢间内容的字符和攒里偶尔表'

def wfile(fname, content):
    '将content中内容写入文件fname中'

if __name__ == '__main__':
    fname = get_fname()
    content  get_content()
    wfile(fname, content)

#4.编写每个函数
#序列对象
#list 将对象转成列表
list('abc') #['a','b','c']
list(range(10)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#tuple将对象转成元组
tuple('abc') #('a', 'b', 'c')
tuple(range(10))  #(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
#str将对象转成字符串
str(10) #'10'

#reversed函数用于反转对象
from random import randint
nums = [randint(1,100)for i in range(10)]
print(nums) #[68, 48, 98, 78, 43, 78, 94, 5, 53, 11]
print(reversed(nums)) #<list_reverseiterator object at 0x7f480addcc18>
list(reversed(nums)) #[11, 53, 5, 94, 78, 43, 78, 98, 48, 68]

#sorted函数用于排序
sorted(nums) #[5, 11, 43, 48, 53, 68, 78, 78, 94, 98]

#倒叙
sorted(nums,reverse=True)

#enumerate#可以同时得到下标和值
for data in enumerate(nums):
    print(data)

#分别将下标和值赋值给i和n
for i, n in enumerate(nums):
    print(i,n)

#*********character string
"""字符串
-比较大小,是按照字符的码值比较
-常用的编码有:ASCII、Lantin-1(ISO8859-1)、GB2312、GB18030、GBK、utf8
"""
s = '中'
print(s) #中
s.encode() #将字符(str)转成bytes类型(b'\xe4\xb8\xad')
a = s.encode()
print(a.decode()) #将bytes类型转成str类型
'中'
#****************string operators
#字符串格式化操作符
#基础格式
print("" % ())  #如果字符串中只有一项需要替换,()可以省略
print('%s is %s years old' % ('tom', 20))
'tom is 20 years old'
print('%s is %d years old ' % ('tom', 20)) #%d表示需要用整数进行替换
'tom is 20 years old'
print('%d is %d years old' % ('tom', 20)) #错误,tom转不成整数
print('%8s%5s' %('name', 'age')) #默认右对齐
'    name  age'
print('%8s%5s' % ('tom', 20))
'     tom   20'
print('%-8s%-5s' % ('name','age')) #数字为负表示左对齐
'name    age  '
print('%-8s%-5s' % ('tom', 20))
'tom     20  '

#以下备查
print('%#o' % 10)  #转8进制
'0o12'
print('%#x' % 10)  #转16进制
'0xa'
print('%f' % (5/3))
'1.666667'
print('%.2f' % (5/3)) #保留2位小数
'1.67'
print('%5.2f' % (5/3))  #输出总宽度为5,小数位2位,不够宽度补空格
print('%e' % 10000) #科学计数法
'1.000000e+04'

#字符串格式化还可以使用format方法
print('{} is {} years old'.format('bob', 20))
'bob is 20 years old'
print('{} is {} years old'.format(20, 'bob'))
'20 is bob years old'
print('{1} is {0} years old'.format(20, 'bob'))
'bob is 20 years old'

#字符串方法
#没有字符串方法,判断一个字符串是不是全为数字
a = input('data: ') #data: 1234
for i in a:
    if i  not in '0123456789':
        print(False)
        break
    else:
        print(True)

#用字符串方法判断字符串中所有的字符是否为数字
a = '123a456'
b = '123'
a.isdigit() #False
b.isdigit() #True
s1 = '  hello \n'
s1.strip()  #去除两端空白字符
'hello'
s1.rstrip()  #去除右侧空白字符
'   hello \n'
s1.lstrip()  #去除左侧空白字符
'hello \n'
'hello world hao 123'.split() #切割字符串(['hello', 'world', 'hao', '123'])
'hello.world.hao.123'.split('.') #切割用·分割的字符串(['hello', 'world', 'hao', '123'])
a = ['hello', 'world', 'hao', '123']
print('-'.join(a))  #用-拼接字符串
'hello-world-hao-123'
'hello world'.replace('l', 'a') #将l替换为a
'heaao worad'
'hello'.center(20)  #居中
'       hello       '
'hello'.center(20,'#')
'#######hello#######'
'hello'.ljust(20,'*') #左对齐
'hello***************'
'hello'.rjust(20, '*') # 右对齐
'***************hello'
'hello'.upper() #转大写
'HELLO'
'HELLO'.lower()  #转小写
'hello'
'hao1233'.islower() #字母都是小写的么? #True
'hao1233'.isdigit()  #所有的字符都是数字么? #False
'''
完整的字符串方法参见:https://docs.python.org/zh-cn/3.6/library/stdtypes.html#text-sequence-type-str
'''
#*************list:容器 可变 序列
alist = [10,8,20,365,23,4]
alist[0] = 100
print(alist) #[100, 8 ,20 ,365, 23 ,4]
print(alist[1:3]) #[8,20]
alist[1:3] = [9, 6, 9, 5, 200]
print(alist)  #[100, 9, 6, 9, 5, 200, 365, 23, 4]

#列表方法
alist.append(1000) #追加
alist.append((1,2)) #把元组追加到列表
print(alist)



