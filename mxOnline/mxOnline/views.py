from django.shortcuts import render
from django.views.generic import View

from organization.models import CourseOrg
from users.models import Banner

class IndexView(View):
    def get(self, request):
        orgs = CourseOrg.objects.all().order_by("-click_nums")[:15]
        banners = Banner.objects.all().order_by("index")[:5]
        return render(request, "index.html", context={
            "orgs" : orgs,
            "banners" : banners,
        })
