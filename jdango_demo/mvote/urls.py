from django.conf.urls import url, include
from mvote import views

app_name = "mvote"

urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^$', views.index, name="index"),
    url(r'^poll/(\d+)$', views.poll, name="poll"),
    url(r'^vote/(\d+)/(\d+)$', views.vote, name="vote"),
    url(r'^remove/(\d+)/(\d+)$', views.remove_pollitem, name="remove"),
]