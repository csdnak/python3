from django.contrib import admin
#导入模块
from .models import HostGroup, Host, Module, Args

# Register your models here.
for item in [HostGroup, Host, Module, Args]:
    # 循环注册
    admin.site.register(item)