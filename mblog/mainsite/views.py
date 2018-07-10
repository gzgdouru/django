from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, "index.html", locals())

def post_detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        return render(request, "post.html", context={
            "post" : post,
        })
    except Exception as e:
         return redirect("/")