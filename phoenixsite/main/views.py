from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from .models import Product
from .forms import ContactUs
from . models import Customer, Complaints

def index(request):
    return render(request, "main/base.html", {})

def home(request):
    return render(request, "main/index.html")

def aboutus(request):
    return render(request, "main/about.html")

def contactus(request):
    if request.method == "POST":
        form = ContactUs(request.POST)
        if form.is_valid():
           info = Customer(first_name = request.POST.get('first_name'), last_name = request.POST.get('last_name'), email = request.POST.get('email'), gender = request.POST.get('gender'), phone_number = request.POST.get('phone_number'), address = request.POST.get('address'))
           info.save()
     
           co = Complaints(issue = request.POST.get('issues'), other = request.POST.get('other'))
           co.save()

        #use the following line when redirecting to user a/c page once I create the form
        #return HttpResponseRedirect(#url of page to redirect to #)

    else:
        form = ContactUs()
    return render(request, "main/contactUs.html", {"form":form})

def products(request):
   return render(request, "main/products.html")

def store(request):
   return render(request, "main/store.html")

# def productsid(response, id):
#     pn = Product.objects.get(product_id = id)
#     return HttpResponse("<h1> %s </h1>" %pn.product_name)