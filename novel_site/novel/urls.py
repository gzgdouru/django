from django.conf.urls import url
from django.views.decorators.cache import cache_page
from . import views

app_name = "novel"

urlpatterns = [
    url(r'^(\d+)/$', views.novel_detail, name="novel_detail"),
    url(r'^(\d+)/(\d+)/$', cache_page(60*15)(views.chapter_detail), name="chapter_detail"),
]