from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as AuthUser
from .forms import LoginForm, DiaryForm, UserInfoForm
from .models import User, Diary, UserInfo
import json

# Create your views here.
@login_required
def index(request):
    # if "username" in request.COOKIES and "usercolor" in request.COOKIES:
    #     username = json.loads(request.COOKIES.get("username"))
    #     usercolor = json.loads(request.COOKIES.get("usercolor"))

    # if "username" in request.session:
    messages.get_messages(request)
    if request.user.is_authenticated:
        username = request.user.username
        user = AuthUser.objects.filter(username=username).first()
        diaries = Diary.objects.filter(user=user)
        # useremail = request.session.get("useremail")
    return render(request, "diary/index.html", context=locals())

# def login(request):
#     if request.method == "POST":
#         loginForm = LoginForm(request.POST)
#         if loginForm.is_valid():
#             # rep = redirect("/diary")
#             # username = loginForm.cleaned_data.get("username")
#             # usercolor = loginForm.cleaned_data.get("usercolor")
#             # rep.set_cookie("username", json.dumps(username))
#             # rep.set_cookie("usercolor", json.dumps(usercolor))
#             loginName = loginForm.cleaned_data.get("username")
#             loginPass = loginForm.cleaned_data.get("passwd")
#
#             # user = User.objects.filter(name=loginName).first()
#             user = auth.authenticate(username=loginName, password=loginPass)
#             if user is not None:
#                 # if user.passwd == loginPass:
#                 if user.is_active:
#                     auth.login(request, user)
#                     messages.add_message(request, messages.INFO, "登入成功")
#                     # request.session["username"] = user.name
#                     # request.session["useremail"] = user.email
#                     return redirect("/diary")
#                 else:
#                     # messages.add_message(request, messages.WARNING, "密码错误")
#                     messages.add_message(request, messages.WARNING, "账号尚未启用")
#             else:
#                 # messages.add_message(request, messages.WARNING, "用户不存在")
#                 messages.add_message(request, messages.WARNING, "登入失败")
#         else:
#             messages.add_message(request, messages.INFO, "请检查输入的内容")
#     else:
#         loginForm = LoginForm()
#
#     return render(request, "diary/login.html", context={
#         "login_form" : loginForm,
#         # "messages" : messages.get_messages(request),
#     })

# def logout(request):
#     # response = redirect("/diary")
#     # response.delete_cookie("username")
#     # return response
#
#     # if "username" in request.session:
#     #     del request.session["username"]
#
#     auth.logout(request)
#     messages.add_message(request, messages.INFO, "登出成功")
#     return redirect("/diary")

@login_required
def userinfo(request):
    # if "username" in request.session:
    #     username = request.session.get("username")
    # else:
    # return redirect("/diary/login")
    # userinfo = User.objects.filter(name=username).first()

    messages.get_messages(request)
    userinfo = UserInfo.objects.filter(user=request.user).first()
    return render(request, "diary/userinfo.html", context=locals())

@login_required
def modify_userinfo(request):
    messages.get_messages(request)
    userinfo = UserInfo.objects.filter(user=request.user).first()
    if not userinfo:  userinfo = UserInfo(user=request.user)
    if request.method == "POST":
        userinfoForm = UserInfoForm(request.POST, instance=userinfo)
        if userinfoForm.is_valid():
            messages.add_message(request, messages.INFO, "修改个人资料成功")
            userinfoForm.save()
            return redirect("/diary/userinfo/")
    else:
        userinfoForm = UserInfoForm(instance=userinfo)
    return render(request, "diary/modify_userinfo.html", context={
        "userinfo_form": userinfoForm,
    })

@login_required
def posting(request):
    messages.get_messages(request)
    if request.method == "POST":
        diaryForm = DiaryForm(request.POST, instance=Diary(user=request.user))
        if diaryForm.is_valid():
            ddate = diaryForm.cleaned_data.get("ddate")
            tmpDate = Diary.objects.filter(user=request.user, ddate=ddate)
            if not tmpDate:
                messages.add_message(request, messages.INFO, "日记保存成功")
                diaryForm.save()
                return redirect("/diary")
            else:
                messages.add_message(request, messages.WARNING, "已有[{}]的日记".format(ddate.strftime("%Y-%m-%d")))
        else:
            messages.add_message(request, messages.WARNING, "请检查表单内容")
    else:
        diaryForm = DiaryForm()

    return render(request, "diary/posting.html", context={
        "form" : diaryForm,
        "username" : request.user.username,
    })
