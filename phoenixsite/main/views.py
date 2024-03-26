from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from .models import Product
from .forms import ContactUs
from . models import Customer
from productManagement.models import Complaints, Order
from productManagement.utils import cartData
from django.contrib.auth.models import User

def index(request):
    data = cartData(request)
    cartItems = data['cartItems']
  

    context ={'cartItems': cartItems}
    return render(request, "main/base.html", context)

def home(request):
    return render(request, "main/index.html")

def aboutus(request):
    return render(request, "main/about.html")

def contactus(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname'] 
        email = request.POST['email']       
        phonenumber = request.POST['phonenumber']
        complaints = request.POST['complaints']
        other = request.POST['other']
        

        if User.objects.filter(email=email):
            myCustomer = request.user.customer

            customer_complaint = Complaints(customer = myCustomer, first_name = fname, last_name=lname, email = email, phone_number = phonenumber, issue=complaints, other=other)
            customer_complaint.save()
        
        else:
            customer_complaint = Complaints(customer = myCustomer, first_name = fname, last_name=lname, email = email, phone_number = phonenumber, issue=complaints, other=other)
            customer_complaint.save()      
       
    return render(request, "main/contactUs.html")

# def productsid(response, id):
#     pn = Product.objects.get(product_id = id)
#     return HttpResponse("<h1> %s </h1>" %pn.product_name)