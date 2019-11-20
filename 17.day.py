#!/bin/env python3
#-*- coding:utf8 -*-
#学Python3的第十七天(CI/CD项目)
#*****************Jenkins********************
"""项目所需机器环境
-一台localgit虚拟机:用来当做程序员敲代码的服务器
    配置:运行内存500MB即可
    IP:192.168.1.31
-一台gitserver虚拟机:部署gitlab服务(跟github是一个东西)
    配置:运行内存3.5G~4G推荐4G
    IP:192.168.1.30
-一台Jenkins虚拟机:部署jenkins(CI交付工具)服务
    配置:运行内存500MB即可
    IP:192.168.1.32
"""
"""CI/CD:持续集成/持续交付
-流程:
    开发部门->交付给测试部->反馈给开发部的同时->交付给运维部
graph LR
d(开发部)--交付-->qa(测试部)
qa--反馈-->d
qa--交付-->o(运维部)
"""
"""程序语言
- 解释型语言：python / shell / php
- 编译型语言：C / C++ / Java / Go
    examples:
        [root@jenkins ~]# yum -y install gcc
        [root@jenkins ~]# vim hello.c
        [root@jenkins ~]# cat hello.c 
        #include <stdio.h>
        
        int main(void){
            printf("Hello World!\n");
            return 0;
        }
        [root@jenkins ~]# gcc -o hello hello.c 
        [root@jenkins ~]# ls
        hello  hello.c  jenkins-2.190.1-1.1.noarch.rpm
        [root@jenkins ~]# ./hello 
        Hello World!
"""
"""Jenkins(java写的)
-是一个CI交付工具:
    graph LR
    d(程序员)--上传-->g(gitlab)
    j(jenkins服务器)--下载-->g
    a1(应用服务器)--下载-->j
    a2(应用服务器)--下载-->j
    a3(应用服务器)--下载-->j
-由于Jenkins是java写的,所以需要java环境:
    需要接入互联网、需要安装了java

[root@jenkins ~]# yum -y install java-1.8.0-openjdk
[root@jenkins ~]# ls
jenkins-2.190.1-1.1.noarch.rpm     #自行下载
[root@jenkins ~]# rpm -ih jenkins-2.190.1-1.1.noarch.rpm 
警告：jenkins-2.190.1-1.1.noarch.rpm: 头V4 DSA/SHA1 Signature, 密钥 ID d50582e6: NOKEY
################################# [100%]
正在升级/安装...
################################# [100%]
[root@jenkins ~]# systemctl start jenkins
[root@jenkins ~]# systemctl enable jenkins
jenkins.service is not a native service, redirecting to /sbin/chkconfig.
Executing /sbin/chkconfig jenkins on
[root@jenkins ~]# firefox 192.168.1.32:8080
#访问http://x.x.x.x:8080 -> 根据提示解锁 -> 自定义部分，点击“选择插件来安装”，再选“无”后安装 -> 创建第一个管理员，选右下角“使用admin继续登陆“ -> 保存并完成 -> 开始使用
[root@jenkins ~]# cat /var/lib/jenkins/secrets/initialAdminPassword 
6b9ab6b453d2429c9468adc30e8ad2fa
"""
"""修改管理员密码改为国内镜像站点安装插件
首页 -> Manage Jenkins -> Manage Plugins -> Advanced -> Update Site: https://mirrors.tuna.tsinghua.edu.cn/jenkins/ -> Submit
页面右上角admin -> configure -> password -> Save
"""
"""安装插件
Available -> 按ctrl + f搜索 -> 选中Localization: Chinese (Simplified)和Git Parameter -> Install without restart -> 勾选Restart Jenkins when installation is complete and no jobs are running
"""
"""CI/CD流程
***1).程序猿在自己的电脑上编写代码
[root@localgit ~]# mkdir myweb
[root@localgit ~]# cd myweb/
[root@localgit myweb]# git init
初始化空的 Git 版本库于 /root/myweb/.git/
[root@localgit myweb]# echo "<marquee><font color=yellow><h1>Hello world</h1>" > index.html
[root@localgit myweb]# git add .
[root@localgit myweb]# git commit -m 'my site 1.0'
[master（根提交） b984e1d] my site 1.0
 1 file changed, 1 insertion(+)
 create mode 100644 index.html
[root@localgit myweb]# git tag 1.0
[root@localgit myweb]# echo '<h2>my site 2.0</h2>' >> inedx.html
[root@localgit myweb]# git add .
[root@localgit myweb]# git commit -m "my site 2.0"
[master 0e3a6f9] my site 2.0
 1 file changed, 1 insertion(+)
 create mode 100644 inedx.html
[root@localgit myweb]# git tag 2.0

***2).管理员在gitlab上创建项目,类型为公开,为组创建.添加昨天创建的普通用户为该项目的主程序猿

***3).程序员上传代码到gitlab服务器
[root@localgit myweb]# git remote add origin http://192.168.1.30/newgroup/website.git
[root@localgit myweb]# git push -u origin --all
Username for 'http://192.168.1.30': csdnak
Password for 'http://csdnak@192.168.1.30': 
Counting objects: 6, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (6/6), 509 bytes | 0 bytes/s, done.
Total 6 (delta 0), reused 0 (delta 0)
To http://192.168.1.30/newgroup/website.git
 * [new branch]      master -> master
分支 master 设置为跟踪来自 origin 的远程分支 master。
[root@localgit myweb]# git push -u origin --tags
Username for 'http://192.168.1.30': csdnak
Password for 'http://csdnak@192.168.1.30': 
Total 0 (delta 0), reused 0 (delta 0)
To http://192.168.1.30/newgroup/website.git
 * [new tag]         1.0 -> 1.0
 * [new tag]         2.0 -> 2.0
 
***4).配置jenkins下载代码
[root@jenkins ~]# yum -y install git
#Jenkins网页操作
新建Item -> 任务名：website / Freestyle project -> 勾选This project is parameterized -> 添加参数 -> Git Parameter => Name: webver / Parameter Type: Branch or Tag  / Default Value: origin/master -> 源码管理 => Git => Repository URL: http://192.168.1.30/newgroup/website.git / Branches to build：$webver -> 保存

构建：

Build with Parameters -> 选择相关的tag进行构建。构建完成的内容自动放到了/var/lib/jenkins/workspace目录
-然后点击左边Build with Parameters里面的1.0->开始构建->2.0->开始构建:
-到Jenkins服务器上查看
[root@jenkins ~]# ls  /var/lib/jenkins/workspace/website
index.html  inedx.html
[root@jenkins ~]# cat /var/lib/jenkins/workspace/website/*
<marquee><font color=yellow><h1>Hello world</h1>
<h2>my site 2.0</h2>

***5).修改工程.将程序下载到子目录中.配置->源码管理->Additional Behaviours=>
Checkout to a sub-direcotry:  website-$webver -> 保存后构建测试

***6).修改工程:
    1.将软件目录拷贝到/var/www/html/deploy/pkgs
    2.将软件目录下的.git隐藏目录删除
    3.将软件目录打包,便于下载
    4.删除软件目录
    5.计算压缩包的md5值
    6.生成/var/www/html/deploy/{last_ver,live_ver}两个文件,分别记录前一版本号和当前版本号

[root@jenkins ~]# yum -y install httpd    
[root@jenkins ~]# systemctl restart httpd
[root@jenkins ~]# systemctl enable httpd
Created symlink from /etc/systemd/system/multi-user.target.wants/httpd.service to /usr/lib/systemd/system/httpd.service.
[root@jenkins ~]# mkdir -p /var/www/html/deploy/pkgs
[root@jenkins ~]# chown -R jenkins.jenkins /var/www/html/deploy
"""
"""execute shell中添写的脚本代码：
deploy_dir=/var/www/html/deploy/pkgs  #定义变量
cp -r website-$webver $deploy_dir   #拷贝软件目录到web目录
cd $deploy_dir  #切换到web目录
rm -rf website-$webver/.git  #删除版本库文件
tar czf website-$webver.tar.gz website-$webver   #打包压缩
rm -rf website-$webver    #删除软件目录,只保留压缩包
#计算压缩包的md5值
md5sum website-$webver.tar.gz |awk '{print $1}' > website-$webver.tar.gz.md5
#生成last_ver和live_ver文件
cd ..
[-f live_ver]&&cat live_ver > last_ver
echo $webver > live_ver
"""
"""自动部署
- /var/www/download:保存下载的压缩包
- /var/www/deploy:保存live_ver文件和解压目录
- /var/www/html/csdnak:指向发不的应用目标
脚本具体作用:
    程序员开发完新版->发布到gitlab->jenkins构建新项目->deploy.py实现自动部署上线新版本程序
"""
#deploy.py
import wget
import os
import requests
import hashlib
import tarfile

def has_new_ver(ver_url, ver_fname):
    '有新版本返回True，否则返回False'
    # 如果本地没有版本文件，则为True
    if not os.path.isfile(ver_fname):
        return True

    # 取出本地版本
    with open(ver_fname) as fobj:
        local_ver = fobj.read()

    # 本地版本与网上版本比较，如果不一致返回True
    r = requests.get(ver_url)
    if local_ver != r.text:
        return True
    else:
        return False

def file_ok(md5_url, fname):
    '如果文件已损坏返回False，否则返回True'
    # 计算本地文件的md5值
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while 1:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    # 取出网上的md5值，进行比较
    r = requests.get(md5_url)
    if m.hexdigest() == r.text.strip():
        return True
    else:
        return False

def deploy(app_fname):
    '部署软件'
    deploy_dir = '/var/www/deploy'
    dest = '/var/www/html/csdnak'
    # 解压
    tar = tarfile.open(app_fname)
    tar.extractall(path=deploy_dir)
    tar.close()

    # 取出软件目录名
    app_dir = app_fname.split('/')[-1]
    app_dir = app_dir.replace('.tar.gz', '')
    app_dir = os.path.join(deploy_dir, app_dir)

    # 如果目标链接文件已存在，先删除
    if os.path.exists(dest):
        os.remove(dest)

    # 创建软链接
    os.symlink(app_dir, dest)


if __name__ == '__main__':
    # 判断是否有新版本，没有则退出
    ver_url = 'http://192.168.1.32/deploy/live_ver'
    ver_fname = '/var/www/deploy/live_ver'
    if not has_new_ver(ver_url, ver_fname):
        print('未发现新版本。')
        exit(1)

    # 下载新版本软件
    r = requests.get(ver_url)
    ver = r.text.strip()  # 把额外的\n删除，得到版本
    app_url = 'http://192.168.1.32/deploy/pkgs/website-%s.tar.gz' % ver
    down_dir = '/var/www/download'
    wget.download(app_url, down_dir)

    # 校验。如果下载的文件已损坏，删除它
    md5_url = app_url + '.md5'
    app_fname = app_url.split('/')[-1]
    app_fname = os.path.join(down_dir, app_fname)
    if not file_ok(md5_url, app_fname):
        os.remove(app_fname)
        print('文件已损坏。')
        exit(2)

    # 部署软件
    deploy(app_fname)

    # 更新live_ver文件的版本
    if os.path.exists(ver_fname):
        os.remove(ver_fname)

    wget.download(ver_url, ver_fname)

"""项目执行顺序(再次强调)
(程序员)localgit->发布到gitlab服务器上->在jenkins构建新项目->利用以上脚本deploy.py实现自动部署上线新版本程序
"""
#具体过程如下
"""发布1.0版本
[root@room9pc01 ~]# cd /var/www/
[root@room9pc01 www]# mkdir download
[root@room9pc01 untitled]# ./17.day.py    #执行脚本查看效果
100% [.......................................................................] 4 / 4
[root@room9pc01 www]# ls
cgi-bin  deploy  download  exam  html
[root@room9pc01 www]# ls deploy/
live_ver  website-1.0   #版本号
[root@room9pc01 www]# ls download/
website-1.0.tar.gz    #版本包
[root@room9pc01 www]# ls html/ 
csdnak  #生成的软连接
[root@room9pc01 www]# firefox http://127.0.0.1/csdnak/   #访问你的软链接,内容就是1.0版本网页内容
"""
"""发布4.0版本(gitlab必须构建了4.0版本)
[root@room9pc01 untitled]# ./17.day.py 
100% [.......................................................................] 4 / 4
[root@room9pc01 www]# ls  deploy/ download/ html/
deploy/:
live_ver  website-1.0  website-4.0         #版本号也多出来一个4.0

download/:
website-1.0.tar.gz  website-4.0.tar.gz       #可以看到多出一个4.0版本包

html/:
csdnak         #链接已被重置,直接访问看效果即可

[root@room9pc01 www]# firefox http://127.0.0.1/csdnak/
"""
#如果想相返回旧版本可以写一个回滚脚本
"""回滚思路
-取出last_ver版本号,赋值给ver
-构建本地目录'/var/www/deploy/website-%s' % ver
-把/var/www/html/nsd1906删除
-创建软链接
"""
#
# def has_new_ver(ver_url, ver_fname):
#     '有新版本返回True，否则返回False'
#     # 如果本地没有版本文件，则为True
#     if not os.path.isfile(ver_fname):
#         return True
#
#     # 取出本地版本
#     with open(ver_fname) as fobj:
#         local_ver = fobj.read()
#
# def deploy(app_fname):
#     '部署软件'
#     deploy_dir = '/var/www/deploy'
#     dest = '/var/www/html/csdnak'
#     # 解压
#     tar = tarfile.open(app_fname)
#     tar.extractall(path=deploy_dir)
#     tar.close()
#
#     # 取出软件目录名
#     app_dir = app_fname.split('/')[-1]
#     app_dir = app_dir.replace('.tar.gz', '')
#     app_dir = os.path.join(deploy_dir, app_dir)
#
#     # 如果目标链接文件已存在，先删除
#     if os.path.exists(dest):
#         os.remove(dest)
#
#     # 创建软链接
#     os.symlink(app_dir, dest)
#
# if __name__ == '__main__':
#     # 校验。如果下载的文件已损坏，删除它
#     md5_url = app_url + '.md5'
#     app_fname = app_url.split('/')[-1]
#     app_fname = os.path.join(down_dir, app_fname)
#     if not file_ok(md5_url, app_fname):
#         os.remove(app_fname)
#         print('文件已损坏。')
#         exit(2)
#
#     # 部署软件
#     deploy(app_fname)
#
#     # 更新live_ver文件的版本
#     if os.path.exists(ver_fname):
#         os.remove(ver_fname)
