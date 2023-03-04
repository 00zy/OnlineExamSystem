"""
代码功能：操作数据表格，导出Excel、导入注册模型
时间：2023/3/4 20:58
作者：zx
"""
from openpyxl import Workbook  # 操作数据表格，导出Excel
from django.contrib import admin  # 所用的后台管理系统的模板
from django.http import HttpResponse  # http协议
# 导入注册模型
from .models import Student, Teacher, QuestionBank, TestPaper, Academy, Speciality, Course, Record


# 增加导出Excel功能
class ExportExcelMixin(object):
    def export_as_excel(self, request, queryset):
        meta = self.model._meta  # 用于定义文件名，格式为：app名.模型类名
        field_names = [field.name for field in meta.fields]  # 模型所有字段名

        response = HttpResponse(content_type='application/msexcel')  # 定义响应内容类型
        response['Content-Disposition'] = f'attachment; filename={meta}.xlsx'  # 定义响应数据格式
        wb = Workbook()  # 新建一个Workbook
        ws = wb.active  # 使用当前活动的sheet表
        ws.append(field_names)  # 将模型字段名作为标题写入第一行
        for obj in queryset:  # 遍历选择的对象列表
            for field in field_names:
                # 将模型属性值的文本格式组成列表
                data = [f'{getattr(obj, field)}' for field in field_names]
            ws.append(data)  # 写入模型属性值
        wb.save(response)  # 将数据存入响应内容
        return response

    export_as_excel.short_description = '导出到Excel'  # 通过wb把他生成为一个Excel表格


# 学院信息
@admin.register(Academy)
class AcademyAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    # 按照学号降序排列
    ordering = ("id",)


# 专业信息
@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ("id", "xueyuan", "zhuanye")
    ordering = ("id",)


# 课程信息
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "course_id", "course_name")
    ordering = ("id",)


# 将模型注册到admin中
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin, ExportExcelMixin):
    # 显示出来的信息
    list_display = ("sid", "name", "sex", "age", "xueyuan", "major", "sclass", "email")
    # 根据学号和姓名查找
    search_fields = ('sid', 'name')
    # 过滤器  根据下列的选项去过滤
    list_filter = ("name", "sex", "xueyuan", "major", "sclass")
    # 按照学号降序排列
    ordering = ("sid",)
    # 分页
    list_per_page = 10
    actions = ["export_as_excel", ]  # 排序功能，导入到Excel


# 教师表
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin, ExportExcelMixin):
    list_display = ("tid", "name", "sex", "xueyuan", "email")
    # 根据教职工 工号  去查找
    search_fields = ('tid', 'name')
    # 过滤器  根据教师的姓名 学院
    list_filter = ("name", "xueyuan")
    # 按照工号降序排列
    ordering = ("tid",)
    # 分页
    list_per_page = 10
    actions = ["export_as_excel", ]


# 题库表
@admin.register(QuestionBank)
class QuestionBankAdmin(admin.ModelAdmin, ExportExcelMixin):
    list_display = ("id", "zhuanye", "course", "title", "a", "b", "c", "d", "answer", "difficulty", "score")
    # 根据科目 专业去搜索
    search_fields = ("zhuanye", "course")
    # 过滤器  根据题科目的名称  以及专业的名称  题目名称
    list_filter = ("zhuanye", "course", "title")
    # 按照序号排列
    ordering = ("id",)
    list_per_page = 10
    actions = ["export_as_excel", ]


# 试卷
@admin.register(TestPaper)
class TestPaperAdmin(admin.ModelAdmin, ExportExcelMixin):
    def show_question(self, obj):
        return [exam_q.title for exam_q in obj.exam_questions.all()]

    list_display = ("id", "title", "tid", "course", "zhuanye", 'time')

    # filter_horizontal = ("exam_questions",)

    # 根据科目 专业去搜索
    search_fields = ("tid", "zhuanye", "course")
    # 过滤器  根据题科目的名称  以及专业的名称  题目名称
    list_filter = ("tid", "zhuanye", "course")
    # 按照序号排列
    list_per_page = 10
    ordering = ['id']
    actions = ["export_as_excel", ]


# 成绩表
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin, ExportExcelMixin):
    list_display = ("id", "xuehao", "course", "grade")
    # 根据科目 专业去搜索
    search_fields = ("xuehao",)
    # 过滤器  根据题科目的名称  以及专业的名称  题目名称
    list_filter = ("xuehao",)
    # 按照序号排列
    # list_per_page = 10
    # 按照成绩降序排列
    ordering = ['-grade']
    actions = ["export_as_excel", ]


# 站点名称
admin.site.site_header = '基于Django和遗传算法的智能组卷在线考试系统'

# 网页标题
admin.site.site_title = '在线考试后台管理系统'
