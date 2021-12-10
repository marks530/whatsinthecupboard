from django.db.models.aggregates import Count
from django.urls import reverse
from django.contrib import admin, messages
from django.http.request import HttpRequest
from django.utils.html import format_html, urlencode #utility function
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status','collection_title', 'collection']
    list_editable = ['unit_price', 'collection']
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
    list_display = ['first_name', 'last_name', 'membership', 'orders']#, 'order_id'
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 20 
    
    @admin.display(ordering='orders_count')
    def orders(self, customer):
        url = (
            reverse('admin:store_order_changelist')
            + '?'
            + urlencode({
                'customer__id': str(customer.id)
            }))
        return format_html('<a href="{}">{} Orders</a>', url, customer.orders_count) 
    #def order_customer(self, customer_id):
        #return customer_id   
       
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at','customer']
    #list_editable = ['placed_at']
    #ordering = ['first_name', 'last_name']
    list_per_page = 20 

#admin.site.register(models.Collection)

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'products_count']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        #changelist is the name of the page in the collections admin section
        url = (
            reverse('admin:store_product_changelist')
            + '?'
            + urlencode({
                'collection__id': str(collection.id)  #enables filtering when jumping to the Products list
            }))

        return format_html('<a href="{}">{} Products</a>', url, collection.products_count)
         

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )    

class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['product']
    min_num = 1
    max_num = 10
    model = models.OrderItem
    extra = 0    
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    #inlines = [OrderItemInline]
    list_display = ['id', 'placed_at', 'customer']

#admin.site.register(models.Product, ProductAdmin)