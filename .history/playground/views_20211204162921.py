from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product


def say_hello(request):
   queryset = Product.objects.filter(email__contains='.com')
   return render(request, 'hello.html', {'name': 'Mark', 'products': list(queryset)})
