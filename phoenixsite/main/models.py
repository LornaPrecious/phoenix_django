from django.db import models
 
class Product(models.Model): 
    product_id = models.IntegerField(max_length = 5, primary_key=True)
    name = models.CharField(max_length = 250) 
    product_price = models.FloatField() #sale price
    description = models.TextField()
    stock = models.IntegerField() #automate? goods not sold/ in storage
    products_bought = models.IntegerField() #no of products bought,
    purchase_price = models.IntegerField()# amount used to purchase the products for sale


class Order (models.Model):
    order_id = models.IntegerField(max_length=5, primary_key=True)
    product_id = models.IntegerField(max_length = 5, foreign_key=True)
    quantity = models.IntegerField() #number of products bought per order
    order_date = models.DateField(auto_now=True) 
    order_status = models.CharField()
    tax = models.FloatField()
    cost = models.IntegerField() # total quantity * product_price - discount + tax applied(if it's separate)
    customer_id = models.IntegerField(max_length=5, foreign_key= True)
    order_discount = models.FloatField() #optional depending with order
    shipping_code = models.CharField(max_length=15, foreign_key=True)#optional depending with order

class Customer (models.Model):
    customer_id = models.IntegerField(max_length=5, primary_key= True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(help_text='joedoe@gmail.com')
    phone_number = models.IntegerField(help_text='0712345678 or +254712345678') #look for a validator, ie. regex 
    gender = models.CharField(max_length=7)
    address = models.CharField()

class Shipping(models.Model):
    shipping_code = models.CharField(max_length=15, primary_key=True)
    product_weight = models.FloatField()
    location = models.CharField(max_length=200)
    delivery_cost = models.FloatField() #depending with location, product_weight, any discounts
    order_id = models.IntegerField(max_length=5, foreign_key=True)
    customer_id = models.IntegerField(max_length=5, foreign_key=True)
    shipping_discount = models.FloatField() #optional depending with shipping


class Offer(models.Model): #can I apply these discounts to the other tables?
    coupon_code = models.CharField(max_length = 10, primary_key=True)
    offer_discount = models.FloatField()
    description = models.CharField(max_length=1000)



