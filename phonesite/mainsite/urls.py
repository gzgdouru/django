from django.conf.urls import url
from mainsite import views

app_name = "mainsite"

urlpatterns = [
    url(r'^detail/(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name="detail"),
]