from django.contrib import admin
from .models.products import Products
from .models.category import Category
from .models import Customers
from .models.address import Address
from .models.orders import Orders

class AdminProductView(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class AdminCategoryView(admin.ModelAdmin):
        list_display = ['category_name']


class CustomerAdminView(admin.ModelAdmin):
    list_display = ['name', 'mobile_number', 'email']


class AddressAdminView(admin.ModelAdmin):
    list_display = ['full_name', 'mobile', 'address']

class OrderView(admin.ModelAdmin):
    list_display = ['customer','product']

admin.site.register(Products, AdminProductView)
admin.site.register(Category, AdminCategoryView)
admin.site.register(Customers,CustomerAdminView)
admin.site.register(Address, AddressAdminView)
admin.site.register(Orders, OrderView)
