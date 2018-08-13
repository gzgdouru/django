from django.shortcuts import render
from django.views.generic import View

from .models import City, CourseOrg

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


class OrgListView(View):
    def get(self, request):
        all_city = City.objects.all()
        all_org = CourseOrg.objects.all()
        org_nums = all_org.count()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_org, 1, request=request)

        orgs = p.page(page)

        return render(request, "org-list.html", context={
            "all_city" : all_city,
            "all_org" : orgs,
            "org_nums" : org_nums,
        })
