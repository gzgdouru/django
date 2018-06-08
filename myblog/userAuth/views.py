from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegisterForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            user_list = User.objects.filter(email=email)
            if user_list is None:
                form.save()
                return render(request, "userAuth/register_done.html", context={})
            else:
                form.errors["email"] = "该邮箱已经注册过了!"
    else:
        form = RegisterForm()

    return render(request, "userAuth/register.html", context={
        "form" : form
    })

