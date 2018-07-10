from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm
from .models import Profile

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect("/extenduser/userinfo")
    else:
        return redirect("/extenduser/login")

# def login(request):
#     if request.method == "POST":
#         loginForm = LoginForm(request.POST)
#         if loginForm.is_valid():
#             username = loginForm.cleaned_data.get("username")
#             passwd = loginForm.cleaned_data.get("passwd")
#             user = auth.authenticate(username=username, password=passwd)
#             if user:
#                 auth.login(request, user)
#                 return redirect("/extenduser")
#             else:
#                 messages.add_message(request, messages.WARNING, "登入失败!")
#         else:
#             messages.add_message(request, messages.WARNING, "请检查表单内容!")
#     else:
#         loginForm = LoginForm()
#
#     return render(request, "/extenduser/login.html", context={
#         "login_form" : loginForm
#     })

@login_required()
def userinfo(request):
    userinfo = Profile.objects.filter(user=request.user).first()
    if not userinfo: Profile(user=request.user).save()
    return render(request, "extend_user/userinfo.html", context=locals())
