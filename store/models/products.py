from django.db import models
from .category import Category


class Products(models.Model):
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=40, default='', null=True, blank=True)
    products_image = models.ImageField(upload_to='images', null=True, blank=True)



    @staticmethod
    def get_all_product():
        return Products.objects.all()

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_product_by_Id():
        return Products.objects.filter()

    @staticmethod
    def get_all_category_by_id(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.objects.all()

    @staticmethod
    def get_product_by_id(ids):
        return Products.objects.filter(id__in=ids)



    @staticmethod
    def get_product_by_id_from_buy_now(buy_now_product_id):
        return Products.objects.filter(id=buy_now_product_id)

