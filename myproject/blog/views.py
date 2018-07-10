# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, render_to_response
from models import BlogPost, BlogPostForm
from datetime import datetime
from django.template.context_processors import csrf

# Create your views here.
def first_page(request):
    return HttpResponse("<p>welcome to my blog</p>")

def archive(request):
    postList = BlogPost.objects.all().order_by("-timestamp")
    ctx = {}
    ctx["posts"] = postList
    return render_to_response("blogpost.html", ctx)

def create(request):
    if request.POST:
        # title = request.POST.get("title")
        # timestamp = datetime.now()
        # body = request.POST.get("body")
        #BlogPost(title=title, timestamp=timestamp, body=body).save()
        form = BlogPostForm(request.POST)
        if form.is_valid():
            BlogPost(title=form.cleaned_data["title"], timestamp=datetime.now(), body=form.cleaned_data["body"]).save()
    ctx = {}
    ctx.update(csrf(request))
    postList = BlogPost.objects.all().order_by("-timestamp")
    ctx["posts"] = postList
    form = BlogPostForm()
    ctx["form"] = form
    return render_to_response("create.html", ctx)