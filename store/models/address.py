from django.db import models
from .customers import Customers


class Address(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE,null=False, blank=False)
    full_name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    address = models.TextField(max_length=200)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pin = models.CharField(max_length=8)



    def __str__(self):
        return self.full_name

    @staticmethod
    def get_address():
        return Address.objects.all()

    @staticmethod
    def get_address_by_id(address_id):
        return Address.objects.filter(id=address_id)



    @staticmethod
    def get_address_by_customer_id(customer):
        return Address.objects.filter(customer=customer)