from django import forms
from .models import product

class ProductForm(forms.Form):
    name = forms.CharField(
    max_length=100,
    required = True,
    help_text='Enter Product Name',
    widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Product Name'}),
    )  
