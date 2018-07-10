from django.db import models

# Create your models here.
# 手机厂商
class Maker(models.Model):
    name = models.CharField(max_length=10)  # 厂商名称
    country = models.CharField(max_length=10)   #所属国家

    def __str__(self):
        return self.name

#手机规格
class PModel(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)  #厂商
    name = models.CharField(max_length=20)  #手机款式
    url = models.URLField()     #规格说明网址

    def __str__(self):
        return self.name

#手机
class Product(models.Model):
    pmodel = models.ForeignKey(PModel, on_delete=models.CASCADE, verbose_name="型号")    #手机规格
    nickname = models.CharField(max_length=15, default="超值二手机")  #简单说明
    description = models.TextField(default="暂无说明")    #详细说明
    year = models.PositiveIntegerField(default=2016)    #制造年份
    price = models.PositiveIntegerField(default=0)   #售价

    def __str__(self):
        return self.nickname

#手机照片
class PPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  #手机
    description = models.CharField(max_length=20, default="产品照片")   #照片内容
    url = models.URLField() #照片的url


