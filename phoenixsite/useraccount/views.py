from django.shortcuts import render, redirect
from main.models import Customer
from .forms import CreateAccount

# Create your views here.

def register (request):
    if request.method =="POST":
        form = CreateAccount(request.POST)
        if form.is_valid():
            info = Customer(password = request.POST.get('password'), username = request.POST.get('username_field'), first_name = request.POST.get('first_name'), last_name = request.POST.get('last_name'), email = request.POST.get('email'), gender = request.POST.get('gender'), phone_number = request.POST.get('phone_number'), address = request.POST.get('address'))
            info.save()
        return redirect("/home")
    else:
        form = CreateAccount()
    return render(request, "useraccount/register.html", {"form":form})
