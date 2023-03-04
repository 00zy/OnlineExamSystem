"""
代码功能：主要是业务逻辑的实现，包括学生和老师的登录、学生和老师的退出、学生考试、计算考试成绩、教师查看成绩、查看学生和老师的个人信息
时间：2023/3/4 11:18
作者：zx
"""
from django.shortcuts import render, redirect, reverse

# from cms import models

# 首页
from cms.migrations import models


def index(request):
    return render(request, 'stu/index.html')


# 学生登录
def studentLogin(request):
    if request.method == 'POST':  # 判断他是一个post请求
        # 获取表单信息
        sid = request.POST.get('id')
        password = request.POST.get('password')
        # print("id", sid, "password", password)
        # 通过学号获取该学生实体
        try:
            student = models.Student.objects.get(sid=sid)
            # 从cms目录下的models中找到Student表然后objects(操作)get(获得)id，然后where sid=sid进行比较，从数据库中找到对应的学生信息
        except:
            return render(request, 'stu/index.html', {'message': '账号密码不正确'})
            # 若是在表中查找不到，则在index页面反馈一个message信息。
        if password == student.pwd:
            # 查询考试成绩
            paper = models.TestPaper.objects.filter(zhuanye=student.major)
            # 查询成绩信息
            grade = models.Record.objects.filter(xuehao=student.sid)
            # 渲染index模板，把数据传到前端页面
            return render(request, 'stu/index.html', {'student': student, 'paper': paper, 'grade': grade})
        else:
            return render(request, 'stu/index.html', {'message': '密码不正确！'})


# 老师登录
def teacherLogin(request):
    if request.method == 'POST':
        tid = request.POST.get('id')
        password = request.POST.get('password')
        try:
            teacher = models.Teacher.objects.get(tid=tid)
        except:
            return render(request, 'stu/index.html', {'message': '账号或密码不正确'})
        if password == teacher.pwd:  # 登录成功
            # 保存老师的信息到session
            tea = models.Teacher.objects.filter(tid=tid).values('tid').first()  # first()是查询数据库中满足条件的第一个
            request.session['tea'] = tea
            # 实现试卷统计功能
            # 在试卷列表中找到该老师发布的试题
            paper = models.TestPaper.objects.filter(tid=teacher.tid).all()  # .all()是在数据库中查询所有满足tid=teacher.tid的行数。
            return render(request, 'tea/teacher.html', {'teacher': teacher, 'paper': paper})
        else:
            return render(request, 'stu/index.html', {'message': '密码不正确'})


# 学生退出登录
def stulogout(request):
    url = reverse('front:index')
    return redirect(url)


# 老师退出登录
def tealogout(request):
    url = reverse('front:index')
    request.session.clear()
    return redirect(url)


# 教师查看成绩
def showGrade(request):
    subject1 = request.GET.get('subject') # subject点击查看试卷详情后，传递给后台一个subject(哪个科目)
    grade = models.Record.objects.filter(course__course__name=subject1)
    # 分数段的统计
    data1 = models.Record.objects.filter(course__course__name=subject1, grade__lt=60).count() # grade__lt低于60分
    data2 = models.Record.objects.filter(course__course_name=subject1, grade__gte=60, grade__lt=70).count()
    data3 = models.Record.objects.filter(course__course_name=subject1, grade__gte=70, grade__lt=80).count()
    data4 = models.Record.objects.filter(course__course_name=subject1, grade__gte=80, grade__lt=90).count()
    data5 = models.Record.objects.filter(course__course_name=subject1, grade__gte=90).count()
    # data字典，并且传给前端页面
    data = {'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5}
    return render(request, 'tea/showGrade.html', {'grade': grade, 'data': data, 'subject': subject1})


# 开始考试
def startExam(request):
    sid = request.GET.get('sid')
    title = request.GET.get('title')  # 试卷名字唯一的
    subject1 = request.GET.get('subject')  # 考试科目
    print("subject1:", subject1)
    # 拿到学生信息
    student = models.Student.objects.get(sid=sid)
    # 试卷信息
    paper = models.TestPaper.objects.filter(title=title, course__coure__name=subject1)
    print(paper.all())
    exam_time = paper[0].time
    # 封装了context字典
    context = {
        'student': student,
        'paper': paper,
        'title': title,
        'subject': subject1,
        'count': paper.count(),  # 数据表中数据的条数
        'exam_time': exam_time * 60  # 考试的时间
    }
    print(paper.count())
    return render(request, 'stu/exam.html', context=context)


# 计算考试成绩
def calculateGrade(request):
    if request.method == 'POST':
        sid = request.POST.get('sid')
        subject1 = request.POST.get('subject')
        student = models.Student.objects.get(sid=sid)
        paper = models.TestPaper.objects.filter(zhuanye=student.major)
        course = models.Course.objects.filter(course_name=subject1).first()  # filter和get的功能一样，但是filter的后缀多。
        # print(course.id)
        # 计算考试成绩
        questions = models.TestPaper.objects. \
            filter(course__course_name=subject1).values('pid').values('pid__id', 'pid__answer', 'pid__score')
        stu_grade = 0  # 初始化一个成绩
        for p in questions:
            qid = str(p['pid__id'])
            stu_ans = request.POST.get(qid)
            cor_ans = p['pid__answer']
            if stu_ans == cor_ans:
                stu_grade += p['pid__score']
        print("stu_grade:", stu_grade)
        models.Record.objects.create(xuehao_id=sid, course_id=course.id, grade=stu_grade)
        grade = models.Record.objects.filter(xuehao_id=student.sid)
        print(len(grade))
        context = {
            'student': student,
            'paper': paper,
            'grade': grade
        }
        return render(request, 'stu/index.html', context=context)
