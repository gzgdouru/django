from django.shortcuts import render, HttpResponse
from django.views.generic import View

from .models import City, CourseOrg
from .forms import UserAskForm

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
