# Generated by Django 5.0.1 on 2024-01-24 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(choices=[(1, 'Active'), (0, 'Inactive')]),
        ),
    ]
