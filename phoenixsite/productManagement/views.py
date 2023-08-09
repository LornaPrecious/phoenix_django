from django.shortcuts import render
from .models import *

def products(request):
   return render(request, "productManagement/products.html")

def store(request):
   return render(request, "productManagement/store.html")

def cart(request):
   context ={}
   return render(request, "productManagement/cart.html", context)

def checkout(request):
   context = {}
   return render(request, "productManagement/checkout.html", context)

def dresses(request):
   products = Product.objects.all()
   context = {'products': products}
   return render(request, "productManagement/dresses.html", context)

def product_view(request):
   context = {}
   return render(request, "productManagement/product_view.html", context)