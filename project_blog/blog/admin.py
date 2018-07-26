from django.contrib import admin
from .models import Category, Post, Comment, User

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "abstract", "category", "author", "views", "created_time"]

class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_time"]

class UserAdmin(admin.ModelAdmin):
    list_display = ["nickname", "register_time", "fans_num", "concern_num"]

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(User, UserAdmin)
