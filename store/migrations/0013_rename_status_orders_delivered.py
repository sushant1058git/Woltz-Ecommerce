# Generated by Django 3.2.5 on 2021-08-11 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_orders_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='status',
            new_name='delivered',
        ),
    ]