#!/bin/env python3
#-*- coding:utf8 -*-
#学Python3的第十六天
#-----ansible-----
"""如果你链接远程主机是个普通用户,怎么执行管理任务?
#vim ansible.cfg
[defaults]
inventory = inventory
remote_user = csdnak

[priviledge_escalation] #提权
become = yes            #需要切换用户
become_method = sudo    #切换方式是sudo(另一种方式是su)
become_user = root      #切换成管理员
become_ask_pass = no    #不询问切换密码

#被管理的非要我要去,需要配置sudo
#visudo
csdnak ALL=(ALL) NOPASSWD: ALL #设置给csdnak所有sudo权限且不需要输入密码
"""
#***********ansible-cmdb*************
"""将ansible收集的主机信息转换成web页面
# 收集远程主机的信息
(csdnak) [root@room8pc16 myansible]# ansible all -m setup --tree /tmp/csdnakout

# 安装ansible-cmdb
(csdnak) [root@room8pc16 myansible]# pip install /var/ftp/pub/zzg_pypkgs/ansible-cmdb_pkgs/*
# 或在线安装
(csdnak) [root@room8pc16 myansible]# pip install ansible-cmdb

# 生成web页面(hosts文件不能有x权限)
(csdnak) [root@room8pc16 myansible]# ansible-cmdb /tmp/csdnakout > /tmp/hosts.html
(csdnak) [root@room8pc16 myansible]# firefox /tmp/hosts.html &
"""
#****************Git******************
"""
-分布式软件控制系统
"""
"""git配置
#安装
[root@localhost ~]# yum -y install git
#配置基本信息
[root@localhost ~]# git config --global user.name "Mr.Wang"
[root@localhost ~]# git config --global user.email "csdn@ak.com"
[root@localhost ~]# git config --global core.editor vim  #配置编辑器用vim
#查看刚才配置的信息
[root@localhost ~]# git config --list
user.name=Mr.Wang
user.email=csdn@ak.com
core.editor=vim
#or
[root@localhost ~]# cat ~/.gitconfig 
[user]
	name = Mr.Wang
	email = csdn@ak.com
[core]
	editor = vim
"""
"""git的重要工作区域
工作区: 编写代码的工作目录
暂存区: .git/index,工作区和版本库之间的缓冲地带
版本库: 工作区中的.git目录
"""
#******git应用
"""创建版本库,方法一:编写项目之初创建
[root@localhost ~]# git init csdnak
初始化空的 Git 版本库于 /root/csdnak/.git/
[root@localhost ~]# ls -A csdnak/
.git
"""
"""创建版本库,方法二:在已存在的项目中创建版本库
[root@localhost ~]# mkdir ak
[root@localhost ~]# echo "<marquee><font color=red><h1>csdnak</h1>" > ak/test.html
[root@localhost ~]# ls ak/
test.html
[root@localhost ~]# cd ak/
[root@localhost ak]# git init
初始化空的 Git 版本库于 /root/ak/.git/
[root@localhost ak]# ls -A
.git  test.html
"""
"""查看当前库状态
[root@localhost ak]# git status
# 位于分支 master
#
# 初始提交
#
# 未跟踪的文件:
#   （使用 "git add <file>..." 以包含要提交的内容）
#
#	test.html
提交为空，但是存在尚未跟踪的文件（使用 "git add" 建立跟踪）
[root@localhost ak]# git status -s
?? test.html   #??表示未知
"""
"""添加文件
[root@localhost ak]# git status -s
?? test.html
[root@localhost ak]# git add .
[root@localhost ak]# git status -s
A  test.html     #A表示已添加到暂存区
[root@localhost ak]# git status
# 位于分支 master
#
# 初始提交
#
# 要提交的变更：
#   （使用 "git rm --cached <file>..." 撤出暂存区）
#
#	新文件：    test.html
#
[root@localhost ak]# 
"""
"""从暂存区撤除test.html
[root@localhost ak]# git rm --cached test.html
rm 'test.html'
[root@localhost ak]# git status -s
?? test.html
[root@localhost ak]# git status
# 位于分支 master
#
# 初始提交
#
# 未跟踪的文件:
#   （使用 "git add <file>..." 以包含要提交的内容）
#
#	test.html
提交为空，但是存在尚未跟踪的文件（使用 "git add" 建立跟踪）
"""
"""创建.gitignore,忽略不需要加入到版本库的文件
[root@localhost ak]# git status -s
?? passwd
?? test.html
[root@localhost ak]# ls
passwd  test.html
[root@localhost ak]# echo passwd >> .gitignore  #把不需要加入版本仓库的文件放进.gitignore
[root@localhost ak]# echo .gitignore >> .gitignore #.gitignore自己也要放进去
[root@localhost ak]# cat .gitignore 
passwd
.gitignore
[root@localhost ak]# ls
passwd  test.html
[root@localhost ak]# git status -s
?? test.html           #不再显示passwd的状态
"""
"""commit提交
[root@localhost ak]# git add .
[root@localhost ak]# git commit -m test   #-m后跟注释(必须写)
[master（根提交） 89868df] test
 1 file changed, 1 insertion(+)
 create mode 100644 test.html
[root@localhost ak]# git status -s     #没有未知状态文件了
"""
"""删除工作区文件并恢复
1)单个
[root@localhost ak]# rm -f test.html 
[root@localhost ak]# git status
# 位于分支 master
# 尚未暂存以备提交的变更：
#   （使用 "git add/rm <file>..." 更新要提交的内容）
#   （使用 "git checkout -- <file>..." 丢弃工作区的改动）
#
#	删除：      test.html
#
修改尚未加入提交（使用 "git add" 和/或 "git commit -a"）
[root@localhost ak]# git checkout test.html
[root@localhost ak]# git status
# 位于分支 master
无文件要提交，干净的工作区
[root@localhost ak]# ls
passwd  test.html
2)批量
[root@localhost ak]# rm -rf *
[root@localhost ak]# ls
[root@localhost ak]# git status
# 位于分支 master
# 要提交的变更：
#   （使用 "git reset HEAD <file>..." 撤出暂存区）
#
#	新文件：    1
#	新文件：    2
#	新文件：    3
#
# 尚未暂存以备提交的变更：
#   （使用 "git add/rm <file>..." 更新要提交的内容）
#   （使用 "git checkout -- <file>..." 丢弃工作区的改动）
#
#	删除：      1
#	删除：      2
#	删除：      3
#	删除：      test.html
# 
[root@localhost ak]# git checkout -- *
[root@localhost ak]# ls
1  2  3  test.html
[root@localhost ak]# 
"""
"""彻底删除
[root@localhost ak]# git commit -m "rm -f 1 2 3"
# 位于分支 master
# 尚未暂存以备提交的变更：
#   （使用 "git add/rm <file>..." 更新要提交的内容）
#   （使用 "git checkout -- <file>..." 丢弃工作区的改动）
#
#	删除：      1
#	删除：      2
#	删除：      3
#
修改尚未加入提交（使用 "git add" 和/或 "git commit -a"）
[root@localhost ak]# ls
test.html
[root@localhost ak]# git checkout -- *
[root@localhost ak]# ls
test.html
"""
"""切换到某一版本的状态
[root@localhost ak]# git log    #查看日志
commit ccd8a8ebb79aabdf7e264a259853ed39906eb608
Author: Mr.Wang <csdn@ak.com>
Date:   Mon Nov 18 11:51:59 2019 +0800

    rm -f 1 2 3

commit 89868df637aa420bb5e80aee0f93bbea833cf9c0
Author: Mr.Wang <csdn@ak.com>
Date:   Mon Nov 18 11:31:46 2019 +0800

    test
[root@localhost ak]# git checkout ccd8a8ebb79aabdf7e264a259853ed39906eb608
D	1
D	2
D	3
Note: checking out 'ccd8a8ebb79aabdf7e264a259853ed39906eb608'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b new_branch_name

HEAD 目前位于 ccd8a8e... rm -f 1 2 3
[root@localhost ak]# ls
1  2  3  test.html
"""
#*******Git TAG标记
"""
-tag可以为某一次提交设置标记
-如果某一次提交设置为软件的版本号
"""
"""
查看tag
[root@localgit ak]# git tag
为某一次提交设置tag标记
[root@localgit ak]# git tag 1.0
[root@localgit ak]# git tag
1.0
"""
"""分枝管理
#创建分支
[root@localgit ak]# git branch b1
#查看分支
[root@localgit ak]# git branch 
* （分离自 89868df）
  b1
  master

#在master分之上编写代码并提交
[root@localgit csdnak]# cp /etc/passwd .
[root@localgit csdnak]# git add .
[root@localgit csdnak]# git commit -m 'add passwd'
[master（根提交） a7f0724] add passwd
 1 file changed, 21 insertions(+)
 create mode 100644 passwd
[root@localgit csdnak]# ls
passwd
#切换到b1分支
[root@localgit csdnak]# ls
passwd
[root@localgit csdnak]# git checkout b1
切换到分支 'b1'
[root@localgit csdnak]# ls
#切换到master
[root@localgit csdnak]# git checkout master
切换到分支 'master'
#合并分支,将b1汇入主干
[root@localgit csdnak]# git branch
  b1
* master
[root@localgit csdnak]# git merge b1   #在跳出的vim中写入日志
Already up-to-date.
[root@localgit csdnak]# ls
1  2  3  passwd  shadow  test.html
#分支不需要时可以删除
[root@localgit ak]# git help  branch  #查看帮助
[root@localgit ak]# git branch 
  b1
* master
[root@localgit ak]# git branch -d b1
已删除分支 b1（曾为 89868df）。
[root@localgit ak]# git branch 
* master
"""
#*********gitlab服务器***********
"""配置环境
-安装docker并启动
#虚拟机必须3.5G~4G
[root@gitserver ~]# yum -y install docker
[root@gitserver ~]# systemctl restart docker
[root@gitserver ~]# systemctl enable docker
-将镜像导入
[root@gitserver ~]# ls
gitlab_zh.tar
[root@gitserver ~]# docker load -i gitlab_zh.tar 
a94e0d5a7c40: Loading layer 116.5 MB/116.5 MB
88888b9b1b5b: Loading layer 15.87 kB/15.87 kB
52f389ea437e: Loading layer 14.85 kB/14.85 kB
52a7ea2bb533: Loading layer 5.632 kB/5.632 kB
db584c622b50: Loading layer 3.072 kB/3.072 kB
62786ff6a243: Loading layer 75.85 MB/75.85 MB
71bc04f4b7c7: Loading layer 2.048 kB/2.048 kB
26e083d332d8: Loading layer 2.048 kB/2.048 kB
2c02e58e96b8: Loading layer 2.048 kB/2.048 kB
589c7a23de2a: Loading layer 15.87 kB/15.87 kB
44474d2cdcd1: Loading layer 1.359 GB/1.359 GB
41c94e16b901: Loading layer 16.78 MB/16.78 MB
04cafa6a1534: Loading layer   160 MB/160 MB
Loaded image: gitlab_zh:latest
[root@gitserver ~]# docker images 
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
gitlab_zh           latest              1f71f185271a        20 months ago       1.627 GB
# 将docker宿主机ssh端口号改为2022
[root@gitserver ~]# vim /etc/ssh/sshd_config 
Port 2022
[root@gitserver ~]# systemctl restart sshd
# 再次连接时，需要指定端口号
[root@room8pc16 ~]# ssh -p2022 gitserver
# 启动容器
[root@gitserver ~]# docker run -d -h gitlab --name gitlab -p 443:443 -p 80:80 -p 22:22 --restart always -v /srv/gitlab/config:/etc/gitlab -v /srv/gitlab/logs:/var/log/gitlab -v /srv/gitlab/data:/var/opt/gitlab gitlab_zh:latest 
[root@gitserver ~]# docker ps   #STATUS必须出现healthy(启动时间有点长)
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                   PORTS                                                          NAMES
099a45dc7052        gitlab_zh:latest    "/assets/wrapper"   4 minutes ago       Up 4 minutes (healthy)   0.0.0.0:22->22/tcp, 0.0.0.0:80->80/tcp, 0.0.0.0:443->443/tcp   gitlab
[root@room9pc01 ~]# firefox http://192.168.1.30 #起来以后即可访问虚拟机ip
"""
#*******gitlab应用*****
"""
1.登录服务器http://192.168.1.30,设置root密码
2.gitlab重要的概念
    1.群组group:对应一个开发团队
    2.用户,成员member:对应用户账户,可以将用户加入到组或项目
    3.项目:对应软件项目
-创建名为devops的组,类型为公开
-创建一个用户账号,新建用户时,不能设置密码.创建完成后,可以在编辑,以设置密码.
-创建项目：为devops组创建项目，项目名为myweb，类型为公开。
 	为项目授权：点击项目左边栏的设置。将前一步创建的普通用户加入项目，成为主程序员。

#切换为普通用户，上传代码

- 新用户首次登陆时，需要改密码
- 点击项目，因为项目是空的，它将提示你如何操作
  - 创建新版本库：适用于你本地没有任何文件
  - 已存在的文件夹：适用于你已经创建了基目目录，但是没有执行过git init实现初始化
  - 已存在的 Git 版本库：适用于你已经使用git管理的项目目录
"""
"""
[root@node4 ~]# cd myweb/
# 创建仓库，该仓库与一个gitlab项目的url关联
[root@node4 myweb]# git remote add origin http://192.168.4.5/devops/myweb.git
# 推送本地代码到gitlab
[root@node4 myweb]# git push -u origin --all
Username for 'http://192.168.4.5': zzg
Password for 'http://zzg@192.168.4.5': 
# 推送tag到gitlab
[root@node4 myweb]# git push -u origin --tags
Username for 'http://192.168.4.5': zzg
Password for 'http://zzg@192.168.4.5': 

# 如果在add时，有输入错误，可以把它删掉
[root@node4 myweb]# git remote remove origin
"""
"""通过ssh免密上传代码
1. 点击页面右上角用户->设置
2. 把你的公钥复制到“SSH密钥” （左边栏->ssh密钥）
"""
"""
[root@node4 myweb]# ssh-keygen -t rsa -C "zzg@tedu.cn" -b 4096
[root@node4 myweb]# cat ~/.ssh/id_rsa.pub 
"""
"""通过ssh上传代码
# 将http的方式删除
[root@node4 myweb]# git remote remove origin
# 更新上传方式为ssh
[root@node4 myweb]# git remote add origin git@192.168.4.5:devops/myweb.git
# 上传代码
[root@node4 myweb]# echo 'how are you?' > aaa.html
[root@node4 myweb]# git add .
[root@node4 myweb]# git commit -m 'create aaa.html'
[root@node4 myweb]# git push

# 通过http下载
[root@node4 myweb]# cd /tmp/
[root@node4 tmp]# git clone http://192.168.4.5/devops/myweb.git
[root@node4 tmp]# ls -A myweb/
aaa.html  .git  hi.txt  passwd

# 同步代码
[root@node4 tmp]# cd myweb/
[root@node4 myweb]# git pull
Already up-to-date.
"""

#****************复习*******************
# #*********time-module*******
# import time
#
# t = time.localtime() #返回当前时间的九元组
# time.gmtime() #返回格林威治0时区 当前时间的九元组
# time.time() #常用, 与1970-1-1 8:00之间的秒数,时间戳
# time.mktime(t) #吧九元组时间转成时间戳
# time.sleep(1)  #睡1秒
# time.asctime() #如果有参数,是九元组形式
# time.ctime() #返回当前时间,参数是时间戳,常用
# time.strftime('%Y-%m-%d')  #常用
# time.strptime('2018-07-20', '%Y-%m-%d') #返回九元组时间格式
# time.strftime('%H:%M:%S')
################################
# from datetime import datetime
# from datetime import timedelta
# datetime.today() #返回当前时间的datetime对象
# datetime.now() #同上,可以用时区作为参数
# datetime.strptime("2018/06/30", '%Y/%m/%d') #返回datetime对象
# dt = datetime.today()
# datetime.ctime(dt)
# datetime.strftime(dt, "%Y%m%d")
#
# days = timedelta(days=90,hours=3)  #常用
# dt2 = dt + days
# print(dt2.year)
# print(dt2.month)
# print(dt2.day)
# print(dt2.hour)

#*********os模块常用方法
# import os
#
# os.getcwd() #pwd (显示当前路径)
# os.listdir() #ls -a
# os.listdir('/tmp')  #ls -a /tmp
# os.mkdir('/tmp/mydemo') #mkdir /tmp/demo
# os.chdir('/tmp/mydemo') #cd /tmp/demo
# os.listdir()
# os.mknod('test.txt')  #touch test.txt
# os.symlink('/etc/hosts', 'zhuji') #ln -s /etc/hosts zhuji
# os.path.isfile('test.txt') #判断test.txt 是不是文件
# os.path.islink('zhuji') #判断zhuji是不是软连接
# os.path.isdir('/etc') #判断/etc是不是目录
# os.path.exists('/tmp') #判断/tmp是否存在
# os.path.basename('/tmp/abc/aaa.txt') #判断是不是系统变量名
# os.path.dirname('/tmp/abc/aaa.txt')  #判断目录名是否存在
# os.path.split('/tmp/abc/aaa.txt') #分离
# os.path.join('tmp/abc/', 'aaa.txt') #合并
# os.path.abspath('test.txt') #返回当前目录test.txt的绝对路径(/tmp/mydemo/test.txt)

#**************funcation-group***********
# """
# -定义参数时,参数名前面加上*表示使用元组接收参数
# -定义参数时,参数名前加上**表示使用字典接收参数
# """
# def fun1(*args):
#     print(args)
#
# func1() #()
# func1('hao') #(hao,)
# func1('hao', 123) #('hao', 123)
# func1('hao', 123, 'bob', 'alice')
#
# def func2(**kwargs):
#     print(kwargs)
#
# func2() #{}
# func2(name='bob') #{'name': 'bob'}
# func2(name='bob', age=20) #{'name': 'bob', 'age': 20}
# """
# -传参时,*表示吧序列对象拆开
# -传参试,**表示把字典对象拆开
# """
# def fun3(x,y):
#     return x + y
# nums = [10,20]
# func3(*nums) #func3(10,20)  #30
# def func4(name,age):
#     print('%s is %s  years.old.' % (name,age))
#
# adict = {'name':'alice','age': 18}
# func4(**adict)  #func4(name='alice',age=18) -> alice is 18 years old.
#
# #*****匿名函数(忘了单词只能写汉字了)************
# def add(x,y):
#     return x + y
# #可以改写为
# myadd = lambda x, y:x + y
# add(10, 5)  #15
# myadd(10, 5) #15
# ********(filter and map )funcation******
"""filter-funcation
-它接受两个参数.filter(func,seq)
-第一个参数是函数,如func
-第二个参数是序列对象
func它必须接受一个参数,返回值必须是True或False
filter函数工作时,将序列对象中的每一个值作为func的参数进行过滤,结果为真的保留,为假的舍弃.
"""
"""map-funcation
-它接受两个参数.map(func,seq)
-第一个参数是函数,如func
func他必须是一个参数,它将接收到的数据进行处理,然后返回
"""
"""variable
-在函数外面定义的变量是global(全局变量).全局变量从定义开始,到程序结束,任意地方可见可用.
"""
# x = 10
#
#
# def func1():
#     print(x)
#
#
# func1()  # 10
#
#
# # 在函数内定义的变量是局部变量,局部变量只能在函数内部使用.
# def func2():
#     a = 100
#     print(a)
#
#
# func2()  # 100
# print(a)
# """报以下错误
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# NameError: name 'a' is not defined
# """
# # 如果局部和全局有同名变量.局部变量将会遮盖住全局变量.
# x = 10
#
#
# def func3():
#     x = 'hello world'
#     print(x)
#
#
# func3()  # hello world!
# print(x)  # 10 (全局变量x没有受到影响)
#
#
# # 如果希望通过函数改变全局变量,需要使用关键字global
# def func4():
#     global x
#     x = 10000
#     print(x)
#
#
# func4()  # 10000
# print(
#     x  # 10000
# )

