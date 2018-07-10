# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
import models

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "timestamp")

# Register your models here.
admin.site.register(models.BlogPost, BlogPostAdmin)
