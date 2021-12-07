from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product


def say_hello(request):
   queryset = Product.objects.filter(unit_price__range=(2,5))
   return render(request, 'hello.html', {'name': 'Mark', 'products': list(queryset)})
