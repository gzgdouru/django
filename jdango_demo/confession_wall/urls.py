from django.conf.urls import url
from confession_wall import views

app_name = "confession"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^modify/$', views.modify_profile, name="modify"),
    url(r'^show/$', views.show_profile, name="show"),
    url(r'^post/$', views.post, name="post"),
    url(r'^remove/(\d+)/$', views.remove_post, name="remove"),
]