from django.conf.urls import url
from gen import views

app_name = "gen"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^gen/$', views.gen, name="gen"),
    url(r'^vip/$', views.vip, name="vip"),
]