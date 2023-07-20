from django.shortcuts import render

def products(request):
   return render(request, "productManagement/products.html")

def store(request):
   return render(request, "productManagement/store.html")

def cart(request):
   context ={}
   return render(request, "products/cart.html", context)

def checkout(request):
   context = {}
   return render(request, "products/checkout.html", context)