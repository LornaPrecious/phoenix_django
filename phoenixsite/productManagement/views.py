from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime
from .utils import cartData

def products(request):
   return render(request, "productManagement/products.html")

def store(request):
  
   return render(request, "productManagement/store.html")

def product_view(request):
   context = {}
   return render(request, "productManagement/product_view.html", context)

def dresses(request):
   products = Product.objects.all()
   context = {'products': products}
   return render(request, "productManagement/dresses.html", context)

#******************************************************************************************************************************
def cart(request):
   data = cartData(request)
   cartItems = data['cartItems']
   order = data['order']
   items = data['items']

   context ={'order': order, 'items': items, 'cartItems': cartItems}
   return render(request, "productManagement/cart.html", context) 

#*********************************************************************************************************************
def checkout(request):
   data = cartData(request)
   cartItems = data['cartItems']
   order = data['order']
   items = data['items']


   if cartItems == 0:
        # Render a template indicating that the cart is empty
      return render(request, "productManagement/products.html")



   context = {'items': items, 'order': order, 'cartItems': cartItems}
   return render(request, "productManagement/checkout.html", context) 


#*********************************************************************************************************************
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

#****************************************************************************

def processOrder(request):
   data = json.loads(request.body)
#  transaction_id = datetime.datetime.now().timestamp()

   if request.user.is_authenticated:
      customer = request.user.customer
      order, created = Order.objects.get_or_create(customer=customer, complete=False) 
   
   else:
      pass
     # customer, order = guestOrder(request, data)
      
      

   total = float(data['form']['total'])
   total == float(order.get_cart_total)
   order.complete = True
   order.save()

         
#REVIEW THE CODE BELOW IF STATEMENT
      
   if order.shipping == True:
      if request.method == "POST":
         address = request.Post['address']
         address2 = request.Post['address2']
         country = request.Post['country']
         city = request.POST['city']
         zipcode = request.POST['zipcode']

         shipping = ShippingAddress(customer=customer, order= order, address=address, address2=address2, country=country, city=city, zipcode=zipcode)
         shipping.save()

   return JsonResponse('Payment complete', safe=False)