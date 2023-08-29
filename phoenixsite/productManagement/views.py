from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime

def products(request):
   return render(request, "productManagement/products.html")

def store(request):
   #items = order.orderitem_set.all()
   #cartItems = order.get_cart_items
   return render(request, "productManagement/store.html")

def product_view(request):
   context = {}
   return render(request, "productManagement/product_view.html", context)

def dresses(request):
   products = Product.objects.all()
   context = {'products': products}
   return render(request, "productManagement/dresses.html", context)


def cart(request):
   if request.user.is_authenticated:
      customer = request.user.customer
      order, created = Order.objects.get_or_create(customer=customer, complete=False) #creating/quering an object
     
      items = order.orderitem_set.all()

   else: #if user isn't authenticated/hasn't logged in
      items = []
      order = {'get_cart_total': 0, 'get_cart_items':0, 'get_full_total': 0, 'shipping': False}

   context ={'order': order, 'items': items}
   return render(request, "productManagement/cart.html", context) 

def checkout(request):
   if request.user.is_authenticated:
      customer = request.user.customer
      order, created = Order.objects.get_or_create(customer=customer, complete=False) #creating/quering an object
   
      items = order.orderitem_set.all()

   else: #if user isn't authenticated/hasn't logged in
      items = []
      order = {'get_cart_total': 0, 'get_cart_items':0, 'get_full_total': 0, 'shipping': False}

   context = {'items': items, 'order': order}
   return render(request, "productManagement/checkout.html", context) 


def updateItem(request):
   data = json.loads(request.body)
   productId = data['productId']
   action = data['action']

   print('Action: ', action)
   print('ProductID: ', productId)

   customer = request.user.customer
   product = Product.objects.get(product_id = productId)
   order, created = Order.objects.get_or_create(customer=customer, complete=False) 
   
   orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

   if action == 'add':
      orderItem.quantity +=1
   
   elif action =='remove':
      orderItem.quantity -= 1

   orderItem.save()

   if orderItem.quantity <= 0 or action =='remove_product':
      orderItem.delete()

   return JsonResponse('Product added successfully', safe=False)

def processOrder(request):
   data = json.loads(request.body)

   if request.user.is_authenticated:
      customer = request.user.customer
      order, created = Order.objects.get_or_create(customer=customer, complete=False)
      
      total = float(data['form']['total'])
    

      if total == float(order.get_cart_total):
         order.complete = True
         order.save()
      
      else:
         order.complete = False

      if order.shipping == True:
         if request.method == "POST":
            address = request.Post['address']
            address2 = request.Post['address2']
            country = request.Post['country']
            city = request.POST['city']
            zipcode = request.POST['zipcode']

            shipping = ShippingAddress(address=address, address2=address2, country=country, city=city, zipcode=zipcode)
            shipping.save()
         
   else:
      print('User is not logged in')

   return JsonResponse('Payment complete', safe=False)