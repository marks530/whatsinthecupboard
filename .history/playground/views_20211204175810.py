from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from store.models import Product,Customer,Order,OrderItem


def say_hello(request):
    queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct())
    return render(request, 'hello.html', {'name': 'Mark', 'products': list(queryset)})
