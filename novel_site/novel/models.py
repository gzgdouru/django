from django.db import models

from authors.models import Author


class Chapter0(models.Model):
    novel = models.ForeignKey('Novel', models.CASCADE, verbose_name="小说")
    chapter_url = models.URLField(unique=True, max_length=255, verbose_name="章节链接")
    chapter_index = models.PositiveIntegerField(verbose_name="章节顺序", default=0)
    chapter_name = models.CharField(max_length=255, verbose_name="章节名称")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "小说章节表0"
        verbose_name_plural = verbose_name
        db_table = 'tb_chapter_0'


class Chapter1(models.Model):
    novel = models.ForeignKey('Novel', models.CASCADE, verbose_name="小说")
    chapter_url = models.URLField(unique=True, max_length=255, verbose_name="章节链接")
    chapter_index = models.PositiveIntegerField(verbose_name="章节顺序", default=0)
    chapter_name = models.CharField(max_length=255, verbose_name="章节名称")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "小说章节表1"
        verbose_name_plural = verbose_name
        db_table = 'tb_chapter_1'


class Chapter2(models.Model):
    novel = models.ForeignKey('Novel', models.CASCADE, verbose_name="小说")
    chapter_url = models.URLField(unique=True, max_length=255, verbose_name="章节链接")
    chapter_index = models.PositiveIntegerField(verbose_name="章节顺序", default=0)
    chapter_name = models.CharField(max_length=255, verbose_name="章节名称")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "小说章节表2"
        verbose_name_plural = verbose_name
        db_table = 'tb_chapter_2'


class Chapter3(models.Model):
    novel = models.ForeignKey('Novel', models.CASCADE, verbose_name="小说")
    chapter_url = models.URLField(unique=True, max_length=255, verbose_name="章节链接")
    chapter_index = models.PositiveIntegerField(verbose_name="章节顺序", default=0)
    chapter_name = models.CharField(max_length=255, verbose_name="章节名称")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "小说章节表3"
        verbose_name_plural = verbose_name
        db_table = 'tb_chapter_3'


class Chapter4(models.Model):
    novel = models.ForeignKey('Novel', models.CASCADE, verbose_name="小说")
    chapter_url = models.URLField(unique=True, max_length=255, verbose_name="章节链接")
    chapter_index = models.PositiveIntegerField(verbose_name="章节顺序", default=0)
    chapter_name = models.CharField(max_length=255, verbose_name="章节名称")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "小说章节表4"
        verbose_name_plural = verbose_name
        db_table = 'tb_chapter_4'


class Chapter5(models.Model):
    novel = models.ForeignKey('Novel', models.CASCADE, verbose_name="小说")
    chapter_url = models.URLField(unique=True, max_length=255, verbose_name="章节链接")
    chapter_index = models.PositiveIntegerField(verbose_name="章节顺序", default=0)
    chapter_name = models.CharField(max_length=255, verbose_name="章节名称")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "小说章节表5"
        verbose_name_plural = verbose_name
        db_table = 'tb_chapter_5'


class Chapter6(models.Model):
    novel = models.ForeignKey('Novel', models.CASCADE, verbose_name="小说")
    chapter_url = models.URLField(unique=True, max_length=255, verbose_name="章节链接")
    chapter_index = models.PositiveIntegerField(verbose_name="章节顺序", default=0)
    chapter_name = models.CharField(max_length=255, verbose_name="章节名称")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "小说章节表6"
        verbose_name_plural = verbose_name
        db_table = 'tb_chapter_6'


class Chapter7(models.Model):
    novel = models.ForeignKey('Novel', models.CASCADE, verbose_name="小说")
    chapter_url = models.URLField(unique=True, max_length=255, verbose_name="章节链接")
    chapter_index = models.PositiveIntegerField(verbose_name="章节顺序", default=0)
    chapter_name = models.CharField(max_length=255, verbose_name="章节名称")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "小说章节表7"
        verbose_name_plural = verbose_name
        db_table = 'tb_chapter_7'


class Chapter8(models.Model):
    novel = models.ForeignKey('Novel', models.CASCADE, verbose_name="小说")
    chapter_url = models.URLField(unique=True, max_length=255, verbose_name="章节链接")
    chapter_index = models.PositiveIntegerField(verbose_name="章节顺序", default=0)
    chapter_name = models.CharField(max_length=255, verbose_name="章节名称")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "小说章节表8"
        verbose_name_plural = verbose_name
        db_table = 'tb_chapter_8'


class Chapter9(models.Model):
    novel = models.ForeignKey('Novel', models.CASCADE, verbose_name="小说")
    chapter_url = models.URLField(unique=True, max_length=255, verbose_name="章节链接")
    chapter_index = models.PositiveIntegerField(verbose_name="章节顺序", default=0)
    chapter_name = models.CharField(max_length=255, verbose_name="章节名称")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "小说章节表9"
        verbose_name_plural = verbose_name
        db_table = 'tb_chapter_9'


class NovelCategory(models.Model):
    name = models.CharField(max_length=32, verbose_name="分类名称")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "小说分类"
        verbose_name_plural = verbose_name
        db_table = "tb_novel_category"

    def __str__(self):
        return self.name


class Novel(models.Model):
    novel_name = models.CharField(unique=True, max_length=32, verbose_name="小说名称")
    site_name = models.CharField(max_length=32, verbose_name="小说网站")
    url = models.CharField(unique=True, max_length=255, verbose_name="小说链接")
    category = models.ForeignKey(NovelCategory, models.CASCADE, verbose_name="小说分类", null=True, blank=True)
    image = models.ImageField(upload_to='novel/%Y/%m/', max_length=200, verbose_name="小说图片", null=True, blank=True, default="default.jpg")
    author = models.ForeignKey(Author, models.CASCADE, verbose_name="小说作者", null=True, blank=True)
    desc = models.CharField(max_length=255, verbose_name="小说简介", null=True, blank=True)
    detail = models.TextField(verbose_name="详细介绍", null=True, blank=True)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "小说"
        verbose_name_plural = verbose_name
        db_table = 'tb_novel'

    def __str__(self):
        return self.novel_name
