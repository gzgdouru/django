# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.contrib.auth import *
from  django.http import  HttpResponse
from django import forms

# Create your views here.
def first_page(request):
    return HttpResponse("<p>users</p>")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

def user_login(request):
    # if request.POST:
    #     username = password = ""
    #     username = request.POST.get("username")
    #     password = request.POST.get("password")
    #     user = authenticate(username=username, password=password)
    #     if not user and user.is_active:
    #         login(request, user)
    #         return redirect("/")
    # ctx = {}
    # ctx.update(csrf(request))
    # return render(request, "login.html", ctx)

    if request.POST:
        recvForm = LoginForm(request.POST)
        if recvForm.is_valid():
            username = recvForm.cleaned_data["username"]
            password = recvForm.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if not user and user.is_active:
                #login(request, user)
                return redirect("/")
    recvForm = LoginForm()
    ctx = {}
    ctx.update(csrf(request))
    ctx["form"] = recvForm
    return render(request, "login.html", ctx)

def user_logout(request):
    logout(request)
    return redirect("/")