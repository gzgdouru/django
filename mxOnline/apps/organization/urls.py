from django.conf.urls import url, include

from .views import OrgListView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, AddFavView

app_name = "org"

urlpatterns = [
    url(r'^list/$', OrgListView.as_view(), name="org_list"),
    url(r'^add_ask', AddUserAskView.as_view(), name="add_ask"),
    url(r'^org_home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name="org_home"),
    url(r'^org_course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name="org_course"),
    url(r'^org_desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name="org_desc"),
    url(r'^org_teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name="org_teahcer"),
    url(r'^add_fav/$', AddFavView.as_view(), name="add_fav"),
]