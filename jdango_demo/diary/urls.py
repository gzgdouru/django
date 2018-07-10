from django.conf.urls import url
from diary import views

app_name = "diary"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^userinfo/$', views.userinfo, name="userinfo"),
    url(r'^post/$', views.posting, name="post"),
    url(r'^modify/$', views.modify_userinfo, name="modify"),
]