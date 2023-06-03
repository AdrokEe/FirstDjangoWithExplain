from django.shortcuts import render

from django.http import HttpResponse


# 新增一个 index 视图， 创建 urls.py 文件映射它
def index(request):
    return HttpResponse("Hello, this is the polls index")
