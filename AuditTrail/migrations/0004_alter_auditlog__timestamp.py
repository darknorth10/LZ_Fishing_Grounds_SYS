# Generated by Django 5.0.1 on 2024-03-13 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuditTrail', '0003_rename_timestamp_auditlog__timestamp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditlog',
            name='_timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
