from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=20, verbose_name="城市")
    desc = models.TextField(verbose_name="描述")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name="机构名称")
    desc = models.TextField(verbose_name="机构描述")
    category = models.CharField(max_length=20, choices=(("pxjg", "培训机构"), ("gr", "个人"), ("gx", "高校")), default="pxjg", verbose_name="机构类别")
    click_nums = models.PositiveIntegerField(default=0, verbose_name="点击数")
    fav_nums = models.PositiveIntegerField(default=0, verbose_name="收藏数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="封面图", max_length=100)
    address = models.CharField(max_length=150, verbose_name="地址")
    city = models.ForeignKey(City, verbose_name="城市", on_delete=models.CASCADE)
    tag = models.CharField(max_length=10, verbose_name="机构标签", default="全国知名")
    students = models.PositiveIntegerField(default=0, verbose_name="学习人数")
    course_nums = models.PositiveIntegerField(default=0, verbose_name="课程数")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name="所属机构", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="教师名称")
    work_years = models.PositiveIntegerField(default=0, verbose_name="工作年限")
    work_company = models.CharField(max_length=50, verbose_name="就职公司")
    work_position = models.CharField(max_length=50, verbose_name="公司职位")
    points = models.CharField(max_length=50, verbose_name="教学特点")
    click_nums = models.PositiveIntegerField(default=0, verbose_name="点击数")
    fav_nums = models.PositiveIntegerField(default=0, verbose_name="收藏数")
    image = models.ImageField(upload_to="teacher/%Y/%m", verbose_name="教师图片", max_length=200, default="")
    age = models.PositiveIntegerField(default=0, null=True, blank=True, verbose_name="讲师年龄")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name