#!/bin/env python3
#-*- coding:utf8 -*-
#学Python3的第二十天
#*****************django**************
#管理网站(应用集成)
"""MTV
- M：Model模型，对应数据库
- T：Template模板，对应web页面
- V：Views视图，对应函数
- URLConf：路由系统，记录了url与函数的对应关系

#流程
c(客户端)--访问-->s(服务器URLConf)
s--调用-->v(Views视图函数)
v--操作-->m(Model数据库模型)
m--返回-->v
v--调用-->t(Template模板)
t--响应-->c
"""
"""安装django
(csdnak) [root@room8pc16 untitled]# pip install /var/ftp/pub/zzg_pypkgs/dj_pkgs/*
# 或在线安装
(csdnak) [root@room8pc16 untitled]# pip install django==1.11.6
Collecting django==1.11.6
  Downloading https://files.pythonhosted.org/packages/82/33/f9d2871f3aed5062661711bf91b3ebb03daa52cc0e1c37925f3e0c4508c5/Django-1.11.6-py2.py3-none-any.whl (6.9MB)
     |████████████████████████████████| 7.0MB 12kB/s 
Collecting pytz
  Downloading https://files.pythonhosted.org/packages/e7/f9/f0b53f88060247251bf481fa6ea62cd0d25bf1b11a87888e53ce5b7c8ad2/pytz-2019.3-py2.py3-none-any.whl (509kB)
     |████████████████████████████████| 512kB 13kB/s 
Installing collected packages: pytz, django
Successfully installed django-1.11.6 pytz-2019.3
"""
"""配置
-创建项目,方法一:直接用django的命令(不推荐)
(csdnak) [root@room9pc01 untitled]# django-admin startproject mytest
(csdnak) [root@room9pc01 untitled]# ls mytest/
manage.py  mytest

-创建项目,方法二:使用pycharm创建.推荐(必须是企业版才能创建)
File -> New Project -> 左窗格选djang,右窗格填写位置
-django默认目录结构
(venv) [root@room9pc01 Django]# pwd
/home/student/PycharmProjects/Django/Django  #项目路径
(venv) [root@room8pc16 Django]# tree .
.
├── manage.py         # 项目管理文件
├── Django            # 项目配置目录
│   ├── __init__.py   # 项目的初始化文件
│   ├── settings.py   # 项目的配置文件
│   ├── urls.py       # 路由文件URLConf
│   └── wsgi.py       # 部署django到web服务器的配置文件
└── templates         # 模板目录

1 directory, 5 files
# django项目最终需要放到nginx或apache上对外提供服务。但量，为了程序员编程上的方便，
django提供了一个测试服务器，以便看到实时的效果。
注意：测试服务器不应该用在生产环境。
"""
"""创建数据库
(venv) [root@room9pc01 Django]# ls
20.day.py  __init__.py  settings.py  urls.py  wsgi.py
(nsd1906) [root@room9pc01 Django]# virsh list --all
 Id    名称                         状态
----------------------------------------------------
 -     gitserver                      关闭
 -     Jenkins                        关闭
 -     localgit                       关闭
 -     mysql                          关闭
(venv) [root@room9pc01 Django]# virsh start mysql
域 mysql 已开始

[student@room9pc01 ~]$ ssh root@192.168.1.50
[root@mysql ~]# mysql -uroot -p123456   #我前几天用过mariadb所以有密码(如果前几天跟着学的小伙伴可以跟我一样设置)
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 2
Server version: 5.5.56-MariaDB MariaDB Server

Copyright (c) 2000, 2017, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> CREATE DATABASE djcsndak DEFAULT CHARSET UTF8;
Query OK, 1 row affected (0.00 sec)

#前几天跟着做的这一步授权可不写,没跟着做的需要做一下
MariaDB [(none)]> grant all on djcsdnak.* to 'root'@'%' identified by '123456'; 
Query OK, 0 rows affected (0.00 sec)

MariaDB [(none)]> quit
Bye
"""
"""修改配置
#mysite/setting.py
ALLOWED_HOSTS = ['*'] #允许所有的客户端访问

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djcsdnak',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
LANGUAGE_CODE = 'zh-hans'  #简体中文(后台也是中文的)

TIME_ZONE = 'Asia/Shanghai' #时区亚洲上海

USE_I18N = True

USE_L10N = True

USE_TZ = False  #关闭

# 初始化数据库模块
# mysite/__init__.py
import pymysql

pymysql.install_as_MySQLdb()
# 重新运行测试服务器，监听在0.0.0.0的80端口。注意：如果不是root，不能监听1024以下端口
(venv) [root@room9pc01 Django]# systemctl stop httpd  #如果被占用就停掉http
(venv) [root@room9pc01 Django]# python manage.py runserver 0:80
Performing system checks...

System check identified no issues (0 silenced).

You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

November 22, 2019 - 11:20:01
Django version 1.11.6, using settings 'Django.settings'
Starting development server at http://0:80/
Quit the server with CONTROL-C.

^Z
[1]+  已停止               python manage.py runserver 0:80
(venv) [root@room9pc01 Django]# bg    #放入后台运行
[1]+ python manage.py runserver 0:80 &

# django项目默认集成了一些应用，这些应用需要把数据写到数据库。
# 初始化数据库
(venv) [root@room9pc01 Django]# python manage.py makemigrations #数据库中生成表
No changes detected
(venv) [root@room9pc01 Django]# python manage.py migrate #真正在数据库中生成
System check identified some issues:

WARNINGS:
?: (mysql.W002) MySQL Strict Mode is not set for database connection 'default'
	HINT: MySQL's Strict Mode fixes many data integrity problems in MySQL, such as data truncation upon insertion, by escalating warnings into errors. It is strongly recommended you activate it. See: https://docs.djangoproject.com/en/1.11/ref/databases/#mysql-sql-mode
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying sessions.0001_initial... OK
  
"""
"""检查数据库初始化导入是否成功
MariaDB [(none)]> use djcsdnak
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [djcsdnak]> show tables;
+----------------------------+
| Tables_in_djcsdnak         |
+----------------------------+
| auth_group                 |
| auth_group_permissions     |
| auth_permission            |
| auth_user                  |
| auth_user_groups           |
| auth_user_user_permissions |
| django_admin_log           |
| django_content_type        |
| django_migrations          |
| django_session             |
+----------------------------+
10 rows in set (0.00 sec)

MariaDB [djcsdnak]> 

"""
"""创建管理员用户(超级用户)
(venv) [root@room9pc01 Django]# python manage.py createsuperuser
Username (leave blank to use 'student'): root
Email address: 9748527@qq.com
Password: 
Password (again): 
Superuser created successfully.
(venv) [root@room9pc01 Django]# 
"""
"""访问
(nsd1906) [root@room9pc01 Django]# firefox http://127.0.0.1/admin
[22/Nov/2019 11:33:32] "GET /admin HTTP/1.1" 301 0
[22/Nov/2019 11:33:32] "GET /admin/ HTTP/1.1" 302 0
[22/Nov/2019 11:33:32] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 1652
[22/Nov/2019 11:33:32] "GET /static/admin/css/base.css HTTP/1.1" 200 16066
[22/Nov/2019 11:33:32] "GET /static/admin/css/login.css HTTP/1.1" 200 1203
[22/Nov/2019 11:33:32] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
[22/Nov/2019 11:33:32] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 80304
[22/Nov/2019 11:33:32] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 81348
Not Found: /favicon.ico
[22/Nov/2019 11:33:32] "GET /favicon.ico HTTP/1.1" 404 1957
Not Found: /favicon.ico
[22/Nov/2019 11:33:32] "GET /favicon.ico HTTP/1.1" 404 1957
^Z
[2]+  已停止               firefox http://127.0.0.1/admin
(nsd1906) [root@room9pc01 Django]# bg
[2]+ firefox http://127.0.0.1/admin &
"""
"""创建应用
-一个项目由很多功能构成,如新闻,博客,论坛等
-每个功能都是一个功能模块,可以由不同的人来开发
-项目拆分成应用模块,简化开发过程
-应用将来还可以直接集成到其他项目
"""
#***************投票应用*************
"""实现的功能
- http://127.0.0.1:8000/polls/：投票首页，列出所有的投票问题
- http://127.0.0.1:8000/polls/1/：投票详情页，用于投票
- http://127.0.0.1:8000/polls/1/result/：投票结果页，显示每个选项的票数
"""
"""具体过程
#创建名为polls的应用
#一个应用对应一个目录,创建polls应用,将出现polls目录
(venv) [root@room9pc01 Django]# python manage.py startapp polls
(venv) [root@room9pc01 Django]# ls
Django  manage.py  polls  templates  venv
#创建了应用,仅仅是出现了一个目录,还需要把它真正的集成到项目
#Django/settings.py
INSTALLED_APPS = [
    ... ...
    'polls',  #吧polls添加到这个位置即可
]

#授权,应用的url交给应用处理,将以/polls/开头的url都交给
urlpatterns = [
    #正则匹配时,从http://x.x.x.x/后面开始算起
    url(r'^admin/', admin.site.urls),
    url(r'^polls/',include('polls.urls'))
]
"""
#polls/urls.py(新建文件)
"""添加以下内容
from django.conf.urls import url

urlpatterns = []
"""
"""编写投票首页
-定义url
#*****polls/urls.py

from django.conf.urls import url
#from polls import views   #也可以用下面的形式
from . import views   #从当前目录(包)导入views模块

urlpatterns = [
    #url从http://x.x.x.x/polls/后面开始匹配
    #访问投票首页时,使用views.index函数响应
    #为该url(http://x.x.x.x/polls/)起名为index
    url(r'^$',views.index,name='index'),
]
"""
"""编写index函数
#polls/views.py (编辑views.py)

from django.shortcuts import render

# Create your views here.
def index(request): #括号中参数名随意
    #用户发起的请求将会作为第一个参数传给函数
    # 所以函数至少要定义一个参数来接收用户的请求
    #render负责找寻模板文件发送给用户
    return render(request,'index.html')
"""
"""编写模板文件
#templates/index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>投票详情</title>
</head>
<body>
<marquee><font color="purple"><h1>{{ question_id }}号问题投票详情</h1></font></marquee>
</body>
</html>
"""
"""编写投票详情页
#polls/urls.py

urlpatterns = [
    #url从http://x.x.x.x/polls/后面开始匹配
    #访问投票首页时,使用views.index函数响应
    #为该url(http://x.x.x.x/polls/)起名为index
    url(r'^$',views.index,name='index'),
    #将\d+用()括起来,他匹配的内容,将会作为detail的参数
    url(r'^(\d+)/$',views.detail,name='detail'),
]
#polls/views.py
...
def detail(request, question_id):
    #字典的内容将会成为模板文件的变量,字典的key是变量名,val是变量值
    return render(request, 'detail.html', {'question_id': question_id})

#templates/detail.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>投票首页</title>
</head>
<body>
<marquee><font color="purple"><h1>投票首页</h1></font></marquee>
</body>
</html>

### 编写投票结果页

```python
# polls/urls.py
urlpatterns = [
    ... ...
    url(r'^(\d+)/result/$', views.result, name='result'),
]

# polls/views.py
def result(request, question_id):
    return render(request, 'result.html', {'question_id': question_id})

# templates/result.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>投票结果</title>
</head>
<body>
<marquee><font color="purple"><h1>{{ question_id }}号问题投票结果</h1></font></marquee>
</body>
</html>
"""
"""数据库模型
-OBM
  - Object对象
  - Relationship关系
  - Mapper映射
-数据库中的表与class相关联
-class中的类变量与标的字段关联
-数据库中的数据类型与django的一些类关联
-表的记录与class的实例字段

"""
"""投票应用的数A据字段
-字段:问题 选项 选项票数
-创建两个模型
    1.问题:问题id,问题内容,发布时间
    2.选项:选项id,选项内容,选项票数,问题id
"""
"""创建模型
-创建实体类
#polls/models.py
from django.db import models

# Create your models here.
class Question(models.Model):
    '实体类必须是models.Model的子类'
    question_text = models.CharField(max_length=200, unique=True)
    pub_date = models.DateTimeField()

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    q = models.ForeignKey(Question)
"""
"""在数据库中生成表
(venv) [root@room9pc01 Django]# python manage.py makemigrations
Migrations for 'polls':
  polls/migrations/0001_initial.py
    - Create model Choice
    - Create model Question
    - Add field q to choice
(venv) [root@room9pc01 Django]# python manage.py migrate 
System check identified some issues:

WARNINGS:
?: (mysql.W002) MySQL Strict Mode is not set for database connection 'default'
	HINT: MySQL's Strict Mode fixes many data integrity problems in MySQL, such as data truncation upon insertion, by escalating warnings into errors. It is strongly recommended you activate it. See: https://docs.djangoproject.com/en/1.11/ref/databases/#mysql-sql-mode
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying polls.0001_initial... OK

"""
"""查看表
MariaDB [djcsdnak]> show tables;  #查看表
+----------------------------+
| Tables_in_djcsdnak         |
+----------------------------+
| auth_group                 |
| auth_group_permissions     |
| auth_permission            |
| auth_user                  |
| auth_user_groups           |
| auth_user_user_permissions |
| django_admin_log           |
| django_content_type        |
| django_migrations          |
| django_session             |
| polls_choice               | #多了俩polls标
| polls_question             |
+----------------------------+
#说明:表明的构成:应用名_class名  全部小写
MariaDB [djcsdnak]> desc polls_question;  #查看表结构
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| id            | int(11)      | NO   | PRI | NULL    | auto_increment |
| question_text | varchar(200) | NO   | UNI | NULL    |                |
| pub_date      | datetime     | NO   |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)
#说明:模型声明中,没有明确声明主键,django自动创建名为id的主键字段

MariaDB [djcsdnak]> desc polls_choice; #查看表结构
+-------------+--------------+------+-----+---------+----------------+
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| id          | int(11)      | NO   | PRI | NULL    | auto_increment |
| choice_text | varchar(200) | NO   |     | NULL    |                |
| votes       | int(11)      | NO   |     | NULL    |                |
| q_id        | int(11)      | NO   | MUL | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)
#说明:Choice模型,q是外键,django自动为它加上_id成为外键字段

"""
"""修改
-修改模型,将q改为question
#polls/models.py
...
class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question)

-将修改反馈到数据库中
(venv) [root@room9pc01 Django]# python manage.py makemigrations
Did you rename choice.q to choice.question (a ForeignKey)? [y/N] y
Migrations for 'polls':
  polls/migrations/0002_auto_20191122_1711.py
    - Rename field q on choice to question
(venv) [root@room9pc01 Django]# python manage.py migrate
System check identified some issues:

WARNINGS:
?: (mysql.W002) MySQL Strict Mode is not set for database connection 'default'
	HINT: MySQL's Strict Mode fixes many data integrity problems in MySQL, such as data truncation upon insertion, by escalating warnings into errors. It is strongly recommended you activate it. See: https://docs.djangoproject.com/en/1.11/ref/databases/#mysql-sql-mode
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying polls.0002_auto_20191122_1711... OK
  
"""
"""查看修改结果
MariaDB [djcsdnak]> desc polls_choice;
+-------------+--------------+------+-----+---------+----------------+
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| id          | int(11)      | NO   | PRI | NULL    | auto_increment |
| choice_text | varchar(200) | NO   |     | NULL    |                |
| votes       | int(11)      | NO   |     | NULL    |                |
| question_id | int(11)      | NO   | MUL | NULL    |                | #发现变了
+-------------+--------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)

"""
"""注册模型到管理后台
#polls/admin.py
from django.contrib import admin
#在当前目录下的models模块中导入模型
from .models import Question, Choice


# Register your models here.
admin.site.register(Question)  #将两个模型注册进去(注册到django控制台)
admin.site.register(Choice)

"""
"""后台管理
#在后台管理界面创建问题,显示的是Question object;创建选项,显示的是Choice object.
-下面修复它:
#polls/model.py
...
class Question(models.Model):
    '实体类必须是models.Model的子类'
    question_text = models.CharField(max_length=200, unique=True)
    pub_date = models.DateTimeField()

    def __str__(self):
        return '问题:%s' % self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question)

    def __str__(self):
        return '%s=>选项:%s' % (self.question, self.choice_text)
#改完后刷新Django web控制台查看 已可以显示所输入的值
"""
"""引入bootstrap
-拷贝昨天的static目录到polls目录
(venv) [root@room8pc16 Django]# cp -r ../../day02/static/ polls/

#templates/index.html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>投票首页</title>
    {#  自动伸缩  #}
    <meta name="viewport" content="width=device-width, initial-scale=1">
    {#  导入bootstrap  #}
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
</head>
<body>
<div class="container">
    <div id="linux-carousel" class="carousel slide">
        <ol class="carousel-indicators">
{#      图片个数      #}
            <li class="active" data-target="#linux-carousel" data-slide-to="0"></li>
            <li data-target="#linux-carousel" data-slide-to="1"></li>
            <li data-target="#linux-carousel" data-slide-to="2"></li>
        </ol>
        <div class="carousel-inner">
{#      导入图片      #}
            <div class="item active">
                <a href="http://www.sogou.com" target="_blank">
                    <img src="{% static 'imgs/first.jpg' %}">
                </a>
            </div>
            <div class="item">
                <img src="{% static 'imgs/second.jpg' %}">
            </div>
            <div class="item">
                <img src="{% static 'imgs/third.jpg' %}">
            </div>
        </div>
{#    轮播图左右移动按键    #}
        <a href="#linux-carousel" data-slide="prev" class="carousel-control left">
            <span class="glyphicon glyphicon-chevron-left"></span>
        </a>
        <a href="#linux-carousel" data-slide="next" class="carousel-control right">
            <span class="glyphicon glyphicon-chevron-right"></span>
        </a>
    </div>
{#  正文内容  #}
    <div>
        <h1 class="text-center text-warning">投票首页</h1>

    </div>
    <div class="h4 text-center">
        CSDN阿坤 <a href="#">csdnak</a>
    </div>
</div>
{# js轮播动态效果 #}
<script src="{% static 'js/jquery.min.js' %}"></script>
<script src="{% static 'js/bootstrap.min.js' %}"></script>
<script type="text/javascript">
    $('#linux-carousel').carousel({
        interval : 3000
    });
</script>
</body>
</html>
"""#说明:必须重启 才能加载出static模块

