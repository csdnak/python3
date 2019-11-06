#!/bin/env python3
#-*- coding:utf8 -*-
#学python3的第五天
#早晨时刻
# a = input('data: ')
# for i in a:
#     if i not in '0123456789':
#         print(False)
#         break
#     else:
#         print('不是数字')
# alist = [1,2,3,4,5]
# print(alist)
# alist[0] = 100
# print(alist)
# print(alist[1:3]) #切片取值
# alist[1:3] = [9,6,9,5,9,200]
# print(alist)
# # 列表方法
# #追加
# alist.append(1000)
# print(alist)
# alist.append((1,2)) #把元组追加到列表
# print(alist)
# alist.extend((1,2)) #将序列中的每一项作为列表项加入
# print(alist)
# alist.remove((1,2)) #将列表中的元组项删除
# print(alist)
# a =alist.index(1000) #取出1000项的下表
# print(a)
# alist.reverse() #反转列表
# print(alist)
# print(list(enumerate(alist))) #以key:value形式列出下标和对应项
# for x,y in list(enumerate(alist)):
#     print(x,y)
# alist.insert(2,9) #在下标为2的位置插入数据9
# alist.sort() #升序排列
# print(alist)
# alist.sort(reverse=True) #降序排列(利用了反转)
# print(alist)
# alist.count(9) #统计9出现的次数
# print(alist.count(9))
# alist.pop() #弹出数据(默认将最后一个数据弹出)
# print(alist)
# alist.pop(2) #弹出下标为2的数据项
# print(alist)
# blist = alist.copy() #讲alist值拷贝出来赋值给blist(指向不同空间)
# print(blist)
# blist.clear() #清空列表
# print(blist)
# atu = (10,20,30)
# atu.count(100)
# print(atu.count(100)) #统计有几个100
# atu.index(30)
# print(atu.index(30)) #看30的下标
# #单元素元组必须加逗号
# a = (10)
# print(type(a)) #是int型
# a = (10,) #是tuple元组
# print(type(a))
# print(len(a)) #这是一项
#案例1:用列表构建栈的结构
'''
(0)压栈
(1)出栈
(2)查询
(3)退出
请选择(0/1/2/3):
'''
# #2.分析程序功能,将功能编写成函数
# #3.编写主程序代码
#
# stack = []
#
# def push_it():
#     #读取用户输入,非空内容追加到列表,否则打印提示
#     data = input('数据: ').strip() #去除两边空白
#     if data: #如果data非空
#         stack.append(data)
#         print('写入栈中数据: %s' % stack)
#     else:
#         print('输入内容为空.')
#
# def pop_it():
#     if stack:   #列表非空为真执行
#         print('从栈中,弹出: %s' % stack.pop())
#     else:
#         print('空栈')
#
# def view_it():
#     print(stack)
#
# def show_menu():
#     prompt = """(0)压栈
# (1)出栈
# (2)查询
# (3)退出
# 请选择(0/1/2/3): """
#     while 1:
#         #将用户输入字符去除两端空白字符,赋值给choice
#         choice = input(prompt).strip()
#         if choice not in ['0','1','2','3']:
#             print('Please re-enter:input is not value!')
#             continue
#
#         if choice == '0':
#             push_it()
#         elif choice == '1':
#             pop_it()
#         elif choice == '2':
#             view_it()
#         else:
#             print('\nBye-bye')
#             break
#
# if __name__ == '__main__':
#     show_menu()
# #*************优化版本***************
# stack = []
#
# def push_it():
#     #读取用户输入,非空内容追加到列表,否则打印提示
#     data = input('数据: ').strip() #去除两边空白
#     if data: #如果data非空
#         stack.append(data)
#         print('写入栈中数据: %s' % stack)
#     else:
#         print('输入内容为空.')
#
# def pop_it():
#     if stack:   #列表非空为真执行
#         print('从栈中,弹出: %s' % stack.pop())
#     else:
#         print('空栈')
#
# def view_it():
#     print(stack)
#
# def show_menu(): #优化
#     cmds = {'0':push_it,'1':pop_it,'2':view_it}
#     prompt = """(0)压栈
# (1)出栈
# (2)查询
# (3)退出
# 请选择(0/1/2/3): """
#     while 1:
#         #将用户输入字符去除两端空白字符,赋值给choice
#         choice = input(prompt).strip()
#         if choice not in ['0','1','2','3']:
#             print('Please re-enter:input is not value!')
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
#=========午间练习===========
# #!/bin/env python3
# #-*- coding:utf8 -*-
# stack = []
#
# '功能模块区'
# def push_it():
#     data = input('数据: ').strip() #消除两边空白行
#     if data: #data非空执行
#         stack.append(data)
#     else:
#         print('输入内容为空.')
#
# def pop_it():
#     if stack:
#         print('从栈中,弹出: %'% stack.pop()) #在输出操作时候并执行弹出操作
#     else:
#         print('空栈')
#
# def view_it():
#     print(stack)
#
# def show_menu():
#     prompt = """(0)压栈
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
#         if choice == '0':
#             push_it()
#         elif choice == '1':
#             pop_it()
#         elif choice == '2':
#             view_it()
#         else:
#             print('\nBye-bye')
#             break
#
# if __name__ == '__main__':
#     show_menu()
#改良版本
#!/bin/env python3
#-*- coding:utf8 -*-
# stack = []
#
# def push_it():
#     data = input('数据: ').strip()
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
# def view_it():
#     print(stack)
#
# def show_menu():
#     cmds = {'0':push_it,'1': pop_it,'2': view_it}
#     prompt = """(0)压栈
# (1)出栈
# (2)查询
# (3)退出
# 请选择(0/1/2/3): """
#
#     while 1:
#         choice = input(prompt).strip()
#         if choice not in ['0','1','2','3']:
#             print('无效的输入,请重试.')
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
# #字典:容器 可变 映射
# #key 不能重复 不可变类型
# #dict 字符串 元组 列表都可以写入(必须只有两个元素
# adict = dict(['ad',('name','bob'),['age',20]]) #dict创建字典的函数
# print(adict)
# #创建具有相同值的字典
# bdict = {}.fromkeys(['bob','alice','tom'],7)
# print(bdict)
# #利用for循环找到key的值
# for key in adict:
#     print(key,adict[key])
# #也可以用%s替换做
# a = '%(name)s is %(age)d years old' % adict
# print(a)
#
# #赋值时,key在字典里就会更新 不在则会添加
# adict['age'] = 22
# print(adict)
# adict['email'] = 'tedu@.cn'
# print(adict)
# #成员关系判断
# print('bob' in adict)
# print('name' in adict)  #name是字典的key么?
# print(len(adict))
# #字典的方法
# #如果字典里存在 那么二者无区别
# a = adict.get('age')
# b = adict['age']
# print(a,b)
# #如果字典里不存在
# a = adict.get('bcz') #不会报错 返回None(用函数取值)
# b = adict['bcz'] #没有直接报错(直接取值)
# print(a,b)
# #keys获得所有key
# bdict = {}.fromkeys(['bob','alice','tom'],7)
# ak = bdict.keys()
# print(ak)
# #取出所有的value
# av = bdict.values()
# print(av)
# #取出key,value对
# keva = list(bdict.items())
# print(keva)
# '''keva排列'''
# print('key:','\t','value:')
# for i in keva:
#     for x in i:
#         print(x,'\t   ',end='')
#     print()
# #案例2:模拟用户登录信息系统
# #!/bin/env python3
# #-*- coding:utf8 -*-
# import getpass
#
# usrdb = {}
#
# def register(): #注册
#     username = input('\033[1;32m注册用户名:\033[0m ').strip()
#     if username and (username not in usrdb): #可以加上括号提高可读性
#         password = input('\033[1;32m请输入密码:\033[0m ').strip()
#         usrdb[username] = password
#         if username in usrdb:
#             print("\033[1;36m注册成功!\033[0m")
#         else:
#             print("\033[1;31注册失败!\033[0m")
#     else:
#         print('用户名为空或已存在!')
#
# def login(): #登录
#     username = input('\033[1;33m输入用户名:\033[0m ').strip()
#     password = getpass.getpass('\033[33;1m请输入密码:\033[0m ').strip()
#     #if (username in usrdb) and (usrdb[username] == password):
#     if usrdb.get(username) == password: #利用get取出密码(如果不存在不会报错回取出来None)
#         print('\033[1;36m欢迎 %s回来!\033[0m' % username)
#     else:
#         print('\033[1;31m用户名或密码错误!\033[0m')
#
# def show_menu():
#     cmds = {'0': register,'1': login}
#     prompt = """\033[1;35m(0)注册用户
# (1)登入系统
# (2)退出
# 请选择(0/1/2):\033[0m """
#     while 1:
#         choice = input(prompt).strip()
#         if choice not in ['0','1','2']:
#             print('\033[1;31m无效的输入,请重试!\033[0m')
#             continue
#
#         if choice == '2':
#             print('\n\033[1;36mBye-bye\033[0m')
#             break
#
#         cmds[choice]()
#
# if __name__ == '__main__':
#     show_menu()
# #集合:不可变 不可重复(如果有重复的就留一个) 无顺序
# #集合就像一个没有键值的键值对(和字典相比较)
# s1 = set('abc')
# s2 = set('bcd')
# s3 = set(['tom', 'jerry', 'bob', 'alice'])
# print(s1)
# print(s2)
# print(s3)
# print(set('hello'))
# #查看集合长度
# print(len(s3))
# #for循环打印集合内容
# for name in s3:
#     print(name)
# #集合可做成员关系判断
# print('tom' in s3)
# print('zhangsan' in s3)
# print('zhangsna' not in s3)
# #集合工具:交集 并集 差补(常用三种方式)
# #交集:共有的
# print(s1 & s2)
# #并集:合并
# print(s1 | s2) #集合不可重复(重复的视为多余去除了)
# #差补:其中一个有的
# print(s1 - s2)
# #集合添加成员
# s3 = set() #添加空集合
# s3.add(10) #向集合中加10数据
# print(s3)
# #print(s3.add([20,30])) #错误,因为列表是可变的
# s3.update([20,30]) #成功,因为字典可变
# print(s3)
# #删除元素
# s3.remove(30)
# print(s3)
# s4 = set((10 ,20 ,30,40))
# print(s4)
#
# #子集:被包含的集合
# s3.issubset(s4) #s3是s4的子集么?
# print(s3.issubset(s4))
# #超集:包含子集的集合
# s4.issuperset(s3) #s4是s3的超集么?
# print(s4.issuperset(s3))
# #集合的 交集 并集 差补函数
# print(s1.intersection(s2)) #s1 & s2
# print(s1.union(s2)) #s1 | s2
# print(s1.difference(s2)) #s1 -s2
# #集合的应用
# #去重复
# from random import randint
# nums = [randint(1,20) for i in range(20)]
# print(nums)
# print(set(nums))
# print(list(set(nums)))
#
# #日志去重url
# with open('/tmp/mima1') as f1:
#     s1 = set(f1)
# with open('/tmp/mima2') as f2:
#     s2 = set(f2)
# with open('/tmp/mima3','w') as f3:
#     f3.writelines(s2 - s1)
# alist = [10, 8 ,20 ,365 ,23, 4]
# print("%s is %s years old" % ('bob',23)) #常用
# print("%s is %d years old" % ('bob',23)) #常用
# print('%s is %d years old' % ('bob',23.5)) #%d是整数常用(打印不会显示小数)
# #?print('%s is %5.2f years old' % ('bob',23.5)) #%5.2f是宽度为5,2位小数(宽度写不写看起来没区别)
# print('97 is %c' % 97) #acci码中97为小写a编号
# print('11 is %#o' % 11) #表示有前缀的八进制
# print('11 is %#x' % 11)
# print('%10s%5s'% ('name','age')) #表示总宽度为10,右对齐,常用
# print('%10s%5s'% ('bob',25))
# print('%10s%5s'% ('alice',23))
# print('%-10s%-5s'% ('bob',25)) #表示左对齐,常用
# print('%10d'%123) #宽度为10默认空格补全
# print('%010d'% 123) #宽度为10 改用0补全
#
# print('{} is {} years old'.format('bob',25))
# print('{1} is {0} years old'.format(25,'bob'))
# print("{:<10}{:<8}".format('name','age'))
# import shutil
#
# with open('/etc/password','rb') as sfobj:
#     with open('/tmp/mima.txt','wb') as dfobj:
#         shutil.copyfileobj(sfobj,dfobj) #拷贝文件对象
#
# shutil.copyfile('/etc/password','/tmp/mima2.txt')
# shutil.copy('/etc/shadow','/tmp/') #cp /etc/shadow /tmp/
# shutil.copy2('/ect/shadow','/tmp/') #cp -p /etc/shadow /tmp/
# shutil.move('/tmp/mima.txt','/var/tmp/') #mv /tmp/mima.txt /var/tmp
# shutil.copytree('/etc/security','/tmp/anquan') #cp -r /etc/security /tmp/anquan
# shutil.rmtree('/tmp/anquan') #rm -rf /tmp/anquan
# #讲mima2.txt的权限设置成与/etc/shadow一样
# shutil.copymode('/etc/shadow','/tmp/mima2.txt')
# #将mima2.txt的元数据设置成与/etc/shadow一样
# #元数据使用stat /etc/shadow查看
# shutil.copystat('/etc/shadow','/tmp/mima2.txt')
# shutil.chown('/tmp/mima2.txt',user='zhangsan',group='zhangsan')
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
# alist = [1,2,3,'bob','alice']
# alist[0] = 10
# alist[1:3] = [20,30]
# alist[2:2]= [22 ,24 ,26 ,28]
# print(alist)
# alist.append(100)
# alist.remove(24) #删除的一个24
# alist.index('bob') #返回下标
# blist = alist.copy() #相当于blist = alist[:]
# alist.insert(1,15) #向下标为1的位置插入数字15
# alist.pop() #默认弹出最后一项
# alist.pop(2) #弹出下标为2的项目
# alist.pop(alist.index('bob'))
# alist = [1,2,3,0,-1]
# print(alist.sort()) #升序排列
# alist.reverse() #反转
# alist.sort(reverse=True) #倒叙排列
# alist.count(20) #统计20在列表中出现的次数
# alist.clear() #清空
# alist.append('new')
# alist.extend('new')
# print(alist)
# alist.extend(['hello','world','hehe']) #会把每一项加进列表
# print(alist)
# import sys
# import keyword #检查合法字符模块
# import string
#
# first_chs = string.ascii_letters + '_'
# all_chs = first_chs + string.digits
#
# def check_id(idt): #由sys.arvg交互而得到变量赋值给idt(智能交互终端)
#     if keyword.iskeyword(idt):
#         return "%s is keyword" % idt
#
#     if idt[0] not in first_chs:
#         return '1st invalid'
#
#     for ind,ch in enumerate(idt[1:]):
#         if ch not in all_chs:
#             return 'char in postion #%s invalid' %  (ind + 2)
#
#     return '%s is valid' % idt
#
# if __name__ == '__main__':
#     print(check_id(sys.argv[1])) #python3 chekcid py abc@123
#**************************************************************
# import  subprocess
# import sys
# from randpass2 import randpass
#
# def adduser(username,password,fname):
#     data="""user information:
# %s:%s
# """
#     subprocess.call('useradd %s' % username,shell=True)
#     subprocess.call(
#         'echo %s | password --stdin %s'% (password,username),
#         shell=True
#     )
#     with open(fname,'a')as fobj:
#         fobj.write(data % (username,password))
#
# if __name__ == '__main__':
#     username = sys.argv[1]
#     password = randpass()
#     adduser(username,password,'/tmp/user.txt')
#     #python3 adduser.py jhon
#*********************************************************
# stack = []
#
# def push_it():
#     item = input('item to push: ')
#     stack.append(item)
#
# def pop_it():
#     if stack:
#         print('from stack poped %s' % stack.pop())
#
# def view_it():
#     print(stack)
#
# def show_menu():
#     cmds = {'0': push_it,'1': pop_it,'2': view_it}
#     prompt = """(0)push it
# (1)pop it
# (2)view it
# (3)exit
# Please input your choice(0/1/2/3): """
#
#     while True:
#         choice = input(prompt).strip()[0]
#         if choice not in '0123':
#             print('Invalid input,Try again.')
#             continue
#
#         if choice == '3':
#             break
#
#
#         cmds[choice]()
#
# if __name__ == '__main__':
#     show_menu()
#**************************************************
# import sys
#
# def unix2doc(fname):
#     dst_fname = fname + '.txt'
#
#     with open(fname)as src_fobj:
#         with open(dst_fname,'w')as dst_fobj:
#             for line in src_fobj:
#                 line = line.rstrip()+ '\r\n'
#                 dst_fobj.write(line)
#
#
# if __name__ == '__main__':
#     unix2doc(sys.argv[1])
#***************************************************
# import time
#
# length = 19
# count = 0
#
# while True:
#     print('\r%s@%s'% ('#' * count,'#' * (length-count)),end='')
#     try:
#         time.sleep(0.3)
#     except KeyboardInterrupt:
#         print('\nBye-bye')
#         break
#     if count == length:
#         count = 0
#     count += 1
#*************************
# adict = dict() #{}
# dict(['ab','cd'])
# bdict = dict([('name','bob'),('age',25)])
# print({}.fromkeys(['zhangsan','list','wangwu'],11))
#
# for key in bdict:
#     print('%s:%s'% (key,bdict[key]))
#
# print('%(name)s:%(age)s' % bdict)
#
# bdict['name'] ='tom'
# bdict['email'] = 'tom@tedu.cn'
#
# del bdict['email']
# bdict.pop('age')
# bdict.clear()


