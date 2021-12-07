from django.contrib import admin
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price']
    list_editable = ['unit_price']
    list_per_page = 20


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = f{'first_name'}, {'last_name'}
    list_editable = ['membership']
    list_per_page = 20    


admin.site.register(models.Collection)

#admin.site.register(models.Product, ProductAdmin)