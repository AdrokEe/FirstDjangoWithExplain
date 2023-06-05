# 不推荐这种写法，但是这也是可行的
# from django.template import loader
# from django.http import HttpResponse
# from django.http import Http404
# from django.http import HttpResponseRedirect

from django.utils import timezone
from django.urls import reverse
from django.views import generic
from django.shortcuts import HttpResponse, render, get_object_or_404, redirect

from .models import Question, Choice

from django.db.models import F

# 1.1 新增一个 index 视图
# 创建并前往 urls.py 文件  > 1.2
# def index(request):
#     return HttpResponse("Hello, this is the polls index")


# 3.1 创建视图和页面
# 3.1.5 在该目录下创建 templates 目录，然后再创建 polls 目录，创建对应的网页
# 前往 urls.py 文件  > 3.2.2
# 前往 detail3_3.html 和 index.html > 3.3

# 4.1 继续编写 detail.html 添加表单

# 3.1.1 完善 index 视图
# def index(request):
#     # 在排列的列名前加 - 表示倒序
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#
#     # 使用 loader 的写法:
#     # template = loader.get_template("polls/index.html")
#     # return HttpResponse(template.render(context, request))
#
#     return render(request, "polls/index.html", context)


# 3.1.1 显示查询的问题的编号
# def detail(request, question_id):
#
#     # 自己编写异常处理
#     # try:
#     #     question = Question.objects.filter(id=question_id).first()
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})


# 3.1.2 显示返回的问题的编号
# def results(request, question_id):
#     response = "This is the id of question resulted: %s."
#     return HttpResponse(response % question_id)

# 4.3 完善 results 函数
# 创建 results.html 页面  > 4.4
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})


# 3.1.3 显示问题的投票数
# def vote(request, question_id):
#     return HttpResponse("This is the number of voting on question: %s." % question_id)


# 4.6 使用通用视图替代上面的 index results vote 函数，降低耦合度
# 完成后回到 WhatHappen.md 开始自动化测试  > 5.1

# 4.6.1 index 视图继承自 ListView
# https://docs.djangoproject.com/zh-hans/4.2/ref/class-based-views/generic-display/#django.views.generic.list.ListView
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    # 这会将未来的问题也返回给主页
    # def get_queryset(self):
    #     return Question.objects.order_by("-pub_date")[:5]

    # 5.4.1 改进会返回未来问题的错误
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


# 4.6.2 detail 视图继承自 DetailView
# https://docs.djangoproject.com/zh-hans/4.2/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    # 5.5 为了不让用户直接通过 url 访问到未来的问题，我们需要添加一些约束
    # 回到 tests.py 测试这个问题是否还存在  > 5.6
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


# 4.6.3 results 视图继承自 DetailView
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


# 4.2 完善投票功能
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # 可以通过 request.POST["name"] 访问 POST 提交的内容，如果不存在将会抛出错误。所以请使用此类属性时进行异常处理
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoseNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        # 此处的 selected_choice.votes 为 python 在上文中获取的固定数值，这会导致一个问题
        # 如果同时有两个 POST 同时被提交，假设原本 votes = 5 ，则 votes = 6 会被保存两次而不是期望的 votes = 7
        # 为了解决这个问题我们需要把递增操作交给数据库而不是 python

        # selected_choice.votes += 1
        # selected_choice.save()

        # 使用 F() 函数会将运算交由 SQL 而非 Python 处理
        # 这个操作意味着每次执行到此处时都会从数据库中刷新这个查询，而不是使用在上文查询时就保存的这个静态对象
        # 详见: https://docs.djangoproject.com/zh-hans/4.2/ref/models/expressions/#avoiding-race-conditions-using-f
        selected_choice.votes = F("votes") + 1
        selected_choice.save()

        # 使用 HttpResponseRedirect 将会重定向至该 url
        # return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

        # 更推荐使用 shortcuts 中的方法
        # reverse 会生成该字符串： "/polls/3/results/"
        return redirect(reverse("polls:results", args=(question.id,)))
        # 继续完善 results 函数  > 4.3
