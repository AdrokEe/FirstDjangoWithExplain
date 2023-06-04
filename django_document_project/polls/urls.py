from django.urls import path

from . import views

# 1.2 在 urlpatterns 中添加所需的视图映射
# 前往主目录下的 urls.py 中插入这个 app  > 1.3

# 设置命名空间
app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),

    # 3.2.2 添加对应的视图

    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),

    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),

    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
