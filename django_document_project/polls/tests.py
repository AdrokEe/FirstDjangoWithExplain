from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

import datetime

from .models import Question


# 在终端输入 python manage.py test polls 进行测试
# 这会让 django 去寻找 polls 应用中的测试代码。目前，这回寻找到 TestCase 的子类
# 之后会创建一个数据库给测试使用
# 然后运行在这个类中寻找到的以 test 开头的测试方法

# 让我们去修改这个问题后再回来进行一次测试，查看这之间有什么区别
# 前往 models.py  > 5.2

# 5.1 问题模型测试类
class QuestionModelTests(TestCase):

    # 方法名必须以 test 开头，这样才可以被认定为测试方法
    def test_was_published_recently_with_future_question(self):
        """
        当问题发布时间为未来时，应该返回 False
        :return:
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)

        # 判断是否为同一个对象（相当于 ==）
        self.assertIs(future_question.was_published_recently(), False)

    # 5.3 添加更多测试方法

    # 5.3.1 测试判断条件一秒前是否会成立
    def test_was_published_recently_with_old_question(self):
        """
        当问题发布时间在一天外时，应该返回 False
        :return:
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    # 5.3.2 测试判断条件一秒后是否会成立
    def test_was_published_recently_with_recent_question(self):
        """
        当问题发布时间在一天内时，应该返回 True
        :return:
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


# 5.4 测试 index 视图
# 前往 views.py 改进 index 视图  > 5.4.1
# 5.4.2 编写测试

# 前往 views.py 为 DetailView 添加约束  > 5.5

# 包装创建问题的快捷函数
def create_question(question_text, days):
    """
    创建一个 Question 对象
    :param question_text:
    :param days:
    :return:
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_question(self):
        """
        当没有问题时，应该返回错误提示
        :return:
        """
        # client 用以模拟用户和视图之间的交互（相当于浏览器访问时发送的 request）
        response = self.client.get(reverse("polls:index"))

        # 判断内容是否相同（相当于 equal 函数）
        self.assertEqual(response.status_code, 200)
        # 判断 A 是否包含 B
        self.assertContains(response, "No polls are available.")
        # 判断可迭代对象的内容是否相同（例如列表）
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """
        过去的问题应该被显示
        :return:
        """
        question = create_question(question_text="Past question", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [question]
        )

    def test_future_question(self):
        """
        未来的问题不应该被显示
        :return:
        """
        create_question(question_text="Future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        """
        当过去和未来的问题同时存在时，应该只显示过去的问题
        :return:
        """
        question = create_question(question_text="Past question", days=-30)
        create_question(question_text="Future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [question]
        )

    def test_two_past_questions(self):
        """
        当存在多条过去的数据时，应该按照倒序的顺序排序显示
        :return:
        """
        question1 = create_question(question_text="Past question 1", days=-20)
        question2 = create_question(question_text="Past question 2", days=-10)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [question2, question1]
        )

# 5.6 编写测试 DetailView 视图


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        访问未来的问题应该返回 404 报错
        :return:
        """
        future_question = create_question(question_text="Future question.", days=10)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        访问过去的问题应该被正确显示
        :return:
        """
        past_question = create_question(question_text="Past question.", days=-10)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

# 测试部分至此告一段落，理论上随着开发的进程需要持续不断的编写新的测试，这是一种好的开发习惯
# 更多测试内容详见: https://docs.djangoproject.com/zh-hans/4.2/topics/testing/
# 现在回到 WhatHappen.md 查看静态文件管理内容
