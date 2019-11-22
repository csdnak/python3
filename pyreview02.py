#!/bin/env python3
#-*- coding:utf8 -*-
#复习python3第二天
py_str = 'python'
print(len(py_str)) #计算长度
print(py_str[0])  #取出下标为0的字符
py_str[6]  #下标超出范围将会报错
py_str[2:6] #切片 不会出现下标越界的错误
py_str[2:] #结束不写,表示取到尾
py_str[:2] #开头不写,表示从开头取
py_str[::2] #切片默认步长值为1,改为2 结果为'pto'
py_str[::-1]  #步长值为负,表示从右向左取
'abc' + '123'  #字符串拼接
py_str + 'good'
#************list
#列表与字符串类似 都是序列对象
alist = [1,2,3,'tom','jerry']
print(len(alist))
alist[0]
alist[3:]  #['tom','jerry']
3 in alist #True
'o' in alist #False
alist + [10, 20] #[1, 2, 3, 'tom', 'jerry', 10, 20]
alist * 2 #[1, 2, 3, 'tom', 'jerry', 1, 2, 3, 'tom', 'jerry']
alist.append('bob') #向列表尾部追加一个字符串
alist #[1, 2, 3, 'tom', 'jerry', 'bob']
#*********tuple
#元组:可以认为它是不可变的列表
atup = (1,2,3,'bob','tom')
print(len(atup)) #5
atup[0] #1
atup[3:] #('bob','tom')
print(alist) #[1, 2, 3, 'tom', 'jerry', 'bob']
alist[0] = 10 #列表可变,可以吧元素重新赋值
print(alist) #[10, 2, 3, 'tom', 'jerry', 'bob']
atup[0] = 10 #元组不可变,所以不能把它的元素重新赋值
"""Error:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
"""
#*********dictionary
#dictionary采用的是key:value形式
adict = {'name': 'tom', 'age': 20}
print(len(adict)) #2
adict[0] #字典是无序的,所以没有下标
"""Error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 0
"""
print('tom' in adict)  #tom是字典的key么? (False)
print('name' in adict)  #True
adict['name']  #通过key来找到val(tom)
"""数据类型的特点
-按存储模型分类
    1.标量:数据中不能包含其他类型数据
    2.容器:可以包含其他类型的数据.列表、元组、字典
-按更新模型分类
    1.不可变:数字、字符串、元组
    2.可变:列表、字典
-按访问模型分类
    1.直接:数字
    2.顺序:字符串、列表、元组
    3.映射:字典
"""
#**********判断
#syntax
if 判断条件:
    如果条件为真才执行的语句块
else:
    判断条件为假才执行的语句块
"""可以用数据类型作为判断条件
    1.任何值为0的数字都是假,非0为真
    2.任何非空对象都是真,空是假
"""
#**********while循环
while 条件:
    如果条件为真则