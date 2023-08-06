from django.db import models
from django.contrib.auth.models import User


    

class Customer (models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    password = models.CharField(max_length= 100, null=True)
    customer_id = models.IntegerField(primary_key= True)
    email = models.EmailField()
    phone_number = models.IntegerField(help_text='0712345678 or +254712345678') #look for a validator, ie. regex 
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    def __str__(self):
        return str(self.customer_id)
    class Meta:
        db_table='customer'
    






