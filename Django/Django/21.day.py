#!/bin/env python
#-*- coding:utf8 -*-
#学Python3的第二十一天
#Django是python写的web前段框架
#******承接昨天项目********
"""使用python shell:对mysql进行curl操作(增删改查)
#一定要用manage.py进入python(能够初始化Django环境)
(venv) [root@room9pc01 Django]# python manage.py shell
Python 3.6.7 (default, Feb 20 2019, 15:08:07)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-36)] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
#导入模型
>>> from polls.models import Question, Choice

#创建问题,方法一:直接创建实例
>>> q1 = Question(question_text="散伙饭去哪吃?", pub_date='2019-1-25')
>>> q1.save()   #需要保存,Django页面才会显示
<bound method Model.save of <Question: 问题:散伙饭去哪吃?>>

# 创建问题，方法二：使用objects管理器。django为每个实体类都创建了一个名为objects的管理，通过它的方法可以实现对模型的增删改查等操作。
# get_or_create是，如果没有相关记录则创建，如果库中已有相关记录则取出
>>> q2 = Question.objects.get_or_create(question_text="你打算到哪 个城市找工作？", pub_date="2019-12-1")
#现在网页应该能够看到,并且q1 q2可取出
>>> q2
(<Question: 问题:你打算到哪 个城市找工作？>, False) #False意思是没存进去,因为存在,只好取出来
>>> q1
<Question: 问题:散伙饭去哪吃？>

#对Choice操作

-创建选项:
1.方法一:  (创建实例的方法)
>>> c1 = Choice(choice_text='杭州',question=q2[0]) #[0]只用第一项(第二项是False)
>>> c1.save()

2.方法二:  (通过object创建)
>>> c2 = Choice.objects.get_or_create(choice_text='深圳',question=q2[0])

3.方法三:  (通过问题反推创建选项)
# 创建选项，方法三：通过问题创建选项。问题和选项有一对多关系，一个问题有多个选项。
每个问题的实例都有一个管理器，通过这个管理器可以创建选项。选项的class名叫Choice，
那么管理器就叫choice_set；如果选项的class叫XuanXiang，那么管理器叫xuanxiang_set。
>>> q2[0].choice_set.all()  #取出所有Question选项(包括刚才提交的q1)
<QuerySet [<Choice: 问题:你打算到哪 个城市找工作？=>选项:杭州>, <Choice: 问题:你打算到哪 个城市找工作？=>选项:深圳>]>
>>> c3 = q2[0].choice_set.get_or_create(choice_text='成都')
#此时你的Django管理台的Choice应该可以看到刚才插入的三条信息了
"""
"""查询
#取出所有问题,返回所有问题实例构成的列表
>>> Question.objects.all()
<QuerySet [<Question: 问题:你期待哪家公司给你发Offer?>, <Question: 问题:你是不是喜欢小美俄米?>, <Question: 问题:散伙饭去哪吃？>, <Question: 问题:你打算到哪 个城市找工作？>]>
#取出所有问题,按发布时间升序排列
>>> Question.objects.order_by('pub_date')
<QuerySet [<Question: 问题:你是不是喜欢小美俄米?>, <Question: 问题:你期待哪家公司给你发Offer?>, <Question: 问题:散伙饭去哪吃？>, <Question: 问题:你打算到哪 个城市找工作？>]>
#取出所有问题,按发布时间降序排列
>>> Question.objects.order_by('-pub_date') #前面加-号就行(Django特殊设定)
<QuerySet [<Question: 问题:你打算到哪 个城市找工作？>, <Question: 问题:散伙饭去哪吃？>, <Question: 问题:你期待哪家公司给你发Offer?>, <Question: 问题:你是不是喜欢小美俄米?>]>
>>> for q in Question.objects.order_by('-pub_date'):   #使用for循环遍历更清晰
...     print(q.pub_date, q.question_text)
... 
2019-12-01 00:00:00 你打算到哪 个城市找工作？
2019-11-25 00:00:00 散伙饭去哪吃？
2019-11-22 17:24:00 你期待哪家公司给你发Offer?
2019-11-04 00:00:00 你是不是喜欢小美俄米?
**********get 和 filter************
-get返回实例
    不存在就会报错,并且只允许1项满足要求(多一个少一个就报错)
-filter返回列表
    不存在不会报错,允许没0~多个项目符合要求
    
#通过get取出满足条件的实例,如果结果不是一项则报错(只能取一项)
>>> Question.objects.get(id=1)  #存在并且为一条,成功取出
<Question: 问题:你期待哪家公司给你发Offer?>
>>> Question.objects.get(id=10)   #不存在就报错
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/root/nsd1906/lib/python3.6/site-packages/django/db/models/manager.py", line 85, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/root/nsd1906/lib/python3.6/site-packages/django/db/models/query.py", line 380, in get
    self.model._meta.object_name
polls.models.DoesNotExist: Question matching query does not exist. 

#通过filter取出满足条件的实例列表,列表中可以是0到多项
>>> Question.objects.filter(id=10)  #不存在不会报错(返回空列表)
<QuerySet []>
>>> Question.objects.filter(id=1)  #以列表的形式展现(吧实例放进了列表里)
<QuerySet [<Question: 问题:你期待哪家公司给你发Offer?>]>
>>> Question.objects.filter(id=1)[0]  #因为是列表,加上下标就可以和get取得结果一样了
<Question: 问题:你期待哪家公司给你发Offer?>
>>> Question.objects.filter(id=10)[0]  #不存在并且还要取第一项才会报错(空列表没下标)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/root/nsd1906/lib/python3.6/site-packages/django/db/models/query.py", line 289, in __getitem__
    return list(qs)[0]
IndexError: list index out of range  #没有下标

#查询条件
#django中查询条件使用双下划线代替句点表示属性或方法
#id=1,实际上是id__exact=1的缩写
>>> Question.objects.filter(id__exact=1)
<QuerySet [<Question: 问题:你期待哪家公司给你发Offer?>]>
#id>1,是id__gt=1
>>> Question.objects.filter(id__gt=1)
<QuerySet [<Question: 问题:你是不是喜欢小美俄米?>, <Question: 问题:散伙饭去哪吃？>, <Question: 问题:你打算到哪 个城市找工作？>]>
#id<2,是id__lt=1
>>> Question.objects.filter(id__lt=2)
<QuerySet [<Question: 问题:你期待哪家公司给你发Offer?>]>
#pub_date.month==12的写法:
>>> Question.objects.filter(pub_date__month=12)
<QuerySet [<Question: 问题:你打算到哪 个城市找工作？>]>

#字符串方法举例,判断字符串是否以某些字符开头
>>> s1 = 'hello world'
>>> s1.startswith('he')
True
>>> Question.objects.filter(question_text__startswith='你')
<QuerySet [<Question: 问题:你期待哪家公司给你发Offer?>, <Question: 问题:你是不是喜欢小美俄米?>, <Question: 问题:你打算到哪 个城市找工作？>]>
"""
"""修改问题
#只要将问题实例取出,重新赋值即可
>>> q = Question.objects.get(question_text='你期待哪家公司给你发Offer?')
>>> q
<Question: 问题:你期待哪家公司给你发Offer?>
>>> q.question_text = '你心仪的公司是哪家?'
>>> q.save()
"""
"""删除
#删除,将问题实例取出,调用删除方法
>>> q = Question.objects.get(question_text='散伙饭去哪吃？')
>>> q.delete()
(1, {'polls.Choice': 0, 'polls.Question': 1})
#千万不要q.save()否则就会保存回去(如果不小心删错了就可以用save)
"""
#**********修改首页
"""#修改index首页
-修改index函数,取出所有的问题,发给模板
#polls/views.py
...
from .models import Question

# Create your views here.
def index(request):
    # 用户发起的请求将会作为第一个参数传给函数
    # 所以函数至少要定义一个参数来接收用户的请求
    questions = Question.objects.order_by('-pub_date')
    # render负责找寻模板文件发送给用户
    return render(request, 'index.html',{'questions': questions})

#修改模板
#template/index.html
# 模板文件中，变量用{{ var }}，模板语法用{% %}。在花括号外面的部分，是html语法
{# 加载static目录内容 #}
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
{#  从数据库中读取数据  #}
        <div class="h4">
{#    定义有序列表    #}
            <ol>
{#      使用for循环遍历出来      #}
                {% for question in questions %}
                    <li>
                        <a href="{% url 'detail' question.id %}" target="_blank">
{#            问题内容                #}
                            {{ question.question_text }}
                        </a>
{#           问题日期             #}
                        {{ question.pub_date }}
                    </li>
                {% endfor %}
            </ol>
        </div>
    </div>
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

"""
#************模板继承
"""
-为了使得各个页面用一致的风格,可以采用模板继承的方法
-创建一个基础模板,把共性内容写到基础摸板中.把个性内容,使用block占位
-具体的每个web页面,都基于基础板创建,把个性内容写到相应的block中
"""
"""
#基于index.html实现模板继承
(venv) [root@room9pc01 Django]# cp templates/index.html templates/basic.html
(venv) [root@room9pc01 Django]# ls templates/
basic.html  detail.html  index.html  result.html

#templates/basic.html #把个性内容block替换,共性内容保留
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
"""
"""index.html内容
{% extends 'basic.html' %}
{% load static %}
{% block title %}投票首页{% endblock %}
{% block content %}
{#  正文内容  #}
    <div>
        <h1 class="text-center text-warning">投票首页</h1>
{#  从数据库中读取数据  #}
        <div class="h4">
{#    定义有序列表    #}
            <ol>
{#      使用for循环遍历出来      #}
                {% for question in questions %}
                    <li>
                        <a href="{% url 'detail' question.id %}" target="_blank">
{#            问题内容                #}
                            {{ question.question_text }}
                        </a>
{#           问题日期             #}
                        {{ question.pub_date }}
                    </li>
                {% endfor %}
            </ol>
        </div>
{% endblock %}

"""
"""detail.html内容
{% extends 'basic.html' %}
{% load static %}
{% block title %}投票详情{% endblock %}
{% block content %}
    <div>
        <h1 class="text-center text-warning">投票详情</h1>
    </div>
<marquee><font color="purple"><h1>{{ question_id }}号问题投票详情</h1></font></marquee>
{% endblock %}
"""
"""result.html内容
{% extends 'basic.html' %}
{% load static %}
{% block title %}投票结果{% endblock %}
{% block content %}
    <div>
        <h1 class="text-center text-warning">投票结果</h1>
    </div>
<marquee><font color="purple"><h1>{{ question_id }}号问题投票结果</h1></font></marquee>
{% endblock %}
"""
"""完成投票详情页
#取出某一问题的实例,交给模板处理

通过问题取出所有的选项:
(venv) [root@room9pc01 Django]# python manage.py shell
Python 3.6.7 (default, Feb 20 2019, 15:08:07) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-36)] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from polls.models import Question
>>> q1 = Question.objects.get(id=1)
>>> q1
<Question: 问题:你心仪的公司是哪家?>
#问题实例有一个名为choice_set的选项集,他也是一个管理器,可以通过这个管理器管理该问题的选项
>>> q1.choice_set.all()
<QuerySet [<Choice: 问题:你心仪的公司是哪家?=>选项:condom>]>
>>> q1.choice_set.order_by('id')
<QuerySet [<Choice: 问题:你心仪的公司是哪家?=>选项:condom>]>


#**************polls/views.py
def detail(request, question_id):
    #在数据库中取出具体的问题
    question = Question.objects.get(id=question_id)
    # 字典的内容将会成为模板文件的变量，字典的key是变量名，val是变量值
    return render(request, 'detail.html', {'question': question})

#修改模板
#teamplates/detail.html
{% extends 'basic.html' %}
{% load static %}
{% block title %}投票详情{% endblock %}
{% block content %}
    <div>
        <h1 class="text-center text-warning">{{ question.id }}号问题投票详情</h1>
    </div>
    <h3>{{ question.question_text }}</h3>
    <div class="h4">
        <form action="" method="post">
            {#csrf_token是安全选项,必须配置#}
            {% csrf_token %}
            {% for choice in question.choice_set.all %}
                <div class="radio">
                    <label>
                        <input type="radio" name="choice_id" value="{{ choice.id }}">
                        {{ choice.choice_text }}
                    </label>
                </div>
            {% endfor %}
            <div class="form-group">
                <input class="btn btn-primary" type="submit" value="提交">
            </div>
        </form>
    </div>
{% endblock %}
"""
"""实现投票功能
-投票功能应该是执行一个函数,该函数能够把选项votes字段加1
-在django中访问某一url将会调用相关函数
-所以,要想实现投票功能,应该在detail页面中,提交表单时,提交到一个url,该url调用
 相关函数.函数用于在数据库中找到选项,把选项votes字段值加1.

#polls/urls.py
urlpatterns = [
    ... ...
    url(r'^(\d+)/vote/$', views.vote, name='vote'),
]

#polls/views.py
from django.shortcuts import render, redirect #redirect重定向
from .models import Question
...
def vote(request, question_id):
    #取出问题
    question  =Question.objects.get(id=question_id)
    #request是用户的请求,他有很多属性,客户端提交的数据,保存到了
    #request.POST字典中,choice_id是表单的属性
    choice_id = request.POST.get('choice_id')
    #通过问题取出选项实例
    choice = question.choice_set.get(id=choice_id)
    #将选项的votes属性值+1
    choice.votes += 1
    choice.save()
    #投票结束后,跳转到结果页面
    return  redirect('result', question.id)
    
#teamplates/detail.html
{% extends 'basic.html' %}
{% load static %}
{% block title %}投票详情{% endblock %}
{% block content %}
    <div>
        <h1 class="text-center text-warning">{{ question.id }}号问题投票详情</h1>
    </div>
    <h3>{{ question.question_text }}</h3>
    <div class="h4">
{#  action里写投票结vote果提交到数据库中votes中  #}
        <form action="{% url 'vote' question.id %}" method="post">
            {#csrf_token是安全选项,必须配置#}
            {% csrf_token %}
            {% for choice in question.choice_set.all %}
                <div class="radio">
                    <label>
                        <input type="radio" name="choice_id" value="{{ choice.id }}">
                        {{ choice.choice_text }}
                    </label>
                </div>
            {% endfor %}
            <div class="form-group">
                <input class="btn btn-primary" type="submit" value="提交">
            </div>
        </form>
    </div>
{% endblock %}

#改完后去网页测试投票同时看后台对应选项票数是否有增加
"""
"""完成投票结果页
#修改函数,取出问题
#polls/views.py
...
def result(request, question_id):
    question  =Question.objects.get(id=question_id)
    return render(request, 'result.html', {'question': question})

#***teamplates/result.html
{% extends 'basic.html' %}
{% load static %}
{% block title %}投票结果{% endblock %}
{% block content %}
    <h1 class="text-center text-warning">
        {{ question.id }}号问题投票结果
    </h1>
    <h2>{{ question.question_text }}</h2>
    <table class="table table-striped table-hover h4">
        <thead class="bg-primary">
            <tr>
                <th>选项</th>
                <th>票数</th>
            </tr>
        </thead>
        {% for choice in question.choice_set.all %}
            <tr>
                <td>{{ choice.choice_text }}</td>
                <td>{{ choice.votes }}</td>
            </tr>
        {% endfor %}
    </table>
    <h5>
        <a href="{% url 'index' %} ">返回首页</a>
    </h5>

{% endblock %}
#完成后到此结束
"""