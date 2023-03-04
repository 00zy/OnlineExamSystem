from pathlib import Path
import os
import pymysql
pymysql.install_as_MySQLdb()
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
    # 'message'
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
    'default': {
        'toolbar': (
            ['div', 'Source', '-', 'Save', 'NewPage', 'Preview', '-', 'Templates'],
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Print', 'SpellChecker', 'Scayt'],
            ['Undo', 'Redo', '-', 'Find', 'Replace', '-', 'SelectAll', 'RemoveFormat'],
            ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField'],
            ['Bold', 'Italic', 'Underline', 'Strike', '-', 'Subscript', 'Superscript'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', 'Blockquote'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Maximize', 'ShowBlocks', '-', 'About', 'pbckcode'],
            ['Blockquote', 'CodeSnippet'],
        ),
        # 宽度自适应
        'width': 'auto',
        # 添加按钮在这里
        'toolbar_Custom': [
            ['NumberedList', 'BulletedList'],
            ['Blockquote', 'CodeSnippet'],
        ],
        # 加入代码块插件
        'extraPlugins': ','.join(['codesnippet', 'widget', 'lineutils', ]),
    },
}

# 中间件：用户发出的请求在系统中都会从中间件运行一遍。
# 也可以自定义一些中间件（自定义某些功能），比如说用户发出的请求经过一些处理后再传给服务器。
# 或者是响应用户的一些请求，交给服务器传来的数据经过一些处理后再传给用户。
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 根URL配置 主路由
ROOT_URLCONF = 'OnlineExamSystem.urls'

# 模板 前端页面
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'reception/templates')]  # 用DIRS告诉整个项目的前端页面放在哪里。
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': [
                'django.templatetags.static'  # 在模板中使用load标签加载static 标签。
            ]  # 不想每次在模板中加载静态文件都使用load加载static标签.
        },
    },
]

# WSGI_应用程序  http底层封装的一个协议。
WSGI_APPLICATION = 'OnlineExamSystem.wsgi.application'


# 数据库配置、连接.
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


# 密码验证
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


# 国际化配置
LANGUAGE_CODE = 'zh-hans'
# 遵循亚洲上海的时间 当前时间
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# 静态文件地址
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'reception', 'front')  # css和js存放的一个路径
]

# 发送邮件
# EMAIL_BACKEND = 'django.core.mail.backends.smpt.EmailBackend'

# 采用安全链接
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
# 发送邮箱的邮件
EMAIL_HOST_USER = '1605482347@qq.com'
# 授权码
EMAIL_HOST_PASSWORD = 'mplbgoywhpezibia'
# 收件人看到的发件人
EMAIL_FROM = '1605482347@qq.com'

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
