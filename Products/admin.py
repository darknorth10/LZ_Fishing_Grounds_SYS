from django.contrib import admin
from .models import Products, StocksLog

# Register your models here.
admin.site.register({Products, StocksLog})