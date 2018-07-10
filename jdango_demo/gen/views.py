from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import GenForm, CustomForm, UploadForm
from PIL import ImageFont, Image, ImageDraw
from .public import mergepic, save_backfile
import os

# Create your views here.
def index(request):
    fileList = os.listdir("gen/static/images/")
    files = []
    for file in fileList:
        filename = os.path.basename(file)
        files.append("images/{}".format(filename))
    paginator = Paginator(files, 5)
    p = request.GET.get("p")
    try:
        files = paginator.page(p)
    except:
        files = paginator.page(1)
    return render(request, "gen/index.html", context={
        "files" : files,
    })

def gen(request):
    backfiles = os.listdir("gen/static/images")
    if request.method == "POST":
        form = GenForm(request.POST)
        if form.is_valid():
            newFile = mergepic(form.cleaned_data.get("backfile"),
                            form.cleaned_data.get("msg"),
                            int(form.cleaned_data.get("font_size")),
                            int(form.cleaned_data.get("x")),
                            int(form.cleaned_data.get("y")))
            newFile = "/images/gen/{}".format(newFile)
    else:
        form = GenForm(backfiles)
    return render(request, "gen/gen.html", context=locals())

@login_required
def vip(request):
    messages.get_messages(request)
    if "custom_backfile" in request.session and len(request.session.get("custom_backfile")) > 0:
        custom_backfile = request.session.get("custom_backfile")
    else:
        custom_backfile = None

    if request.method == "POST":
        if "change_backfile" in request.POST:
            upload_form = UploadForm(request.POST, request.FILES)
            if upload_form.is_valid():
                custom_backfile = save_backfile(request.FILES["file"])
                request.session["custom_backfile"] = "images/gen/{}".format(custom_backfile)
                messages.add_message(request, messages.INFO, "档案上传成功.")
            else:
                messages.add_message(request, messages.WARNING, "档案上传失败!")
            return redirect("/gen/vip")
        else:
            form = CustomForm(request.POST)
            if form.is_valid():
                if custom_backfile:
                    backFile = os.path.join("gen/static/", custom_backfile)
                else:
                    backFile = os.path.join("gen/static/images", "2.jpg")
                new_file = mergepic(backFile,
                                   form.cleaned_data.get("msg"),
                                   int(form.cleaned_data.get("font_size")),
                                   int(form.cleaned_data.get("x")),
                                   int(form.cleaned_data.get("y")))
                new_file = "/images/gen/{}".format(new_file)
    else:
        form = CustomForm()
        upload_form = UploadForm()
    return render(request, "gen/vip3.html", context=locals())