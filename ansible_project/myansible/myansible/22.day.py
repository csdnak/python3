#!/bin/env python3
#-*- coding:utf8 -*-
#学python3的第二十二天
"""
## 运维web化项目

- ansible
- django
- bootstrap

"""
"""项目规划
- http://127.0.0.1/：项目首页，列出有哪些功能
- http://127.0.0.1/webadmin/：管理首页，列出所有主机信息
- http://127.0.0.1/webadmin/addhosts/：添加/显示主机和主机组
- http://127.0.0.1/webadmin/addmodules/：添加/显示模块和参数
- http://127.0.0.1/webadmin/tasks/：在指定的主机或组上执行管理任务
-根据规划的url特点创建两个应用:index和webadmin
"""
"""创建初始化项目
首先,通过pycharm创建名为myansible项目
- 数据库用默认的sqlite3，它是一个文件型数据库，默认创建在项目的根目录下，名为db.sqlite3。
mysql是数据库服务器软件，它可以包含很多个库，mysql还可以通过网络提供服务；sqlite是文件型的，
一个文件就是一个库。

# 创建应用
(venv) [root@room8pc16 myansible]# python manage.py startapp index
(venv) [root@room8pc16 myansible]# python manage.py startapp webadmin
# 修改主配置文件
# myansible/settings.py
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    ... ...
    'index',
    'webadmin'
]
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False
STATICFILES_DIRS = [  # 指定静态文件目录还有根目录的static
    os.path.join(BASE_DIR, "static"),
]

# 将前面课程中的static目录拷贝到项目目录下
(venv) [root@room8pc16 myansible]# cp -r /home/student/PycharmProjects/Django/polls/static/ .

#授权,将应用的url交个应用处理
#myansible/usrs.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'webadmin/', include('webadmin.urls')),
    #r''可以匹配任意字符串(要写到最后,因为匹配即停止)
    url(r'', include('index.urls')),
]

# webadmin/urls.py
from django.conf.urls import url

urlpatterns = []

# index/urls.py
from django.conf.urls import url

urlpatterns = []



# 生成数据库表
(venv) [root@room9pc01 myansible]# python manage.py makemigrations
No changes detected
(venv) [root@room9pc01 myansible]# python manage.py migrate
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


# 创建管理员用户
(venv) [root@room8pc16 myansible]# python manage.py createsuperuser
Username (leave blank to use 'student'): csdnak
Email address: csdnak@qq.com             
Password: 
Password (again): 
Superuser created successfully.

"""
"""## 编写index应用
# 编写url
# index/urls.py
urlpatterns = [
    # url从http://x.x.x.x/polls/后面开始匹配
    # 访问投票首页时，使用views.index函数响应
    # 为该url(http://x.x.x.x/polls/)起名为index
    url(r'^$', views.index, name='index'),
]

# 编写函数
# index/views.py
from django.shortcuts import render

# Create your views here.
def index(request):
    # 用户发起的请求将会作为第一个参数传给函数
    # 所以函数至少要定义一个参数来接收用户的请求
    # render负责找寻模板文件发送给用户
    return render(request, 'index.html')


# 实现模板继承
#basic.html
{# 加载static目录内容 #}
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
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
       {% block content %}{% endblock %}
    </div>
{# 居中举办方 #}
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

# 编写模板
#templates/index.html
{% extends 'basic.html' %}
{% load static %}
{% block title %}Ansible Webadmin{% endblock %}
{% block content %}
{#  设置格式为行  四号标题  #}
<div class="row h4">
{# 设置为三行(一行四列),因为最多12个3x4=12  文本居中#}
    <div class="col-sm-3 text-center">
{#     设置超链接(#链接自己)可根据需要修改   #}
        <a href="#">
{#      修改宽度150像素      #}
            <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
            主机信息
        </a>
    </div>
    <div class="col-sm-3 text-center">
        <a href="#">
            <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
            添加主机
        </a>
    </div>
    <div class="col-sm-3 text-center">
        <a href="#">
            <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
            添加模块
        </a>
    </div>
    <div class="col-sm-3 text-center">
        <a href="#">
            <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
            执行任务
        </a>
    </div>
</div>
{% endblock %}



# 引入bootstrap(已经在模板文件basic.html文件里导入了所以不需要做此步骤)
"""
"""编写webadmin

# 创建模型，webadmin/models.py
from django.db import models

# Create your models here.
class HostGroup(models.Model):
    groupname = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return "主机组:%s" % self.groupname

class Host(models.Model):
    hostname = models.CharField(max_length=200)
    ip_addr = models.CharField(max_length=15)
    group = models.ForeignKey(HostGroup)

    def __str__(self):
        return "%s=>%s:%s" % (self.group, self.hostname, self.ip_addr)

class Module(models.Model):
    # unique是否唯一
    modulename = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return "模块:%s" % self.modulename

class Argument(models.Model):
    arg_text = models.CharField(max_length=200)
    module = models.ForeignKey(Module)

    def __str__(self):
        return "%s=>%s" % (self.module, self.arg_text)
        
#生成数据库表
(venv) [root@room9pc01 myansible]# python manage.py makemigrations
Migrations for 'webadmin':
  webadmin/migrations/0001_initial.py
    - Create model Argument
    - Create model Host
    - Create model HostGroup
    - Create model Module
    - Add field group to host
    - Add field module to argument
(venv) [root@room9pc01 myansible]# python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, webadmin
Running migrations:
  Applying webadmin.0001_initial... OK


#查看数据库(没有创建数据库时用以下方法查看是否创建成功)
(venv) [root@room9pc01 myansible]# sqlite3 db.sqlite3   #  sqlite3用于查看数据库生成文件
SQLite version 3.7.17 2013-05-20 00:56:22
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .help  #查看帮助
sqlite> .tables   # show tables;
auth_group                  django_content_type       
auth_group_permissions      django_migrations         
auth_permission             django_session            
auth_user                   webadmin_argument         
auth_user_groups            webadmin_host             
auth_user_user_permissions  webadmin_hostgroup        
django_admin_log            webadmin_module   
sqlite> .schema webadmin_host   # desc webadmin_host
CREATE TABLE "webadmin_host" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "hostname" varchar(200) NOT NULL, "ip_addr" varchar(15) NOT NULL, "group_id" integer NOT NULL REFERENCES "webadmin_hostgroup" ("id"));
CREATE INDEX "webadmin_host_group_id_d1b3c875" ON "webadmin_host" ("group_id");
sqlite> select * from webadmin_host;  #因为现在数据库中没有插入任何数据所以什么也没显示
#ctrl + d(退出)


#注册模型到web后台管理界面
#webadmin/admin.py
from django.contrib import admin
#导入模块
from .models import HostGroup, Host, Module, Argument

# Register your models here.
for item in [HostGroup, Host, Module, Argument]:
    # 循环注册
    admin.site.register(item)

"""
"""## 配置ansible
(venv) [root@room8pc16 myansible]# mkdir ansible_cfg
(venv) [root@room8pc16 myansible]# cd ansible_cfg
(venv) [root@room8pc16 ansible_cfg]# vim ansible.cfg
[defaults]
inventory = dhosts.py
remote_user = root
(venv) [root@room8pc16 ansible_cfg]# touch dhosts.py
(venv) [root@room8pc16 ansible_cfg]# chmod +x dhosts.py

#动态主机清单要求,脚本执行的输出为以下模式
{
    'dbservers': {
        'hosts': ['192.168.1.50']
    },
    '组2': {
        'hosts':[组2的主机列表]
    }
}

# 解题思路
>>> result = {}   # 创建保存结果的字典
>>> if 'webservers' not in result:
...   result['webservers'] = {}
... 
>>> result
{'webservers': {}}
# result['webservers']也是字典
>>> result['webservers']
{}
>>> result['webservers']['hosts'] = []
>>> result
{'webservers': {'hosts': []}}
# result['webservers']['hosts']是列表，可以追加数据
>>> result['webservers']['hosts'].append('192.168.4.5')
>>> result['webservers']['hosts'].append('192.168.4.6')
>>> result
{'webservers': {'hosts': ['192.168.4.5', '192.168.4.6']}}
"""
"""vim dhosts.py

#!/root/nsd1906/bin/python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建到数据库的连接引擎

engine = create_engine(
    'sqlite:////home/student/PycharmProjects/ansible_project/myansible/db.sqlite3',
    encoding='utf8',
)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class HostGroup(Base):
    __tablename__ = 'webadmin_hostgroup'
    id = Column(Integer, primary_key=True)
    groupname = Column(String(20), unique=True)

class Host(Base):
    __tablename__ = 'webadmin_host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(200))
    ipaddr = Column(String(15))
    group_id = Column(Integer, ForeignKey('webadmin_hostgroup.id'))

if __name__ == '__main__':
    session = Session()
    qset = session.query(HostGroup.groupname, Host.ipaddr).join(Host)
    # print(qset.all())
    result = {}
    for g, ip in qset:
        if g not in result:
            result[g] = {}
            result[g]['hosts'] = []
        result[g]['hosts'].append(ip)

    print(result)

"""
"""配置主机信息页

# 生成主机信息页
(venv) [root@room8pc16 ansible_cfg]# ansible all -m setup --tree /tmp/webadmin/
(venv) [root@room8pc16 ansible_cfg]# ansible-cmdb /tmp/webadmin/ > ../templates/webadmin.html

# 编写url, webadmin/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='webadmin'),
]

# 编写函数，webadmin/views.py
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'webadmin.html')

# 修改templates/index.html，为主机信息加超链接
<a href="{% url 'webadmin' %}" target="_blank">
    <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
    主机信息
</a>
"""
"""完成添加主机页
# webadmin/urls.py
    url(r'^addhosts/$', views.add_hosts, name='add_hosts'),

# webadmin/views.py
from django.shortcuts import render
from .models import HostGroup

# Create your views here.
def index(request):
    return render(request, 'webadmin.html')

def add_hosts(request):
    groups = HostGroup.objects.all()
    return render(request, 'add_hosts.html', {'groups': groups})

# templates/add_hosts.html

# templates/index.html
<a href="{% url 'add_hosts' %}">
    <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
    添加主机
</a>
"""
"""修改add_hosts.html
{% extends 'basic.html' %}
{% load static %}
{% block title %}添加主机{% endblock %}
{% block content %}
{#  action为空,表示提交给自己  #}
    <form action="" method="post" class="form-inline h4" >
        {% csrf_token %}
        <div class="form-group">
            <label>主机组: </label>
            <input type="text" class="form-control" name="group">
        </div>
        <div class="form-group">
            <label>主机: </label>
            <input type="text" class="form-control" name="host">
        </div>
        <div class="form-group">
            <label>IP: </label>
            <input type="text" class="form-control" name="ip">
        </div>
        <div class="form-group">
            <input type="submit" class="btn btn-primary" value="提交">
        </div>
    </form>
{#  border格子  #}
    <table class="text-center table table-striped table-hover table-bordered h4">
        <thead class="bg-primary">
            <tr>
                <th class="text-center">主机组</th>
                <th class="text-center">主机</th>
                <th class="text-center">IP</th>
            </tr>
        </thead>
        {% for group in  groups %}
            <tr>
                <td>{{ group.groupname }}</td>
                <td>
                    <ul class="list-unstyled">
                        {% for host in group.host_set.all %}
                            <li>
                                {{ host.hostname }}
                            </li>
                        {% endfor %}
                    </ul>
                </td>
                <td>
                    <ul class="list-unstyled">
                        {% for host in group.host_set.all %}
                            <li>
                                 {{ host.ipaddr }}
                            </li>
                        {% endfor %}
                    </ul>
                </td>
            </tr>
         {% endfor %}
    </table>
{% endblock %}
"""
"""# templates/index.html
<a href="{% url 'add_hosts' %}">
    <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
    添加主机
</a>
"""
"""# 完善add_hosts函数
def add_hosts(request):
    # 如果是表单的post方法，则取出相关的参数，创建主机和组
    if request.method == 'POST':
        group = request.POST.get('group').strip()
        host = request.POST.get('host').strip()
        ip = request.POST.get('ip').strip()
        if group:  # 如果group字符串非空
            # get_or_create返回的是元组: (组实例, True/False)
            g = HostGroup.objects.get_or_create(groupname=group)[0]
            if host and ip:  # 如果host和ip都非空
                g.host_set.get_or_create(hostname=host, ipaddr=ip)

    groups = HostGroup.objects.all()
    return render(request, 'add_hosts.html', {'groups': groups})
"""
