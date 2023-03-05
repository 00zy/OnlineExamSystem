from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField  # 用于上传图片题目


# 学院表
class Academy(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('学院', max_length=20)

    # 修改显示的表的名字
    class Meta:
        db_table = "academy"
        # 给模型类起一个更可读的名字
        verbose_name = '学院'
        # 模型的复数形式
        verbose_name_plural = '学院信息表'

    # 作为外键显示的字段
    def __str__(self):
        return self.name


# 专业表
class Speciality(models.Model):
    id = models.AutoField('序号', primary_key=True)
    # 一对一外键
    xueyuan = models.ForeignKey(Academy, on_delete=models.CASCADE, verbose_name='学院')
    zhuanye = models.CharField('专业', max_length=30)

    # 修改显示的表的名字
    class Meta:
        db_table = "speciality"
        verbose_name = '专业'
        verbose_name_plural = '专业信息表'

    def __str__(self):
        return self.zhuanye


# 课程表
class Course(models.Model):
    id = models.AutoField('序号', primary_key=True)
    course_id = models.CharField('课程号', max_length=10)
    course_name = models.CharField('课程名称', max_length=30)

    class Meta:
        db_table = "course"
        verbose_name = '课程'
        verbose_name_plural = '课程信息表'

    def __str__(self):
        return self.course_name


# 学生表
class Student(models.Model):
    sid = models.CharField('学号', max_length=12, primary_key=True)
    name = models.CharField('姓名', max_length=20, unique=True)
    sex = models.BooleanField('性别', choices=((0, '女'), (1, '男')))
    age = models.IntegerField('年龄')
    # 一对一外键
    xueyuan = models.ForeignKey(Academy, on_delete=models.CASCADE, verbose_name='学院')
    # 一对一外键
    major = models.ForeignKey(Speciality, on_delete=models.CASCADE, verbose_name='专业')
    sclass = models.CharField('班级', max_length=20, help_text='例如: 17-03')
    email = models.EmailField('邮箱', default=None)  # 默认为空   唯一值
    pwd = models.CharField('密码', max_length=20)

    # 修改显示的表的名字
    class Meta:
        db_table = "student"
        verbose_name = '学生'
        verbose_name_plural = '学生信息表'

    def __str__(self):
        return self.sid


# 老师
class Teacher(models.Model):
    tid = models.CharField('教职工号', max_length=10, primary_key=True)
    name = models.CharField('姓名', max_length=20)
    sex = models.BooleanField('性别', choices=((0, '女'), (1, '男')))
    # 一对一外键
    xueyuan = models.ForeignKey(Academy, on_delete=models.CASCADE, verbose_name='学院')
    email = models.EmailField('邮箱', default=None)  # 默认为空   唯一值
    pwd = models.CharField('密码', max_length=20)

    # 修改显示的表的名字
    class Meta:
        db_table = "teacher"
        verbose_name = '教师'
        verbose_name_plural = '教职工信息表'

    def __str__(self):
        return self.name


# 题库表
class QuestionBank(models.Model):
    id = models.AutoField('序号', primary_key=True)
    zhuanye = models.ForeignKey(Speciality, on_delete=models.CASCADE, verbose_name='专业')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='科目')
    title = RichTextUploadingField(default='', verbose_name='题目', help_text='上传图片，图片宽度控制在800px')  # 富文本编辑器
    a = models.CharField('A选项', max_length=40)
    b = models.CharField('B选项', max_length=40)
    c = models.CharField('C选项', max_length=40)
    d = models.CharField('D选项', max_length=40)
    answer = models.CharField('答案', choices=(('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')), max_length=4)
    difficulty = models.CharField('难度', choices=(('easy', '简单'), ('middle', '中等'), ('difficult', '难')), max_length=10)
    score = models.IntegerField('分值')

    class Meta:
        db_table = "question_bank"
        verbose_name = '题库'
        verbose_name_plural = '单选题库信息表'

    def __str__(self):
        return '<%s:%s>' % (self.course, self.title)


# 试卷表
class TestPaper(models.Model):
    id = models.AutoField('序号', primary_key=True)
    title = models.CharField('题目', max_length=40, unique=True)
    pid = models.ManyToManyField(QuestionBank)
    tid = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='教师')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='科目')
    zhuanye = models.ForeignKey(Speciality, on_delete=models.CASCADE, verbose_name='试卷适合专业')
    time = models.IntegerField('考试时长', help_text='单位是分钟')
    examtime = models.DateTimeField('考试时间')

    class Meta:
        db_table = "test_paper"
        verbose_name = '试卷'
        verbose_name_plural = '试卷信息表'


# 学生成绩表
class Record(models.Model):
    id = models.AutoField('序号', primary_key=True)
    xuehao = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='学号', related_name='stu_xuehao')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='考试科目', related_name='stu_course')
    grade = models.FloatField('成绩')

    class Meta:
        db_table = "record"
        verbose_name = '学生成绩'
        verbose_name_plural = '学生成绩信息表'

    def __str__(self):
        return '<%s:%s>' % (self.xuehao, self.grade)

# 更行数据库命令（在项目终端目录下）
# python manage.py makemigrations
# python manage.py migrate

# 创建管理员账号命令（在项目终端目录下）
# python manage.py createsuperuser
