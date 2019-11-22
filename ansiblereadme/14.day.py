#!/bin/env python3
#-*- coding:utf8 -*-
#学python3的第十四天(运维开发者工具)
#Ansible批量管理
# """配置简单ansible环境
# [root@room9pc01 ~]# cat  /etc/hosts
# 127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
# ::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
# 192.168.1.50  node4
# 192.168.1.5   node5
# 192.168.1.6   node6
# [root@room9pc01 ~]#mkdir ansiblereadme
# [root@room9pc01 ~]#cd ansiblereadme
# [root@room9pc01 ansiblereadme]#vim ansible.cfg
# [defaults]
# inventory = hosts
# remote_user = root
# host_key_checking = False
#
# #vim hosts
# [dbservers]
# node4
#
# [webservers]
# node5
# node6
# """
# #两种命令管理方式:adhoc,playbook
# #1)adhoc临时命令
# #adhoc方式配置yum
# """
# [root@room9pc01 ansiblereadme]#  ansible all -m yum_repository -a "name=Server baseurl=ftp://192.168.1.254/centos-1804 enabled=yes gpgcheck=no description='Centos 7.4'"
# node5 | CHANGED => {
#     "changed": true,
#     "repo": "Server",
#     "state": "present"
# }
# node6 | CHANGED => {
#     "changed": true,
#     "repo": "Server",
#     "state": "present"
# }
# node4 | CHANGED => {
#     "changed": true,
#     "repo": "Server",
#     "state": "present"
# }
# """
# """检查yum是否配好
# [root@room9pc01 ansiblereadme]# for i in node{4,5,6}
# > do
# > ssh $i 'yum repolist'
# > done
# 已加载插件：fastestmirror
# Loading mirror speeds from cached hostfile
# 源标识                             源名称                                  状态
# Server                             Centos 7.4                              9,911
# local_repo                         CentOS-7 - Base                         9,911
# repolist: 19,822
# 已加载插件：fastestmirror
# Determining fastest mirrors
# 源标识                             源名称                                  状态
# Server                             Centos 7.4                              9,911
# local_repo                         CentOS-7 - Base                         9,911
# repolist: 19,822
# 已加载插件：fastestmirror
# Determining fastest mirrors
# 源标识                             源名称                                  状态
# Server                             Centos 7.4                              9,911
# local_repo                         CentOS-7 - Base                         9,911
# repolist: 19,822
# """
# #2)playbook创建lamp环境
# """修改vim配置,适应yaml语法(非必须)
# [root@room9pc01 ansiblereadme]# vim ~/.vimrc
# [root@room9pc01 ansiblereadme]# cat ~/.vimrc
# autocmd FileType yaml setlocal sw=2 ts=2 et ai
# """
# """编写playbook配置lamp
# [root@room9pc01 ansiblereadme]# vim lamp.yml
# [root@room9pc01 ansiblereadme]# cat lamp.yml
# ---
# - name: configure webservers
#   hosts: webservers
#   tasks:
#     - name: install web pkgs
#       yum:
#         name: httpd, php, php-mysql
#         state: installed
#
#     - name: configure web service
#       service:
#         name: httpd
#         state: started
#         enabled: yes
#
# - name: configure dbservers
#   hosts: dbservers
#   tasks:
#     - name: install db pkgs
#       yum:
#         name: mariadb-server
#         state: present
#     - name: configure db service
#       service:
#         name: mariadb
#         state: started
#         enabled: yes
# """
# """检查配置文件语法
# [root@room9pc01 ansiblereadme]# ansible-playbook --syntax-check lamp.yml
#
# playbook: lamp.yml
# """
# """执行playbook
# [root@room9pc01 ansiblereadme]# ansible-playbook lamp.yml
#
# PLAY [configure webservers] *****************************************************************
#
# TASK [Gathering Facts] **********************************************************************
# ok: [node6]
# ok: [node5]
#
# TASK [install web pkgs] *********************************************************************
# ok: [node6]
# ok: [node5]
#
# TASK [configure web service] ****************************************************************
# changed: [node6]
# changed: [node5]
#
# PLAY [configure dbservers] ******************************************************************
#
# TASK [Gathering Facts] **********************************************************************
# ok: [node4]
#
# TASK [install db pkgs] **********************************************************************
# ok: [node4]
#
# TASK [configure db service] *****************************************************************
# ok: [node4]
#
# PLAY RECAP **********************************************************************************
# node4                      : ok=3    changed=1    unreachable=0    failed=0
# node5                      : ok=3    changed=1    unreachable=0    failed=0
# node6                      : ok=3    changed=1    unreachable=0    failed=0
# """
# """检查是否成功
# [root@room9pc01 ansiblereadme]# check () {
# > ssh node4 'netstat -ntlupa|grep 3306'
# > ssh node5 'netstat -ntlupa|grep 80'
# > ssh node6 'netstat -ntlupa|grep 80'
# > }
# [root@room9pc01 ansiblereadme]# check
# tcp        0      0 0.0.0.0:3306            0.0.0.0:*               LISTEN      835/mysqld
# tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      23818/httpd
# tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      23801/httpd
# """
"""ansible编程(主要用途:以Python调用Ansible)
ansile官方站点：https://docs.ansible.com/ansible/2.7/index.html
 -> 搜索 python api -> 将示例代码拷贝出来，执行。
 确认可执行后 修改如下内容再次执行!
"""
#***************python API****************
# #!/usr/bin/env python
#
# import shutil
# from collections import namedtuple
# from ansible.parsing.dataloader import DataLoader
# from ansible.vars.manager import VariableManager
# from ansible.inventory.manager import InventoryManager
# from ansible.playbook.play import Play
# from ansible.executor.task_queue_manager import TaskQueueManager
# import ansible.constants as C
#
# # since API is constructed for CLI it expects certain options to always be set, named tuple 'fakes' the args parsing options object
# # option用于定义选项，绝大部分使用默认值即可
# # connection是连接方式，有三种：
# # local: 本地执行指令；ssh: 通过ssh连接执行；smart：自动判断
# # fork指定可以创建的进程数，每个进程连接一台服务器
# Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
# # options = Options(connection='local', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)
# options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)
#
# # initialize needed objects
# # DataLoader负责将yaml、json、ini等文件转换成python的数据类型
# loader = DataLoader() # Takes care of finding and reading yaml, json and ini files
# #存储加密密码
# passwords = dict(vault_pass='secret')
#
# # create inventory, use path to host config file as source or hosts in a comma separated string
# #主机清单 有两种形式,一种是用逗号将所有的主机分割的字符串
# #另一种形式,是使用列表将主机清单文件位置包含
# inventory = InventoryManager(loader=loader, sources='ansiblereadme/hosts')
#
# # variable manager takes care of merging all the different sources to give you a unifed view of variables available in each context
# #用于保管变量的管理器
# variable_manager = VariableManager(loader=loader, inventory=inventory)
#
# # create datastructure that represents our play, including tasks, this is basically what our YAML loader does internally.
# #创建代表play的数据结构
# play_source =  dict(
#         name = "Ansible Play",
#         hosts = 'webservers', #在那些主机上执行任务
#         gather_facts = 'no',
#         tasks = [
#             dict(action=dict(module='shell', args='ls'), register='shell_out'),
#             dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
#          ]
#     )
#
# # Create play object, playbook objects use .load instead of init or new methods,
# # this will also automatically create the task objects from the info provided in play_source
# #创建一个play对象
# play = Play().load(play_source, variable_manager=variable_manager, loader=loader)
#
# # Run it - instantiate task queue manager, which takes care of forking and setting up all objects to iterate over host list and tasks
# #创建任务队列管理器,用于调度执行play
# tqm = None
# try:
#     tqm = TaskQueueManager(
#               inventory=inventory,
#               variable_manager=variable_manager,
#               loader=loader,
#               options=options,
#               passwords=passwords,
#           )
#     result = tqm.run(play) # most interesting data for a play is actually sent to the callback's methods
# finally:
#     # we always need to cleanup child procs and the structres we use to communicate with them
#     #请理执行后的环境,如删除临时文件
#     if tqm is not None:
#         tqm.cleanup()
#
#     # Remove ansible tmpdir
#     shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)
"""执行
(csdnak) [root@room9pc01 untitled]# ./14.day.py 

PLAY [Ansible Play] *****************************************************************

TASK [shell] ************************************************************************
changed: [node6]
changed: [node5]

TASK [debug] ************************************************************************
ok: [node5] => {
    "msg": ""
}
ok: [node6] => {
    "msg": ""
}

"""
#Ansible加密/解密文件测试
"""对应上方passwords选项(选用)
# 加密文件
[root@room8pc16 ansiblereadme]# echo 'hello world' > hi.txt
[root@room8pc16 ansiblereadme]# cat hi.txt 
hello world
[root@room8pc16 ansiblereadme]# ansible-vault encrypt hi.txt 

# 解密
[root@room8pc16 ansiblereadme]# ansible-vault decrypt hi.txt 
"""
#****************Funcation Python API*****************************
"""
还可添加sys模块用sys.argv模块来进行传参操作!
可直接当成模块import啦!
"""
# #!/bin/env python3
# import shutil
# from collections import namedtuple
# from ansible.parsing.dataloader import DataLoader
# from ansible.vars.manager import VariableManager
# from ansible.inventory.manager import InventoryManager
# from ansible.playbook.play import Play
# from ansible.executor.task_queue_manager import TaskQueueManager
# import ansible.constants as C
#
# def adhoc(sources, hosts, module, args):
#     Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
#     options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)
#     loader = DataLoader() # Takes care of finding and reading yaml, json and ini files
#     passwords = dict(vault_pass='secret')
#     inventory = InventoryManager(loader=loader, sources=sources)
#     variable_manager = VariableManager(loader=loader, inventory=inventory)
#     play_source=dict(
#             name="Ansible Play",
#             hosts=hosts,  # 在哪些主机上执行任务
#             gather_facts='no',
#             tasks=[
#                 dict(action=dict(module=module, args=args), register='shell_out'),
#                 dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
#              ]
#         )
#     play = Play().load(play_source, variable_manager=variable_manager, loader=loader)
#     tqm = None
#     try:
#         tqm = TaskQueueManager(
#                   inventory=inventory,
#                   variable_manager=variable_manager,
#                   loader=loader,
#                   options=options,
#                   passwords=passwords,
#               )
#         result = tqm.run(play) # most interesting data for a play is actually sent to the callback's methods
#     finally:
#         if tqm is not None:
#             tqm.cleanup()
#
#         shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)
# if __name__ == '__main__':
#     adhoc(sources=['ansiblereadme/hosts'], hosts='dbservers', module='shell', args='id root')
"""执行
(csdnak) [root@room9pc01 untitled]# ./14.day.py 

PLAY [Ansible Play] *****************************************************************

TASK [shell] ************************************************************************
changed: [node4]

TASK [debug] ************************************************************************
ok: [node4] => {
    "msg": "uid=0(root) gid=0(root) 组=0(root)"
}
"""
#***********************Python3 Funcation Playbook************************
"""
实现python调用playbook
"""
# #!/bin/env python3
# from collections import namedtuple
# from ansible.parsing.dataloader import DataLoader
# from ansible.vars.manager import VariableManager
# from ansible.inventory.manager import InventoryManager
# from ansible.executor.playbook_executor import PlaybookExecutor
#
# def runpb(hosts_list, playbooks):
#     Options = namedtuple('Options',
#                          ['connection',
#                           'remote_user',
#                           'ask_sudo_pass',
#                           'verbosity',
#                           'ask_pass',
#                           'module_path',
#                           'forks',
#                           'become',
#                           'become_method',
#                           'become_user',
#                           'check',
#                           'listhosts',
#                           'listtasks',
#                           'listtags',
#                           'syntax',
#                           'sudo_user',
#                           'sudo',
#                           'diff'])
#     options = Options(connection='smart',
#                       remote_user='root',
#                       ask_pass=None,
#                       sudo_user=None,
#                       forks=5,
#                       sudo=None,
#                       ask_sudo_pass=False,
#                       verbosity=5,
#                       module_path=None,
#                       become=None,
#                       become_method=None,
#                       become_user=None,
#                       check=False,
#                       diff=False,
#                       listhosts=None,
#                       listtasks=None,
#                       listtags=None,
#                       syntax=None)
#     loader = DataLoader()
#     passwords = dict()
#     inventory = InventoryManager(loader=loader, sources=hosts_list)
#     variable_manager = VariableManager(loader=loader, inventory=inventory)
#     playbook = PlaybookExecutor(
#         playbooks=playbooks,
#         inventory=inventory,
#         variable_manager=variable_manager,
#         loader=loader,
#         options=options,
#         passwords=passwords
#     )
#     result = playbook.run()
#     return result
#
# if __name__ == '__main__':
#     print(runpb(['ansiblereadme/hosts'], playbooks=['ansiblereadme/lamp.yml']))
#
"""执行(因为前面执行过安装mariadb httpd所以改变结果为0 )
(csdnak) [root@room9pc01 untitled]# ./14.day.py 

PLAY [configure webservers] *********************************************************

TASK [Gathering Facts] **************************************************************
ok: [node5]
ok: [node6]

TASK [install web pkgs] *************************************************************
ok: [node5]
ok: [node6]

TASK [configure web service] ********************************************************
ok: [node5]
ok: [node6]

PLAY [configure dbservers] **********************************************************

TASK [Gathering Facts] **************************************************************
ok: [node4]

TASK [install db pkgs] **************************************************************
ok: [node4]

TASK [configure db service] *********************************************************
ok: [node4]

PLAY RECAP **************************************************************************
node4                      : ok=3    changed=0    unreachable=0    failed=0   
node5                      : ok=3    changed=0    unreachable=0    failed=0   
node6                      : ok=3    changed=0    unreachable=0    failed=0   

0

"""
#*****************************************************************
# """命名的元组
# - 本质上还是元组
# - 元组通过下标取值
# - 命名的元组只是给下标起名。可以通过名字进行取值
# """
# from collections import namedtuple
# Poin = namedtuple('Point',['x','y','z'])
# p1 = Poin(10, 20, 15)
# print(p1[1:])  #(20, 15)
# print(p1[-1])  #15
# print(p1.x)  #10
# print(p1.y)  #20
# print(p1.z)  #15
#*****************************************************************
#将yaml文件转成python数据库类型(手动版本)
"""
-开头的转成列表
:开头的转成字典
"""
#一个playbook由两个play构成,每个play都是一个列表项
#每个play又是一个字典结构
# [
#     {
#         name: configure webservers,
#         hosts: webservers,
#         tasks: [
#             {
#                 name: install web pkgs,
#                 yum: {
#                     name: httpd, php, php-mysql,
#                     state: present
#                 }
#             },
#             {
#                 name: configure web service,
#                 service: {
#                     name: httpd,
#                     state: started,
#                     enabled: yes
#                 }
#             },
#         ],
#     },
#     {
#         name: configure dbservers,
#         hosts: dbservers,
#         tasks: [
#             {
#                 name: install db pkgs,
#                 yum: {
#                     name: mariadb-server,
#                     state: present
#                 }
#             },
#             {
#                 name: configure db service,
#                 service: {
#                     name: mariadb,
#                     state: started,
#                     enabled: yes
#                 }
#             }
#         ]
#     },
# ]

#*********创建ansible模块目录**********
"""必须做此步骤(否则模块不能用)
(csdnak) [root@room9pc01 untitled]# mkdir /tmp/mylib
(csdnak) [root@room9pc01 untitled]# export ANSIBLE_LIBRARY=/tmp/mylib
(csdnak) [root@room8pc16 day03]# vim /tmp/mylib/rcopy.py
"""
# #!/bin/env python3
# #实现copy功能
# from ansible.module_utils.basic import AnsibleModule
# import shutil
#
# def main():
#     module = AnsibleModule(
#         argument_spec=dict(
#             source=dict(required=True, type='str'),
#             destination=dict(required=True, type='str')
#         )
#     )
#     shutil.copy(module.params['source'], module.params['destination'])
#     module.exit_json(changed=True)
#
# if __name__ == '__main__':
#     main()
"""执行
(csdnak) [root@room9pc01 ansiblereadme]# ansible dbservers -m 14.day -a "source=/etc/hosts destination=/tmp/csdnak"
node4 | CHANGED => {
    "changed": true
}
#查看node4上是否有阿坤文件
(csdnak) [root@room9pc01 ansiblereadme]# ssh node4 'ls /tmp/csdnak'
/tmp/csdnak
"""
#************************
"""实现以下程序必须保证src和dst两机python都有wget模块
- 在http://pypi.org查找并下载wget
- 拷贝wget到目标主机
[root@node4 ~]# unzip wget-3.2.zip 
[root@node4 ~]# cd wget-3.2/
[root@node4 wget-3.2]# python setup.py install
"""
#!/bin/env python3
#实现资源下载
from ansible.module_utils.basic import  AnsibleModule
import wget

def main():
    module = AnsibleModule(
        argument_spec=dict(
            url=dict(required=True, type='str'),
            dest=dict(required=True, type='str')
        )
    )
    wget.download(module.params['url'], module.params['dest'])
    module.exit_json(changed=True)

if __name__ == '__main__':
    main()

