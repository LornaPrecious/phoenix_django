from django.shortcuts import render

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
   context = {}
   return render(request, "productManagement/dresses.html", context)