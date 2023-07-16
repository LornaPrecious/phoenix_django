from django.db import models

class Customer (models.Model):
    customer_id = models.IntegerField(primary_key= True)
    password = models.CharField(max_length= 100)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    username_field = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.IntegerField(help_text='0712345678 or +254712345678') #look for a validator, ie. regex 
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    def __str__(self):
        return self.customer_id
    class Meta:
        db_table='customer'
    






