from django.urls import path

from . import views

# 在 urlpatterns 中添加所需的视图映射， 之后在主目录下的 urls.py 中插入这个 app
urlpatterns = [
    path("", views.index, name="index"),
]
