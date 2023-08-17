from django.db import models
from django.contrib.auth.models import User


    

class Customer (models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length= 100, null=True, blank=True)
    last_name = models.CharField(max_length= 100, null=True, blank=True)
    user_name = models.CharField(max_length= 100, null=True, blank=True)
    password = models.CharField(max_length= 100, null=True, blank=True)
    customer_id = models.IntegerField(primary_key= True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.IntegerField(help_text='0712345678 or +254712345678', null=True, blank=True) #look for a validator, ie. regex 
    gender = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    address2 = models.CharField(max_length=250, null=True, blank=True)
    country =models.CharField(max_length=250, null=True, blank=True)
    cityOrcounty = models.CharField(max_length=250, null=True, blank=True)
     
    def __str__(self):
        return str(self.customer_id)
    class Meta:
        db_table='customer'
    






