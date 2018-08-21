from django.shortcuts import render, redirect, HttpResponse, reverse, render_to_response
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic import View
from django.contrib.auth.hashers import make_password
import json

from .models import UserProfile, EmailVerifyRecord, Banner
from .forms import LoginForm, RegisterForm, ForgetPwdForm, ModifyPwdForm
from .forms import ImageUploadForm, UserInfoForm
from untis.email_send import send_register_email
from untis.mixin_utils import LoginRequiredMixin
from organization.models import CourseOrg, Teacher
from courses.models import Course
from operation.models import UserCourse, UserFavorite, UserMessage

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

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


class IndexView(View):
    '''
    慕学在线网首页
    '''
    def get(self, request):
        orgs = CourseOrg.objects.all().order_by("-click_nums")[:15]
        banners = Banner.objects.all().order_by("index")[:5]
        courses = Course.objects.all().order_by("-click_nums")[:6]
        banner_courses = Course.objects.filter(is_banner=True)[:3]

        return render(request, "index.html", context={
            "orgs" : orgs,
            "banners" : banners,
            "courses" : courses,
            "banner_courses" : banner_courses,
        })


class RegisterView(View):
    '''
    用户注册
    '''
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

            #写入欢迎注册消息
            UserMessage(user=userProfile.id, message="欢迎注册慕学在线网", has_read=False).save()

            send_register_email(userProfile.username, "register")
            userProfile.save()

            return redirect("/login/")
        else:
            return render(request, "register.html", context={
                "register_form" : registerForm
            })



class ActiveView(View):
    '''
    激活用户
    '''
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



class LoginView(View):
    '''
    用户登录
    '''
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


class LogoutView(LoginRequiredMixin, View):
    '''
    用户登出
    '''
    def get(self, request):
        logout(request)
        return redirect(reverse("index"))


class ForgetPwdView(View):
    '''
    忘记密码
    '''
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



class ResetView(View):
    '''
    重置密码
    '''
    def get(self, request, active_code):
        record = EmailVerifyRecord.objects.filter(code=active_code).first()
        if record:
            email = record.email
            return render(request, "password_reset.html", context={
                "email" : email,
            })
        else:
            return HttpResponse("无效链接或者链接已失效!")



class ModifyPwdView(View):
    '''
    修改密码
    '''
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


class UserInfoView(LoginRequiredMixin, View):
    '''
    用户信息中心
    '''
    def get(self, request):
        return  render(request, "usercenter-info.html", context={})

    def post(self, request):
        userinfoForm = UserInfoForm(request.POST, instance=request.user)
        if userinfoForm.is_valid():
            userinfoForm.save()
            return HttpResponse('{"status":"success"}', content_type="application/json")
        else:
            return HttpResponse(json.dumps(userinfoForm.errors), content_type='application/json')


class ImageUploadView(LoginRequiredMixin, View):
    '''
    头像上传
    '''
    def post(self, request):
        imageUploadForm = ImageUploadForm(request.POST, request.FILES, instance=request.user)
        if imageUploadForm.is_valid():
            imageUploadForm.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail"}', content_type='application/json')


class UpdatePwdView(LoginRequiredMixin, View):
    '''
    个人中心修改密码
    '''
    def post(self, request):
        modifyForm = ModifyPwdForm(request.POST)
        if modifyForm.is_valid():
            password1 = request.POST.get("password")
            password2 = request.POST.get("password2")
            if password1 != password2:
                return HttpResponse('{"status":"fail", "msg":"密码不一致"}', content_type='application/json')
            else:
                user = request.user
                user.password = make_password(password1)
                user.save()
                return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse(json.dumps(modifyForm.errors))


class SendEmailCodeView(LoginRequiredMixin, View):
    '''
    发送邮箱验证码
    '''
    def get(self, request):
        email = request.GET.get("email", "")

        if not email:
            return HttpResponse('{"email":"邮箱不能为空"}', content_type="application/json")

        if UserProfile.objects.filter(email=email):
            return HttpResponse('{"email":"邮箱已存在"}', content_type="application/json")
        send_register_email(email, "update_email")
        return HttpResponse('{"status":"success"}', content_type="application/json")


class UpdateEmailView(View):
    '''
    个人邮箱修改
    '''
    def post(self, request):
        email = request.POST.get("email", "")
        code = request.POST.get("code", "")

        if EmailVerifyRecord.objects.filter(email=email, code=code, send_type="update_email"):
            request.user.email = email
            request.user.save()
            return HttpResponse('{"status":"success"}', content_type="application/json")

        return HttpResponse('{"email":"验证码错误"}', content_type="application/json")


class MyCourseView(LoginRequiredMixin, View):
    '''
    我的课程
    '''
    def get(self, request):
        all_userCourse = UserCourse.objects.filter(user=request.user)
        courses = [userCourse.course for userCourse in all_userCourse]
        return render(request, "usercenter-mycourse.html", context={
            "courses" : courses,
        })


class MyFavOrgView(LoginRequiredMixin, View):
    '''
    我的收藏 - 课程机构
    '''
    def get(self, request):
        all_favs = UserFavorite.objects.filter(user=request.user, fav_type=2)
        fav_ids = [fav.fav_id for fav in all_favs]
        course_orgs = CourseOrg.objects.filter(id__in=fav_ids)
        return render(request, "usercenter-fav-org.html", context={
            "orgs" : course_orgs,
        })


class MyFavCourseView(LoginRequiredMixin, View):
    '''
    我的收藏 - 公开课
    '''
    def get(self, request):
        all_favs = UserFavorite.objects.filter(user=request.user, fav_type=1)
        fav_ids = [fav.fav_id for fav in all_favs]
        courses = Course.objects.filter(id__in=fav_ids)
        return render(request, "usercenter-fav-course.html", context={
            "courses" : courses,
        })


class MyFavTeacherView(LoginRequiredMixin, View):
    '''
    我的收藏 - 授课讲师
    '''
    def get(self, request):
        all_favs = UserFavorite.objects.filter(user=request.user, fav_type=3)
        fav_ids = [fav.fav_id for fav in all_favs]
        teachers = Teacher.objects.filter(id__in=fav_ids)
        return render(request, "usercenter-fav-teacher.html", context={
            "teachers" : teachers,
        })


class MyMessageView(LoginRequiredMixin, View):
    '''
    我的消息
    '''
    def get(self, request):
        all_messages = UserMessage.objects.filter(user=request.user.id)

        #将用户消息设为已读
        userMessages = UserMessage.objects.filter(user=request.user.id, has_read=False)
        for userMsg in userMessages:
            userMsg.has_read = True
            userMsg.save()

        #分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_messages, 10, request=request)
        messages = p.page(page)

        return render(request, "usercenter-message.html", context={
            "messages" : messages,
        })


def page_not_found(request):
    '''
    全局404处理函数
    '''
    response = render_to_response("404.html", context={})
    response.status_code = 404
    return response


def page_error(request):
    '''
    全局500处理函数
    '''
    response = render_to_response("500.html", context={})
    response.status_code = 500
    return response
