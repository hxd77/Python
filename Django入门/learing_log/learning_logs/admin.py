from django.contrib import admin
from .models import Topic#.表示在admin.py所在的目录中查找models.py

admin.site.register(Topic)#让Django通过管理网站管理模型
# 在这里注册你的模型

