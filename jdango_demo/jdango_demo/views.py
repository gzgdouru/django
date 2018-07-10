from django.shortcuts import render
from django.contrib import messages

def index(request):
    messages.get_messages(request)
    return render(request, "index.html", context={})