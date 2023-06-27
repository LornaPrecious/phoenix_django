from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "main/index.html")

def aboutus(request):
    return render(request, "main/about.html")

def contactus(request):
    return render(request, "main/contactUs.html")

def products(request):
   return render(request, "main/products.html")


