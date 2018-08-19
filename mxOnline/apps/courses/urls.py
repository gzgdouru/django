from django.conf.urls import url, include

from .views import CourseListView, CourseDetail, CourseInfoView, CourseCommentsView, AddCommentView, CoursePlayView

app_name = "course"

urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name="course_list"),
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetail.as_view(), name="course_detail"),
    url(r'^video/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="course_info"),
    url(r'^comment/(?P<course_id>\d+)/$', CourseCommentsView.as_view(), name="course_comment"),
    url(r'^add_comment/$', AddCommentView.as_view(), name="add_comment"),
    url(r'^play/(?P<video_id>\d+)/$', CoursePlayView.as_view(), name="video_play"),
]