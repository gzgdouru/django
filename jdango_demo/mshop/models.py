from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)    #分类
    sku = models.CharField(max_length=20)   # 产品编号
    name = models.CharField(max_length=200) # 产品名称
    description = models.TextField()    # 产品描述
    image = models.CharField(max_length=200, null=True)  # 图片网址
    website = models.URLField(null=True)    # 产品网址
    stock = models.PositiveIntegerField(default=0)  # 库存
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0) # 价格

    def __str__(self):
        return self.name

class LineItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    total_price = models.FloatField()

class Cart(object):
    def __init__(self, *args, **kwargs):
        self.items = []

    def __iter__(self):
        for item in self.items:
            yield item

    def add_product(self, product):
        for item in self.items:
            if product.id == item.product.id:
                item.quantity += 1
                return None
        self.items.append(LineItem(product=product, quantity=1, total_price=product.price))

    def summary(self):
        total_price = 0
        for item in self.items:
            total_price += item.total_price
        return total_price

    def remove_product(self, productId):
        for item in self.items:
            if item.product.id == productId:
                self.items.remove(item)
                return None

    def count(self):
        result = 0
        for item in self.items:
            result += (1 * item.quantity)
        return result

    def clear(self):
        self.items.clear()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return "Order:{}".format(self.id)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return "{}".format(self.id)




