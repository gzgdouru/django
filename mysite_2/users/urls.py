from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.first_page),
    url(r'^login/', views.user_login),
    url(r'^logout/', views.user_logout),
]