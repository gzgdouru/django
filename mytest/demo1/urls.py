from django.conf.urls import url
from .views import home, index

app_name = "demo1"

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^(?P<tvno>\d{1})/$', index, name="index"),
]