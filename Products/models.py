from django.db import models
from django.core.validators import MinValueValidator


CATEGORY_CHOICES = [
    ("fish", "Fish"),
    ("aquarium supplies", "Aquarium Supplies"),
    ("fish food", "Fish Food"),
]

class Products(models.Model):
    
    name = models.CharField(max_length=60, null=False, unique=True)
    category = models.CharField(max_length=40, null=False, choices=CATEGORY_CHOICES)
    sub_category = models.CharField(max_length=40, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    stocks = models.PositiveIntegerField(null=False)
    description = models.CharField(max_length=255, null=True)
    scientific_name = models.CharField(max_length=100, null=True)
    is_available = models.BooleanField(null=False, default=1)
    product_img = models.ImageField(upload_to='products', default='lz_fishing.jpg')
    date_registered = models.DateField(null=True, auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class StocksLog(models.Model):
    product_id = models.CharField(max_length=200, null=True)
    supplier = models.CharField(max_length=200, null=False)
    total_cost = models.DecimalField(max_digits=9, decimal_places=2, null=False)
    stocks_added = models.PositiveIntegerField(null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    added_by = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return str(self.product_id)