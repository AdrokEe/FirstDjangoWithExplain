import datetime

from django.db import models
from django.utils import timezone


# 2.3 建立两个模型 Question 和 Choice
# 在 settings.py 中添加此应用以激活模型  > 2.4

# 每个类都是 django.db.models.Model 类的子类
# 详见：https://docs.djangoproject.com/zh-hans/4.2/ref/models/instances/#django.db.models.Model

# 每个字段都是 Field 类的示例
# 详见：https://docs.djangoproject.com/zh-hans/4.2/ref/models/fields/#django.db.models.Field

# 属性：问题的内容和发布时间
class Question(models.Model):
    # 如果未指定主键，将会自动生成名为 id 的主键
    # 如果未指定字段名，将会自动生成'模型名_变量名'的字段名
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField(verbose_name="date published")

    # 修改当访问该对象时返回的内容以便之后在命令台查看（此类方法为 Python 中所有类都可以重写的魔术方法）
    def __str__(self):
        return self.question_text

    # 创建一个自定义方法，判断该问题发表时间是否在一天之内
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# 属性：选项内容和选项票数
class Choice(models.Model):
    # 如果未指定外键的字段名，将会生成'变量名_id'的字段名
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
