from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.first_page),
    url(r'^staff/', views.staff),
    url(r'^templay/', views.templay),
    url(r'^form/', views.form),
    url(r'^investigate/', views.investigate),
]