import xadmin

from .models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse


class UserAskAdmin:
    list_display = ["name", "mobile", "course_name", "add_time"]
    search_fields = ["name", "mobile", "course_name"]
    list_filter = ["name", "mobile", "course_name", "add_time"]


class CourseCommentsAdmin:
    list_display = ["user", "course", "comments", "add_time"]
    search_fields = ["user__username", "course__name", "comments"]
    list_filter = ["user__username", "course__name", "comments", "add_time"]


class UserFavoriteAdmin:
    list_display = ["user", "fav_id", "fav_type", "add_time"]
    search_fields = ["user__username", "fav_id", "fav_type"]
    list_filter = ["user__username", "fav_id", "fav_type", "add_time"]


class UserMessageAdmin:
    list_display = ["user", "message", "has_read", "add_time"]
    search_fields = ["user", "message", "has_read"]
    list_filter = ["user", "message", "has_read", "add_time"]


class UserCourseAdmin:
    list_display = ["user", "course", "add_time"]
    search_fields = ["user__username", "course__name"]
    list_filter = ["user__username", "course__name", "add_time"]


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)