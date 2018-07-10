# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models

# Register your models here.
class TagInline(admin.TabularInline):
    model = models.Tag

class ContactAdmin(admin.ModelAdmin):
    #fields = ("name", "email")

    inlines = [TagInline]
    fieldsets = (
        ["Main", {
            "fields" : ("name", "email")
        }],
        ["Advance", {
            "classes" : ("collapse",),
            "fields" : ("age",)
        }]
    )
    list_display = ("name", "email", "age")
    search_fields = ("name",)

admin.site.register(models.Contact, ContactAdmin)
admin.site.register([models.Character, models.Tag])
