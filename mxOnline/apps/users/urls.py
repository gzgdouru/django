from django.conf.urls import url, include

from .views import LoginView, RegisterView, ActiveView, ForgetPwdView, ResetView, ModifyPwdView

app_name = "users"

urlpatterns = []
