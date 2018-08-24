from django.conf.urls import url
from django.views.decorators.cache import cache_page
from . import views
from .views import CategoryListView, CategoryDetailView, SearchView

app_name = "novel"

urlpatterns = [
    url(r'^detail/(\d+)/$', views.novel_detail, name="novel_detail"),
    url(r'^chapter/(\d+)/(\d+)/$', cache_page(60*15)(views.chapter_detail), name="chapter_detail"),
    url(r'^category/list/$', CategoryListView.as_view(), name="category_list"),
    url(r'^category/detail/(?P<category_id>\d+)/$', CategoryDetailView.as_view(), name="category_detail"),
    url(r'^search/$', SearchView.as_view(), name="search"),
]