from django.contrib import admin
from .models import Post, Mood

class PostAdmin(admin.ModelAdmin):
    list_display = ["nickname", "message", "enabled", "pub_time"]
    ordering = ["-pub_time"]
    actions = ["enable_post"]

    def enable_post(self, request, queryset):
        queryset.update(enabled=True)
    enable_post.short_description = "enable select posts"

# Register your models here.
admin.site.register(Mood)
admin.site.register(Post, PostAdmin)