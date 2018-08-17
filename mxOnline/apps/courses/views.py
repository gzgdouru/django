from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from .models import Course
from operation.models import UserFavorite, UserCourse

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


class CourseListView(View):
    def get(self, request):
        current_page = "course"
        all_course = Course.objects.all().order_by("-add_time")
        hot_courses = all_course.order_by("-click_nums")[:3]

        sortby = request.GET.get("sort", "")
        if sortby:
            if sortby == "hot":
                all_course = all_course.order_by("-click_nums")
            elif sortby == "students":
                all_course = all_course.order_by("-students")

        #分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_course, 5, request=request)
        courses = p.page(page)

        return render(request, "course-list.html", context={
            "current_page" : current_page,
            "courses" : courses,
            "hot_courses" : hot_courses,
            "sort" : sortby,
        })


class CourseDetail(View):
    def get(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)

        #增加点击数
        course.click_nums += 1
        course.save()

        #相关课程查找
        tag = course.tag
        if tag:
            relation_courses = Course.objects.filter(tag=course.tag).exclude(id=course_id)
        else:
            relation_courses = []

        has_fav_course = False  #是否已收藏课程
        has_fav_org = False #是否已收藏课程机构
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(fav_id=course_id, fav_type=1):
                has_fav_course = True

            if UserFavorite.objects.filter(fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True

        return render(request, "course-detail.html", context={
            "course" : course,
            "relation_courses" : relation_courses,
            "has_fav_course" : has_fav_course,
            "has_fav_org"   : has_fav_org,
        })


class CourseInfoView(View):
    def get(self, request, course_id):
        #检查用户是否已登录
        if not request.user.is_authenticated:
            # 用户未登录即跳转到登录页面
           return redirect("/users/login/")

        course = get_object_or_404(Course, pk=course_id)

        #添加课程学生数和记录用户课程
        if not UserCourse.objects.filter(user=request.user, course=course):
            UserCourse(user=request.user, course=course).save()
            course.students += 1
            course.save()

        #获取该课程的同学还学过哪些课程
        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]
        relation_courses = UserCourse.objects.filter(user__id__in=user_ids).exclude(course__id=course.id)

        return render(request, "course-video.html", context={
            "course" : course,
            "relation_courses" : relation_courses,
        })

