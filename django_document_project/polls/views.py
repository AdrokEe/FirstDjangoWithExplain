from django.shortcuts import render

from django.http import HttpResponse


# 1.1 新增一个 index 视图
# 创建并前往 urls.py 文件  > 1.2
def index(request):
    return HttpResponse("Hello, this is the polls index")
