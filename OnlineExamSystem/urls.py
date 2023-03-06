from django.contrib import admin
from django.urls import re_path as url
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# 主路由
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('front.urls')),
    # 没有这一句无法显示上传的图片
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
