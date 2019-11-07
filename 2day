#!/bin/env python3
#-*- coding:utf8 -*-
#学python3的第二天
#语法结构\
# py_str = 'Python'
# if 'th' in py_str:
#     print('th在%s'% py_str)
# if -0.0:
#     print('值为0的数字为假')
# if ' ':
#     print('空格也是个字符,为真')
# if []:
#     print('空列表为假') #空的都不打印
# if ['']:
#     print('列表不为空所以打印')
# if (1,2):
#     print('非空元组打印')
# if {'name': 'bob'}:
#     print('非空字典打印')
# if not {}:
#     print('空字典为假,取反打印')
# if not None:
#     print("None表示空对象,类似于mysql中的null,为假,取反为真")
# #知识简用:阿坤的QQ号位数截取
# num = input("Please input number: ")
# if num == 1:
#     n = input('Please a n[]')
#     if n == 9:
#         print('This is QQ NO.1 number 9!')
#     print('This is number one!')
# elif  num == 2:
#     n2 = input('Please a n[]')
#     if n2 == 7:
#         print('This is QQ NO.2 number 7!')
#     print('This is number two!')
# elif  num == 3:
#     n3 = input('Please a n[]')
#     if n3 == 4:
#         print('This is QQ NO.3 number 4!')
#     print('This is number three!')
# elif  num == 4:
#     n4 = input('Please a n[]')
#     if n4 == 8:
#         print('This is QQ NO.4 number 8!')
#     print('This is number four!')
# elif  num == 5:
#     n5 = input('Please a n[]')
#     if n5 == 5:
#         print('This is QQ NO.5 number 5!')
#     print('This is number five!')
# elif  num == 6:
#     n6 = input('Please a n[]')
#     if n6 == 2:
#         print('This is QQ NO.6 number 2!')
#     print('This is number six!')
# elif  num == 7:
#     n7 = input('Please a n[]')
#     if n7 == 7:
#         print('This is QQ NO.7 number 7!')
#     print('This is number seven!')
# elif  num == 8:
#     n8 = input('Please a n[]')
#     if n8 == 2:
#         print('This is QQ NO.8 number 2!')
#     print('This is number eight!')
# elif  num == 9:
#     n9 = input('Please a n[]')
#     if n9 == 7:
#         print('This is QQ NO.9 number 7!')
#     print('This is number nine!')
# else:
#     print('Please input options!')
# #方法一
# a = 10
# b = 20
# if a < b:
#     s1 = a
# else:
#     s1 = b
# print('s1=%s'% s1)
# #方法二(今后必须掌握)
# s2 = a if a < b else  b
# print('s2=%s'% s2)
# #案例一
# import getpass #导入getpass模块(不会明文显示密码)
#
# uname = input('username: ')
# upass = getpass.getpass('password: ')
#
# if uname == 'bob' and upass == '123456':
#     print('\033[1;32mWelcome go home %s\033[0m'% uname) #显示高亮度绿色
# else:
#     print('\033[1;31mError: username or password is Null!\033[0m') #显示高亮度红色
# #案例二 grade.py
# #方法一:常规
# grade = input('Please input your grade: ')
# gd = int(grade)
# if gd >= 90:
#     print('\033[1;32m恭喜你成绩优秀！\033[0m')
# elif gd >= 80:
#     print('\033[1;33m恭喜你成绩优秀！\033[0m')
# elif gd >= 70:
#     print('\033[1;34m恭喜你成绩良好!\033[0m')
# elif gd >= 60:
#     print('\033[1;35m恭喜你成绩合格!\033[0m')
# else:
#     print('\033[1;31m成绩不合格!!\033[0m')
# #方法二:区间
# score = int(input('分数: '))
#
# if 60 <= score < 70:
#     print('及格')
# elif 70 <= score < 80 :
#     print('良好')
# elif 80 <= score < 90 :
#     print('优秀')
# else:
#     print('你要努力了')
# #方法三:and
# score = int(input('分数: '))
#
# if score <= 60 and score < 70:
#     print('及格')
# elif score <= 70 and score < 80 :
#     print('良好')
# elif score <= 80 and score < 90 :
#     print('优秀')
# else:
#     print('你要努力了')
# #猜拳游戏
# #思路:人的三种情况(结构)+每种情况下出现的子情况=计算机的三种情况(内嵌)
# #方法一:常规
# import random #导入随机模块
#
# all_choices = ['石头','剪刀','布']
# computer = random.choice(all_choices)
# player = input('请出拳(石头/剪刀/布): ')
#
# if player == '石头':
#     if computer == '石头':
#         print('It ends in a draw!')
#     elif computer == '剪刀':
#         print("You Win!")
#     else:
#         print('Game Over!')
# elif player == '剪刀':
#     if computer == '石头':
#         print('Game Over!')
#     elif computer == '剪刀':
#         print("It ends in a draw!")
#     else:
#         print('Game Over!')
# else:
#     if computer == '石头':
#         print('You Win!')
#     elif computer == '剪刀':
#         print("Game Over!")
#     else:
#         print('It ends in a draw!')
# if '': #如果用户不输入
#     print('Please input options!!!')
# #方法二:自己的方法
# import random #导入随机模块
#
# all_choices = ['石头','剪刀','布']
# win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]
# computer = random.choice(all_choices)
# player = input('请出拳(石头/剪刀/布): ')
# result = 'It ends in a draw!' if computer == player else ('WIN!' if [player,computer] in win_list else 'LOSE!')
#
# print('You %s'% result)
# #方法三:张老师版本
# import random #导入随机模块
#
# all_choices = ['石头','剪刀','布']
# #人在前,计算机在后,组成小列表,把人赢的情况再放大到列表中
# win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']] #也可以换成lose_list/draw_list
# computer = random.choice(all_choices)
# player = input('请出拳(石头/剪刀/布): ')
#
# print("Your choice: %s, computer's choice: %s"% (player,computer))
# if player == computer:
#     print('It ends in a draw!')
# elif [player,computer] in win_list:
#     print('You WIN!!!')
# else:
#     print('You LOSE!!!')
# #优化版本
# import random #导入随机模块
#
# all_choices = ['石头','剪刀','布']
# #人在前,计算机在后,组成小列表,把人赢的情况再放大到列表中
# win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']] #也可以换成lose_list/draw_list
# prompt = """(0)石头
# (1)剪刀
# (2)布
# 请选择(0/1/2): """
# computer = random.choice(all_choices)
# ind = int(input(prompt)) # 将用户输入的数字字符转为数字
# player = all_choices[ind] # 将数字作为下标从列表中取出元素
#
# print("Your choice: %s, computer's choice: %s"% (player,computer))
# if player == computer:
#     print('It ends in a draw!')
# elif [player,computer] in win_list:
#     print('You WIN!!!')
# else:
#     print('You LOSE!!!')
# #优化版本2
# import random #导入随机模块
#
# all_choices = ['石头','剪刀','布']
# #人在前,计算机在后,组成小列表,把人赢的情况再放大到列表中
# win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']] #也可以换成lose_list/draw_list
# prompt = """(0)石头
# (1)剪刀
# (2)布
# 请选择(0/1/2): """
# pwin = 0 #　人的计分板
# cwin = 0 #　计算机的计分板
#
# while pwin < 2 and  cwin < 2:
#     # 人和计算机都没有赢够两次则继续
#     computer = random.choice(all_choices)
#     ind = int(input(prompt)) # 将用户输入的数字字符转为数字
#     player = all_choices[ind] # 将数字作为下标从列表中取出元素
#
#     print("Your choice: %s, computer's choice: %s"% (player,computer))
#     if player == computer:
#         print('\033[1;32mIt ends in a draw!\033[0m')
#     elif [player,computer] in win_list:
#         print('\033[1;31mYou WIN!!!\033[0m')
#         pwin += 1 #　人赢得时候,计算器加1(人计分板)
#     else:
#         print('\033[1;31mYou LOSE!!!\033[0m')
#         cwin += 1 # 计算机赢的时候,计算器加1(计算机计分板)
# #1)
# import random #导入随机模块
#
# all_choices = ['石头','剪刀','布']
# #人在前,计算机在后,组成小列表,把人赢的情况再放大到列表中
# lose_list = [['剪刀','石头'],['布','剪刀'],['石头','布']]
# computer = random.choice(all_choices)
# player = input('请出拳(石头/剪刀/布): ')
#
# print("Your choice: %s, computer's choice: %s"% (player,computer))
# if player == computer:
#     print('It ends in a draw!')
# elif [player,computer] in lose_list:
#     print('You LOSE!!!')
# else:
#     print('You WIN!!!')
# #2)
# import random #导入随机模块
#
# all_choices = ['石头','剪刀','布']
# #人在前,计算机在后,组成小列表,把人赢的情况再放大到列表中
# peace_list = [['石头','石头'],['剪刀','剪刀'],['布','布']] #也可以换成lose_list/draw_list
# win_list   = [['石头','剪刀'],['剪刀','布'],['布','石头']]
# computer = random.choice(all_choices)
# player = input('请出拳(石头/剪刀/布): ')
#
# print("Your choice: %s, computer's choice: %s"% (player,computer))
# if [player,computer] in win_list:
#     print('You WIN!')
# elif [player,computer] in peace_list:
#     print('It ends in a draw!!!')
# else:
#     print('You LOSE!!!')
# #午间练习:时长两小时
# print('hello world!')
#
# if 3 > 0:
#     print('OK')
#     print('yes')
#
# x = 3;y = 4 #不推荐,还是应该写成两行,可读性差
# print(x + y)
# print('hello world!')
# print('hello','world')
# print('hello' + 'world')
# print('hello','world',sep='***') #单词间用***分隔
# print('#'*50) #*号表示重复50遍
# print('How are you?',end='') #默认print会打印回车,end=''表示不要回车
# print(5/2) #2.5
# print(5//2) #丢弃余数,只保留商
# print(5%2) #求余数
# print(5**3) #5的3次方
# print(5>3) #返回True
# print(3 > 5) #返回False
# print(20 > 10 > 5) #python支持连续比较
# print(20 > 10 and 10 > 5) #与上面相同含义
# print(not 20 > 10) #False
# number = input('Please input number: ') #input用于获取键盘输入
# print(number)
# print(type(number)) #input 获得的数据是字符型
#
# print(number + 10) #报错,不能把字符和数字做运算
# print(int(number) + 10) #int 可以将字符串10转换成数字10
# print(number + str(10)) #str将10转换为字符串后实现字符串拼接
# username = input('username: ')
# print('welcome',username) #print各项间默认以空格作为分隔符
# print('welcome' + username) #注意引导号内最后的空格
#
# sentence = 'tom\'s pet is a cat' #单引号中间还有单引号,可以转译
# print(sentence)
# sentence2 = "tom's pet is a cat" #也可以用双引号包含单引号
# print(sentence2)
# sentence3 = "tom said:\"Hello World!\""
# print(sentence3)
# sentence4 = 'tom said:"Hello World!"'
# print(sentence4)
# #三个连续的单引号或双引号,可以保存输入格式,允许输入多行字符串
# words ="""
# hello
# world
# abcd"""
# print(words)
#
# py_str='python'
# print(len(py_str)) #取长度
# print(py_str[0]) #第一个字符
# print('python'[0])
# print(py_str[-1]) #最后一个字符
# #py_str[6] #错误,下标超出范围
# print(py_str[2:4]) #切片取法,起始下标包含,结束下标不包含
# print(py_str[2:]) #从下标为2的字符取到结尾
# print(py_str[:2]) #从开头取到下标是2之前的字符
# print(py_str[:]) #取出全部
# print(py_str[::2]) #步长值为2,默认是1
# print(py_str[1::2]) #取出yhn
# print(py_str[:-1]) #步长为负,表示自右向左取
#
# print(py_str + 'is good ') #简单的拼接到一起
# print(py_str *3) #把字符串重复3遍
#
# print('t' in py_str) # True
# print('th' in py_str) # True
# print('to' in py_str) # False
# print('to' not in py_str) # True
#循环语句
#能预知循环次数就用for,反之用while
# result = 0 # 创建变量用于保存累加的结果
# counter = 1 #　创建计数器,将其值累加到result中
# #0+....+100=5050
# while counter <= 100:
#     result += counter #result: 1
#     counter += 1      # counter: 2
# print(result)
# #现学现卖
# import getpass
#
# while True:
#     usr = input('username: ')
#     if usr == '':
#         print('\033[1;31mUsername not NULL!!!\033[0m')
#     elif usr == 'csdnak' :
#         pas = getpass.getpass('password: ')
#         if pas == '123456':
#             print('\033[1;32mWelcome %s world!\033[0m' % usr)
#             break
#         else:
#             print('\033[1;31mError: username or password input is False!\033[0m')
#             print('\033[1;33mPlease re-enter!\033[0m')
# #计算100以内偶数之和
# result = 0 # 创建变量用于保存累加的结果
# counter = 1 # 创建计数器,将其值累加到result中
#
# while counter < 100:
#     counter += 1
#
#     # if counter % 2 == 1:
#     if counter % 2: # 结果只有1或0,1为真,0为假
#         continue
#
#     result += counter
#
# print(result)
# #猜字游戏
# import random
#
# number = random.randint(1,100)
# counter = 0
# #print(number) #开挂
# while counter < 5:
#     counter += 1
#     answer = int(input('guess(1-100): '))
#     if answer > number:
#         print('猜大了')
#     elif answer < number:
#         print('猜小了')
#     else:
#         print('猜对了')
#         break
# else:
#     #循环也有else语句,如果循环被break,else不执行,否则执行
#     print('这个数是: %s' % number)
# #for循环
# s1 = 'hello'
# nums = [10,20,15,80]
# names = ('tom', 'jerry')
# user = {'name': 'bob','age': 20}
#
# for st in s1:
#     print(st)
# print('*' * 50)
#
# for i in nums:
#     print(i)
# print('*' * 50)
#
# for name in names:
#     print(name)
# print('*' * 50)
#
# for usr in user:
#     print(usr,user[usr])
# print('*' * 50)
# #for循环常与range连用
# print(range(10)) # range只是一个对象,潜在可以生成很多数
# #range没有给起始值,从0开始,结束数字不包含
# for i in range(10):
#     print(i)
#
# #将range转换成列表在打印
# print(list(range(10)))
#
# for n in list(range(10)):
#     print(n)
# print('*' * 50)
#
# #打印6到10的列表
# print(list(range(6,11)))
# #倒着打印10到1
# print(list(range(10,0,-1)))
#
# for number in list(range(6,11)):
#     print(number)
# #如果直接用列表显示,数字多的话就会霸屏
# print(list(range(10000)))
# #神奇的菲波那切数列
# fib = [0, 1]
#
# for i in range(8):
#     fib.append(fib[-1] + fib[-2]) #只能是-1,-2 因为后面的两位一直在变(是向后延伸的)
# print(fib)
#打印9x9乘法表
"""
原理:
i取值[1,2,3]
i == 1, j取值[1,2,3]
i == 2, j取值[1,2,3]
...
print默认会在结束打印换行,可以使用end=' '替换为空格
"""
# #实例:
# for i in range(1,4):
#     for j in range(1,i + 1):
#         print('hello',end=' ')
#     print() #用来起到换行作用(print默认在结束时自带换行)
# #具体实现
# for i in range(1,10):
#     for j in range(1,i + 1):
#         print(j,"x",i,"=",i*j,end='  ') #根据外观调试i和j调换了顺序
#     print()
# #优化版9*9
# for i in range(1,10): # [1,2,3...9]
#     for j in range(1,i + 1): # [1,2,3...9]
#         print('%sx%s=%s' % (j ,i ,i * j),end=' ')
#     print()
# #列表解析
# print([5])
# print([5 + 2]) #　将表达式到列表
# print([5 + 2 for i in range(1,11)]) # 循环决定表达式计算的次数
# print([5 + i for i in range(1,11)]) # 在表达式中用循环的变量
# #从中抽出了i = [1,3,5,7,9]
# print([5 + i for i in range(1,11) if i %2]) # 判断条件作为过滤条件(1为真0为假不输出所以i%2==1和i%2结果一样)
# print(['192.168.1.%s' % i for i in range(1,255)])
#晚间联系:时长两小时
# alist = [10,20,30,'bob','alice',[1,2,3]]
# print(alist)
# print(alist[-1]) #取出最后一项
# print(alist[-1][-1]) #因为最后一项是列表,列表还可以继续取下标
# print([1,2,3][-1]) #[1,2,3]是列表,[-1]表示列表最后一项
# print(alist[-2][2]) #列表倒数第2项是字符串,在取出字符下标为2的字符
# print(alist[3:5]) #['bob','alice']
# print(10 in alist) #True
# print('o' in alist) #False
# print(100 not in alist) #True
# #修改最后一项的值
# alist[-1] = 100
# print(alist)
# #向列表中追加一项
# alist.append(200)
# print(alist)
#
# atuple = (10,20,30,'bob','alice',[1,2,3]) #元祖与列表基本上是一样的,只是元祖不可变列表可变.
# print(len(atuple))
# print(10 in atuple)
# print(atuple[2])
# print(atuple[3:5])
# #atuple[-1]= 100 ,这样写是不对的(元组是不可变的)
#
# #字典是key-value键值对形式的,没有顺序,通过键值取出值(key来取value)
# adict = {'name':'csdnak' ,'age':23}
# print(len(adict))
# print('csdnak' in adict) #False
# print('name' in adict) #True
# adict['email']= 'csdnak@github.cn' #字典中没有key,则添加新项目
# print(adict)
# adict['age']= 25 #字典中已有key,修改对应的value
# print(adict)
#
# if 3 > 0:
#     print('yes')
#     print('ok')
#
# if 10 in [10,20,30]:
#     print('ok')
#
# if -0.0:
#     print('yes') #任何值为0的数字都是False
#
# if [1,2]:
#     print('yes') #非空对象都是True
#
# if '':
#     print('yes') #空格字符也是义字符,条件为True
#
# a = 10
# b = 20
#
# if a < b:
#     smaller = a
# else:
#     smaller = b
#
# print(smaller)
#
# s = a if a < b else b #和上面的if-else语句等价
#
# print(s)
#
#
# import getpass #导入模块
#
# username = input('username: ')
# #getpass模块中,有一个方法也叫getpass
# password = getpass.getpass('password: ')
#
# if username == 'csdnak' and password == '123456':
#     print('Login successful!')
# else:
#     print('Login incorrect')
#
# import random
#
# num = random.random(1,10) #随机生成1-10之间的数字
# answer = int(input('guess a number: ')) #将用户输入的字符转换成整数
# if answer > num:
#     print('猜大了')
# elif answer < num:
#     print('猜小了')
# else:
#     print('猜对了')
#
# print('the number: ',num)
#
#
# score = int(input('分数: '))
#
# if score >= 90:
#     print('优秀')
# elif score >= 80:
#     print('好')
# elif score >= 70:
#     print('良好')
# elif score >= 60:
#     print('及格')
# else:
#     print('你要努力了')
#
# if score >= 60 and score < 70:
#     print('及格')
# elif 70 <= score < 80:
#     print('良好')
# elif 80 <= score < 90:
#     print('优秀')
# else:
#     print('你要努力了')
#
#
# import random
#
# all_choices = ['石头','剪刀','布']
# computer = random.choice(all_choices)
# player = input('请出拳: ')
#
# #print('Your choice: ',player,"Computer's choice: ",computer)
# print("Your choice: %s,Computer's choice: %s"% (player,computer))
# if player == '石头':
#     if computer == '石头':
#         print('平局')
#     elif computer == '剪刀':
#         print('你赢了')
#     else:
#         print('You LOSE ')
# elif player == '剪刀':
#     if computer == '石头':
#         print('You LOSE')
#     elif computer == '剪刀':
#         print('平局')
#     else:
#         print('You WIN!!!')
# else:
#     if computer == '石头':
#         print('You WIN!!')
#     elif computer == '剪刀':
#         print('You LOSE!!!')
#     else:
#         print('平局')
#
# import random
#
# all_choices = ['石头','剪刀','布']
# win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]
# prompt = """(0)石头
# (1)剪刀
# (2)布
# 请选择(0/1/2)"""
# computer = random.choice(all_choices)
# ind = int(input(prompt))
# player = all_choices[ind]
#
# print("'Your choice: %s,Computer's choice: %s" % (player,computer))
# if player == computer:
#     print("\033[32;1m平局\033[0m])]")
# elif [player,computer] in  win_list:
#     print('\033[31;1mYou WIN!!!\033[0m')
# else:
#     print('\033[31;1mYou LOSE!!!\033[0m')
#
# import random
#
# num = random.randint(1,10)
# running = True
#
# while running:
#     answer = int(input('guess the number: '))
#     if answer > num:
#         print('猜大了')
#     elif answer < num:
#         print('猜小了')
#     else:
#         print('猜对了')
#         running = False
#
# import random
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
#     counter += 1
# else: #循环被break就不执行了,没有被break才执行
#     print('the number is: ',num)
#
#
# sum100 = 0
# counter = 1
#
# while counter < 101:
#     sum100 += counter
#     counter += 1
#
# print(sum100)
#
#
# while True:
#     yn = input('Continue(y/n)')
#     if yn in ['n','N']:
#         break
#     print('running...')
#
# sum100 = 0
# counter = 0
#
#
# while counter < 100:
#     counter += 1
#     #if counter % 2:
#     if counter % 2 ==1:
#         continue
#     sum100 += counter
#
# print(sum100)
#
# astr = 'hello'
# alist = [10,20,30]
# atuple = ('bob','tom','alice')
# adict = {'name':'john','age':'23'}
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
# for i in range(1,10): # [1,2,3...9]
#     for j in range(1,i + 1): # [1,2,3...9]
#         print('%sx%s=%s' % (j ,i ,i * j),end=' ')
#     print()
# #菲波那切数列
# fib = [0, 1]
# for i in range(8):
#     fib.append(fib[-1] + fib[-2])
# print(fib)
