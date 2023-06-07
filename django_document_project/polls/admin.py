from django.contrib import admin
from .models import Question, Choice

# 2.6 在此处注册需要显示在后台管理界面的模型
# admin.site.register(Question)

# 7.1 创建一个模型后台类再进行注册，观察 admin 怎么工作的
# 访问管理后台并查看 Question 模型，字段将会按照我们指定的顺序排序


# 7.4 将其设置为行内添加
# 前往 models.py 改进显示  > 7.5
# class ChoiceInline(admin.StackedInline):  以字段显示
class ChoiceInline(admin.TabularInline):  # 以表单显示

    extra = 3
    model = Choice

    # 7.4.1 为了实现根据是否新建来追加选项，编写一个方法
    @classmethod  # 作用于静态类而不是实例化类
    def set_extra(cls, extra=3):
        # 额外显示的行数，默认为3
        cls.extra = extra


class QuestionAdmin(admin.ModelAdmin):
    # 对字段指定显示顺序
    # fields = ["pub_date", "question_text"]

    # 7.4.1 判断是否为新建的问题来决定是否在末尾追加三个选项
    # 当获取文件集合时调用
    def get_fieldsets(self, request, obj=None):
        # 对字段进行分组
        fieldsets = [
            (None, {"fields": ["question_text"]}),
            ("Date information", {"fields": ["pub_date"]})
        ]

        self.list_display = ["question_text", "pub_date", "was_published_recently"]
        # 7.6 添加一个过滤器
        # 在侧边栏添加一个过滤器（过滤字段）
        self.list_filter = ["pub_date"]

        # 7.7 添加一个搜索框
        # 搜索哪个字段
        self.search_fields = ["question_text"]

        # 7.8 添加分页器

        # 判断改数组是否已经存在
        if obj:
            ChoiceInline.set_extra(extra=0)
            self.inlines = [ChoiceInline]
        else:
            ChoiceInline.set_extra()
            self.inlines = [ChoiceInline]

        return fieldsets


# 7.3 注册 Choice 模型观察如何显示关联对象

# 这不够便捷实用，我们将其更改为创建问题时同时添加选项  > 7.4
# admin.site.register(Choice)


admin.site.register(Question, QuestionAdmin)
