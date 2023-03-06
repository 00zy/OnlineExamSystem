from django.urls import path
from . import views

app_name = 'front'

urlpatterns = [
    path('', views.index, name='index'),
    path('stulogout/', views.stulogout, name='stulogout'),  # 学生退出登录
    path('tealogout/', views.tealogout, name='tealogout'),  # 学生退出登录
    path('studentLogin/', views.studentLogin, name='studentLogin'),  # 学生登录
    path('teacherLogin/', views.teacherLogin, name='teacherLogin'),  # 老师登录
    path('startExam/', views.startExam, name='startExam'),  # 开始考试
    path('calculateGrade/', views.calculateGrade, name='calculateGrade'),  # 交卷计算成绩
    path('showGrade/', views.showGrade, name='showGrade'),  # 成绩统计
]
