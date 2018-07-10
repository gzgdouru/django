# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from  django.http import  HttpResponse
from models import Character
from django.template.context_processors import csrf
from django import forms

# Create your views here.
def first_page(request):
    return HttpResponse("<p>west</p>")

def staff(request):
    staff_list = Character.objects.all()
    # staff_str = map(str, staff_list)
    # content = {"label" : " ".join(staff_str)}
    # return render(request, "templay.html", content)
    return render(request, "templay.html", {"staffs": staff_list})

def templay(request):
    content = {}
    content["label"] = "hello world"
    return render(request, "templay.html", content)

def form(request):
    return render(request, "form.html")

class CharacterForm(forms.Form):
    name = forms.CharField(max_length=200)

def investigate(request):
    # rlt = request.GET["staff"]
    # return HttpResponse(rlt)

    # ctx = {}
    # ctx.update(csrf(request))
    # if request.POST:
    #     ctx["rlt"] = request.POST["staff"]
    # return render(request, "investigate.html", ctx)

    # if request.POST:
    #     submitted = request.POST["staff"]
    #     newRecord = Character(name=submitted)
    #     newRecord.save()
    # ctx = {}
    # ctx.update(csrf(request))
    # allRecords = Character.objects.all()
    # ctx["staff"] = allRecords
    # return render(request, "investigate.html", ctx)

    if request.POST:
        recvForm = CharacterForm(request.POST)
        if recvForm.is_valid():
            submitted = recvForm.cleaned_data["name"]
            newRecord = Character(name=submitted)
            newRecord.save()
    recvForm = CharacterForm()
    ctx = {}
    ctx.update(csrf(request))
    allRecords = Character.objects.all()
    ctx["staff"] = allRecords
    ctx["form"] = recvForm
    return render(request, "investigate.html", ctx)