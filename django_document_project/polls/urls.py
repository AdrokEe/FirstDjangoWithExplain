from django.urls import path

from . import views

# 1.2 在 urlpatterns 中添加所需的视图映射
# 前往主目录下的 urls.py 中插入这个 app  > 1.3

# 设置命名空间
app_name = "polls"
urlpatterns = [
    # ex: /polls/
    # path("", views.index, name="index"),

    # 3.2.2 添加对应的视图

    # ex: /polls/5/
    # path("<int:question_id>/", views.detail, name="detail"),

    # ex: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),

    # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),

    # 4.5 优化匹配模式
    # 前往 views.py 优化视图  > 4.6
    path("", views.IndexView.as_view(), name="index"),
    # 继承自 generic 内的类可以使用 pk 表示为主键
    # 继承自 generic 内的类需要使用 as_view() 来返回视图对象
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
