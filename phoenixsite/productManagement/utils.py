import json
import random
from .models import *
from django.contrib.auth.models import User

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart']) #parse the cookie which is a string back to python dictionary
    except:
            cart = {}
    print('Cart:', cart)
    items = []
    order = {'get_cart_total': 0, 'get_cart_items':0, 'get_full_total': 0, 'shipping': False}
    cartItems = order['get_cart_items']

    for i in cart:
        try:
            cartItems += cart[i]["quantity"]

            product = Product.objects.get(product_id=i)
            total = (product.product_price * cart[i]["quantity"])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]["quantity"]

            item = {
                'product':{
                    'product_id': product.product_id,
                    'product_name': product.product_name,
                    'product_price': product.product_price,
                    'product_imagesURL': product.product_imagesURL,
                    },
                
                'quantity': cart[i]["quantity"],
                'get_total': total
                }

            items.append(item)

                #If products are digital and/or physical

            if product.digital == False:
                order['shipping'] = True

        except:
            pass
    return {'cartItems': cartItems, 'order': order, 'items':items}


def cartData(request):
    if request.user.is_authenticated:
      customer = request.user.customer
      order, created = Order.objects.get_or_create(customer=customer, complete=False) #creating/quering an object
   
      items = order.orderitem_set.all()
      cartItems = order.get_cart_items
    else: #if user isn't authenticated/hasn't logged in
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
    
    return {'cartItems': cartItems, 'order': order, 'items': items}


def guestOrder(request, data):

    print('User is not logged in')
    print('COOKIES:', request.COOKIES)
    
    first_name = data['form']['fname']
    last_name = data['form']['lname']
    email = data['form']['email']
    phone_number = data['form']['phonenumber']


    customer, created = Customer.objects.get_or_create(
    email=email, defaults={
        'first_name': first_name,
        'last_name': last_name,
        'phone_number': phone_number,
        }
    )

#Created is bool, True if instance is created, False if fetched 
# Update the customer details if the customer already exists
    if not created:
        customer.first_name = first_name
        customer.last_name = last_name
        customer.phone_number = phone_number
        customer.save()
    
#Creating a 'guest' customer order

    order = Order.objects.get_or_create(customer=customer, complete = False)
    total = float(data['form']['total'])
    total == float(order.get_cart_total)
    order.complete = True
    order.save()

    cookieData = cookieCart(request)
    items = cookieData['items']
         

    for item in items:
        product = Product.objects.get(product_id = item['product']['product_id'])
      
        try:
            orderItem = OrderItem.objects.get(product=product, order=order)
            orderItem.quantity = item['quantity']
            orderItem.save()
        except OrderItem.DoesNotExist:
            orderItem = OrderItem.objects.create(product=product, order=order, quantity=item['quantity'])

    return (customer, order)
