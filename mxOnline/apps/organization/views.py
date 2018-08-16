from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import View

from .models import City, CourseOrg
from .forms import UserAskForm
from operation.models import UserFavorite

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


class OrgListView(View):
    def get(self, request):
        all_city = City.objects.all()
        all_org = CourseOrg.objects.all()
        hot_org = all_org.order_by("-click_nums")[:3]

        #分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        #城市分类
        cityId = request.GET.get("city", "")
        if cityId:
            all_org = all_org.filter(city_id=int(cityId))

        #机构类别分类
        category = request.GET.get("ct", "")
        if category:
            all_org = all_org.filter(category=category)

        #排序
        sortby = request.GET.get("sort", "")
        if sortby:
            if sortby == "students":
                all_org = all_org.order_by("-students")
            elif sortby == "courses":
                all_org = all_org.order_by("-course_nums")

        p = Paginator(all_org, 5, request=request)

        orgs = p.page(page)

        org_nums = all_org.count()

        return render(request, "org-list.html", context={
            "all_city" : all_city,
            "all_org" : orgs,
            "org_nums" : org_nums,
            "city_id" : cityId,
            "category" : category,
            "hot_org" : hot_org,
            "sort" : sortby,
        })


class AddUserAskView(View):
    def post(self, request):
        userAskForm = UserAskForm(request.POST)
        if userAskForm.is_valid():
            userAskForm.save(commit=True)
            return HttpResponse('''{
            "status" : "success"
            }''', content_type="application/json")
        else:
            print(userAskForm.errors)
            # if "name" in userAskForm.errors:
            #     errMsg = "请输入正确的名字!"
            # elif "mobile" in userAskForm.errors:
            #     errMsg = "请输入正确的手机号码!"
            # elif "course_name" in userAskForm.errors:
            #     errMsg = "请输入正确的课程名!"
            # else:
            #     errMsg = "未知错误"

            return HttpResponse('''{
            "status" : "fail",
            "msg" : "输入的信息错误!"
            }''', content_type="application/json")


class OrgHomeView(View):
    def get(self, request, org_id):
        current_page = "home"
        course_org = get_object_or_404(CourseOrg, pk=org_id)
        all_course = course_org.course_set.all()[:4]
        all_teacher = course_org.teacher_set.all()[:4]

        has_fav = False
        if request.user.is_authenticated and UserFavorite.objects.filter(fav_id=course_org.id, fav_type=2):
            has_fav = True

        return render(request, "org-detail-homepage.html", context={
            "all_course" : all_course,
            "all_teacher" : all_teacher,
            "course_org" : course_org,
            "current_page" : current_page,
            "has_fav" : has_fav,
        })


class OrgCourseView(View):
    def get(self, request, org_id):
        current_page = "course"
        course_org = get_object_or_404(CourseOrg, pk=org_id)
        all_course = course_org.course_set.all()

        has_fav = False
        if request.user.is_authenticated and UserFavorite.objects.filter(fav_id=course_org.id, fav_type=2):
            has_fav = True

        return render(request, "org-detail-course.html", context={
            "all_course" : all_course,
            "course_org" : course_org,
            "current_page": current_page,
            "has_fav" : has_fav,
        })


class OrgDescView(View):
    def get(self, request, org_id):
        current_page = "desc"
        course_org = get_object_or_404(CourseOrg, pk=org_id)

        has_fav = False
        if request.user.is_authenticated and UserFavorite.objects.filter(fav_id=course_org.id, fav_type=2):
            has_fav = True

        return render(request, "org-detail-desc.html", context={
            "course_org" : course_org,
            "current_page" : current_page,
            "has_fav" : has_fav,
        })

class OrgTeacherView(View):
    def get(self, request, org_id):
        current_page = "teacher"
        course_org = get_object_or_404(CourseOrg, pk=org_id)
        all_teacher = course_org.teacher_set.all()

        has_fav = False
        if request.user.is_authenticated and UserFavorite.objects.filter(fav_id=course_org.id, fav_type=2):
            has_fav = True

        return render(request, "org-detail-teachers.html", context={
            "all_teacher" : all_teacher,
            "course_org" : course_org,
            "current_page" : current_page,
            "has_fav" : has_fav,
        })

class AddFavView(View):
    def post(self, request):
        if not request.user.is_authenticated:
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')

        fav_id = int(request.POST.get("fav_id", 0))
        fav_type = int(request.POST.get("fav_type", 0))

        fav_record = UserFavorite.objects.filter(fav_id=fav_id, fav_type=fav_type)
        if fav_record:
            fav_record.delete()
            return HttpResponse('{"status":"success", "msg":"收藏"}', content_type='application/json')
        else:
            if fav_id > 0 and fav_type > 0:
                UserFavorite(user=request.user, fav_id=fav_id, fav_type=fav_type).save()
                return HttpResponse('{"status":"success", "msg":"已收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"success", "msg":"收藏出错, 数据错误!"}', content_type='application/json')

