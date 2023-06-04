# 不推荐这种写法，但是这也是可行的
# from django.template import loader
# from django.http import HttpResponse
# from django.http import Http404

from django.shortcuts import HttpResponse, render, get_object_or_404

from .models import Question

# 1.1 新增一个 index 视图
# 创建并前往 urls.py 文件  > 1.2
# def index(request):
#     return HttpResponse("Hello, this is the polls index")


# 3.1 创建视图
# 3.1.1 在该目录下创建 templates 目录，然后再创建 polls 目录，创建对应的网页
# 前往 urls.py 文件  > 3.2.2
# 前往 detail.html 和 index.html > 3.3

# 4.1 继续编写 detail.html 添加表单

def index(request):
    # 在排列的列名前加 - 表示倒序
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }

    # 使用 loader 的写法:
    # template = loader.get_template("polls/index.html")
    # return HttpResponse(template.render(context, request))

    return render(request, "polls/index.html", context)


# 显示查询的问题的编号
def detail(request, question_id):

    # 自己编写异常处理
    # try:
    #     question = Question.objects.filter(id=question_id).first()
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


# 显示返回的问题的编号
def results(request, question_id):
    response = "This is the id of question resulted: %s."
    return HttpResponse(response % question_id)


# 显示问题的投票数
def vote(request, question_id):
    return HttpResponse("This is the number of voting on question: %s." % question_id)
