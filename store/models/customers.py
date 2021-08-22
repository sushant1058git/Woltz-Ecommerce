from django.db import models

class Customers(models.Model):
    name = models.CharField(max_length=15)
    mobile_number = models.CharField(max_length=12)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


    @staticmethod
    def get_customer_by_email(mail):
        try:
            return Customers.objects.get(email = mail)

        except:
            return False

    @staticmethod
    def isExists(newmail):
        if Customers.objects.filter(email = newmail):
            return True
        else:
            return False


    @staticmethod
    def get_customer_by_id(customer):
        return Customers.objects.filter(id=customer)
