from django.db import models
from .products import Products
from .customers import Customers
import datetime


class Orders(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=200, default="", blank=True)
    mobile = models.CharField(max_length=12, default="", blank=True)
    date = models.DateField(default=datetime.datetime.today)
    delivered = models.BooleanField(default=0)




    def get_order_by_customerId(customerId):
        return Orders.objects.filter(customer = customerId )

