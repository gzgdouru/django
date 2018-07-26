from django.conf.urls import url
from . import views

app_name = "novel"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(\d+)/$', views.novel_detail, name="novel_detail"),
    url(r'^(\d+)/(\d+)/$', views.chapter_detail, name="chapter_detail"),
]