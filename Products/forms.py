from django import forms

from .models import Products

class ProductCreationForm(forms.ModelForm):
    description = forms.CharField(required=False)
    scientific_name = forms.CharField(required=False)
    
    class Meta:
        model = Products
        fields = ("__all__")
        
