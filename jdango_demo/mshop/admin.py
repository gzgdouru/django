from django.contrib import admin
from .models import Category, Product, Order, OrderItem

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ["category", "sku", "name", "stock", "price"]
    ordering = ["category"]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
