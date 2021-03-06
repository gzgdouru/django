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
from mxOnline.settings import MEDIA_ROOT, STATIC_ROOT

from users.views import LoginView, RegisterView, ActiveView, ForgetPwdView, ResetView, \
    ModifyPwdView, IndexView, LogoutView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    url(r'^$', IndexView.as_view(), name="index"), #首页
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^active/(?P<active_code>.*)/$', ActiveView.as_view(), name="active"),
    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    url(r'^modify/$', ModifyPwdView.as_view(), name="modify_pwd"),

    #课程机构相关url配置
    url(r'^org/', include("organization.urls")),

    #公开课相关url配置
    url(r'^course/', include("courses.urls")),

    #用户个人中心url配置
    url(r'^users/', include("users.urls")),

    #配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),

    # url(r'^static/(?P<path>.*)$', serve, {"document_root":STATIC_ROOT}),

    #第三方处理url
    url(r'^captcha/', include('captcha.urls')),
]

#配置全局页面错误处理函数
handler404 = "users.views.page_not_found"
handler500 = "users.views.page_error"