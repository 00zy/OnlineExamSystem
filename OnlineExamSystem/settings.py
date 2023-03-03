from pathlib import Path
import os

# 在项目内部构建路径
# BASE_DIR = Path(__file__).resolve().parent.parent  原来的代码中的配置
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 对生产中使用的密钥保密，所有的Django实例之间都是唯一的，每个项目都是不一样的
SECRET_KEY = 'django-insecure-(n+6loejrpl_9xt^gj6nll&yy_8tp!lh1ilillam-n9)o9#*5z'

# 调试模式，如果项目没有部署到远程服务器，且DEBUG = True(线下模式，允许调试)，如果要发布的时候则改为False
# 降低系统的带宽，让系统更轻松一些，省去了一些不必要的调试功能
DEBUG = True

# 设置允许哪些主机可以访问我们的Django后台站点
# 如果项目上线部署到远程服务器，那就必须设置ALLOWED_HOSTS为本地的ipv4的地址
# (设置为“*”也可以，但是不安全)，否则本地是无法访问远程的Django站点
ALLOWED_HOSTS = []


# 应用程序的定义
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'simpleui',  #Django admin 美化
    'ckeditor',  # 富文本编辑器
    'ckeditor_uploader',  # 富文本编辑器上传图片模块
    'cms',  # 管理员
    'front',  # 学生和老师
]

# 媒体文件配置
# MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = ""
MEDIA_ROOT = os.path.join(BASE_DIR, "")
# 上传图片保存路径，如果没有图片存储或者使用自定义存储位置
# 那么直接写''，如果是使用Django本身的存储方式，那么你就指明一个目录用来存储即可
CKEDITOR_UPLOAD_PATH = 'images'

# 富文本编辑器ckeditor配置
CKEDITOR_CONFIGS = {
    # (1)默认配置
    # 'default': {
    #     'toolbar': 'full',  # 工具条功能
    #     'height': 300,  # 编辑器高度
    #     'width': 800,  # 编辑器宽度
    # },
    # (2)自定义配置代码块显示
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'OnlineExamSystem.urls'

# 模板 前端页面
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'OnlineExamSystem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_online_exam',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
