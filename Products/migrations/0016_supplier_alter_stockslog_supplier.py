# Generated by Django 5.0.1 on 2024-03-02 17:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0015_product_category_alter_stockslog_product_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='stockslog',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.supplier'),
        ),
    ]
