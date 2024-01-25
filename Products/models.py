from django.db import models


CATEGORY_CHOICES = [
    ("fish", "Fish"),
    ("aquarium supplies", "Aquarium Supplies"),
    ("fish food", "Fish Food"),
]

class Products(models.Model):
    
    name = models.CharField(max_length=60, null=False, unique=True)
    
    category = models.CharField(max_length=40, null=False, unique=True, choices=CATEGORY_CHOICES)
    sub_category = models.CharField(max_length=40, null=False, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    current_stocks = models.PositiveIntegerField(null=False)
    description = models.CharField(max_length=255, null=True)
    scientific_name = models.CharField(max_length=100, null=True)
    is_available = models.BooleanField(null=False, default=1)
    product_img = models.ImageField(upload_to='products', default='lz_fishing.jpg')
    date_registered = models.DateField(null=True, auto_now_add=True)
    
    def __str__(self):
        return self.name