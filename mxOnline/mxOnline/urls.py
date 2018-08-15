"""mxOnline URL Configuration

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
from django.views.generic import TemplateView
import xadmin
from django.views.static import serve
from mxOnline.settings import MEDIA_ROOT

from .views import IndexView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    url(r'^$', IndexView.as_view(), name="index"), #首页
    url(r'^users/', include("users.urls")),  #用户url
    url(r'^org/', include("organization.urls")),    #机构url

    url(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),  #配置上传文件的访问处理函数

    #第三方处理url
    url(r'^captcha/', include('captcha.urls')),
]
