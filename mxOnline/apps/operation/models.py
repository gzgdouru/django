from django.db import models

from courses.models import Course
from users.models import UserProfile

# Create your models here.


class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name="姓名")
    mobile = models.CharField(max_length=11, verbose_name="手机")
    course_name = models.CharField(max_length=50, verbose_name="课程名称")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    comments = models.CharField(max_length=200, verbose_name="评论")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    def __str__(self):
        return "{}({})".format(self.user.username, self.course.name)

    class Meta:
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    fav_id = models.PositiveIntegerField(default=0, verbose_name="数据id")
    fav_type = models.PositiveIntegerField(choices=((1, "课程"), (2, "课程机构"), (3, "讲师")), default=1, verbose_name="收藏类型")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.PositiveIntegerField(default=0, verbose_name="接收用户")
    message = models.CharField(max_length=500, verbose_name="消息内容")
    has_read = models.BooleanField(default=False, verbose_name="是否已读")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "用户课程"
        verbose_name_plural = verbose_name

