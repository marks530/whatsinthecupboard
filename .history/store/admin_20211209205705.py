from django.db.models.aggregates import Count
from django.urls import reverse
from django.contrib import admin, messages
from django.http.request import HttpRequest
from django.db.models.query import QuerySet
from django.utils.html import format_html, urlencode #utility function
from . import models


#admin.site.register(models.OrderItem)
class InventoryFilter(admin.SimpleListFilter):
    title = 'Stock Levels'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin): #model_admin: Any) -> List[Tuple[Any, str]]:
        return [
            ('<10', 'Stock Levels Low'),
            ('>10', 'Stock Levels OK')
        ]
    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)
        #else:
        #    return queryset.filter(inventory__gt=10)



@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    actions = ['clear_inventory']
    list_display = ['title', 'unit_price', 'inventory', 
    'inventory_status','collection_title', 'collection']#, 'collection'
    list_editable = ['unit_price', 'collection']
    list_filter = ['collection', 'last_update', InventoryFilter]
    list_per_page = 20
    list_select_related = ['collection'] #to reduce the number of queries to the database

    def collection_title(self, product):
        return product.collection.title

    #def order_id( self, order):
     #  return order.placed_at   
     

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'Grand'

    @admin.action(description='Clear Stock Levels')    
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message.user(
            request, 
            f'{updated_count} products were successfully updated'
        )
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'id' , 'products_count']
    search_fields = ['title']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        #changelist is the name of the page in the collections admin section
        #return collection.products_count
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


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    #autocomplete_fields = ['customer']
    list_display = ['first_name', 'last_name', 'membership', 'orders']#, 'orders'
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 20
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
 
    @admin.display(ordering='orders_count')
    def orders(self, customer):
        url = (
            reverse('admin:store_order_changelist')
            + '?'
            + urlencode({
                'customer__id': str(customer.id)
            }))
        return format_html('<a href="{}">{} Orders</a>', url, customer.orders_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            orders_count=Count('order')
        )
    
    
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    list_display = ['id', 'placed_at','customer', 'payment_status']
    #list_editable = ['placed_at']
    ordering = ['payment_status']
    list_per_page = 20 
    

#admin.site.register(models.Collection)
@admin.register(models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'product','quantity', 'unit_price']
    #list_editable = ['placed_at']
    ordering = ['order_id']
    list_per_page = 20 
    


    #def get_queryset(self, request):
     #   return super().get_queryset(request).annotate(
      #      products_count=Count('product')
       # )    


class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['product']
    min_num = 1
    max_num = 10
    model = models.OrderItem
    extra = 0 

    
    

#admin.site.register(models.Product, ProductAdmin)