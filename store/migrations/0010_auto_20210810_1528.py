# Generated by Django 3.2.5 on 2021-08-10 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='address',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='orders',
            name='mobile',
            field=models.CharField(blank=True, default='', max_length=12),
        ),
    ]