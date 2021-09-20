from .models import Product
from django import forms

class OrderForm(forms.Form):

    name = forms.CharField(max_length=255)
    surname = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    address = forms.CharField(widget=forms.Textarea())
    city = forms.CharField(max_length=255)