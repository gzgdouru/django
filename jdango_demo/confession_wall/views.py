from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Post
from .forms import ProfileForm, PostForm

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by("-created_time")
    return render(request, "confession_wall/index.html", context=locals())

@login_required
def modify_profile(request):
    messages.get_messages(request)
    if request.method == "POST":
        profile = Profile.objects.filter(user=request.user).first()
        if not profile: profile = Profile(user=request.user)
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "编辑个人简介成功.")
            return redirect("/confession/show/")
        else:
            messages.add_message(request, messages.WARNING, "编辑个人简介失败, 请检查表单内容是否正确!")
    else:
        form = ProfileForm()
    return render(request, "confession_wall/modify_profile.html", context=locals())

@login_required
def show_profile(request):
    messages.get_messages(request)
    profile = Profile.objects.filter(user=request.user).first()
    return render(request, "confession_wall/show_profile.html", context=locals())

@login_required
def post(request):
    messages.get_messages(request)
    if request.method == "POST":
        form = PostForm(request.POST, instance=Post(user=request.user))
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "告白讯息发表成功.")
            return redirect("/confession/")
        else:
            messages.add_message(request, messages.WARNING, "告白讯息发表失败, 请检查表单内容是否正确!")
    else:
        form = PostForm()
    return render(request, "confession_wall/post.html", context=locals())

@login_required
def remove_post(request, postId):
    post = get_object_or_404(Post, pk=postId)
    if post.user.id == request.user.id:
        post.delete()
        messages.add_message(request, messages.INFO, "移除记录成功")
    else:
        messages.add_message(request, messages.WARNING, "移除记录失败, 只能移除自己发表的记录!")
    return redirect("/confession/")

