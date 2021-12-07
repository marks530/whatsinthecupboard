from django.contrib import admin
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status','collection_title']
    list_editable = ['unit_price']
    list_per_page = 20
    list_select_related = ['collection']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'    


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 20 
    
       
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at','customer']
    #list_editable = ['placed_at']
    #ordering = ['first_name', 'last_name']
    list_per_page = 20 



@admin.register(models.Collections)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    #list_editable = ['placed_at']
    #ordering = ['first_name', 'last_name']
    list_per_page = 20 



#admin.site.register(models.Product, ProductAdmin)