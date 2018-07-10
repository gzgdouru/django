from django.contrib import admin
from .models import Poll, PollItem, VoteChech

# Register your models here.
class PollAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "enabled"]
    ordering = ["-created_at"]

class PollItemAdmin(admin.ModelAdmin):
    list_display = ["poll", "name", "vote", "image_url"]
    ordering = ["poll"]

admin.site.register(Poll, PollAdmin)
admin.site.register(PollItem, PollItemAdmin)
admin.site.register(VoteChech)