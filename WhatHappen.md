<h3>一、创建项目</h3>
新建项目：

```shell
> django-admin startproject django_document_project
```

<br>

完成之后将会得到这样一个文件目录：

```text
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

- 外层的 mysite/ 为项目的容器名，可以随意修改
- manage.py 为 Django 提供的命令行管理工具
- 里层的 mysite/ 为一个 Python 包，当引用内部对象时需要使用
- mysite/\_\_init__.py 是为了使 Python 将该目录定义为包的文件，之后不再复述
- mysite/settings.py 项目配置文件
- mysite/urls.py 项目 URL 声明文件
- mysite/asgi.py 作为项目运行在 ASGI 兼容的服务器上的入口
- mysite/wsgi.py 作为项目运行在 WSGI 兼容的服务器上的入口

<br>

启动项目：

```shell
> python manage.py runserver [ip:port]
```

<br>

<h3>二、新建应用</h3>
创建投票应用：

```shell
> python manage.py startapp polls
```

<br>

完成之后将会得到这样一个文件目录：

```text
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

现在来编写视图，在 polls/views.py 文件中查看接下来是如何运作的

> 前往 polls/views.py 查看1.1

<br>
<h3>三、管理界面</h3>
创建管理员账号：

```shell
> python manage.py createsuperuser
```

访问本地域名/admin/目录即可看见管理员登录界面<br>
为了在后台管理中看到我们刚刚创建的投票应用，需要编辑 polls/admin.py 文件

> 前往 polls/admin.py 查看2.6

<br>
<h3>四、实现功能</h3>
接下来回到 polls/views.py 中继续添加内容以实现投票功能

> 前往 polls/views.py 查看3.1

<br>
<h3>五、自动化测试</h3>
系统测试会自动在所有以 tests 开头的文件里寻找并执行测试代码<br>
我们之前在编写 question 模型时，查询问题是否是最近发布的方法中含有 bug ——如果问题来自未来也会返回 `True` <br>
现在来编写自动测试以发现这个问题

> 前往 polls/tests.py 查看5.1

<br>
<h3>六、管理静态文件</h3>
Django 会自动管理分发静态文件，通过 settings.py 可以进行相关配置<br>
让我们来编写一个 css 看看这是怎么运行的

> 创建并前往 polls/static/polls/style.css 查看6.1

<br>
<h3>七、自定义后台</h3>