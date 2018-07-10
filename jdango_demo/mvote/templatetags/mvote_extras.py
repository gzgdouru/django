from django import template
from mvote.models import Poll, PollItem

register = template.Library()

@register.filter(name="show_items")
def show_items(value):
    try:
        poll = Poll.objects.get(id=int(value))
        items = PollItem.objects.filter(poll=poll).count()
    except:
        items = 0
    return items

@register.filter(name="show_votes")
def show_votes(value):
    try:
        poll = Poll.objects.get(id=int(value))
        pollItems = PollItem.objects.filter(poll=poll)
        votes = 0
        for pollitem in pollItems:
            votes += pollitem.vote
    except:
        votes = 0
    return votes