from django import forms

from .models import Products

class ProductCreationForm(forms.ModelForm):
    description = forms.CharField(required=False)
    scientific_name = forms.CharField(required=False)
    
    class Meta:
        model = Products
        fields = ("name", "category", "sub_category", "price", "stocks", "description", "scientific_name", "is_available", "product_img")
        
class ProductChangeForm(forms.ModelForm):
    description = forms.CharField(required=False)
    scientific_name = forms.CharField(required=False)
    
    class Meta:
        model = Products
        fields = ("name", "category", "sub_category", "price", "description", "scientific_name", "is_available", "product_img")
        
