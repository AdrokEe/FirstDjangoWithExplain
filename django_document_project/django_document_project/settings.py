"""
Django settings for django_document_project project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 一串用以生成各种于安全验证有关的种子
# 注意：部署时请务必隐藏此数值于任何可在外部访问到的地方
SECRET_KEY = os.environ.get('DJANGO_SECRT_KEY', 'django-insecure-=g&li8&!0to&*3)tp54*-t&9-ig=u2vketmx4+f6e*mw7#=m&^')
# os.environ.get() 将会从系统变量中获取这个键所对应的值，未获取则返回第二个字符串

# SECURITY WARNING: don't run with debug turned on in production!
# 是否显示报错信息
# 注意：部署时请务必关闭显示报错信息
DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))

ALLOWED_HOSTS = []


# Application definition

# 2.1 查看并编辑所需要的配置文件，前往 TIME_ZONE 选项修改时区  > 2.1.1
# 2.2.1 （可选）在DATABASES 中配置数据库配置，修改为 MySQL 数据库（默认为SQLite）
# 2.2.2 一些应用需要在数据库中创建表，因此请执行 python manage.py migrate 以创建数据表
# 前往 polls/models.py 编写应用中需要使用的模型  > 2.3

# 2.4 在此处添加应用
# 之后执行 python manage.py makemigrations polls 迁移修改过的模型文件
# 在 polls/migrations/0001_initial.py 中可以阅读到迁移数据
# 执行 python manage.py sqlmigrate polls 0001 可以查看对应的 SQL 语句
# 此时并没有真正修改数据表，再次执行 python manage.py migrate 以应用数据表迁移

# 之后所有涉及对数据表的改动都依照以下步骤进行不再复述：
# 编辑 models.py 文件，改变模型
# 运行 python manage.py makemigrations [app_name] 生成迁移文件
# 运行 python manage.py migrate 应用迁移

# 2.5 执行 python manage.py shell 使用命令行练习常用方法

# from polls.models import Choice, Question  导入模型
# from django.utils import timezone  导入时间库
# q = Question(question_text="This is a new", pub_date=timezone.now())  新建一条数据，时间为现在
# q.save()  保存该对象
# q.id  查看 id （我们并编写创建这个属性，这是 django 自动在数据表中生成的主键）
# q.question_text  查看内容
# q.pub_date  查看时间
# Question.objects.filter(id=1)  查询 id 为 1 的字段 filter 会返回对象的内容
# Question.objects.filter(question_text__startswith="This")  查询内容以 This 开头的字段（django 中条件查询都以"字段名__条件名"做为属性查询）
# current_year = timezone.now().year  创建一个时间对象，年份为今年
# Question.objects.get(pub_date__year=current_year)  get 方法会返回该对象本身，属性与 filter 类似
# q = Question.objects.get(pk=1)  查询主键为 1 的字段赋值给q（pk 属性用于查询主键，主键的名称不会影响查询）
# q.choice_set.create(choice_text="A choice", votes=0)  创建一个选项
# c = q.choice_set.all()  查询该对象对应的 choice （在一对多关系中，一对象的"字段名_set"属性可以访问到多对象）
# c.question  一对多关系中，多对象可以直接通过属性名访问到一对象
# Choice.objects.filter(question__pub_date__year=current_year)  一对多关系查询时，直接使用“外键模型名__外键属性名”即可访问一对象
# c = q.choice_set.filter(choice_text__startswith="A").first()
# c.delete()  删除字段

# 更多双下划线查询方法详见：https://docs.djangoproject.com/zh-hans/4.2/topics/db/queries/#field-lookups-intro
# 接下来回到 WhatHappen.md 创建管理页面

# 这个配置项中包含了项目中启用的应用
INSTALLED_APPS = [

    # 管理员站点
    'django.contrib.admin',

    # 认证授权系统
    'django.contrib.auth',

    # 内容类型框架
    'django.contrib.contenttypes',

    # 会话框架
    'django.contrib.sessions',

    # 消息框架
    'django.contrib.messages',

    # 管理静态文件的框架
    'django.contrib.staticfiles',

    # 2.4 新增的投票应用
    'polls.apps.PollsConfig',
]

# 这个配置项中为项目启用的中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_document_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_document_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# 默认数据库配置为创建时自动新建的 sqlite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 2.2.1 （可选）配置为 MySQL 数据库

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.environ.get('DJANGO_MYSQL_DATABASE', 'django_document_project'),
#         'USER': os.environ.get('DJANGO_MYSQL_USER', 'root'),
#         'PASSWORD': os.environ.get('DJANGO_MYSQL_PASSWORD', 'root'),
#         'HOST': os.environ.get('DJANGO_MYSQL_HOST', 'localhost'),
#         'PORT': int(os.environ.get('DJANGO_MYSQL_PORT', '3306')),
#         'OPTIONS': {'charset': 'utf8mb4'},
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# 语言
LANGUAGE_CODE = 'zh-hans'

# 2.1.1 修改时区为本地时区
# 时区
TIME_ZONE = 'Asia/Shanghai'

# 是否启用翻译系统，不开启则无视语言选项只显示英语
# 作用于 django 创建的页面
USE_I18N = True

# 2.1.1 修改时区之后需要将此属性改为 False 否则仍然是 UTC 时区
# 是否根据 TIME_ZONE 中的时区读写数据库中的时间信息
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
