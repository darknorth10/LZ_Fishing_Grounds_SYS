# Generated by Django 5.0.1 on 2024-01-24 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_rename_current_stock_products_current_stocks_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='t_img',
            new_name='product_img',
        ),
    ]
