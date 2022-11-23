from django import forms
from .models import supplier

class SupplierForm(forms.Form):
    name = forms.CharField(
    max_length=100,
    required = True,
    help_text='Enter Supplier Name',
    widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Supplier Name'}),
    ) 
    address = forms.CharField(
    max_length=100,
    required = True,
    help_text='Enter Supplier Address',
    widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Supplier Address'}),
    ) 
    country = forms.CharField(
    max_length=20,
    required = True,
    help_text='Enter Country Address',
    widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Supplier Country'}),
    ) 
    telephone = forms.CharField(
    max_length=20,
    required = True,
    help_text='Enter Supplier Telephone',
    widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Supplier Telephone'}),
    )  