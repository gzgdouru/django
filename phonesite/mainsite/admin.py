from django.contrib import admin
from mainsite import models

class MakerAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]

class PModelAdmin(admin.ModelAdmin):
    list_display = ["name"]

class ProductAdmin(admin.ModelAdmin):
    list_display = ["pmodel", "nickname", "year", "price"]
    search_fields = ["nickname"]
    ordering = ["price"]

class PPhotoAdmin(admin.ModelAdmin):
    list_display = ["product"]

# Register your models here.
admin.site.register(models.Maker, MakerAdmin)
admin.site.register(models.PModel, PModelAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.PPhoto, PPhotoAdmin)
