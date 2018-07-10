from django.conf.urls import url
from mshop import views

app_name = "mshop"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^category/(\d+)/$', views.category, name="category"),
    url(r'^product/(\d+)/$', views.product, name="product"),
    url(r'^cart/$', views.cart, name="cart"),
    url(r'^additem/(\d+)/(\d+)/$', views.add_to_cart, name="additem"),
    url(r'^removeitem/(\d+)/$', views.remove_from_cart, name="removeitem"),
    url(r'^order/$', views.order, name="order"),
    url(r'^myorder/$', views.myorder, name="myorder"),
    url(r'^payment/(\d+)/$', views.payment, name="payment"),
    url(r'^paymentdone/(\d+)/$', views.payment_done, name="payment_done"),
]