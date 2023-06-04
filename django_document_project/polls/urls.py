from django.urls import path

from . import views

# 1.2 在 urlpatterns 中添加所需的视图映射
# 前往主目录下的 urls.py 中插入这个 app  > 1.3
urlpatterns = [
    path("", views.index, name="index"),
]
