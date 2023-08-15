from django.shortcuts import render
from .models import *

def products(request):
   return render(request, "productManagement/products.html")

def store(request):
   return render(request, "productManagement/store.html")

def cart(request):
   if request.user.is_authenticated:
      customer = request.user.customer
      order, created = Order.objects.get_or_create(customer=customer, complete=False) #creating/quering an object
      items = order.orderitem_set.all()

   else: #if user isn't authenticated/hasn't logged in
      items = []
      order = {'get_cart_total': 0, 'get_cart_items':0 }
   context ={'items': items, 'order': order}
   return render(request, "productManagement/cart.html", context)

def checkout(request):
   if request.user.is_authenticated:
      customer = request.user.customer
      order, created = Order.objects.get_or_create(customer=customer, complete=False) #creating/quering an object
      items = order.orderitem_set.all()

   else: #if user isn't authenticated/hasn't logged in
      items = []
      order = {'get_cart_total': 0, 'get_cart_items':0 }
   context = {'items': items, 'order': order}
   return render(request, "productManagement/checkout.html", context)

def dresses(request):
   products = Product.objects.all()
   context = {'products': products}
   return render(request, "productManagement/dresses.html", context)

def product_view(request):
   context = {}
   return render(request, "productManagement/product_view.html", context)