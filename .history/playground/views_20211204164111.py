from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product,Customer,Order,OrderItem


def say_hello(request):
   queryset = Customer.objects.filter(first_name__icontains='.de')
   return render(request, 'hello.html', {'name': 'Mark', 'customers': list(queryset)})
