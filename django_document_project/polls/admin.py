from django.contrib import admin
from .models import Question

# 2.6 在此处注册需要显示在后台管理界面的模型
admin.site.register(Question)
