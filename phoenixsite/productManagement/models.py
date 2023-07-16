from django.db import models
from main.models import Customer

class Product(models.Model): 
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length = 350) 
    product_price = models.FloatField() #sale price per product
    product_tax = models.FloatField()
    product_discount = models.FloatField() #optional depending with products bought
    stock = models.IntegerField() #automate? goods not sold/ in storage
    products_bought = models.IntegerField() #no of products bought,
    purchase_price = models.IntegerField()# amount used to purchase the products for sale
    def __str__(self):
        return self.product_name
    class Meta:
        db_table='product'

class Order (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    order_id = models.IntegerField(primary_key=True)
    quantity = models.IntegerField() #number of products bought per order
    order_date = models.DateField(auto_now=True) 
    order_status = models.CharField(max_length=250)
    cost = models.IntegerField() # total quantity * product_price - discount 
    order_discount = models.FloatField() #optional depending with order, ie. an order above 5k has 10% discount
    def __str__(self):
        return self.order_id
    class Meta:
        db_table='order'

    
class Shipping(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    shipping_code = models.CharField(max_length=20, primary_key=True)
    product_weight = models.FloatField()
    location = models.CharField(max_length=200)
    delivery_cost = models.FloatField() #depending with location, product_weight, any discounts
    shipping_discount = models.FloatField() #optional depending with shipping
    shipping_status = models.CharField(max_length=250) 
    def __str__(self):
        return self.shipping_code
    class Meta:
        db_table='shipping'

class PaymentInfo(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)#reference to cutomerID
    order = models.ForeignKey(Order, on_delete=models.CASCADE)#orderID for product being paid
    shipping = models.ForeignKey(Shipping, models.SET_NULL, blank=True, null = True)

    payment_code = models.CharField(max_length= 20, primary_key=True)
    payment_type = models.CharField(max_length= 250, help_text="Mpesa(Kenyan phone numbers only), Bank_Transaction, cash on delivery")
    payment_phone = models.IntegerField(help_text='0712345678 or +254712345678') #look for a validator, ie. regex 
    amount = models.FloatField() #amount being paid
    payment_status = models.CharField(max_length= 250)
    def __str__(self):
        return self.payment_code
    class Meta:
        db_table='payment_information'

class Offer(models.Model): #can I apply these discounts to the other tables and automatically?
    product = models.ForeignKey(Product, models.SET_NULL, blank=True, null = True)
    order = models.ForeignKey(Order, models.SET_NULL, blank=True, null = True)
    shipping = models.ForeignKey(Shipping,models.SET_NULL, blank=True, null = True)

    coupon_code = models.CharField(max_length = 20, primary_key=True)
    offer_discount = models.FloatField() #percentage discount being offer
    description = models.CharField(max_length=1000)
    def __str__(self):
        return self.coupon_code
    class Meta:
        db_table='offer'

class Complaints(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)#orderID for product being paid
    shipping = models.ForeignKey(Shipping, models.SET_NULL, blank=True, null = True)

    complaint_code = models.CharField(max_length=20)
    issue = models.CharField(max_length=300)
    other = models.TextField()
    def __str__(self):
        return self.complaint_code
    class Meta:
        db_table='complaints'