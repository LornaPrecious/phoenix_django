from django.db import models
from main.models import Customer

class Product(models.Model): 
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length = 350) 
    product_image = models.ImageField(null=True, blank=True)
    product_price = models.FloatField() #sale price per product
    digital = models.BooleanField(default=False, null=True, blank=True) #ship product if its not digital, hence the default false
    product_tax = models.FloatField()
    stock = models.IntegerField() #automate? goods not sold/ in storage
    products_bought = models.IntegerField() #no of products bought,
    purchase_price = models.IntegerField()# amount used to purchase the products for sale
    def __str__(self):
        return self.product_name
    class Meta:
        db_table='product'

    @property #help us access this as an attribute rather than as a model
    def product_imagesURL(self):
        try: 
            url = self.product_image.url
        except:
            url = ''
        return url

class Order (models.Model): ##This basically represents the CART
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True) #one to many relationship, 1 customer, can have multiple orders

    order_id = models.IntegerField(primary_key=True)
    order_date = models.DateField(auto_now=True) 
    complete = models.BooleanField(default=False) #if complete is false can continue adding items, changes status of cart is it same as order status??
    cost = models.IntegerField() # total quantity * product_price - discount 
    def __str__(self):
        return str(self.order_id)
    
    @property
    def shipping(self):
        shipping = False
        orderitems= self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping
    
    @property
    def get_cart_total(self):
        orderitems= self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems= self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    class Meta:
        db_table='order'

    
class OrderItem (models.Model): #This items represents items within the cart
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True) #one to many relationship, 1 customer, can have multiple orders
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)


    quantity = models.IntegerField(default=0, null=True, blank=True) #number of products bought per order
    date_added = models.DateField(auto_now=True) #date we added an item to order
    def __str__(self):
        return str(self.product.product_name)
    
    @property
    def get_total(self):
        product_total = self.product.product_price * self.quantity
        return product_total
    
    class Meta:
        db_table='orderItem'

    
class ShippingAddress(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)

    shipping_code = models.CharField(max_length=20, primary_key=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    delivery_cost = models.FloatField() #depending with location, product_weight, any discounts
    shipping_date = models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        return self.shipping_code
    class Meta:
        db_table='shippingAddress'

    @property
    def get_full_total(self):
        if (self.order.get_cart_total >= 5499):
            full_total = (self.order.get_cart_total - (self.order.get_cart_total * 0.13)) + self.delivery_cost

        elif(self.order.get_cart_total >= 2499 and self.order.get_cart_total <= 5498):
            full_total =(self.order.get_cart_total - (self.order.get_cart_total * 0.10)) + self.delivery_cost
        else:
            full_total = self.order.get_cart_total + self.delivery_cost 
        return full_total


class PaymentInfo(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)#reference to cutomerID
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)#orderID for product being paid
    shippingAddress = models.ForeignKey(ShippingAddress, models.SET_NULL, blank=True, null = True)

    payment_code = models.CharField(max_length= 20, primary_key=True)
    payment_type = models.CharField(max_length= 250, help_text="Mpesa(Kenyan phone numbers only)")
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
    shippingAddress = models.ForeignKey(ShippingAddress, models.SET_NULL, blank=True, null = True)

    coupon_code = models.CharField(max_length = 20, primary_key=True)
    offer_discount = models.FloatField() #Must be in percentages
    description = models.CharField(max_length=1000)
    def __str__(self):
        return self.coupon_code
    class Meta:
        db_table='offer'

    

class Complaints(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null = True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null = True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null = True)#orderID for product being paid
    shipping = models.ForeignKey(ShippingAddress, models.SET_NULL, blank=True, null = True)

    complaint_code = models.CharField(max_length=20)
    first_name = models.CharField(max_length= 100, null=True, blank=True)
    last_name = models.CharField(max_length= 100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.IntegerField(help_text='0712345678 or +254712345678', null=True, blank=True) #look for a validator, ie. regex 
    gender = models.CharField(max_length=20, null=True, blank=True)
    issue = models.CharField(max_length=300, null=True, blank=True)
    other = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.complaint_code
    class Meta:
        db_table='complaints'