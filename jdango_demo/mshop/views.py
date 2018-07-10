from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from .models import Cart, Order, OrderItem
from .forms import OrderForm

# Create your views here.
def index(request, cateId=0):
    cart = request.session.get("cart")
    all_products = Product.objects.all()
    paginator = Paginator(all_products, 5)
    p = request.GET.get("p")
    try:
        products = paginator.page(p)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    categorys = Category.objects.all()
    return render(request, "mshop/index.html", context=locals())

def product(request, productId):
    product = get_object_or_404(Product, pk=productId)
    categorys = Category.objects.all()
    return render(request, "mshop/product.html", context=locals())

def category(request, cateId):
    category = get_object_or_404(Category, pk=cateId)
    all_products = Product.objects.filter(category=category)
    paginator = Paginator(all_products, 5)
    p = request.GET.get("p")
    try:
        products = paginator.page(p)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    categorys = Category.objects.all()
    return render(request, "mshop/category.html", context=locals())

@login_required
def cart(request):
    cart = request.session.get("cart")
    if not cart:
        cart = Cart()
        request.session["cart"] = cart
    categorys = Category.objects.all()
    return render(request, "mshop/cart.html", context=locals())

def add_to_cart(request, productId, quantity):
    cart = request.session.get("cart")
    product = get_object_or_404(Product, pk=productId)
    redirect_to = request.GET.get("next")
    if  not cart: cart = Cart()
    cart.add_product(product)
    request.session["cart"] = cart

    if redirect_to:
        return redirect(redirect_to)
    else:
        return redirect("/mshop/")

def remove_from_cart(request, productId):
    cart = request.session.get("cart")
    if cart:
        cart.remove_product(int(productId))
        request.session["cart"] = cart
    return redirect("/mshop/cart/")

@login_required
def order(request):
    cart = request.session.get("cart")
    categorys = Category.objects.all()
    if request.method == "POST":
        user = User.objects.filter(username=request.user.username).first()
        newOrder = Order(user=user)
        forms = OrderForm(request.POST, instance=newOrder)
        if forms.is_valid():
            order = forms.save()
            emailMsg = "您的购物清单如下:\n"
            for item in cart:
                OrderItem.objects.create(order=order, product=item.product, price=item.product.price, quantity=item.quantity)
                emailMsg += "{}, {}, {}\n".format(item.product.name, item.product.price, item.quantity)
            emailMsg += "以上共计{}元, 感谢您的订购!".format(cart.summary())
            cart.clear()
            messages.add_message(request, messages.INFO, "订单已储存, 我们会尽快处理.")
            send_mail("感谢您的订购", emailMsg, "18719091650@163.com", ["gzgdouru@163.com"])
            return redirect("/mshop/myorder/")
    else:
        form = OrderForm()
    return render(request, "mshop/order.html", context=locals())

@login_required
def myorder(request):
    categorys = Category.objects.all()
    user = User.objects.filter(username=request.user.username).first()
    orders = Order.objects.filter(user=user)
    return render(request, "mshop/myorder.html", context=locals())

@login_required
def payment(request, orderid):
    categorys = Category.objects.all()
    order = get_object_or_404(Order, pk=orderid)
    orderItems = OrderItem.objects.filter(order=order)
    items = []
    total = 0
    for orderItem in orderItems:
        item = {}
        item["name"] = orderItem.product.name
        item["price"] = orderItem.price
        item["quantity"] = orderItem.quantity
        item["subtotal"] = orderItem.price * orderItem.quantity
        total += (orderItem.price * orderItem.quantity)
        items.append(item)
    return render(request, "mshop/payment.html", context={
        "categorys" : categorys,
        "items" : items,
        "total" : total,
        "order" : order,
    })

@login_required
def payment_done(request, orderid):
    order = get_object_or_404(Order, pk=orderid)
    order.paid = True
    order.save()
    return render(request, "mshop/payment_done.html", context={})



