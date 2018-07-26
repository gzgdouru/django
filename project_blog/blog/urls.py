from django.conf.urls import url
from . import views

app_name = "blog"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(\d+)/$', views.detail, name="detail"),
    url(r'^category/(\d+)/$', views.show_category_post, name="category"),
    url(r'^archive/(\d+)/(\d+)/$', views.show_archive_post, name="archive"),
    url(r'^comment/(\d+)/$', views.post_comment, name="comment"),
]