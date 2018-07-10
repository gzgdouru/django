from django.contrib import admin
from .models import Profile, Post

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["nickname", "male", "age"]

class PostAdmin(admin.ModelAdmin):
    list_display = ["user", "created_time"]
    ordering = ["-created_time"]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)
