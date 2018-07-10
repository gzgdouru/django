from django.conf.urls import url
from .views import index

app_name = "demo2"

urlpatterns = [
    url(r'^$', index),
    url(r'^(?P<maker>\d+)/$', index, name="index")
]