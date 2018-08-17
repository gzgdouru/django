from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic import View
from django.contrib.auth.hashers import make_password

from .models import UserProfile, EmailVerifyRecord, Banner
from .forms import LoginForm, RegisterForm, ForgetPwdForm, ModifyPwdForm
from untis.email_send import send_register_email
from organization.models import CourseOrg
from courses.models import Course

#重写authenticate认证方法
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
            else:
                return None
        except:
            return None

# Create your views here.


#慕学在线网首页视图
class IndexView(View):
    def get(self, request):
        orgs = CourseOrg.objects.all().order_by("-click_nums")[:15]
        banners = Banner.objects.all().order_by("index")[:5]
        courses = Course.objects.all().order_by("-click_nums")[:6]

        current_page = "home"

        return render(request, "index.html", context={
            "orgs" : orgs,
            "banners" : banners,
            "current_page" : current_page,
            "courses" : courses,
        })


#用户注册视图
class RegisterView(View):
    def get(self, request):
        registerForm = RegisterForm()
        return render(request, "register.html", context={
            "register_form" : registerForm
        })

    def post(self, request):
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            userProfile = UserProfile()
            userProfile.username = request.POST.get("email")
            userProfile.email = request.POST.get("email")
            if UserProfile.objects.filter(email=userProfile.email):
                return render(request, "register.html", context={
                    "msg" : "该用户已存在",
                    "register_form" : registerForm
                })

            userProfile.password = make_password(request.POST.get("password"))
            userProfile.is_active = False

            send_register_email(userProfile.username, "register")
            userProfile.save()

            return redirect("/login/")
        else:
            return render(request, "register.html", context={
                "register_form" : registerForm
            })


#用户激活视图
class ActiveView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return HttpResponse("无效链接或者链接已失效!")
        return HttpResponse("用户激活成功, 请到登录页面进行登录.")


#用户登录视图
class LoginView(View):
    def get(self, request):
        return render(request, "login.html", context={})

    def post(self, request):
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            userName = request.POST.get("username")
            passWord = request.POST.get("password")
            user = authenticate(username=userName, password=passWord)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("/")
                else:
                    return render(request, "login.html", context={
                        "login_form": loginForm,
                        "msg" : "用户未激活"
                    })
            else:
                return render(request, "login.html", context={
                    "login_form": loginForm,
                    "msg" : "用户或密码错误!"
                })
        else:
            return render(request, "login.html", context={
                "login_form" : loginForm
            })


#忘记密码视图
class ForgetPwdView(View):
    def get(self, request):
        forgetForm = ForgetPwdForm()
        return render(request, "forgetpwd.html", context={
            "forget_form" : forgetForm
        })

    def post(self, request):
        forgetForm = ForgetPwdForm(request.POST)
        if forgetForm.is_valid():
            email = request.POST.get("email")
            if UserProfile.objects.filter(email=email):
                send_register_email(email, "forget")
                return HttpResponse("邮件已发送, 请查收!")
            else:
                return render(request, "forgetpwd.html", context={
                    "msg" : "用户不存在",
                    "forget_form" : forgetForm
                })
        else:
            return render(request, "forgetpwd.html", context={
                "forget_form" : forgetForm
            })


#重置密码视图
class ResetView(View):
    def get(self, request, active_code):
        record = EmailVerifyRecord.objects.filter(code=active_code).first()
        if record:
            email = record.email
            return render(request, "password_reset.html", context={
                "email" : email,
            })
        else:
            return HttpResponse("无效链接或者链接已失效!")


#修改密码视图
class ModifyPwdView(View):
    def post(self, request):
        modifyForm = ModifyPwdForm(request.POST)
        if modifyForm.is_valid():
            password = request.POST.get("password")
            confirmPwd = request.POST.get("password2")
            email = request.POST.get("email")
            if password != confirmPwd:
                return render(request, "password_reset.html", context={
                    "msg" : "密码不一致!"
                })
            else:
                user = UserProfile.objects.get(email=email)
                user.password = make_password(password)
                user.save()
                return redirect("/login/")
        else:
            return render(request, "password_reset.html", context={
                "modify_form" : modifyForm
            })

