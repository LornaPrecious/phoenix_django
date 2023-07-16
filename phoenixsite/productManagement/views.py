from django.shortcuts import render

def products(request):
   return render(request, "productManagement/products.html")

def store(request):
   return render(request, "productManagement/store.html")
