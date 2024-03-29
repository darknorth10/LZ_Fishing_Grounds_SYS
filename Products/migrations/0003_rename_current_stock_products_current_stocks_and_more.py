# Generated by Django 5.0.1 on 2024-01-24 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_alter_products_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='current_stock',
            new_name='current_stocks',
        ),
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='scientific_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
