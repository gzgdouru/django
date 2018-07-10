"""jdango_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^mood/', include("mood_wall.urls")),
    url(r'^captcha/', include("captcha.urls")),
    url(r'^diary/', include("diary.urls")),
    url(r'^extenduser/', include("extend_user.urls")),
    url(r'^mvote/', include("mvote.urls")),
    url(r'^accounts/', include("allauth.urls")),
    url(r'^mshop/', include("mshop.urls")),
    url(r'^gen/', include("gen.urls")),
    url(r'^confession/', include("confession_wall.urls")),
]
