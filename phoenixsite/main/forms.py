from django import forms
from .models import Customer

customer_gender =[
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
]
concerns = [
    ('damaged_product', 'Damaged product'),
    ('delayed_delivery', 'Delayed delivery'),
    ('no_delivery', 'No delivery'),
    ('missing_product', 'Missing item from my order'),
    ('canceled_order', 'Canceled order'),
    ('payment_issues', 'Trouble paying'),
    ('customer_experience', 'Poor customer experience'),
    ('other', 'Other'),
] 

class ContactUs(forms.Form):
    first_name = forms.CharField(label = "First name", max_length=250, required = True)
    last_name = forms.CharField(label = "Last name", max_length=250, required = True)
    email = forms.EmailField(help_text='joedoe@gmail.com', label="Email", required = True)
    gender = forms.ChoiceField(label='Gender', required = True, widget=forms.RadioSelect(choices=customer_gender))
    phone_number = forms.IntegerField(label = 'Phone Number', required = True,)
    address = forms.CharField(max_length=250, label="Address", required = False,)
    issue = forms.MultipleChoiceField(label = 'What are your concerns?', widget=forms.CheckboxSelectMultiple(choices=concerns))
    other = forms.CharField(widget=forms.Textarea, label = "Other", max_length=600) 
 
"""
        Given a Widget instance (*not* a Widget class), return a dictionary of
        any HTML attributes that should be added to the Widget, based on this
        Field.
        """
""" class CreateAccount(forms.ModelForm):
    class Meta:
      model = Customer
      fields = ('password', 'first_name', 'last_name', 'email', 'phone_number', 'address') """


