from django.conf.urls import url, include

from .views import CourseListView, CourseDetail, CourseInfoView

app_name = "course"

urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name="course_list"),
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetail.as_view(), name="course_detail"),
    url(r'^video/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="course_info"),
]