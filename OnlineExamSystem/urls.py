from django.contrib import admin
from django.urls import path

# 主路由：整个项目的启动路径
urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^ckeditor/', include('ckeditor_uploader.urls')),  # 导入图片操作
    # path('', include('front.urls')),  # 包含了整个项目的路由
    # 没有这一句无法显示上传的图片
]  # + static(setting.MEDIA_URL, document_root=settings.MEDIA_ROOT)
