from django.conf.urls import url, include

from .views import UserInfoView, ImageUploadView, UpdatePwdView

app_name = "users"

urlpatterns = [
    url(r'^info/$', UserInfoView.as_view(), name="user_info"),
    url(r'^image/upload/$', ImageUploadView.as_view(), name="image_upload"),
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),
]
