from django.shortcuts import render, HttpResponse
from datetime import datetime

# Create your views here.
def home(request):
    return HttpResponse("welcome")

def index(request, tvno='0'):
    tvList = [
        {"name" : "东森", "tvcode" : "dongsen"},
        {"name" : "民视", "tvcode" : "minshi"},
        {"name" : "台视", "tvcode" : "taishi"},
        {"name" : "华视", "tvcode" : "huashi"},
    ]

    tv = tvList[int(tvno)]
    # now = datetime.now()

    return render(request, "demo1/index.html", locals())