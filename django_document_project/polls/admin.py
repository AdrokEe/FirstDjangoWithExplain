from django.contrib import admin
from .models import Question, Choice

# 2.6 在此处注册需要显示在后台管理界面的模型
# admin.site.register(Question)

# 7.1 创建一个模型后台类再进行注册，观察 admin 怎么工作的
# 访问管理后台并查看 Question 模型，字段将会按照我们指定的顺序排序


class QuestionAdmin(admin.ModelAdmin):
    # 对字段指定显示顺序
    # fields = ["pub_date", "question_text"]

    # 也可以对字段进行分组
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]})
    ]


admin.site.register(Question, QuestionAdmin)

# 7.3 注册 Choice 模型观察如何显示关联对象
