from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from main.models import Customer
from django.contrib.auth.models import User
from django import forms

customer_gender =[
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
]

class CreateAccount(UserCreationForm):
    first_name = forms.CharField(label = "First name", max_length=250, required = True)
    last_name = forms.CharField(label = "Last name", max_length=250, required = True)
    email = forms.EmailField(help_text='joedoe@gmail.com', label="Email", required = True)
    gender = forms.ChoiceField(label='Gender', required = True, widget=forms.RadioSelect(choices=customer_gender))
    phone_number = forms.IntegerField(label = 'Phone Number', required = True,)
    address = forms.CharField(max_length=250, label="Address", required = False,)

    class Meta:
      model = Customer
      model = User
      fields = ('first_name', 'last_name', 'username', 'email', 'phone_number','gender', 'address', 'password1', 'password2')


