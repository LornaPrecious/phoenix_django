from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    return render(request, "main/index.html")

def aboutus(request):
    return render(request, "main/about.html")

def contactus(request):
    return render(request, "main/contactUs.html")

def products(request):
   return render(request, "main/products.html")

def productsid(response, id):
    pn = Product.objects.get(product_id = id)
    return HttpResponse("<h1> %s </h1>" %pn.product_name)