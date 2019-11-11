#!/bin/env python3
#-*- coding:utf8 -*-
#周末python练习01
"""
1. 需要支持完全和增量备份
2. 周一执行完全备份
3. 其他时间执行增量备份
4. 备份文件需要打包为tar文件并使用gzip格式压缩
"""
# import time
#
# t = time.localtime()  # 返回当前时间的九元组
# time.gmtime()  # 返回格林威治0时区当前时间的九元组
# time.time()  # 常用，与1970-1-1 8:00之间的秒数，时间戳
# time.mktime(t)  # 把九元组时间转成时间戳
# time.sleep(1)
# time.asctime()  # 如果有参数，是九元组形式
# time.ctime()  # 返回当前时间，参数是时间戳，常用
# time.strftime("%Y-%m-%d") # 常用
# time.strptime('2018-07-20', "%Y-%m-%d")  # 返回九元组时间格式
# time.strftime('%H:%M:%S')
#
# ###########################################
# from datetime import datetime
# from datetime import timedelta
# datetime.today()  # 返回当前时间的datetime对象
# datetime.now()  # 同上，可以用时区作参数
# datetime.strptime('2018/06/30', '%Y/%m/%d')  # 返回datetime对象
# dt = datetime.today()
# datetime.ctime(dt)
# datetime.strftime(dt, "%Y%m%d")
#
# days = timedelta(days=90, hours=3)  # 常用
# dt2 = dt + days
# dt2.year
# dt2.month
# dt2.day
# dt2.hour

# import os
#
# os.getcwd()  # 显示当前路径
# os.listdir()  # ls -a
# os.listdir('/tmp')  # ls -a /tmp
# os.mkdir('/tmp/mydemo')  # mkdir /tmp/mydemo
# os.chdir('/tmp/mydemo')  # cd /tmp/mydemo
# os.listdir()
# os.mknod('test.txt')  # touch test.txt
# os.symlink('/etc/hosts', 'zhuji')  # ln -s /etc/hosts zhuji
# os.path.isfile('test.txt')  # 判断test.txt是不是文件
# os.path.islink('zhuji')  # 判断zhuji是不是软链接
# os.path.isdir('/etc')
# os.path.exists('/tmp')  # 判断是否存在
# os.path.basename('/tmp/abc/aaa.txt')
# os.path.dirname('/tmp/abc/aaa.txt')
# os.path.split('/tmp/abc/aaa.txt')
# os.path.join('/home/tom', 'xyz.txt')
# os.path.abspath('test.txt')  # 返回当前目录test.txt的绝对路径

# import pickle
# """以前的文件写入 只能写入字符串如果希望把任意数据对象(数字 列表等)写入文件,
# 取出来的数据类型不变就用到pickle了
# """
# #shop_list = ['eggs'.'apple','peach']
# #with open('/tmp/shop.data','wb') as fobj
# #  pickle.dump(shop_list,fobj)
#
# with open('/tmp/shop.data','rb')as fobj:
#     mylist = pickle.load(fobj)
#
# print(mylist[0],mylist[1],mylist[2])
#
# #异常处理模块
# try: #吧友嗯呢该发生的异常的语句放到try里执行
#     n = int(input('number: '))
#     result = 100 / n
#     print(result)
# except ValueError:
#     print('invalid number')
# except ZeroDivisionError:
#     print('0 not allowed')
# except KeyboardInterrupt:
#     print('\nBye-bye')
# except EOFError:
#     print('\nBye-bye')
#
# print('Done')
#
# #异常处理完正语法
# try:
#     n = int(input('number: '))
#     result = 100 / n
# except (ValueError,ZeroDivisionError):
#     print('invalid number')
# except (KeyboardInterrupt,EOFError):
#     print('\nBye-bye')
# else:
#     print(result) #异常不发生时才执行else句子
# finally:
#     print('Dnoe') #不管异常是否发生都必须执行的语句
#
# #常用形式有try-except和try-finally
#
# #自定义异常
# def set_age(name, age):
#     if not 0 < age < 120:
#         raise ValueError('年龄超过范围')  # 自主决定触发什么样的异常
#     print("%s is %d years old" % (name, age))
#
# def set_age2(name, age):
#     assert 0 < age < 120, '年龄超过范围'   # 断言异常
#     print("%s is %d years old" % (name, age))
#
# if __name__ == '__main__':
#     set_age('zhangsan', 20)
#     set_age2('lisi', 200)
#
# x = 10 #全局变量从订一开始道程序结束,一直可见可用
#
# def foo():
#     print(x)
#
# foo()
#
# def bar():
#     x = 20 #此处的x是局部变量,将全局变量遮盖住 不会影响全局变量的值
#     print(x)
#
# bar() # x -> 20
# print(x) # x -> 10
#
# def aaa():
#     global  x #在局部引用全局变量
#     x = 100 #将全局变量x重新赋值100
#     print(x) #x -> 100
#
# aaa()
#
# print(x) #x -> 100
#
# #函数调用:参数使用注意事项
#
# def get_age(name,age):
#     print('%s is %s years old'% (name,age))
#
# get_age('bob',22) #参数按顺序传递
# get_age(25,'bob') #没有语法错误,但是语义不对
# get_age(age=25,name='bob')
# #get_age() #Error,少参数
# #get_age('bob',25,100) #Error 多参数
# #get_age(age=25,'bob') #语法错误
# #get_age(25,name='bob') #错误 参数按顺序传递,name得道多个值
# get_age('bob',age=26)
#
# def funcation1(*args): #*表示args是个元组
#     print(args)
#
# def funcation2(**kwargs): #**表示kwargs是个字典
#     print(kwargs)
#
# def funcation3(x,y):
#     print(x * y)
#
# def funcation4(name,age):
#     print('%s is %s years old'% (name,age))
#
# if __name__ == '__main__':
#     funcation1()
#     funcation1(10)
#     funcation1(10,'bob')
#     funcation2()
#     funcation2(name='bob',age=25)
#     funcation3(*[10,5]) #调用的时候,*表示拆开后面的数据类型
#     funcation4(**{'name':'bob','age': 25}) #name = 'bob',age = 25

# #偏函数基础应用
# from functools import  partial
#
# def foo(a,b,c,d,f):
#     return a + b + c +d + f
#
# if __name__ == '__main__':
#     print(foo(10,20,30,40,5))
#     print(foo(10,20,30,40,25))
#     print(foo(10,20,30,40,69))
#     add = partial(foo,a=10,b=20,c=30,d=40)
#     print(add(f=5)) #foo(10,20,30,40,5)
#     print(add(f=8)) #foo(10,20,30,40,8)

#偏凉函数应用：简单的图形窗口
# import tkinter
# from functools import partial
#
# root = tkinter.Tk()
# lb = tkinter.Label(text="Hello world!")
# b1 = tkinter.Button(root, fg='white', bg='blue', text='Button 1')  # 不使用偏函数生成按钮
# MyBtn = partial(tkinter.Button, root, fg='white', bg='blue')  # 使用偏函数定义MyBtn
# b2 = MyBtn(text='Button 2')
# b3 = MyBtn(text='quit', command=root.quit)
# lb.pack()
# b1.pack()
# b2.pack()
# b3.pack()
# root.mainloop()

# def mygen():
#     yield 'hello'
#     a = 10 +20
#     yield  a
#     yield [1,2,3]
#
# if __name__ == '__main__':
#     m = mygen()
#     for i in m:
#         print(i)
#
#     for i  in m:
#         print(i) #无值 因为生成器对象只能用一次
#
# #生成器实例:每次取出文件的10行内容
# def block(fobj):
#     block=[]
#     counter = 0
#     for line in fobj:
#         block.append(line)
#         counter += 1
#         if counter == 10:
#             yield block #反回中间结果 下次取值 从这里继续向下执行
#             block = []
#             counter  = 0
#         if block: #文件最后不够10行的部分
#             yield block
#
# if __name__ == '__main__':
#     fobj = open('/tmp/passwd') #cp /etc/passwd /tmp
#     for lines in blocks(fobj):
#         print(lines)
#         print()
#     fobj.close()
#
# from random import randint
#
# def funcation(x):
#     return  x % 2
#
# if __name__ == '__main__':
#     alist = [randint(1,100)for i in range(10)]
#     print(alist)
#     #filter要求第一个参数势函数,该函数必须反悔True或False
#     #执行时吧alist的每一项作为 funcation的参数 反悔真留下,否则过滤掉
#     #filter函数的参数又是函数 乘坐高阶函数
#     result = filter(funcation,alist) #不适用匿名函数
#     print(list(result))
#     result2 = filter(lambda x: x % 2,alist) #匿名函数,不适用常规函数
#     print(list(result2))
#
# from random import randint
#
# def funcation(x):
#     return x * 2+1
#
# if __name__ == '__main__':
#     alist = [randint(1,100)for i in range(10)]
#     print(alist)
#     #map将第二个参数中的每一项都交给funcation函数进行加工 保留加工后的记过
#     result = map(funcation,alist) #使用常规函数作为参数
#     result2 = map(lambda x: x*2+1,alist)# 使用匿名函数作为参数
#     print(list(result))
#     print(list(result2))

# #函数练习 数字游戏
# from random import  randint,choice
#
# def add(x,y):
#     return x + y
#
# def sub(x,y):
#     return x - y
#
# def exam():
#     cmds = {'+':add,'-':sub}
#     nums = [randint(1,100)for i in range()2]
#     nums.sort(reverse=True) #列表降序排列
#     op = choice('+-')
#     result = cmds[op](*nums)
#     prompt = '%s %s %s = ' % (nums[0],op,nums[1])
#     tries = 0
#
#     while tries < 3:
#         try:
#             answer = int(input(prompt))
#         except: #简单粗暴底捕获所有异常
#             continue
#
#         if answer == result:
#             print('Very good !')
#             break
#         else:
#             print('Wrong answer.')
#             tries +=1
#     else: #此得是while的else,全算错才给答案 算对了就不用给出答案了
#         print('%s %s'% (prompt,result))
#
# if __name__ == '__main__':
#     while True:
#         exam()
#         try:
#             yn = input('Continue(y/n)?').strip()[0]
#         except IndexError:
#             continue
#         except(KeyboardInterrupt,EOFError):
#             print()
#             yn = 'n'
#
#         if yn in 'nN'
#             break

#改良版猜数游戏
# from random import randint,choice
#
# def exam():
#     cmds = {'+':lambda x,y:x + y,'_':lambda x,y:x - y}
#     nums = [randint(1,100)for i in range(2)]
#     nums,sorted(reverse=True)
#     op = choice('+-')
#     result = cmds[op](*nums)
#     prompt = '%s %s %s=' %(nums[0],op,nums[1])
#     tries = 0
#
#     while tries <3:
#         try:
#             answer = int(input(prompt))
#         except
#             continue
#
#         if answer == result:
#             print('Very good!')
#             break
#         else:
#             print('Wrong answer.')
#             tries += 1
#
#     else:
#         print('%s %s'% (prompt,result))
#
# if __name__ == '__main__':
#     while True:
#         exam()
#         try:
#             yn = input('Continue(y/n)?').strip()[0]
#         except IndexError:
#             continue
#         except (KeyboardInterrupt,EOFError):
#             print()
#             yn = 'n'
#
#         if yn in 'Nn':
#             break
#
# #递归函数计算阶乘
# def funcation(n): #5
#     if n == 1:
#         return n
#     return n * funcation(n - 1)
#         #5 * funcation(4)
#         #5 * 4 * funcation(3)
#         #5 * 4 * 3 *funcation(2)
#         #5 * 4 * 3 * 2 * funcation(1)
#         #5 * 4 * 3 * 2 * 1
#
# if __name__ == '__main__':
#     print(funcation(5))
#     print(funcation(6))

# #listdir.py递归函数练习:主机列出目录内容
# import os
# import sys
#
# def list_file(path):
#     if os.path.isdir(path):
#         print(path + ":")
#         content = os.listdir(path)
#         print(content)
#         for fname in content:
#             fname = os.path.join(path,fname)
#             list_files(fname)
#
# if __name__ == '__main__':
#     list_file(sys.argv[1]) #python3 listdir.py /etc

# #快速排序
# from random import randint
#
# def quick_sort(num_list):
#     if len(num_list):
#         return  num_list
#
#     middle = num_list[0]
#     smaller = []
#     larger = []
#     for i in num_list[1:]:
#         if i < middle:
#             smaller.append(i)
#         else:
#             larger.append(i)
#
#     return quick_sort(smaller) + [middle] + quick_sort(larger)
#
# if __name__ == '__main__':
#     alist = [randint(1,100)for i in range(10)]
#     print(alist)
#     print(quick_sort(alist))

# #记账小程序复习
# import pickle
# import os
# import time
#
# def cost(wallet,record): #记录花钱的函数
#     amount = int(input('amount: '))
#     comment = input('comment: ')
#     date = time.strftime('%Y-%m-%d')
#     with open(wallet,'rb') as fobj:
#         balance = pickle.load(fobj) - amount
#     with open(wallet,'wb') as fobj:
#         pickle.dump(balance,fobj)
#     with open(record,'a') as fobj:
#         fobj.writable(
#             '%-12s%-8s%-8s%-10s%-20s\n' % (date,amount,'',balance,comment)
#         )
#
# def save(wallet,record): #记录存钱的函数
#     amount = int(input('amount: '))
#     comment = input('comment: ')
#     date = time.strftime('%Y-%m-%d')
#     with open(wallet,'rb') as fobj:
#         balance =pickle.load(fobj) + amount
#     with open(wallet,'wb') as fobj:
#         pickle.dump(balance,fobj)
#     with open(record,'a' as fobj):
#         fobj.write(
#             '%-12s%-8s%-8s%-10s%-20s\n' % (date,'',amount,balance,comment)
#         )
#
# def query(wallet,record): #查询收支明细的函数
#     print('%-12s%-8s%-8s%-10s%-20s' % ('date','cost','save','balace','comment'))
#     with open(record) as fobj:
#         for line in fobj:
#             print(line,end='')
#     with open(wallet,'rb') as fobj:
#         balance = pickle.load(fobj)
#     print('Latest Balance: %d' %balance)
#
# def show_menu():
#     cmds = {'0': cost,'1': save,'2': query}
#     prompt = """(0)cost
# (1)save
# (2)query
# (3)exit
# Please input your choice(0/1/2/3): """
#     wallet = 'wallet.data'
#     record = 'record.txt'
#     if not os.path.exists(wallet):
#         with open(wallet,'wb')as fobj:
#             pickle.dump(10000,fobj)
#
#     while True:
#         try:
#             choice = input(prompt).strip()[0]
#         except IndexError:
#             continue
#         except (KeyboardInterrupt,EOFError):
#             prompt
#             choice = '3'
#
#         if choice not in '0123':
#             print('Invalid input. Try again.')
#             continue
#
#         if choice == '3';
#             break
#         cmds[choice](wallet,record)
#
# if __name__ == '__main__':
#     show_menu()

#os.walk的使用
list(os.walk('/etc/security'))
result = list(os.walk('/etc/security'))
len(result)
print(
    result[0]
)
#os.walk实例
import sys
import os

def lsdir(directory):
    for path,folder,files in os.walk(firectory):
        print('%s:'% path)
        for d in folder:
            print('\033[34;1m%s\t\033[0m'% d ,end='')
        for file in files:
            print('%s\t'% file,end="")
        print('\n')

if __name__ == '__main__':
    lsdir(sys.argv[1])


#增量备份预习
import time
import os
import tarfile
import hashlib
import pickle

def check_md5(fname):
    m = hashlib.md5()
    with open(fname,'rb')as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

def full_backup(src_dir,dst_dir,md5file):
    fname = os.path.basename(src_dir.rstrip('/'))
    fname = '%s_full_%s.tar.gz' % (fname,time.strftime('%Y-%m-%d'))
    fname = os.path.join(dst_dir,fname)
    md5dict = {}

    tar = tarfile.open(fname,'w:gz')
    tar.add(src_dir)
    tar.close()

    for path,folders,files in os.walk(src_dir):
        for each_file in filesL
            key = os.path.join(path,each_file)
            md5dict[key] = check_md5(key)

    with open(md5file,'wb')as fobj:
        pickle.dump(md5dict,fobj)

def incr_backup(src_dir,dst_dir,md5file):
    fname = os.path.basename(src_dir.rstrip('/'))
    fname = '%s_incr_%s.tar,gz'% (fnaem,time.strftime('%Y%m%d'))
    fname = os.path.join(dst_dir,fname)
    md5dict = {}

    with open(md5file,'rb') as fobj:
        oldmd5 = pickle.load(fobj)

    for path,folders,files in os.walk(src_dir):
        for each_file in files:
            key = os.path.join(path,each_file)
            md5dict[key] = check_md5(key)

    with open(md5file,'wb') as fobj:
        pickle.dump(md5dict,fobj)

    tar = tarfile.open(fname,'w:gz')
    for key in md5dict:
        if oldmd5.get(key) != md5dict[key]:
            tar.add(key)
    tar.close()

if __name__ == '__main__':
    #mkdir /tmp/demo; cp -r /ect/security /tmp/demo
    src_dir = '/tmp/demo/security'
    dst_dir = '/var/tmp/backup' #mkdir /var/tmp/backup
    md5file = '/var/tmp/backup/md5.data'
    if time.strftime('%a') == 'Mon':
        full_backup(src_dir,dst_dir,md5file)
    else:
        incr_backup(src_dir,dst_dir,md5file)
#type weekend01.py | find /v /c ""