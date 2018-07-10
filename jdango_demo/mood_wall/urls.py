from django.conf.urls import url
from mood_wall import views

app_name = "mood_wall"

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^post/$', views.postDetail, name="post"),
    url(r'^delete/(?P<id>\d+)/(?P<passwd>\w+)/$', views.postDelete, name="delete"),
    url(r'^contact/$', views.Contact, name="contact"),
    url(r"^post2db/$", views.post2db, name="post2db"),
]