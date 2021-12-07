from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product


def say_hello(request):
    product = Product.objects.get(id=1)
    
    return render(request, 'hello.html', {'name': 'Mark'})
