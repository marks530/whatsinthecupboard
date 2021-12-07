from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from store.models import Product,Customer,Order,OrderItem


def say_hello(request):
    queryset = OrderItem.objects.values_list('product_id').distinct()
    return render(request, 'hello.html', {'name': 'Mark', 'orderitems': list(queryset)})
