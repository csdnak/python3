from django.conf.urls import url
from . import views

urlpatterns = [
    # url从http://x.x.x.x/polls/后面开始匹配
    # 访问投票首页时，使用views.index函数响应
    # 为该url(http://x.x.x.x/polls/)起名为index
    url(r'^$', views.index, name='index'),
]