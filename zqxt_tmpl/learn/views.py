# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
    msg = "sb来了"
    return render(request, "home.html", {"message" : msg})