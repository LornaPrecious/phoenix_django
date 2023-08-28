from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from main.models import Customer
from django.contrib import messages
# Create your views here.

def register (request):
    if request.method =="POST":
            username = request.POST['username'] 
            fname = request.POST['fname']
            lname = request.POST['lname'] 
            email = request.POST['email']       
            password = request.POST['password']
            pass2 = request.POST['pass2']
            phonenumber = request.POST['phonenumber']
            gender = request.POST['gender']  
          
            
            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = lname

            user.save()
   
            
            mycustomer=Customer(user = user, first_name = fname, last_name = lname, email=email, password=password, phone_number=phonenumber, gender=gender )                                
            mycustomer.save()

            messages.success(request, "Your account has been successfully created.")

            return redirect('login')

    return render(request, "registration/register.html")

def custom_login(request):
      if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                  login(request, user)
                  username = user.username
                  return render(request, "main/index.html", {'username': username})

            else:
                  messages.error(request, "Wrong credentials")
                  return redirect('register')

      return render(request, "registration/login.html")
