#!/bin/env python3
#-*- coding:utf8 -*-
#学python3的第9天
#注意:写程序要解耦(不可藕断丝连)
#标准版的记账程序
# import os
# import pickle
# from time import strftime
#
#
# def save(fname):
#     amount = int(input('金额: '))
#     comment = input('备注: ')
#     date = strftime('%Y-%m-%d')
#     # 从文件中取出全部记录
#     with open(fname, 'rb') as fobj:
#         records = pickle.load(fobj)
#     # 计算最新余额
#     balance = records[-1][-2] + amount
#     record = [date, amount, 0, balance, comment]
#     records.append(record)
#     # 把更新后的列表再次存入文件
#     with open(fname, 'wb') as fobj:
#         pickle.dump(records, fobj)
#
# def cost(fname):
#     amount = int(input('金额: '))
#     comment = input('备注: ')
#     date = strftime('%Y-%m-%d')
#     # 从文件中取出全部记录
#     with open(fname, 'rb') as fobj:
#         records = pickle.load(fobj)
#     # 计算最新余额
#     balance = records[-1][-2] - amount
#     record = [date, 0, amount, balance, comment]
#     records.append(record)
#     # 把更新后的列表再次存入文件
#     with open(fname, 'wb') as fobj:
#         pickle.dump(records, fobj)
#
# def query(fname):
#     # 取出全部的记录
#     with open(fname, 'rb') as fobj:
#         records = pickle.load(fobj)
#
#     # 打印表头
#     print(
#         '%-12s%-8s%-8s%-12s%-20s' % ('date', 'save', 'cost', 'balance', 'comment')
#     )
#     # 打印记录
#     for record in records:
#         print('%-12s%-8s%-8s%-12s%-20s' % tuple(record))
#
# def show_menu():
#     cmds = {'0': save, '1': cost, '2': query}
#     prompt = """(0) save
# (1) cost
# (2) query
# (3) quit
# Please input your choice(0/1/2/3): """
#     fname = 'account.data'
#     init_data = [
#         [strftime('%Y-%m-%d'), 0, 0, 10000, 'init data']
#     ]
#     # 如果文件不存在，把初始化数据写进去
#     if not os.path.exists(fname):
#         with open(fname, 'wb') as fobj:
#             pickle.dump(init_data, fobj)
#
#     while 1:
#         choice = input(prompt).strip()
#         if choice not in ['0', '1', '2', '3']:
#             print('无效的输入，请重试。')
#             continue
#
#         if choice == '3':
#             print('\nBye-bye')
#             break
#
#         cmds[choice](fname)
#
# if __name__ == '__main__':
#     show_menu()
# #改良版本
# import os
# import pickle
# from time import strftime
#
#
# def save(fname):
#     try: #异常情况处理
#         amount = int(input('\033[33;1m金额: \033[0m').strip())
#         comment = input('\033[33;1m备注: \033[0m').strip()
#     except ValueError as echo:
#         print('\033[33;1mInvalid input: %s\033[0m' % echo)
#     except (KeyboardInterrupt, EOFError):
#         print('\n\033[32mBye-bye\033[0m')
#         print('\n\033[32mDone\033[0m')
#         exit()
#     else:
#         date = strftime('%Y-%m-%d')
#         # 从文件中取出全部记录
#         with open(fname, 'rb') as fobj:
#             records = pickle.load(fobj)
#         # 计算最新余额
#         balance = records[-1][-2] + amount
#         record = [date, amount, 0, balance, comment]
#         records.append(record)
#         # 把更新后的列表再次存入文件
#         with open(fname, 'wb') as fobj:
#             pickle.dump(records, fobj)
#     finally:
#         print(strftime('\033[35;1m%Y-%m-%d %H:%M:%S\033[0m'))
#
# def cost(fname):
#     try:
#         amount = int(input('\033[33;1m金额: \033[0m').strip())
#         comment = input('\033[33;1m备注: \033[0m').strip()
#     except ValueError as echo:
#         print('\033[33;1mInvalid input: %s\033[0m' % echo)
#     except (KeyboardInterrupt, EOFError):
#         print('\n\033[32mBye-bye\033[0m')
#         print('\n\033[32mDone\033[0m')
#         exit()
#     else:
#         date = strftime('%Y-%m-%d')
#         # 从文件中取出全部记录
#         with open(fname, 'rb') as fobj:
#             records = pickle.load(fobj)
#         # 计算最新余额
#         balance = records[-1][-2] - amount
#         record = [date, 0, amount, balance, comment]
#         records.append(record)
#         # 把更新后的列表再次存入文件
#         with open(fname, 'wb') as fobj:
#             pickle.dump(records, fobj)
#     finally:
#         print(strftime('\033[35;1m%Y-%m-%d %H:%M:%S\033[0m'))
#
#
# def query(fname):
#     # 取出全部的记录
#     with open(fname, 'rb') as fobj:
#         records = pickle.load(fobj)
#
#     # 打印表头
#     print(
#         '\033[35;1m%-12s%-8s%-8s%-12s%-20s\033[0m' % (
#             'date', 'save', 'cost', 'balance', 'comment'
#         )
#     )
#     # 打印记录
#     for record in records:
#         print('\033[36;1m%-12s%-8s%-8s%-12s%-20s\033[0m' % tuple(record))
#     print(strftime('\033[35;1m%Y-%m-%d %H:%M:%S\033[0m'))
#
# def show_menu():
#     cmds = {'0': save, '1': cost, '2': query}
#     prompt = """\033[32;1m(0) save
# (1) cost
# (2) query
# (3) quit
# Please input your choice(0/1/2/3):\033[0m """
#     fname = 'account.data'
#     init_data = [
#         [strftime('%Y-%m-%d'), 0, 0, 10000, 'init data']
#     ]
#     # 如果文件不存在，把初始化数据写进去
#     if not os.path.exists(fname):
#         with open(fname, 'wb') as fobj:
#             pickle.dump(init_data, fobj)
#
#     while True:
#         try:
#             choice = input(prompt).strip() #加了下标就得用IndexError报错
#         except (ValueError,IndexError) as echo:
#             print('\033[33;1mInvalid input: %s\033[0m' % echo)
#         except (KeyboardInterrupt, EOFError):
#             print('\n\033[32mBye-bye\033[0m')
#             print('\n\033[32mDone\033[0m')
#             print(strftime('\033[35;1m%Y-%m-%d %H:%M:%S\033[0m'))
#             exit()
#         else:
#             if choice not in ['0', '1', '2', '3']:
#                 print('\033[33;1mInvalid input,Try again.\033[0m')
#                 continue
#             if choice == '3':
#                 print('\n\033[32mBye-bye\033[0m')
#                 break
#             cmds[choice](fname)
#
#
#
# if __name__ == '__main__':
#     show_menu()

# #函数引用问题
# def funch1():
#     print('funch 1')
#     funch2()
#
# def funch2():
#     print('funch 2')
#
# if __name__ == '__main__':
#     funch1() #完全没问题
# #函数参数
# def func1(name,age):
#     print('%s is %s years old.'% (name,age))
#
# func1('bob',20) #OK
# func1(20,'bob') #语法ok　语义不对
# func1(age=20,name='bob') #OK
# func1(age=20,'bob') #语法错误 关键字必须在后
# func1(20,name=bob) #Error,name得到了多个值
# func1('bob',age=20) #OK

# #定义参数
# def func1(*args): #变量名前加*可以吧变量变成元组从而达到传多个参数目的
#     print(args)
#
# func1('hao')
# func1('hao',123)
# func1('hao',123,'bob','alice')
#
# def func2(**kwargs):  #**变成字典传参方式key-value支持多个
#     print(kwargs)
#
# func2()
# func2(name='bob')
# func2(name='bob',age=20)

#传参
"""
传参时　*表示把序列对象拆开
传参试　**表示把字典对象拆开
"""
# def funcation(x,y):
#     return x + y
#
# nums = [10,20]
# funcation(*nums) #funcation(10,20)
#
# def funcation2(name,age):
#     print('%s is %s years old.'% (name,age))
#
# adict = {'name': 'alice','age': 18}
# funcation2(**adict) #funcation2(name='alice',age=18)

# #案例:计数游戏
# from random import randint,choice
#
# def add(x,y):
#     return x + y
#
# def sub(x,y):
#     return x + y
#
# def exam():
#     cmds = {'+': add,'-': sub}
#     nums = [randint(1,100)for i in range(2)]
#     nums.sort(reverse=True) #降序排列
#     op = choice('+-') #choice随机选择一个(详细用法看随机密码笔记)
#     #计算标准答案
#     result = cmds[op](*nums) #*可拆分列表
#
#     #提示语,即算式
#     prompt = '%s %s %s = ' % (nums[0],op,nums[1])
#     counter = 0
#     while counter < 3:
#         try:
#             answer = int(input(prompt).strip()[0])
#         except (ValueError,IndexError) as echo:
#             print('Invalid input,Try again: %s' % echo)
#         except (KeyboardInterrupt, EOFError):
#             print('\nBye-bye')
#             print('\nDone')
#             exit()
#         else:
#             if answer == result:
#                 print('Very Good!!!')
#                 break
#             print('Result Error.')
#             counter += 1
#     else:
#         print('%s%s' % (prompt,result))
#
# def main():
#     while True:
#         try:
#             exam()
#             user = input('Continue(y/n)? ').strip()[0]
#         except (ValueError, IndexError) as echo:
#             print('Invalid input,Try again: %s' % echo)
#         except (KeyboardInterrupt,EOFError):
#             print('\nBye-bye')
#             print('\nDone')
#             exit()
#         else:
#             if user in 'nN':
#                 print('\nBye-bye')
#                 break
#
#
# if __name__ == '__main__':
#     main()

# #匿名函数
# #lambda高阶函数用法(匿名函数:跟普通函数一样的效果)
# def add(x,y):
#     return  x + y
# print(add(5,10))
# #可以改写为下面的
# myadd = lambda x, y: x + y
# print(myadd(10,5))
# #实际例子:
# from random import randint, choice
#
# def exam():
#     cmds = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
#     nums = [randint(1, 100) for i in range(2)]
#     nums.sort(reverse=True)  # 降序排列
#     op = choice('+-')
#     # 计算标准答案
#     result = cmds[op](*nums)
#
#     # 提示语，即算式
#     prompt = '%s %s %s = ' % (nums[0], op, nums[1])
#     counter = 0
#     while counter < 3:
#         try:
#             answer = int(input(prompt))
#         except:  # 可以捕获所有异常，但是不推荐
#             print()
#             continue
#
#         if answer == result:
#             print('Very Good!!!')
#             break
#         print('不对哟!!!')
#         counter += 1
#     else:
#         print('%s%s' % (prompt, result))
#
# def main():
#     while 1:
#         exam()
#         try:
#             yn = input('Continue(y/n)? ').strip()[0]
#         except IndexError:
#             yn = 'y'
#         except (KeyboardInterrupt, EOFError):
#             yn = 'n'
#
#         if yn in 'nN':
#             print('\nBye-bye')
#             break
#
# if __name__ == '__main__':
#     main()

#高阶函数filter(高阶函数处理的数据只能print一次 第二次为空:高阶函数又称生成器:只能取一次值)
"""
- 它接受两个参数。filter(func, seq)
- 第一个参数是函数，如func
- 第二个参数是序列对象
- func它必须接受一个参数，返回值必须是True或False
- filter函数工作时，将序列对象中的每个值作为func的参数进行过滤，结果为真的保留，为假的舍弃
"""
# #举例子
# from random import  randint
#
# def funcation(x):
#     return x % 2  #效果和下边等同
#     #return  True if x % 2 == 1 else False
#
# if __name__ == '__main__':
#     nums = [randint(1,100) for i in range(10)]
#     print(nums)
#     result = filter(funcation,nums)
#     print(list(result)) #筛选出来基数
#     result2 = filter(lambda x: not x % 2, nums) #匿名函数与上方正常函数效果一样
#     print(list(result2)) #筛选出来偶数
#     print(list(result2)) #二次print为空
#     print(set(nums))

#map函数
"""
- 它接受两个参数。map(func, seq)
- 第一个参数是函数，如func
- 第二个参数是序列对象
- func它必须接受一个参数，它将接收到的数据进行处理，然后返回
"""
# from random import  randint
#
# def funcation2(x):
#     return x * 2
#
# if __name__ == '__main__':
#     nums = [randint(1,100) for i in range(10)]
#     print(nums)
#     result3 = map(funcation2,nums)
#     print(list(result3))
#     result4 = map(lambda x: x * 2,nums)
#     print(list(result4))
#****************

# #变量
# """
# - 在函数外面定义的变量是全局变量。全局变量从定义开始，到程序结束，任意地方可见可用。
# """
# #****global
# x = 10
# def funcation():
#     print(x)
# #                   ******优先级global>local*****
# print(funcation())
# """
# - 在函数内定义的变量是局部变量。局部变量只能在函数内部使用。
# """
# #****local
# def funcation2():
#     y = 5
#     print(y)
# """
# - 如果局部和全局有同名变量。局部变量将会遮盖住全局变量。
# """
# y = 10
# def funcation3():
#     y = 5
#     print(y)
# """
# - 如果希望通过函数改变全局变量，需要使用关键字global
# """
# #global使用
# def funcation4():
#     global x   #不再是local而是global了
#     x = 100000
#     print(x)
#

#偏函数:固参
"""
- 改造现有函数，生成新函数
- 改造时，可以将现有函数的一些参数固定
"""
# def funcation5(a,b,c,d,e): #函数必须有五个参数
#     return a + b + c + d + e
# print(funcation5(10 ,20 ,30 ,40 ,2)) #每次传参　前4个数固定
#
# from functools import partial
#
# myadd = partial(funcation5,10, 20, 30, 40)
# print(myadd(2))
#
# int2 = partial(int,base=2)  #修改int函数固定base=2值　生成新函数int2(二进制转换十进制)
# print(int2('10')) #2

# #案例2: GUI
# #tkinter 窗口模块
# import tkinter
# root = tkinter.Tk()

#递归函数
#数字阶乘:自己调用自己
"""
5! = 5x4x3x2x1
"""
# def funcation(x):
#     if x == 1:
#         return 1
#     return x * funcation(x - 1)
#
# print(funcation(5)) #120
"""函数流程
5*funcation(4)
 4*funcation(3)
  3*funcation(2)
   2*funcation(1)
    1
"""

#快速排序
# from random import  randint
#
# def quickly_sort(seq):
#     #如果对象的长度是0或1 那么直接返回　不用在排序
#     if len(seq)<2:
#         return seq
#     #假设第一个数是中间值　比他小的放到一个列表
#     #比他大的放到另一个列表
#     middle = seq[0]
#     smaller = []
#     larger = []
#     for i in seq[1:]:
#         if i  <= middle:
#             smaller.append(i)
#         else:
#             larger.append(i)
#     #把各项从小到大拼接　如果对列表继续进行排序
#     return quickly_sort(smaller) + [middle] + quickly_sort(larger)
#
# if __name__ == '__main__':
#     nums = [randint(1,100) for i in range(10)]
#     print(nums)
#     print(quickly_sort(nums))

#生成器:直接把列表解析变成()即可　且只能取一次值
"""
  - 可以通过生成器表达式得到生成器
"""
# from random import randint
#
# nums = (randint(1,100) for i  in range(10))
# for i in nums:
#     print(i)

#使用函数的形式
"""
  - 常规函数通过return返回一个最终结果
  - 生成器通过yield语句，返回多个中间结果
"""
# def mygen():
#     yield 10
#     a = 100 +5
#     yield a
#     yield 200
#
# mg = mygen()
# print(list(mg))
# print(list(mg)) #再次取值就为空[]

#模块
"""导入模块时，python到指定路径下搜寻
- sys.path定义的路径
- PYTHONPATH环境变量定义的路径

"""

# import sys #导入以第一次为准　如果修改了需要退出python重新导入!!
#
# print(sys.path) #查看all变量目录

"""终端操作
#cp qsort.py /var/tmp
#cd /tmp/
#python
>>>import qsort  //报错
#export PYTHONPATH = /var/tmp
#python
>>>import qsort  //成功
"""

#tarfile压缩文件模块
"""

"""
#创建压缩文件
import  tarfile

tar = tarfile.open('/tmp/mytest.tar.gz','w:gz')
tar.add('/etc/hosts') #tar /etc/hosts
tar.close()
#解压,打开时不用指定压缩格式(程序会自动判断)
tar = tarfile.open('/tmp/mytest.tar.gz')
tar.extractall(path='/var/tmp') #解压到制定的目录　默认当前路径
tar.close()

#计算数据的哈希值
import hashlib
m = hashlib.md5(b'123456')
m.hexdigest()
'e10adc3949ba59abbe56e057f20f883e'

with open('/etc/passwd', 'rb') as fobj:
    data = fobj.read()

m = hashlib.md5(data)
m.hexdigest()
'687950834a69d8e7ab0ba9e9111eeb1f'

m = hashlib.md5()
m.update(b'12')
m.update(b'34')
m.update(b'56')
m.hexdigest()
'e10adc3949ba59abbe56e057f20f883e'


