from django.db import models

# Create your models here.
class Cart(models.Model):

    product_id = models.CharField(max_length=50, null=False)
    product_name = models.CharField(max_length=100, null=False)
    subtotal = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.PositiveIntegerField(null=False)
    
    
    def __str__(self):
        return self.product_name
    
class Transaction(models.Model):
    
    total = models.DecimalField(max_digits=9, decimal_places=2)
    change  = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    date_occured = models.DateField(auto_now_add=True)
    cashier = models.CharField(max_length=50, null=False)
    payment_method = models.CharField(max_length=50, null=False, default="cash")
    payment = models.DecimalField(max_digits=9, decimal_places=2, null=True, default=0)
    gcash_num = models.CharField(max_length=50, null=True)
    ref = models.CharField(max_length=50, null=True)
    
class Item(models.Model):
    
    tnum = models.IntegerField(null=False)
    product_id = models.CharField(max_length=50, null=False)
    quantity = models.IntegerField(null=False)
    subtotal = models.DecimalField(max_digits=9, decimal_places=2)
    
