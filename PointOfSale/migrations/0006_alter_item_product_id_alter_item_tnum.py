# Generated by Django 5.0.1 on 2024-03-02 21:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PointOfSale', '0005_transaction_status_alter_transaction_payment_method'),
        ('Products', '0018_alter_products_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.products'),
        ),
        migrations.AlterField(
            model_name='item',
            name='tnum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PointOfSale.transaction'),
        ),
    ]