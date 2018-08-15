from django.conf.urls import url, include

from .views import LoginView, RegisterView, ActiveView, ForgetPwdView, ResetView, ModifyPwdView

app_name = "users"

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^active/(?P<active_code>.*)/$', ActiveView.as_view(), name="active"),
    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    url(r'^modify/$', ModifyPwdView.as_view(), name="modify_pwd"),
]
