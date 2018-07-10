from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, PPhoto

# Create your views here.
# def index(request):
#     products = Product.objects.all()
#     return render(request, "index.html", context={
#         "products" : products,
#     })

class IndexViwe(ListView):
    model = Product
    template_name = "index.html"
    context_object_name = "products"

# def detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     images = PPhoto.objects.filter(product=product)
#     return render(request, "detail.html", context={
#         "product" : product,
#         "images" : images,
#     })

class ProductDetailView(DetailView):
    model = Product
    template_name = "detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        product = context.get("product")
        images = PPhoto.objects.filter(product=product)
        context.update({
            "images" : images,
        })
        return context
