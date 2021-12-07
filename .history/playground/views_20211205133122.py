from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from store.models import Product,Customer,Order,OrderItem


def say_hello(request):
    queryset = OrderItem.objects.values('order', 'product_id')
    #queryset = Product.objects.prefetch_related(
        #'promotions').select_related('collection').all()
    # queryset = Product.objects.values('id', 'title')
    #queryset = Product.objects.filter(
        #id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    return render(request, 'hello.html', {'name': 'Mark', 'products': list(queryset)})
