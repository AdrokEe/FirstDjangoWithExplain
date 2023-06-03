<h3>创建项目</h3>
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

<h3>新建应用</h3>
创建应用：

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

现在编写视图，在 polls/views.py 文件中查看接下来是如何运作的