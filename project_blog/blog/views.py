from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Post, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def index(request):
    allPost = Post.objects.all()
    paginator = Paginator(allPost, 10)

    p = request.GET.get("p")
    try:
        posts = paginator.page(p)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "blog/index.html", context={
        "posts" : posts,
    })

def detail(request, postId):
    post = get_object_or_404(Post, pk=postId)
    post.increase_views()
    all_comment = Comment.objects.filter(post=post).order_by("-created_time")
    paginator = Paginator(all_comment, 10)

    p = request.GET.get("p")
    try:
        comments = paginator.page(p)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    try:
        last_post = Post.objects.get(id=(int(postId)-1))
    except:
        last_post = None

    try:
        next_post = Post.objects.get(id=(int(postId)+1))
    except:
        next_post = None

    return render(request, "blog/post.html", context={
        "post" : post,
        "comments" : comments,
        "last_post" : last_post,
        "next_post" : next_post,
    })

def show_category_post(request, categoryId):
    # category = get_object_or_404(Category, categoryId)
    posts = Post.objects.filter(category__id=categoryId)
    return render(request, "blog/index.html", context=locals())

def show_archive_post(request, year, month):
    posts = Post.objects.filter(created_time__year=year, created_time__month=month)
    return render(request, "blog/index.html", context=locals())

def post_comment(request, postId):
    post = get_object_or_404(Post, pk=postId)
    if request.method == "POST":
        content = request.POST.get("content")
        Comment.objects.create(user=request.user, post=post, content=content)
        return redirect(post)
    comments = Comment.objects.filter(post=post).order_by("-created_time")
    return render(request, "blog/post.html", context={
        "post" : post,
        "comments" : comments,
    })
