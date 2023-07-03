from django import forms

customer_gender =[
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other')
]

concerns = [
    ('damaged_product', "Damaged product"),
    ("delayed_delivery", "Delayed delivery"),
    ('no_delivery', 'No delivery'),
    ("missing_product", 'Missing item from my order'),
    ('canceled_order', "Canceled order"),
    ('payment_issues', "Trouble paying"),
    ('customer_experience', "Poor customer experience"),
    ('other', 'Other')
]

class ContactUs(forms.Form):
    first_name = forms.CharField(label = "First name", max_length=250, required = True)
    last_name = forms.CharField(label = "Last name", max_length=250, required = True)
    email = forms.EmailField(help_text='joedoe@gmail.com', error_messages="Enter a valid email address", label="Email", required = True)
    gender = forms.CharField(label='Gender', required = False, widget=forms.RadioSelect(choices = customer_gender))
    phone_number = forms.IntegerField(label = 'Phone Number', required = True)
    address = forms.CharField(max_length=250, label="Address", required = False)
    issue = forms.MultipleChoiceField(required = True, label = 'What are your concerns?', widget=forms.CheckboxSelectMultiple(choices=concerns))
    other = forms.CharField(widget=forms.Textarea)


