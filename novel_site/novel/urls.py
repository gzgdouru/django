from django.conf.urls import url
from django.views.decorators.cache import cache_page
from .views import CategoryListView, CategoryDetailView, SearchView, NovelListView, \
    ChapterListView, ChapterDetailView

app_name = "novel"

urlpatterns = [
    url(r'^list/$', NovelListView.as_view(), name="novel_list"),
    url(r'^chapter/list/(?P<novel_id>\d+)/$', ChapterListView.as_view(), name="chapter_list"),
    url(r'^chapter/detail/(?P<novel_id>\d+)/(?P<chapter_id>\d+)/$', cache_page(60*15)(ChapterDetailView.as_view()), name="chapter_detail"),
    url(r'^category/list/$', CategoryListView.as_view(), name="category_list"),
    url(r'^category/detail/(?P<category_id>\d+)/$', CategoryDetailView.as_view(), name="category_detail"),
    url(r'^search/$', SearchView.as_view(), name="search"),
]