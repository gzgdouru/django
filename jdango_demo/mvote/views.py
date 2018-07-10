from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Poll, PollItem, VoteChech
from datetime import datetime

# Create your views here.
def index(request):
    all_polls = Poll.objects.all().order_by("-created_at")
    paginator = Paginator(all_polls, 5)
    p = request.GET.get("p")
    try:
        polls = paginator.page(p)
    except PageNotAnInteger:
        polls = paginator.page(1)
    except EmptyPage:
        polls = paginator.page(paginator.num_pages)

    return render(request, "mvote/index.html", context=locals())

# class IndexView(ListView):
#     model = Poll
#     template_name = "mvote/index.html"
#     context_object_name = "polls"

@login_required
def poll(request, pollId):
    poll = get_object_or_404(Poll, pk=pollId)
    pollitems = PollItem.objects.filter(poll=poll).order_by("-vote")
    return render(request, "mvote/poll.html", context=locals())

@login_required
def vote(request, pollId, pollItemId):
    if not VoteChech.objects.filter(userid=request.user.id, pollid=pollId, vote_date=datetime.today().date()):
        voteRec = VoteChech(userid=request.user.id, pollid=pollId, vote_date=datetime.today().date())
        voteRec.save()

        pollItem = get_object_or_404(PollItem, pk=pollItemId)
        pollItem.vote += 1
        pollItem.save()
        messages.add_message(request, messages.WARNING, "投票成功")
    else:
        messages.add_message(request, messages.WARNING, "您今天已经投过票了, 请明天再投")
    return redirect("/mvote/poll/{}".format(pollId))

@login_required
def remove_pollitem(request, pollId, pollItemId):
    try:
        pollItem = get_object_or_404(PollItem, pk=pollItemId)
        pollItem.delete()
        messages.add_message(request, messages.INFO, "移除成功")
    except:
        messages.add_message(request, messages.ERROR, "移除失败")
    return redirect("/mvote/poll/{}".format(pollId))
