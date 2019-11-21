#!/bin/env python3
#-*- coding:utf8 -*-
#复习python第一天
#*********print(output sentence)
print('hello world!') #字符串必须用引号引起来,单双引号无区别
print('hao',123)  #打印多项,用逗号分隔,输出时各项间默认是空格
print('hao', 123, sep='***')  #设置输出的各项间以***做为分隔符
print('hao' + 123)  #字符串和数字不能拼接,报错
"""output:
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: must be str, not int
"""
print('hao' + '123')   #字符串拼接用+
#**********input(input sentence)
user = input('username: ')
print(user)
n = input('number: ') #input读入一定是字符串
print(n)
print(n + 5)  #n为字符串,所以不能和数字5做运算
"""Error:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int
"""
print(int(n) + 5) #int将字符串形式的数字转成真正的数字
print(n + str(5)) #str将对象转成字符串(结果就成了字符串拼接了)
#***********variable
"""
-可变化的两是变量,如a = 10 ,以后还可以改变它,a = 100
-与变量相反的是字面量,如字符串"hello",数字100,都是字面量
-写程序时,如果总是用字面量,就是硬编码.
-合法变量名的要求:
    1.首字符必须是字母或下划线
    2.其他字符可以是数字 字母 下划线
    3.区分大小写
-推荐的名称写法
    1.变量名全部用小写,尽量有意义,pythonstring
    2.简短,pystr
    3.多个单词间用下划线分隔,py_str
    4.变量名用词,如phone;函数名用谓词(动词+名词),update_phone
    5.类名采用驼峰的形式,MyClass
-变量赋值自右向左进行,将=右边表达式的计算结果赋值给左边的变量
-变量使用之前必须赋值
"""
a = 10
a = a + 5
print(a)  #15
a += 5
print(a)  #20
a -= 10
print(a) #10
a *= 2
print(a) #20
print(b + 5) #变量b没有赋初值,将会出现名称错误
"""Error:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'b' is not defined
"""
"""python之禅(当练习手速准确率了)
The Zen of Python, by Tim Peters

Beautiful is better than ugly. #美胜丑
Explicit is better than implicit. #明胜暗
Simple is better than complex.  #间胜繁
...
"""
#***************operator(运算符)
print(5/3) #1.6666666666666667
print(5//3) #只保留商(1)
print(5 % 3)  #求余,模运算(2)
divmod(5, 3) #5/3返回商和余数(//的结果,%的结果)(1, 2)
a, b = divmod(5, 3)
print(a) #1
print(b) #2
print(2**3) #2的三次方,幂运算(8)
print(3 ** 4) #3的四次方 (81)
#***************compare-operator(比较运算符):result(True或False)
#3 = 3是赋值不是比较
"""Error
File "<stdin>", line 1
SyntaxError: can't assign to literal
"""
print(
    3 == 3 #比较必须使用==表示判断是否相等
)
print(
    10 > 5 > 1  #python支持连续比较
)
print(
    20 > 10 < 30  #相当于是20 > 10 and 10 < 30
)
#*************logic-operator(逻辑运算符):result(True或False)
print(10> 50 and 2 < 5)  #False
print(10 > 5 and 2 < 5)  #and两边全为True,最终才是True
print(10 > 50 or 2 < 5)  #or两边只要一边为True就是True
print(2 * 3**2)  #18
print(2 * (3 ** 2))   #18
print(not 10 > 50 or 2 < 5) #涉及到可读性差的代码,应该加()
print((not 10 > 50) or 2 < 5)   #提高代码可读性
print(not 10 > 3 )  #not是取反,真变假,假变真(真亦是假亦真)
#**********data type summary(数据类型概述)
#digit
print(type(1.3))  #有小数点浮点数
print(type(10))  #没有小数点为整数
print(True + 1) #2
print(False * 5)  #0
#python默认使用十进制数字表示数字
#如果以0o或0O开头表示8进制数
print(0o11) #9
print(oct(10))  #将十进制数转为八进制数
print(0x11)  #十六进制数以0x开头(17)
print(hex(20))  #十进制转换16进制
print(0b11)  #二进制数以0b开头
print(bin(7))  #十进制转换成二进制(0b111)
#***********character-string(字符串)
#三引号就是三个连续的单引号或双引号
words = "hello  #希望每个单词占一行,但是不能直接回车,写到下一行
"""
File "<stdin>", line 1
  words = "hello
               ^
               
SyntaxError: EOL while scanning string literal
"""
words = 'hello
File "<stdin>", line 1
words = 'hello
             ^

SyntaxError: EOL while scanning string literal
words = "hello\nwelcome\ngreet"
print(words)  #print将\n转义成回车
#三引号可以保存用户的输入格式
wds = """hello
welcome
greet"""