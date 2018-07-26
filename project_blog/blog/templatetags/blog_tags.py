from ..models import Category, Post, Comment, User
from django import template
from django.db.models import Count
from datetime import datetime, timedelta

register = template.Library()

@register.simple_tag
def get_posts(num=None):
    num = Post.object.all().count() if not num else num
    return Post.objects.all().order_by("-created_time")[:num]

@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_post=Count("post")).all()

@register.simple_tag
def archives():
    archive_list = []
    result = Post.objects.dates('created_time', 'month', order='DESC')
    for res in result:
        num_post = Post.objects.filter(created_time__year=res.year, created_time__month=res.month).count()
        archive_list.append({
            "archive_date" : res,
            "num_post" : num_post,
        })
    return archive_list

@register.simple_tag
def get_new_comments():
    return Comment.objects.all().order_by("-created_time")[:5]

@register.simple_tag
def read_ranking():
    return Post.objects.filter(views__gt=0).order_by("-views")[:5]

@register.simple_tag
def comment_ranking():
    return Post.objects.annotate(num_comment=Count("comment")).filter(num_comment__gt=0).order_by("-num_comment")[:5]

@register.simple_tag
def get_master():
    master = User.objects.get(master=True)
    now = datetime.now()
    if now.month < master.register_time.month:
       year = now.year - master.register_time.year - 1
       month = now.month + 12 - master.register_time.month
    else:
        year = now.year - master.register_time.year
        month = now.month - master.register_time.month
    master.age = {"year" : year, "month" : month}
    return master
