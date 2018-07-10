from django.conf.urls import url
from  extend_user import views

app_name = "extend_user"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # url(r'^login/$', views.login, name="login"),
    url(r'^userinfo/$', views.userinfo, name="userinfo"),
]