#!/bin/env python3
# -*- coding:utf8 -*-
# #学python3的第八天
# #time时间模块
# #表示方式:
# # 时间戳(1970-1-1 0:0:0到某一时间点之间的秒数)
# # UTC时间(世界协调时,以英国格林威治所在的纵切面作为标准时区 每隔15°是一个时区　共24个时区)
# # 9元组:(年月日时分秒,一周中的第几天,一年中的第几天,是否为夏时制)
# #当前时间的时间戳
# import  time
# a = time.time()
# print(
#     a
# )
#
# #计算1+到10000001用多长时间
# import time
#
# result = 0
#
# start = time.time()
# for i in range(
#         1,10000001
# ):
#     result += i
# end = time.time()
#
# print(
#     result
# )
# print(
#     end - start
# )
#
# #字符串表示的ＵＴＣ时间
# t = time.ctime()
# print(
#     t
# )
# t = time.ctime(0) #0是时间戳
# print(
#     t
# )
# #时间格式化
# t = time.strftime(
#     '%Y-%m-%d %H:%M:%S'
# )
# print(
#     t
# )
# print(
#     time.strftime(
#         '%Y-%m-%d %a %H:%M:%S'
#     )
# )
# #9元组时间
# t =  time.localtime()
# print(
#     t
# )
# print(
#     t.tm_year
# ) #从九元组里截取年份
# tt = time.strptime(
#     '2019-11-11 00:00:00','%Y-%m-%d %H:%M:%S'
# )
# print(
#     tt
# )
#
# 截取时间段
# import time
#
# fname = '/home/student/PycharmProjects/untitled/my.log'
# t9 = time.strptime(
#     '2019-5-15 09:00:00', '%Y-%m-%d %H:%M:%S'
# )
# t12 =time.strptime(
#     '2019-05-15 12:00:00','%Y-%m-%d %H:%M:%S'
# )
#
# with open(
#         fname
# ) as fobj:
#     for line  in fobj:
#         t =time.strptime(
#             line[:19],'%Y-%m-%d %H:%M:%S'
#         )
#         if t9 <= t <= t12:
#             print(
#                 line,
#                 end=''
#             )
# 优化
# import time
#
# fname = '/home/student/PycharmProjects/untitled/my.log'
# t9 =time.strptime(
#     '2019-05-15 09:00:00','%Y-%m-%d %H:%M:%S'
# )
# t12 =time.strptime(
#     '2019-05-15 12:00:00','%Y-%m-%d %H:%M:%S'
# )
#
# with open(
#         fname
# )as fobj:
#     for line  in fobj:
#         t =time.strptime(
#             line[:19],'%Y-%m-%d %H:%M:%S'
#         )
#         if t > t12:
#             break
#         if t >= t9:
#             print(
#                 line,
#                 end=''
#             )
# #time.sleep#实现睡眠
# import time
#
# start = time.time(
#
# )
# time.sleep(3)
# end = time.time(
#
# )
#
# print(
#     start - end
# )
# #datetime模块
# #取出当前时间　分别为年月日时分秒毫秒
# from datetime import datetime
# t1 = datetime.now(
#
# )
# print(
#     t1
# )
# print(
#     t1.year,t1.month,t1.day,
#     sep='-'
# )
# print(
#     t1.hour,t1.minute,t1.second,t1.microsecond
# )
# #创建指定时间，没有指定的，默认为0
# t2 = datetime(
#     2019,11,11
# )
# print(
#     t2
# )
# #返回指定格式字符串
# print(
#     t1.strftime(
#         '%Y-%m-%d' '%H:%M:%S'
#     )
# )
# #将指定字符串转为datetime对象
# t3 = datetime.strptime('2019-11-11 08:00:00', '%Y-%m-%d %H:%M:%S')
# print(
#     t3
# )
# 计算时间差
# from datetime import  datetime,timedelta
#
# t1 = datetime.now(
#
# )
# print(
#     t1
# )
#
# days = timedelta(
#     days=50,hours=1
# )
#
# h = t1 - days #50天1小时之前
# print(
#     h
# )
#
# h = t1 + days #50天1小时之后
# print(
#     h
# )
# #datetime改版
# from datetime import  datetime,timedelta
#
# fname = '/home/student/PycharmProjects/untitled/my.log'
#
# t9 =datetime.strptime(
#     '2019-05-15 09:00:00','%Y-%m-%d %H:%M:%S'
# )
# t12 =datetime.strptime(
#     '2019-05-15 12:00:00','%Y-%m-%d %H:%M:%S'
# )
#
# with open(
#         fname
# )as fobj:
#     for line  in fobj:
#         t =datetime.strptime(
#             line[:19],'%Y-%m-%d %H:%M:%S'
#         )
#         if t > t12:
#             break
#         if t >= t9:
#             print(
#                 line,
#                 end=''
#             )
# #异常处理:避免遇到错误程序崩溃导致终止 使得程序继续运行
#
# """常见的报错:
# NameError     //
# SyntaxError   //
# ...
# """
#
#
# # #***try处理
# # try:
# #     有可能发生异常的语句
# # except (异常1,异常2):
# #     发生异常时执行的代码
# # except (异常4,异常3):
# #     发生异常时执行的代码
# # else:
# #     不发生异常才执行的代码
# #例子
#
# try:
#     n = int(
#         input(
#             'number: '
#         )
#     )
#     result = 100/n
#
# except (
#         ValueError,
#         FileExistsError
# ):  #错误输出(多个可以加括号)
#     print(
#         'Invalid input.Try again.'
#     )
# except \
#         ZeroDivisionError:
#     print(
#         'Invalid input.Try again.'
#     )
# except \
#         KeyboardInterrupt:
#     print(
#         '\nBye-bye'
#     )
# except EOFError as echo: #将异常保存到变量echo中
#     print(
#         '\nBye-bye: ',
#         echo
#     )
# else:                     #正确才会输出
#     print(
#         result
#     )
# finally:                  #不管错不错都会输出
#     print(
#         '***oooxxx***'
#     )
# print(
#     'Done'  #不管怎么样都会执行的Done
# )
# #*******************show time*******************
# import time
#
# t9 = time.strptime(
#     '2019-5-15 09:00:00','%Y:%m:%d %H:%M:%S'
# )
# t12 = time.strptime(
#     '2019-5-15 12:00:00','%Y:%m:%d %H:%M:%S'
# )
#
# with open(
#         'my.log'
# ) as fobj:
#     for line in fobj:
#         t = time.strptime(
#             line[:19],'%Y-%m-%d %H:%M:%S'
#         )
#         if t > t12:  #避免不必要的循环重复
#             break
#         if t >= t9:
#             print(
#                 line,end=''
#             )
#
# with open(
#         'my.log'
# ) as fobj:
#     for line in fobj:
#         t = time.strptime(
#             line[:19],'%Y-%m-%d %H:%M:%S'
#         )
#         if t9 <= t <= t12:
#             print(
#                 line,end=''
#             )
#
# from datetime import  datetime
#
# t9 = datetime.strptime(
#     '2019-5-15 09:00:00','%Y-%m-%d %H:%M:%S'
# )
# t12 = datetime.strptime(
#     '2019-5-15 12:00:00','%Y-%m-%d %H:%M:%S'
# )
#
# with open(
#         'my.log'
# ) as fobj:
#     for line in fobj:
#         t = datetime.strptime(
#             line[:19],'%Y-%m-%d %H:%M:%S'
#         )
#         if t > t12:
#             break
#         if t >= t9:
#             print(
#                 line,end=''
#             )
#
# import time
#
# result = 0
#
# start = time.time(
#
# )
# for i in range(
#         1,10000001
# ):
#     result += i
# end = time.time(
#
# )
#
# print(
#     result
# )
# print(
#     end - start
# )
#
# try:
#     n = int(
#         input(
#         'number: '
#     )
#     )
#     result = 100/n
#     print(
#         result
#     )
#     print(
#         'Done'
#     )
# except (
#         ValueError #值错
# ):
#     print(
#         'Invalid input.Try again.'
#     )
# except (
#         ZeroDivisionError #100/0
# ):
#     print(
#         'Invalid input.Try again.'
#     )
# except (
#         KeyboardInterrupt #ctrl + c
# ):
#     print(
#         '\nBye-bye'
#     )
# except(
#     EOFError
# ):
#     print(
#         '\nBye-bye'
#     )
#
# try:
#     n = int(
#         input(
#             'number: '
#         )
#     )
#     result = 100 / n
#     print(
#         result
#     )
#     print(
#         'Done'
#     )
# #将常量保存到变量echo中
# except (
#     ValueError,
#     ZeroDivisionError #ctrl + d
# ) as echo:
#     print(
#         'Invalid input,Try again.',
#         echo
#     )
# except (
#     KeyboardInterrupt,
#     EOFError
# ):
#     print(
#         '\nBye-bye'
#     )
# #完整步骤
# try:
#     n = (
#         int(
#             input(
#                 'number: '
#             )
#         )
#     )
#     result = 100 / n
# except (
#     ValueError,
#     ZeroDivisionError
# ) as echo:
#     print(
#         'Invalid input.Try again.'
#     )
# except (
#     KeyboardInterrupt,
#     EOFError
# ):
#     print(
#         '\nBye-bye'
#     )
#     exit()
# else:
#     print(
#         result
#     )
# finally:
#     print(
#         'End'
#     )
#
# print(
#     'Done'
# )
# ***********************************************************
# #主动出发异常
# #使用raise制定触发
#
# def set_age(name,age):
#     if not 0 < age < 120:
#         raise ValueError('Age out of range!') #指定异常
#     print('%s is %d years old'% (name,age))
#
# def set_age2(name,age):
#     assert 0 < age < 120, 'Age out of range!'
#     print('%s is %d years old'% (name,age))
#
# if __name__ == '__main__':
#     set_age('NB',20)
#     set_age2('NB',20)
# os模块(系统命令)
import os
# print(
#     os.getcwd(
#
#     ) #pwd
# )
# print(
#     os.mkdir(
#         '/tmp/wxk'
#     ) #mkdir /wxk
# )
# print(
#     os.makedirs(
#         '/ak/wxk'
#     ) #mkdir -p /ak/wxk
# )
# print(
#     os.listdir(
#
#     ) #ls
# )
# print(
#     os.chdir(
#         '/tmp/nsd1906/demo' #cd /tmp/nsd1906/demo
#     )
# )
# print(
#     os.mknod(
#         'myfile.txt' #touch myfile.txt
#     )
# )
# print(
#     os.symlink(
#         '/etc/hosts',
#         'zhuji' #ln -s /etc/hosts zhuji
#     )
# )
# print(
#     os.stat(
#         '/etc/hosts'
#     )
# )
# hosts = os.stat(
#     '/etc/hosts' #fileinfo
# )
# print(
#     hosts.st_size
# ) #size
# print(
#     os.chmod(
#         'myfile.txt',
#         0o644 #linux权限是八进制数 chmod 644 myfile.txt(python中默认是十进制数)
#     )
# )
# print(
#     os.remove(
#         'zhuji' #rm zhuji
#     )
# )
# print(
#     os.path.abspath('python3') #取出绝对路径
# )
# print(
#     os.path.dirname(
#         '/tmp/nsd1906/deno/myfile.txt' #名字
#     )
# )
# print(
#     os.path.split(
#         '/tmp/nsd196/demo/myfile.txt' #分离
#     )
# )
# print(
#     os.path.join(
#         '/tmp/nsd1906/demo','myfile.txt' #拼接
#     )
# )
# print(
#     os.path.isfile(
#         '/etc/hosts' #存在并且是文件么
#     )
# )
# print(
#     os.path.ismount(
#         '/etc' #/etc是挂载点么??
#     )
# )
# print(
#     os.path.isdir(
#         '/' #存在并且是目录么?
#     )
# )
# print(
#     os.path.islink(
#         '/etc/grub2.cfg' #存在并且是软连接么?
#     )
# )
# print(
#     os.path.exists(
#         '/etc' #存在么?
#     )
# )
# os.walk使用
# 分析．result列表共有五项，每一项内容其结构完全一样
# 字符串:路径
# 如result[0](字符　列表　列表)
# 第一个列表:路径下的目录
# 第二个列表:路径下的文件
# result = list(
#     os.walk(
#         '/etc/security'
#     )
# )
# print(
#     len(
#         result
#     )
# )
# 实现ls -R /etc/security功能
# import sys
# import os
#
#
# def lsdir_R(
#         directory
# ):
#     for (
#             path, folder, files
#     ) in os.walk(
#         directory
#     ):
#         print(
#             '%s:'
#             %
#             path
#         )
#         for d in folder:
#             print(
#                 '\033[34;1m%s\t\t\033[0m'
#                 %
#                 d,
#                 end=''
#             )
#         print(
#
#         )
#         for file in files:
#             print(
#                 '%s\t\t' % file,
#                 end=''
#             )
#         # print('\n')
#         print(
#
#         )
#         print(
#
#         )
#
#
# if __name__ == '__main__':
#     lsdir_R(
#         sys.argv[
#             1
#         ]
#     )

# #进度条(给程序加进度条)****process_bar
# from tqdm import tqdm
# import  time
#
# for i in tqdm(
#         range(
#             10
#         )
# ):
#     time.sleep(
#         0.2
#     )
#
# print(
#
# )
# #copy文件带进度条
# import \
#     os
# import \
#     sys
# from \
#     tqdm\
#     import\
#     tqdm
#
# def \
#         copy\
#                 (
#                 src_fname,dst_fname,length=4096
#         ):
#     size = os.stat(
#         src_fname
#     ).st_size
#     times,extra = divmod(
#         size,
#         length
#     )
#     if extra:
#         times += 1
#
#     with open(
#             src_fname,
#             'rb'
#     )as src_fobj:
#         with open(
#                 dst_fname,'wb'
#         )as dst_fobj:
#             for\
#                     i\
#                     in\
#                     tqdm(
#                     range(
#                         times
#                     )
#             ):
#                 data = src_fobj.read(
#                     length
#                 )
#                 dst_fobj.write(
#                     data
#                 )
#
# if __name__ == '__main__':
#     copy(
#         sys.argv[
#             1
#         ],
#         sys.argv[
#             2
#         ]
#     )
#pickle模块:能够无损的取出
#存入的字典取出还是字典
# import pickle
#
# adict = {
#     'name':'bob',
#     'age':20
# }
# f =\
#     open(
#     '/tmp/a.data','wb'
#     )
# pickle.dump(
#     adict,f
# ) #将字典写入文件,如果用wirte只能写str类型
# f.close(
#
# )
# quit(
#
# )
#
# import picke
# f = open(
#     '/tmp/a.data','rb'
# )
# bdict = pickle.load(
#     f
# )
# f.close(
#
# )
# print(
#     bdict
# )
#记账程序
import time
import pickle

adict = {} #小字典
records = []  #总表
int_data = time.strftime('%Y-%m-%d') #date

def save_it(save=0): #存入余额
    try:
        if save != 0:
            save = input('\033[33;1msave: \033[0m').strip()[0]
    except ValueError as prompt:
        print('\033[36;1mInvalid input,Try again: %s\033[0m' % prompt)
    except (KeyboardInterrupt,EOFError):
        print('\033[32;1m\nBye-bye!\033[0m')
    else:
        print('\033[32;1mSave successfully!\033[0m')
        return save


def cost_it(cost=0): #支出余额
    try:
        if cost != 0:
            cost = input('\033[33;1mcost: \033[0m').strip()[0]
    except ValueError as prompt:
        print('\033[36;1mInvalid input,Try again: %s\033[0m' % prompt)
    except (KeyboardInterrupt,EOFError):
        print('\033[32;1m\nBye-bye!\033[0m')
    else:
        print('\033[32;1mCost successfully!\033[0m')
        return cost


def comment_it(): #零钱明细
    comment = input('\033[33;1mcomment: \033[0m').strip()[0]
    return comment

def view_it(): #账单查询
    print(records)

def write_list(): #写入总表
    records.append(adict)

def show_menu():
    cmds = {'0': save_it,'1': cost_it,'2': view_it}
    prompt = """\033[33;1m(0)save
(1)cost
(2)view
(3)exit
请选择(0/1/2/3/4): \033[0m """
    while True:
        choice = input(prompt).strip()[0]
        if choice == '0':
            save = input('\033[33;1msave: \033[0m').strip()[0]
            save_it(int(save))
            cost_it()
            comment_it()
            adict.clear()
            adict.update(
                {
                    'date': int_data,
                    'save': save_it(),
                    'cost': cost_it(),
                    'balance': counter,
                    'comment': comment_it()
                }
            )
            write_list()
        elif choice == '1':
            cost = input('\033[33;1msave: \033[0m').strip()[0]
            cost_it(int(cost))
            save_it()
            comment_it()
            adict.clear()
            adict.update(
                {
                    'date': int_data,
                    'save': save_it(),
                    'cost': cost_it(),
                    'balance': counter,
                    'comment': comment_it()
                }
            )
            write_list()
        elif choice == '2':
            view_it()
        else:
            break

    cmds[choice]()


if __name__ == '__main__':
    counter = records[-1][-2] - cost_it() if records[-1][-2] > cost_it() else records[-1][-2] + cost_it()
    show_menu()




