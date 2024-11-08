from django import forms
from .models import *

class AddCustomer(forms.ModelForm):
    class Meta:
        model = Customers
        fields = "__all__"

class AddOrder(forms.ModelForm):
    class Meta:
        model = Orders
        fields = "__all__"