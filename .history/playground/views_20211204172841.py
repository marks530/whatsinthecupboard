from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from store.models import Product,Customer,Order,OrderItem


def say_hello(request):
   queryset = Product.objects.filter(email__icontains='em')
   return render(request, 'hello.html', {'name': 'Mark', 'customers': list(queryset)})
