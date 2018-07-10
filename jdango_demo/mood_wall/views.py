from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.core.mail import send_mail
from .models import Mood, Post
from .forms import ContactForm, PostForm

# Create your views here.
# def index(request):
#     return render(request, "mood_wall/index.html", context={})

class IndexView(ListView):
    model = Post
    template_name = "mood_wall/index.html"
    context_object_name = "posts"
    ordering = ["-pub_time"]

    def get_queryset(self):
        return super(IndexView, self).get_queryset().filter(enabled=True)

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(IndexView, self).get_context_data(**kwargs)
    #     posts = Post.objects.filter(enabled=True)
    #
    #     context.update({
    #         "posts" : posts,
    #     })
    #     return context

def postDetail(request):
    moods = Mood.objects.all()
    message = None

    if request.method == "POST":
        try:
            userPost = request.POST["user_post"]
            userId = request.POST["user_id"]
            userPass = request.POST["user_pass"]
            userMood = request.POST["mood"]
        except Exception:
            message = "如要粘贴信息, 则每一栏信息都要填写..."
        else:
            mood = Mood.objects.get(status=userMood)
            post = Post.objects.create(mood=mood, nickname=userId, del_pass=userPass, message=userPost)
            post.save()
            message = "成功储存! 请谨记你的编辑密码[{}]! 讯息需经审查后才会显示.".format(userPass)

    return render(request, "mood_wall/post.html", context={
        "moods": moods,
        "message" : message,
    })

def postDelete(request, id, passwd):
    post = get_object_or_404(Post, pk=id)
    if post.del_pass != passwd:
        message = "密码错误!"
    else:
        post.delete()
        message = "删除成功!"

    posts = Post.objects.filter(enabled=True)
    moods = Mood.objects.all()

    return render(request, "mood_wall/index.html", context={
        "posts" : posts,
        "moods" : moods,
        "message" : message,
    })

def Contact(request):
    message = None
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            message = "感谢你的来信"
            user_name = form.cleaned_data.get("user_name")
            user_city = form.cleaned_data.get("user_city")
            user_school = form.cleaned_data.get("user_school")
            user_email = form.cleaned_data.get("user_email")
            user_message = form.cleaned_data.get("user_message")

            mailBody = '''
            网友姓名:{name}
            居住城市:{city}
            是否在学:{in_school}
            反映意见:{message}
            '''.format(name=user_name, city=user_city, in_school=user_school, message=user_message)
            send_mail("来自[不吐不快]网站的网友意见", mailBody, "18719091650@163.com", ["gzgdouru@163.com"])
        else:
            message = "请检查您输入的资料是否正确!"
    else:
        form = ContactForm()
    return render(request, "mood_wall/contact.html", context=locals())

def post2db(request):
    message = None
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # mood = form.cleaned_data.get("mood")
            # nickname = form.cleaned_data.get("nickname")
            # userMsg = form.cleaned_data.get("message")
            # userPass = form.cleaned_data.get("del_pass")
            # post = Post.objects.create(mood=mood, nickname=nickname, message=userMsg, del_pass=userPass)
            # post.save()
            post = form.save(commit=False)
            if post.del_pass: post.enabled = True
            post.save()
            message = "成功储存! 请谨记你的编辑密码[{}]! 讯息需经审查后才会显示.".format(post.del_pass)
        else:
            message = "请检查您输入的资料是否正确!"
    else:
        form = PostForm()
    return render(request, "mood_wall/post2db.html", context={
        "form" : form,
        "message" : message,
    })