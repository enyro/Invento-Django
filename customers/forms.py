from django import forms
from .models import Customer

class CustomerForm(forms.Form):
    name = forms.CharField(
    max_length=100,
    required = True,
    help_text='Enter Customer Name',
    widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Customer Name'}),
    ) 
    address = forms.CharField(
    max_length=100,
    required = True,
    help_text='Enter Customer Address',
    widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Customer Address'}),
    ) 
    telephone = forms.CharField(
    max_length=20,
    required = True,
    help_text='Enter Customer Telephone',
    widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Customer Telephone'}),
    )  