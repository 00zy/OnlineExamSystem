"""
ASGI config for OnlineExamSystem project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""
# 封装http、https底层的通信协议，可以通过链接访问  wsgi.py
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OnlineExamSystem.settings')

application = get_asgi_application()