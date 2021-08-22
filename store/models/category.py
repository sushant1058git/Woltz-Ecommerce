from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

