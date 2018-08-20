from django.conf.urls import url, include

from .views import UserInfoView, ImageUploadView, UpdatePwdView
from .views import SendEmailCodeView, UpdateEmailView, MyCourseView
from .views import MyFavOrgView, MyFavCourseView, MyFavTeacherView, MyMessageView

app_name = "users"

urlpatterns = [
    url(r'^info/$', UserInfoView.as_view(), name="user_info"),
    url(r'^image/upload/$', ImageUploadView.as_view(), name="image_upload"),
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name="sendemail_code"),
    url(r'^update_email/$', UpdateEmailView.as_view(), name="update_email"),
    url(r'^my_course/$', MyCourseView.as_view(), name="my_course"),
    url(r'^my_fav/org/$', MyFavOrgView.as_view(), name="my_fav_org"),
    url(r'^my_fav/course/$', MyFavCourseView.as_view(), name="my_fav_course"),
    url(r'^my_fav/teacher/$', MyFavTeacherView.as_view(), name="my_fav_teacher"),
    url(r'^my_message/$', MyMessageView.as_view(), name="my_message"),
]
