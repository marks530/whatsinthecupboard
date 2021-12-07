from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, Count, Max, Min, Sum
from store.models import Product,Customer,Order,OrderItem


def say_hello(request):
    result = Order.objects.aggregate(count=Count('id'))
    result2 = Product.objects.aggregate(Min('unit_price'))
    result3 = OrderItem.objects.filter(product_id=1).aggregate(units_sold=Sum('quantity'))
    #queryset = Order.objects.select_related(
        #'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[0:5]
    #queryset = Product.objects.prefetch_related(
        #'promotions').select_related('collection').all()
    # queryset = Product.objects.values('id', 'title')
    #queryset = Product.objects.filter(
        #id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    return render(request, 'hello.html', {'name': 'Mark', 'result': result, 'result2': result2})
